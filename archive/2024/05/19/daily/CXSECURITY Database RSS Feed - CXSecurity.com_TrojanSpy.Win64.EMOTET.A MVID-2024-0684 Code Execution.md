---
title: TrojanSpy.Win64.EMOTET.A MVID-2024-0684 Code Execution
url: https://cxsecurity.com/issue/WLB-2024050050
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-19
fetch_date: 2025-10-06T16:48:38.131111
---

# TrojanSpy.Win64.EMOTET.A MVID-2024-0684 Code Execution

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
|  |  | |  | | --- | | **TrojanSpy.Win64.EMOTET.A MVID-2024-0684 Code Execution** **2024.05.18**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/f917c77f60c3c1ac6dbbadbf366ddd30.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: TrojanSpy.Win64.EMOTET.A
Vulnerability: Arbitrary Code Execution
Description: The malware looks for and executes a x64-bit "CRYPTBASE.dll" PE file in its current directory. Therefore, we can hijack the DLL and execute our own code to intercept and terminate the malware. Once loaded the exploit dll will check if the current directory is "C:\Windows\System32", if not we grab our process ID and terminate. Leverage RansomLord v3 for DLL generation, while written as a proof-of-concept to specifically defeat ransomware, it can also be used to generate DLLs to try an exploit other types of malwares. All basic tests were conducted successfully in a virtual machine environment.
Family: EMOTET
Type: PE64
MD5: f917c77f60c3c1ac6dbbadbf366ddd30
SHA256: b76fbc81bbb7f3108d27d9da9e2646aeb3769fba62bf7961f79306812de3486c
Vuln ID: MVID-2024-0684
Disclosure: 05/14/2024
Exploit/PoC:
1) Download RansomLord v3
https://github.com/malvuln/RansomLord
2) Locate the x64 CRYPTBASE.dll entry using the -m flag (DLL Map)
3) Use -g flag (Generate Exploit) to output an x64 DLL CRYPTBASE.dll, based on an existing vulnerable malware in the victims list.
4) (Optional) -e flag to setup Windows event IOC logging in the registry, this will log the SHA256 hash, full path and filename.
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050050)

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