---
title: The Making Of: qa-squeaky-toys.docm
url: https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/
source: Didier Stevens
date: 2022-10-29
fetch_date: 2025-10-03T21:13:04.879027
---

# The Making Of: qa-squeaky-toys.docm

# [Didier Stevens](https://blog.didierstevens.com/)

## Friday 28 October 2022

### The Making Of: qa-squeaky-toys.docm

Filed under: [Hacking](https://blog.didierstevens.com/category/hacking/) — Didier Stevens @ 0:00

qa-squeaky-toys.docm is a challenge I made for [CSCBE 2022](https://www.cybersecuritychallenge.be/).

It’s a Word document with VBA code. But the VBA code has been “cleaned” by an anti-virus.

I was inspired by a real maldoc cleaned by a real anti-virus: “[Maldoc Cleaned by Anti-Virus](https://isc.sans.edu/forums/diary/Maldoc%2BCleaned%2Bby%2BAntiVirus/28460/)“.

Here is how I made this [challenge](https://github.com/DidierStevens/FalsePositives/blob/master/DST_CSC_2022_Challenge_extra.zip).

I created a .docm file with the following vba code:

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-225152.png)

I extracted the vbaProject.bin file from the OOXML file (.docm).

First, I removed all the compiled VBA code from stream 3. -s 3c selects the compiled code stored in VBA stream 3.

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-225332.png)

I open a copy of vbaProject.bin with a binary editor, and search for the bytes of the compiled code. And I set them all to 0x00.

Then at position 0x40 inside that stream, I write this ASCII test: “Cleaned by your favorite anti-virus!”.

Next I will shorten the compressed VBA source code. This is the compressed VBA source code (selected with 3v):

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-225759.png)

Value F4B0 is a little-endian integer: 0xB0F4. B are some flags, F4 is the length of the chunk of compressed VBA code. F4 hexadecimal is 244 decimal. I shorten this by 206 bytes. Thus I replace F4 with 26 (with a binary editor).

The result is that now, only the first line is readable, followed by some gibberish:

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-230441.png)

And to get rid of the gibberisch, I also shorten the length of the stream. It is 1380 bytes long:

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-230543.png)

That’s 64 05 00 00 (representation for a 32-bit little-endian unsigned integer).

I subtract 204, thus 1380 – 204 = 1176. Or 98 04 00 00. I use again the binary editor to make this change.

Result:

![](https://blog.didierstevens.com/wp-content/uploads/2022/10/20221027-230956.png)

How did I find the values to subtract? Educated guessing and trial and error. Why 2 different subtractions? Because that was also the case in the original sample that inspired me.

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/feed/) [TrackBack URI](https://blog.didierstevens.com/2022/10/28/the-making-of-qa-squeaky-toys-docm/trackback/)

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
  + [My Software](https://blog.didierste...