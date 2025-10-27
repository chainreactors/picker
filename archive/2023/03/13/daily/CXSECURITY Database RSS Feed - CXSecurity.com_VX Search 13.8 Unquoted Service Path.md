---
title: VX Search 13.8 Unquoted Service Path
url: https://cxsecurity.com/issue/WLB-2023030028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-13
fetch_date: 2025-10-04T09:23:08.013160
---

# VX Search 13.8 Unquoted Service Path

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
|  |  | |  | | --- | | **VX Search 13.8 Unquoted Service Path** **2023.03.12**  Credit:  **[Thurein Soe](https://cxsecurity.com/author/Thurein%2BSoe/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-24671](https://cxsecurity.com/cveshow/CVE-2023-24671/ "Click to see CVE-2023-24671")**  CWE: **[CWE-428](https://cxsecurity.com/cwe/CWE-428 "Click to see CWE-428")** | |

Executive Summary:
Product Name: VX Search
Vendor Home Page: https://www.vxsearch.com/
Affected Version(s): VX Search v13.8
Fixed Version: all versions later v13.8
Vulnerability Type: Unquoted Search Path (CWE-428)
CVE Reference: CVE-2023-24671
Credit: Thurein Soe
Vendor Description:
VX Search is an automated, rule-based file search solution allowing one to
search files by file type, category, file name, size, location, extension,
regular expressions, text and binary patterns.
Vulnerability description:
VX Search v13.8 was discovered to contain an unquoted service path
vulnerability which allows attackers to execute arbitrary commands.
However, this could not lead to a fully local privilege escalation attack.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030028)

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