---
title: 512 bytes at a time: reconstructing IBM i save-file checksums
url: https://blog.silentsignal.eu/2026/10/06/512-bytes-at-a-time-reconstructing-IBM-i-save-file-checksums/
source: Silent Signal Techblog
date: 2026-10-12
fetch_date: 2026-10-13T08:38:44.586077
---

# 512 bytes at a time: reconstructing IBM i save-file checksums

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![512 bytes at a time: reconstructing IBM i save-file checksums](/img/gibson.jpg)

# 512 bytes at a time: reconstructing IBM i save-file checksums

[pz](/authors/pz.html) 2026-10-12

## Intro

What exactly must be recalculated when bytes inside an IBM i save file are modified?

IBM i save files, usually called SAVFs, use two container-consistency checksum mechanisms. Every 512-byte payload has a 16-byte trailer, and the logical stream also carries a 16-byte global checksum in its final payload. I wanted to understand both mechanisms well enough to reproduce them, modify a SAVF, and repair only the bytes that depended on my change.

For the reconstruction, I used a small IBM-generated SAVF and the publicly distributed jSAVF reader, whose JAR I decompiled. I reimplemented both algorithms in Python and reproduced every stored checksum in the original file. A second file contained three changed payload bytes and a stale global checksum. Repairing that container changed only the global-checksum field and the final record trailer. I also found the global algorithm’s table and adjacent constants in IBM i Licensed Internal Code (LIC) installation media.

Finally, I used the reconstructed format to remove one complete object from a two-object SAVF. A copy with valid record trailers but a stale global checksum was rejected during import. After I regenerated the global checksum and final trailer, IBM i accepted the shorter SAVF, `DSPSAVF` showed only the retained object, and that unchanged object restored successfully.

These values provide internal consistency checks for the SAVF container, but they are deterministic, unkeyed, and recomputable. They do not authenticate the source or prevent somebody from modifying a file and recalculating its checksums. IBM i has separate mechanisms for SAVF signatures and for validating the objects stored inside the container. I will return to that boundary after the reversing work.

## Building a SAVF I could modify

I wanted a small SAVF whose contents I controlled, so I created one containing a disposable program named `USERB1/CALLAES`. I disabled data compression because fixed, uncompressed payloads are much easier to compare byte for byte:

```
CRTSAVF FILE(USERB1/SAVE1)
SAVOBJ OBJ(CALLAES) LIB(USERB1) OBJTYPE(*PGM) DEV(*SAVF) SAVF(USERB1/SAVE1) DTACPR(*NO)
```

