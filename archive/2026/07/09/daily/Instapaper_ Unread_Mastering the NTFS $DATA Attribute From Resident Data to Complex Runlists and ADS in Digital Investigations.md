---
title: Mastering the NTFS $DATA Attribute From Resident Data to Complex Runlists and ADS in Digital Investigations
url: https://digitalinvestigator.blogspot.com/2026/07/mastering-ntfs-data-attribute-from.html
source: Instapaper: Unread
date: 2026-07-09
fetch_date: 2026-07-10T06:00:03.512059
---

# Mastering the NTFS $DATA Attribute From Resident Data to Complex Runlists and ADS in Digital Investigations

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Mastering the NTFS $DATA Attribute: From Resident Data to Complex Runlists and ADS in Digital Investigations

Joseph Moronwi
July 06, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY0DFs5IRDXVyQIFvR3su_gU_-oKjSASk4C24ETsdMDjGDx8BGZEhMvCFDq653guNtCETQHuKuiocBOefQdiYI-wKDdRCxMotwJ6tBwjpqgzqv13lXWfF4_734y8hOmhepzHoiJpvEuoYiUouIvWAD3_LrEduvvafU6Cw1V6CCOR9B7vh_1OG5K8K9lV0/w658-h258/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhY0DFs5IRDXVyQIFvR3su_gU_-oKjSASk4C24ETsdMDjGDx8BGZEhMvCFDq653guNtCETQHuKuiocBOefQdiYI-wKDdRCxMotwJ6tBwjpqgzqv13lXWfF4_734y8hOmhepzHoiJpvEuoYiUouIvWAD3_LrEduvvafU6Cw1V6CCOR9B7vh_1OG5K8K9lV0/s845/1.png)

In the examination of NTFS Master File Table (MFT) records, the $DATA attribute (type 0x80) assumes paramount importance as the primary repository for file content. This attribute either encodes mapping metadata—via a runlist—to resolve the on-disk location of the file’s allocated clusters or, for sufficiently small streams (typically ≤ ~700 bytes, contingent upon MFT record utilization by other attributes), stores the data directly within the MFT record itself in **resident** form, thereby optimizing I/O efficiency and minimizing fragmentation.

While conventional file systems impose a singular one-to-one correspondence between a file and its primary data content, NTFS imposes no such architectural constraint. A file may possess **multiple associated data streams** (also known as Alternate Data Streams or ADS when named). The default (unnamed) $DATA attribute represents the primary data fork visible to most applications and the Win32 API. Additional named streams (e.g., $DATA:"Zone.Identifier", $DATA:"AFP\_AfpInfo", or user-defined streams) can coexist within the same MFT record, each potentially resident or non-resident, and each independently allocated and accessible.

This multi-stream capability, while powerful for metadata embedding, application-specific storage, and certain persistence techniques, introduces significant forensic considerations, including the potential concealment of data in alternate streams that are often invisible to standard directory listings and many forensic triage tools.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc-VnTFbUaJGJySl59v2u5nvzCINTG5_lKalM9gZ5513Wl97dsMLpoFZJVfV6WWdX9mTAyDaElHnfGyQ6QgK-DvanSuLpC68lylBoHkDVJfWJN-_kn-6VLGjHF9XJXELCs2i_oBKx38sTl7BCJP7L7OwVYmGLIlEDk2BiB2OPOabTFbBrtfrKUXNAS1Bg/w655-h258/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc-VnTFbUaJGJySl59v2u5nvzCINTG5_lKalM9gZ5513Wl97dsMLpoFZJVfV6WWdX9mTAyDaElHnfGyQ6QgK-DvanSuLpC68lylBoHkDVJfWJN-_kn-6VLGjHF9XJXELCs2i_oBKx38sTl7BCJP7L7OwVYmGLIlEDk2BiB2OPOabTFbBrtfrKUXNAS1Bg/s845/1.png)

