---
title: AeroCMS v0.0.1 - Stored Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023040073
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:25.430772
---

# AeroCMS v0.0.1 - Stored Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **AeroCMS v0.0.1 - Stored Cross-Site Scripting (XSS)** **2023.04.21**  **![bd](https://cert.cx/cxstatic/images/flags/bd.png) [Rahad Chowdhury](https://cxsecurity.com/author/Rahad%2BChowdhury/1/) **(BD)** ![bd](https://cert.cx/cxstatic/images/flags/bd.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-29847](https://cxsecurity.com/cveshow/CVE-2023-29847/ "Click to see CVE-2023-29847")**  CWE: **N/A** | |

# Exploit Title: AeroCMS v0.0.1 - Stored Cross-Site Scripting (XSS)
# Date: 2023-03-14
# Exploit Author: Rahad Chowdhury
# Vendor Homepage: https://github.com/MegaTKC/AeroCMS
# Software Link: https://github.com/MegaTKC/AeroCMS/archive/refs/tags/v0.0.1.zip
# Version: 0.0.1
# Tested on: Windows 10, PHP 7.4.29, Apache 2.4.53
# CVE: CVE-2023-29847
Steps to Reproduce:
1. At first open any post.
2. then fill up comments section and your request data will be
POST /AeroCMS/post.php?p\_id=1 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 86
Origin: http://127.0.0.1
Cookie: PHPSESSID=qtj8dhp0jub18i2agkfm4bf5ea
Connection: close
comment\_author=test&comment\_email=test@test.com&comment\_content=test&create\_comment=
3. "comment\_author" and "comment\_content" parameters are vulnerable. Let's try to use any XSS payload in "comment\_author" and "comment\_content" parameters.
4. Now login admin panel and go to "Comments" Menu
5. You will see XSS pop up (If admin approve comment so XSS pop up execute in post section).

**##### References:**

https://github.com/MegaTKC/AeroCMS/issues/11

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040073)

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