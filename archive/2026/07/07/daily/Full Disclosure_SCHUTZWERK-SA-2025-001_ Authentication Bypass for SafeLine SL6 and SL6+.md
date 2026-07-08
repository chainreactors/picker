---
title: SCHUTZWERK-SA-2025-001: Authentication Bypass for SafeLine SL6 and SL6+
url: https://seclists.org/fulldisclosure/2026/Jul/17
source: Full Disclosure
date: 2026-07-07
fetch_date: 2026-07-08T05:05:54.641215
---

# SCHUTZWERK-SA-2025-001: Authentication Bypass for SafeLine SL6 and SL6+

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# SCHUTZWERK-SA-2025-001: Authentication Bypass for SafeLine SL6 and SL6+

---

*From*: Jan Hüber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 6 Jul 2026 13:24:41 +0200

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Authentication Bypass for SafeLine SL6 and SL6+
===============================================
```

The SafeLine SL6 and SL6+ devices integrated into elevator emergency
intercom systems are
vulnerable to an authentication bypass. This vulnerability allows
attackers to bypass
authentication requirements and access the device's configuration
service via the
Bluetooth Low Energy (BLE) interface. Consequently, an attacker within
wireless range can

```
gain unauthorized administrative access to the device configuration.

Metadata
========

* Affected product: SafeLine SL6/SL6+
* Affected version: Introduced in version 4.82, patched in version 4.97
* Vendor: SafeLine
* Problem type(s): CWE-305 Authentication bypass by primary weakness
* CVE ID: CVE-2025-4994
* CVE URL: https://www.cve.org/CVERecord?id=CVE-2025-4994
* CVSS 4.0 score: 8.7
* Advisory URL: https://www.schutzwerk.com/blog/schutzwerk-sa-2025-001/

Details
=======
```

The SafeLine SL6 and SL6+ act as communication gateway devices that use
4G VoLTE to
facilitate emergency calls for elevators. The device supports
configuration via its
Bluetooth Low Energy (BLE) interface, typically managed using the
SafeLine LYNX mobile
application to configure settings such as the phone numbers to be dialed
when the elevator
emergency button is pressed. The device operates in two modes regarding
the BLE interface,

```
depending on the "Auto Enable BLE" configuration setting:
```

\* Auto Enable BLE enabled: When active, the BLE interface remains
enabled and is secured

```
  by a configurable PIN.
```

\* Auto Enable BLE disabled: After a device reboot, the BLE interface is
available only for
  a short window without authentication. Afterwards, BLE is disabled
and can only be

```
  enabled by a reboot.
```

By default, "Auto Enable BLE" is enabled. The vulnerability lies in the
implementation of
the authentication functionality, which allows an attacker to
successfully bypass PIN
protection and access the configuration interface wirelessly without
knowledge of the
configured PIN code. The discovered vulnerability requires only a small
number of requests

```
to the target device and is fully reproducible.

Risk
====
```

This vulnerability poses a severe risk to the operational integrity of
the SafeLine SL6
and SL6+. By accessing the configuration interface, an attacker can
manipulate critical
device settings, specifically emergency contact phone numbers. In the
context of elevator
emergency intercom systems, this potentially allows attackers to hijack
communication
channels, preventing emergency services or building management from
being notified during

```
an incident.

Workaround
==========
```

The "Auto Enable BLE" setting should be disabled. This ensures that the
BLE interface is
deactivated after the initial time window, preventing wireless access to
the configuration

```
interface.

Solution/Mitigation
===================
```

A patch is available in firmware version 4.97 and should be applied
immediately. This
version removes the PIN authentication feature in BLE entirely. Access
to the
configuration interface via Bluetooth is only possible for a brief time
window following a
reboot, which is similar to the current behavior when disabling "Auto
Enable BLE".

```

```

If patching is not possible for currently deployed devices, the
workaround described above

```
should be applied.

Timeline
========

