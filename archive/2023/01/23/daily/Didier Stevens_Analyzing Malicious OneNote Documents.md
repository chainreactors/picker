---
title: Analyzing Malicious OneNote Documents
url: https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/
source: Didier Stevens
date: 2023-01-23
fetch_date: 2025-10-04T04:35:37.330192
---

# Analyzing Malicious OneNote Documents

# [Didier Stevens](https://blog.didierstevens.com/)

## Sunday 22 January 2023

### Analyzing Malicious OneNote Documents

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/) — Didier Stevens @ 18:09

About a week ago, I [was asked](https://twitter.com/James_inthe_box/status/1613912937491755010) if I had tools for OneNote files.

I don’t, and I had no time to take a closer look.

But last Thursday night, I had some time to take a look. I looked at this [OneNote maldoc sample](https://bazaar.abuse.ch/sample/f408ef3fa89546483ba63f58be3f27a98795655eb4b9b6217cbe302a5ba9d5f7/).

I opened the file in the binary editor I use often ([010 Editor](https://www.sweetscape.com/010editor/)):

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-155955.png)

I expected to see some magic header, a special sequence of byte that would tell me which file type is used. I didn’t see that, but I noticed that the first 16 bytes look random. And they were the same for another sample. So this could be a [GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). GUIDs in Microsoft’s representation are a mix of little- and big-endian hexadecimal integers. That’s why 010 Editor has an entry for GUIDs in its inspector tab:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-160034.png)

This is the GUID represented as a string: {7B5C52E4-D88C-4DA7-AEB1-5378D02996D3}

Looking this up with Google:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-104844.png)

That’s great, Microsoft has a document [[MS-ONESTORE]](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/ae670cd2-4b38-4b24-82d1-87cfb2cc3725) describing this file format.

Unfortunately, I did a quick search but didn’t find a pure Python module to read this file format. Maybe it exists, but I didn’t find it.

Next I tried my pecheck.py tool to locate the executable inside the onenote sample. That worked well:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-104933.png)

At position 0x2aa4, here’s an embedded PE file. Taking a look with the binary editor:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-183421.png)

I see the MZ header, and 36 bytes in front of that, another random looking sequence of 16 bytes. Maybe another GUID:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-183430.png)

{BDE316E7-2665-4511-A4C4-8D4D0B7A9EAC}

A bit of Google search:

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-183710.png)

Turns out that this is a [FileDataStoreObject structure](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/8806fd18-6735-4874-b111-227b83eaac26).

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-183738.png)

So looking for this GUID in any file, one can find (and extract) embedded files. So that’s what I quickly coded using [my Python template for binary files](https://blog.didierstevens.com/my-python-templates/) (there are some issues with this GUID-search method, I’ll address these in an upcoming blog post or video)

![](https://blog.didierstevens.com/wp-content/uploads/2023/01/20230122-185231.png)

A new tool: [onedump.py](https://blog.didierstevens.com/2023/01/22/new-tool-onedump-py/)

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/feed/) [TrackBack URI](https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
  + [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
  + [Overview of Content Published in September](https://blog.didierstevens.com/2025/10/02/overview-of-content-published-in-september-9/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
* ## Categories

  + [.NET](https://blog.didierstevens.com/category/net/)
  + [010 Editor](https://blog.didierstevens.com/category/010-editor/)
  + [Announcement](https://blog.didierstevens.com/category/announcement/)
  + [Arduino](https://blog.didierstevens.com/category/arduino/)
  + [Bash Bunny](https://blog.didierstevens.com/category/bash-bunny/)
  + [Beta](https://blog.didierstevens.com/category/beta/)
  + [bpmtk](https://blog.didierstevens.com/category/bpmtk/)
  + [Certification](https://blog.didierstevens.com/category/certification/)
  + [Didier Stevens Labs](https://bl...