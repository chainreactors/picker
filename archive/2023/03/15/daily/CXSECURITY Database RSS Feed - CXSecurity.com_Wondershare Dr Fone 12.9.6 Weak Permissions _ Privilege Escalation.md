---
title: Wondershare Dr Fone 12.9.6 Weak Permissions / Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023030037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-15
fetch_date: 2025-10-04T09:33:06.080779
---

# Wondershare Dr Fone 12.9.6 Weak Permissions / Privilege Escalation

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
|  |  | |  | | --- | | **Wondershare Dr Fone 12.9.6 Weak Permissions / Privilege Escalation** **2023.03.14**  Credit:  **[Thurein Soe](https://cxsecurity.com/author/Thurein%2BSoe/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-27010](https://cxsecurity.com/cveshow/CVE-2023-27010/ "Click to see CVE-2023-27010")**  CWE: **[CWE-250](https://cxsecurity.com/cwe/CWE-250 "Click to see CWE-250")  [CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Executive Summary:
Product Name: Wondershare Dr. Fone
Vendor Home Page: https://drfone.wondershare.com
Affected Version(s): Dr Fone version 12.9.6
Vulnerability Type: Execution with Unnecessary Privileges (CWE-250)
CVE Reference: CVE-2023-27010.
Credit: Thurein Soe
Vendor Description:
Wondershare Dr. Fone is an app designed to help with data recovery and
management for all Android and iOS devices.
Vulnerability description:
Wondershare Dr Fone version 12.9.6 running services named "WsDrvInst" on
Windows have weak service permissions and are susceptible to local
privilege escalation vulnerability. Weak service permissions run with
system user permission, allowing a standard user/domain user to elevate to
administrator privilege upon successfully modifying the service or
replacing the affected executable. DriverInstall.exe gave modification
permission to any authenticated users in the windows operating system,
allowing standard users to modify the service and leading to Privilege
Escalation.
C:\Users\NyaMeeEain\Desktop>cacls "C:\Program Files
(x86)\Wondershare\drfone\Addins\Repair\DriverInstall.exe"
C:\Program Files (x86)\Wondershare\drfone\Addins\Repair\DriverInstall.exe
Everyone:(ID)F
NT AUTHORITY\SYSTEM:(ID)F
BUILTIN\Administrators:(ID)F
BUILTIN\Users:(ID)R
APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(ID)R
APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(ID)R
C:\Users\NyaMeeEain\Desktop>sc qc WsDrvInst
SERVICE\_NAME: WsDrvInst
TYPE : 10 WIN32\_OWN\_PROCESS
START\_TYPE : 3 DEMAND\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : "C:\Program Files
(x86)\Wondershare\drfone\Addins\Repair\DriverInstall.exe"
LOAD\_ORDER\_GROUP :
TAG : 0
DISPLAY\_NAME : Wondershare Driver Install Service
DEPENDENCIES : RPCSS
SERVICE\_START\_NAME : LocalSystem
References:
https://cwe.mitre.org/data/definitions/250.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030037)

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