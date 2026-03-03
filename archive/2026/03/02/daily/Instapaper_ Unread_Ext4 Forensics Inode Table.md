---
title: Ext4 Forensics Inode Table
url: https://digitalinvestigator.blogspot.com/2026/02/ext4-forensics-inode-table.html
source: Instapaper: Unread
date: 2026-03-02
fetch_date: 2026-03-03T04:13:50.373427
---

# Ext4 Forensics Inode Table

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: Inode Table

Joseph Moronwi
February 27, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEtRojvyeNqMufqfSuvrH2AYUEW-nltp6oudrvVYKDmkV3mBjMVhMuiI5_FZe_69F4ASY47J6GUfAEuVJEP6B6pF1JIUh1x7oYxe6JezUs4ys4WDTM8jzOS182UalvORKhRc6D-14b4PajRvBU79XskG3LQJN440Pc5GrOTAxMIKeP1s99QAewdw5MuaA/w654-h381/inode23-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEtRojvyeNqMufqfSuvrH2AYUEW-nltp6oudrvVYKDmkV3mBjMVhMuiI5_FZe_69F4ASY47J6GUfAEuVJEP6B6pF1JIUh1x7oYxe6JezUs4ys4WDTM8jzOS182UalvORKhRc6D-14b4PajRvBU79XskG3LQJN440Pc5GrOTAxMIKeP1s99QAewdw5MuaA/s724/inode23-1.png)

An inode (index node) is a fixed-size data structure that holds metadata about a file, directory, symlink, etc., but not the file name or the actual file content/data. Typical metadata includes file type and permissions, owner UID/GID, size (in bytes), timestamps (creation/change/modification/access), link count (for hard links), and pointers to data blocks (in ext4, usually via extents rather than direct/indirect data blocks).  The inode size can
be set to any power-of-two larger than 128 bytes size up
to the file system block size by using the mke2fs-I [inode
size] option at format time. Previous versions of the extended file system used a 128-byte-sized inode, which is already crowded with data
and has little space for new fields. In ext4, the default
inode structure size is 256 bytes. However, the first
128 bytes are backward compatible with previous versions of ext.

Inodes are numbered, starting with inode number 1, and stored in
the inode table of their respective block group. There is no inode 0. Inode numbers are analogous to MFT entry number in NTFS forensics. The ext4 inode table is a contiguous on-disk structure in the ext4 file system that stores all the inodes (index nodes) for a specific block group. It is a linear array of these inode structures—basically one long sequence of 256-byte (or whatever inode size) records. Each block group in an ext4 filesystem has its own inode table. The location (starting block) of the inode table for a block group is recorded in that group's entry in the Group Descriptor Table as follows:

* `bg_inode_table_lo` (bytes offset 0x08-0x0B) → Lower 32 bits.
* `bg_inode_table_hi` (bytes offset 0x28-0x2B if the 64-bit feature [`INCOMPAT_64BIT`] is enabled) → Upper 32 bits.

The number of inodes per group is set when the file system is created (controlled by the `-i / inode_ratio` option; common default is one inode per 16 KB–32 KB of space). The inode bitmap (one bit per inode) tells which inodes in the inode table are used/free. The inode table itself contains no headers or separators — it's purely a flat array of `struct ext4_inode`. To determine the block group of a respective inode, we use the formula given below:

```
block_group = (inode_number - 1) / sb.s_inodes_per_group
```

To calculate the index of the used inode within the block group, we use the following formula:

```
index = (inode_number - 1) % sb.s_inodes_per_group
```

Then you go to that group's inode table and read the entry at the calculated offset.