`CRTSAVF` creates the save-file object. [`SAVOBJ`](https://www.ibm.com/docs/en/i/7.5.0?topic=ssw_ibm_i_75/cl/savobj.html) saves the program into it, and `DTACPR(*NO)` keeps the data uncompressed. It does not disable either checksum layer.

I copied the SAVF directly from `/QSYS.LIB` over SCP:

```
scp userb1@ibmi.example:/QSYS.LIB/USERB1.LIB/SAVE1.FILE .
```

The `/QSYS.LIB/USERB1.LIB/SAVE1.FILE` path is the Integrated File System view of the SAVF object. This transfer gives me a binary file that I can inspect byte for byte.

The resulting `SAVE1.FILE` is 84,480 bytes long.

## What a SAVF looks like

I did not have to discover the outer record format from scratch. A [January 2001 MI400 post](https://archive.midrange.com/mi400/200101/msg00072.html) describes RISC SAVFs as 528-byte records: 512 data bytes, a four-byte binary record number, and a 12-byte checksum. A [2007 midrange.com discussion](https://archive.midrange.com/midrange-l/200710/msg01516.html) also describes checksum information in each 528-byte record.

That layout fits my test file exactly:

```
84,480 bytes = 160 * 528
```

Each physical record contains a 512-byte payload followed by a 16-byte trailer:

```
physical file:  | 512-byte payload | 16-byte trailer | 512-byte payload | ...
logical stream: |         512 payload bytes         |         512 payload bytes
```

Removing the trailers leaves an 81,920-byte logical stream:

```
81,920 bytes = 160 * 512
```

Once those trailers are removed, an offset inside the logical SAVF stream no longer matches the corresponding raw-file offset. I therefore use two coordinate systems:

* a **physical offset** addresses the transferred file, including the trailers;
* a **logical offset** addresses the concatenated 512-byte payloads.

The conversion is:

```
def logical_to_physical(offset: int) -> int:
    return (offset // 512) * 528 + (offset % 512)
```

A modified copy named `SAVE2.FILE` appears later in the experiment. Its three payload differences from `SAVE1.FILE` show why this distinction matters:

| Logical offset | Record index | Offset in payload | Physical offset |
| --- | --- | --- | --- |
| `0x6D50` | 54 | `0x150` | `0x70B0` |
| `0x6D52` | 54 | `0x152` | `0x70B2` |
| `0x6D53` | 54 | `0x153` | `0x70B3` |

Here, `index 54` means the zero-based record index. The trailer stores a one-based sequence, so the same unit is **record #55**. Hex editors and `cmp` use physical offsets; structures inside the SAVF use logical offsets.

IBM also documents part of this outer layer. The [`CRTSAVF` documentation](https://www.ibm.com/docs/en/i/7.5.0?topic=ssw_ibm_i_75/cl/crtsavf.html) says that retrieved SAVF records carry sequencing checksum information. IBM i validates it when records are inserted and rejects changed or out-of-sequence records. That documentation covers per-record insertion checks, not the global checksum discussed later.

I did not run a separate live negative control for a corrupted record trailer. Record-level enforcement is documented by IBM; the controlled negative experiment later in this article isolates the second mechanism, the global checksum.

Other public work already covered more than the outer layout. The initial 9 August 2026 revision of the [Try-AS/400 SAVF page](https://try-as400.pocnet.net/wiki/File_Formats%3ASAVF), preserved as revision `1781` in its [page history](https://try-as400.pocnet.net/index.php?action=history&title=File_Formats%3ASAVF), documented the per-record folding, timestamp XOR, global overlay, and backup at logical `0x40`. It also documented the header-length and record-count fields, the item marker, name, catalogue reference, stored and total lengths, and the QSYS catalogue’s object count and descriptor layout used by the removal experiment below. The page warns that some material was generated or amended by AI and has not been checked, so I credit it as prior public documentation and validate the fields independently against my fixture and jSAVF.

This article focuses on the complete global state-machine order, tests with nonzero backups, the matching LIC data, deterministic reconstruction and repair, public test vectors, and controlled IBM i behavior.

## Reconstructing the per-record checksum

Instead of guessing standard checksum families, I looked for an existing SAVF reader. [jSAVF](https://www.anerty.net/software/file/jSAVF/?lang=en) already implemented the format, and its author credits information from the `archive.midrange.com` community, especially for IBM’s two proprietary checksum algorithms. I decompiled the distributed JAR and used its `ChunkChecker` logic as the starting point for the per-record algorithm.

The first four bytes of each 16-byte trailer are the one-based record sequence. The remaining 12 bytes are the transformed checksum value. The values are easy to see in `SAVE1.FILE`:

```
index 0   / record #1:   00000001 8f40b6a68e88a98ea91e2d60
index 1   / record #2:   00000002 af2012d24b4b7f2000004000
index 159 / record #160: 000000a0 afc501282b18f73c5c308e69
```

The decompiled code also uses the first eight bytes of the SAVF when building every record checksum. In `SAVE1.FILE`, those bytes are:

```
af2012d24b4b7f20
```

jSAVF treats this value as the SAVF timestamp and mixes it into the checksum after the reduction passes.

The main operation in the decompiled code is a shifted byte-array addition. jSAVF calls it `chkAdd`; the Python reconstruction below uses the name `chk_add`. The destination is one byte longer than the source:

```
def chk_add...