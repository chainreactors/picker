---
title: [REVIVE-SA-2025-003] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2025/Nov/20
source: Full Disclosure
date: 2025-11-19
fetch_date: 2025-11-20T03:10:22.433439
---

# [REVIVE-SA-2025-003] Revive Adserver Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# [REVIVE-SA-2025-003] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Wed, 19 Nov 2025 11:05:36 +0100

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2025-003
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2025-003
------------------------------------------------------------------------
Date:                  2025-11-05
Risk Level:            High
Applications affected: Revive Adserver
Versions affected:     <= 6.0.1, <= 5.5.2
Versions not affected: >= 6.0.2, >= 5.5.3
Website:               https://www.revive-adserver.com/
========================================================================

========================================================================
Vulnerability 1: Authorization bypass
========================================================================
Vulnerability Type:    Improper Access Control [CWE-284]
CVE-ID:                CVE-2025-48986
CVSS Base Score:       8.8
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
========================================================================

Description
-----------
```

HackerOne community member Dao Hoang Anh (yoyomiski) has reported an
authorization bypass vulnerability in the “admin-user.php”,
“advertiser-user.php”, “affiliate-user.php”, and “agency-user.php”
scripts. A logged in user, with enough privileges to access any of the
affected scripts, can craft a specific payload to change the email
address of any user in the system.

```
Details
-------
```

The functionality behind the “\*-user.php” scripts was always updating
the user details with the data coming from the POST parameters even for
existing users. In case an existing user was being added to an account,
the form data was prepared with the read-only email address for the
user. The attacker could craft specific POST payloads to alter the email
address of any user, potentially gaining access to their username
through the “Forgot Password” functionality.

```
References
----------
https://hackerone.com/reports/3398283
https://github.com/revive-adserver/revive-adserver/commit/7527d00
https://github.com/revive-adserver/revive-adserver/commit/8242644
https://cwe.mitre.org/data/definitions/284.html

========================================================================
Vulnerability 2: Stored XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2025-52668
CVSS Base Score:       8.7
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N
========================================================================

Description
-----------
```

HackerOne community member Vitaly Simonovich (cyberjoker) has reported a
stored XSS vulnerability in the “statistics-conversions.php” script,
with the tracker or campaign name being the vector for attack.

```
Details
-------
```

The “statistics-conversions.php” script, included by the main stats.php
front controller, was not properly sanitising tracker and campaign names
before displaying them on the page.
If conversion tracking is enabled on the installation, a manager user
could set up the XSS attack and create all the required preconditions,
so that a specifically crafted link to “stats.php” would execute
injected javascript code. Successful exploitation requires an attacker
to trick a logged in administrator into visiting such URL. The session
cookie cannot be accessed or stolen via JavaScript, but session riding
would be possible, allowing to create new usernames or chain other kind
of exploits.

```
References
----------
https://hackerone.com/reports/3400506
https://github.com/revive-adserver/revive-adserver/commit/3443963
https://github.com/revive-adserver/revive-adserver/commit/0f3b4a4
https://cwe.mitre.org/data/definitions/79.html

========================================================================
Vulnerability 3: Authorization Bypass
========================================================================
Vulnerability Type:    Authorization Bypass Through User-Controlled Key
                       [CWE-639]
CVE-ID:                CVE-2025-52670
CVSS Base Score:       7.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:L
========================================================================

Description
-----------
```

HackerOne community member Vitaly Simonovich (cyberjoker) has reported
an authorization bypass vulnerability in the “delete-banner.php” script
of Revive Adserver. Users with permissions to delete banners are
mistakenly allowed to delete banners owned by other accounts.

```
Details
-------
```

The Revive Adserver “delete-banner.php” script was not properly checking
ownership of the “bannered” parameter before deleting the resource. That
allows several types of malicious attacks and highly affects the data
integrity of the affected system.

```
References
----------
https://hackerone.com/reports/3401612
https://github.com/revive-adserver/revive-adserver/commit/1e0d1d1
https://github.com/revive-adserver/revive-adserver/commit/f5eef75
https://cwe.mitre.org/data/definitions/639.html

========================================================================
Vulnerability 4: Reflected XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2025-55124
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Dang Hung Vi (vidang04) has reported a
reflected XSS vulnerability in the “banner-zone.php” script since Revive
Adserver 6.0.0. An attacker can craft a specific URL that includes an
HTML payload in a parameter. If a logged in administrator visits the
URL, the HTML is sent to the browser and malicious scripts would be
executed.

```
Details
-------
```

The “filterWebsite” and “filterZone” GET parameters sent to the
“banner-zone.php” script were used in the output without proper
sanitisation, allowing an attacker to craft specific URLs and have
payloads output in the HTML, JS, and/or CSS context. Successful
exploitation requires an attacker to trick a logged in administrator
into visiting the crafted URL. Most importantly, the session cookie
cannot be accessed or stolen via JavaScript, so the disruption would be
limited.

```
References
----------
https://hackerone.com/reports/3403727
https://github.com/revive-adserver/revive-adserver/commit/514bff9
https://cwe.mitre.org/data/definitions/79.html

========================================================================
Vulnerability 5: Reflected XSS
========================================================================
Vulnerability Type:    Improp...