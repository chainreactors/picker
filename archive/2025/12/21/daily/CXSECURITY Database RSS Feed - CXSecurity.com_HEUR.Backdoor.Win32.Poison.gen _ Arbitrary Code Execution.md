---
title: HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution
url: https://cxsecurity.com/issue/WLB-2025120020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-21
fetch_date: 2025-12-22T03:27:57.797172
---

# HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution

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
|  |  | |  | | --- | | **HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution** **2025.12.21**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source: https://malvuln.com/advisory/b2e50fa38510a5ea8e11f614b1c1d0d5.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13@gmail.com
Media: x.com/malvuln
Threat: HEUR.Backdoor.Win32.Poison.gen
Vulnerability: Arbitrary Code Execution
Description: The malware looks for and executes a x32-bit "WININET.dll" PE file in its current directory. Therefore, we can hijack the DLL and execute our own code to intercept and terminate the malware. Leverage RansomLordNG v1.0 for DLL generation, while written as a proof-of-concept to specifically defeat ransomware, these DLLs may also defeat other types of malware if vulnerable. All basic tests were conducted successfully in a virtual machine environment. RansomLordNG v1.0 currently includes enhanced logging, memory dump and deweaponize features.
Family: Poison
Type: PE32
Attack-pattern TTP: Hijack Execution Flow (T1574)
MD5: b2e50fa38510a5ea8e11f614b1c1d0d5
SHA256: 0de336f07cc19a6fda4cf9dacf1c4be0c6fb17158182d5274355cffa494ac8ed
Vuln ID: MVID-2025-0701
Disclosure: 12/20/2025
Exploit/PoC:
1) Download RansomLordNG v1.0
https://github.com/malvuln/RansomLord
2) Locate the x32 WININET.dll entry using the -m flag (DLL Map)
3) Use -g flag (Generate Exploit) to output an DLL, based on an existing vulnerable malware in the victims list.
4) (Optional) -e flag to setup Windows event IOC logging in the registry, this will log the SHA256 hash, full path and filename.
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120020)

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