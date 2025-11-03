---
title: Analyzing The FAT Table For Digital Evidence
url: https://digitalinvestigator.blogspot.com/2025/11/analyzing-fat-table-for-digital-evidence.html
source: Instapaper: Unread
date: 2025-11-02
fetch_date: 2025-11-03T03:15:44.813047
---

# Analyzing The FAT Table For Digital Evidence

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Analyzing The FAT Table For Digital Evidence

Joseph Moronwi
November 01, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp0tBS_EU_U1qU-HfQoSmQTav044Lv5wxhAELJOBBcMBtxLwhij19vJ44VK1zeDk3SLuqZp5Y2CUKkq_f6YhAPAAViW_YJxJfnZxL5oAX8UuT5rFyL0StKKjcLI8SyifTtUeMZJbuiVDajxeWpp5O-Wi57OzUnFV78kpaoKjg9x9Ozj1hjr6gSmwJgyCc/w647-h486/slide8-n.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp0tBS_EU_U1qU-HfQoSmQTav044Lv5wxhAELJOBBcMBtxLwhij19vJ44VK1zeDk3SLuqZp5Y2CUKkq_f6YhAPAAViW_YJxJfnZxL5oAX8UuT5rFyL0StKKjcLI8SyifTtUeMZJbuiVDajxeWpp5O-Wi57OzUnFV78kpaoKjg9x9Ozj1hjr6gSmwJgyCc/s720/slide8-n.jpg)

A partition is divided into equally sized clusters — small, contiguous blocks of storage. The actual cluster size depends on the FAT variant and the size of the partition, but it usually falls somewhere between 2 KB and 32 KB. A file can span one or many clusters depending on its size, and the FAT file system represents each file as a chain of clusters linked together (forming a singly linked list). Importantly, these clusters are not always stored next to each other physically on disk but are often fragmented throughout the [Data Region](https://www.google.com/search?ved=1t:260882&q=Data+Region+file+system&bbid=5842881150816663200&bpid=1570478718897523229).  The File Allocation Table (FAT) is a list of entries that map to each cluster on the partition.  It contains cluster status and a pointer
to the next cluster in the chain that is allocated to a file.

# The FAT Table

The FAT area holds the FAT table(s), and the FAT table entries point to the
clusters in the data area. The FAT table is a data structure which stores the information about which clusters are used, free, or possibly unusable In addition to that, it stores information about the chain of clusters that belong to a particular file. The first data cluster in the volume is cluster #2. Multiple copies of the FAT table reside in the FAT area as
well, with the exact number given in the
[boot sector](https://www.google.com/search?ved=1t:260882&q=boot+sector+file+system&bbid=5842881150816663200&bpid=1570478718897523229). These are identical, synchronized copies of the FAT. This is only strictly for
redundancy purposes. If an error occurs from reading the primary allocated table, the
file system will attempt to read from the backup copies.  In [FAT32](https://www.google.com/search?ved=1t:260882&q=FAT32+file+system&bbid=5842881150816663200&bpid=1570478718897523229), a user can disable
this [FAT mirroring feature](https://www.google.com/search?ved=1t:260882&q=FAT+mirroring+feature&bbid=5842881150816663200&bpid=1570478718897523229) and dedicate an “active” table, other than the primary
table, for the operating system to read from. The first FAT starts after the [reserved sectors](https://www.google.com/search?ved=1t:260882&q=reserved+sectors+file+system&bbid=5842881150816663200&bpid=1570478718897523229), the size of which is given in the boot [sector](https://www.google.com/search?ved=1t:260882&q=sector+storage&bbid=5842881150816663200&bpid=1570478718897523229). The total size of each FAT is also given in the boot sector, and the second FAT, if it exists, starts in the sector following the end of the first.

A FAT table contains indexed entries for
each data block on the disk, indexed by the cluster address. The FAT has one entry
per cluster. Different versions of
FAT file systems use different file allocation table entry lengths, and this is where they get their name from.  The
[FAT12 file system](https://www.google.com/search?ved=1t:260882&q=FAT12+file+system&bbid=5842881150816663200&bpid=1570478718897523229) uses 12 bits per FAT entry; thus, two entries span 3 bytes. It is consistently
[little-endian](https://www.google.com/search?ved=1t:260882&q=define+little-endian&bbid=5842881150816663200&bpid=1570478718897523229): if those
three bytes are considered as one little-endian 24-bit number, the 12 least significant bits represent the first entry (i.e.,
cluster 0) and the 12 most significant bits the second (i.e., cluster 1). In other words, while the low eight bits of the first
cluster in the row are stored in the first byte, the top four bits are stored in the low nibble of the second byte, whereas the
low four bits of the subsequent cluster in the row are stored in the high nibble of the second byte and its higher eight bits in
the third byte.  The
[FAT16 file system](https://www.google.com/search?ved=1t:260882&q=FAT16+file+system&bbid=5842881150816663200&bpid=1570478718897523229) uses 16 bits per FAT entry; thus, one entry spans two bytes in little-endian byte order. The
[FAT32 file system](https://www.google.com/search?ved=1t:260882&q=FAT32+file+system&bbid=5842881150816663200&bpid=1570478718897523229) uses 32 bits per FAT entry; thus, one entry spans four bytes in little-endian byte order. The high four bits of each entry are reserved for other purposes, cleared during volume format, and should not be changed otherwise. A FAT32 entry, thus, actually uses the low 28-bits to address clusters.

Corresponding to any cluster number, a FAT entry can have certain permissible values given in the table below.  Note that FAT32 uses only 28 bits of the 32 possible bits. The upper 4 bits are usually zero, but are
reserved and should be left untouched. In the table below, these are denoted by a question mark.

|  |  |  |  |
| --- | --- | --- | --- |
| **Table 1: FAT entry cluster values** | | | |
| **FAT12** | **FAT16** | **FAT32** | **Description** |
| 0x000 | 0x0000 | 0x?0000000 | Free cluster. |
| 0x001 | 0x0001 | 0x?0000001 | Reserved value; do not use. |
| 0x002 - 0xFEF | 0x0002 - 0xFFEF | 0x?0000002 - 0x?FFFFFEF | Cluster is allocated. Value of the entry is the cluster number of the next cluster following this corresponding cluster. MAX is the Maximum Valid Cluster Number |
| 0xFF0 - 0xFF6 | 0xFFF0 - 0xFFF6 | 0x?FFFFFF0 - 0x?FFFFFF6 | Reserved and must not be used. |
| 0xFF7 | 0xFFF7 | 0x?FFFFFF7 | Indicates a bad (defective) cluster. |
| 0xFF8 - 0xFFF | 0xFFF8 - 0xFFFF | 0x?FFFFFF8 - 0x?FFFFFFF | Last cluster in file or End of Cluster chain (EOC) or End of File (EOF). |

The first cluster of the Data Region is cluster #2. That leaves the first two entries of the FAT unused. In the first byte (8 bits) of the first entry, a copy of the BIOS Parameter Block at offset 0x15 (the media descriptor) is stored. The remaining 8 bits (if FAT16) or 20 bits (if Fat32) of this entry are set to 1. In the second entry the end-of-cluster-chain marker is stored. The high order two bits of the second entry are sometimes, in the case of FAT16 and FAT32, used for dirty volume management: high-order bit if set to 1 indicates the last shutdown was clean, otherwise abnormal; the next highest bit if set to 1 indicates that during the previous mount, no disk I/O errors were detected, else there were. Because the first two FAT entries store special values, there is no cluster 0 or 1. The first addressable cluster is cluster 2, which is the reason why BPB value at offsets 0...