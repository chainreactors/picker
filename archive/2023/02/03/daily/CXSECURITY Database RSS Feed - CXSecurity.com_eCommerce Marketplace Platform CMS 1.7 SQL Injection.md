---
title: eCommerce Marketplace Platform CMS 1.7 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-03
fetch_date: 2025-10-04T05:33:07.664737
---

# eCommerce Marketplace Platform CMS 1.7 SQL Injection

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
|  |  | |  | | --- | | **eCommerce Marketplace Platform CMS 1.7 SQL Injection** **2023.02.02**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

┌┌───────────────────────────────────────────────────────────────────────────────────────┐
││ C r a C k E r ┌┘
┌┘ T H E C R A C K O F E T E R N A L M I G H T ││
└───────────────────────────────────────────────────────────────────────────────────────┘┘
┌──── From The Ashes and Dust Rises An Unimaginable crack.... ────┐
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ [ Vulnerability ] ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: Author : CraCkEr :
│ Website : mybizcms.com │
│ Vendor : MyBizCMS │
│ Software : Emporium Multi-Vendor - eCommerce Marketplace Platform CMS 1.7 │
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
CryptoJob (Twitter) twitter.com/0x0CryptoJob
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ © CraCkEr 2023 ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Path: /categories/phones
/categories/phones?min\_price=2485[SQLI]&max\_price=145000[SQLI]&brand[]=16&review\_ratings=5&a4tech-brand[]=50[SQLI]&battery[]=44[SQLI]&storage[]=41[SQLI]&display[]=37[SQLI]&performance[]=36[SQLI]&attribute3[]=7[SQLI]
GET parameter 'min\_price' is vulnerable to SQLI
GET parameter 'max\_price' is vulnerable to SQLI
GET parameter 'a4tech-brand[]' is vulnerable to SQLI
GET parameter 'battery[]' is vulnerable to SQLI
GET parameter 'display[]' is vulnerable to SQLI
GET parameter 'performance[]' is vulnerable to SQLI
GET parameter 'attribute3[]' is vulnerable to SQLI
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020007)

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