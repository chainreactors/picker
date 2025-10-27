---
title: needyamin Library Card System Registration Page signup.php cross site scripting
url: https://cxsecurity.com/issue/WLB-2025020016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-25
fetch_date: 2025-10-06T20:32:30.452104
---

# needyamin Library Card System Registration Page signup.php cross site scripting

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
|  |  | |  | | --- | | **needyamin Library Card System Registration Page signup.php cross site scripting** **2025.02.24**  **![bd](https://cert.cx/cxstatic/images/flags/bd.png) [Maloy Roy Orko](https://cxsecurity.com/author/Maloy%2BRoy%2BOrko/1/) **(BD)** ![bd](https://cert.cx/cxstatic/images/flags/bd.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-0844](https://cxsecurity.com/cveshow/CVE-2025-0844/ "Click to see CVE-2025-0844")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** inurl: signup.php](https://cxsecurity.com/dorks/)** | |

Title of the Vulnerability: Library-Card-System | Stored Cross Site Scripting In signup.php |
Finder & Exploit Owner: Maloy Roy Orko
Vulnerability Class: Stored Cross Site Scripting
Product Name: Library-Card-System
Vendor: Needyamin
Type: Library-Card-System
Vulnerable Product Link: https://github.com/needyamin/Library-Card-System/
Vendor Link:
https://github.com/needyamin/
Affected Components: /signup.php
In Short:
Stored Cross Site Scripting Vulnerability Found By Maloy Roy Orko At /signup.php In Library-Card-System 1.0(Vendor: Needyamin).The Sign Up Fields In (/signup.php) Don't Validate Or Sanitize The User Inputs Even No Defense Against XSS.So,The Fields Can Be Used To Execute Malicious JavaScript Commands.
Suggested Description:
Stored Cross Site Scripting in "/signup.php" in "Library-Card-System application By needyamin v 1.0" Found By "Maloy Roy Orko" allows "remote" attacker "To Execute Malicious JavaScript Commands Because User Can Register With XSS Payloads & JavaScript Codes" via "/admindashboard.php & card.php".
Attack Vectors:
To exploit vulnerability,he has to register with xss payloads in signup fields like name,book in /signup.php.Thus, Attacker can execute malicious JavaScript codes in /admindashboard.php & /card.php!
Detailed Blog:
https://www.websecurityinsights.my.id/2025/01/library-card-system-stored-cross-site.html?m=1

**##### References:**

https://www.websecurityinsights.my.id/2025/01/library-card-system-stored-cross-site.html?m=1

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020016)

[Tweet](https://twitter.com/share)

Vote for this issue:
 3
 -1

75%

25%

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