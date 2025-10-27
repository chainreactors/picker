---
title: Wireshark Lua Fixed Field Length Dissector: fl-dissector
url: https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/
source: Didier Stevens
date: 2024-05-21
fetch_date: 2025-10-06T16:50:59.857151
---

# Wireshark Lua Fixed Field Length Dissector: fl-dissector

# [Didier Stevens](https://blog.didierstevens.com/)

## Monday 20 May 2024

### Wireshark Lua Fixed Field Length Dissector: fl-dissector

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/),[Networking](https://blog.didierstevens.com/category/networking/),[Reverse Engineering](https://blog.didierstevens.com/category/reverse-engineering/),[Wireshark](https://blog.didierstevens.com/category/wireshark/) — Didier Stevens @ 11:58

I developed a Wireshark dissector (fl-dissector) in Lua to dissect TCP protocols with fixed field lengths. The dissector is controlled through protocol preferences and Lua script arguments.

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-130128.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-130150.png)

The port number is an essential argument, if you don’t provide it, default port number 1234 will be used.

Example for TCP port 50500: -X lua\_script1:port:50500.

The protocol name (default fldissector) can be changed with argument protocolname: -X lua\_script1:protocolname:firmware.

The length of the fields can be changed via the protocol preferences dialog:

![](https://blog.didierstevens.com/wp-content/uploads/2024/05/20240520-132450.png)

Field lengths are separated by a comma.

Field lengths can also be defined by Lua script argument fieldlengths, like this: -X lua\_script1:fieldlengths:1,1,2:L,2:L.

When field lengths are defined via a Lua script argument, this argument takes precedence over the settings in the protocol preferences dialog. fieldlengths can also specify the field type, but only via Lua script argument, not via protocol preferences (this is due to a Lua script dissector design limitation: protocol preferences can only be read after dissector initialization, and fields have to be defined before dissector initialization). Field types are defined like this: length:type. Type can be L (or l) and defines a little-endian integer, or B (or b) and defines a big-endian integer. The length of the integer (8, 16, 24 or 32 its) is inferred from the fieldlength. Fields without a defined type ate byte fields.

The length of the last field is not specified, it contains all the remaining bytes (if any).

Field names are specified with Lua script argument fieldnames: -X lua\_script1:fieldnames:Function,Direction,Counter,DataLength,Data.

[fl\_dissector\_V0\_0\_1.zip](https://didierstevens.com/files/software/fl_dissector_V0_0_1.zip) ([http](http://didierstevens.com/files/software/fl_dissector_V0_0_1.zip))
MD5: F3DDC28F8D470DC4F9037644D3AF919A
SHA256: BF7406BCD36334E326BF4A6650DECD1D955EB4BD9D9563332AA4AE38507B29D4

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/05/20/wireshark-lua-fixed-field-length-dissector-fl-dissector/trackback/)

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
  ...