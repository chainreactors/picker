---
title: Ecommerce-PHP-kurniaramadhan-1.0- Stored Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025010013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-13
fetch_date: 2025-10-06T20:07:27.456688
---

# Ecommerce-PHP-kurniaramadhan-1.0- Stored Cross Site Scripting

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
|  |  | |  | | --- | | **Ecommerce-PHP-kurniaramadhan-1.0- Stored Cross Site Scripting** **2025.01.12**  **![bd](https://cert.cx/cxstatic/images/flags/bd.png) [Maloy Roy Orko](https://cxsecurity.com/author/Maloy%2BRoy%2BOrko/1/) **(BD)** ![bd](https://cert.cx/cxstatic/images/flags/bd.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-13205](https://cxsecurity.com/cveshow/CVE-2024-13205/ "Click to see CVE-2024-13205")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** "Powered by kurniaramadhan"](https://cxsecurity.com/dorks/)** | |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Exploit Title: Ecommerce-PHP-kurniaramadhan-1.0- Stored Cross Site Scripting
#Title of the Vulnerability: Stored Cross Site Scripting
#Product Name: E-Commerce-PHP
#Vendor: https://github.com/kurniaramadhan/
#Vulnerable Product Link: https://github.com/kurniaramadhan/E-Commerce-PHP
#Date: 2025-01-10
#Exploit Author: Maloy Roy Orko
#Google Dork: "Powered by kurniaramadhan"
#Category:Webapps
#Tested On: Android,Mac, Firefox
## Reference:
https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html
https://vuldb.com/?id.290798
###Affected Components: /admin/create\_product.php & /admin/product.php
#Description:
Stored Cross Site Scripting in "/admin/create\_product.php & /admin/product.php" in "E-commerce PHP application By kurniaramadhan v 1.0" allows "remote" attacker "to store XSS payload as create product fields aren't protected" via "/admin/create\_product.php & /admin/product.php".
###Proof of Concept:
### Demo :
http://192.168.1.100:8080/admin/create\_product.php
http://192.168.1.100:8080/admin/product.php
###Attack Vectors:
To exploit vulnerability,he has to input exploits via prodyct name change or create in new name and then he can execute malicious javascript code in the visitors browser,mainly,here XSS can be exploited then.
###Detailed Blog About The Poc:
https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Discovered by: Maloy Roy Orko
#Website: https://www.websecurityinsights.my.id/
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**##### References:**

https://vuldb.com/?id.290798

https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html?m=1

https://nvd.nist.gov/vuln/detail/CVE-2024-13205

https://www.cve.org/CVERecord?id=CVE-2024-13205

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010013)

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