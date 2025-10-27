---
title: Windows Shell Items Analysis
url: https://blog.cyber5w.com/Shell_Item_Analysis.html
source: Instapaper: Unread
date: 2024-10-02
fetch_date: 2025-10-06T18:58:54.026486
---

# Windows Shell Items Analysis

[![CYBER 5W](/images/logo.png)](/)

## Menu

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

Search

Search for Blog

![Windows Shell Items Analysis](/images/shell_item_pic/cover.png)

2 min read
Sep 28, 2024

## Windows Shell Items Analysis

[![Cyber 5W's Picture](https://avatars.githubusercontent.com/u/80437140?s=328&v=32)](/about/)

[Cyber 5W](/about/)
in

[Disk-Forensics](/tag/Disk-Forensics)

# Shell-Item Analysis

Windows 10 shell items are metadata files that hold details about various objects in the Windows operating system, including shortcuts, files, and folders. These items are invaluable for forensic investigations because they provide insights into the location and usage of these objects.

To perform shell item forensics on Windows 10, you can use forensic tools such as Autopsy, EnCase, or Belkasoft Evidence Center, which are capable of extracting and analyzing shell item metadata. Additionally, manual analysis of shell items is possible using the Windows Shellbags parser, a tool that extracts and interprets the binary data stored in shell item files.

Shell items hold data that helps recreate the layout of a file system and understand how files and folders are used. This data is important in different forensic situations, such as looking into cybercrime, digital scams, and stealing of intellectual property.

In Windows forensics, there are three important types of information related to shortcuts and folders. These are Shellbags, .lnk files, and jump lists. Shellbags store information about folder view settings, such as the size and position of windows, and can reveal how a folder has been used.
.lnk files are shortcuts to files, folders, or applications, containing details like the target path, date and time stamps, and various attributes.
Jump lists, a feature in Windows 10, store lists of recently opened files, folders, or applications for specific programs, offering insights into the usage patterns of these applications.

# Shellbags

Shellbags are a crucial type of metadata in Windows 10 that store information about the view settings of a folder, such as window size and position, column widths and order in Details view, and sort order. Stored in the registry, shellbags offer valuable insights for forensic investigations by revealing how a folder has been used, including access dates and times, files opened, and the order of these activities.

## Key Forensic Insights from Shellbags

From another viewpoint, shellbags are groups of special settings in a computer’s memory that tell us about folders someone has looked at. This can be helpful when trying to find out what happened, like when a company says important information has been taken without permission. By looking at these settings, we can see which folders were viewed recently and who looked at them. Microsoft Windows keeps track of what people do with their files and computer screens using these settings.

### Locating and Analyzing Shellbags

USRCLASS.DAT File:

* Path: `C:\Users\<Username>\AppData\Local\Microsoft\Windows`
* Contains: User-specific settings and configuration details like desktop background and window size… etc.

Registry Hives:

* Path: `USRCLASS.DAT\LocalSettings\Software\Microsoft\Windows\Shell\Bags`
* Stores: Folder view settings as binary data.

By examining the USRCLASS.DAT file and the Bags subkey, forensic investigators can learn about how files and folders have been accessed and reconstruct the file system activity.
BagMRU Subkey:

* Path: `USRCLASS.DAT\LocalSettings\Software\Microsoft\Windows\Shell\BagMRU`
* Contains: Information about the most recently used (MRU) folders.

Examining the BagMRU subkey reveals the folders that have been used most recently, providing useful information about how files and folders are being used.

ShellNoRoam Subkey:

* Path: `USRCLASS.DAT\LocalSettings\Software\Microsoft\Windows\Shell\ShellNoRoam\Bags`
* Stores: Folder view settings for a specific user profile without syncing between devices or profiles.

### NTUSER.DAT File and Related Keys

NTUSER.DAT File:

* Path: `C:\Users\<Username>`
* Contains: User-specific settings and configurations.

Registry Paths:

* `NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags`
* `NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU`
* `NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam\Bags`
* `NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam\BagMRU`

Examining the NTUSER.DAT file and its related parts helps us understand how a user’s computer is used and set up, particularly looking at the folders they use most often.

## Forensic Tools for Shellbag Analysis

### ShellBag Explorer:

ShellBag Explorer by Eric Zimmerman is a powerful tool designed specifically for analyzing Shellbag data. It processes the binary data from the USRCLASS.DAT and NTUSER.DAT files and presents it in an easy-to-read format.

### How to use ShellBag Explorer:

1. Open ShellBag Explorer.
2. Load the NTUSER.DAT or USRCLASS.DAT file from the user directory (`C:\Users\<Username>\`).
3. The tool will automatically parse the data and display folder view settings, MRU folders, and access timestamps.

Or load active registry:

![error](/images/shell_item_pic/shellbags_explorer.png)

Tools like SBECmd.exe by Eric Zimmerman can be used to analyze shellbag data from the USRCLASS.DAT and NTUSER.DAT files. For example:
`SBECmd.exe -f "E:\Users\UserName\AppData\Local\Microsoft\Windows\UsrClass.dat" –csv c:\report\`
`SBECmd.exe -f "E:\Users\UserName\NTUSER.dat" –csv c:\report\`
These commands provide detailed information on BagPath, Slot, NodeSlot, MRUPosition.

# Recent Documents (LNK)

Windows automatically creates these shortcuts when the user open, uses or creates a file in:

* Win7-Win10: `C:\Users\\AppData\Roaming\Microsoft\Windows\Recent\`
* Office: `C:\Users\\AppData\Roaming\Microsoft\Office\Recent\`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU`

When a folder is created, a link to the folder, to the parent folder, and the grandparent folder is also created.
To inspect these files, you can use LinkParser.

In this tools you will find 2 sets of timestamps:

* First Set:
  1. FileModifiedDate
  2. FileAccessDate
  3. FileCreationDate
* Second Set:
  1. LinkModifiedDate
  2. LinkAccessDate
  3. LinkCreationDate.

## LinkParser Tool

For analyzing .LNK files (shortcuts), LinkParser helps extract information about recently accessed files. LNK files contain two sets of timestamps, revealing both the original file’s activity and the creation time of the shortcut itself.
How to use LinkParser:

1. Run LinkParser on a directory containing LNK files:
   `LECmd.exe -d C:\Users\Username\Desktop\LNKs --csv C:\Users\Username\Desktop\Report.csv`
2. The tool will generate a CSV file containing details such as FileModifiedDate, FileAccessDate, and FileCreationDate for both the link and the original file.

![error](/images/shell_item_pic/lecmde.png)

The first set of timestamp references the timestamps of the link file itself. The second set references the timestamps of the linked file.

You can get the same information running the Windows CLI tool: LECmd.exe
`LECmd.exe -d C:\Users\student\Desktop\LNKs --csv C:\Users\student\Desktop\LNKs`
In this case, the information is going to be saved inside a CSV file.

# JumpList

These are the recent files indicated in the application. It’s the list of recent files used by an application that you can access on each application. They can be created automatically or be custom.

The jumplists created automatically are stored in `C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\`.

The custom jumplists are stor...