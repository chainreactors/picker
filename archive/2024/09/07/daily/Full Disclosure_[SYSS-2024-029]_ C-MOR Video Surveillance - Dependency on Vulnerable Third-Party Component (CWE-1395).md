---
title: [SYSS-2024-029]: C-MOR Video Surveillance - Dependency on Vulnerable Third-Party Component (CWE-1395)
url: https://seclists.org/fulldisclosure/2024/Sep/22
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:30:59.781574
---

# [SYSS-2024-029]: C-MOR Video Surveillance - Dependency on Vulnerable Third-Party Component (CWE-1395)

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-029]: C-MOR Video Surveillance - Dependency on Vulnerable Third-Party Component (CWE-1395)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:13:57 +0200

---

```
Advisory ID:               SYSS-2024-029
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401
Tested Version(s):         5.2401
```

Vulnerability Type: Dependency on Vulnerable Third-Party
Component (CWE-1395)
 Use of Unmaintained Third Party Components
(CWE-1104)

```
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2024-04-05
Solution Date:             2024-07-31
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2017-9798, CVE-2017-3167, and more
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

The C-MOR system uses several outdated third-party software components
with known security vulnerabilities.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR system, it was found that the C-MOR system depends
on several outdated third-party software components with known security
vulnerabilities, for instance an old Linux kernel, Apache HTTP Server
2.2.16, PHP 5.3.3, or Python 2.6.

Some of the used software components have also reached their end of life
and are not supported anymore by a maintainer.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The following excerpt of the "dpkg-query" output illustrates some outdated
third-party software components used on the C-MOR system:

$ sudo dpkg-query -l
(...)
```

ii apache2 2.2.16-6+squeeze10
Apache HTTP Server metapackage
ii apache2-mpm-prefork 2.2.16-6+squeeze10
Apache HTTP Server - traditional non-threaded model
ii apache2-utils 2.2.16-6+squeeze10
utility programs for webservers
ii apache2.2-bin 2.2.16-6+squeeze10
Apache HTTP Server common binary files
ii apache2.2-common 2.2.16-6+squeeze10
Apache HTTP Server common files

```
(...)
```

ii libapache2-mod-php5 5.3.3-7+squeeze14
server-side, HTML-embedded scripting language (Apache 2 module)

```
(...)
```

ii libssl0.9.8 0.9.8o-4squeeze14 SSL
shared libraries

```
(...)
```

ii linux-image-4.7.8 c-mor-v5-00
Linux kernel binary image for version 4.7.8

```
(...)
```

ii php5 5.3.3-7+squeeze14
server-side, HTML-embedded scripting language (metapackage)
rc php5-cgi 5.3.3-7+squeeze14
server-side, HTML-embedded scripting language (CGI binary)
ii php5-cli 5.3.3-7+squeeze14
command-line interpreter for the php5 scripting language
ii php5-common 5.3.3-7+squeeze14
Common files for packages built from the php5 source
ii php5-gd 5.3.3-7+squeeze14 GD
module for php5
ii php5-mysql 5.3.3-7+squeeze14
MySQL module for php5
ii php5-suhosin 0.9.32.1-1
advanced protection module for php5

```
(...)
```

ii python2.6 2.6.6-8+b1 An
interactive high-level object-oriented language (version 2.6)
ii python2.6-minimal 2.6.6-8+b1 A
minimal subset of the Python language (version 2.6)

```
(...)

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
[2] SySS Security Advisory SYSS-2024-029

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-029.txt
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Chris Beiter, and Frederik
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
[OpenPGP\_signature.asc](att-22/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **[SYSS-2024-029]: C-MOR Video Surveillance - Dependency on Vulnerable Third-Party Component (CWE-1395)** *Matthias Deeg via Fulldisclosure (Sep 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https...