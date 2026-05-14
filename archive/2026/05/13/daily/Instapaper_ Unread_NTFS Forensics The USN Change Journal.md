---
title: NTFS Forensics The USN Change Journal
url: https://digitalinvestigator.blogspot.com/2026/05/ntfs-forensics-usn-change-journal.html
source: Instapaper: Unread
date: 2026-05-13
fetch_date: 2026-05-14T05:47:18.407775
---

# NTFS Forensics The USN Change Journal

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# NTFS Forensics: The USN Change Journal

Joseph Moronwi
May 10, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg5_ci36vvdLY8WrHjQWwGFCHouIuNpq4wCbIXEFCgGuDfxUI0iBt4GXTfagIoKdiqezBDa1mjJimCl2Tzbo08rjgZpPkFM7-GuKDhzreLICD219d79mLCKnzYc9t0EnpZw1vy2r1aYi7lDuf-S4ePZ-vpOHve2x7OqjkzmA5-elQVA811xb4TgnsrDvk/w657-h312/$J-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg5_ci36vvdLY8WrHjQWwGFCHouIuNpq4wCbIXEFCgGuDfxUI0iBt4GXTfagIoKdiqezBDa1mjJimCl2Tzbo08rjgZpPkFM7-GuKDhzreLICD219d79mLCKnzYc9t0EnpZw1vy2r1aYi7lDuf-S4ePZ-vpOHve2x7OqjkzmA5-elQVA811xb4TgnsrDvk/s732/%24J-1.png)

The Update Sequence Number (USN) Journal was first introduced with NTFS in Windows 2000. However, it remained largely inactive by default until Windows Vista, when Microsoft began enabling it automatically on most volumes. Since then, it has stayed enabled by default in all newer Windows versions. Unlike the NTFS $LogFile, which is poorly documented, Microsoft has provided reasonably good documentation for the USN Journal and its associated APIs. It resides as a system metafile in the hidden $Extend directory. The actual journal data is stored in the $J alternate data stream, so the full internal path is typically expressed as `\$Extend\$UsnJrnl:$J`. Another small ADS, $Max, contains metadata about the journal itself, such as its maximum size.

The USN Journal records in the $UsnJrnl:$J data stream are of variable length and are stored consecutively. The $J stream is implemented as a sparse file. It uses two important parameters defined in the USN Journal metadata ($Max stream):

* MaximumSize — the target maximum amount of journal data.
* AllocationDelta — the size (in bytes) by which the journal grows or shrinks.

**Record allocation behavior**:

* New USN records are appended to the end of the active data area.

* When the amount of data exceeds MaximumSize, the journal is allowed to temporarily grow by up to one AllocationDelta.

* During the next NTFS checkpoint, NTFS deallocates space from the front of the journal in chunks of AllocationDelta. These deallocated areas become sparse (they logically contain zeros when read, but occupy no physical disk space).

As a result, the logical size of the $J attribute can appear very large, while the actual allocated data on disk remains roughly constant — typically bounded near the configured MaximumSize plus one AllocationDelta. On modern Windows client systems, the default MaximumSize is usually 0x2000000 (32 MB). Servers and domain controllers often use significantly larger values (e.g., 512 MB or more).

In digital forensics, the USN Journal is highly valuable because it logs detailed file system changes, including file creations, modifications, renames, and deletions. This makes it possible to reconstruct timelines of file activity, recover evidence of deleted files, and detect signs of anti-forensic techniques (such as timestomping or mass file wiping). Even sophisticated attackers or malware that attempt to cover their tracks often leave detectable footprints in the journal, as entries can persist until the fixed-size journal wraps around and overwrites older records.

The USN Journal consists of a sequence of USN records. Each record provides a high-level description of changes made to a file or directory (such as creation, deletion, rename, or data modification), which is significantly more abstract than the low-level transaction records found in the NTFS $LogFile. Microsoft defines three main record versions: USN\_RECORD\_V2, USN\_RECORD\_V3, and USN\_RECORD\_V4. The differences between V2 and V3 are relatively minor (V3 adds support for 128-bit file identifiers). USN\_RECORD\_V4 is used specifically for range tracking of modified byte extents in large files and must be explicitly enabled — it is not used for standard change journaling. While older documentation suggested V3 would appear starting with Windows 8 / Server 2012, in practice, many modern Windows 10 and 11 systems still primarily generate V2 or V3 records depending on the volume and configuration.

Unlike a traditional circular log, the USN Journal is not strictly circular in its on-disk allocation. When it needs more space, new clusters are allocated. Old clusters are eventually deallocated during NTFS checkpoints. Because these deallocated blocks may remain intact on disk until they are reused, forensic analysts can often carve older USN records from unallocated space, sometimes recovering significant historical file activity even after the active journal has moved on.

The USN Journal ($UsnJrnl) and the NTFS $LogFile complement each other well. While the USN Journal records high-level file system events (such as creation, deletion, renaming, or modification of files and directories), the $LogFile captures low-level metadata transactions. Combining the two provides a much clearer picture of the operations performed on a file. Furthermore, the USN Journal forms part of what is often called the NTFS Trinity (sometimes referred to as TriForce in forensic literature). This combination consists of three key artifacts: the Master File Table (MFT), the $LogFile, and the USN Journal. When analyzed together, these three NTFS structures enable investigators to reconstruct detailed timelines and gain deep insight into file system activity on a Windows system, including operations that are no longer visible in the active MFT.

The tables below show the data structure for the $UsnJrnl:$J records: USN\_RECORD v2 (Windows 7 and below, Windows Server 2008 R2 and below) and USN\_RECORD v3 (Windows 8+, Windows Server 2012+).

|  |  |  |
| --- | --- | --- |
| **Offset** | **Size** | **Description** |
| 0x00 | DWORD | Size of journal entry |
| 0x04 | WORD | Major Version |
| 0x06 | WORD | Minor Version |
| 0x08 | LONGLONG | MFT Reference of the file that caused this entry |
| 0x10 | LONGLONG | Parent MFT Reference for the file that caused this entry |
| 0x18 | LONGLONG | USN for entry |
| 0x20 | LONGLONG | Timestamp |
| 0x28 | DWORD | Reason code (flags for type of change) (to be discussed below) |
| 0x2C | DWORD | Source information |
| 0x30 | DWORD | Security ID (SID) |
| 0x34 | DWORD | File Attributes |
| 0x38 | WORD | Size of file name (in bytes) |
| 0x3A | WORD | Offset to file name |
| 0x3C | Variable | File name |
| V+0x3C | Padding | Padding (align to 8bytes) |

The USN\_RECORD version is determined by the OS that created the journal, not the volume format alone. A disk created on Windows 7 (v2) and later mounted on Windows 10 may retain v2 records until the journal is recreated. Deleting and recreating the journal (`fsutil usn deletejournal /d`) on a newer OS forces v3 records.

|  |  |  |
| --- | --- | --- |
| **Offset** | **Size** | **Description** |
| 0x00 | DWORD | Size of journal entry |
| 0x04 | WORD | Major Version |
| 0x06 | WORD | Minor Version |
| 0x08 | FILE\_ID\_128 | MFT Reference of the file that caused this entry |
| 0x18 | FILE\_ID\_128 | Parent MFT Reference for the file that caused this ent...