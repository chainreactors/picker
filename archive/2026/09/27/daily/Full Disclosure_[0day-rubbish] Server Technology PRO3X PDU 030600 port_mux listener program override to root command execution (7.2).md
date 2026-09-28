---
title: [0day-rubbish] Server Technology PRO3X PDU 030600 port_mux listener program override to root command execution (7.2)
url: https://seclists.org/fulldisclosure/2026/Sep/79
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:57:00.424311
---

# [0day-rubbish] Server Technology PRO3X PDU 030600 port_mux listener program override to root command execution (7.2)

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

[![Previous](/images/left-icon-16x16.png)](78)
[By Date](date.html#79)
[![Next](/images/right-icon-16x16.png)](80)

[![Previous](/images/left-icon-16x16.png)](78)
[By Thread](index.html#79)
[![Next](/images/right-icon-16x16.png)](80)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Server Technology PRO3X PDU 030600 port\_mux listener program override to root command execution (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 04:55:27 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Server
Technology (Legrand group) PRO3X series intelligent rack PDUs, firmware
spdu-pro3x-030600 build 46640 (ARM 32-bit uClibc Linux).

Type: authenticated listener program override leading to root command execution
(CWE-78, CWE-269; a separate hard-coded factory credential is reported as
CWE-798). PRO3X PDUs run port_mux, an inetd-style launcher that starts every
protocol listener with fork + execv and never drops privileges, so listeners run
as root. The executable path is proto_listener_entry.program in cfg_pmux.cdl,
typed nctl_nspc_nempty_str_512, a free-form string with no whitelist, and an
authenticated administrator rewrites it through setConfiguration (POST /J/cfg).
Pointing the port 80 http listener at /bin/sh with arguments -c "<cmd>" applies at
runtime: the next TCP connection to port 80 executes the attacker's command as
uid 0.

Scoring. This finding is dual-scored, with the conditional figure published
alongside the primary:
- PRIMARY, 7.2 High, CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H. An
  authenticated administrator is required, and that gate was verified unbypassed.
- CONDITIONAL, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. Where
  the factory default administrator credential is left unchanged, unrotated units
  are open with no privileged secret.

Impact: root (uid 0) on the rack power distribution controller, a
critical-infrastructure power monitoring and control appliance. Full configuration
control follows; the disabled modbus (502) and mbusd (503) listeners can be armed
with attacker-chosen programs. Outlet switching and power cycling were not
separately exercised by this proof-of-concept.

Authentication: post-authentication administrator (with a shipped default
administrator credential reported separately as CWE-798).

Verification boundary, stated plainly. No physical PRO3X hardware was used, and
the three-step HTTP chain (POST /J/auth, POST /J/cfg, then the TCP trigger) was
NOT exercised end to end against a device. What was dynamically proven is the
root execution primitive: port_mux fork + execv of an injected /bin/sh -c as uid
0, run twice inside a network namespace under qemu-arm-static against the
rootfs unpacked from the firmware Squashfs, each producing a root-owned marker
containing uid=0(root). Each link of the HTTP delivery path was confirmed
component by component (httpd.conf routing, the BusyBox SCM_RIGHTS descriptor
passing, the administrator credential accepted by auth_cli, and the configuration
write accepted and read back through cfgc). SCM_RIGHTS descriptor passing between
the separate httpd and jsonrpcd processes does not complete under qemu user-mode
emulation, which is an emulation-environment limitation rather than a property of
the vulnerability. Only this build was tested; no other build or model is claimed.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/servertech-pro3x-port-mux-command-injection

Project archive (ongoing disclosure series):
  https://github.com/Exploit-Garbage/0day-Rubbish

The vendor has been notified through its published security contact. No vulnerability identifier has been assigned to
this finding yet.

--
0day Rubbish Research Team
disclosure () 0day-rubbish com
https://0day-rubbish.com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](78)
[By Date](date.html#79)
[![Next](/images/right-icon-16x16.png)](80)

[![Previous](/images/left-icon-16x16.png)](78)
[By Thread](index.html#79)
[![Next](/images/right-icon-16x16.png)](80)

### Current thread:

* **[0day-rubbish] Server Technology PRO3X PDU 030600 port\_mux listener program override to root command execution (7.2)** *disclosure via Fulldisclosure (Sep 26)*

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