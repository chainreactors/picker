---
title: Ext4 Forensics The Superblock
url: https://digitalinvestigator.blogspot.com/2026/01/ext4-forensics-superblock.html
source: Instapaper: Unread
date: 2026-02-08
fetch_date: 2026-02-09T04:18:48.735207
---

# Ext4 Forensics The Superblock

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: The Superblock

Joseph Moronwi
January 29, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgagZmOm-iBZgETnahK6pDFDucoxaDaxmtoCwZ6SdR0Dn84vPaAkI7vLn90a8mPewBKLAqr3ultEAksDjQz47Kdc6Ese84IySFLvww_qZPX4E2oR9MSPmfrTEmStoJhestllpR1U2exGNFGTP0yzl5VEfmWoH8NCxkVRe2lhgzNC7KELx2t7Vd8bv-mcgE/w654-h408/superblock.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgagZmOm-iBZgETnahK6pDFDucoxaDaxmtoCwZ6SdR0Dn84vPaAkI7vLn90a8mPewBKLAqr3ultEAksDjQz47Kdc6Ese84IySFLvww_qZPX4E2oR9MSPmfrTEmStoJhestllpR1U2exGNFGTP0yzl5VEfmWoH8NCxkVRe2lhgzNC7KELx2t7Vd8bv-mcgE/s717/superblock.png)

In the first block of the filesystem, the first 1024 bytes are left for the installation of boot sectors and other oddities. And the next 1024 bytes are used for the superblock (`struct ext4_super_block`). The remaining 2048 bytes in the first block remain unused (a block has a size of 4096 bytes).

# The SuperBlock

The superblock itself is one of the most important structures in ext4 and the beginning of any analysis of the file system. A superblock describes the filesystem and tells the operating system where to find various elements (inodes, etc.). It is the master metadata structure for the ext4 filesystem, analogous to the BIOS parameter block in the FAT and NTFS file systems in purpose. It records various information about the layout, size, and enabled features of the file system.  Originally, the superblock and group
descriptors were replicated in every block group, with those
located in block group 0 designated as the primary copies.
This is no longer common practice due to the sparse feature option. This option only replicates the file system superblock and group
descriptors in a fraction of the block groups.  The sparse feature flag (`sparse_super`) is set by default and will store redundant copies of superblocks and group descriptors in block group 0, and then in block group 3x, 5x, and 7x. Another feature flag that organizes superblocks is sparse\_super2. If set, the file system will only contain two superblock backups. The backup superblocks and backup group descriptors are never updated by the kernel. They will be updated only if any fundamental parameters of the filesystem are changed, for example, by resizing the filesystem.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTNC-wsO9FxMMipPCm0-v9QZJy6uenpd7PcBD0eWCc2nZ3dBLfwJ7B_D_ebTAHVyjA4uiYIL9LO-oyF8XxOacXcdykBAgF6QURNapdQXtubfY32jbsNuwlgj0fDfnnW-0daX95SApqYQxAiTNBvjJCsrcMiCaQfDYPcJ2jezMv0u86mTJiV-Xiw2I2gHc/w664-h423/sb_struct_1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTNC-wsO9FxMMipPCm0-v9QZJy6uenpd7PcBD0eWCc2nZ3dBLfwJ7B_D_ebTAHVyjA4uiYIL9LO-oyF8XxOacXcdykBAgF6QURNapdQXtubfY32jbsNuwlgj0fDfnnW-0daX95SApqYQxAiTNBvjJCsrcMiCaQfDYPcJ2jezMv0u86mTJiV-Xiw2I2gHc/s1585/sb_struct_1.jpg) |
| Figure 1: Byte-level view of an ext4 Superblock |

The table below explains the data structure of the ext4 file system superblock.

