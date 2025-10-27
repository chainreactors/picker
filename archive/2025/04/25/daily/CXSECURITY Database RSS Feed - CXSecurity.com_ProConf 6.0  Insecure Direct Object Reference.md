---
title: ProConf 6.0  Insecure Direct Object Reference
url: https://cxsecurity.com/issue/WLB-2025040037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:28.302438
---

# ProConf 6.0  Insecure Direct Object Reference

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
|  |  | |  | | --- | | **ProConf 6.0 Insecure Direct Object Reference** **2025.04.24**  Credit:  **[S. M. Zia Ur Rashid](https://cxsecurity.com/author/S.%2BM.%2BZia%2BUr%2BRashid/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2018-16606](https://cxsecurity.com/cveshow/CVE-2018-16606/ "Click to see CVE-2018-16606")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "CWE-200")**  CVSS Base Score: **4/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Partial**  Integrity impact: **None**  Availability impact: **None** | |

# Exploit Title: ProConf 6.0 - Insecure Direct Object Reference (IDOR)
# Date: 19/07/2018
# Exploit Author: S. M. Zia Ur Rashid, SC
# Author Contact: https://www.linkedin.com/in/ziaurrashid/
# Vendor Homepage: http://proconf.org & http://myproconf.org
# Version: <= 6.0
# Tested on: Windows
# CVE : CVE-2018-16606
# Patched Version: 6.1
# Description:
In ProConf before 6.1, an Insecure Direct Object Reference (IDOR) allows
any author to view and grab all submitted papers (Title and Abstract) and
their authors' personal information (Name, Email, Organization, and
Position) by changing the value of Paper ID (the pid parameter).
# PROOF-OF-CONCEPT
Step 1: Sign In as an author for a conference & submit a paper. Youall get
a paper ID.
Step 2: Now go to paper details and change the value of Paper ID (param
pid=xxxx) to nearest previous value to view others submitted paper &
authors information.
http:// <http:>
[host]/conferences/[conference-name]/author/show\_paper\_details.php?pid=xxxx

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040037)

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