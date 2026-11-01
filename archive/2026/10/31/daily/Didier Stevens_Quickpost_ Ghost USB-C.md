---
title: Quickpost: Ghost USB-C
url: https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/
source: Didier Stevens
date: 2026-10-31
fetch_date: 2026-11-01T08:20:52.451865
---

# Quickpost: Ghost USB-C

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 31 October 2026

### Quickpost: Ghost USB-C

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/),[Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 0:00

You’ve probably encountered devices that are powered via a USB-C connector, but that don’t work when you connect them to a USB-C charger or powerbank. They only work with a USB-A to USB-C cable, not with a USB-C to USB-C cable.

I used to encounter such devices regularly a couple of years ago, but far less nowadays. Until we went on holiday this summer, and my wife used a small portable fan. She connected it to her USB-C charger, and it didn’t work. So I fixed this with a USB-A to USB-C cable plugged into a charger with USB-A connector.

But this got me thinking: surely, there must be a small USB-C adapter that solves this problem? The problem occurs because in the USB-C standard, a power source doesn’t put 5 Volts on VBUS, until it detects there is a device connected that requires power. It detects the presence of such a device because of current flowing between the CC pins and GND. This happens because the device has resistors between the CC lines and GND. And some devices, like this fan, lack these resistors, and thus no power is present on VBUS. While with USB-A, there is always power on VBUS, whether a device is connected or not.

I did find such an adapter:

![](https://blog.didierstevens.com/wp-content/uploads/2026/10/image-3.png)

I has a female and male USB-C connector, and it contains two 5.1 kΩ resistors, one between line CC1 and GND, and the other between line CC2 and GND. This instructs the power source to deliver 5V between the VBUS lines and GND.

The result is that with this adapter, I can power these non-compliant devices with a classic USB-C power source and a classic USB-C cable.

With USB-A, it is clear from the difference in physical connectors, which device is a power source and which device is a power sink. With USB-C, that physical difference is gone. Both connectors on a USB-C cable are physically identical. Furthermore, with USB-C, the same device can adopt the role of a power source or the role of a power sink. For example, a laptop can be charged via its USB-C port (power sink role), and the same laptop can charge your phone via the same USB-C port (not simultaneously, of course). That’s the power source role.

Thus, with USB-C, a device must announce that it requires power before it receives power from a device that can act as a power source. And this fan doesn’t do this.

Be sure to only use this adapter between a power source and a power sink that is not compliant. If you would use this adapter to connect two power sources together, both power sources would energize the VBUS lines and one of the power sources would start to sink power. Power sources are not designed to sink power. Although this adapter turns a non-compliant device into a compliant device, the adapter itself is non-compliant.

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/?share=facebook)
* [Share on X (Opens in new window)
  X](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/feed/) [TrackBack URI](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/trackback/)

### Leave a Reply (comments are moderated)

Comment

Name

Email

Website

Turn on JavaScript to leave a comment.

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
  + [Quickpost: Ghost USB-C](https://blog.didierstevens.com/2026/10/31/quickpost-ghost-usb-c/)
  + ["A Ring Tone That I Cannot Hear" - Twenty Years Later](https://blog.didierstevens.com/2026/10/30/a-ring-tone-that-i-cannot-hear-twenty-years-later/)
  + [Quickpost: WT20 Welding Electrodes & Radiation](https://blog.didierstevens.com/2026/10/31/quickpost-wt20-welding-electrodes-radiation/)
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
...