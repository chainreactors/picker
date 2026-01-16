---
title: [REVIVE-SA-2026-001] Revive Adserver Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Jan/19
source: Full Disclosure
date: 2026-01-15
fetch_date: 2026-01-16T03:31:07.492346
---

# [REVIVE-SA-2026-001] Revive Adserver Vulnerabilities

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

# [REVIVE-SA-2026-001] Revive Adserver Vulnerabilities

---

*From*: Matteo Beccati <php () beccati com>
*Date*: Wed, 14 Jan 2026 13:39:23 +0100

---

```
========================================================================
Revive Adserver Security Advisory                     REVIVE-SA-2026-001
------------------------------------------------------------------------
https://www.revive-adserver.com/security/revive-sa-2026-001
------------------------------------------------------------------------
Date:                  2026-01-14
Risk Level:            High
Applications affected: Revive Adserver
Versions affected:     <= 6.0.4
Versions not affected: >= 6.0.5
Website:               https://www.revive-adserver.com/
========================================================================

========================================================================
Vulnerability 1: Format string injection
========================================================================
Vulnerability Type:    Use of Externally-Controlled Format String
                       [CWE-134]
CVE-ID:                CVE-2026-21640
Risk level:            Low
CVSS Base Score:       2.7
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:L
========================================================================

Description
-----------
```

HackerOne community member Faraz Ahmed (PakCyberbot) has reported a
format string injection in the Revive Adserver settings. When specific
character combinations are used in a setting, the admin user console
could be disabled due to a fatal PHP error.

```
Details
-------
```

The Revive Adserver settings are stored using INI files, which support
variable interpolation. Using certain character sequences, such as '${{'
in a setting was causing a PHP fatal error when reading back the
configuration, due to inadequate escaping in the INI file writing
classes from the PEAR\_Config package. Only administrators are allowed to
change settings, so, in normal circumstances, the disruption would be
limited.

```
References
----------
https://hackerone.com/reports/3445332
https://github.com/revive-adserver/revive-adserver/commit/c40187d8
https://cwe.mitre.org/data/definitions/134.html

========================================================================
Vulnerability 2: Authorization Bypass
========================================================================
Vulnerability Type:    Authorization Bypass Through User-Controlled Key
                       [CWE-639]
CVE-ID:                CVE-2026-21641
Risk level:            High
CVSS Base Score:       7.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:L
========================================================================

Description
-----------
```

HackerOne community member Jad Ghamloush (0xjad) has reported an
authorization bypass vulnerability in the 'tracker-delete.php' script of
Revive Adserver. Users with permissions to delete trackers are
mistakenly allowed to delete trackers owned by other accounts.

```
Details
-------
```

The Revive Adserver 'tracker-delete.php' script was not properly
checking ownership of the 'clientid' parameter before deleting the
resource. That allows several types of malicious attacks and highly
affects the data integrity of the affected system.

```
References
----------
https://hackerone.com/reports/3445710
https://github.com/revive-adserver/revive-adserver/commit/f6059335
https://cwe.mitre.org/data/definitions/639.html

========================================================================
Vulnerability 3: Reflected XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2026-21642
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Patrick Lang (7yr) has reported a reflected
XSS vulnerability in the ’banner-acl.php’ and ’channel-acl.php’ scripts
of Revive Adserver. An attacker can craft a specific URL that includes
an HTML payload in a parameter. If a logged-in administrator visits the
URL, the HTML is sent to the browser and malicious scripts would be
executed.

```
Details
-------
```

The ’acls[0][executionorder]’ request parameter sent to the
’banner-acl.php’ or ’channel-acl.php’ scripts were used in the output
without proper sanitisation, allowing an attacker to craft specific URLs
and have payloads output in the HTML, JS, and/or CSS context. Successful
exploitation requires an attacker to trick a logged-in user into
visiting the crafted URL.

```
References
----------
https://hackerone.com/reports/3470970
https://github.com/revive-adserver/revive-adserver/commit/e245a88
https://github.com/revive-adserver/revive-adserver/commit/0ebc96d
https://cwe.mitre.org/data/definitions/79.html

========================================================================
Vulnerability 4: Reflected XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2026-21663
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Patrick Lang (7yr) has reported a reflected
XSS vulnerability in the 'banner-acl.php' script of Revive Adserver. An
attacker can craft a specific URL that includes an HTML payload in a
parameter. If a logged-in administrator visits the URL, the HTML is sent
to the browser and malicious scripts would be executed.

```
Details
-------
```

The ’cap’, ’session\_capping’ and ’time’ request parameters sent to the
’banner-acl.php’ script were used in the output without proper
sanitisation, allowing an attacker to craft specific URLs and have
payloads output in the HTML, JS, and/or CSS context. Successful
exploitation requires an attacker to trick a logged-in user into
visiting the crafted URL.

```
References
----------
https://hackerone.com/reports/3473696
https://github.com/revive-adserver/revive-adserver/commit/c130eb0
https://cwe.mitre.org/data/definitions/79.html

========================================================================
Vulnerability 5: Reflected XSS
========================================================================
Vulnerability Type:    Improper Neutralization of Input During Web Page
                       Generation (‘Cross-site Scripting’) [CWE-79]
CVE-ID:                CVE-2026-21664
Risk level:            Medium
CVSS Base Score:       6.1
CVSS Vector:           CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
========================================================================

Description
-----------
```

HackerOne community member Huynh Pham Thanh Luc (nigh7c0r3) has reported
a re...