---
title: Ext4 Forensics Inode Bitmaps
url: https://digitalinvestigator.blogspot.com/2026/02/ext4-forensics-inode-bitmaps.html
source: Instapaper: Unread
date: 2026-02-24
fetch_date: 2026-02-25T04:15:38.942898
---

# Ext4 Forensics Inode Bitmaps

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: Inode Bitmaps

Joseph Moronwi
February 21, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSBbNeggBT6R_fgVuR8OjIf6jry-ON5wrf0-yI48OlNjdRSzYIBub1GrehHHAuSxHCiVUO9Ea7vK8DanR6CWFu6GKdFLKrztOMQL6Oa1JiZngMXhZE_GC8aN2OgA93Hog2YFnktvjr6Gk8EClzasE9BLL-h3qAVTymLjudrHmd-jacdhK02FLo-qKb6w0/w651-h412/uninit.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSBbNeggBT6R_fgVuR8OjIf6jry-ON5wrf0-yI48OlNjdRSzYIBub1GrehHHAuSxHCiVUO9Ea7vK8DanR6CWFu6GKdFLKrztOMQL6Oa1JiZngMXhZE_GC8aN2OgA93Hog2YFnktvjr6Gk8EClzasE9BLL-h3qAVTymLjudrHmd-jacdhK02FLo-qKb6w0/s719/uninit.png)

An inode bitmap is a sequence of bits that tracks inode allocation status within a block group/flex group. A single bit is used to represent each inode, with
a value of 1 signifying that the inode is in use and a value of zero signifying that the inode is not
being used. In the case of the block bitmap, the least significant bit of byte 0 represents block 0 in the block
group’s data area. The most significant bit in byte 0 represents block 7 in the data area. In byte 1,
the least significant bit represents block 8, and so on. The process is the same in the inode bitmap
except that the first inode number is 1, rather than 0. Hence, the least significant bit in byte 0 of
the inode bitmap represents the allocation status of inode 1. The most significant bit represents the
allocation status of inode 8 and so on.

In `flex_bg`, inode bitmaps for several groups are co-located in the first group of the flex group. The inode bitmap occupies exactly one block (typically 4096 bytes = 32768 bits), allowing it to track up to 32768 inodes. Its location is stored in the group descriptor as follows:

* `bg_inode_bitmap_lo` (bytes offset 0x04 - 0x07) → lower 32 bits
* `bg_inode_bitmap_hi` (bytes offset 0x24-0x27; if 64-bit [`INCOMPAT_64BIT`] feature enabled) → upper 32 bits.

In ext4 (and earlier ext variants), each block group has:

* A fixed number of blocks per group (blocks\_per\_group, often matching the block size in bits—e.g., 32,768 for 4 KB blocks).
* A separate number of inodes per group (inodes\_per\_group), set at filesystem creation time via mkfs.ext4 (defaults commonly range from 8,192 to 16,384 or similar, depending on the inode ratio, like one inode per 16 KB of space).

The inode bitmap for each block group is always one block in size (e.g., 4,096 bytes on a 4 KB-block file system). It uses 1 bit per inode to track whether that inode is allocated or free. Since inodes\_per\_group is typically much smaller than blocks\_per\_group (e.g., 8,192 inodes need only 1,024 bytes of bitmap = 8,192 bits / 8), the inode bitmap rarely fills the entire block. This leaves slack space (unused bytes) at the end of each inode bitmap block. The usable slack space per inode bitmap block is approximately BlockSize−(inode\_per\_group/8) bytes. (The division by 8 converts inodes to bytes needed.) This slack exists repeatedly across all block groups (there are many block groups on any reasonably sized file system). The total hidden storage capacity is therefore roughly (BlockSize−(inode\_per\_group/8 ))\*BlockGroups bytes. This slack space is not checked or used by the kernel or standard file system tools for inode allocation tracking—it's just padding/unused. Writing arbitrary data there does not break file system consistency in a way that triggers errors during normal operation or most checks. Importantly, e2fsck (the standard ext4 file system checker) does not detect or complain about non-zero data in this inode bitmap slack space. It survives a forced check (e2fsck -f or similar) without flagging inconsistencies, because the tool only validates the actual bits corresponding to the valid inode range—it ignores or tolerates the trailing bytes.

When conducting ext4 file system forensics, one commonly overlooked structure is the `bg_flags` field of the block group descriptor. The bg\_flags field is a 16-bit value in each block group descriptor (at offset 0x12 in struct ext4\_group\_desc) that contains bitwise flags that describe the initialization and state of the block group's block bitmap, inode bitmap, and inode table. It is part of ext4's lazy initialization features, which optimize file system creation (e.g., via mkfs) by deferring full setup of bitmaps and tables until needed, reducing initial formatting time. Failing to interpret `bg_flags` correctly can lead to false deleted-file conclusions, misinterpretation of uninitialized inode tables, incorrect timeline reconstruction, and, ultimately, courtroom credibility issues.

The inode bitmap determines allocation status, where the value **0** denotes a free inode, and the value **1** denotes an allocated inode. But this allocation status is only valid if the group descriptor says the inode table and bitmap are initialized (i.e., `EXT4_BG_INODE_UNINIT` is NOT set). That is where the `bg_flags` becomes critical. These flags directly determine whether allocation metadata is forensically trustworthy. The bg\_flags field can have any combination of the following values.

* `EXT4_BG_INODE_UNINIT` (0x0001) → This is the most important flag for inode bitmap forensics. This implies that the inode bitmap and inode table are not initialized. The kernel treats the inode bitmap as all zeros (all inodes free), even if metadata might reside in the group. It has the following forensic implication:

+ The inode bitmap does NOT contain valid allocation data.
+ A '**0**' bit does NOT mean the inode was deleted. You might find historical data that predates the file system creation—but it's not evidence of file deletion.
+ Allocation status cannot be reconstructed reliably. You cannot trust any inode structures, extents, timestamps, etc., found there for allocation status or file recovery.
+ Thus, if EXT4\_BG\_INODE\_UNINIT is set, their bitmaps or inode tables have not yet been fully initialized. In such cases, the kernel treats the group as logically empty until it is first used. While allocation bitmaps reflect the logical file system state, the underlying inode table blocks may still contain residual data until background zeroing occurs. Forensic tools that rely solely on bitmap interpretation for quick scanning may overlook structures present in uninitialized tables. Therefore, investigators should directly parse inode tables and examine journal data (JBD2) to verify file system contents. In newly created or recently resized large file systems, deferred initialization may leave remnants of prior data in uninitialized groups, creating potential recovery opportunities.
+ If this flag is not set, the inode table is fully initialized and trustworthy. The inode bitmap can be read to identify free (or potentially deleted) inodes. The inode table is valid and can be parsed for i\_dtime, extents, etc.

* `EXT4_BG_BLOCK_UNINIT` (0x0002) → This is irrelevant to inodes. It implies that the data block bitmap is not initialized. The kernel assumes all data blocks in the group are free. It was covered in a [**prev...