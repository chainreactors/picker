---
title: Linux Kernel mseal Invariant Violation (Linux kernel 6.17-7.0 rc5)
url: https://cxsecurity.com/issue/WLB-2026040003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-04
fetch_date: 2026-04-05T04:31:09.363935
---

# Linux Kernel mseal Invariant Violation (Linux kernel 6.17-7.0 rc5)

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
|  |  | |  | | --- | | **Linux Kernel mseal Invariant Violation (Linux kernel 6.17-7.0 rc5)** **2026.04.04**  Credit:  **[Antonius](https://cxsecurity.com/author/Antonius/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-23416](https://cxsecurity.com/cveshow/CVE-2026-23416/ "Click to see CVE-2026-23416")**  CWE: **[CWE-754](https://cxsecurity.com/cwe/CWE-754 "Click to see CWE-754")** | |

Title : CVE-2026-23416 - Linux Kernel mseal Invariant Violation (Linux kernel 6.17-7.0 rc5)
Exploit Poc : https://github.com/bluedragonsecurity/CVE-2026-23416-POC
Discovered by : Antonius (w1sdom)
Web : www.bluedragonsec.com
Github : https://github.com/bluedragonsecurity
Date of Discovery : March 27 2026
Overview
An invariant violation (VM\_WARN\_ON\_VMG) fires at mm/vma.c:830 inside vma\_merge\_existing\_range() when mseal(2) is called with a range spanning two adjacent VMAs where one has VM\_SEALED set and the other does not.
Affected Versions
Linux kernel 6.17 through Linux kernel 7.0-rc5 (confirmed).
Call Path
The vulnerability is triggered through the following call chain: mseal(2) → do\_mseal() in mm/mseal.c → mseal\_apply() → vma\_modify\_flags() in mm/vma.c → vma\_modify() → vma\_merge\_existing\_range(), where the VM\_WARN\_ON\_VMG assertion fires at line 830.
Root Cause
do\_mseal() calls vma\_modify\_flags() with the original mseal() start address without clamping it to the current VMA's vm\_start when the mseal range spans two VMAs with different VM\_SEALED states. This causes vma\_merge\_existing\_range() to receive an inconsistent vmg state, triggering the assertion: vmg->start != middle->vm\_start. github
Security Relevance
The bug is reachable from unprivileged userspace (UID 1000, no capabilities required — only memfd\_create, mmap, and mseal syscalls are needed). Since mseal(2) is itself a security primitive protecting VMA immutability, an invariant violation in its application logic means VM\_SEALED may be applied incorrectly when spanning VMAs with mixed seal states, potentially undermining the security guarantee mseal provides. In production kernels where WARN compiles to a no-op, the inconsistent vmg state proceeds silently — the VMA tree could be left with incorrect seal state without any visible error.
Exploitation Characteristics
- Access required: Unprivileged (UID 1000, no CAP\_\*)
- Reproducibility: 100% deterministic, triggers in under 1 second, no fault injection needed
- Impact: Silent corruption of VMA seal state in production kernels, potentially allowing sealed memory regions to be incorrectly modified

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040003)

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