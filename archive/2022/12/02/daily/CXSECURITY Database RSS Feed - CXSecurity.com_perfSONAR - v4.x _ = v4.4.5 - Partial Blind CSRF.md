---
title: perfSONAR - v4.x < = v4.4.5 - Partial Blind CSRF
url: https://cxsecurity.com/issue/WLB-2022120002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:16:02.970213
---

# perfSONAR - v4.x < = v4.4.5 - Partial Blind CSRF

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
|  |  | |  | | --- | | **perfSONAR - v4.x <= v4.4.5 - Partial Blind CSRF** **2022.12.01**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Ryan Moore](https://cxsecurity.com/author/Ryan%2BMoore/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2022-41413](https://cxsecurity.com/cveshow/CVE-2022-41413/ "Click to see CVE-2022-41413")**  CWE: **N/A** | |

https://github.com/renmizo/CVE-2022-41413/
Vendor: perfSONAR
Link: https://github.com/perfsonar/
Affected Versions: v4.x <= v4.4.5
Vulnerability Type: Partial Blind CSRF
Discovered by: Ryan Moore
CVE: CVE-2022-41413
Summary
A partial blind CSRF vulnerability exists in perfSONAR v4.x <= v4.4.5 within the /perfsonar-graphs/ test results page. Parameters and values can be injected/passed via the URL parameter, forcing the client to connect unknowingly in the background to other sites via transparent XMLHTTPRequests. This partial blind CSRF bypasses the built-in whitelisting function in perfSONAR.
This vulnerability was patched in perfSONAR v4.4.6.
Proof of Concept
Examples
Here are two examples of this vulnerability. For further details, review the Technical Overview section below.
Example 1:
Client browser connects to www.google.com in the background.
http://192.168.68.145/perfsonar-graphs/?source=1&dest=2&url=https://www.google.com
Example 2:
Client browser connects to arbitrary IP and port in the background, passing delete parameter to /api endpoint.
http://192.168.68.145/perfsonar-graphs/?source=8.8.8.8&dest=%26action%3Ddelete&url=http://192.168.68.113:4444/api

**##### References:**

https://lists.internet2.edu/sympa/arc/perfsonar-user/2022-11/msg00008.html

https://www.perfsonar.net/releasenotes-2022-11-09-4-4-6.html

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41413

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120002)

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