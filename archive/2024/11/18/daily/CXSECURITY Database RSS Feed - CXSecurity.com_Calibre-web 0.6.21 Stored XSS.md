---
title: Calibre-web 0.6.21 Stored XSS
url: https://cxsecurity.com/issue/WLB-2024110029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-18
fetch_date: 2025-10-06T19:12:13.345385
---

# Calibre-web 0.6.21 Stored XSS

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
|  |  | |  | | --- | | **Calibre-web 0.6.21 Stored XSS** **2024.11.17**  Credit:  **[Pentest-Tools](https://cxsecurity.com/author/Pentest-Tools/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-39123](https://cxsecurity.com/cveshow/CVE-2024-39123/ "Click to see CVE-2024-39123")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Stored XSS in Calibre-web
# Date: 07/05/2024
# Exploit Authors: Pentest-Tools.com (Catalin Iovita & Alexandru Postolache)
# Vendor Homepage: (https://github.com/janeczku/calibre-web/)
# Version: 0.6.21 - Romesa
# Tested on: Linux 5.15.0-107, Python 3.10.12, lxml 4.9.4
# CVE: CVE-2024-39123
## Vulnerability Description
Calibre-web 0.6.21 is vulnerable to a Stored Cross-Site Scripting (XSS) vulnerability. This vulnerability allows an attacker to inject malicious scripts that get stored on the server and executed in the context of another user's session.
## Steps to Reproduce
1. Log in to the application.
2. Upload a new book.
3. Access the Books List functionality from the `/table?data=list&sort\_param=stored` endpoint.
4. In the `Comments` field, input the following payload:
<a href=javas%1Bcript:alert()>Hello there!</a>
4. Save the changes.
5. Upon clicking the description on the book that was created, in the Book Details, the payload was successfully injected in the Description field. By clicking on the message, an alert box will appear, indicating the execution of the injected script.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110029)

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