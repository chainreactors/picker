---
title: Xlibre Xnest 24.1.0 / 24.2.0 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2024110004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-03
fetch_date: 2025-10-06T19:13:48.374938
---

# Xlibre Xnest 24.1.0 / 24.2.0 Buffer Overflow

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
|  |  | |  | | --- | | **Xlibre Xnest 24.1.0 / 24.2.0 Buffer Overflow** **2024.11.02**  Credit:  **[Enrico Weigelt](https://cxsecurity.com/author/Enrico%2BWeigelt/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-9632](https://cxsecurity.com/cveshow/CVE-2024-9632/ "Click to see CVE-2024-9632")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

XLibre project security advisory
---------------------------------
As Xlibre Xnest is based on Xorg, it is affected by some security issues
which recently became known in Xorg:
CVE-2024-9632: can be triggered by providing a modified bitmap to the
X.Org server.
CVE-2024-9632: Heap-based buffer overflow privilege escalation in
\_XkbSetCompatMap
See: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9632
Affected versions:
\* 24.1.0
\* 24.2.0
24.1.x release:
Repo: https://gitlab.freedesktop.org/metux/xserver.git
Branch: xlibre/xnest/24.1
Tag: xnest-24.1.1
SHA: 11450b0946c1035944c5946d665f21f83356b6b9
24.2.x release:
Repo: https://gitlab.freedesktop.org/metux/xserver.git
Branch: xlibre/xnest/24.2
Tag: xnest-24.2.1
SHA: 9a6aec9bf62b6bdd75795a5e28648d4af07fe413
These bugfix branches also contain several other pointer and bounds
related problems that haven't been rated as possibly exploitable yet,
but no other unnecessary changes which don't fix actual bugs.
All users are strongly advised to upgrade to the fixed mainenance
releases ASAP.
--mtx
--
---
Enrico Weigelt, metux IT consult
Free software and Linux embedded engineering
info@metux.net -- +49-151-27565287

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110004)

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