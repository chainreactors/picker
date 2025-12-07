---
title: Quickpost: USB-C Rechargeable Batteries
url: https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/
source: Didier Stevens
date: 2025-12-06
fetch_date: 2025-12-07T03:25:49.197128
---

# Quickpost: USB-C Rechargeable Batteries

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 6 December 2025

### Quickpost: USB-C Rechargeable Batteries

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/),[Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 10:52

I discovered USB-C rechargeable batteries, and bought a set of AA and AAA batteries.

They have a USB-C connector for recharging, so you don’t need a separate charger like you do for NiMH batteries.

![](https://blog.didierstevens.com/wp-content/uploads/2025/11/20251205-180451.png)

This post is not a full blog post, but more a collection of lab notes.

These USB-C batteries deliver 1,5 Volt (unlike NiMH batteries that deliver 1,3 Volt). And during discharge tests, I noticed that the voltage almost doesn’t change. So not only must they have battery charger electronics inside, but also converter electronics that deliver a constant voltage. Probably something like a [switching-mode power supply](https://en.wikipedia.org/wiki/Switched-mode_power_supply) circuit, because when I look at the ripple of the voltage with an oscilloscope, I see a pattern that makes me think of a switching-mode power supply:

![](https://blog.didierstevens.com/wp-content/uploads/2025/11/sds00003.png)

That’s for a AA battery that delivers power to an electronic load that draws 0,100 A current:

![](https://blog.didierstevens.com/wp-content/uploads/2025/11/image.png)

The ripple could also come from the electronic load itself, or some electronic noise source in my lab. So to rule that out, I discharged an alkaline battery and got this:

![](https://blog.didierstevens.com/wp-content/uploads/2025/11/sds00005.png)

This is a different pattern and it repeats with a different frequency, to the ripple we saw in the first scope picture must come from the battery.

I also did measurements with a spectrum analyzer:

![](https://blog.didierstevens.com/wp-content/uploads/2025/12/png4.png)

Here you can see a peak (and its harmonics) around 1,20 MHz.

That too comes from the battery, as these peaks do not appear with an alkaline battery:

![](https://blog.didierstevens.com/wp-content/uploads/2025/12/png5.png)

In the picture of the electronic load screen, one can see 1493 mWh: that’s for the discharge of an AA battery at 0,100 A until the voltage reaches 0,5 V. 1493 is far less than the 3400 mWh printed in a large font on each battery.

I did a series of tests with my AA (0,100 A discharge current) and AAA (0,025 A discharge current) batteries, and on average I get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Type | Measured output (mWh) | Advertized output | Measured input (mWh) | RTE |
| AA | 1527 | 3400 | 2114 | 72% |
| AAA | 478 | 1200 | 754 | 63% |

Unfortunately, these batteries deliver far less electrical energy than advertized.

For comparison, I also discharged an fresh alkaline AAA battery and got 1380 mWh out of it.

![](https://blog.didierstevens.com/wp-content/uploads/2025/12/image.png)

I created a discharge graph for a USB-C rechargeable AA battery:

![](https://blog.didierstevens.com/wp-content/uploads/2025/11/2025-11-30-9-3-57-ebc-a20.png)

During more than 9 hours, the voltage stays around 1,45 V (for a 0,100 A discharge current). Then it abruptly drops to 1,05 V, and then 0 V.

Charging the AA batteries requires 2114 mWh on average, the AAA batteries require 754 mWh. This is also far less than the advertized capacity. This allowed me to calculate the Round Trip Efficiency (RTE) in the table above.

Despite the discrepancy in capacity, these batteries have advantages too:

* the nominal voltage is 1,5 Volt
* the voltage curve remains (mostly) flat while discharging
* their chemistry doesn’t result in battery leaks that corrode your electronics
* you don’t need a battery charger

Disadvantages:

* far less capacity than advertized
* very abrupt voltage drop when fully discharged
* they can’t negotiate power with a USB charger (you can’t charge them with a USB-C to USB-C cable, you must use a USB-A to USB-C cable like the one included)
* some electronic noise because of the switching power supply

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/12/06/quickpost-usb-c-rechargeable-batteries/trackback/)

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
  + [Quickpost: USB-C Rechargeable Bat...