---
title: Analyzing The FAT Boot Record For Digital Evidence
url: https://digitalinvestigator.blogspot.com/2025/10/analyzing-fat-boot-record-for-digital.html
source: Instapaper: Unread
date: 2025-10-30
fetch_date: 2025-10-31T03:14:52.601302
---

# Analyzing The FAT Boot Record For Digital Evidence

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Analyzing The FAT Boot Record For Digital Evidence

Joseph Moronwi
October 28, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnfQtnR0BRuABZT2nC7pkjl9segJ32LiFMqH67Aazzdk2aGSaW3BxIfKRQqx9hhh9ecQY6_W-G9u3xtbyTiFdrAm4fDgkK6r_v64Md6Lv3yGX3z8c_RzI0KoumSOKxKmZFyjIdvB4t974MWoFYaeWVcHJa9JW9bIgMvDE4-2OmGML-oIo3wyxEwZNTcJI/w651-h489/slide4-n.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnfQtnR0BRuABZT2nC7pkjl9segJ32LiFMqH67Aazzdk2aGSaW3BxIfKRQqx9hhh9ecQY6_W-G9u3xtbyTiFdrAm4fDgkK6r_v64Md6Lv3yGX3z8c_RzI0KoumSOKxKmZFyjIdvB4t974MWoFYaeWVcHJa9JW9bIgMvDE4-2OmGML-oIo3wyxEwZNTcJI/s720/slide4-n.jpg)

