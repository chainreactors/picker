---
title: Intelight X-1L Traffic controller Maxtime 1.9.6 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025040024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-16
fetch_date: 2025-10-06T22:03:50.287692
---

# Intelight X-1L Traffic controller Maxtime 1.9.6 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Intelight X-1L Traffic controller Maxtime 1.9.6 Remote Code Execution (RCE)** **2025.04.15**  Credit:  **[Andrew Lemon](https://cxsecurity.com/author/Andrew%2BLemon/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-38944](https://cxsecurity.com/cveshow/CVE-2024-38944/ "Click to see CVE-2024-38944")**  CWE: **N/A** | |

# Exploit Title: Intelight X-1L Traffic controller Maxtime 1.9.6 - Remote Code Execution (RCE)
# Google Dork: N/A
# Date: 07/09/2024
# Exploit Author: Andrew Lemon/Red Threat https://redthreatsec.com
# Vendor Homepage: https://www.q-free.com
# Software Link: N/A
# Version: 1.9
# Tested on: (Intelight x-1) Linux 3.14.57
# CVE : CVE-2024-38944
## Vulnerability Description
This vulnerability allows remote attackers to bypass authentication on affected installations of MaxTime Database Editor.
Authentication is not required to exploit this vulnerability.
The specific flaw exists within the web-based UI on Traffic Controllers running version 1.9.x firmware.
The issue results from the lack of authentication prior to allowing access to functionality.
An attacker can leverage this vulnerability to gain full control of Intelight Traffic Controllers and modify the configuration of a traffic intersection,
modify traffic light sequences, or trigger the intersection to go into 4 way flash causing a denial of service and causing traffic congestion.
## Steps to Reproduce
Navigate to the IP address of an identified controller
When prompted for authentication append /cgi-bin/generateForm.cgi?formID=142 to the end of the IP address
Under the web security tab change the drop down from enabled to disabled and select apply or take note of the username and password and login with those.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040024)

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