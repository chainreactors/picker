---
title: RiteCMS 3.0.0 Reflected Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025080018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-21
fetch_date: 2025-10-07T00:12:42.231367
---

# RiteCMS 3.0.0 Reflected Cross Site Scripting

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
|  |  | |  | | --- | | **RiteCMS 3.0.0 Reflected Cross Site Scripting** **2025.08.20**  Credit:  **[GURJOT SINGH](https://cxsecurity.com/author/GURJOT%2BSINGH/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-28623](https://cxsecurity.com/cveshow/CVE-2024-28623/ "Click to see CVE-2024-28623")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: RiteCMS 3.0.0 – Reflected Cross-Site Scripting (XSS)
# Google Dork: N/A
# Date: 2024-08-12
# Exploit Author: GURJOT SINGH
# Vendor Homepage: https://ritecms.com/
# Software Link: https://github.com/handylulu/RiteCMS/releases/download/V3.0.0/ritecms.v3.0.0.zip
# Version: <= 3.0.0
# Tested on: Ubuntu 22.04 LTS, PHP 8.1, Apache 2.4
# CVE: CVE-2024-28623
## Description:
A reflected Cross-Site Scripting (XSS) vulnerability exists in RiteCMS v3.0.0 within the `main\_menu/edit\_section` parameter.
An attacker can inject arbitrary JavaScript code that will execute in the context of the victim's browser session.
## Impact:
- Theft of credentials or session tokens
- Phishing or malicious redirection
- Full control over the victim’s active browser session
## Proof of Concept (PoC):
Payload:
'"><svg/onload=confirm(/xsss/)>
Steps:
1. Log in or navigate to the vulnerable `main\_menu/edit\_section` functionality.
2. Inject the above payload into the vulnerable parameter.
3. Observe the execution of the injected JavaScript.
Video PoC:
https://github.com/GURJOTEXPERT/ritecms/blob/main/POC.mp4
Full write-up & repository:
https://github.com/GURJOTEXPERT/ritecms
## Mitigation:
- Implement strict input validation and output encoding.
- Enforce a Content Security Policy (CSP) to limit script execution.
- Update RiteCMS to a patched version when available.

**##### References:**

https://github.com/GURJOTEXPERT/ritecms/blob/main/POC.mp4

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080018)

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