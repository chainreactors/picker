---
title: [REVIVE-SA-2026-004] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Nov/23
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.749102
---

# [REVIVE-SA-2026-004] Revive Adserver Vulnerabilities

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
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# [REVIVE-SA-2026-004] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Thu, 12 Nov 2026 18:56:21 +0100

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2026-004
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2026-004
------------------------------------------------------------------------
Date:                  2026-11-11
Risk Level:            Medium to High
Applications affected: Revive Adserver
Versions affected:     <= 6.0.8
Versions not affected: >= 6.0.9
Website:               https://www.revive-adserver.com/
========================================================================

========================================================================
1. Blind SQL injection through inconsistent request precedence
========================================================================
Vulnerability Type:    CWE-89: SQL Injection
CVE-ID:                CVE-2026-107662
Risk level:            High
CVSS Base Score:       8.8
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member sh4d0byss reported blind SQL injection in the
banner-zone and campaign-zone administration pages. Permission checks
and database queries could use different values for the same request
parameter. A restricted manager could exploit this mismatch to extract
arbitrary database values, including password hashes and active session
identifiers. Reusing an extracted, unexpired administrator session can
grant administrative access and the ability to modify configuration or
disrupt ad delivery.

```
Resolution
----------
```

The fix combines the request-precedence correction described in the
authorization bypass finding with changes to the common input helpers.
Global input registration and query-side helpers now both read POST
values before GET values, ensuring that permission checks and database
queries use the same identifiers. Cookies are excluded from this input
path, removing dependence on the PHP request\_order configuration. Both
changes are required to close the reported input-source mismatch.

```
References
----------
https://hackerone.com/reports/3896779
https://github.com/revive-adserver/revive-adserver/commit/e301dbbb7
https://github.com/revive-adserver/revive-adserver/commit/0aa9d0124
https://cwe.mitre.org/data/definitions/89.html

========================================================================
2. Authorization bypass through inconsistent request precedence
========================================================================
```

Vulnerability Type: CWE-639: Authorization Bypass Through
User-Controlled Key

```
CVE-ID:                CVE-2026-107247
Risk level:            High
CVSS Base Score:       8.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member kushbafti reported an authorization bypass
affecting multiple administration pages in Revive Adserver 6.0.0 through
6.0.8. The regression was introduced in commit 156dee7bc during
input-helper simplification. Version 5.5.3 retains the original
POST-first behavior and is not affected by this regression. Object
identifiers used for permission checks were read with GET precedence,
while form submissions could select different objects through POST
parameters. A manager could supply identifiers belonging to their own
agency in the URL and another agency in the submitted form, allowing
unauthorized changes, campaign reassignment and access to other
agencies' inventory.

```
Resolution
----------
```

Global input registration now gives POST parameters precedence over GET
parameters, so permission checks and submitted form values use the same
object identifiers.

```
References
----------
https://hackerone.com/reports/3831102
https://github.com/revive-adserver/revive-adserver/commit/e301dbbb7
https://github.com/revive-adserver/revive-adserver/commit/156dee7bc
https://cwe.mitre.org/data/definitions/639.html

========================================================================
3. Reflected XSS in conversion statistics
========================================================================
Vulnerability Type:    CWE-79: Cross-site Scripting
CVE-ID:                CVE-2026-108558
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member Patrick Lang (7YR) reported a reflected XSS
vulnerability in the conversion-statistics pages. An incorrect ownership
check used the advertiser identifier in place of the website identifier,
allowing crafted website input to reach the page output. An attacker can
send a crafted URL to an authenticated user and execute JavaScript in
that user's browser. A related hour-parameter output issue is addressed
by the same fix.

```
Resolution
----------
```

Website ownership checks now validate the correct identifier, and the
hour parameter is normalised to an integer before formatting.

```
References
----------
https://hackerone.com/reports/3878649
https://github.com/revive-adserver/revive-adserver/commit/b9fd9b04b
https://cwe.mitre.org/data/definitions/79.html

========================================================================
4. Reflected XSS in iframe invocation dimensions
========================================================================
Vulnerability Type:    CWE-79: Cross-site Scripting
CVE-ID:                CVE-2026-108559
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
------------------------------------------------------------------------

Description
-----------
```

HackerOne community member Adam Rayyan Aryasatya (kannrisha) reported
reflected XSS in the iframe invocation options. The frame\_width and
frame\_height request parameters could be included in HTML attributes
without appropriate encoding when generating invocation tags for an
any-size zone. An attacker can send a crafted URL to an authenticated
user to execute JavaScript in that user's browser.

```
Resolution
----------
```

Width and height values are now HTML-encoded when included in
invocation-option form fields.

```
References
----------
https://hackerone.com/reports/3908050
https://github.com/revive-adserver/revive-adserver/commit/9643f44dc
https://cwe.mitre.org/data/definitions/79.html

========================================================================
5. Unauthenticated reflected XSS in update history
========================================================================
Vulnerability Type:    CWE-79: Cross-site Scripting
CVE-ID:                CVE-2026-108560
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/P...