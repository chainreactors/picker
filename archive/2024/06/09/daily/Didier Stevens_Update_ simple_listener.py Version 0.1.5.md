---
title: Update: simple_listener.py Version 0.1.5
url: https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/
source: Didier Stevens
date: 2024-06-09
fetch_date: 2025-10-06T16:55:58.372720
---

# Update: simple_listener.py Version 0.1.5

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 8 June 2024

### Update: simple\_listener.py Version 0.1.5

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/),[Update](https://blog.didierstevens.com/category/update/) — Didier Stevens @ 0:00

I added IPv6 support to simple\_listener.py.

Although it was not by design, it turned out that simple\_listener.py only works for IPv4. So I made some small changes to add IPv6 support.

When you use dictionary to define your listeners, use THP\_TCP6 and THP\_UDP6 to define TCP IPv6 and UDP IPv6 listeners respectively. The meaning of THP\_TCP and THP\_UDP has not changed, that’s for IPv4 listeners.

When you use port options to define your listeners, use prefix t6: and u6: to define TCP IPv6 and UDP IPv6 listeners respectively. The meaning of t: and u: has not changed, that’s for IPv4 listeners.

And by default, listening takes place on all IPv4 interfaces (0.0.0.0) when IPv4 listeners are defined, and listening takes place on all IPv6 interfaces (::) when IPv6 listeners are defined. That’s governed by option -a –address’ default value 0.0.0.0,::.

To explicitly specify an interface with option -a, you will need to provide an IPv4 address and an IPv6 address separated by a comma.

[simple\_listener\_v0\_1\_5.zip](https://didierstevens.com/files/software/simple_listener_v0_1_5.zip) ([http](http://didierstevens.com/files/software/simple_listener_v0_1_5.zip))
MD5: 3FAC80E7D6E3CE71AD4276125AD080E8
SHA256: BA716A27401DB4A76D3FE826A21BA4F7C74DC26AF4B96EA965D5E85517F94214

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/06/08/update-simple_listener-py-version-0-1-5/trackback/)

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
  + [Quickpost: No Escape From PDF](https://blog.didierstevens.com/2010/06/29/quickpost-no-escape-from-pdf/)
  + [Escape From PDF](https://blog.didierstevens.com/2010/03/29/escape-from-pdf/)
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
  + [Shellcode](https://blog.didierstevens.com/category/shellc...