---
title: Re: Ransom.Haron / Code Execution
url: https://seclists.org/fulldisclosure/2023/Jul/17
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:52.913574
---

# Re: Ransom.Haron / Code Execution

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Re: Ransom.Haron / Code Execution

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Mon, 10 Jul 2023 02:03:50 -0400

---

```
*** Correction: should have been CRYPTSP.dll ***

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/dedad693898bba0e4964e6c9a749d380.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln

Threat: Ransom.Haron
Vulnerability: Code Execution
Description: Haron looks for and executes DLLs in its current directory.
Therefore, we can potentially hijack a vuln DLL execute our own code,
control and terminate the malware pre-encryption. The exploit dll will
check if the current directory is "C:\Windows\System32", if not we grab our
process ID and terminate. We do not need to rely on hash signature or
third-party product, the malwares own flaw will do the work for us.
Endpoint protection systems and or antivirus can potentially be killed
prior to executing malware, but this method cannot as theres nothing to
kill the DLL just lives on disk waiting. From defensive perspective you can
add the DLLs to a specific network share containing important data as a
layered approach. All basic tests were conducted successfully in a virtual
machine environment.
Family: Haron
Type: PE32
MD5: dedad693898bba0e4964e6c9a749d380
Vuln ID: MVID-2022-0609
Disclosure: 06/06/2022

Exploit/PoC:
1) Compile the following C code as "CRYPTSP.dll"
2) Place the DLL in same directory as the ransomware
3) Optional - Hide it: attrib +s +h "CRYPTSP.dll"
4) Run the malware

#include "windows.h"

//By malvuln
//Purpose: Exploit Haron
/** DISCLAIMER:
Author is NOT responsible for any damages whatsoever by using this software
or improper malware
handling. By using this code you assume and accept all risk implied or
otherwise.
**/

//gcc -shared -o CRYPTSP.dll CRYPTSP.c -m32

BOOL APIENTRY DllMain(HINSTANCE hInst, DWORD reason, LPVOID reserved){
  switch (reason) {
  case DLL_PROCESS_ATTACH:
   MessageBox(NULL, "Haron\nPWNED By MALVULN", "Code Exec PoC", MB_OK);
   TCHAR buf[MAX_PATH];
   GetCurrentDirectory(MAX_PATH, TEXT(buf));
   int rc = strcmp("C:\\Windows\\System32", TEXT(buf));
    if(rc != 0){
    HANDLE handle = OpenProcess(PROCESS_TERMINATE, FALSE, getpid());
     if (NULL != handle) {
        TerminateProcess(handle, 0);
       CloseHandle(handle);
     }
   }
    break;
  }
  return TRUE;
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

On Mon, Jun 6, 2022 at 10:09â€¯PM malvuln <malvuln13 () gmail com> wrote:
```

> ```
> Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
> Original source:
> https://malvuln.com/advisory/dedad693898bba0e4964e6c9a749d380.txt
> Contact: malvuln13 () gmail com
> Media: twitter.com/malvuln
>
> Threat: Ransom.Haron
> Vulnerability: Code Execution
> Description: Haron looks for and executes DLLs in its current directory.
> Therefore, we can potentially hijack a vuln DLL execute our own code,
> control and terminate the malware pre-encryption. The exploit dll will
> check if the current directory is "C:\Windows\System32", if not we grab our
> process ID and terminate. We do not need to rely on hash signature or
> third-party product, the malwares own flaw will do the work for us.
> Endpoint protection systems and or antivirus can potentially be killed
> prior to executing malware, but this method cannot as theres nothing to
> kill the DLL just lives on disk waiting. From defensive perspective you can
> add the DLLs to a specific network share containing important data as a
> layered approach. All basic tests were conducted successfully in a virtual
> machine environment.
> Family: Haron
> Type: PE32
> MD5: dedad693898bba0e4964e6c9a749d380
> Vuln ID: MVID-2022-0609
> Disclosure: 06/06/2022
>
> Exploit/PoC:
> 1) Compile the following C code as "VERSION.dll"
> 2) Place the DLL in same directory as the ransomware
> 3) Optional - Hide it: attrib +s +h "VERSION.dll"
> 4) Run the malware
>
> #include "windows.h"
>
> //By malvuln
> //Purpose: Exploit Haron
> /** DISCLAIMER:
> Author is NOT responsible for any damages whatsoever by using this
> software or improper malware
> handling. By using this code you assume and accept all risk implied or
> otherwise.
> **/
>
> //gcc -c VERSION.c -m32
> //gcc -shared -o VERSION.dll VERSION.o -m32
>
> BOOL APIENTRY DllMain(HINSTANCE hInst, DWORD reason, LPVOID reserved){
>   switch (reason) {
>   case DLL_PROCESS_ATTACH:
>    MessageBox(NULL, "Haron\nPWNED By MALVULN", "Code Exec PoC", MB_OK);
>    TCHAR buf[MAX_PATH];
>    GetCurrentDirectory(MAX_PATH, TEXT(buf));
>    int rc = strcmp("C:\\Windows\\System32", TEXT(buf));
>     if(rc != 0){
>     HANDLE handle = OpenProcess(PROCESS_TERMINATE, FALSE, getpid());
>      if (NULL != handle) {
>         TerminateProcess(handle, 0);
>        CloseHandle(handle);
>      }
>    }
>     break;
>   }
>   return TRUE;
> }
>
>
> Disclaimer: The information contained within this advisory is supplied
> "as-is" with no warranties or guarantees of fitness of use or otherwise.
> Permission is hereby granted for the redistribution of this advisory,
> provided that it is not altered except by reformatting it, and that due
> credit is given. Permission is explicitly given for insertion in
> vulnerability databases and similar, provided that due credit is given to
> the author. The author is not responsible for any misuse of the information
> contained herein and accepts no responsibility for any damage caused by the
> use or misuse of this information. The author prohibits any malicious use
> of security related information or exploits by the author or elsewhere. Do
> not attempt to download Malware samples. The author of this website takes
> no responsibility for any kind of damages occurring from improper Malware
> handling or the downloading of ANY Malware mentioned on this website or
> elsewhere. All content Copyright (c) Malvuln.com (TM).
> ```

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left...