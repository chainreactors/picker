---
title: Windows Defender (MsMpEng.exe) Race Condition -> LPE / SYSTEM / Use-After-Free -> Crash
url: https://cxsecurity.com/issue/WLB-2026060013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:38.396121
---

# Windows Defender (MsMpEng.exe) Race Condition -> LPE / SYSTEM / Use-After-Free -> Crash

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
|  |  | |  | | --- | | **Windows Defender (MsMpEng.exe) Race Condition -> LPE / SYSTEM / Use-After-Free -> Crash** **2026.06.15**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Titles: Windows Defender (MsMpEng.exe) Race Condition -> LPE / SYSTEM / Use-After-Free -> Crash
# Author: nu11secur1ty
# Date: 2026-06-11
# Vendor: Microsoft Corporation
# Software: Windows Defender Antivirus (MsMpEng.exe)
# Reference: https://gitlab.com/nu11secur1ty/0/-/raw/main/README.md?ref\_type=heads
## Description:
A race condition exists between Windows Defender's `MpCleanCallbackFunction` (cleanup routine) and Volume Shadow Copy creation. Successful exploitation results in:
1. LPE (Local Privilege Escalation) to NT AUTHORITY\SYSTEM via `CreateProcessAsUser`
2. Use-after-free condition causing Windows Defender (`MsMpEng.exe`) to crash
3. System remains without antivirus protection for the session
The exploit uses:
- Fake ISO mount via `OpenVirtualDisk` / `AttachVirtualDisk`
- Real-time priority escalation (`REALTIME\_PRIORITY\_CLASS` + `THREAD\_PRIORITY\_TIME\_CRITICAL`)
- Speed racing against Defender's cleanup routine
\*\*STATUS: HIGH - Critical (0-Day / LPE)\*\*
Exploit:
[url](https://gitlab.com/nu11secur1ty/0.git)
Demo:
[url](https://www.patreon.com/nu11secur1ty/posts/honda-exploit-160798929)
Time spent:
9:10:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty https://www.asc3t1c-nu11secur1ty.com/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060013)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top