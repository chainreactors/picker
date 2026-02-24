---
title: Oracle HTTP Server & WebLogic Proxy Plug-in – Unauthenticated Improper Access Control
url: https://cxsecurity.com/issue/WLB-2026020027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:31.941438
---

# Oracle HTTP Server & WebLogic Proxy Plug-in – Unauthenticated Improper Access Control

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
|  |  | |  | | --- | | **Oracle HTTP Server & WebLogic Proxy Plug-in – Unauthenticated Improper Access Control** **2026.02.23**  Credit:  **[RERO](https://cxsecurity.com/author/RERO/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-21962](https://cxsecurity.com/cveshow/CVE-2026-21962/ "Click to see CVE-2026-21962")**  CWE: **[CWE-284 – Improper Access Control](https://cxsecurity.com/cwe/CWE-284%20%E2%80%93%20Improper%20Access%20Control "Click to see CWE-284 – Improper Access Control")** | |

A critical improper access control vulnerability has been identified in Oracle HTTP Server and the Oracle WebLogic Proxy Plug-in. This issue allows a remote, unauthenticated attacker to bypass security restrictions and perform unauthorized actions through network-based HTTP requests.
The vulnerability originates from insufficient enforcement of access control mechanisms at the proxy layer, which operates at a trusted boundary between external clients and internal application services. Due to this flaw, malicious requests may be improperly forwarded and processed with elevated trust, enabling unauthorized access to sensitive functionality.
Successful exploitation can lead to a complete compromise of confidentiality and integrity, including unauthorized access to application data and backend resources accessible through the affected services. Given the remote attack vector, lack of authentication requirements, and low attack complexity, this vulnerability poses a severe security risk and should be considered critical.

**##### References:**

https://nvd.nist.gov/vuln/detail/CVE-2026-21962

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-21962

https://www.oracle.com/security-alerts/cpujan2026verbose.html

https://cvefeed.io/vuln/detail/CVE-2026-21962

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020027)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top