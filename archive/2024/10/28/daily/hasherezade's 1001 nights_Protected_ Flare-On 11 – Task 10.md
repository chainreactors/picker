---
title: Protected: Flare-On 11 – Task 10
url: https://hshrzd.wordpress.com/2024/10/27/flare-on-11-task-10/
source: hasherezade's 1001 nights
date: 2024-10-28
fetch_date: 2025-10-06T18:49:03.394197
---

# Protected: Flare-On 11 – Task 10

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/cat-emerging-from-matrix-1.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Magniber ransomware analysis: Tiny Tracer in action](https://hshrzd.wordpress.com/2023/03/30/magniber-ransomware-analysis/)

[Flare-On 11 – Task 9 →](https://hshrzd.wordpress.com/2024/10/29/flareon-11-task-9/)

## [Flare-On 11 – Task 10](https://hshrzd.wordpress.com/2024/10/27/flare-on-11-task-10/)

Posted on [October 27, 2024](https://hshrzd.wordpress.com/2024/10/27/flare-on-11-task-10/ "5:34 pm") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*[Flare-On](https://flare-on.com/) is an annual CTF run by [Mandiant Flare Team](https://cloud.google.com/blog/topics/threat-intelligence/flareon-11-challenge-solutions). In this series of writeups I present solutions to some of my favorite tasks from this year. All the sourcecodes are available on my Github, in dedicated repository: [flareon2024](https://github.com/hasherezade/flareon2024)*.

The recent, 11-th edition, had 10 tasks. The final one was named “Catbert Ransomware”:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/task10_info.png?w=723)

We are provided with two files: `bios.bin` containing firmware, and `disk.img` containing the disk. We can run it with the help of QEMU:

```
qemu-system-x86_64 -drive file=disk.img,format=raw -bios bios.bin
```

The firmware boots and we are prompted with the following message:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/message.png?w=631)

By the command:

```
fs0:
```

We can enter to the mounted `disk.img`. Listing its main directory shows 4 files: three cat memes, encrypted, with a .c4tb extension, and an EFI binary, also encrypted but with a different algorithm.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/files.png?w=481)

The initial message says that we are supposed to decrypt the .c4tb files, using a decryption tool that is available within this shell. Let’s first find this utility. Using the command `help` we can list all available commands. By [Page Up] and [Page Down] we can roll the screen back and forth, and see the initial commands. Among them, there is one especially interesting:

```
decrypt_file  - Decrypts a user chosen .c4tb file from a mounted storage, given a decryption key.
```

This tool can decrypt our files, but it is not gonna be that easy. First, we need to find an appropriate password for each of them. This requires diving deeper into the code implementing the decryption process.

## Finding the shell binary

At this point we are sure that the binary we are looking for is somewhere in the bios.bin. I started by extracting its content by binwalk:

```
$ binwalk bios.bin -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             UEFI PI Firmware Volume, volume size: 540672, header size: 0, revision: 0, Variable Storage, GUID: FFF12B8D-7696-4C8B-85A9-2747075B4F50
540672        0x84000         UEFI PI Firmware Volume, volume size: 3440640, header size: 96, revision: 0, EFI Firmware File System v2, GUID: 8C8CE578-8A3D-4F1C-3599-896185C32DD3
540840        0x840A8         LZMA compressed data, properties: 0x5D, dictionary size: 16777216 bytes, uncompressed size: 16122000 bytes
3981312       0x3CC000        UEFI PI Firmware Volume, volume size: 212992, header size: 96, revision: 0, EFI Firmware File System v2, GUID: 8C8CE578-8A3D-4F1C-3599-896185C32DD3
3981460       0x3CC094        Microsoft executable, portable (PE)
```

Binwalk created a directory with extracted contents:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/bios_extracted.png?w=322)

If we open the first binary (`840A8`) in hexeditior, we can see that it contains plenty of different PE files. Many of them have strings referencing the the project:
<https://github.com/tianocore/edk2/> and suggesting that the challenge has been created upon this base. Most of those binaries are not relevant to the main problem of the task.

Let’s try to pinpoint the exact module that will be responsible for processing the .c4tb files. A command that may be of help is the hexeditor available from within the shell:

```
hexedit       - Provides a full screen hex editor for files, block devices, or memory.
```

With its help we can see that every .c4tb binary starts with the magic
“C4TB”. We can guess that the binary responsible for the decryption will start validating the input by checking for the presence of this marker. Let’s see if any of the binaries in the decompressed bios references this magic number:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/marker_found.png?w=618)

The marker was found. We can assume that it is inside the PE that processes the .c4tb files. Let’s find the beginning of this PE, by searching for the MZ signature backwards from the marker.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/pe_found.png?w=619)

Having the offset, I just carved out the relevant PE and opened it in IDA. The PDB confirms that it is the shell executable.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/pdb_path.png?w=777)

By following where the previously found marker is referenced, I pinpointed the routine responsible for password verification.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/marker_check.png?w=547)

The same function contains other familiar strings that were displayed on the attempt of decrypting a file with `decrypt_file` utility. This confirms that it is indeed the part of code we were looking for:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/marker_check_disasm.png?w=878)

Following the flow of the function, we an see the routine that seems to be used for password verification:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/to_pass_check.png?w=546)

This routine turns out to be interesting. It consists of the main loop, that parses given arguments, and executes operations depending on the content of the first argument. It reminds of a small VM, processing some bytecode.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/arithmetic.png?w=640)

And where is this bytecode located? It turns out that it is in the `.c4tb` file itself! The code just before the verification function parses the header at the beginning of the provided file:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/file_buf.png?w=522)

After the magic (C4TB) marker, there are 3 other DWORDs. The whole structure can be summarized as:

```
struct c4tb_hdr{
    DWORD magic;
    DWORD dataSize;
    DWORD codeOffset;
    DWORD codeSize;
};
```

It turns out the relevant bytecode is appended at the end of the file, after the block of encrypted data. It is pointed by the offset stored in the header. The bytecode itself implements the password verification program.

The password is always 16 characters long. It is filled in the bytecode, each character at predefined offset.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/10/fill_pass-1.png?w=535)

## Running the verification function

At this point I decided that it will be be...