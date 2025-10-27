---
title: SEH utnserver Pro 20.1.22 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024120015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-11
fetch_date: 2025-10-06T19:34:28.974428
---

# SEH utnserver Pro 20.1.22 Cross Site Scripting

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
|  |  | |  | | --- | | **SEH utnserver Pro 20.1.22 Cross Site Scripting** **2024.12.10**  Credit:  **[P. Riedl](https://cxsecurity.com/author/P.%2BRiedl/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11304](https://cxsecurity.com/cveshow/CVE-2024-11304/ "Click to see CVE-2024-11304")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

St. Plten UAS 20241118-0
-------------------------------------------------------------------------------
title| Multiple Stored Cross-Site Scripting
product| SEH utnserver Pro
vulnerable version| 20.1.22
fixed version| 20.1.35
CVE number| CVE-2024-11304
impact| High
homepage| https://www.seh-technology.com/
found| 2024-05-24
by| P. Riedl, J. Springer, P. Chist, D. Sagl, S. Vogt
| These vulnerabilities were discovery during research at
| St.Plten UAS, supported and coordinated by CyberDanube.
|
| https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"We are SEH from Bielefeld - manufacturer of high-quality network solutions.
With over 35 years of experience in the fields of printing and networks, we
offer our customers a broad and high-level expertise in solutions for all types
of business environments."
Source: https://www.seh-technology.com/us/company/about-us.html
Vulnerable versions
-------------------------------------------------------------------------------
utnserver Pro / 20.1.22
utnserver ProMAX / 20.1.22
INU-100 / 20.1.22
Vulnerability overview
-------------------------------------------------------------------------------
1) Multiple Stored Cross-Site Scripting (CVE-2024-11304)
Different settings on the web interface of the device can be abused to store
JavaScript code and execute it in the context of a user's browser.
Proof of Concept
-------------------------------------------------------------------------------
1) Multiple Stored Cross-Site Scripting (CVE-2024-11304)
The following snippet can be used to demonstrate, that stored cross-site
scripting is possible in multiple locations on the device:
"><script>alert(document.location)</script>
Examples are:
\* Users password: "usrMg\_pwd"
This can be displayed in cleartext and executed in the device configuration.
\* Certificate options: "Common name", "Organization name", "Locality name"
This can be executed in the certificate information.
\* Device description: "Host name", "Contact person", "Description"
This can be executed in "Device -> Description".
\* USB password via uploading a crafted "\_parameters.txt" file: "usbMdg\_pwd"
This can be executed in the "Maintenance -> Content View" tab.
Saving this text to the device description leads to a persistent cross-site
scripting. Therefore, everyone who openes the device description executes the
injected code in the context of the own browser.
The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).
Solution
-------------------------------------------------------------------------------
Install firmware version 20.1.35 to fix the vulnerabilities.
Workaround
-------------------------------------------------------------------------------
None
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends SEH Computertechnik customers to upgrade the firmware to
the latest version available.
Contact Timeline
-------------------------------------------------------------------------------
2024-09-23: Contacting SEH Computertechnik and sent advisory to support.
Support answered, that vulnerabilities are fixed in version
20.1.35.
2024-10-21: Closed the issue and scheduled publication for November.
2024-11-18: Coordinated disclosure of advisory.
Web: https://www.fhstp.ac.at/
Twitter: https://x.com/fh\_stpoelten
Mail: mis@fhstp.ac.at
EOF T. Weber / @2024

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120015)

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