---
title: New Tool: dns-pydivert.py
url: https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/
source: Didier Stevens
date: 2022-12-27
fetch_date: 2025-10-04T02:32:41.117989
---

# New Tool: dns-pydivert.py

# [Didier Stevens](https://blog.didierstevens.com/)

## Monday 26 December 2022

### New Tool: dns-pydivert.py

Filed under: [Announcement](https://blog.didierstevens.com/category/announcement/),[My Software](https://blog.didierstevens.com/category/my-software/) — Didier Stevens @ 0:00

dns-pydivert is a tool that uses [WinDivert](https://reqrypt.org/windivert.html), a “user-mode packet capture-and-divert package for Windows” to divert IPv4 DNS packets to and from the machine it is running on.

This tool requires admin rights.

When started, it listens for IPv4 UDP packets with source and/or destination port equal to 53.
When this tools processes its first UDP packet with destination port 53, it considers the source address of this packet as the DNS client’s IPv4 address (e.g., the Windows machine this tool is running on) and the destination address to be the IPv4 address of the DNS server used by the client.
From then on, all IPv4 UDP packets with source or destination port 53 (including that first packet) are altered by the tool.
All IPv4 UDP packets with destination port 53, have their destination address changed to the IPv4 address of the client.
All IPv4 UDP packets with source port 53, have their source address changed to the IPv4 address of the DNS server.

This tool can be used to redirect all DNS IPv4 traffic to the machine itself, where a tool like dnsresolver.py can handle the DNS requests.

![](https://blog.didierstevens.com/wp-content/uploads/2022/12/20221224-100719.png)

Caveats:

* This tool does not handle IPv6.
* This tool does not check if the UDP packets to and/or from port 53 are actual DNS packets.
* This tool ignores DNS traffic over TCP.
* This tool does not handle queries to multiple DNS servers (different IPv4 addresses) correctly.

[dns-pydivert\_V0\_0\_1.zip](https://didierstevens.com/files/software/dns-pydivert_V0_0_1.zip) ([http](http://didierstevens.com/files/software/dns-pydivert_V0_0_1.zip))
MD5: BEAB8F9D180E15B27EB86CBEF7429216
SHA256: 7CB4BA7A4ABC0788AB8CE3F2DD1006DF86AD5D80943A4716FC3E62F1FA2100F6

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/feed/) [TrackBack URI](https://blog.didierstevens.com/2022/12/26/new-tool-dns-pydivert-py/trackback/)

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
  + [Poll](https://blog.didierste...