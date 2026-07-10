---
title: [REVIVE-SA-2026-003] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Jul/19
source: Full Disclosure
date: 2026-07-09
fetch_date: 2026-07-10T06:00:09.226245
---

# [REVIVE-SA-2026-003] Revive Adserver Vulnerabilities

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
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [REVIVE-SA-2026-003] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Tue, 7 Jul 2026 09:20:11 +0200

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2026-003
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2026-003
------------------------------------------------------------------------
Date: 2026-06-25
Risk Level: Medium to High
Applications affected: Revive Adserver
Versions affected: <= 6.0.7
Versions not affected: >= 6.0.8
Website: https://www.revive-adserver.com/
========================================================================

========================================================================
1. Improper Access Control
========================================================================
Vulnerability Type:    CWE-284: Improper Access Control
CVE-ID:                CVE-2026-50739
Risk level:            Medium
CVSS Base Score:       4.3
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member hakuopi (and independently sy2no,
garuthacktvist, and aszh) has reported a bypass of the fix for
CVE‑2026‑34913. Proper ownership validation had not been applied to the
reverse operation of linking campaigns and trackers through the
`tracker-campaigns.php` script in Revive Adserver 6.0.7 and earlier. As
a result, a low‑privileged user could link their trackers to campaigns
owned by other managers on the same instance, leading to inconsistent
ownership relationships.

```
Resolution
----------
```

Ownership validation has been added to ensure that campaigns can only be
linked to trackers owned by the same advertiser.

```
References
----------
https://hackerone.com/reports/3780709
https://github.com/revive-adserver/revive-adserver/commit/c03a0b6d
https://cwe.mitre.org/data/definitions/284.html

========================================================================
2. Reflected XSS
========================================================================
Vulnerability Type:    CWE-79: Cross-site Scripting
CVE-ID:                CVE-2026-50740
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member Mahmoud Khaled (Kanon4) has reported a
missing sanitisation of user input in the `zone-include.php` script of
Revive Adserver 6.0.7 and earlier. A low‑privileged user could exploit
the `refresh` parameter of the iFrame invocation tag to perform
reflected XSS attacks.

```
Resolution
----------
```

Input sanitisation has been improved to ensure that the affected
parameter is properly validated.

```
References
----------
https://hackerone.com/reports/3780806
https://github.com/revive-adserver/revive-adserver/commit/03d9ad8b
https://cwe.mitre.org/data/definitions/79.html

========================================================================
3. Remote Code Execution
========================================================================
Vulnerability Type:    CWE-94: Code Injection
CVE-ID:                CVE-2026-50741
Risk level:            High
CVSS Base Score:       8.8
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
------------------------------------------------------------------------

Description
-----------
```

HackerOne community members Rio Darmawan (riodrwn) and Mikhail Ilin
(doomtech) have independently reported new vectors to bypass the fix for
CVE‑2026‑34916. Variants of such vectors were also reported by phucrio
and offsetmd. The fix could be bypassed either by sending a disallowed
but otherwise valid plugin identifier as `type`, or by using the
`ox.setChannelTargeting` XML‑RPC API method.

```
Resolution
----------
```

Validation of plugin identifiers and XML‑RPC inputs has been
strengthened to prevent unsafe code paths.

```
References
----------
https://hackerone.com/reports/3780854
https://hackerone.com/reports/3781492
https://github.com/revive-adserver/revive-adserver/commit/3d1485de
https://github.com/revive-adserver/revive-adserver/commit/becaf6e7
https://cwe.mitre.org/data/definitions/94.html

========================================================================
4. Stored XSS
========================================================================
Vulnerability Type:    CWE-79: Cross-site Scripting
CVE-ID:                CVE-2026-50742
Risk level:            Medium
CVSS Base Score:       4.4
CVSS Vector:           CVSS:3.0/AV:N/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member Althaf Shajahan (AnGrY) has reported stored
XSS vulnerabilities in the `maintenance-acl-check.php` and
`maintenance-banners-check.php` tools of Revive Adserver 6.0.7. The
issue was caused by entity names being displayed without proper escaping
when inconsistencies were detected. Whether the XSS payload is executed
when an administrator uses the affected maintenance tools is not
entirely under the attacker’s control.

```
Resolution
----------
```

Output encoding has been corrected to ensure entity names are safely
escaped in the affected maintenance tools.

```
References
----------
https://hackerone.com/reports/3781311
https://github.com/revive-adserver/revive-adserver/commit/91abb6ab
https://cwe.mitre.org/data/definitions/79.html

========================================================================
5. Cross-Site Request Forgery
========================================================================
Vulnerability Type:    CWE-352: Cross-Site Request Forgery
CVE-ID:                CVE-2026-50743
Risk level:            Medium
CVSS Base Score:       5.4
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member Althaf Shajahan (AnGrY) has reported that the
`zone-include.php` script in Revive Adserver 6.0.7 was vulnerable to a
CSRF attack. Linking and unlinking banners or campaigns to zones could
be triggered via crafted GET or POST requests without any verification
of the CSRF token, allowing an attacker to perform these actions on
behalf of an authenticated administrator.

```
Resolution
----------
```

CSRF token checks have been added to all link and unlink operations in
`zone-include.php`.

```
References
----------
https://hackerone.com/reports/3781691
https://github.com/revive-adserver/revive-adserver/commit/e3c84d6f
https://cwe.mitre.org/data/definitions/352.html

========================================================================
6. Improper Access Control
========================================================================
Vulnerability Type:    CWE-284: Improper Access Control
CVE-ID:                CVE-2026-50744
Risk level:            Medium
CVSS Base Score:       ...