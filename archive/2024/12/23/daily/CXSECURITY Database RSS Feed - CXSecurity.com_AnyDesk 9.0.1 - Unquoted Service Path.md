---
title: AnyDesk 9.0.1 - Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2024120024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-23
fetch_date: 2025-10-06T19:35:40.887728
---

# AnyDesk 9.0.1 - Unquoted Service Path

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
|  |  | |  | | --- | | **AnyDesk 9.0.1 - Unquoted Service Path** **2024.12.22**  Credit:  **[Parastou Razi(IR)](https://cxsecurity.com/author/Parastou%2BRazi%28IR%29/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: AnyDesk 9.0.1 - Unquoted Service Path
# Date: 2024-12-11
# Exploit Author: Parastou Razi
# Contact: razi.parastoo@gmail.com
# Vendor Homepage: http://anydesk.com
# Software Link: http://anydesk.com/download
# Version: Software Version 9.0.1
# Tested on: Windows 11 x64
1. Description:
The Anydesk installs as a service with an unquoted service path running
with SYSTEM privileges.
This could potentially allow an authorized but non-privileged local
user to execute arbitrary code with elevated privileges on the system.
2. Proof
C:\>sc qc anydesk --service
[SC] QueryServiceConfig SUCCESS
SERVICE\_NAME: anydesk
TYPE : 10 WIN32\_OWN\_PROCESS
START\_TYPE : 2 AUTO\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : "C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
--service
LOAD\_ORDER\_GROUP :
TAG : 0
DISPLAY\_NAME : AnyDesk Service
DEPENDENCIES : RpcSs
SERVICE\_START\_NAME : LocalSystem

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120024)

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