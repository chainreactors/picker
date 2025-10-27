---
title: Adobe Reader CoolType Out-Of-Bounds Read
url: https://cxsecurity.com/issue/WLB-2025020021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-03-01
fetch_date: 2025-10-06T21:55:46.044705
---

# Adobe Reader CoolType Out-Of-Bounds Read

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
|  |  | |  | | --- | | **Adobe Reader CoolType Out-Of-Bounds Read** **2025.02.28**  Credit:  **[Mjurczyk](https://cxsecurity.com/author/Mjurczyk/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

The Type1/CFF CharString interpreter code in the Adobe Reader CoolType.dll font library does not check if the input stream pointer has not gone beyond the end of the source buffer, which stores the state machine instructions.
The unbounded reads can happen:
1) At the beginning of the VM execution loop (reading main opcode).
2) While reading the second opcode byte in case of the 'escape' instruction.
3) While reading the 'extendedmbr' instruction parameter, or the 16/32-bit numeric value to be pushed onto the interpreter stack.
This may result in the following outcomes:
1) The parser reads garbage, uninitialized or left-over data and interprets them as CharString instructions.
2) The parser reaches the end of a mapped memory page and attempts to read bytes beyond it, consequently resulting in a crash of the sandboxed AcroRd32.exe process.
Neither scenario is a serious security threat (contrary to an equivalent bug filed on Windows Kernel ATMFD.DLL, which can lead to global system crash or information disclosure), so this bug is filed just as a general note on the code quality of the CharString interpreter in CoolType. Adobe Reader 11.0.10 is confirmed to be affected, but we expect all prior versions of the software to be prone to the bug, too.
Due to minimal severity of the issue, we have not developed a proof of concept.
This bug is subject to a 90 day disclosure deadline. If 90 days elapse without a broadly available patch, then the bug report will automatically become visible to the public.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020021)

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