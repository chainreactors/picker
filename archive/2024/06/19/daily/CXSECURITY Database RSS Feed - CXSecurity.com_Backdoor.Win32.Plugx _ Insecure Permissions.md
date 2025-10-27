---
title: Backdoor.Win32.Plugx / Insecure Permissions
url: https://cxsecurity.com/issue/WLB-2024060042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-19
fetch_date: 2025-10-06T16:54:25.387605
---

# Backdoor.Win32.Plugx / Insecure Permissions

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
|  |  | |  | | --- | | **Backdoor.Win32.Plugx / Insecure Permissions** **2024.06.18**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/eeb631127f1b9fb3d13d209d8e675634.txt
Contact: malvuln13@gmail.com
Media: x.com/malvuln
Threat: Backdoor.Win32.Plugx
Vulnerability: Insecure Permissions
Family: Plugx
Type: PE32
MD5: eeb631127f1b9fb3d13d209d8e675634
SHA256: c2804080c3f45e8232b3e955611f56c9ba513a7845ddad56a588c4191d139990
Vuln ID: MVID-2024-0686
Disclosure: 06/17/2024
Description: The PlugX malware installs a service "McAfeeOEMInfoOME" which runs as SYSTEM. It also creates a hidden directory "TaskSchedulerome" under C:\ProgramData, granting full (F) permissions to the Everyone user group. Any user can replace the PE files dropped by the malware to disable it or replace it with their own executable. Then wait for a privileged user to logon to the infected machine to potentially escalate privileges.
Exploit/PoC:
cacls C:\ProgramData\TaskSchedulerome\mcf.exe
ProgramData\TaskSchedulerome\mcf.exe Everyone:(OI)(CI)F
attrib -s -h C:\ProgramData\TaskSchedulerome
dir /a C:\ProgramData\TaskSchedulerome
Directory of C:\ProgramData\TaskSchedulerome
02/10/2018 01:21 AM 116,493 mcf.ep
02/10/2018 01:21 AM 140,576 mcf.exe
02/10/2018 01:21 AM 167,776,542 mcutil.dll
3 File(s) 168,033,611 bytes
2 Dir(s) 67,722,203,136 bytes free
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060042)

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