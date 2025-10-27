---
title: Quickpost: Testing The Capacity Of My New Power Bank
url: https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/
source: Didier Stevens
date: 2025-04-17
fetch_date: 2025-10-06T22:04:44.323736
---

# Quickpost: Testing The Capacity Of My New Power Bank

# [Didier Stevens](https://blog.didierstevens.com/)

## Wednesday 16 April 2025

### Quickpost: Testing The Capacity Of My New Power Bank

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/),[Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 0:00

I bought a new power bank (Anker PowerCore 533, capacity 10.000 mAh 36 Wh, 30 Watt Power Delivery) and did some tests that I’m summarizing here.

Charging it with a generic USB C charger capable of delivering 20 W PD required 46,979 Wh. That’s measured on the 230V side, thus including the loss in the charger.

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250407-171213.png)

Charging it with a Anker 737 Charger (GaNPrime 120W) required 45,515 Wh.

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250409-213724.png)

Discharging the power bank via the USB A port connected to an electronic load gave me:

* 30,970 Wh (6516 mAh ) when drawing 0,5A
* 29,362 Wh (6523 mAh) when drawing 1,0A

30 Wh compared to 36 Wh (the advertised capacity of the power bank) is 83,33%, which is much better than what Anker [estimates](https://support.anker.com/s/article/Why-does-the-power-bank-discharge-quickly-when-charging-other-devices) you can get out of a power bank (60% to 70%).

As I couldn’t get more than 1,0A out of the power bank via the USB A port, I used the USB C port with a trigger module to deliver 20,0V.

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-205104.png)

The electronic load drew 1,250A and measured around 18,6V, or 23,25W. I got 29,020 Wh (1557 mAh) out of it.

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-205502.png)

The power bank became hot while getting completely drained at 23W:

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-205716.png)

You can see the outline of the cells and the electronic circuit (it’s the hottest: white).

I couldn’t immediately recharge my power bank after that, I had to let it cool down (“Let the power bank cool down before use”):

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-205935.png)

I also tried to get more out of the power bank by drawing 1,5A at 18,55V or 27,82W (advertized maximum is 30W).

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-210434.png)

But after 34 minutes (delivering 15,670 Wh) it stopped delivering power and displayed the following message (“Use after protection removal”):

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-210634.png)

I guess that’s the overcurrent protection kicking in. I’m not sure why this happened, as the electronic load was in constant current mode.

I had to disconnect the cable to use the power bank again.

And finally, this power bank is capable of trickle charging: delivering a very low current for about two hours. You enable this mode by pushing the button twice.

I configured the electronic load to draw a really low current of 0,005A (it measured 0,003A) from the USB A port and it delivered 0,032 Wh (6 mAh) over a period of 2:01:05 after which it shut down automatically (as advertized).

![](https://blog.didierstevens.com/wp-content/uploads/2025/04/20250415-211150.png)

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/04/16/quickpost-testing-the-capacity-of-my-new-power-bank/trackback/)

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
  + [Certification](h...