---
title: Recycle Bin Forensic
url: https://forensicfossil.com/2024/09/recycle-bin-forensic
source: Instapaper: Unread
date: 2024-10-02
fetch_date: 2025-10-06T18:58:47.300447
---

# Recycle Bin Forensic

![](https://forensicfossil.com/themes/blog/images/logo.png)

## [Forensicfossil](https://forensicfossil.com/)

SOC Analyst Blog

[Twitter](https://twitter.com/forensicfossil)[Instagram](https://instagram.com/forensicfossil)[RSS](https://forensicfossil.com/feed/rss)

Toggle navigation

* [Home](https://forensicfossil.com/)

1. [Home](https://forensicfossil.com/)
»2. [Windows Artifacts](https://forensicfossil.com/category/windows-artifacts)
» Recycle Bin Forensic

[![Recycle Bin Forensic](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*RrJuA6XIy6hhY-CkWKiq-g.png)](https://forensicfossil.com/2024/09/recycle-bin-forensic)

# Recycle Bin Forensic

26 September 2024 - Posted in
[Windows Artifacts](https://forensicfossil.com/category/windows-artifacts) by
[forensicfossil](https://forensicfossil.com/author/forensicfossil)

The Recycle Bin is a feature in Microsoft Windows that allows users to recover deleted files. When a file is deleted from the computer, it is not immediately erased from the hard drive but instead it is moved to the Recycle Bin. The Recycle Bin acts as a temporary storage location for deleted files, and users can restore these files if they need to. This makes the Recycle Bin an important location for forensic investigations, as deleted files may contain valuable information that can help in an investigation.

![enter image description here](https://miro.medium.com/v2/resize:fit:500/format:webp/0*u0uiddywy77KM8X6.png)

Today, with the recycle bin, each user has his/her own recycle bin directory. This is why it is trivial for a forensic investigator to understand these directories, their permissions and privileges in order to be able to analyze them and acquire useful information such as reconstructing the content.

**Please Note** that users could easily bypass the Recycle Bin by using the **Shift + delete** key combination!
The case where a user uses Shift + delete a file could be analyzed going back to a lower level, and here i mean by diving into the file system and disk level. Analyzing the system on a file system and disk level could aid in such scenerio.

**Where is the recycle bin located?**

In Windows XP and earlier versions of Windows, the Recycle Bin data is stored in a hidden directory at the root of each drive, and it’s named **“RECYCLER”** This directory contains a system folder with a unique identifier for each user, and it’s where the Recycle Bin stores the deleted files.

For example:

**C:\RECYCLER\S-1–5–21-… (followed by a unique user identifier)**

In Windows 10 and more recent versions of Windows, including Windows 8 and Windows 7, the structure has changed, and the Recycle Bin data is stored in a hidden directory named **“$Recycle.Bin”** at the root of each drive. Like in Windows XP, it contains a system folder with a unique identifier for each user.

For example:

**C:\$Recycle.Bin\S-1–5–21-… (followed by a unique user identifier)**
The identifiers following the “S-1–5–21” part will be unique to each user account on the system. \*\*The use of unique identifiers ensures that each user’s deleted files are stored separately within the Recycle Bin.

![enter image description here](https://forensicfossil.com/content/images/20240926153536-SID-1.png)

The command **wmic useraccount get name,sid** retrieves and displays the names and Security Identifiers (SIDs) of all user accounts on a Windows system.

I am currently log in as Pawn which end with the SID of 1001 so that is the folder under which my Recycle bin should be stored.

![enter image description here](https://forensicfossil.com/content/images/20240926155106-SID-2.png)

After navigating into the Pawn SID directory, I found it empty. I will proceed by deleting two images and then attempt this process again

![Deleted-files](https://forensicfossil.com/content/images/20240926155328-SID-3.png)

After deleting two images 4 files as expected two $I containing the metadeta and two $R containing the actual deleted files.

**What are $I and $R files?**
**$I and $R** files are components of the Windows Recycle Bin that store information about deleted files:

**$I Files:** : $I Files with names starting with $I are known as INFO2 files. They store metadata information about each deleted file, such as the original file name, the date and time it was deleted, and other attributes. The $I files help the Recycle Bin maintain a record of the deleted files. The $I file contains information about the deleted file including the file’s size, deleted time, path, etc.Example: $I1234567890.txt

**$R Files:** $R Files with names starting with $R are known as the Recycle Bin data files. These files store the actual data of deleted file itself . Each $R file corresponds to a specific deleted file and contains the file’s content. Example: $R1234567890.ext

The extension of the $R file corresponds to the original extension of the deleted file. To check its content, we need to copy this file outside the Recycle Bin directory in order to proceed with its opening.

![enter image description here](https://forensicfossil.com/content/images/20240926164955-SID-4.png)

We see it indeed the original file that was deleted has been renamed with a random seven character value and in front of that the $R has been prepended.

if i open the $I file with notepad

![enter image description here](https://forensicfossil.com/content/images/20240926165926-SID-5.png)

After opening the $I file with Notepad, we were able to view the directory and the original file name of the image. However, this information is not sufficient for our analysis. Therefore, I will be using a command-line tool called RecBin. This tool will help us parse the $I file and provide additional details, such as the date and time of deletion

![enter image description here](https://forensicfossil.com/content/images/20240926170618-SID-6.png)

The command **recbin.exe -f $I5TEENF.jpg** retrieves metadata from the Recycle Bin for the deleted file associated with the **$I5TEENF.jpg** metadata file.

* **C:\Users\Pawn\Downloads\what-is-cybersecurity.jpg:** This is the original file path before the file was deleted
* **[99022 bytes]:** This is the size of the deleted file, what-is-cybersecurity.jpg, which is 99,022 bytes.
* deleted on **Thu Sep 26 19:41:24 2024 Z:** This shows the exact date
  and time (in UTC, as indicated by the Z suffix) when the file was
  deleted—September 26, 2024, at 19:41:24

**Second $I File:**
![enter image description here](https://forensicfossil.com/content/images/20240926171341-SID-7.png)

**Significance of the Windows Recycle Bin in Digital Forensic Examinations**

The Windows Recycle Bin is a pivotal artifact in digital forensic investigations for several reasons:

**Data Recovery:** Deleted files that are not permanently removed can be recovered from the Recycle Bin, providing crucial evidence.

**User Activity Reconstruction:** Metadata associated with deleted files, such as original file paths and deletion timestamps, helps reconstruct user actions and timelines.
**Attribution:** In multi-user environments, individual user directories within the Recycle Bin allow for accurate attribution of deleted files to specific users.

**Case Examples**

**Law Enforcement**
In a criminal investigation, law enforcement can analyze the Recycle Bin to recover deleted files that might contain incriminating evidence, such as illegal downloads or communications. For example, in a case of online harassment, recovered deleted chat logs can provide crucial evidence to identify and prosecute the perpetrator.

**Internal Investigations**
During an internal corporate investigation into data theft, the Windows Recycle Bin can reveal attempts to cover up malicious activity. For instance, an employee suspected of stealing sensitive data may delete files after transferring them to an external drive. Forensic analysis of the Recycle Bin can recover these deleted files and uncover the breach.

**E-Discovery**
In e-discovery during lit...