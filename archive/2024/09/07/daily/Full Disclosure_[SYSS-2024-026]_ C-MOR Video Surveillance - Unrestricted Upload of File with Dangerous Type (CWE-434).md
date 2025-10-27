---
title: [SYSS-2024-026]: C-MOR Video Surveillance - Unrestricted Upload of File with Dangerous Type (CWE-434)
url: https://seclists.org/fulldisclosure/2024/Sep/19
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:08.030919
---

# [SYSS-2024-026]: C-MOR Video Surveillance - Unrestricted Upload of File with Dangerous Type (CWE-434)

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-026]: C-MOR Video Surveillance - Unrestricted Upload of File with Dangerous Type (CWE-434)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:13:27 +0200

---

```
Advisory ID:               SYSS-2024-026
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401
Tested Version(s):         5.2401
```

Vulnerability Type: Unrestricted Upload of File with Dangerous
Type (CWE-434)

```
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2024-04-05
Solution Date:             2024-07-31
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2024-45171
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

Due to improper user input validation, it is possible to upload
dangerous files, for instance PHP code, to the C-MOR system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR web interface, it was found that the
upload functionality for backup files allows an authenticated user to
upload arbitrary files. The only condition is that the file name
contains the string ".cbkf".

Therefore, "webshell.cbkf.php" is considered a valid file name for
the C-MOR web application.

Uploaded files are stored within the directory "/srv/www/backups" on
the C-MOR system and can thus be accessed via the URL
https://<HOST>/backup/upload_<FILENAME>.

Due to broken access control, also low-privileged authenticated users
can use this file upload functionality (see SYSS-2024-024[3]).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

Using the upload functionality for backup files, it is possible to
upload arbitrary PHP code, for instance a simple PHP web shell such
as the following one, in a file named "webshell.cbkf.php":

<?php echo system($_GET['cmd'); ?>

After a successful file upload, the uploaded PHP web shell can be
accessed and used via the following URL, leading to OS command
execution:

https://<HOST>/backup/upload_webshell.cbkf.php?cmd=<COMMAND>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

Install C-MOR Video Surveillance version 6.00PL1.

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
[2] SySS Security Advisory SYSS-2024-026

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-026.txt
[3] SySS Security Advisory SYSS-2024-024

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-024.txt
[4] SySS Responsible Disclosure Policy
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
[OpenPGP\_signature.asc](att-19/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **[SYSS-2024-026]: C-MOR Video Surveillance - Unrestricted Upload of File with Dangerous Type (CWE-434)** *Matthias Deeg via Fulldisclosure (Sep 05)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)*...