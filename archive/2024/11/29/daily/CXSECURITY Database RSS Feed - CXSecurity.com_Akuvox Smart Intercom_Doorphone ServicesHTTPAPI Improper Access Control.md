---
title: Akuvox Smart Intercom/Doorphone ServicesHTTPAPI Improper Access Control
url: https://cxsecurity.com/issue/WLB-2024110042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-29
fetch_date: 2025-10-06T19:14:31.013997
---

# Akuvox Smart Intercom/Doorphone ServicesHTTPAPI Improper Access Control

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
|  |  | |  | | --- | | **Akuvox Smart Intercom/Doorphone ServicesHTTPAPI Improper Access Control** **2024.11.28**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Akuvox Smart Intercom/Doorphone ServicesHTTPAPI Improper Access Control
Vendor: The Akuvox Company
Product web page: https://www.akuvox.com
Affected version: Doorphone:
S539
S532
X916
X915
X912
R29
Intercom:
E16C
R20K-2
R20A-2
C313W-2
NS-2
NC-2
NX-2
Firmware: 912.30.1.137
Summary: Vandal-resistant Door Phone for High-end Buildings. Offering
top-of-the-line features, Akuvox X912 is targeted at high-end residential
and commercial projects. With a compact size, it is perfect for buildings
with limited installation space.
Desc: The Akuvox Smart Intercom/Doorphone suffers from an insecure service
API access control. The vulnerability in ServicesHTTPAPI endpoint allows
users with "User" privileges to modify API access settings and configurations.
This improper access control permits privilege escalation, enabling unauthorized
access to administrative functionalities. Exploitation of this issue could
compromise system integrity and lead to unauthorized system modifications.
Tested on: lighttpd/1.4.30
EasyHttpServer
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2024-5862
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2024-5862.php
25.02.2024
--
http://192.168.1.2/#/ServicesHTTPAPI
# user:user

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110042)

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