---
title: ABB Cylon FLXeon 9.3.4 Default Credentials
url: https://cxsecurity.com/issue/WLB-2025020007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-14
fetch_date: 2025-10-06T20:32:31.454291
---

# ABB Cylon FLXeon 9.3.4 Default Credentials

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
|  |  | |  | | --- | | **ABB Cylon FLXeon 9.3.4 Default Credentials** **2025.02.13**  Credit:  **[Gjoko 'LiquidWorm' Krstic](https://cxsecurity.com/author/Gjoko%2B%26%23039%3BLiquidWorm%26%23039%3B%2BKrstic/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

ABB Cylon FLXeon 9.3.4 Default Credentials
Vendor: ABB Ltd.
Product web page: https://www.global.abb
Affected version: FLXeon Series (FBXi Series, FBTi Series, FBVi Series)
CBX Series (FLX Series)
CBT Series
CBV Series
ABB UC32 Series Main Plant Controllers (Cylon's UnitronUC32.xx)
Firmware: <=9.3.4
Summary: BACnet® Smart Building Controllers. ABB's BACnet portfolio features a
series of BACnet® IP and BACnet MS/TP field controllers for ASPECT® and INTEGRA™
building management solutions. ABB BACnet controllers are designed for intelligent
control of HVAC equipment such as central plant, boilers, chillers, cooling towers,
heat pump systems, air handling units (constant volume, variable air volume, and
multi-zone), rooftop units, electrical systems such as lighting control, variable
frequency drives and metering.
The FLXeon Controller Series uses BACnet/IP standards to deliver unprecedented
connectivity and open integration for your building automation systems. It's scalable,
and modular, allowing you to control a diverse range of HVAC functions.
Desc: The ABB Cylon FLXeon BACnet controller uses a weak set of default administrative
credentials that can be guessed in remote password attacks and gain full control of
the system.
Tested on: Linux Kernel 5.4.27
Linux Kernel 4.15.13
NodeJS/8.4.0
Express
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2025-5919
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2025-5919.php
21.04.2024
--
$ cat project
P R O J E C T
.|
| |
|'| .\_\_\_\_\_
\_\_\_ | | |. |' .---"|
\_ .-' '-. | | .--'| || | \_| |
.-'| \_.| | || '-\_\_ | | | || |
|' | |. | || | | | | || |
\_\_\_\_| '-' ' "" '-' '-.' '` |\_\_\_\_
$ cat cyloncreds.txt
admin:cylonctl
cxpro:siteguide
UC32Net:CylonCtl

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020007)

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