---
title: Weak Password Complexity - elggv6.3.3
url: https://seclists.org/fulldisclosure/2026/Jan/29
source: Full Disclosure
date: 2026-01-29
fetch_date: 2026-01-30T04:04:26.243843
---

# Weak Password Complexity - elggv6.3.3

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# Weak Password Complexity - elggv6.3.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sat, 24 Jan 2026 18:01:43 +0000

---

```
# Exploit Title: Elgg - Lack of Password Complexity
# Date: 1/2026
# Exploit Author: Andrey Stoykov
# Version: 6.3.3
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2026/01/friday-fun-pentest-series-48-weak.html

// HTTP Request - Changing Password

POST /action/usersettings/save HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 216
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/settings/user/admin
Cookie: Elgg=5ivi0vt1g9jqu1sju70hfnm0mc
Upgrade-Insecure-Requests: 1
Priority: u=0, i

__elgg_token=nIY_M_wh53bUxoHvuKO1YA&__elgg_ts=1769266299&username=admin&name=Admin+User&email_password=&email=
admin () example com
&current_password=[REDACTED]&password=Passw0rd%21&password2=Passw0rd%21&language=en&guid=46

// HTTP Response - Changing Password

HTTP/1.1 302 Found
Date: Sat, 24 Jan 2026 14:52:07 GMT
Server: Apache/2.4.52 (Ubuntu)
Cache-Control: must-revalidate, no-cache, no-store, private
expires: Thu, 19 Nov 1981 08:52:00 GMT
pragma: no-cache
Location: http://elgg.local/settings/user/admin
Vary: User-Agent
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
Content-Length: 394

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url='
http://elgg.local/settings/user/admin'"; />

        <title>Redirecting to http://elgg.local/settings/user/admin</title>
    </head>
    <body>
        Redirecting to <a href="http://elgg.local/settings/user/admin";>
http://elgg.local/settings/user/admin</a>.
    </body>
</html>

// HTTP Request - Changing Password - Following Redirect

GET /settings/user/admin HTTP/1.1
Host: elgg.local
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0)
Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
Origin: http://elgg.local
Sec-GPC: 1
Connection: keep-alive
Referer: http://elgg.local/action/usersettings/save
Cookie: Elgg=5ivi0vt1g9jqu1sju70hfnm0mc
Upgrade-Insecure-Requests: 1
Priority: u=0, i

// HTTP Response - Changing Password - Following Redirect

HTTP/1.1 200 OK
Date: Sat, 24 Jan 2026 14:52:11 GMT
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
Content-Length: 27859

[...]
<div class="elgg-message elgg-message-success"><div class="elgg-inner"><div
class="elgg-body">Password changed</div></div></div>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

### Current thread:

* **Weak Password Complexity - elggv6.3.3** *Andrey Stoykov (Jan 29)*

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