---
title: Micro Focus GroupWise Session ID Disclosure
url: https://cxsecurity.com/issue/WLB-2023010048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-29
fetch_date: 2025-10-04T05:06:40.779705
---

# Micro Focus GroupWise Session ID Disclosure

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
|  |  | |  | | --- | | **Micro Focus GroupWise Session ID Disclosure** **2023.01.28**  Credit:  **[Stefan Pietsch](https://cxsecurity.com/author/Stefan%2BPietsch/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-38756](https://cxsecurity.com/cveshow/CVE-2022-38756/ "Click to see CVE-2022-38756")**  CWE: **[CWE-598](https://cxsecurity.com/cwe/CWE-598 "Click to see CWE-598")** | |

# Trovent Security Advisory 2203-01 #
#####################################
Micro Focus GroupWise transmits session ID in URL
#################################################
Overview
########
Advisory ID: TRSA-2203-01
Advisory version: 1.0
Advisory status: Public
Advisory URL: https://trovent.io/security-advisory-2203-01
Affected product: Micro Focus GroupWise
Affected version: prior to 18.4.2
Vendor: Micro Focus, https://www.microfocus.com
Credits: Trovent Security GmbH, Stefan Pietsch
Detailed description
####################
Micro Focus GroupWise is a messaging software for email and personal information
management.
Trovent Security GmbH discovered that the GroupWise web application transmits
the session ID in HTTP GET requests in the URL when email content is accessed.
The exposed session ID can be recorded in the browser history of the client and
in log files of the web server or reverse proxy server.
A possible attacker with access to the browser history or the server log files
is able to take control of the user session with the help of the session ID.
Severity: Medium
CVSS Score: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)
CVE ID: CVE-2022-38756
CWE ID: CWE-598
Proof of concept
################
Simplified HTTP request:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET /attachment?session=<SESSIONID>&id=... HTTP/1.1
Host: <HOSTNAME>
...
X-User-Agent: GroupWise Web (18.4.0-139604)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Solution / Workaround
#####################
The vendor released a fixed version of GroupWise.
Fixed in version 18.4.2.
History
#######
2022-03-30: Vulnerability found
2022-08-05: Vendor contacted
2022-10-31: Contacted vendor again
2022-11-01: Vendor replied that the vulnerability will be investigated
2022-11-14: Vendor contacted, asking for status
2022-11-16: Vendor replied that a security bulletin is being prepared
2022-12-06: Vendor published security bulletin
2023-01-27: Advisory published

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010048)

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