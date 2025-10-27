---
title: Backdoor.Win32.Agent.pw / Remote Stack Buffer Overflow (SEH)
url: https://seclists.org/fulldisclosure/2024/Sep/55
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:26:00.068076
---

# Backdoor.Win32.Agent.pw / Remote Stack Buffer Overflow (SEH)

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Agent.pw / Remote Stack Buffer Overflow (SEH)

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 27 Sep 2024 16:20:23 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/68dd7df213674e096d6ee255a7b90088.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Agent.pw
Vulnerability: Remote Stack Buffer Overflow (SEH)
Description: The malware listens on TCP port 21111. Third-party
attackers who can reach an infected machine can send specially crafted
sequential packetz triggering a stack buffer overflow overwriting the
ECX, EDI registers and Structured Exception Handler (SEH). Sending a
packet containing the ascii character "A" or "41", registers are
overwritten with "3431" as 4 is 34 hex and 1 is 31 hex. The lowercase
character "R" consistently triggers an access violation with registers
being overwritten with "r" 72 hex.
Family: Agent
Type: PE32
MD5: 68dd7df213674e096d6ee255a7b90088
SHA256: 2ba1d27325224407b6d57e0e8d141e3f301225d18a68bb5380c46287a0fc4441
Vuln ID: MVID-2024-0697
Dropped files:
ASLR: False
DEP: False
CFG: False
Safe SEH: False
Disclosure: 09/27/2024

Memory Dump:
(1f90.1888): Stack buffer overflow - code c0000409 (first/second
chance not available)
eax=00000000 ebx=00000000 ecx=72727272 edx=040b1a3c esi=00000000 edi=00000002
eip=76fced3c esp=0019de98 ebp=0019ded8 iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
ntdll!ZwWaitForMultipleObjects+0xc:
76fced3c c21400          ret     14h

0:000> .ecxr
eax=025806f0 ebx=00000150 ecx=72727272 edx=040b1a3c esi=00000000 edi=72727272
eip=00411515 esp=0019e54c ebp=0019e56c iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+0x11515:
00411515 897904          mov     dword ptr [ecx+4],edi ds:002b:72727276=????????

0:000> !analyze -v
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************

FAULTING_IP:
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+11515
00411515 897904          mov     dword ptr [ecx+4],edi

EXCEPTION_RECORD:  0019e09c -- (.exr 0x19e09c)
ExceptionAddress: 00411515
(Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+0x00011515)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000008
NumberParameters: 2
   Parameter[0]: 00000001
   Parameter[1]: 72727276
Attempt to write to address 72727276

PROCESS_NAME:  Backdoor.Win32.Agent.pw.68dd7df213674e096d6ee255a7b90088.exe

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

CONTEXT:  0019e0ec -- (.cxr 0x19e0ec)
eax=025806f0 ebx=00000150 ecx=72727272 edx=040b1a3c esi=00000000 edi=72727272
eip=00411515 esp=0019e54c ebp=0019e56c iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+0x11515:
00411515 897904          mov     dword ptr [ecx+4],edi ds:002b:72727276=????????
Resetting default scope

WRITE_ADDRESS:  72727276

FOLLOWUP_IP:
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+11515
00411515 897904          mov     dword ptr [ecx+4],edi

FAULTING_THREAD:  00001888

BUGCHECK_STR:
APPLICATION_FAULT_STACK_BUFFER_OVERRUN_MISSING_GSFRAME_STRING_DEREFERENCE_EXPLOITABLE_FILL_PATTERN_72727272

PRIMARY_PROBLEM_CLASS:  STACK_BUFFER_OVERRUN_EXPLOITABLE_FILL_PATTERN_72727272

DEFAULT_BUCKET_ID:  STACK_BUFFER_OVERRUN_EXPLOITABLE_FILL_PATTERN_72727272

LAST_CONTROL_TRANSFER:  from 0040c987 to 00411515

STACK_TEXT:
WARNING: Stack unwind information not available. Following frames may be wrong.
0019e56c 0040c987 025805a8 0000003f 0019e5bc
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+0x11515
0019e768 72727272 72727272 72727272 72727272
Backdoor_Win32_Agent_pw_68dd7df213674e096d6ee255a7b90088+0xc987
0019e76c 72727272 72727272 72727272 72727272 0x72727272
0019e770 72727272 72727272 72727272 72727272 0x72727272
0019e774 72727272 72727272 72727272 72727272 0x72727272
0019e778 72727272 72727272 72727272 72727272 0x72727272
0019e77c 72727272 72727272 72727272 72727272 0x72727272
0019e780 72727272 72727272 72727272 72727272 0x72727272
0019e784 72727272 72727272 72727272 72727272 0x72727272
0019e788 72727272 72727272 72727272 72727272 0x72727272
0019e78c 72727272 72727272 72727272 72727272 0x72727272
0019e790 72727272 72727272 72727272 72727272 0x72727272
0019e794 72727272 72727272 72727272 72727272 0x72727272
0019e798 72727272 72727272 72727272 72727272 0x72727272
0019e79c 72727272 72727272 72727272 72727272 0x72727272
0019e7a0 72727272 72727272 72727272 72727272 0x72727272
0019e7a4 72727272 72727272 72727272 72727272 0x72727272
0019e7a8 72727272 72727272 72727272 72727272 0x72727272
0019e7ac 72727272 72727272 72727272 72727272 0x72727272
0019e7b0 72727272 72727272 72727272 72727272 0x72727272
0019e7b4 72727272 72727272 72727272 72727272 0x72727272
0019e7b8 72727272 72727272 72727272 72727272 0x72727272
0019e7bc 72727272 72727272 72727272 72727272 0x72727272
0019e7c0 72727272 72727272 72727272 72727272 0x72727272
0019e7c4 72727272 72727272 72727272 72727272 0x72727272
0019e7c8 72727272 72727272 72727272 72727272 0x72727272
0019e7cc 72727272 72727272 72727272 72727272 0x72727272
0019e7d0 72727272 72727272 72727272 72727272 0x72727272
0019e7d4 72727272 72727272 72727272 72727272 0x72727272
0019e7d8 72727272 72727272 72727272 72727272 0x72727272
0019e7dc 72727272 72727272 72727272 72727272 0x72727272
0019e7e0 72727272 72727272 72727272 72727272 0x72727272
0019e7e4 72727272 72727272 72727272 72727272 0x72727272
0019e7e8 72727272 72727272 72727272 72727272 0x72727272
0019e7ec 72727272 72727272 72727272 72727272 0x72727272
0019e7f0 72727272 72727272 72727272 72727272 0x72727272
0019e7f4 72727272 72727272 72727272 72727272 0x72727272
0019e7f8 72727272 72727272 72727272 72727272 0x72727272
0019e7fc 72727272 72727272 72727272 72727272 0x72727272
0019e800 72727272 72727272 72727272 72727272 0x72727272
0019e804 72727272 72727272 72727272 72727272 0x72727272
0019e808 72727272 72727272 72727272 72727272 0x72727272
0019e80c 72727272 72727272 72727272 72727272 0x72727272
0019e810 72727272 72727272 72727272 72727272 0x72727272
0019e814 72727272 72727272 72727272 72727272 0x72727272
0019e818 72727272 72727272 72727272 72727272 0x72727272
0019e81c 7272...