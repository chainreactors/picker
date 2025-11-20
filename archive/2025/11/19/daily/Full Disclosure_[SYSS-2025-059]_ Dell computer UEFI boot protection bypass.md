---
title: [SYSS-2025-059]: Dell computer UEFI boot protection bypass
url: https://seclists.org/fulldisclosure/2025/Nov/19
source: Full Disclosure
date: 2025-11-19
fetch_date: 2025-11-20T03:10:22.522710
---

# [SYSS-2025-059]: Dell computer UEFI boot protection bypass

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
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2025-059]: Dell computer UEFI boot protection bypass

---

*From*: Micha Borrmann via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 19 Nov 2025 10:04:21 +0100

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Advisory ID:               SYSS-2025-059
Product:                   Dell computer
Manufacturer:              Dell
Affected Version(s):       Probably all Dell computers
Tested Version(s):         Latitude 5431 (BIOS 1.33.1),
                           Latitude 7320 (BIOS 1.44.1),
                           Latitude 7400 (BIOS 1.41.1),
                           Latitude 7480 (BIOS 1.41.3),
                           Latitude 9430 (BIOS 1.33.1)
```

Vulnerability Type: CWE-288 (Authentication Bypass Using an
Alternate Path or Channel)

```
Risk Level:                Low
Solution Status:           Open
Manufacturer Notification: 2025-10-09
Solution Date:             No solution
Public Disclosure:         2025-11-19
CVE Reference:             Not yet assigned
Author of Advisory:        Micha Borrmann, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

The UEFI (or BIOS) of Dell computers can be protected with an
administrator password ([1]). Among other things, setting this admin
password restricts both legacy boot devices and UEFI boot paths, and
thus protects the system from being booted from external media, for
instance USB flash drives, by non-administrative users.

In order to boot from restricted boot devices, the set admin password
has to be entered in the one-time boot menu, which is usually
accessible by pressing the F12 key during system startup.

Many companies and government agencies protect their Dell devices in
such a way.

However, this boot protection can be easily bypassed.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

It is possible to bypass the boot protection concerning legacy and
restricted boot devices, which is enabled when an admin password is set
in the Dell UEFI.

Thus, an attacker can run other operating systems on the computer
system than the one intended by the system administrator, which may
result in abuse scenarios.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

If the computer is running Microsoft Windows, the authentication to
boot from an external boot medium can be bypassed via Windows Recovery
Environment. With the default Windows settings, every user can start
the Windows Recovery Environment, for example by pressing the shift
key when triggering a system restart.

In the Windows Recovery Environment, there is an option called "Use a
device" to boot the system from an external medium (e.g., a USB flash
drive). If this option is selected, the system starts from the
external boot medium without requiring the set UEFI admin password.

If the computer is running Linux with the GRUB boot loader, the GRUB
console can be used to set up a USB flash drive as new root, and
afterward the system can also boot from a restricted USB boot device
without requiring the set UEFI admin password.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

As of today, no solution is available.

As a measure against unauthorized boot from external media, the entire
"USB Boot Support" setting can be disabled in the UEFI (or BIOS).

If on such a device anybody needs to boot from external media, the
administrator password (which should be known to boot from external
media) must be used to change the UEFI settings to enable "USB Boot
Support". Afterward, this setting has to be disabled again. However,
this only works for protecting from system boot using external media
via the Windows Recovery Environment. It does not protect from booting
via USB using the GRUB console.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Response from manufacturer:

After reviewing this issue, we believe it falls outside the scope of
control of UEFI.

UEFI protections – such as disabling USB boot support and enabling
Secure Boot – adequately safeguard the system during the portion of
the boot process that UEFI governs. Once UEFI hands off control to the
bootloader (e.g., Windows Recovery Environment or GRUB), those systems
become responsible for loading the operating system and enforcing their
own security mechanisms.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2025-09-16: Vulnerability discovered
2025-10-09: Vulnerability reported to manufacturer
2025-10-24: Response received from manufacturer
2025-11-19: Public disclosure of vulnerability

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:
```

[1] Dell Knowledge Base: Understanding System Password, Admin Password,
and HDD Password in BIOS
<https://www.dell.com/support/kbdoc/en-en/000132226/dell-system-prompts-for-a-hard-drive-hdd-or-bios-password>

```
[2] SySS Security Advisory SYSS-2025-059
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-059.txt>

```
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Micha Borrmann of SySS GmbH.

E-Mail: micha.borrmann (at) syss.de
```

Public Key:
<https://www.syss.de/fileadmin/dokumente/PGPKeys/Micha_Borrmann.asc>

```
Key ID: 0xCFC2D5B08EE0CBB9
Key Fingerprint: 38BD 7A9C 3EA9 39C5 33F9  94D0 CFC2 D5B0 8EE0 CBB9

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory
may be updated in order to provide as accurate information as
possible. The latest version of this security advisory is available on
the SySS website.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attribution (by) - Version 4.0
URL: https://creativecommons.org/licenses/by/4.0/deed.en

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEEOL16nD6pOcUz+ZTQz8LVsI7gy7kFAmkbJOcACgkQz8LVsI7g
y7nktw/9FVr8c3z6aK1mIDFEOq0Q/W5VhKinWNwBxJW3ZG8aBJP9mGj8MOccmli8
UGLxAWHhY6o86YmBg7g54oDWEdD2MMGbUVB+UEUCpnph5tZJBap5xivqL/Oz8/XY
w3Xt0Kxza7SqUL06X/d0TZa5TrXLO6t79QsuxNSXeKaFBACh2q0bLykQzepx4cMh
XHarHgczIDWPdwMpLi1fjOKbCIK+4aa3LDZXwzDq43khYcNgRydADm737fmTUZWz
RCrnTEDNW83c/BsMwNNxS9SWWWt4CGyjLS3QQe8OHwxFu6N2bQOKX7UHEUX0sanH
QqEwFzj8rNGbZIB7cUwoZccyRXsDWffAsABgPasbBGyMAfCEuIsEnKYdkwnDJXda
LRhyNSUICu6ibGVGsOSnab45O4wrOHrHE+LwlzMfei8gaYvfjyDaA/cCaAXaI5nY
dN7FOL9YNH+2ZdRcRgWx6DANZ3ivBVBwGRCOwLzVZRXn343ONOaDllx2WW4NT9Zp
PebgqaOm/spgsO/hs8G5DsF0ByjV8JYsLvhtaQycM4/ewUdepc1STyoizEIi3gmO
LmjqUfARiMFyRDIzU2nWBUlBhQzGJoP6s+lYNraLYyfBeUgNASCBXSwpLsnBbRnU
n28IAL21QS9lkpqa+U+GwjVFy1xnHm/FUTj5nDXsrCpv0bBvwO0=
=zyrH
-----END PGP SIGNATURE-----
```

**Attachment:
[smime.p7s](att-19/smime_p7s.bin)**
*Description:* Kryptografische S/MIME-Signatur

```
_______________________________________________
Sent through the Full Disclosure mailing list
htt...