---
title: Ext4 Forensics Group Descriptors
url: https://digitalinvestigator.blogspot.com/2026/02/ext4-forensics-group-descriptors.html
source: Instapaper: Unread
date: 2026-02-08
fetch_date: 2026-02-09T04:18:49.532650
---

# Ext4 Forensics Group Descriptors

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: Group Descriptors

Joseph Moronwi
February 06, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis0-BIMbKpDNuUcZ6lX-Oez6cErw6-GDkRy_5DQ1zW82R0Txor73kJOUwViDdQ4fGXvV3vqYuwxKwzd6lhh0Cu_jQ-mgesNGJewvFR2RCQkZhzRfKpaZ3DBGzRRofIvAm7997bfi_Vka85fdYMG_Re6jYYPSj8UqbO3UVaSVhD85nvpRJsGsxn8kr_UqY/w654-h442/GDT.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis0-BIMbKpDNuUcZ6lX-Oez6cErw6-GDkRy_5DQ1zW82R0Txor73kJOUwViDdQ4fGXvV3vqYuwxKwzd6lhh0Cu_jQ-mgesNGJewvFR2RCQkZhzRfKpaZ3DBGzRRofIvAm7997bfi_Vka85fdYMG_Re6jYYPSj8UqbO3UVaSVhD85nvpRJsGsxn8kr_UqY/s672/GDT.png)

The smallest storage unit addressable by a disk is a **sector**, which has traditionally been 512 bytes in size, although modern disks may use 4096-byte sectors. However, to improve I/O performance, file systems typically operate on larger units composed of multiple sectors. ExtX file systems will normally perform read/writes in 4KB chunks called **blocks**. Blocks are composed of sectors (usually 8 sectors in extended file systems).

To the reader who is familiar with the FAT and NTFS file systems, a block in Unix/Linux is roughly equivalent to a cluster in DOS or Windows. On modern Linux file systems, the standard 4 KB block is the smallest allocation unit for a file. If the file is smaller than 4 KB, the remainder of the block is unused or "slack" space.

When writing a large file that spans multiple blocks, the file system will try to allocate consecutive blocks where possible. This will increase the read efficiency because the file system can read ahead in large swaths. But this tendency also turns out to be useful when an examiner is trying to recover data. If you locate a suspicious string in the middle of a deleted block of data, you may be able to recover the entire deleted file by capturing the blocks immediately before and after the "interesting" block.

Blocks are further organized into structures known as block groups. A block group is a contiguous range of blocks that also contains related metadata, such as inodes and bitmaps. It is a logical grouping of contiguous blocks, whose size is equal to the number of bits in
one block. For example, in a filesystem with a block size of 4096 bytes, a block group will have 4096\*8
= 32768 blocks. Block groups are designed to improve file system performance by preserving locality—wherever possible, the file system attempts to allocate a file’s inode and data blocks within the same block group. This reduces fragmentation and, on mechanical disks, minimizes disk head movement during read and write operations. An ext4 partition is divided into block groups.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzRBuLYup_OeBWR03aIAHB__oZNgQJhgNfNgjGI9iZlpK4LM-nyIKqvVT1YpUp_MarZLD20ZQCYavsoIsHOnsYRrSyILofqb0S_Zz2keC45H-Um8-1j93CNT8P0_x7TYD4DIEgvleOlC-7KVLcOEWnTdU56JAZAqVkrhPC_qkII8xVuWznDb0KH_ImBvw/w660-h359/ext4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzRBuLYup_OeBWR03aIAHB__oZNgQJhgNfNgjGI9iZlpK4LM-nyIKqvVT1YpUp_MarZLD20ZQCYavsoIsHOnsYRrSyILofqb0S_Zz2keC45H-Um8-1j93CNT8P0_x7TYD4DIEgvleOlC-7KVLcOEWnTdU56JAZAqVkrhPC_qkII8xVuWznDb0KH_ImBvw/s866/ext4.png) |
| Figure 1: Layout of the ext4 file system |

# Group Descriptors

Each block group is represented by its block group descriptor. A group descriptor contains meta information about a particular block group, such as the range of inodes in the group, the blocks included in the group, the offset of key blocks into the group, the locations of the block bitmap, inode bitmap, and the inode table.

To find the group descriptor, we need to know the block size, and this is calculated using the formula 2^(10+`s_log_block_size`), where `s_log_block_size` is given in the superblock. We can find the group descriptor in the block following the superblock. To find the group descriptor, we move 4096 bytes (one block) forward from the start of the superblock, from byte offset 0, not from 1024. Using the superblock and group descriptors, we can
locate all of the data structures that are used by files and directories.

The Group Descriptor Table (GDT) is a collection of block group descriptors representing every block group within the file system. We can call the GDT a table of
block group descriptors of all block groups of the file system. The ext4 filesystem extends the group descriptor size from 32 to 64 bytes when the 64-bit feature  (`INCOMPAT_64BIT`) is enabled. To support future expansion of the file system, `mke2fs` allocates several group descriptor growth blocks after the group descriptor table.  The number of reserved group descriptor table blocks for future file system expansion is stored in the superblock if the feature flag `COMPAT_RESIZE_INODE` is set. The size of the block group descriptor
table can be calculated from the superblock. To do this, it is necessary to determine the
block size, the number of blocks per group, and the total number of blocks. Traditional block group descriptors (ext2 and ext3) contain a single 32-byte entry for each block group in the file system. Ext4 requires more information. In particular, ext4 requires 64-bit addressing, meaning that ext4 block group descriptor entries require 64 bytes of storage. Using this information, it is possible to determine
how many blocks are needed for the block group descriptor table. The first 0x12 bytes of the ext4 block group descriptor structure are identical to those in earlier versions of ext. The additional information is added beyond this point. This includes some extra count information, checksums, and the location of the snapshot exclusion block (which will exclude certain
files/directories from backups/snapshots in ext4).

Although the table is designed to store descriptors efficiently, slack space may still exist at the end of the GDT. This unused area, along with any backup copies of the GDT and reserved GDT, should be examined during analysis, as it may be abused to conceal data. Unused reserved GDT blocks can also be used to hide data. This results in `s_reserved_gdt_blocks` ∗
block size ∗ (n special block groups) usable bytes, where n special block groups are the block
groups whose number is a power of 3, 5, or 7. Each block group descriptor in the EXT4 file system has 4 bytes, which are used as padding to make
the group descriptor 64 bytes long if the 64-bit feature  (`INCOMPAT_64BIT`) is enabled. This padding space can be used to hide data and therefore
results in 4 ∗ BlockGroups bytes to hide data.

Additional copies of the GDT are stored alongside backup superblocks, following the same placement rules. The sparse feature flag (`sparse_super`) is set by default and will store redundant copies of superblocks, group descriptor tables, and group descriptor
growth blocks in block group 0 and then in block groups 3x, 5x, and 7x. Another feature flag that organizes superblocks is `sparse_super2`. If set, the file system will only contain two copies of the superblock, group descriptor table, and group de...