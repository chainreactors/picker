---
title: NetLlix - A Project Created With An Aim To Emulate And Test Exfiltration Of Data Over Different Network Protocols
url: https://buaq.net/go-141025.html
source: unSafe.sh - 不安全
date: 2022-12-23
fetch_date: 2025-10-04T02:18:06.899149
---

# NetLlix - A Project Created With An Aim To Emulate And Test Exfiltration Of Data Over Different Network Protocols

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

![](https://8aqnet.cdn.bcebos.com/53cdb1fea3a2eb5e8075bb0d2cac2355.jpg)

NetLlix - A Project Created With An Aim To Emulate And Test Exfiltration Of Data Over Different Network Protocols

A project created with an aim to emulate and test exfiltration of data over different networ
*2022-12-22 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-141025.htm)
阅读量:28
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjQVmCOTrFL3yFw1QPeOOS68lqEpC0X-G8dny_A9DXerl4SMMiZ_drJsnGvpthAmjJ30nczKPi0EteB6Fqi25kCkkhx3OdQl5438luYuvdLB47o0vZtW4WQKqtsJtqoNDuyJcmWI9SuBNSUvuDuDhiihieMCTHNQHmBV-KscLid1LdakuNYKXdktupjKg=w640-h210)](https://blogger.googleusercontent.com/img/a/AVvXsEjQVmCOTrFL3yFw1QPeOOS68lqEpC0X-G8dny_A9DXerl4SMMiZ_drJsnGvpthAmjJ30nczKPi0EteB6Fqi25kCkkhx3OdQl5438luYuvdLB47o0vZtW4WQKqtsJtqoNDuyJcmWI9SuBNSUvuDuDhiihieMCTHNQHmBV-KscLid1LdakuNYKXdktupjKg)

A project created with an aim to emulate and test [exfiltration](https://www.kitploit.com/search/label/Exfiltration "exfiltration") of data over different network protocols. The [emulation](https://www.kitploit.com/search/label/Emulation "emulation") is performed w/o the usage of native API's. This will help [blue teams](https://www.kitploit.com/search/label/Blue%20Teams "blue teams") write correlation rules to detect any type of C2 communication or data exfiltration.

Currently, this project can help generate HTTP/HTTPS traffic (both GET and POST) using the below metioned progamming/scripting languages:

* CNet/WebClient: Developed in CLang to generate network traffic using the well know WIN32 API's (WININET & WINHTTP) and raw socket programming.
* HashNet/WebClient: A C# binary to generate network traffic using .NET class like HttpClient, WebRequest and raw sockets.
* PowerNet/WebClient: [PowerShell](https://www.kitploit.com/search/label/PowerShell "PowerShell") [scripts](https://www.kitploit.com/search/label/Scripts "scripts") to generate network traffic using socket programming.

### Usage:

Download the latest ZIP from realease.

#### Running the server:

* With SSl: `python3 HTTP-S-EXFIL.py ssl`
* Without SSL: `python3 HTTP-S-EXFIL.py`

#### Running the client:

* CNet - `CNet.exe <Server-IP-ADDRESS>` - Select any option
* HashNet - `ChashNet.exe <Server-IP-ADDRESS>` - Select any option
* PowerNet - `.\PowerHttp.ps1 -ip <Server-IP-ADDRESS> -port <80/443> -method <GET/POST>`

NetLlix - A Project Created With An Aim To Emulate And Test Exfiltration Of Data Over Different Network Protocols
![NetLlix - A Project Created With An Aim To Emulate And Test Exfiltration Of Data Over Different Network Protocols](https://blogger.googleusercontent.com/img/a/AVvXsEjQVmCOTrFL3yFw1QPeOOS68lqEpC0X-G8dny_A9DXerl4SMMiZ_drJsnGvpthAmjJ30nczKPi0EteB6Fqi25kCkkhx3OdQl5438luYuvdLB47o0vZtW4WQKqtsJtqoNDuyJcmWI9SuBNSUvuDuDhiihieMCTHNQHmBV-KscLid1LdakuNYKXdktupjKg=s72-w640-c-h210)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/netllix-project-created-with-aim-to.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)