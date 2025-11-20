---
title: [REVIVE-SA-2025-004] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2025/Nov/21
source: Full Disclosure
date: 2025-11-19
fetch_date: 2025-11-20T03:10:22.335802
---

# [REVIVE-SA-2025-004] Revive Adserver Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [REVIVE-SA-2025-004] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Wed, 19 Nov 2025 15:26:12 +0100

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2025-004
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2025-004
------------------------------------------------------------------------
Date:                  2025-11-19
Risk Level:            Medium
Applications affected: Revive Adserver
Versions affected:     <= 6.0.2
Versions not affected: >= 6.0.3
Website:               https://www.revive-adserver.com/
========================================================================

========================================================================
Vulnerability 1: Stored XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2025-55126
Risk Level:            Medium
CVSS Base Score:       6.5
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Dang Hung Vi (vidang04) has reported a stored
XSS vulnerability involving the navigation box at the top of
advertiser-related pages, with campaign names being the vector for the
stored XSS.

```
Details
-------
```

Advertiser/campaign names dynamically loaded via the
“inventory-retrieve.php” script were not properly escaped before being
displayed on the screen.

```

```

A manager user could craft campaign names to cause the script to execute
malicious JS code when using the navigation box at the top of the page
to switch between advertisers and campaigns. Successful exploitation
requires an attacker to trick a logged-in administrator into visiting
specific pages, and also performing some actions, such as switching
advertiser and campaigns using the navigation box. Most importantly, the
session cookie cannot be accessed or stolen via JavaScript, so the
disruption would be limited.

```
References
----------
https://hackerone.com/reports/3411750
https://github.com/revive-adserver/revive-adserver/commit/8053286
https://cwe.mitre.org/data/definitions/79.html

========================================================================
Vulnerability 2: Improper Neutralization of Whitespace
========================================================================
Vulnerability Type:    Improper Neutralization of Whitespace [CWE-156]
CVE-ID:                CVE-2025-52672
Risk Level:            Medium
CVSS Base Score:       5.4
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Dao Hoang Anh (yoyomiski) has reported an
improper neutralization of whitespace in the username when adding new
users. A username with leading or trailing whitespace could be virtually
indistinguishable from its legitimate counterpart when the username is
displayed in the UI, potentially leading to confusion.

```
Details
-------
```

Username validation was not preventing whitespace characters from being
used. An attacker with user creation permissions could specifically
craft a username with leading or trailing whitespace and trick an admin
user to grant specific permissions to it rather than the legitimate user.

```
References
----------
https://hackerone.com/reports/3413764
https://github.com/revive-adserver/revive-adserver/commit/9b963ac
https://cwe.mitre.org/data/definitions/156.html

========================================================================
Vulnerability 3: Uncontrolled Resource Consumption
========================================================================
Vulnerability Type:    Allocation of Resources Without Limits or
                       Throttling [CWE-770]
CVE-ID:                CVE-2025-55128
Risk Level:            Medium
CVSS Base Score:       6.5
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
========================================================================

Description
-----------
```

HackerOne community member Dang Hung Vi (vidang04) has reported an
uncontrolled resource consumption vulnerability in the
“userlog-index.php”. An attacker with access to the admin interface
could request an arbitrarily large number of items per page, potentially
leading to a denial of service.

```
Details
-------
```

The “userlog-index.php” script and some other scripts using the pager
component were not restricting the “setPerPage” parameter, allowing
large number to be injected as “LIMIT” in SQL queries. The user log
table could grow very large on some installations, making the vector
effective for denial of service attacks performed by authenticated users.

```
References
----------
https://hackerone.com/reports/3413890
https://github.com/revive-adserver/revive-adserver/commit/d5141f7
https://cwe.mitre.org/data/definitions/770.html

========================================================================
Solution
========================================================================
```

We recommend updating to the most recent 6.0.3 version of Revive
Adserver, or whatever happens to be the current release at the time of
reading this security advisory.

```
========================================================================
Contact Information
========================================================================

The security contact for Revive Adserver can be reached at:
<security AT revive-adserver DOT com>.
```

Please review <https://www.revive-adserver.com/security/> before doing so.
We only accept security reports through HackerOne.

```
--
Matteo Beccati
On behalf of the Revive Adserver Team
https://www.revive-adserver.com/
```

**Attachment:
[OpenPGP\_0x819BAF32F410D901.asc](att-21/OpenPGP_0x819BAF32F410D901_asc.bin)**
*Description:* OpenPGP public key

**Attachment:
[OpenPGP\_signature.asc](att-21/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **[REVIVE-SA-2025-004] Revive Adserver Vulnerabilities** *Matteo Beccati (Nov 19)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)
...