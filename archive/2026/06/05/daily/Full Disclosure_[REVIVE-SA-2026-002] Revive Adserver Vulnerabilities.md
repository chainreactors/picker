---
title: [REVIVE-SA-2026-002] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Jun/0
source: Full Disclosure
date: 2026-06-05
fetch_date: 2026-06-06T05:51:34.847550
---

# [REVIVE-SA-2026-002] Revive Adserver Vulnerabilities

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
![Next](/images/right-icon-16x16.png)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [REVIVE-SA-2026-002] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Wed, 3 Jun 2026 15:43:47 +0200

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2026-002
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2026-002
------------------------------------------------------------------------
Date: 2026-06-03
Risk Level: Medium to High
Applications affected: Revive Adserver
Versions affected: <= 6.0.6
Versions not affected: >= 6.0.7
Website: https://www.revive-adserver.com/
========================================================================

========================================================================
1. Improper Access Control
========================================================================
Vulnerability Type: CWE-284: Improper Access Control
CVE-ID: CVE-2026-34912
Risk level: Medium
CVSS Base Score: 4.3
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Ahmed Ghadban (DarkyOS) has reported that
proper access control is missing when linking banners or campaigns to a
zone through the ‘zone-include.php` script of Revive Adserver 6.0.6 and
earlier, or via its API. A low‑privileged user could link their zones to
banners or campaigns owned by other managers on the same instance,
resulting in inconsistent ownership relationships.

```
Resolution
----------
```

Same‑manager ownership of banners and campaigns is now verified when the
link is added.

```
References
----------
https://hackerone.com/reports/3650504
https://github.com/revive-adserver/revive-adserver/commit/e1c9b8478
https://cwe.mitre.org/data/definitions/284.html

========================================================================
2. Improper Access Control
========================================================================
Vulnerability Type: CWE-284: Improper Access Control
CVE-ID: CVE-2026-34913
Risk level: Medium
CVSS Base Score: 4.3
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Ahmed Ghadban (DarkyOS) has reported a
missing access control check when linking trackers to campaigns through
the `campaign-trackers.php` script of Revive Adserver 6.0.6 and earlier.
A low‑privileged user could link their trackers to campaigns owned by
other managers on the same instance, resulting in inconsistent ownership

```
relationships.

Resolution
----------
```

Ownership validation has been added to ensure that campaigns can only be
linked to trackers owned by the same advertiser.

```
References
----------
https://hackerone.com/reports/3650582
https://github.com/revive-adserver/revive-adserver/commit/f1b5e8504
https://cwe.mitre.org/data/definitions/284.html

========================================================================
3. Blind SQL Injection
========================================================================
Vulnerability Type: CWE-89: SQL Injection
CVE-ID: CVE-2026-34914
Risk level: High
CVSS Base Score: 8.3
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:H
========================================================================

Description
-----------
```

HackerOne community member Kaushalendra Dubey (titanrain) has reported a
missing sanitisation of user input in the `zone-include.php` script of
Revive Adserver 6.0.6 and earlier. A low‑privileged user could exploit
the `clientid` parameter to perform blind SQL injection attacks.

```
Resolution
----------
```

Input sanitisation has been improved to ensure that all parameters
processed by the script are properly validated.

```
References
----------
https://hackerone.com/reports/3653196
https://github.com/revive-adserver/revive-adserver/commit/b541d1d05
https://cwe.mitre.org/data/definitions/89.html

========================================================================
4. Reflected XSS
========================================================================
Vulnerability Type: CWE-79: Cross-site Scripting
CVE-ID: CVE-2026-34915
Risk level: Medium
CVSS Base Score: 6.1
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Kaushalendra Dubey (titanrain) has reported a
missing sanitisation of user input in the `zone-include.php` script of
Revive Adserver 6.0.6 and earlier. A low‑privileged user could exploit
the `clientid` parameter to perform reflected XSS attacks.

```
Resolution
----------
```

Input sanitisation has been improved to ensure that all parameters
processed by the script are properly validated.

```
References
----------
https://hackerone.com/reports/3653316
https://github.com/revive-adserver/revive-adserver/commit/b541d1d05
https://cwe.mitre.org/data/definitions/79.html

========================================================================
5. Remote Code Execution
========================================================================
Vulnerability Type: CWE-94: Code Injection
CVE-ID: CVE-2026-34916
Risk level: High
CVSS Base Score: 8.8
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
========================================================================

Description
-----------
```

HackerOne community member 0x4c616e has reported a missing validation of
user input when saving delivery limitations in Revive Adserver 6.0.6 and
earlier. A low‑privileged user could use the logical parameter to inject
malicious PHP code into the `compiledlimitations` field, which would
then be executed during banner delivery.

```
Resolution
----------
```

Input sanitisation has been improved to ensure that the parameter is
properly validated.

```
References
----------
https://hackerone.com/reports/3656781
https://github.com/revive-adserver/revive-adserver/commit/de3525e12
https://cwe.mitre.org/data/definitions/94.html

========================================================================
6. Improper Authentication
========================================================================
Vulnerability Type: CWE-287: Improper Authentication
CVE-ID: CVE-2026-34917
Risk level: Medium
CVSS Base Score: 4.3
CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
========================================================================

Description
-----------
```

HackerOne community member 0x4c616e has reported that low‑privileged
session IDs generated for the web admin console could be reused in the
XML‑RPC API, whose authentication is normally restricted to admin users.
An attacker could leverage this to gain unauthorised access and exploit
API‑level vulnerabilities.

```
Resolution
----------
```

The session context (web/API) is now recorded along with other session
data, preventing session IDs from being used interchangeably.

```
References
----------
https://hackerone.com/reports/3672641
https://github.com/revive-adserver/revive-a...