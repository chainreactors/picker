---
title: SigInt-Hombre v1 / dynamic Suricata detection rules from real-time threat feeds
url: https://cxsecurity.com/issue/WLB-2026010001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-07
fetch_date: 2026-01-08T03:29:11.627764
---

# SigInt-Hombre v1 / dynamic Suricata detection rules from real-time threat feeds

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
|  |  | |  | | --- | | **SigInt-Hombre v1 / dynamic Suricata detection rules from real-time threat feeds** **2026.01.07**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

SigInt-Hombre, generates derived Suricata detection rules from live
URLhaus threat indicators at runtime and deploy them to the Security
Onion platform for high-coverage real-time network monitoring.
https://github.com/malvuln/sigint-hombre
What it does:
Pulls the public URLhaus feed in real time (not mirrored or redistributed)
Skips:
Comments, empty lines, malformed URLs, and feed self-references
Normalizes and extracts:
Protocol, host, URI path, and port
Deduplicates hosts into consistent rule keys
Generates original, derived Suricata alerts for 3 layers:
HTTP → host + URI path, any port if none is specified (max coverage)
TLS → HTTPS detection via SNI (tls.sni) only
DNS → domain lookup visibility via dns.query
Deduplication logic:
HTTP → (host, path)
HTTPS/TLS → host
DNS → host
Writes all alerts into a single combined rule file
Restarts Suricata rules (so-suricata-restart --force)
Malvuln

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010001)

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