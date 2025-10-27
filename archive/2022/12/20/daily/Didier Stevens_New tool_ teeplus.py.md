---
title: New tool: teeplus.py
url: https://blog.didierstevens.com/2022/12/19/new-tool-teeplus-py/
source: Didier Stevens
date: 2022-12-20
fetch_date: 2025-10-04T01:58:25.638682
---

# New tool: teeplus.py

# [Didier Stevens](https://blog.didierstevens.com/)

## Monday 19 December 2022

### New tool: teeplus.py

Filed under: [Announcement](https://blog.didierstevens.com/category/announcement/),[My Software](https://blog.didierstevens.com/category/my-software/) — Didier Stevens @ 0:00

This new tool, teeplus.py, is an extension of the [tee command](https://en.wikipedia.org/wiki/Tee_%28command%29).

The tools takes (binary) data from stdin, and sends it to stdout, while also writing the data to a file on disk.

While the tee command requires a filename as argument, teeplus.py takes no arguments (only options).

By default, teeplus.py will write the data to a file on disk, with filename equal to the sha256 of the data and extension .vir.

And it will also log this activity in a log file (teeplus.log by default).

Here is an example.

I run curl with a request to ipify to get my current public IPv4 address:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001419.png)

Then I pipe this output to teeplus.py:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001447.png)

This results in the creation of two files inside the current directory:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001508.png)

The first file it the output of the curl command:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001518.png)

The filename is the SHA256 hash of the data with extension .vir:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-002057.png)

The second file, teeplus.log, is a log file:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001531.png)

Each line in teeplus.log has 4 fields (comma separated):

1. The ISO timestamp when the activity was logged
2. The length in bytes of the data
3. The SHA256 hash of the data
4. An error message (empty string when no error occured)

A line is created for each invocation of the teeplus.py command:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001620.png)

When the IPv4 address changes:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001736.png)

And the command is executed again, a new .vir file is created (since the received data changed):

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001752.png)

And this is reflected in the log file:

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001806.png)
![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-001821.png)

This allows you to create a log of your public IPv4 address, for example (by scheduling this command as a recurrent task).

I use it for monitoring websites, and saving a copy of the HTML page I downloaded. I will explain how in an upcoming blog post.

teeplus.py has a couple of options: you can change the extension of the saved file, and the filename of the log file. And you can also us option -n to prevent the data to be piped to stdout (or you could redirect to /dev/null).

This is something I would do when the teeplus.py command is not followed by another command.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221219-003636.png)
[teeplus\_V0\_0\_1.zip](https://didierstevens.com/files/software/teeplus_V0_0_1.zip) ([http](http://didierstevens.com/files/software/teeplus_V0_0_1.zip))
MD5: 0A3704CD56BD6B3A1FF2B92FD87476FB
SHA256: 9E3CBE7323D83FFC588FD67F7B762F53189391A43EDF465C64BD0E4D8E7E8990

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/12/19/new-tool-teeplus-py/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/12/19/new-tool-teeplus-py/?share=x)

### *Related*

[Comments (1)](https://blog.didierstevens.com/2022/12/19/new-tool-teeplus-py/#comments)

## 1 Comment [»](#postcomment "Leave a comment")

1. […] New tool: teeplus.py […]

   Pingback by [Week 52 – 2022 – This Week In 4n6](http://thisweekin4n6.com/2022/12/25/week-52-2022/) — Sunday 25 December 2022 @ [5:54](#comment-613474)

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
  + [Didier Stevens Labs](https://blog.didierstevens.com/category/didier-stevens-labs/)
  + [Eee PC](https://blog.didierstevens.com/category/eee-pc/)
  + [Elec](ht...