|  |  |  |  |
| --- | --- | --- | --- |
| **Offset** | **Size (bytes)** | **Name** | **Description** |
| 0x00 | 4 | s\_inodes\_count | The total number of inodes in the file system. |
| 0x04 | 4 | s\_blocks\_count\_lo | The total number of blocks in the file system. |
| 0x08 | 4 | s\_r\_blocks\_count\_lo | Number of blocks reserved to prevent file system from filling up. |
| 0x0C | 4 | s\_free\_blocks\_count\_lo | Number of unallocated blocks. |
| 0x10 | 4 | s\_free\_inodes\_count | Number of unallocated inodes. |
| 0x14 | 4 | s\_first\_data\_block | Block where block group 0 starts. |
| 0x18 | 4 | s\_log\_block\_size | Block size (saved as the number of places to shift 1,024 to the left). This is given by the formula 2(10+`s_log_block_size`). |
| 0x1C | 4 | s\_log\_cluster\_size | Allocation cluster size. |
| 0x20 | 4 | s\_blocks\_per\_group | Number of blocks in each block group. |
| 0x24 | 4 | s\_clusters\_per\_group | Clusters per group. |
| 0x28 | 4 | s\_inodes\_per\_group | The number of inodes in each block group. |
| 0x2C | 4 | s\_mtime | The UNIX time at which the file system was last mounted. |
| 0x30 | 4 | s\_wtime | The UNIX time at which the file system was last written. |
| 0x34 | 2 | s\_mnt\_count | The number of mounts since the last file system check (**fsck**). |
| 0x36 | 2 | s\_max\_mnt\_count | Number of mounts beyond which a fsck is needed. |
| 0x38 | 2 | s\_magic | Magic signature, 0xEF53. |
| 0x3A | 2 | s\_state | The current state of the file system. Values: 0x0001 → Clean; 0x0002 → Errors; and 0x0004 → Orphan inodes are being recovered. |
| 0x3C | 2 | s\_errors | Error handling method. Values: 1 → Continue; 2 → Remount read-only; and 3 → Panic. |
| 0x3E | 2 | s\_minor\_rev\_level | Minor revision level of the file system. |
| 0x40 | 4 | s\_lastcheck | UNIX time representing the last file system check. |
| 0x44 | 4 | s\_checkinterval | Maximum time between checks, in seconds. |
| 0x48 | 4 | s\_creator\_os | Identifier of the OS that created the file system. Values include: 0 → Linux; 1 → GNU Hurd; 2 → Masix; 3 → Free BSD; and 4 → Lites. |
| 0x4C | 4 | s\_rev\_level | Major revision level of the file system. Values include:      * 0 → Original   version * 1 → Dynamic version.   A dynamic revision refers to the modern, flexible format of the Linux file system that allows for advanced features and backward compatibility with ext2/ext3. Unlike the old, fixed-format "rev0" file systems, the dynamic revision allows for the dynamic allocation of inodes and file system features to be toggled on or off. It allows for features to be added, such as 64-bit support, extents, and flexible block groups (flex\_bg), which improve performance and scalability. |
| 0x50 | 2 | s\_def\_resuid | The UID that can use reserved blocks (default is 0, i.e., root). |
| 0x52 | 2 | s\_def\_resgid | The GID that can use reserved blocks (default is 0). |
| 0x54 | 4 | s\_first\_ino | First non-reserved inode in file system. |
| 0x58 | 2 | s\_inode\_size | Size of inode structure, in bytes. |
| 0x5A | 2 | s\_block\_group\_nr | Block group that this superblock is a part of (if backup copy) |
| 0x5C | 4 | s\_feature\_compat | Compatible feature flags. Kernel can still mount with read/write support even if it does not understand one of the flags in this 32-bit field. The compatible features flag can have the following values:     * 0x1 →  Pre-allocate directory blocks to reduce fragmentation (COMPAT\_DIR\_PREALLOC). * 0x2 → AFS server inodes exist (COMPAT\_IMAGIC\_INODES). * 0x4 → File system has a journal (COMPAT\_HAS\_JOURNAL). * 0x8 → Supports extended attributes (COMPAT\_EXT\_ATTR). * 0x10 → Has reserved GDT blocks for file system expansion (COMPAT\_RESIZE\_INODE). * 0x20 → Directories use hash index (COMPAT\_DIR\_INDEX). * 0x40 → Support for uninitialized block groups. Not in Linux kernel (COMPAT\_LAZY\_BG). * 0x80 → Exclude inode . Not used. (COMPAT\_EXCLUDE\_INODE). * 0x100 → Exclude bitmap . Not used (COMPAT\_EXCLUDE\_BITMAP). * 0x200 → Sparse Super Block, v2. If set, superblock backup\...