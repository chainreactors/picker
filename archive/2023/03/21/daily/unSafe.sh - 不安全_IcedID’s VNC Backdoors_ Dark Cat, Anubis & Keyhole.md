---
title: IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole
url: https://buaq.net/go-154409.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:23.984780
---

# IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/dbf66a9d67a0a9c13590f2774881c4d4.jpg)

IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole

IcedID (a.k.a. BokBot) is a popular Trojan who first emerged in 2017 as an Emotet delivery. Orig
*2023-3-20 22:45:0
Author: [blog.nviso.eu(查看原文)](/jump-154409.htm)
阅读量:57
收藏*

---

IcedID (a.k.a. BokBot) is a popular Trojan who [first emerged in 2017 as an Emotet delivery](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/). Originally described as a banking Trojan, IcedID shifted its focus to embrace the extortion/ransom trend and nowadays acts as an initial access broker mostly delivered through malspam campaigns. Over the last few years, [IcedID has commonly been seen delivering Cobalt Strike prior to a multitude of ransomware strains](https://thedfirreport.com/category/icedid/) such as Conti or REvil.

IcedID itself is composed of multiple modules, one of which is a poorly documented VNC backdoor ([Virtual Network Computing](https://en.wikipedia.org/wiki/Virtual_Network_Computing)) acting as a cross-platform remote desktop solution. Existence of this module (branded “HDESK” or “HDESK bot”) is just partially mentioned by [Malwarebytes (2017)](https://www.malwarebytes.com/blog/news/2019/12/new-version-of-icedid-trojan-uses-steganographic-payloads) and [Kaspersky (2021)](https://securelist.com/trickbot-module-descriptions/104603/) while its usage has been widely observed and [occasionally vulgarized](https://isc.sans.edu/diary/rss/29210) as “Dark VNC”.

As part of our research efforts, NVISO has been analyzing IcedID’s command & control communications. **In this blog-post we will share insights into IcedID’s VNC backdoor(s) as seen from an attacker’s perspective**, insights we obtained by extracting and reassembling VNC ([RFC6143](https://www.rfc-editor.org/rfc/rfc6143)) traffic embedded within private and [public captures published by Brad Duncan](https://malware-traffic-analysis.net/index.html).

In this post we introduce the three variants we observed as well as their capabilities: [Dark Cat](#dark-cat-vnc), [Anubis](#anubis-vnc) and [Keyhole](#keyhole-vnc). We’ll follow by exposing [common techniques employed by the operators](#modus-operandi) before revealing [information they leaked through their clipboard data](#clipboard-leaks).

During our analysis of both public and private IcedID network captures, we identified 3 VNC backdoor variants, all part of the HDESK strain. These backdoors are typically activated during the final initial-access stages to initiate hands-on-keyboard activity. Supposedly short for “Hidden Desktop”, HDESK leverages Windows features allowing the backdoor to create a hidden desktop environment not visible to the compromised user. Within this hidden environment, the threat actors can start leveraging the user interface to perform regular tasks such as web browsing, reading mails in Outlook or executing commands through the Command Prompt and PowerShell.

We believe with medium confidence that these backdoors are not exclusive to IcedID as we occasionally observed their usage alongside network traffic attributed by third-party vendors to other access-broker families.

## Dark Cat VNC

The “Dark Cat VNC” variant was first observed in November 2021 and is believed to be the named releases `v1.1.2` and `v1.1.3`. Its usage was still extensively observed by the end of 2022. Upon initial access, the home screen presents the operator with multiple options to create new sessions alongside backdoor metrics such as idle time or lock state.

![Figure 1: The Dark Cat VNC interface.](https://blog.nviso.eu/wp-content/uploads/2023/03/001200.2021-11-05T17-16-21987.jpeg)

### User Session

Figure 2: A Dark Cat `USER` session.

The `USER` session exists in three variations (`read`, standard and `black`) which allows the operator to switch the VNC view to the user’s visible desktop.

### HDESK Session

The `HDESK` session exists in three variations as well: standard, `Tmp` and `NM` (also called `bot`). This session type causes the backdoor to create a new hidden desktop not visible to the compromised user.

Based on the activity we observed, the `HDESK` sessions are (understandably) preferred by the operators.

Figure 3: A Dark Cat `HDESK` session.

As `HDESK` sessions by default do not benefit from Windows’s built-in UI, operators are presented with an alternative start-menu to launch common programs. In Dark Cat these are Chrome, Firefox, Internet Explorer, Outlook, Command Prompt, Run and the Task Manager. A Windows Shell button is also foreseen which we believe, if used, will spawn the regular Windows UI most of the users are used to. Starting with Dark Cat `v1.1.3` Edge Chromium furthermore joins the list of available software.

![Figure 4: The Dark Cat HDESK session interface.](https://blog.nviso.eu/wp-content/uploads/2023/03/001859.2021-11-05T17-16-28071.jpeg)

Figure 4: The Dark Cat `HDESK` session interface.

Besides the alternate start-menu, operators can access some settings using the top-left orange icon which includes:

* Defining the hidden windows’ sizes.
* Defining the Chrome profile to use (lite or not).
* Deleting the browser’s profile(s).
* Killing the child process(es).

Figure 5: The Dark Cat `HDESK` settings interface.

### WebCam Session

The `WebCam` sessions exist in three variations. While we were unable to capture its usage (honeypots lack webcams and operators do not attempt to use this session kind), its presence suggests IcedID’s VNC backdoors are capable of capturing compromised devices’ webcam feeds.

## Anubis VNC

The “Anubis VNC” variant was first observed in January 2022 and is believed to be the named release `v1.2.0`. Its usage was last observed in Q3 2022. No capability differences were observed between Anubis and Dark Cat `v1.1.3`.

![Figure 6: The Anubis VNC interface.](https://blog.nviso.eu/wp-content/uploads/2023/03/000872.2022-01-12T17-19-20433.jpeg)

Figure 6: The Anubis VNC interface.

## KEYHOLE VNC

The “KEYHOLE VNC” variant was first observed in October 2022 and is believed to be the named releases `v1.3` as well as `v2.1`. Its usage was observed as recently as Q1 2023.

### Grayscale

The first major change observed within Keyhole is its new color palette capability where operators can pick regular [RGB](https://en.wikipedia.org/wiki/RGB_color_model) (a.k.a. colored) or [Grayscaled](https://en.wikipedia.org/wiki/Grayscale) (a.k.a. black & white) feeds. The actual intend of this feature is unclear as, at least from a network perspective, both RGB and Grayscale consume as many bytes per pixel, resulting in equal performances.

![Figure 7: The Keyhole color palette selector.](https://blog.nviso.eu/wp-content/uploads/2023/03/000582.2022-11-11T17-59-33557.jpeg)

Figure 7: The Keyhole color palette selector.

### HDESK Sessions

Keyhole `v1.3` provides a refreshed start-menu where icons have been updated and options renamed; The once cryptic `Win Shell` option has been rebranded to the `My Computer` option.

![Figure 8: The Keyhole (v1.3) HDESK session interface in gray-scaled color palette.](https://blog.nviso.eu/wp-content/uploads/2023/03/002373.2022-11-11T17-59-54357.jpeg)

Figure 8: The Keyhole (`v1.3`) `HDESK` session interface in gray-scaled color palette.

Later-on, with `v2.1`, Keyhole renamed additional options and introduced the `PowerShell` and `Desktop` options. We assess with low confidence that the `Desktop` option only differs from the `My Computer` option by rendering the background as well, whereas the latter option was only seen generating desktop views without backg...