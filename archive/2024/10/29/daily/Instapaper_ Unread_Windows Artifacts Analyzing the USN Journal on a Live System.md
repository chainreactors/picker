---
title: Windows Artifacts Analyzing the USN Journal on a Live System
url: https://cyberdefnerd.com/2024/10/28/windows-artifacts-analyzing-the-usn-journal-on-a-live-system/
source: Instapaper: Unread
date: 2024-10-29
fetch_date: 2025-10-06T18:55:54.988412
---

# Windows Artifacts Analyzing the USN Journal on a Live System

[Skip to content](#main)

[![CyberDefNerd](https://cyberdefnerd.com/wp-content/uploads/2024/11/cropped-CyberDefNerd__1_-removebg-preview.png)](https://cyberdefnerd.com/)

* [Home](https://cyberdefnerd.com/)
* [Articles](https://cyberdefnerd.com/blog/)
* [Videos](https://cyberdefnerd.com/videos/)
* [About](https://cyberdefnerd.com/tools/)

[Subscribe](https://www.linkedin.com/in/krzysztof-gajewski-537683b9/)

* [Home](https://cyberdefnerd.com/)
* [Articles](https://cyberdefnerd.com/blog/)
* [2024](https://cyberdefnerd.com/2024/)
* [October](https://cyberdefnerd.com/2024/10/)
* [28](https://cyberdefnerd.com/2024/10/28/)
* Windows Artifacts: Analyzing the USN Journal on a Live System

Posted in[Forensics](https://cyberdefnerd.com/category/forensics/)

# Windows Artifacts: Analyzing the USN Journal on a Live System

Posted by

![](https://secure.gravatar.com/avatar/0a65a146cbfa1774e32687e50eabb5aa04bf7d155bec54e8f948e7b6e079a926?s=30&d=mm&r=g)

[Krzysztof Gajewski](https://cyberdefnerd.com/author/krzysiu_rysiu/ "View all posts by Krzysztof Gajewski")
2024-10-28[No Comments](https://cyberdefnerd.com/2024/10/28/windows-artifacts-analyzing-the-usn-journal-on-a-live-system/#respond)

In this article, we will explore how to work with the USN Journal without collecting and parsing the **$UsnJrnl:$J** file. We will not discuss this artifact in details, but we will cover just basisc things and then jump to the meritum. For the sake of this article, I will assume that the reader is already familiar with the USN Journal and uses it on a regular basis.

**Agenda:**
– UsnJrnl – $UsnJrnl:$J
– Fsutil
– fsutil usn queryjournal
– fsutil usn readdata
– fsutil usn readJournal [options]
– fsutil usn enumdata

## 1. UsnJrnl – $UsnJrnl:$J

The **USN Journal** is not stored in a traditional file that you can directly access and open like a regular text file. Instead, it’s part of the NTFS filesystem metadata and is saved as a hidden data stream on the NTFS volume.

```
- C:\$Extend\$UsnJrnl:$J
```

If you have raw access to the system, you can (and to be more prciese you SHOULD) collect that file as a part of your standard forensics collection.

Below is how I accessed it using FTK Imager:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/1-1.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/1-1.png)

($UsnJrnl)

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/2.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/2.png)

($UsnJrnl:$J)

Before we go further, I would like to highlight here a file named **$UsnJrnl:$Max**. I would say that almost all analysts ignore this file, probably because they do not know what information can be extracted from it. This is a mistake, as this file indicates the maximum size of the UsnJrnl file, which may be difficult to determine if you just have the collection, without access to the system. But few years ago, I created a parser for that file, which you can find [here](https://github.com/gajos112/Max-Parser).

Okay, once you have the  **$UsnJrnl:$J** you can parse it -there are multiple diffrent tools, personaly I like this one <https://github.com/PoorBillionaire/USN-Journal-Parser/blob/master/README.rst>, but there is much more. Eric’s tool MFTECmd can parse it as well.

2. Fsutil

But today we will not discuss parsing that artifact; I want to show a way to enumerate the UsnJrnl without making any collections or parsing that file on your forensic system. Why? Well, there may be a situation where you need to connect to a live system to take immediate action, and there isn’t time for a collection. You might not have any tools that allow you raw access to the system, or there could be other reasons why you can’t do it in the usual way.

And to do that, Microsoft provides as a very handy tool named FSUTIL 🙂

**`Fsutil`** is a command-line utility in Windows that provides various file system-related tasks and operations. It allows users to perform functions such as managing volumes, querying file system information, managing NTFS file system features, and more.

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/3.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/3.png)

(fsutil options)

As you can see in the screenshot above, this utility can be used to manage and enumerate multiple different items. Let’s take a look at the USN’s options and start talking about them a little bit more:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/4.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/4.png)

(fsutil usn)

## 3. fsutil usn queryjournal

The first useful argument is `queryjournal`. This command provides several pieces of information, but I believe the most valuable is the maximum size of the USN Journal. By default, on Windows systems, it is set to 32MB. This isn’t much, and I highly recommend increasing this size in your organization. However, if you’re working for clients, you’ll have to work with what’s already available, as it’s usually too late to adjust the size after the fact 🙂

**Command:** fsutil usn queryjournal C:

![](https://cyberdefnerd.com/wp-content/uploads/2024/10/5.png)

The size of the UsnJrnl helps you estimate how far back you can go with the logs. I think it is safe to say that, with the default size, you can typically go back just a few days.

## 4. fsutil usn readdata

Another intresting command is **fsutil usn readdata <filename>**. Let’s take a look at the example below:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/6.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/6.png)

With that command, we were able to find **File Refference** and the most recent **Update Sequence Number** (USN) for a file in question – **C:\users\gajos\downloads\guardian-browser-x64.exe**:

* FileRef# : 0x0000000000000000001400000004d5de
* Usn : 0x00000001175e4ee8

Okay, but what is next?

Now there are two other commands we can use to dig deeper.

## 5. fsutil usn readJournal [options]

The next command I want to talk about is **fsutil usn readJournal**. Below you can find a HELP menu for this command:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/9-1024x251.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/9.png)

(HELP menu )

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/8.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/8.png)

(Source: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn>)

The syntax for this command is straightforward, making it one of the most important tools for a quick review of the **UsnJrnl**.

The simplest way to run it is by specifying the volume pathname and the desired output format. Additionally, you can redirect the output to a file or pipe it into the `FINDSTR` command to filter the results for specific matches you’re looking for.

Below, I am looking for all entires containing **guardian-browser-x64.exe** by piping the output to the `FINDSTR` command :

[![](https://cyberdefnerd.com/wp-content/uploads/2024/10/10-1024x391.png)](https://cyberdefnerd.com/wp-content/uploads/2024/10/10.png)

* Yellow – The name opf the file
* Blue – Timestamp
* Green – File Refference number

In results, I got mutltiple entires. At the begining, we have PREFETCH files for **guardian-browser-x64.exe**, the earliest one is from **2024-10-18**. The file refference number of course does not match to what we found ealrier. Going further, we have and entry for **guardian-browser-x64.exe**, this time the file reffrence number is correct – we found what we were looking for! The intresting thing we found here, is that the creation time points to **2024-10-23**. What does it mean? It means that the PREFETCH files were created, prior to the creation of the exectauble… Does it make sense? Yes it does, it means that EXE was created one more time and we do not have entries for the previous version of that file.

To test one more thing, I will just remove the file by putting it to the ...