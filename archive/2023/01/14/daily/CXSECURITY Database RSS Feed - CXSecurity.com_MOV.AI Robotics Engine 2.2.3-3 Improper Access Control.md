---
title: MOV.AI Robotics Engine 2.2.3-3 Improper Access Control
url: https://cxsecurity.com/issue/WLB-2023010019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-14
fetch_date: 2025-10-04T03:49:39.141350
---

# MOV.AI Robotics Engine 2.2.3-3 Improper Access Control

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
|  |  | |  | | --- | | **MOV.AI Robotics Engine 2.2.3-3 Improper Access Control** **2023.01.13**  Credit:  **[Thurein Soe](https://cxsecurity.com/author/Thurein%2BSoe/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-46621](https://cxsecurity.com/cveshow/CVE-2022-46621/ "Click to see CVE-2022-46621")**  CWE: **[CWE-284](https://cxsecurity.com/cwe/CWE-284 "Click to see CWE-284")** | |

Manufacturer: MOV.AI
Product Name: MOV.AI Robotics Engine
Vendor Home Page: https://www.mov.ai/
Affected Version(s): MOV.AI Robotics Engine v2.2.3-3
Patch Release: MOV.AI Robotics Engine v2.2.3-4
Patched Version Release: 22 September 2022
Vulnerability Type: Improper Access Control (CWE-284)
CVE Reference: CVE-2022-46621
Author of Advisory: Thurein Soe
Vendor Description:
MOV.AI is a Robotics Engine platform based on ROS. It is packaged in an
intuitive web-based interface to develop autonomous mobile robots (AMRs)
and automated guided vehicles (AGVs). It integrates with navigation,
localization, calibration, and the enterprise-grade tools they need for
advanced automation.
Vulnerability description:
An improper access control vulnerability in MOV.AI Robotics Engine v2.2.3-3
version allows an unauthenticated user to delete an existing user or create
new user-privileged functionality in the application upon successfully
authenticated user logout from the application due to failure to terminate
the authenticated session immediately after authenticated user logout.
References:
https://www.immuniweb.com/vulnerability/improper-access-control.html
https://www.cvedetails.com/cwe-details/284/Access-Control-Authorization-Issues.html
Disclosure Timeline:
06 July 2022: Found security vulnerability during a security assessment
08 July 2022: Customer reported finding a security vulnerability to MOV.AI
15 September 2022: further details of remediation steps sent to MOV.AI
22 September 2022: Patch released for MOV.AI Customer by MOV.AI
Credits:
Thurein Soe
```
Other submissions will send separately.
Best Regards
Thurein

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010019)

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