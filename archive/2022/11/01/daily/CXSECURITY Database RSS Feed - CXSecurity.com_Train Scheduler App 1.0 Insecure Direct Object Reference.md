---
title: Train Scheduler App 1.0 Insecure Direct Object Reference
url: https://cxsecurity.com/issue/WLB-2022100072
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:42.904126
---

# Train Scheduler App 1.0 Insecure Direct Object Reference

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
|  |  | |  | | --- | | **Train Scheduler App 1.0 Insecure Direct Object Reference** **2022.10.31**  Credit:  **[Rohit Sharma](https://cxsecurity.com/author/Rohit%2BSharma/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Train Scheduler App v1.0 - Insecure Direct Object Reference (IDOR) to "delete user id "
# Exploit Author: Rohit Sharma
# Vendor Name: oretnom23
# Vendor Homepage: https://www.sourcecodester.com/php/15720/train-scheduler-app-using-php-oop-and-mysql-database-free-download.html
# Software Link: https://www.sourcecodester.com/php/15720/train-scheduler-app-using-php-oop-and-mysql-database-free-download.html
# Version: v1.0
# Tested on: window, xampp ,apache
vulnerability description:- Train Scheduler App suffers from an Insecure Direct Object Reference (IDOR) vulnerability
Vulnerable Parameters:
action , id
how to reproduce this vulnerabilty:-
1:- host this web on local host
2:- go to this url http://127.0.0.1/train\_scheduler\_app/
3:- add random number to generate schedule list i creted alot list to testing this application
4:- go this url http://127.0.0.1/train\_scheduler\_app/?action=delete&id=5
5:- id parameter is vulnerbale for idor change this to increasing number to delet user schedule list 5>>6>>7>>8 etc

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100072)

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