The $DATA attribute is identified within an MFT record by its 4-byte type signature value of 0x80 (128 decimal). The common attribute header (beginning with the 4-byte type identifier and 4-byte length field) is followed by the attribute body, which either contains the actual file content (for resident attributes) or the metadata required to resolve the Logical Cluster Numbers (LCNs) of the on-disk allocations (for non-resident attributes).

A single-byte non-resident flag located at offset 0x08 within the attribute header designates residency status: 0x00 indicates a resident attribute whose content is stored directly within the MFT record, while 0x01 denotes a non-resident attribute whose data resides in external clusters. Virtual Cluster Numbers (VCNs) furnish a contiguous, zero-based logical addressing mechanism for the ordered clusters comprising the data stream. While the VCN range for the primary $DATA attribute typically commences at zero and extends through the highest VCN (corresponding to the total clusters consumed), rare cases—such as fragmented attributes or those described via an attribute list—may exhibit non-zero starting VCNs; additionally, the highest VCN may be set to -1 for zero-length streams.

The **Allocated Size** (in the non-resident header) reflects the aggregate on-disk cluster space consumed by the attribute, encompassing both file content and associated slack space. The **True Size** (Real Size or Data Size) specifies the precise logical length of the file content. The **Initialized Size** represents the extent of pre-allocated and initialized space reserved by the operating system for potential file growth; although this region is allocated on disk, it is not yet considered part of the logical file content until explicitly written.

For non-resident attributes, the data runs (runlist) provide a compact description of the file’s allocated segments. The runlist consists of a series of variable-length entries, each commencing with a 1-byte header. This header’s high nibble encodes the byte length of the signed LCN offset (delta) field, while the low nibble encodes the byte length of the run length field. The first run’s LCN offset is absolute, with subsequent offsets expressed as signed deltas relative to the prior LCN, thereby efficiently supporting contiguous, fragmented, sparse, and compressed allocations. The runlist is terminated by a null byte (0x00).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh75HLr9l3rgY68lYXi5aXp8whn8MHsGCcbRuWkxr48VM2jQ7oO7RYkbOO2nRtN2lUDnppBQYBjo2tzob8VSB90ri8H3VbYYWE1iNyU2s4Xx1sXmbvyz5yWXF1CZXCm_9-S9xMOUI7_a0tB_Obz6c-aPJo7OmRUmjpzqxmmDXzr-S6KWyhFrvU8AzL8gYA/w434-h177/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh75HLr9l3rgY68lYXi5aXp8whn8MHsGCcbRuWkxr48VM2jQ7oO7RYkbOO2nRtN2lUDnppBQYBjo2tzob8VSB90ri8H3VbYYWE1iNyU2s4Xx1sXmbvyz5yWXF1CZXCm_9-S9xMOUI7_a0tB_Obz6c-aPJo7OmRUmjpzqxmmDXzr-S6KWyhFrvU8AzL8gYA/s184/2.png)

The forensic breakdown is given in the table below:

| **Bytes** | **Meaning** | **Value** | **Explanation** |
| --- | --- | --- | --- |
| 32 | **Header** | 0x32 | High nibble (3) = 3 bytes for **offset** Low nibble (2) = 2 bytes for **length** |
| 4A 01 | **Run Length** (little-endian) | 0x014A = **330** clusters | Number of contiguous clusters in this run |
| 94 6B 01 | **LCN Offset** (little-endian, signed) | 0x016B94 = **93,076** (decimal) | Starting Logical Cluster Number (LCN) for this run |
| 00 00 | **End of runlist** | 0x0000 | Terminator (null bytes) |

In NTFS, a file may possess multiple data streams beyond the default (unnamed) primary data fork. These secondary streams are formally designated as **Alternate Data Streams (ADS)**. Key characteristics include:

* ADS are tightly bound to the parent file’s MFT record but remain orthogonal to the primary data stream; consequently, they exert no impact on the file’s reported size or content as presented by standard file system APIs and directory listings.
* Each ADS is identified by a discrete Unicode name (e.g., Zone.Identifier, AFP\_AfpInfo, or arbitrary user-defined streams).
* Every ADS maintains independent metadata, including its own $DATA attribute type, residency status, and size fields.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwugCqv3pr...