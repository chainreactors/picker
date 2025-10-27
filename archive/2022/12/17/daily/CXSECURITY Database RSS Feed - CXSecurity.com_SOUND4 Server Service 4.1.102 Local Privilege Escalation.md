---
title: SOUND4 Server Service 4.1.102 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-17
fetch_date: 2025-10-04T01:44:01.227843
---

# SOUND4 Server Service 4.1.102 Local Privilege Escalation

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
|  |  | |  | | --- | | **SOUND4 Server Service 4.1.102 Local Privilege Escalation** **2022.12.16**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

SOUND4 Server Service 4.1.102 Local Privilege Escalation
Vendor: SOUND4 Ltd.
Product web page: https://www.sound4.com | https://www.sound4.biz
Affected version: 4.1.102
Summary: SOUND4 Windows Server Service.
Desc: The application suffers from an unquoted search path issue impacting
the service 'SOUND4 Server' for Windows. This could potentially allow an
authorized but non-privileged local user to execute arbitrary code with
elevated privileges on the system. A successful attempt would require the
local user to be able to insert their code in the system root path undetected
by the OS or other security applications where it could potentially be executed
during application startup or reboot. If successful, the local user's code
would execute with the elevated privileges of the application.
Tested on: Windows 10 Home 64 bit (build 9200)
SOUND4 Server v4.1.102
SOUND4 Remote Control v4.3.17
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
Macedonian Information Security Research and Development Laboratory
Zero Science Lab - https://www.zeroscience.mk - @zeroscience
Advisory ID: ZSL-2022-5721
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5721.php
26.09.2022
--
C:\>sc qc "SOUND4 Server"
[SC] QueryServiceConfig SUCCESS
SERVICE\_NAME: SOUND4 Server
TYPE : 10 WIN32\_OWN\_PROCESS
START\_TYPE : 2 AUTO\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : C:\Program Files\SOUND4\Server\SOUND4 Server.exe --service
LOAD\_ORDER\_GROUP :
TAG : 0
DISPLAY\_NAME : SOUND4 Server
DEPENDENCIES :
SERVICE\_START\_NAME : LocalSystem
C:\>cacls "C:\Program Files\SOUND4\Server\SOUND4 Server.exe"
C:\Program Files\SOUND4\Server\SOUND4 Server.exe NT AUTHORITY\SYSTEM:(ID)F
BUILTIN\Administrators:(ID)F
BUILTIN\Users:(ID)R
APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(ID)R
APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(ID)R
C:\Program Files\SOUND4\Server>"SOUND4 Server.exe" -V
4.1.102

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120028)

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