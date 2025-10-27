---
title: Trojan.Win32.Platinum.gen / Arbitrary Code Execution
url: https://cxsecurity.com/issue/WLB-2022110032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-21
fetch_date: 2025-10-03T23:18:43.630012
---

# Trojan.Win32.Platinum.gen / Arbitrary Code Execution

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
|  |  | |  | | --- | | **Trojan.Win32.Platinum.gen / Arbitrary Code Execution** **2022.11.20**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/71a76adeadc7b51218d265771fc2b0d1.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Trojan.Win32.Platinum.gen
Vulnerability: Arbitrary Code Execution
Description: The malware looks for and executes DLLs in its current directory. Therefore, we can potentially hijack a vuln DLL execute our own code, control and terminate the malware. Once loaded the exploit dll will check if the current directory is "C:\Windows\System32", if not we grab our process ID and terminate. All basic tests were conducted successfully in a virtual machine environment.
Family: PlatinumGroup
Type: PE32
MD5: 71a76adeadc7b51218d265771fc2b0d1
Vuln ID: MVID-2022-0657
Dropped files: Adobe\_Update\_Sync.exe
Disclosure: 11/18/2022
Exploit/PoC:
1) Compile the following C code as "WTSAPI32.dll"
2) Place the DLL in same directory as the malware
3) Optional - Hide it: attrib +s +h "WTSAPI32.dll"
4) Run the malware
#include "windows.h"
//By malvuln - November 2022
//Purpose: PWN Platinum Group malware strain MD5: 71a76adeadc7b51218d265771fc2b0d1
//gcc -c WTSAPI32.c -m32
//gcc -shared -o WTSAPI32.dll WTSAPI32.o -m32
/\*\* DISCLAIMER:
Author is NOT responsible for any damages whatsoever by using this software or improper malware
handling. By using this code you assume and accept all risk implied or otherwise.
\*\*/
BOOL APIENTRY DllMain(HINSTANCE hInst, DWORD reason, LPVOID reserved){
switch (reason) {
case DLL\_PROCESS\_ATTACH:
MessageBox(NULL, "Platinum Group\nPWNED!!! by Malvuln", "Code Exec PoC", MB\_OK);
TCHAR buf[MAX\_PATH];
if(GetCurrentDirectory(MAX\_PATH, buf))
if(strcmp("C:\\Windows\\System32", buf) != 0){
HANDLE handle = OpenProcess(PROCESS\_TERMINATE, FALSE, getpid());
if (NULL != handle) {
TerminateProcess(handle, 0);
CloseHandle(handle);
}
}
break;
}
return TRUE;
}
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110032)

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