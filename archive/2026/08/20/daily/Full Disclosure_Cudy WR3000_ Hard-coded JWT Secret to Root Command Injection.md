---
title: Cudy WR3000: Hard-coded JWT Secret to Root Command Injection
url: https://seclists.org/fulldisclosure/2026/Aug/68
source: Full Disclosure
date: 2026-08-20
fetch_date: 2026-08-21T03:05:27.895522
---

# Cudy WR3000: Hard-coded JWT Secret to Root Command Injection

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

[![Previous](/images/left-icon-16x16.png)](67)
[By Date](date.html#68)
[![Next](/images/right-icon-16x16.png)](69)

[![Previous](/images/left-icon-16x16.png)](67)
[By Thread](index.html#68)
[![Next](/images/right-icon-16x16.png)](69)

![](/shared/images/nst-icons.svg#search)

# Cudy WR3000: Hard-coded JWT Secret to Root Command Injection

---

*From*: Nir Yehoshua <nir () ciphersecuritylabs com>
*Date*: Wed, 19 Aug 2026 13:23:26 -0700

---

```
Hello Full Disclosure list,

Cipher Security Labs has published details for two vulnerabilities
affecting Cudy WR3000 hardware revision 2.0 running firmware before
version 2.5.24.

CVE-2026-71960 - Hard-coded JWT Secret Authentication Bypass
Severity: Critical, CVSS 9.3

The device firmware contains a hard-coded HMAC signing secret used by
the Mosquitto MQTT JWT authentication plugin. Because the secret can
be recovered from the firmware image, an attacker can forge a valid
JWT without the owner's username or password and without user
interaction.

CVE-2026-71961 - OS Command Injection via Mesh MQTT Command Interface
Severity: High, CVSS 8.7

Once authenticated to MQTT, an attacker can send unsanitized input
through the mesh command interface to a shell sink, resulting in
arbitrary operating-system command execution as root.

Combined attack path:

firmware signing key -> forged JWT -> MQTT access -> root commands

Remote-scope clarification:
The attacker does not need physical proximity to the router and does
not need to be connected to the victim's LAN. Exploitation still
requires a network path to the relevant MQTT/control-plane interface.
This disclosure does not claim that every affected router is directly
reachable from the public Internet.

Affected scope:
Cudy WR3000 hardware revision 2.0
Firmware versions earlier than 2.5.24

Cudy lists firmware 2.5.24 with a release date of July 30, 2026. There
is no defensible public estimate of the number of vulnerable devices
because neither the vendor nor public datasets provide installed-base
figures broken down by hardware revision and firmware version.

References:
https://github.com/advisories/GHSA-jw4g-pv34-hp37
https://github.com/advisories/GHSA-8jmp-g7g6-gf45
https://www.cudy.com/en-us/pages/download-center/wr3000-2-0

Researcher:
Nir Yehoshua
Cipher Security Labs
https://ciphersecuritylabs.com/

Regards,
Nir Yehoshua
Cipher Security Labs
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](67)
[By Date](date.html#68)
[![Next](/images/right-icon-16x16.png)](69)

[![Previous](/images/left-icon-16x16.png)](67)
[By Thread](index.html#68)
[![Next](/images/right-icon-16x16.png)](69)

### Current thread:

* **Cudy WR3000: Hard-coded JWT Secret to Root Command Injection** *Nir Yehoshua (Aug 19)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")