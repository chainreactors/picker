---
title: Reservit Hotel 2.1 Stored Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2025040008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:41.363684
---

# Reservit Hotel 2.1 Stored Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **Reservit Hotel 2.1 Stored Cross-Site Scripting (XSS)** **2025.04.06**  Credit:  **[Ilteris Kaan Pehlivan](https://cxsecurity.com/author/Ilteris%2BKaan%2BPehlivan/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-9458](https://cxsecurity.com/cveshow/CVE-2024-9458/ "Click to see CVE-2024-9458")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Reservit Hotel < 3.0 - Admin+ Stored XSS
# Date: 2024-10-01
# Exploit Author: Ilteris Kaan Pehlivan
# Vendor Homepage: https://wpscan.com/plugin/reservit-hotel/
# Version: Reservit Hotel 2.1
# Tested on: Windows, WordPress, Reservit Hotel < 3.0
# CVE : CVE-2024-9458
The plugin does not sanitise and escape some of its settings, which could
allow high privilege users such as admin to perform Stored Cross-Site
Scripting attacks even when the unfiltered\_html capability is disallowed
(for example in multisite setup).
1. Install and activate Reservit Hotel plugin.
2. Go to Reservit hotel > Content
3. Add the following payload to the Button text > French field sane save: "
style=animation-name:rotation onanimationstart=alert(/XSS/)//
4. The XSS will trigger upon saving and when any user will access the
content dashboard again
References:
https://wpscan.com/vulnerability/1157d6ae-af8b-4508-97e9-b9e86f612550/
https://www.cve.org/CVERecord?id=CVE-2024-9458

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040008)

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