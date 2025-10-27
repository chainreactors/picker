---
title: Alternate Data Streams &#x3f; Adversary Defense Evasion and Detection &#x5b;Guest Diary&#x5d;, (Wed, May 28th)
url: https://isc.sans.edu/diary/rss/31990
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-30
fetch_date: 2025-10-06T22:35:51.164233
---

# Alternate Data Streams &#x3f; Adversary Defense Evasion and Detection &#x5b;Guest Diary&#x5d;, (Wed, May 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31986)
* [next](/diary/31994)

# [Alternate Data Streams ? Adversary Defense Evasion and Detection [Guest Diary]](/forums/diary/Alternate%2BData%2BStreams%2BAdversary%2BDefense%2BEvasion%2Band%2BDetection%2BGuest%2BDiary/31990/)

**Published**: 2025-05-28. **Last Updated**: 2025-05-29 00:02:44 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Alternate%2BData%2BStreams%2BAdversary%2BDefense%2BEvasion%2Band%2BDetection%2BGuest%2BDiary/31990/#comments)

[This is a Guest Diary by Ehsaan Mavani, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

Adversaries are leveraging alternate data streams to hide malicious data with the intent of evading detection. Numerous different malicious software has been designed to read and write to alternate data streams [[1](https://attack.mitre.org/techniques/T1564/004/)]. To better assist in detecting and responding to cyber threats, it is important that we understand what an alternate data stream is, ways to discretely write to an alternate data stream, and tools that can assist in detecting alternate data streams.

**Alternate Data Stream**

Every file on a Windows NTFS file system has a default unnamed data stream. This is the mainstream which stores the files data and can be easily viewed with File Explorer. Alternate Data Streams are a Microsoft Windows New Technology File System (NTFS) feature which was added to help support Apple’s Hierarchical File System (HFS) [[2](https://www.irongeek.com/i.php?page=security/altds)]. An Alternate Data Stream is different from the default unnamed mainstream. Alternate Data Streams are named and are not visible within File Explorer [3]. This gives us the capability to write data to a known good files alternate data stream. Essentially, we are able to hide malicious or secret files inside of an innocuous file which can’t be seen in File Explorer.

Directories can also have alternate data streams. Unlike files, directories do not have a default data stream. Instead, they have a default directory stream [[3](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/c54dec26-1551-4d3a-a0ea-4fa40f848eb3)].

**Why does this matter?**

Adversaries want to complete their objectives and need to do so in a manner which evades detection. If our defensive tools and processes don’t scrutinize alternate data streams, adversaries are going to take advantage of our defensive blind spots. Sophisticated threat actors have been using alternate data streams to write and read data. Mitre ATT&CK has documented several skilled groups and malicious software that use this technique, categorized by Mitre as T1564.004 [1].

As a case study, the group known as Indrik Spider [[4](https://www.crowdstrike.com/en-us/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)] has been operating the malicious software BitPaymer [4] to launch targeted ransomware campaigns. In 2017, BitPaymer was first identified being used to ransom the U.K.’s National Health Service, demanding 53 bitcoins. Once a computer has been compromised, the BitPaymer malware attempts to run from an alternate data stream. If it is not being run from an alternate data stream, it automatically creates a file and copies itself to the arbitrarily named alternate data stream ‘bin’. The BitPaymer ransomware has netted Indrik Spider $1.5M USD in the first 15 months of operations [4].

**Writing & Reading an Alternate Data Stream**

I created an empty directory and ran the commands below. When I wrote data to a nonexistent files alternate data stream, Windows automatically created the files default mainstream with no data. Windows also created an alternate data stream with the name ‘secret’, which I specified. Alternate data streams can be named using all Unicode characters except for backslash, forward slash, colon, and control character 0x00. A stream name can be no more than 255 characters in length [[5](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/5953f072-b28c-4fbf-ae50-09b0173317b9)].
1. Write data to a text file’s alternate data stream which I named ‘secret’
2. List directory contents. Windows created file.txt’s default data stream with 0 bytes of data. The alternate data stream ‘secret’ is not visible. Viewing the directory contents in File Explorer will also only show file.txt with 0 bytes of data.
3. Using dir /r to display alternate data streams of files. file.txt:secret will not be shown in File Explorer
4. Displays contents of the text file’s main data stream. Nothing is outputted onto the screen because there is no data in file.txt’s main data stream. Opening the file in Notepad.exe will also show an empty file.
5. Explicitly specify the filename and the stream name to read data

![](https://isc.sans.edu/diaryimages/images/Ehsaan_Mavani_Picture1.png)
Figure 1 Writing, reading, and displaying a file alternate data stream

**Executing Alternate Data Streams**

Alternate data streams can be directly executed by many Windows tools [6]. Powershell, rundll32, wmic, wscript, and cscript are some of the tools that are capable of executing binaries in alternate data streams. These are all legitimate tools that are pre-installed on Windows operating systems.

I created an executable that enumerates all files on a victim machine, sending the results to an attacker-controlled web server via URL encoded GET requests. I hid the executable inside of an alternate data stream. The executable was successfully run with wmic.

![](https://isc.sans.edu/diaryimages/images/Ehsaan_Mavani_Picture2.png)
Figure 2 Executing enumerateFiles.exe in GoodFile’s alternate data stream

**Alternate Data Streams in Reserved Names**

There are special reserved names in Microsoft Windows that cannot be used for file names [[7](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)]. CON is one of those unique reserved file names. If you try to create a file with the name CON using File Explorer, Windows will display an error, preventing the creation of the file.

![](https://isc.sans.edu/diaryimages/images/Ehsaan_Mavani_Picture3.png)
Figure 3 Windows error when creating a file with a reserved name in File Explorer

Interestingly, it is possible to circumvent this error and successfully create a file with a reserved name by utilizing special prefixes [[8](http://www.sourceconference.com/publications/bos10pubs/Windows%20File%20Pseudonyms.pptx)]. “\\?\” is a prefix that can be used to tell the Windows API to disable string parsing, sending the string that follows the prefix straight to the file system [[7](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)].

Even more insidious, alternate data streams written to files with reserved names are not visible to directory listings with dir /r unless the prefix “\\?\” is added to the file path. In order to read, write, and delete the file, the prefix “\\?\” must be added to the file path.
1. Write data to the alternate data stream of a file with the reserved name CON. To create this file, the prefix “\\?\” must be included

2. List directory contents with dir /r. The file CON is visible, but the alternate data stream is not visible. If navigating to “C:\Temp\” within File Explorer, this file and the file’s alternate data stream will not be visible.

3. List directory contents with dir /r and the absolute file path of CON with “\\?\” prepended. The alternate data stream is visible. If navigating to “\\?\C:\Temp\” within File Explorer, this file will be visible, but the alternate data stream will not be visible.

![](https://isc.sans.edu/diaryimages/images/...