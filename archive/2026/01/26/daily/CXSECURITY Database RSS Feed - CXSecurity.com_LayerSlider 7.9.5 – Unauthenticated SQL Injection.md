---
title: LayerSlider 7.9.5 – Unauthenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2026010016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-26
fetch_date: 2026-01-27T03:37:13.576875
---

# LayerSlider 7.9.5 – Unauthenticated SQL Injection

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
|  |  | |  | | --- | | **LayerSlider 7.9.5 – Unauthenticated SQL Injection** **2026.01.26**  Credit:  **[RERO](https://cxsecurity.com/author/RERO/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-2879](https://cxsecurity.com/cveshow/CVE-2024-2879/ "Click to see CVE-2024-2879")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** inurl:"wp-content/plugins/LayerSlider"](https://cxsecurity.com/dorks/)** | |

LayerSlider WordPress plugin versions between 7.9.11 and 7.10.0 are affected by an unauthenticated SQL Injection vulnerability.
The vulnerability exists due to insufficient sanitization of user-supplied input, allowing an unauthenticated remote attacker to manipulate SQL queries executed by the application.
Successful exploitation could allow an attacker to extract sensitive information from the database or modify database content without authentication.
Updating the plugin to version 7.10.1 or later is strongly recommended to mitigate this vulnerability.

**##### References:**

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2879

https://wpscan.com/vulnerability/e28e37b0-b11d-489c-bc77-12410cc91e24

https://www.wordfence.com/threat-intel/vulnerabilities/id/3fddf96e-029c-4753-ba82-043ca64b78d3

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010016)

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