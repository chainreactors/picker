---
title: Quickpost: emldump Bulk Extraction
url: https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/
source: Didier Stevens
date: 2025-06-06
fetch_date: 2025-10-06T22:52:11.778581
---

# Quickpost: emldump Bulk Extraction

# [Didier Stevens](https://blog.didierstevens.com/)

## Thursday 5 June 2025

### Quickpost: emldump Bulk Extraction

Filed under: [Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 0:00

A reader asked about bulk extraction of email attachments with emldump.py

If you want to extract all attachments and write them to disk, you can use the following command:

```
emldump.py --jsonoutput sample.eml | myjson-filter.py -W hashvir
```

This command will produce a MyJSON data structure will the content and metadata of all parts (not only attachments, also the different bodies) and save the parts to disk with filenames formatted as the sha256 hash of the content and the extension .vir.

You can then run the desired analysis commands on the files written to disk.

But you can also run a command directly on the items, without writing them to disk. Here is an example of such a command:

```
emldump.py --jsonoutput sample.eml | myjson-filter.py -r "cmd.exe /c oledump.py"
```

This command will start a oledump.py command for each part in the multipart document, and provide the content of each part via stdout.

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/06/05/quickpost-emldump-bulk-extraction/trackback/)

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
  + [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
  + [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [My Software](https://blog.didierstevens.com/my-software/)
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
  + [Spam](https://blog.didierstevens.com/category/spam/)
  + [technology](https://blog.didierstevens.com/category/technology/)
  + [UltraEdit](https://blog.didierstevens.com/category/ultraedit/)
  + [Uncategorized](https://blog.didierstevens.com/category/uncategorized/)
  + [Update](https://blog.didierstevens.com/category/update/)
 ...