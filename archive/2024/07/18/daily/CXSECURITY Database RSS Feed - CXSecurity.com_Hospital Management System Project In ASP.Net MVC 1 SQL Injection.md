---
title: Hospital Management System Project In ASP.Net MVC 1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024070034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-18
fetch_date: 2025-10-06T17:38:31.879009
---

# Hospital Management System Project In ASP.Net MVC 1 SQL Injection

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
|  |  | |  | | --- | | **Hospital Management System Project In ASP.Net MVC 1 SQL Injection** **2024.07.17**  Credit:  **[0xMykull](https://cxsecurity.com/author/0xMykull/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-40502](https://cxsecurity.com/cveshow/CVE-2024-40502/ "Click to see CVE-2024-40502")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Hospital Management System Project in ASP.Net MVC - SQL
Injection / Authentication Bypass
# Date: 07/16/2024
# Exploit Author: 0xMykull
# Vendor Hompage:
https://itsourcecode.com/free-projects/asp/hospital-management-system-project-in-asp-net-mvc-with-source-code/
# Software Link:
https://itsourcecode.com/free-projects/asp/hospital-management-system-project-in-asp-net-mvc-with-source-code/
# Version: 1
# CVE: CVE-2024-40502
Description:
An SQL injection vulnerability has been discovered in the btn\_login\_b\_Click
function of the affected web application. The vulnerability exists due to
the improper sanitization of user-supplied input in the login form.
Specifically, the txt\_login\_username.Text and txt\_login\_pass.Text fields
are concatenated directly into an SQL query string without proper
parameterization or escaping.
Endpoint: https://localhost:44306/Users/Loginpage.aspx
Bypass Payloads:
(default user)
Username: kihsan'--
password: <anything>
Username: <anyvaliduser>'--
password: <anything>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070034)

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