---
title: XWorm Trojan 2.1 Null Pointer Derefernce DoS
url: https://cxsecurity.com/issue/WLB-2023040018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-06
fetch_date: 2025-10-04T11:30:09.653161
---

# XWorm Trojan 2.1 Null Pointer Derefernce DoS

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
|  |  | |  | | --- | | **XWorm Trojan 2.1 Null Pointer Derefernce DoS** **2023.04.05**  Credit:  **[XWorm Trojan 2.1 - Null Pointer Derefernce DoS](https://cxsecurity.com/author/XWorm%2BTrojan%2B2.1%2B-%2BNull%2BPointer%2BDerefernce%2BDoS/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-476](https://cxsecurity.com/cwe/CWE-476 "Click to see CWE-476")** | |

#Exploit Author: XWorm Trojan 2.1 - Null Pointer Derefernce DoS
# Exploit Author: TOUHAMI KASBAOUI
# Vendor Homepage: https://blog.cyble.com/2022/08/19/evilcoder-project-selling-multiple-dangerous-tools-online/
# Software Link: N/A# Version: 2.1# Tested on: Windows 10
# CVE : N/A
==================================================================
THE BUG : NULL pointer dereference -> DOS crash
==================================================================
The sophisticated XWorm Trojan is well exploited by EvilCoder, where they collect different features such as ransomware and keylogger TAs to make it more risky for victims. The Trojan assigned to victims suffers from a NULL pointer deference vulnerability, which could lead to a denial of service for the server builder of the threat actor by getting his IP address and port of command and control.
==================================================================
WINDBG ANALYSIS AFTER SENDING 1000 'A' BYTES
==================================================================
(160.b98): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
eax=0330c234 ebx=0113e8d4 ecx=00000000 edx=018c0000 esi=0330c234 edi=0113e55c
eip=078f5a59 esp=0113e4f8 ebp=0113e568 iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010246
builder!XWorm.Client.isDisconnected+0xa9:
078f5a59 8b01            mov     eax,dword ptr [ecx]  ds:002b:00000000=????????
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*                                                                             \*
\*                        Exception Analysis                                   \*
\*                                                                             \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
MethodDesc:   055a86b4
Method Name:  XWorm.Client.isDisconnected()
Class:        09fe9634
MethodTable:  055a86d8
mdToken:      06000730
Module:       01464044
IsJitted:     yes
CodeAddr:     078f59b0
Transparency: Critical
MethodDesc:   055a86b4
Method Name:  XWorm.Client.isDisconnected()
Class:        09fe9634
MethodTable:  055a86d8
mdToken:      06000730
Module:       01464044
IsJitted:     yes
CodeAddr:     078f59b0
Transparency: Critical
Failed to request MethodData, not in JIT code range
KEY\_VALUES\_STRING: 1
    Key  : AV.Dereference
    Value: NullPtr
    Key  : AV.Fault
    Value: Read
    Key  : Analysis.CPU.mSec
    Value: 6406
    Key  : Analysis.DebugAnalysisManager
    Value: Create
    Key  : Analysis.Elapsed.mSec
    Value: 12344
    Key  : Analysis.IO.Other.Mb
    Value: 152
    Key  : Analysis.IO.Read.Mb
    Value: 3
    Key  : Analysis.IO.Write.Mb
    Value: 181
    Key  : Analysis.Init.CPU.mSec
    Value: 48905
    Key  : Analysis.Init.Elapsed.mSec
    Value: 6346579
    Key  : Analysis.Memory.CommitPeak.Mb
    Value: 200
    Key  : CLR.BuiltBy
    Value: NET48REL1LAST\_C
    Key  : CLR.Engine
    Value: CLR
    Key  : CLR.Version
    Value: 4.8.4515.0
    Key  : Timeline.OS.Boot.DeltaSec
    Value: 7496
    Key  : Timeline.Process.Start.DeltaSec
    Value: 6371
    Key  : WER.OS.Branch
    Value: vb\_release
    Key  : WER.OS.Timestamp
    Value: 2019-12-06T14:06:00Z
    Key  : WER.OS.Version
    Value: 10.0.19041.1
    Key  : WER.Process.Version
    Value: 2.1.0.0
NTGLOBALFLAG:  0
PROCESS\_BAM\_CURRENT\_THROTTLED: 0
PROCESS\_BAM\_PREVIOUS\_THROTTLED: 0
APPLICATION\_VERIFIER\_FLAGS:  0
EXCEPTION\_RECORD:  (.exr -1)
ExceptionAddress: 078f5a59 (builder!XWorm.Client.isDisconnected+0x000000a9)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000000
Attempt to read from address 00000000
FAULTING\_THREAD:  00000b98
PROCESS\_NAME:  builder.exe
READ\_ADDRESS:  00000000
ERROR\_CODE: (NTSTATUS) 0xc0000005 - The instruction at 0x%p referenced memory at 0x%p. The memory could not be %s.
EXCEPTION\_CODE\_STR:  c0000005
EXCEPTION\_PARAMETER1:  00000000
EXCEPTION\_PARAMETER2:  00000000
IP\_ON\_HEAP:  078f5a59
The fault address in not in any loaded module, please check your build's rebase
log at <releasedir>\bin\build\_logs\timebuild\ntrebase.log for module which may
contain the address if it were loaded.
STACK\_TEXT:
0113e568 73140556     00000000 00000000 00000000 builder!XWorm.Client.isDisconnected+0xa9
0113e574 7314373a     0113e8d4 0113e5b8 732dd3f0 clr!CallDescrWorkerInternal+0x34
0113e5c8 7321f0d1     c887551e 00000000 0335b7dc clr!CallDescrWorkerWithHandler+0x6b
0113e608 7321f1d6     731d7104 0335b7dc 055ab280 clr!CallDescrWorkerReflectionWrapper+0x55
0113e90c 7212853c     00000000 0330a1dc 00000000 clr!RuntimeMethodHandle::InvokeMethod+0x838
0113e930 72114a9d     00000000 00000000 00000000 mscorlib\_ni!
0113e94c 6e14bf55     00000000 00000000 00000000 mscorlib\_ni!
0113e968 6e14be68     00000000 00000000 00000000 System\_Windows\_Forms\_ni!
0113e990 72118604     00000000 00000000 00000000 System\_Windows\_Forms\_ni!
0113e9f4 72118537     00000000 00000000 00000000 mscorlib\_ni!
0113ea08 721184f4     00000000 00000000 00000000 mscorlib\_ni!
0113ea24 6e14bdfa     00000000 00000000 00000000 mscorlib\_ni!
0113ea40 6e14bb9a     00000000 00000000 00000000 System\_Windows\_Forms\_ni!
0113ea80 6e13b07f     00000000 00000000 00000000 System\_Windows\_Forms\_ni!
0113eacc 6e144931     00000000 00000000 00000000 System\_Windows\_Forms\_...