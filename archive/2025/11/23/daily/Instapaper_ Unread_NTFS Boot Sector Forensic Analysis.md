---
title: NTFS Boot Sector Forensic Analysis
url: https://digitalinvestigator.blogspot.com/2025/11/ntfs-boot-sector-forensic-analysis.html
source: Instapaper: Unread
date: 2025-11-23
fetch_date: 2025-11-24T03:22:19.036133
---

# NTFS Boot Sector Forensic Analysis

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# NTFS Boot Sector Forensic Analysis

Joseph Moronwi
November 18, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOu5ld0V1aegyMKGMC-YuNKDTuPSmRhKqLPHtYDXp27OU4PNDCVabyTkrrpLEMaAbWZ4xB6s_6iEsMTxkqGM0F9TG-tHpwteyxSPsiVLJb3e30pGRuKzmrok7PMKHHYmeTMkYnGUSPRgRyHE1rI9aMyqQWPUR5LPrIkcPgZLyU38-ksmQiVUMPBT7SXmI/w663-h438/VBR.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOu5ld0V1aegyMKGMC-YuNKDTuPSmRhKqLPHtYDXp27OU4PNDCVabyTkrrpLEMaAbWZ4xB6s_6iEsMTxkqGM0F9TG-tHpwteyxSPsiVLJb3e30pGRuKzmrok7PMKHHYmeTMkYnGUSPRgRyHE1rI9aMyqQWPUR5LPrIkcPgZLyU38-ksmQiVUMPBT7SXmI/s654/VBR.jpg)

When a volume is formatted with the NTFS file system, several system (metadata) files are created, including the Master File Table (MFT), which stores information about all files and folders on the volume. The volume begins with the partition boot sector (the $Boot metadata file) at sector 0, up to 16 sectors in size, and the first file created is the MFT ($MFT). The following figure shows the layout of an NTFS volume.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikx4DLL_DpFVQ8Ez4xkZEFKArw4-UFDgGs8GArAw2YHnhdk8QyDaqlZp7IU7vwMObBqJov6o-Z9mqQQVg0hj2idKKJPODYqEstko_JrvL6rlnM1MgKoEvfTuzy6YMQmb_KMdPrSH61SBhyHFOHyIq6x1_GwwVeKcsWucSfY-6UIAfPdzoNxkNRqOZkhQM/w659-h187/426239_1_En_7_Fig1_HTML.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikx4DLL_DpFVQ8Ez4xkZEFKArw4-UFDgGs8GArAw2YHnhdk8QyDaqlZp7IU7vwMObBqJov6o-Z9mqQQVg0hj2idKKJPODYqEstko_JrvL6rlnM1MgKoEvfTuzy6YMQmb_KMdPrSH61SBhyHFOHyIq6x1_GwwVeKcsWucSfY-6UIAfPdzoNxkNRqOZkhQM/s685/426239_1_En_7_Fig1_HTML.png)

Like the boot sector in FAT, the boot sector in NTFS describes the data structure of the file system. It provides the cluster size, MFT entry size, and the starting cluster
address of the MFT since it is not placed in a predefined sector.

# The NTFS Partition Boot Sector

On an NTFS volume, the Partition Boot Sector resides at logical sector 0 and occupies the first 16 sectors as the **$Boot** metadata file. Sector 0 contains the boot record and BIOS Parameter Block (BPB), while sectors 1–15 store the remainder of the boot record. NTFS also places a backup copy of this boot sector at the last sector of the partition for reliability.

The BPB provides key file system parameters, including the MFT record size and the starting location of the $MFT. These values are essential for correctly identifying and interpreting MFT records during forensic analysis. The figure below shows the hexadecimal dump of the boot sector.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZZ0siLhbK4W-YL0A6a8z6TLw9GH6aUWjvnRl352DrRHUVQHfQIdKVVf-XgzhH9hOSx-vrnkouxrU80F0yHUddEwVY0vVE1nvTGj62HnC0dk8RGYr8lT8x4h4eKBLqIZYsmA6gtoSYvLojh6rI-l_xdRl0qdXoDsPAlGaZQNs_JsITFPETb2xqca_M-4g/w654-h432/1651783997851128-0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZZ0siLhbK4W-YL0A6a8z6TLw9GH6aUWjvnRl352DrRHUVQHfQIdKVVf-XgzhH9hOSx-vrnkouxrU80F0yHUddEwVY0vVE1nvTGj62HnC0dk8RGYr8lT8x4h4eKBLqIZYsmA6gtoSYvLojh6rI-l_xdRl0qdXoDsPAlGaZQNs_JsITFPETb2xqca_M-4g/s668/1651783997851128-0.jpg) |
| Figure 1: Hexadecimal dump of the NTFS boot sector |

