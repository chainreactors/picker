---
title: Nginx 1.25.x Server Version Information Disclosure
url: https://cxsecurity.com/issue/WLB-2026010018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-29
fetch_date: 2026-01-30T04:02:13.300735
---

# Nginx 1.25.x Server Version Information Disclosure

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
|  |  | |  | | --- | | **Nginx 1.25.x Server Version Information Disclosure** **2026.01.29**  Credit:  **[RERO](https://cxsecurity.com/author/RERO/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-200, CWE-16, CWE-668](https://cxsecurity.com/cwe/CWE-200%2C%20CWE-16%2C%20CWE-668 "Click to see CWE-200, CWE-16, CWE-668")**  **[**Dork:** server: nginx](https://cxsecurity.com/dorks/)** | |

During security testing, the target web server was found to expose
its exact Nginx version (1.25.x) via HTTP response headers.
The "Server" header reveals the full backend software version,
indicating that the 'server\_tokens' directive is not properly disabled.
This represents a security misconfiguration and allows accurate
technology fingerprinting by remote attackers.
Additionally, the server responds with HTTP 403 Forbidden errors
while still disclosing the Nginx version. This behavior increases
the attack surface by providing attackers with valuable reconnaissance
information even when access is restricted.
Furthermore, the affected IP address was observed hosting multiple
virtual hosts, making it susceptible to virtual host enumeration
techniques. Combined with version disclosure, this enables attackers
to identify additional hidden applications and services hosted on
the same infrastructure.
Impact:
- Precise server fingerprinting
- Identification of version-specific vulnerabilities
- Expanded attack surface
- Facilitation of targeted attacks against virtual hosts
This issue can be mitigated by disabling server version disclosure
using 'server\_tokens off' and applying strict security hardening
to HTTP error responses.

**##### References:**

https://owasp.org/www-project-top-ten/2017/A6\_2017-Security\_Misconfiguration

https://cwe.mitre.org/data/definitions/200.html

https://cwe.mitre.org/data/definitions/668.html

https://nginx.org/en/docs/http/ngx\_http\_core\_module.html#server\_tokens

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010018)

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