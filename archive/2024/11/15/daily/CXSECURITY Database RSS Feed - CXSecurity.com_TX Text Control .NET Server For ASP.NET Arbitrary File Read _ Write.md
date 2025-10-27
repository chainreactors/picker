---
title: TX Text Control .NET Server For ASP.NET Arbitrary File Read / Write
url: https://cxsecurity.com/issue/WLB-2024110022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-15
fetch_date: 2025-10-06T19:16:59.319328
---

# TX Text Control .NET Server For ASP.NET Arbitrary File Read / Write

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
|  |  | |  | | --- | | **TX Text Control .NET Server For ASP.NET Arbitrary File Read / Write** **2024.11.14**  Credit:  **[Filip Palian](https://cxsecurity.com/author/Filip%2BPalian/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

Hej,
Let's keep it short ...
=====
Intro
=====
A "sudo make me a sandwich" security issue has been identified in the TX
Text
Control .NET Server for ASP.NET[1].
According to the vendor[2], "the most powerful, MS Word compatible document
editor that runs in all browsers".
Likely all versions are affected however, it was not confirmed.
=====
Issue
=====
It was possible to change the configured system path for reading and writing
files in the underlying operating system with privileges of the user
running a
web application. This could be achieved by calling the setfiledirectory()
function exposed via JavaScript API[3].
===
PoC
===
-- cut --
TXTextControl.setFileDirectory(0, "c:\\")
-- cut --
See also the attached image file for details.
===========
Remediation
===========
Contact the vendor[4] directly for remediation guidance.
========
Timeline
========
14.10.2024: Security contact requested from sales.department@textcontrol.com
.
31.10.2024: CVE requested from MITRE.
......2024: Nobody cares.
12.11.2024: The advisory has been released.
==========
References
==========
[1]
https://www.textcontrol.com/products/asp-dotnet/tx-text-control-dotnet-server/overview/
[2] https://www.textcontrol.com
[3]
https://docs.textcontrol.com/textcontrol/asp-dotnet/ref.javascript.txtextcontrol.setfiledirectory.method.htm
[4] https://www.textcontrol.com/contact/email/general/
Cheers,
Filip Palian

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110022)

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