* 2025-03-28 Vulnerability discovered
* 2025-04-14 Initial contact with vendor
* 2025-04-16 Vulnerability reported to technical support of vendor
* 2025-05-08 Follow-up meeting was canceled by vendor
* 2025-05-16 Initial contact with CTO of vendor
* 2025-05-28 Vulnerability presented to CTO of vendor
* 2025-06-16 Vendor informed SCHUTZWERK that the patch is currently tested
* 2025-07-03 Follow-up meeting was canceled by vendor
* 2025-07-31 Follow-up meeting was requested by SCHUTZWERK
* 2025-08-21 Vendor informed SCHUTZWERK that the patch was postponed
* 2025-08-28 Vendor informed SCHUTZWERK that the patch is currently tested
* 2025-12-19 Vendor informed SCHUTZWERK that the patch was released
```

\* 2025-12-19 Disclosure delayed for 180 days to allow patching the
affected devices during

```
  scheduled maintenance windows
* 2026-06-19 Advisory released by SCHUTZWERK

Credits
=======

The vulnerability was discovered by Jan Hüber of SCHUTZWERK GmbH
-----BEGIN PGP SIGNATURE-----

iQJOBAEBCgA4FiEEgLsg7Oj/wY3LSF87GrXfkTIXLrsFAmpLjrQaHGFkdmlzb3Jp
ZXNAc2NodXR6d2Vyay5jb20ACgkQGrXfkTIXLruNEA/+IiLtH9rqkwhZA3H0qWQp
Z6xH/M7Som+OkCn/qgZ7khBKi2qsC0jdA7ePf/D3LY2VlgA9Y60fAETXarNj2X/y
KgB80TjrPRwBhPhdZKxhn14DCPjLANGVYVDanfR0oQmRzZ8aEjb9No6G04nb+qCV
u7c1aD5Hl0vJRI7AAgkHjz1etgsYm7MKkJYHxhCuJFw2B4XpPjk9TREgofdC3FLk
VkO5xMRUysMy9Sgy8qzesSySX5UHKoPVtndo/EVvDsUJccsIL6WdE4z4odMJ9cRE
r8CX6LAnyhfktgDf8eOgzysfdkYl//0KO1IIGF8ghLqRDpgWkMZTHc2/GXPnPYL1
3uIXI7vG8jGJ99fIijocplug9BAnQnK+w7PBJOzroWMOQC7zJWwy6gL2H/vYIatp
FQFlgF5DnMBdjWX80Gu5CIDPYIVlXW15k7TNF/k5XUW3Uh6/uk8FTLgzPFsR707j
XsWPKk7XICiizJDv2su8rmTtCpPtgHhC0HUoJa6eVBj+37l4EuPS0jpYEByfkmNY
e+eka/F0kF4FzxAp2jWfE4A+QLlP6GGgZSLlfybVgvsjUe468intIDHaR9CPlv74
DtLWZ3zr4OXTare4hm7F0dLN80WAG3A6ELsrqGknaKvD4ePaSBLdkL8q9tKZIQL5
MUv9NZtj3B224OsNyt8EhjA=
=JAMF
-----END PGP SIGNATURE-----

--
SCHUTZWERK GmbH, Pfarrer-Weiß-Weg 12, 89077 Ulm, Germany
Zertifiziert / Certified ISO 27001, 9001 and TISAX

Phone +49 731 977 191 0

advisories () schutzwerk com / www.schutzwerk.com

Geschäftsführer / Managing Directors:
Jakob Pietzka, Michael Schäfer

Amtsgericht Ulm /  HRB 727391
Datenschutz / Data Protection www.schutzwerk.com/datenschutz
```

**Attachment:
[OpenPGP\_signature.asc](att-17/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **SCHUTZWERK-SA-2025-001: Authentication Bypass for SafeLine SL6 and SL6+** *Jan Hüber via Fulldisclosure (Jul 06)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nm...