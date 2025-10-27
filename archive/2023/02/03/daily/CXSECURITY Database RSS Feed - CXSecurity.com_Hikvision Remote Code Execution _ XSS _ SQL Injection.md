---
title: Hikvision Remote Code Execution / XSS / SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-03
fetch_date: 2025-10-04T05:33:06.654973
---

# Hikvision Remote Code Execution / XSS / SQL Injection

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
|  |  | |  | | --- | | **Hikvision Remote Code Execution / XSS / SQL Injection** **2023.02.02**  Credit:  **[Thurein Soe](https://cxsecurity.com/author/Thurein%2BSoe/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-28172](https://cxsecurity.com/cveshow/CVE-2022-28172/ "Click to see CVE-2022-28172")** | **[CVE-2022-28171](https://cxsecurity.com/cveshow/CVE-2022-28171/ "Click to see CVE-2022-28171")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")  [CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")  [CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Detailed Information
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Product Name: Hikvision
Vendor Home Page: https://www.hikvision.com
Fixed Version: fixed versions were released by Hikvision
Vulnerability Type: CWE-78,89 and 94
CVE Numbers: CVE-2022-28171-CVE-2022-28172
Author of Advisory: Thurein Soe
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Vendor Description:
Hikvision is a world-leading surveillance manufacturer and supplier of
video surveillance and Internet of Things (IoT) equipment for civilian and
military purposes.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Vulnerability description:
Some Hikvision Hybrid SAN Products were vulnerable to multiple remote code
execution (command injection) vulnerabilities, including Reflected XSS,
Ruby code injection, classic and blind SQL injection resulting in remote
code execution that allows an adversary to execute arbitrary operating
system commands etc. However, an adversary must be on the same network to
leverage this vulnerability to execute arbitrary commands.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Vulnerable Versions:
Ds-a71024 Firmware
Ds-a71024 Firmware
Ds-a71048r-cvs Firmware
Ds-a71048 Firmware
Ds-a71072r Firmware
Ds-a71072r Firmware
Ds-a72024 Firmware
Ds-a72024 Firmware
Ds-a72048r-cvs Firmware
Ds-a72072r Firmware
Ds-a80316s Firmware
Ds-a80624s Firmware
Ds-a81016s Firmware
Ds-a82024d Firmware
Ds-a71048r-cvs
Ds-a71024
Ds-a71048
Ds-a71072r
Ds-a80624s
Ds-a82024d
Ds-a80316s
Ds-a81016s
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Credits:
Thurein Soe
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
References:
https://www.hikvision.com/en/support/cybersecurity/security-advisory/security-vulnerability-in-some-hikvision-hybrid-san-products/
https://cve.report/CVE-2022-28171
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Timeline:
11 March 2022: Found security vulnerabilities in a few Hikvision Hybrid SAN
Products
23 March 2022: Reported the finding to Hikvision Security Response Center
(HSRC) team
24 March 2022: Hikvision Security Response Center (HSRC) team requested
further details of reproduction steps and remediation
25 March 2022: Further details of reproduction and remediation steps sent
to the Hikvision Security Response Center (HSRC) team
26 March 2022: Hikvision Security Response Center (HSRC) team agreed to
issue only two CVEs due to multiple vulnerabilities in a single parameter
22 June 2022: Hikvision Release the Initial fixed Version for the affected
products in June 2022.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020008)

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