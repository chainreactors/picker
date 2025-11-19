---
title: Deleted File Forensic Recovery In FAT File Systems
url: https://digitalinvestigator.blogspot.com/2025/11/deleted-file-forensic-recovery-in-fat.html
source: Instapaper: Unread
date: 2025-11-18
fetch_date: 2025-11-19T03:14:53.518585
---

# Deleted File Forensic Recovery In FAT File Systems

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Deleted File Forensic Recovery In FAT File Systems

Joseph Moronwi
November 15, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjZsFP7RClImrmjEZiAVu0-qZr_1Nhf-0rOrGwdwhLAoFvmkKgAwkHOPAXxrfcyVnuMKRpdQZlCbr-1o6DKOi0FgXBmLuD1MYGe1g6UuC8QbWSN21KZaEhMUfIbAKcLnd_eRpdhn9XWzJy6rnQ6rTNfaC7ED-CAAsih-ye5m9fIYaN1D0K8IDse2DNjW0/w652-h309/recover.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjZsFP7RClImrmjEZiAVu0-qZr_1Nhf-0rOrGwdwhLAoFvmkKgAwkHOPAXxrfcyVnuMKRpdQZlCbr-1o6DKOi0FgXBmLuD1MYGe1g6UuC8QbWSN21KZaEhMUfIbAKcLnd_eRpdhn9XWzJy6rnQ6rTNfaC7ED-CAAsih-ye5m9fIYaN1D0K8IDse2DNjW0/s849/recover.png)

Data recovery techniques are broadly classified into two categories: **logical data recovery** and **physical data recovery**. The appropriate method depends on the nature of data loss.

Physical data recovery is necessary when data is lost due to actual damage to the storage device's hardware components. This occurs when the drive cannot function properly or is completely inaccessible. Common causes of this category of data loss include mechanical failure (e.g., a broken hard drive read/write head or hard drive motor failure), electronic failure (e.g., a faulty circuit board), physical damage (e.g., fire, water, or impact damage), SSD NAND chip degradation, bad sectors, or platter degradation. The recovery process must be conducted by professionals in a specialized, contaminant-free environment (a "cleanroom"). Technicians may need to repair or replace components to temporarily get the drive running long enough to create a complete image of the data, after which logical techniques are used to extract the files from that image, extracting data by bypassing faulty hardware for SSDs and flash: chip-off or JTAG recovery. Attempting DIY physical recovery can cause further, permanent data loss. This is beyond the scope of this post and will be treated in a later article.

Logical data recovery is performed when the storage medium itself is physically healthy, but the data contained therein is inaccessible due to non-hardware issues. The data loss is typically a result of software or user error problems. Common causes of this category of data loss include accidental file deletion, accidental formatting or re-partitioning of a drive, file system corruption (e.g., due to an operating system crash or power interruption), or malware attacks. In these scenarios, the data might still be present on the storage medium, but the pointers or file system entries that the operating system uses to locate the files are damaged or missing. Recovery technique often involves analyzing and reconstructing file system metadata, scanning for file signatures (file carving), rebuilding damaged partition tables, and recovering deleted entries that have not been overwritten.

# Logical Data Recovery

Logical data recovery is commonly divided into two major categories, based on how the lost data is reconstructed. They include metadata-based (file system-based) recovery and file carving (signature-based recovery). The focus of this post is on the residual file system metadata-based recovery technique in the FAT file system. From a forensics point of view, however, it is not just deleted files that are
of concern. The investigator needs to be able to recognize the presence of
hidden files, disguised files, and invisible files as well.

When a user deletes a file, the clusters assigned by the file system to that file are marked as free, and the space is now unallocated. The data is not affected and is still kept intact until one of two things happens. The first is if the file system identifies the cluster as free and uses it for another file. In that case, however, if the cluster is not completely overwritten, it may be possible to extract data from the part of the cluster not completely overwritten (called file slack space). The second thing that can destroy the data in unallocated clusters is to use a wipe utility. Such a utility overwrites the data repeatedly with 0s and 1s, wiping the data between each pass. Some utilities perform as many as 32 passes. The average digital forensic lab will be unable to retrieve any data from clusters subjected to such a wipe. However, some highly specialized facilities have equipment that can extract information from drives on a molecular level. This, however, is far beyond the scope of this post. Also in this post, I am assuming that neither of the two scenarios just discussed applies.

What is important from a forensic viewpoint is that on deletion of a file, the operating system does not delete the information contained in the clusters; it merely marks them as available for reallocation. It is therefore quite possible to restore a file that has been deleted, provided that the clusters of the file have not been reused. The deleted directory entry will often contain details of the first cluster and the file length, and this can greatly assist the process. Nevertheless, these traditional recovery methods that make
use of the file system structure presented on storage devices become ineffective when
the file system structure is corrupted or damaged, a task easily accomplished by a technically astute criminal or disgruntled insider with freely available tools. A more sophisticated data recovery solution that does not rely on this file system structure has thus become necessary. These new and sophisticated solutions are collectively known as
file carving. File carving recovers data directly from raw disk blocks by identifying file signatures and internal structures, without relying on any file system metadata. This post also assumes that there is no damage to or corruption of the file system.

To understand how file and
data recovery work, it is essential to have at least a rudimentary understanding
of how the file system manages data in memory and in storage systems.

## File Creation and Deletion in FAT File Systems

For simplicity, we will focus on examples involving files located in the root directory. The same principles apply to files in other directories—the only additional step is identifying the directory that contains the target file. This is done by traversing the full file path, starting at the root and moving through each subdirectory until the correct location is reached.

### File Creation

When a new file is created, the operating system determines where to place it on the file system to allow efficient access later. It first looks for a large enough block of consecutive unallocated clusters to store the entire file. Over time, however, free space becomes scattered as files are added and removed, and the largest available block may not be sufficient. When this happens, the file must be divided into smaller parts and stored across multiple separate free-space segments. This process results in a fragmented file as shown by the example (file 2015\_16.xlsx) in the figure below.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUvis4sXR07TrPNmLGCKtZSEK-4z...