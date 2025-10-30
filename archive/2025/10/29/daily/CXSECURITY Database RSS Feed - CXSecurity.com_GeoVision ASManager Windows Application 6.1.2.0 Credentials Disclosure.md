---
title: GeoVision ASManager Windows Application 6.1.2.0 Credentials Disclosure
url: https://cxsecurity.com/issue/WLB-2025100016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-10-29
fetch_date: 2025-10-30T03:10:21.810687
---

# GeoVision ASManager Windows Application 6.1.2.0 Credentials Disclosure

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
|  |  | |  | | --- | | **GeoVision ASManager Windows Application 6.1.2.0 Credentials Disclosure** **2025.10.29**  Credit:  **[Giorgi Dograshvili](https://cxsecurity.com/author/Giorgi%2BDograshvili/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-26263](https://cxsecurity.com/cveshow/CVE-2025-26263/ "Click to see CVE-2025-26263")**  CWE: **N/A** | |

# Exploit Title: GeoVision ASManager Windows Application 6.1.2.0 - Credentials Disclosure
# Date: 19-MAR-2025
# Exploit Author: Giorgi Dograshvili [DRAGOWN]
# Vendor Homepage: https://www.geovision.com.tw/
# Software Link: https://www.geovision.com.tw/download/product/
# Version: 6.1.2.0 or less
# Tested on: Windows 10 | Kali Linux
# CVE : CVE-2025-26263
# PoC: https://github.com/DRAGOWN/CVE-2025-26263
GeoVision ASManager Windows desktop application with the version 6.1.2.0 or less, is vulnerable to credentials disclosure due to improper memory handling in the ASManagerService.exe process.
Requirements
To perform successful attack an attacker requires:
- System level access to the GV-ASManager windows desktop application with the version 6.1.2.0 or less;
- A high privilege account to dump the memory.
Impact
The vulnerability can be leveraged to perform the following unauthorized actions:
- An attacker with high privilege system user, who isn't authorized to access GeoVision ASManager, is able to:
-- Dump ASManager accounts credentials;
-- Authenticate in ASManager.
- After the authenticating in ASManager, an attacker will be able to:
-- Access the resources such as monitoring cameras, access cards, parking cars, employees and visitors, etc.
-- Make changes in data and service network configurations such as employees, access card security information, IP addresses and configurations, etc.
-- Disrupt and disconnect services such as monitoring cameras, access controls.
-- Clone and duplicate access control data for further attack scenarios.
PoC
The steps for a successful exploitation are described in the following GitHub article with screenshots:
- https://github.com/DRAGOWN/CVE-2025-26263
After a successful attack, you will get administrative access to:
- ASManager - Access & Security Management software in OS
- ASWeb - Access & Security Management
- TAWeb - Time and Attendance Management
- VMWeb - Visitor Management

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025100016)

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