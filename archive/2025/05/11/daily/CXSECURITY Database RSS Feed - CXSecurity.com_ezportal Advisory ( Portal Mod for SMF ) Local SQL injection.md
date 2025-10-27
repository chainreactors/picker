---
title: ezportal Advisory ( Portal Mod for SMF ) Local SQL injection
url: https://cxsecurity.com/issue/WLB-2025050029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-11
fetch_date: 2025-10-06T22:24:11.957760
---

# ezportal Advisory ( Portal Mod for SMF ) Local SQL injection

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
|  |  | |  | | --- | | **ezportal Advisory ( Portal Mod for SMF ) Local SQL injection** **2025.05.10**  Credit:  **[Emiliano Febbi](https://cxsecurity.com/author/Emiliano%2BFebbi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** inurl:index.php?action=ezportal](https://cxsecurity.com/dorks/)** | |

# Exploit Title: ezportal Advisory ( Portal Mod for SMF ) Local SQL injection
# Google Dork: inurl:index.php?action=ezportal
# Date: 2025-05-08
# Exploit Author: Emiliano Febbi
# Vendor Homepage: https://www.ezportal.com/
# Software Link: https://custom.simplemachines.org/index.php?mod=1461
# Version: v5.6 (latest version)
# Tested on: Windows 10
###############
# Explication:#
###############
ezportal is a portal mod for Simple Machine Forum, if you have it installed this flaw in it presents a database error,
personally tested on the v5.6 version of the portal.
Probably also present on previous ezportal versions.
###############
# Procedure: #
###############
The bug is present once logged in as administrator, and occurs when editing blocks located in the portal index.
the error generated is the classic database error, exploitable with SQL injection.
################
# Execution: #
################
This is the bugged Query:
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\* index.php?action=ezportal;sa=editblock;block=-1 \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
<-- You can execute this after admin login. I don't know if it can be exploited, but it's still a flaw. -->

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050029)

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