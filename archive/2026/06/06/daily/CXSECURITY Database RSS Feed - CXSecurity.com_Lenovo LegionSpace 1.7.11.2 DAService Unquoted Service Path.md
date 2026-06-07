---
title: Lenovo LegionSpace 1.7.11.2 DAService Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2026060005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-06
fetch_date: 2026-06-07T06:15:46.945512
---

# Lenovo LegionSpace 1.7.11.2 DAService Unquoted Service Path

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
|  |  | |  | | --- | | **Lenovo LegionSpace 1.7.11.2 DAService Unquoted Service Path** **2026.06.06**  Credit:  **[CENACIF-MX](https://cxsecurity.com/author/CENACIF-MX/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Lenovo LegionSpace 1.7.11.2 - 'DAService' Unquoted Service Path
# Exploit Author: CENACIF-MX
# Discovery Date: 2025-12-04
# Vendor Homepage: https://support.lenovo.com/es/es/solutions/legion\_space
# Tested Version: 1.7.11.2
# Vulnerability Type: Unquoted Service Path
# Tested on OS: Microsoft Windows 11 Enterprise x64 es
# Fix: Upgrade to Lenovo LegionSpace 1.8.12.13 or later
# CVE : N/A
# Disclosure Timeline
# | Date | Event |
# |------|-------|
# | 2025-12-04 | Vulnerability discovered |
# | 2025-12-04 | Vendor notified |
# | 2026-02-09 | New version |
# Step to discover Unquoted Service Path:
C:\>wmic service get name, pathname, displayname, startmode | findstr "Auto" | findstr /i /v "C:\Windows\\" | findstr /i "Lenovo" | findstr /i /v """
DAService DAService C:\Program Files\Lenovo\LegionSpace\1.7.11.2\LSDaemon.exe Auto
# Service info:
C:\>sc qc "DAService"
[SC] QueryServiceConfig CORRECTO
NOMBRE\_SERVICIO: DAService
TIPO : 10 WIN32\_OWN\_PROCESS
TIPO\_INICIO : 2 AUTO\_START
CONTROL\_ERROR : 1 NORMAL
NOMBRE\_RUTA\_BINARIO: C:\Program Files\Lenovo\LegionSpace\1.7.11.2\LSDaemon.exe
GRUPO\_ORDEN\_CARGA :
ETIQUETA : 0
NOMBRE\_MOSTRAR : DAService
DEPENDENCIAS :
NOMBRE\_INICIO\_SERVICIO: LocalSystem
#Exploit:
A successful attempt would require the local user to be able to insert their code in the system root path undetected by the OS or other security applications where it could potentially be executed during application startup or reboot. If successful, the local user's code would execute with the elevated privileges of the application.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060005)

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