---
title: Dovecot Security Advisory OXDC-2026-0002
url: https://seclists.org/fulldisclosure/2026/May/2
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:49.945112
---

# Dovecot Security Advisory OXDC-2026-0002

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Dovecot Security Advisory OXDC-2026-0002

---

*From*: Aki Tuomi <aki.tuomi () dovecot fi>
*Date*: Tue, 12 May 2026 16:41:30 +0300 (EEST)

---

```
Hi!

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. This advisory is also published at
https://documentation.open-xchange.com/dovecot/security/advisories/html/2026/oxdc-adv-2026-0002.html

---

Classification: TLP:GREEN

Internal reference: DOV-8967
Type: CWE-235 (Improper Handling of Extra Parameters)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.4, OX Dovecot CE core 2.4.3
First fixed revision: OX Dovecot Pro core 3.1.5, OX Dovecot CE core 2.4.4
Discovery date: 2026-03-29
Solution date: 2026-05-05
Disclosure date: 2026-05-05
Researcher credits: caprinuxx@yeswehack
CVE: CVE-2026-27851
CVSS: 7.4 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N)

Details:
lib-var-expand: Safe filter leaks to all following pipelines. When safe filter is used with variable expansion, all
following pipelines on the same string are incorrectly interpreted as safe too, enabling unsafe data to be unescaped.

Risk:
This can enable SQL / LDAP injection attacks when used in authentication. No publicly available exploits are known.

Solution:
Avoid using safe filter until on fixed version.

---

Internal reference: DOV-8948
Type: CWE-400 (Uncontrolled Resource Consumption)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 2.3.0
First fixed revision: OX Dovecot Pro core 3.1.5, OX Dovecot CE core 2.4.4
Discovery date: 2026-03-24
Solution date: 2026-05-05
Disclosure date: 2026-05-05
Researcher credits: djvirus@yeswehack
CVE: CVE-2026-40016
CVSS: 5.3 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:H)

Details:
Sieve :contains/:matches O(N×M) Substring Match Bypasses sieve_max_cpu_time Limit (130× Overrun). Attacker can upload a
malicious Sieve script over ManageSieve service (or locally) to bypass configured CPU time limits for Sieve up to 130
times of the configured limit.

Risk:
Attacker can use this to degrade server performance and bypass configured CPU time limits for Sieve scripts. No
publicly available exploits are known.

Solution:
Install fixed version, or alternatively prevent direct access to Sieve scripts via ManageSieve or local access.

---

Internal reference: DOV-9030
Type: CWE-99 (Improper Control of Resource Identifiers ('Resource Injection'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot Pro core 3.1.5, OX Dovecot CE core 2.4.4
Discovery date: 2026-04-08
Solution date: 2026-05-05
Disclosure date: 2026-05-05
Researcher credits: ylwango613@yeswehack
CVE: CVE-2026-33603
CVSS: 6.8 (CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N)

Details:
login: Base64 input can contain tabs that bypass IPC protection. Attacker can use a specially crafted base64 exchange
between Dovecot and Client to fake SCRAM TLS channel binding. This requires that the attacker is able to position
itself between Dovecot and the client connection.

Risk:
If successful, the attacker can eavesdrop communications between Dovecot and client as MITM proxy. No publicly
available exploits are known.

Solution:
Install fixed version.

---

Internal reference: DOV-9040
Type: CWE-284 (Improper Access Control)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 2.3.0
First fixed revision: OX Dovecot Pro core 3.1.5, OX Dovecot CE core 2.4.4
Discovery date: 2026-04-08
Solution date: 2026-05-05
Disclosure date: 2026-05-05
Researcher credits: ilhamaf@yeswehack
CVE: CVE-2026-40020
CVSS: 3.1 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:L)

Details:
IMAP folders can be shared-spammed to everyone. Attacker can use the IMAP SETACL command to inject the anyone
permission to user's dovecot-acl file even if imap_acl_allow_anyone=no. This causes folders to be spammed to all users.

Risk:
The impact is limited to being able to spam folders to other users, no unexpected access is gained. No publicly
available exploits are known.

Solution:
Install to fixed version.

---

Internal reference: DOV-9138
Type: CWE-400 (Uncontrolled Resource Consumption)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.0.5, OX Dovecot Pro core 3.1.4, OX Dovecot CE core 2.4.3
First fixed revision: OX Dovecot Pro core 3.1.5, OX Dovecot CE core 2.4.4
Discovery date: 2026-04-27
Solution date: 2026-05-05
Disclosure date: 2026-05-05
Researcher credits: D4RKCYPH3R@yeswehack
CVE: CVE-2026-42006
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L)

Details:
imap-login: Excessive memory usage DoS - Try 2. An attacker can cause uncontrolled memory usage with excessive bracing
over IMAP. The fix in CVE-2026-27857 was incomplete, only blocking one way of doing this, so there was still another
way left open. In particular, the fix was for closing braces, but you could still use open braces to bypass the limit.

Risk:
Using excessive bracing, attacker can cause memory usage up to configured memory limit. No publicly available exploits
are known.

Solution:
Install fixed version, or configure vsz_limit for imap process to low value.
```

**Attachment:
[signature.asc](att-2/signature_asc.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **Dovecot Security Advisory OXDC-2026-0002** *Aki Tuomi (May 17)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/s...