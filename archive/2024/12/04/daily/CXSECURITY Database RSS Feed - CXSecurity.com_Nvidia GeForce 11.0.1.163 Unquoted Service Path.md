---
title: Nvidia GeForce 11.0.1.163 Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2024120002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-04
fetch_date: 2025-10-06T19:36:59.523581
---

# Nvidia GeForce 11.0.1.163 Unquoted Service Path

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
|  |  | |  | | --- | | **Nvidia GeForce 11.0.1.163 Unquoted Service Path** **2024.12.03**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Nvidia GeForce v11.0.1.163 - Unquoted Service Path
# Date: 2024-11-25
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# t.me/Ci3c0
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# Vendor Homepage: https://www.nvidia.com/es-la/
# Software Link: https://www.nvidia.com/es-la/
# Version: 11.0.1.163
# Tested on: Windows 10 Pro x64 Esp
C:\>wmic service get name, pathname, displayname, startmode | findstr
"Auto" | findstr /i /v "C:\Windows\\" | findstr /i "NVIDIA" | findstr /i /v
"""
NVIDIA Update Service Daemon
nvUpdatusService C:\Program Files
(x86)\NVIDIA Corporation\NVIDIA Updatus\daemonu.exe
Auto
C:\>sc qc nvUpdatusService
[SC] QueryServiceConfig CORRECTO
NOMBRE\_SERVICIO: nvUpdatusService
TIPO : 10 WIN32\_OWN\_PROCESS
TIPO\_INICIO : 2 AUTO\_START (DELAYED)
CONTROL\_ERROR : 1 NORMAL
NOMBRE\_RUTA\_BINARIO: C:\Program Files (x86)\NVIDIA
Corporation\NVIDIA Updatus\daemonu.exe
GRUPO\_ORDEN\_CARGA :
ETIQUETA : 0
NOMBRE\_MOSTRAR : NVIDIA Update Service Daemon
DEPENDENCIAS :
NOMBRE\_INICIO\_SERVICIO: .\UpdatusUser

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120002)

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