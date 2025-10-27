---
title: Backdoor.Win32.DarkSky.23 / Remote Stack Buffer Overflow (SEH)
url: https://cxsecurity.com/issue/WLB-2022100043
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:45.948629
---

# Backdoor.Win32.DarkSky.23 / Remote Stack Buffer Overflow (SEH)

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
|  |  | |  | | --- | | **Backdoor.Win32.DarkSky.23 / Remote Stack Buffer Overflow (SEH)** **2022.10.17**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/1164ef21ef2af97e0339359c0dce5e7d.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Backdoor.Win32.DarkSky.23
Vulnerability: Remote Stack Buffer Overflow (SEH)
Description: The malware listens on TCP port 5418. Third-party adversaries who can reach the server can send a specially crafted payload triggering a stack buffer overflow overwriting EDX register and Structured Exception Handler (SEH). In order to see the typical exploit pattern of "\x41" "AAAA" we need to actually send "\x50" as there is an loop that performs an XOR converting our payload. Therefore, if we send "AAAAAAAA" we will get "PPPPPPPP", the malware performs the XOR with the value of 11.
Family: DarkSky
Type: PE32
MD5: 1164ef21ef2af97e0339359c0dce5e7d
Vuln ID: MVID-2022-0648
Dropped files: SysArchive.exe, KNREL32.exe, notepade.exe
ASLR: False
DEP: False
CFG: False
Safe SEH: False
Disclosure: 10/15/2022
Example:
0040134A | 80 34 31 11 | xor byte ptr ds:[ecx+esi],11 | ;XOR converting the payload happens here.
0040134E | 41 | inc ecx |
0040134F | 3B C8 | cmp ecx,eax |
00401351 | 7C F7 | jl sysarchive.40134A |
00401353 | 5E | pop esi |
00401354 | C3 | ret |
Python test...
>>> 0x41 ^ 0x11
80
>>> hex(80)
'0x50'
>>> chr(0x50)
'P'
GET /AAAAA will then become all "P" ...
0019D24C 56 54 45 31 3E 50 50 50 50 50 41 41 41 41 41 41 VTE1>PPPPPAAAAAA
0019D25C 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
0019D26C 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
0019D27C 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
0019D28C 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
So to get our \x41 pattern we need to supply \x50, the malware will XOR it with 0x11 giving us \x41.
>>> 0x50 ^ 0x11
65
>>> hex(65)
'0x41'
>>> chr(65)
'A'
EAX : 7EFEFEFE
EBX : 02902A58
ECX : 0019F4B0
EDX : 41414141
EBP : 0019D230
ESP : 0019D214
ESI : 0019D777
EDI : 0019FF81
EIP : 7451561B msvcrt.7451561B
Finally we see our desired exploit payload converted from \x50 'P' to \x41 or "A"
0019D240 08 DF 8E 02 08 DF 8E 02 01 00 00 00 56 54 45 31 .ÃŸ...ÃŸ......VTE1
0019D250 3E 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 >AAAAAAAAAAAAAAA
0019D260 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
0019D270 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 AAAAAAAAAAAAAAAA
0019D280 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 50 AAAAAAAAAAAAAAAP
0019D290 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 PPPPPPPPPPPPPPPP
0019D2A0 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 PPPPPPPPPPPPPPPP
Memory Dump:
(2798.242c): Stack buffer overflow - code c0000409 (first/second chance not available)
eax=00000000 ebx=00000000 ecx=0019f52c edx=41414141 esi=00000000 edi=00000002
eip=7770ed3c esp=0019cb60 ebp=0019cba0 iopl=0 nv up ei pl nz ac pe nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00000216
ntdll!ZwWaitForMultipleObjects+0xc:
7770ed3c c21400 ret 14h
0:000> .ecxr
eax=7efefefe ebx=02552c88 ecx=0019f52c edx=41414141 esi=0019d777 edi=0019fffd
eip=74515619 esp=0019d214 ebp=0019d230 iopl=0 nv up ei pl zr na pe nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00010246
msvcrt!strcat+0x89:
74515619 8917 mov dword ptr [edi],edx ds:002b:0019fffd=41000000
\*\*\* WARNING: Unable to verify checksum for SysArchive.exe
\*\*\* ERROR: Module load completed but symbols could not be loaded for SysArchive.exe
0:000> !analyze -v
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\* \*
\* Exception Analysis \*
\* \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Failed calling InternetOpenUrl, GLE=12029
FAULTING\_IP:
msvcrt!strcat+89
74515619 8917 mov dword ptr [edi],edx
EXCEPTION\_RECORD: 0019cd64 -- (.exr 0x19cd64)
ExceptionAddress: 74515619 (msvcrt!strcat+0x00000089)
ExceptionCode: c0000005 (Access violation)
ExceptionFlags: 00000008
NumberParameters: 2
Parameter[0]: 00000001
Parameter[1]: 001a0000
Attempt to write to address 001a0000
PROCESS\_NAME: SysArchive.exe
ERROR\_CODE: (NTSTATUS) 0xc0000409 - The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.
EXCEPTION\_CODE: (NTSTATUS) 0xc0000409 - The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.
EXCEPTION\_PARAMETER1: 00000015
MOD\_LIST: <ANALYSIS/>
NTGLOBALFLAG: 70
APPLICATION\_VERIFIER\_FLAGS: 0
CHKIMG\_EXTENSION: !chkimg -lo 50 -d !msvcrt
74515590 - msvcrt!strcat
[ 8b:cc ]
74515617 - msvcrt!strcat+87 (+0x87)
[ eb:cc ]
2 errors : !msvcrt (74515590-74515617)
CONTEXT: 0019cdb4 -- (.cxr 0x19cdb4)
eax=7efefefe ebx=02552c88 ecx=0019f52c edx=41414141 esi=0019d777 edi=0019fffd
eip=74515619 esp=0019d214 ebp=0019d230 iopl=0 nv up ei pl zr na pe nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00010246
msvcrt!strcat+0x89:
74515619 8917 mov dword ptr [edi],edx ds:002b:0019fffd=41000000
Resetting default scope
WRITE\_ADDRESS: 001a0000
FOLLOWUP\_IP:
msvcrt!strcat+89
74515619 8917 mov dword ptr [edi],edx
FAULTING\_THREAD: 0000242c
BUGCHECK\_STR: APPLICATION\_FAULT\_MEMORY\_CORRUPTION\_STACK\_BUFFER\_OVERRUN\_MISSING\_GSFRAME\_LARGE\_EXPLOITABLE\_FILL\_PATTERN\_41414141
PRIMARY\_PROBLEM\_CLASS: MEMORY\_CORRUPTION\_LARGE\_EXPLOITABLE\_FILL\_PATTERN\_41414141
DEFAULT\_BUCKET\_ID: MEMORY\_CORRUPTION\_LARGE\_EXPLOITABLE\_FILL\_PATTERN\_41414141
LAST\_CONTROL\_TRANSFER: ...