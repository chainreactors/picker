---
title: Trojan.Win32.DarkGateLoader (multi variants) / Arbitrary Code Execution
url: https://cxsecurity.com/issue/WLB-2024060018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:33.787613
---

# Trojan.Win32.DarkGateLoader (multi variants) / Arbitrary Code Execution

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
|  |  | |  | | --- | | **Trojan.Win32.DarkGateLoader (multi variants) / Arbitrary Code Execution** **2024.06.07**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/afe012ed0d96abfe869b9e26ea375824.txt
Contact: malvuln13@gmail.com
Media: x.com/malvuln
Threat: Trojan.Win32.DarkGateLoader (multi variants)
Vulnerability: Arbitrary Code Execution
Description: Multiple variants of this malware look for and execute x32-bit "urlmon.dll" PE file in its current directory. Therefore, we can hijack that DLL and execute our own code to intercept and terminate the malware. Once loaded the exploit dll will check if the current directory is "C:\Windows\System32", if not we grab our process ID and terminate. Leverage RansomLord v3.1 for DLL generation, while written as a proof-of-concept to specifically defeat ransomware, it can also be used to generate DLLs to try an exploit other types of malwares. All basic tests were conducted successfully in a virtual machine environment.
Family: DarkGateLoader
Type: PE32
MD5: afe012ed0d96abfe869b9e26ea375824
SHA256: 18d87c514ff25f817eac613c5f2ad39b21b6e04b6da6dbe8291f04549da2c290
Other vulnerable samples:
cad102af0d2709fd57f62d9cce9ba174
ca2ef9d3146341428657295892894170
3c609ac6b2de29578a2383d71e12caa9
Vuln ID: MVID-2024-0685
Disclosure: 06/05/2024
Exploit/PoC:
1) Download RansomLord v3.1
https://github.com/malvuln/RansomLord
2) Locate the x32 urlmon.dll entry using the -m flag (DLL Map)
3) Use -g flag (Generate Exploit) to output an x32 DLL urlmon.dll, based on an existing vulnerable malware in the victims list.
4) (Optional) -e flag to setup Windows event IOC logging in the registry, this will attempt to log the SHA256 hash, full path and filename.
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060018)

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