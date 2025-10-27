---
title: CodeAstro Online Railway Reservation System 1.0 Cross Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2025040025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-17
fetch_date: 2025-10-06T22:04:39.298936
---

# CodeAstro Online Railway Reservation System 1.0 Cross Site Scripting (XSS)

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
|  |  | |  | | --- | | **CodeAstro Online Railway Reservation System 1.0 Cross Site Scripting (XSS)** **2025.04.16**  Credit:  **[Raj Nandi](https://cxsecurity.com/author/Raj%2BNandi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-7815](https://cxsecurity.com/cveshow/CVE-2024-7815/ "Click to see CVE-2024-7815")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: XSS Vulnerability in Online Railway Reservation System 1.0
# Date: 2024-08-15
# Exploit Author: Raj Nandi
# Vendor Homepage: https://codeastro.com/
# Software Link:
https://codeastro.com/online-railway-reservation-system-in-php-with-source-code/
# Version: 1.0
# Tested on: Any OS
# CVE: CVE-2024-7815
## Description:
A Cross-Site Scripting (XSS) vulnerability exists in [Application
Name/Version]. This vulnerability allows an attacker to inject and execute
arbitrary JavaScript code within the context of the user's browser session.
## Proof of Concept (PoC):
1. Navigate to [vulnerable page or input field].
2. Input the following payload: `<script>alert(document.cookie)</script>`
3. Upon execution, the script will trigger and display the user's cookies
in an alert box.
## Mitigation:
To prevent this vulnerability, ensure that all user inputs are properly
sanitized and validated before being reflected back on the webpage.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040025)

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