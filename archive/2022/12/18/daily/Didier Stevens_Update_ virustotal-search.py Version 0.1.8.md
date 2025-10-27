---
title: Update: virustotal-search.py Version 0.1.8
url: https://blog.didierstevens.com/2022/12/17/update-virustotal-search-py-version-0-1-8/
source: Didier Stevens
date: 2022-12-18
fetch_date: 2025-10-04T01:51:34.521633
---

# Update: virustotal-search.py Version 0.1.8

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 17 December 2022

### Update: virustotal-search.py Version 0.1.8

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/),[Update](https://blog.didierstevens.com/category/update/) — Didier Stevens @ 0:00

This update to virustotal-search brings new options:

1. -D don’t send queries to VT, just use the local database
2. –sleep before starting: provide an integer with suffix s (seconds), m (minutes), h (hours) or d (days). Or provide a local time: 01:00:00

[virustotal-search\_V0\_1\_8.zip](https://didierstevens.com/files/software/virustotal-search_V0_1_8.zip) ([http](http://didierstevens.com/files/software/virustotal-search_V0_1_8.zip))
MD5: 69A4504E06E97585EDBA4BBD60EAC36C
SHA256: 16FA2F9748959A88BE38B4A2FF006FC658FB4FF8932F3EC2E2568F48EB9FAE85

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/12/17/update-virustotal-search-py-version-0-1-8/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/12/17/update-virustotal-search-py-version-0-1-8/?share=x)

### *Related*

[Comments (3)](https://blog.didierstevens.com/2022/12/17/update-virustotal-search-py-version-0-1-8/#comments)

## 3 Comments [»](#postcomment "Leave a comment")

1. […] Update: virustotal-search.py Version 0.1.8 […]

   Pingback by [Week 51 – 2022 – This Week In 4n6](http://thisweekin4n6.com/2022/12/18/week-51-2022/) — Sunday 18 December 2022 @ [11:17](#comment-613203)
2. A suggestion for a future update. The Virus Total api limits reset at the beginning of each hour. If you reach your hourly limit, restart processing when the new hour begins instead of 60 minutes from when you reached the hourly API limit. This would greatly speed up in bulk checking, for example if you reach your API limit currently at 2.50pm it wont auto restart until 3.50pm. Basing the restart on the new hour means you only have to wait 10 minutes – or maybe give a 5 minute leeway, restarting at 05min into the new hour.

   Comment by Anonymous — Wednesday 14 August 2024 @ [8:55](#comment-629152)
3. I have not yet observed this. What type of account do you use?

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Thursday 29 August 2024 @ [8:24](#comment-629192)

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
  + [Elec](https://blog.didierstevens.com/category/elec/)
  + [Encryption](https://blog.didierstevens.com/category/encryption/)
  + [Entertainment](https://blog.didierstevens.com/category/entertainment/)
  + [Fellow Bloggers](https://blog.didierstevens.com/category/fellow-bloggers/)
  + [Forensics](https://blog.didierstevens.com/category/forensics/)
  + [Hacking](https://blog.didierstevens.com/category/hacking/)
  + [Hardware](https://blog.didierstevens.com/category/hardware/)
  + [maldoc](https://blog.didierstevens.com/category/maldoc/)
  + [Malware](https://blog.didierstevens.com/category/malware/)
  + [My Software](https://blog.didierstevens.com/category/my-software/)
  + [N800](https://blog.didierstevens.com/category/n800/)
  + [Networking](https://blog.didierstevens.com/category/networking/)
  + [Nonsense](https://blog.didierstevens.com/category/nonsense/)
  + [nslu2](https://blog.didierstevens.com/category/nslu2/)
  + [OSX](https://blog.didierstevens.com/category/osx/)
  + [PDF](https://blog.didierstevens.com/category/pdf/)
  + [Personal](https://blog.didierstevens.com/category/personal/)
  + [Physical Security](https://blog.didierstevens.com/category/physical-security/)
  + [Poll](https://blog.didierstevens.com/category/poll/)
  + [Puzzle](https://blog.didierstevens.com/category/puzzle/)
  + [Quickpost](https://blog.didierstevens.com/category/quickpost/)
  + [Release](https://blog.didierstevens.com/category/release/)
  + [Reverse Engineering](https://blog.didierstevens.com/category/reverse-engineering/)
  + [RFID](https://blog.didierstevens.com/category/rfid/)
  + [Shellcode](https://blog.didierstevens.com/category/shellcode/)
  + [smart card](https://blog.didierstevens.com/category/smart-card/)
  + [Spam](https://blog.didierstevens.com/category/sp...