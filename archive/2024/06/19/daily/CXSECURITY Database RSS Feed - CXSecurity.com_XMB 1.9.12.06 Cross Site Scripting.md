---
title: XMB 1.9.12.06 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024060045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-19
fetch_date: 2025-10-06T16:54:21.136353
---

# XMB 1.9.12.06 Cross Site Scripting

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
|  |  | |  | | --- | | **XMB 1.9.12.06 Cross Site Scripting** **2024.06.18**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Persistent XSS in XMB 1.9.12.06
# Date: 06/12/2024
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.xmbforum2.com/
# Software Link: https://www.xmbforum2.com/download/XMB-1.9.12.06.zip
# Version: 1.9.12.06
# Tested on: Windows XP
# CVE: N/A
## Vulnerability Details
A persistent (stored) XSS vulnerability was discovered in XMB 1.9.12.06.
The vulnerability allows an attacker to inject malicious JavaScript code
into a template or specific fields. This payload is stored on the server
and executed in the browser of any user who visits the forum, leading to
potential session hijacking, data theft, and other malicious activities.
### XSS in Template
An attacker can inject malicious JavaScript code into a template:
1. Login as Admin: Access the XMB Forum with admin privileges.
2. Navigate to the Administration Panel: Go to `/cp.php`, then in "Look &
Feel" select "Templates". This will go to `/cp2.php?action=templates`.
Select the "footer" template and click edit.
3. Enter Payload: Add the XSS payload in the footer template:
<script>alert('XSS');</script>
4. Save the Change: Click "Submit Changes".
5. Trigger the Payload: The XSS payload will trigger anywhere the footer
template is rendered.
### XSS in News Ticker
An attacker can inject malicious JavaScript code into the News Ticker field
of the Front Page Options:
1. Login as Admin: Access the XMB Forum with admin privileges.
2. Navigate to the Administration Panel: Go to `/cp.php`, then in
"Settings" go to "Front Page Options".
3. Enter Payload: Add the XSS payload in the "News in Newsticker" field:
<img src=x onerror=alert(1)>
4. Save the Change: Click "Submit Changes".
5. Trigger the Payload: The XSS payload will trigger anywhere the News
Ticker is displayed eg, home page

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060045)

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