The inodes 1 to 10 are reserved for special functions. For example, inode 2 represents the root directory of the volume and inode 8 represents the file system journal, which was added in Ext3. In Ext4, for the sake of compatibility with prior versions, only a few changes to the inode structure have been implemented. In Ext4, some of the unused space of Ext3 has been used to introduce new attributes. The inode table entry is laid out in
struct struct ext4\_inode as seen in the table below. Note that the size of the structure is 160 bytes, though the standard inode size in ext4 is 256 bytes.  The extra 96 bytes are used to store extended attributes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Offset** | **Size (bytes)** | **Name** | **Description** |
| 0x00 | 0x2 | i \_mode | File mode (type and permissions). |
| 0x02 | 0x2 | i\_uid | Lower 16 bits of the owner id (UID). |
| 0x04 | 0x4 | i\_size\_lo | Lower 32 bits of the file size (in bytes). |
| 0x08 | 0x4 | i\_atime | Last access time, in seconds since the epoch. |
| 0x0C | 0x4 | i\_ctime | Last inode change time, in seconds since the epoch. |
| 0x10 | 0x4 | i\_mtime | Last data modification time, in seconds since the epoch. |
| 0x14 | 0x4 | i\_dtime | Deletion Time, in seconds since the epoch. |
| 0x18 | 0x2 | i\_gid | Lower 16 bits of group id (GID). |
| 0x1A | 0x2 | i\_links\_count | Number of hard links pointing to this file. With the DIR\_NLINK feature enabled, ext4 supports more than 64,998 subdirectories by setting this field to 1 to indicate that the number of hard links is not known. |
| 0x1C | 0x4 | i\_blocks\_lo | Lower 32 bits of 512-byte blocks this file uses. |
| 0x20 | 0x4 | i\_flags | Inode flags. Valid values include:     * 0x1 - This file   requires secure deletion. (Not implemented). * 0x2 - This file   should be preserved should un-deletion be desired. (Not implemented). * 0x4 - File is   compressed. (Not really implemented). * 0x8 - All writes to   the file must be synchronous. * 0x10 - File is   immutable. * 0x20 - File can only   be appended. * 0x40 - The dump (1)   utility should not dump this file. * 0x80 - Do not update   access time. * 0x100 - Dirty   compressed file. (Not used). * 0x200 - File has one   or more compressed clusters. (Not used). * 0x400 - Do not   compress file. (Not used). * 0x800 - Compression   error. (Not used). * 0x1000 - Directory   has hashed indexes. * 0x2000 - AFS magic   directory. * 0x4000 - File data   must always be written through the journal. * 0x8000 - File tail   should not be merged. * 0x10000 - All   directory entry data should be written synchronously. * 0x20000 - Top of   directory hierarchy. * 0x40000 - This is a   huge file. * 0x80000 - Inode uses   extents. * 0x200000 - Inode used   for a large extended attribute. * 0x400000 - This file   has blocks allocated past EOF. * 0x80000000 - Reserved   for ext4 library.     Aggregate Flags:     * 0x4BDFFF -   User-visible flags. * 0x4B80FF -   User-modifiable flags. |
| 0x24 | 0x4 | i\_osd1 | OS descriptor 1. Values include:      |  |  |  |  |  | | --- | --- | --- | --- | --- | | **Tag** | **Contents** | | | | | **Offset** | **Size** | **Name** | **Description** | | linux1 | 0x0 | 0x4 | l\_i\_version | Version | | hurd1 | 0x0 | 0x4 | h\_i\_translator | ?? | | masix1 | 0x0 | 0x4 | m\_i\_reserved | ?? | |
| 0x28 | 0x3C | i\_block[EXT4\_N\_BLOCKS] | Block map or Extent tree. |
| 0x64 | 0x4 | i\_generation | File version for NFS. |
| 0x68 | 0x4 | i\_file\_acl\_lo | Lower 32-bit address of extended attribute block. |
| 0x6C | 0x4 | i\_size\_high | Higher 32-bit address of file size |
| 0x70 | 0x4 | i\_obso\_faddr | (Obsolete) fragment address |
| 0x74 | 0xC | i\_osd2 | OS descriptor 2.      |  |  |  |  |  | | --- | --- | --- | --- | --- | | **Tag** | **Contents** | | | | | **Offset** | **Size** | **Name** | **Description** | | linux2 | 0x0         0x2                  0x4         0x6      0x8 | 0x2   ...