---
title: Ext4 Forensics Block Bitmaps
url: https://digitalinvestigator.blogspot.com/2026/02/ext4-forensics-block-bitmaps.html
source: Instapaper: Unread
date: 2026-02-18
fetch_date: 2026-02-19T04:22:12.098099
---

# Ext4 Forensics Block Bitmaps

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: Block Bitmaps

Joseph Moronwi
February 18, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnn3grv1pqOH1ks9J7AwZpO-hxd7wbS-YIa0NEQYd8JTcu2kSNkqHqZCTPZ4bnhm2GiqjfUf70CWIemlZSswAEqXlsd1gLRe4dzoiLM-7T9unDo0_kMaxp_yO_TpUpM1erdgOteR5iitV8P80pHHphhO7h21zha6zGkpTfuFhLQ-WFFjV6HG0Rk8lctnw/w654-h247/bitmap1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnn3grv1pqOH1ks9J7AwZpO-hxd7wbS-YIa0NEQYd8JTcu2kSNkqHqZCTPZ4bnhm2GiqjfUf70CWIemlZSswAEqXlsd1gLRe4dzoiLM-7T9unDo0_kMaxp_yO_TpUpM1erdgOteR5iitV8P80pHHphhO7h21zha6zGkpTfuFhLQ-WFFjV6HG0Rk8lctnw/s691/bitmap1.jpg)

In file system forensics, a bitmap is a special metadata structure that records which storage units on a disk (blocks or clusters) are allocated (in use) and which are free. It acts like a map of the disk's space usage and is crucial for understanding file allocation, detecting hidden data, and identifying anomalies.

With a maximum supported block size of 4096 bytes, ext4 block and inode bitmaps can each describe up to 32,768 objects (4096 × 8 bits) per block group. In these bitmaps, a value of 1 indicates an allocated (unavailable) object, while 0 denotes a free object. When a block group contains fewer blocks or inodes than the theoretical maximum, the bitmap entries corresponding to nonexistent objects are set to 1 to prevent their allocation. Investigators should note that ext4 features such as lazy bitmap initialization may temporarily affect how these bits appear on disk.

# Block Bitmap

In the ext4 file system, a block bitmap is a metadata structure that records which data blocks inside a block group are currently allocated and which are free. It plays a central role in file creation, deletion, and forensic reconstruction. Every block group in the ext4 partition has its own block bitmap. The bitmap is a sequence of bits. Each bit corresponds to one block in that block group. If a block is in use, its corresponding bit will be set; otherwise, it will be unset.  The least significant bit of byte 0 represents block 0 in the block
group’s data area. The most significant bit in byte 0 represents block 7 in the data area. In byte 1,
the least significant bit represents block 8, and so on.

The block bitmap occupies exactly one block (typically 4096 bytes = 32768 bits), allowing it to track up to 32,768 data blocks per group - matching the typical blocks-per-group value. In flex\_bg mode (almost always enabled by default), the block bitmaps for multiple block groups (usually 16) are consolidated into a single contiguous run starting in the first block group of the flex group (often called the 'flex group block bitmap'). The location of the block bitmap is obtained by reading the `bg_block_bitmap_lo/hi` field of the
specified group descriptor. To determine which bit corresponds to a given block in an ext4 block bitmap, you will need to calculate the block's relative index within its block group with the following steps:

* Determine which block group contains the physical block.

  ```
  Group = Block Number/BLOCKS_PER_GROUP
  ```
* Find the block's position within that specific group (i.e., the relative block number).

  ```
  Relative Block Number = Block Number % BLOCKS_PER_GROUP
  ```
* **Locate the Bit**: The relative block number corresponds to the following expression.

  ```
  Bit = Relative Block % 8
  ```
* **Byte Offset**: To find the specific byte in the bitmap, divide the Relative Block Number by 8.

  ```
  Byte = Relative Block / 8
  ```

Modern ext4 filesystems commonly enable the `BLOCK_UNINIT` feature, which allows block group bitmaps to be created lazily rather than fully initialized at format time. When this feature is active, some block group descriptors are marked with the `EXT4_BG_BLOCK_UNINIT` flag, indicating that the corresponding block bitmap has not yet been populated with a definitive allocation map. From a forensic perspective, this behavior has important consequences. A block marked as “free” in an uninitialized bitmap does not necessarily mean the block was previously allocated and then deleted. Instead, it may simply mean that the kernel has never initialized or scanned that bitmap. As a result, the block may still contain residual data from earlier filesystem instances, previous operating systems, or unrelated disk usage.

This weakens a common forensic assumption: that data carved from unallocated space represents deleted content. On ext4 volumes with `BLOCK_UNINIT` enabled, carved artifacts from such regions should be treated as leads rather than proof of prior file existence. Investigators should therefore verify if `BLOCK_UNINIT` is enabled and correlate block bitmap interpretation with other artifacts such as inode records, directory entries, journal logs, and application traces. When reporting findings, it is good practice to explicitly note that block allocation history may be indeterminate due to lazy bitmap initialization. Understanding this prevents overconfident conclusions and strengthens the defensibility of forensic findings. To detect the BLOCK\_UNINIT feature in the system under investigation, you can use dumpe2fs as follows.

```
sudo dumpe2fs image.dd | grep -i BLOCK_UNINIT
```

Also, each group descriptor has a bg\_flags value at offset 0x1A. 0x01 = INODE\_UNINIT; 0x02 = BLOCK\_UNINIT; 0x04 = ITABLE\_ZEROED. If you see groups with 0x02 or 0x03 (0x01 + 0x02) in bg\_flags, uninitialized block groups are present.

[**When we analyzed the contents of the group descriptor in our example image**](https://digitalinvestigator.blogspot.com/2026/02/ext4-forensics-group-descriptors.html?m=1), we saw
that the block bitmap for group 0 started in block 1035. We can extract the contents of that
block with blkcat (or dd):

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh1DPdjLWBn9eadqC2I4Of_ae33Xa21ycTFxMHqdD2WQ0j-WhRowGNkmMljs2e9LlwxUC-7mgWv3sxEHktTP8mNaOTsIP0L_7G-tQTilmNLjVoRy6GED-8pWw1ryt6FvwWWT9KA2CC6TUah_R8WXN7WmM97ETLG0XV3oXwLM3YGOmgzFrvGg3KB-D9cok/w659-h249/bitmap1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh1DPdjLWBn9eadqC2I4Of_ae33Xa21ycTFxMHqdD2WQ0j-WhRowGNkmMljs2e9LlwxUC-7mgWv3sxEHktTP8mNaOTsIP0L_7G-tQTilmNLjVoRy6GED-8pWw1ryt6FvwWWT9KA2CC6TUah_R8WXN7WmM97ETLG0XV3oXwLM3YGOmgzFrvGg3KB-D9cok/s691/bitmap1.jpg)

The rows of all ‘f’ values indicate that many allocated (in-use) blocks are at the beginning of
block group 0. At byte 0x6B6 (1718) we see the value 0x00. Byte 0x6B6 (1718) corresponds with blocks 13744 (*Relative Block = 8 \* Byte offset*) to 13752. Therefore, as seen here, blocks 13744 onward are free (not allocated).

The block bitmap uses exactly `ceil(blocks_per_group/8)` bytes. With the default blocks\_per\_group = 32768 (on 4KB blocks), exactly 4096 bytes are needed to store the block bitmap. No slack space in the default case. However, when blocks\_per\_group is deliberately set lower than 32768 during formatting (via `mkfs.ext4 -g <smaller_number>`), the bitmap occupies fewer than 4096 bytes, which can result in Blo...