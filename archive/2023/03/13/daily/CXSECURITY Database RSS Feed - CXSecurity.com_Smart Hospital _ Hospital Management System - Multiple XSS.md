---
title: Smart Hospital : Hospital Management System - Multiple XSS
url: https://cxsecurity.com/issue/WLB-2023030031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-13
fetch_date: 2025-10-04T09:23:05.367152
---

# Smart Hospital : Hospital Management System - Multiple XSS

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
|  |  | |  | | --- | | **Smart Hospital : Hospital Management System - Multiple XSS** **2023.03.12**  **![in](https://cert.cx/cxstatic/images/flags/in.png) [Eren Arslan](https://cxsecurity.com/author/Eren%2BArslan/1/) **(IN)** ![in](https://cert.cx/cxstatic/images/flags/in.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Title: Smart Hospital : Hospital Management System - Multiple XSS
# Author: @Eawhitehat - Eren Arslan
# Demo available : https://demo.smart-hospital.in/frontend
# CVE: N/A
# XSS
# Screenshot : https://prnt.sc/2vL46MTZ3ktK
Used Payload :
}}</script><script>alert(/eawhitehat is here/);</script></body></html><!--
Method :
Connect to panel with "SUPER ADMIN" : https://demo.smart-hospital.in/site/login#
#Vulnerabîlity
1. After login with SUPER ADMIN, go to https://demo.smart-hospital.in/admin/visitors#
2. Add "New Visitor" and paste the payload in category NAME and NOTE
3. Reload the Category List page and welcome your XSS
Affected page :
All page !

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030031)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -2

0%

100%

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