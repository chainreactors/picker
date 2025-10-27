---
title: Update: oledump.py Version 0.0.77
url: https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/
source: Didier Stevens
date: 2024-07-12
fetch_date: 2025-10-06T17:43:37.167936
---

# Update: oledump.py Version 0.0.77

# [Didier Stevens](https://blog.didierstevens.com/)

## Thursday 11 July 2024

### Update: oledump.py Version 0.0.77

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/),[Update](https://blog.didierstevens.com/category/update/) — Didier Stevens @ 19:59

This is an update for plugin plugin\_biff.py.

Protected xls files (workbook protection, sheet protection) are protected with a password, but are not encrypted.

The password is hashed to a 16-bit hash called verifier, such a short hash gives ample opportunity for hash collisions.

I calculated passwords for all possible hash values (32768, or 0x8000) mostly with letters and digits, some with special characters (verifier table). This verifier table is not a rainbow table, because the table contains all possible hash values and a corresponding password.

If a verifier can not be cracked with a provided password list, the password will be taken from the verifier list.

Example: this spreadsheet has a sheet protected with password azeqsdwxc, which is not in the embedded password list (obtained from John The Ripper); thus the password from the verifier table is taken (bbbbhz):

![](https://blog.didierstevens.com/wp-content/uploads/2024/07/20240711-215408.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/07/20240711-215255.png)

Passwords azeqsdwxc and bbbbhz both hash to the same verifier value (0xd9b1), thus there is a hash collision, and both passwords can be used to unprotect the sheet.

[oledump\_V0\_0\_77.zip](https://didierstevens.com/files/software/oledump_V0_0_77.zip) ([http](http://didierstevens.com/files/software/oledump_V0_0_77.zip))
MD5: CC8E3BB7BFA8D6312F8371DADE414EE4
SHA256: 08A097FB2491072043BFD4032BEBC4B2994AEF94B99F3C68EFAEB56004AE7ECE

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/07/11/update-oledump-py-version-0-0-77/trackback/)

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
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Quickpost: The Electric Energy Consumption Of A Wired Doorbell](https://blog.didierstevens.com/2024/11/03/quickpost-the-electric-energy-consumption-of-a-wired-doorbell/)
  + [YARA Rule: Detecting JPEG Exif With eval()](https://blog.didierstevens.com/2015/01/20/yara-rule-detecting-jpeg-exif-with-eval/)
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
  + [Release]...