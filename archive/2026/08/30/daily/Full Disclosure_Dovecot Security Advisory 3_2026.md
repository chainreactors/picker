---
title: Dovecot Security Advisory 3/2026
url: https://seclists.org/fulldisclosure/2026/Aug/116
source: Full Disclosure
date: 2026-08-30
fetch_date: 2026-08-31T07:53:51.605650
---

# Dovecot Security Advisory 3/2026

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

[![Previous](/images/left-icon-16x16.png)](115)
[By Date](date.html#116)
[![Next](/images/right-icon-16x16.png)](117)

[![Previous](/images/left-icon-16x16.png)](115)
[By Thread](index.html#116)
[![Next](/images/right-icon-16x16.png)](117)

![](/shared/images/nst-icons.svg#search)

# Dovecot Security Advisory 3/2026

---

*From*: Aki Tuomi <aki.tuomi () dovecot fi>
*Date*: Fri, 28 Aug 2026 13:07:32 +0300 (EEST)

---

```
Hi!

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. This advisory will also be published at
https://documentation.open-xchange.com/dovecot/security/advisories/html/2026/oxdc-adv-2026-0003.html

---

Classification: TLP:GREEN

Internal reference: DOV-8476
Type: CWE-403 (Exposure of File Descriptor to Unintended Control Sphere ('File Descriptor Leak'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Affected versions: OX Dovecot Pro core >=2.3.0 <2.3.22.2, OX Dovecot Pro core >=3.0.0 <3.0.7, OX Dovecot Pro core
```

> ```
> =3.1.0 <3.1.6, OX Dovecot CE core >=2.3.0 <2.4.5
> ```

```
First fixed revision: OX Dovecot Pro core 3.0.7, OX Dovecot Pro core 2.3.22.2, OX Dovecot Pro core 3.1.6, OX Dovecot CE
core 2.4.5
Discovery date: 2025-11-25
Solution date: 2026-08-26
Disclosure date: 2026-08-26
CVE: CVE-2026-33263
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L)

Details:
submission-login: Panic when mail_max_userip_connections is reached: Panic: epoll_ctl(del, 8) failed: Bad file
descriptor. When mail_max_userip_connections is set (defaul
t 10) and reached, submission-login can crash with epoll() panic caused by file descriptor handling issues.

Risk:
If running in high-security mode (default for community releases), only the new submission connection gets terminated.
If running in high-performance mode (default for Pr
o releases), all connections handled by the submission-login process will be terminated. The crashes can cause failure
for user to send a message, or it can cause duplica
te messages to be sent. If TLS is not used (in the backend server processing the submission), duplicate deliveries
cannot happen, because the crash can only happen at AUT
H stage. No publicly available exploits are known.

Solution:
Limit the number of connections handled by single submission-login process. This has a performance impact though.
Update to non-vulnerable version.

---

Internal reference: DOV-8874
Type: CWE-400 (Uncontrolled Resource Consumption)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Affected versions: OX Dovecot Pro core >=2.3.0 <3.0.7, OX Dovecot Pro core >=3.1.0 <3.1.6, OX Dovecot CE core >=2.3.0
<2.4.5
First fixed revision: OX Dovecot Pro core 3.0.7, OX Dovecot Pro core 3.1.6, OX Dovecot CE core 2.4.5
Discovery date: 2026-03-11
Solution date: 2026-08-26
Disclosure date: 2026-08-26
Researcher credits: ylwango613@yeswehack
CVE: CVE-2026-33607
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L)

Details:
Dovecot IMAP LIST match_sub() Exponential Backtracking — CPU Denial of Service. An attacker that has valid credentials
can use IMAP LIST command to consume CPU.

Risk:
This can cause degradation or denial of service for IMAP. No publicly available exploits are known.

Solution:
Monitor system for abnormal CPU usage and kill the offending process and lock account. Alternatively install fixed
version.

---

Internal reference: DOV-8884
Type: CWE-400 (Uncontrolled Resource Consumption)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Affected versions: OX Dovecot Pro core >=2.3.0 <2.3.22.2, OX Dovecot Pro core >=3.0.0 <3.0.7, OX Dovecot Pro core
```

> ```
> =3.1.0 <3.1.6, OX Dovecot CE core >=2.3.0 <2.4.5
> ```

```
First fixed revision: OX Dovecot Pro core 3.0.7, OX Dovecot Pro core 2.3.22.2, OX Dovecot Pro core 3.1.6, OX Dovecot CE
core 2.4.5
Discovery date: 2026-03-13
Solution date: 2026-08-26
Disclosure date: 2026-08-26
CVE: CVE-2026-27852
CVSS: 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

Details:
DoS by sending mail with bad header. An attacker that can send mail to a user can craft a message whose headers contain
a very large number of email addresses or MIME par
ameters, which causes excessive memory usage when the message is later parsed.

Risk:
The message is still delivered, but reading it over IMAP can exhaust the memory limit of the process and terminate it,
causing denial of service for the affected user. No
 publicly available exploits are known.

Solution:
Update to non-vulnerable version.

---

Internal reference: DOV-8941
Type: CWE-93 (Improper Neutralization of CRLF Sequences ('CRLF Injection'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Affected versions: OX Dovecot Pro core >=2.3.0 <2.3.22.2, OX Dovecot Pro core >=3.0.0 <3.0.7, OX Dovecot Pro core
```

> ```
> =3.1.0 <3.1.6, OX Dovecot CE core >=2.3.0 <2.4.5
> ```

```
First fixed revision: OX Dovecot Pro core 3.0.7, OX Dovecot Pro core 2.3.22.2, OX Dovecot Pro core 3.1.6, OX Dovecot CE
core 2.4.5
Discovery date: 2026-03-24
Solution date: 2026-08-26
Disclosure date: 2026-08-26
Researcher credits: thanos_haruki@yeswehack
CVE: CVE-2026-33606
CVSS: 4.8 (CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:N/I:H/A:N)

Details:
dsync: Mail content can cause dsync protocol injection. Mail content stored by a user can be crafted so that it is
interpreted as dsync protocol commands when an administ
rator later runs dsync with the stream protocol, for example during a migration.

Risk:
Injected commands can modify mailbox state on the destination during migration or replication, including internal
mailbox attributes that a user should not be able to set
 directly. It can also cause dsync errors. No publicly available exploits are known.

Solution:
Avoid running dsync with the stream protocol on mailboxes with untrusted content. Update to non-vulnerable version.

---

Internal reference: DOV-8947
Type: CWE-655 (Insufficient Psychological Acceptability)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Affected versions: OX Dovecot Pro core >=2.3.0 <2.3.22.2, OX Dovecot Pro core >=3.0.0 <3.0.7, OX Dovecot Pro core
```

> ```
> =3.1.0 <3.1.6, OX Dovecot CE core >=2.3.0 <2.4.5
> ```

```
First fixed revision: OX Dovecot Pro core 3.0.7, OX Dovecot Pro core 2.3.22.2, OX Dovecot Pro core 3.1.6, OX Dovecot CE
core 2.4.5
Discovery date: 2026-03-24
Solution date: 2026-08-26
Disclosure date: 2026-08-26
Researcher credits: heckintosh@yeswehack
CVE: CVE-2026-33604
CVSS: 5.9 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N)

Details:
SMTP Smuggling via Missing Dot-Stuffing After Bare Carriage Return. An attacker that can get Dovecot to relay a
message, for example through Sieve redirect or submission
relay, can use a crafted line ending in the message body to bypass the outbound protection that prevents message
content from being interpreted as SMTP commands.

Risk:
A downstream mail server that hasn't yet fixed the SMTP smuggling vulnerability can be tricked into treating part of
the message body as new SMTP commands, allowing injec
tion of spoofed email. This is the same vulnerability class as CVE-2023-51764 and CVE-2023-51766. No publicly available
exploits are known.

Solution:
Where you control the receiving mail servers, ensure they reject bare carriage returns in message data. Update to
non-vulnerable version.

---

Internal reference: DOV-8949
Type: CWE-400 (Unc...