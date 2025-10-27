---
title: Image_Gallery | view.php?username= | Cross Site Scripting (Reflected XSS) | Found By Maloy Roy Orko
url: https://cxsecurity.com/issue/WLB-2025020014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-25
fetch_date: 2025-10-06T20:32:34.775573
---

# Image_Gallery | view.php?username= | Cross Site Scripting (Reflected XSS) | Found By Maloy Roy Orko

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
|  |  | |  | | --- | | **Image\_Gallery | view.php?username= | Cross Site Scripting (Reflected XSS) | Found By Maloy Roy Orko** **2025.02.24**  **![bd](https://cert.cx/cxstatic/images/flags/bd.png) [Maloy Roy Orko](https://cxsecurity.com/author/Maloy%2BRoy%2BOrko/1/) **(BD)** ![bd](https://cert.cx/cxstatic/images/flags/bd.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-0721](https://cxsecurity.com/cveshow/CVE-2025-0721/ "Click to see CVE-2025-0721")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** inurl: view.php?username=](https://cxsecurity.com/dorks/)** | |

Title of the Vulnerability: Image\_Gallery | view.php?username= | Cross Site Scripting (Reflected XSS) | Found By Maloy Roy Orko
Product Name: image\_gallery
Product Type: Image Gallery Management System
Finder & Exploit Owner: Maloy Roy Orko
Vulnerability Class: Reflected Cross Site Scripting
Vendor:
needyamin
Vendor Link:
https://github.com/needyamin/
Vulnerable Product Link: https://github.com/needyamin/image\_gallery/
Affected Components:
view.php?username=
Suggested Description:
Reflected XSS in "view.php?username=" in "image\_gallery application By needyamin v 1.0" Found By "Maloy Roy Orko" allows "remote" attacker "to execute malicious JavaScript code via XSS as no validations are provided and can get cookies of admin" via "view.php?username=".
Attack Vectors:
To exploit vulnerability,he has to input XSS exploits via view.php?username= and then he can give the links to their targets even Admin and when targets click it! Attacker can gain admin cookie and then he can login admin and as the file upload isn't protected can hijack the whole server too!He can even execute malicious JavaScript codes into visitors browser via this vulnerability.
Detailed Blog:
https://www.websecurityinsights.my.id/2025/01/imagegallery-viewphpusername-cross-site.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020014)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
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