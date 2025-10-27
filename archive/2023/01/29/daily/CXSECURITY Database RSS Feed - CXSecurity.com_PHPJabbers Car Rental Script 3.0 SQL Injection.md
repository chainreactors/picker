---
title: PHPJabbers Car Rental Script 3.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023010047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-29
fetch_date: 2025-10-04T05:06:42.341193
---

# PHPJabbers Car Rental Script 3.0 SQL Injection

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
|  |  | |  | | --- | | **PHPJabbers Car Rental Script 3.0 SQL Injection** **2023.01.28**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

┌┌───────────────────────────────────────────────────────────────────────────────────────┐
││ C r a C k E r ┌┘
┌┘ T H E C R A C K O F E T E R N A L M I G H T ││
└───────────────────────────────────────────────────────────────────────────────────────┘┘
┌──── From The Ashes and Dust Rises An Unimaginable crack.... ────┐
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ [ Vulnerability ] ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: Author : CraCkEr :
│ Website : PHPJabbers.com │
│ Vendor : PHPJabbers │
│ Software : PHPJabbers Car Rental Script 3.0 │
│ Vuln Type: SQL Injection │
│ Impact : Database Access │
│ │
│────────────────────────────────────────────────────────────────────────────────────────│
│ ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: :
│ Release Notes: │
│ ═════════════ │
│ │
│ SQL injection attacks can allow unauthorized access to sensitive data, modification of │
│ data and crash the application or make it unavailable, leading to lost revenue and │
│ damage to a company's reputation. │
│ │
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Greets:
The\_PitBull, Raz0r, iNs, SadsouL, His0k4, Hussin X, Mr. SQL
CryptoJob (Twitter) twitter.com/CryptozJob
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ © CraCkEr 2023 ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Path: /index.php
POST parameter 'hour\_from' is vulnerable to SQLI
POST parameter 'minutes\_to' is vulnerable to SQLI
date\_from=27.01.2023&hour\_from=[INJECT-HERE]&minutes\_from=00&date\_to=28.01.2023&hour\_to=09&minutes\_to=[INJECT-HERE]&pickup\_id=4&same\_location=1
POST parameter 'col\_name' is vulnerable to SQLI
index.php?controller=pjFront&action=pjActionLoadCars&session\_id=9j5lonhuljjtcpff7l1qjq5a85&type\_id=all&transmission=&col\_name=total\_price&direction=asc
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010047)

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