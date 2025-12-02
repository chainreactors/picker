---
title: My Admin (Powered By Learning Impact) - SQL Injection Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2025120001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-01
fetch_date: 2025-12-02T03:17:39.941864
---

# My Admin (Powered By Learning Impact) - SQL Injection Authentication Bypass

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
|  |  | |  | | --- | | **My Admin (Powered By Learning Impact) - SQL Injection Authentication Bypass** **2025.12.01**  Credit:  **[6ickzone](https://cxsecurity.com/author/6ickzone/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** intitle:"My Admin" "Powered By Learning Impact"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: My Admin (Powered By Learning Impact) - SQL Injection Authentication Bypass
# Date: 2025-11-26
# Exploit Author: 6ickzone
# Vendor Homepage: https://learningimpactmodel.com/
# Software Link: https://learningimpactmodel.com/siteadmin/index.php
# Category: Webapps
# CWE: CWE-89
---
## Description:
A critical SQL Injection (SQLi) vulnerability was discovered in the sign-in mechanism of the "My Admin" portal, powered by "Learning Impact".
The vulnerability allows an unauthenticated attacker to bypass the login page entirely by manipulating the input fields (Username and/or Password). The application fails to properly neutralize special elements in the input before it is used in the SQL query, leading to an exploitable condition.
### Proof of Concept (PoC):
An attacker can utilize the following generic payload in the Username field to inject a condition that forces the WHERE clause to evaluate as true, bypassing the required password check.
\*\*Payload:\*\* `' OR 1=1 LIMIT 1 -- -+`
When the server processes this input, the resulting SQL query authenticates the attacker as the first user found in the database (often an Administrator or the highest-privileged account), granting unauthorized access to the administration panel.
### Mitigation:
Developers must implement \*\*Prepared Statements (Parameterized Queries)\*\* to ensure all user input is treated as data, not executable code. Additionally, implementing input validation and adopting the principle of least privilege for the database connection are strongly recommended to prevent this class of attack.

**##### References:**

http://0x6ick.zone.id

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120001)

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