It should be noted that the values are stored in Little Endian. To parse correctly, the endianness must be reversed. At the table below is shown the outline layout of the BIOS Parameter Block which begins at byte offset 0x0B of the boot sector.

|  |  |  |
| --- | --- | --- |
| **Byte Offset** | **Length** | **Description** |
| 0x0B | WORD | Number of bytes per sector, usually 512 |
| 0x0D | BYTE | Number of sectors per cluster |
| 0x0E | WORD | Number of reserved sectors, usually 0 |
| 0x10 | 3 BYTES | Always 0 |
| 0x13 | WORD | Not used by NTFS |
| 0x15 | BYTE | Media descriptor.  The type of media on which the file system is resident. This is generally 0xF8 for standard hard drives. |
| 0x16 | WORD | Always 0 |
| 0x18 | WORD | Sectors per track (used by BIOS, not critical for NTFS). This value is related to the old format CHS addressing in disks |
| 0x1A | WORD | Number of heads (used by BIOS, not critical for NTFS). This value is related to the old format CHS addressing |
| 0x1C | DWORD | Hidden sectors. Number of sectors before the start of the partition. Meaning uncertain. |
| 0x20 | DWORD | Not used by NTFS |
| 0x24 | DWORD | Not used by NTFS |
| 0x28 | LONGLONG | Total sectors |
| 0x30 | LONGLONG | Logical Cluster Number (LCN) for the file $MFT |
| 0x38 | LONGLONG | Logical Cluster Number (LCN) for the file $MFTMirr |
| 0x40 **\*** | BYTE | Size of the MFT record in clusters, usually 1024. A two’s complement number. A positive number represents the MFT record size in bytes. In the case of a negative number, x, the MFT record size is given by 2|x| bytes. |
| 0x41 | 3 BYTES | Not used |
| 0x44 **\*** | BYTE | Size of index buffer, INDX file, in clusters. |
| 0x45 | 3 BYTES | Not used |
| 0x48 | LONGLONG | Volume Serial Number |
| 0x50 | DWORD | Not used |

The two values marked with an asterisk (\*) (i.e., offsets 0x40 and 0x44) in the table above are signed 8-bit numbers
that may be used in two different ways. If the numbers in these fields are positive
(between 0x00–0x7F) they define how many clusters there are for each MFT record or INDX file. If the numbers are negative (0x80–0xFF), they define how many bytes there are
for each MFT record or INDX file.

The actual value is calculated by raising 2 to the power of the absolute value of this
number. Thus, if byte offset 0x40 contains, as it does in the sample BPB in Figure 1, the value F6h,
then the 8-bit signed value of the number, F6, is –10 and its absolute value is 10. Thus, the number of bytes (because it is negative) in each MFT record entry is 210 = 1024 bytes. This conforms with current experience that all systems seen to date have a
1024-byte MFT record size.

Similar to other file systems, such as FAT, NTFS uses clusters to allocate disk space for files, and each cluster comprises a certain number of sectors, typically a
power of two sectors. The cluster number starts with 0 at the beginning of the file
system. The number of clusters in NTFS is also given another name called LCN
(Logical Cluster Number). Further, the clusters belonging to a file are referenced in
the MFT using virtual cluster numbers (VCNs). VCNs start from 0, sequentially
increasing by 1 until the last cluster allocated to the file. An LCN is its relative offset
from the beginning of an NTFS file system, whereas a VCN is its relative offset from
the beginning of a file. Both LCN and VCN start from 0. The figure below shows an
example of a file with 3 clusters (clusters 1355, 1588, and 2033) and the VCN-to-LCN
mapping for the clusters in the MFT.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_Ob-rXvCywQmJOwdnZuUFsink704kGaONgD8fZkuVVL19NnLuEyJPEnuZRqc5eAXX9fuU-otliRV2lBbFTjMxOZ9tlsxBwodWeFWO0rwinTXyIBoAAhtUnGqifNOcKTjptz84zO_hOM0ekXOCQu3uYCvpXvXVP1frTO12vztsYf0i-q1J0G6XEbBRadQ/w647-h273/f12yj28.jpg)](https://blogger.googleusercontent.com/img/b/...