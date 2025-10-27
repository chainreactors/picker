---
title: WebMethods Integration Server 10.15.0.0000-0092 Improper Access on Login Page
url: https://cxsecurity.com/issue/WLB-2025050017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-07
fetch_date: 2025-10-06T22:23:20.335571
---

# WebMethods Integration Server 10.15.0.0000-0092 Improper Access on Login Page

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
|  |  | |  | | --- | | **WebMethods Integration Server 10.15.0.0000-0092 Improper Access on Login Page** **2025.05.06**  Credit:  **[Rasime Ekici](https://cxsecurity.com/author/Rasime%2BEkici/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: WebMethods Integration Server 10.15.0.0000-0092 - Improper Access on Login Page
# Date: 25-01-2024
# Exploit Author: Rasime Ekici
# Vendor Homepage: www.softwareag.com
# Version: 10.15.0000-0092
# Tested on: 10.15.0000-0092
# CVE : 2024-23733
Description:
The /WmAdmin/,/invoke/vm.server/login login page in the Integration Server in Software AG webMethods 10.15.0 before Core Fix7 allows remote attackers to reach the administration panel,discovering server hostname and version information by sending arbitary username and blank password to the /WmAdmin/#/login/ uri
Interpret the http traffic and send a dummy username with blank password on login screen and drop the request to "/admin/navigation/license" to not logged out.Thus you may able to see:
-real hostname of the installed server
-version info
-administrative api endpoints

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050017)

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