[The File Allocation Table](https://www.google.com/search?ved=1t:260882&q=define+File+Allocation+Table&bbid=5842881150816663200&bpid=7984583167237177894) (FAT) file system was originally designed by **[Marc McDonald](https://www.google.com/search?ved=1t:260882&q=Marc+McDonald+Microsoft&bbid=5842881150816663200&bpid=7984583167237177894)** at [Microsoft](https://www.google.com/search?ved=1t:260882&q=Microsoft+corporation&bbid=5842881150816663200&bpid=7984583167237177894) in **1977** for use with **[Microsoft Standalone Disk BASIC-80](https://www.google.com/search?ved=1t:260882&q=Microsoft+Standalone+Disk+BASIC-80&bbid=5842881150816663200&bpid=7984583167237177894)**. It was later refined and incorporated into **[MS-DOS](https://www.google.com/search?ved=1t:260882&q=MS-DOS+operating+system&bbid=5842881150816663200&bpid=7984583167237177894)**, with contributions from **[Bill Gates](https://www.google.com/search?ved=1t:260882&q=Bill+Gates+Microsoft&bbid=5842881150816663200&bpid=7984583167237177894)** and other Microsoft engineers. Over time, it evolved into three main versions—[FAT12](https://www.google.com/search?ved=1t:260882&q=FAT12+file+system&bbid=5842881150816663200&bpid=7984583167237177894), [FAT16](https://www.google.com/search?ved=1t:260882&q=FAT16+file+system&bbid=5842881150816663200&bpid=7984583167237177894), and [FAT32](https://www.google.com/search?ved=1t:260882&q=FAT32+file+system&bbid=5842881150816663200&bpid=7984583167237177894)—distinguished primarily by the size of their addressable entries in the FAT structure.

Microsoft stopped using FAT file systems for operating systems with the advent of Windows NT in the
mid- to late 1990s. Early versions of Windows assumed that there was only one user. The FAT file
system did not have any way to store file ownership or file access permissions, so it was unsuitable for
an operating system that could handle multiple users. The one arena where FAT32 still survives is in [USB drives](https://www.google.com/search?ved=1t:260882&q=USB+drives&bbid=5842881150816663200&bpid=7984583167237177894). They need to go from a camera to a PC to a phone, etc. Support for FAT32 is ubiquitous, so it is still the standard on USB drives.

The layout of the FAT file system has three physical sections to it, which can be seen
in the figure below.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHm-iUToKiUTnOnMY18hBznf2K6TvAxO1UZqPUUnu4lHwdCn6-8yu9mcud7iMdnM_490RG8f46vdBOekqBynu_VTGuxRoL_f2Ly7MtjtOVKvzEAs5QL3Xa-92pRX7wKqld9Rpzkq8UFIHUK5g_ihl0WGrBNdo0vJytILc8GQwimhZhUJO_EmBgJ2B4n7g/w655-h198/FAT%20layout.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHm-iUToKiUTnOnMY18hBznf2K6TvAxO1UZqPUUnu4lHwdCn6-8yu9mcud7iMdnM_490RG8f46vdBOekqBynu_VTGuxRoL_f2Ly7MtjtOVKvzEAs5QL3Xa-92pRX7wKqld9Rpzkq8UFIHUK5g_ihl0WGrBNdo0vJytILc8GQwimhZhUJO_EmBgJ2B4n7g/s685/FAT%20layout.png) |
| Figure 1: Layout of the FAT file system |

The [reserved area](https://www.google.com/search?ved=1t:260882&q=FAT+file+system+reserved+area&bbid=5842881150816663200&bpid=7984583167237177894) begins at sector 0 of the file system, and its size is defined in the [boot sector](https://www.google.com/search?ved=1t:260882&q=FAT+file+system+boot+sector&bbid=5842881150816663200&bpid=7984583167237177894). In FAT12 and FAT16, it typically consists of a single sector, while FAT32 usually reserves multiple sectors. The data at byte offsets 0xe-0xf in figure 2 (i.e., 0x0026) represents the size in sectors for the reserved area. This corresponds to 38 sectors.

The [FAT area](https://www.google.com/search?ved=1t:260882&q=FAT+file+system+area&bbid=5842881150816663200&bpid=7984583167237177894) follows the reserved area and contains one or more FAT structures. There are two important parameters related to this area: the number of FAT copies and the size of each FAT table. Its total size is determined by multiplying the number of FATs by the size of each one, both values specified in the boot sector. The data at byte offset 0x10 in Figure 2 represents the number of FAT copies, which is
“0x02” (or 2 copies). And the data at byte offsets 0x16-0x17 represents the size
in sectors for one FAT table, which is “0x0000.” It indicates the file system here is
FAT32. Then, it
should be referred to the data at byte
offsets 0x24–0x27 for the FAT table size
in sectors, which is "0x0000038D" (i.e., 909 sectors).

Next is the [data area](https://www.google.com/search?ved=1t:260882&q=FAT+file+system+data+area&bbid=5842881150816663200&bpid=7984583167237177894), which holds the clusters used to store files and directories. It begins immediately after the FAT area, and its size is calculated by subtracting the data area’s starting sector from the total number of sectors in the file system, as indicated in the boot sector. The data area is divided into clusters, with the number of sectors per cluster also defined in the boot sector. The size in
sectors for the file system is represented by the data either at byte offsets 0x13-0x14 (a 2-byte value) or at byte offsets 0x20-0x23 (a 4-byte value) if the 2-byte
value above (bytes 0x13-0x14) is zero. It is obvious that in Figure 2, the
total size of the file system is stored at byte offsets 0x20-0x23. The size of the file system is 0x000E37BA = 931770 sectors. Therefore, the size of the data area is 930823 sectors after subtracting the
sizes of the reserved and FAT areas.

Within the data area, there is one important structure, the [root directory](https://www.google.com/search?ved=1t:260882&q=FAT+file+system+root+directory&bbid=5842881150816663200&bpid=7984583167237177894). The
root directory is always located immediately following the FAT region (i.e., the beginning of the data area) in FAT12 and FAT16, whereas it can be stored anywhere within
the data area in FAT32 (though it is commonly placed at the beginning). This flexibility enables FAT32 to work around bad sectors and allows the root directory to expand as needed. The starting cluster of the FAT32 root directory is defined in the boot sector, while its size is managed through the FAT structure.  In FAT12/16, we know the root directory is located immediately after the FAT area. Then, we know the number of directory entries by referring to the data at byte offsets 0x11-0x12. Since each directory entry is 32 bytes in size, the size of the root directory is obtained by multiplying the number of dire...