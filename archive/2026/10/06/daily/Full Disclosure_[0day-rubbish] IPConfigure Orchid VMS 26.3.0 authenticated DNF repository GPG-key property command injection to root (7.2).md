---
title: [0day-rubbish] IPConfigure Orchid VMS 26.3.0 authenticated DNF repository GPG-key property command injection to root (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/5
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.665014
---

# [0day-rubbish] IPConfigure Orchid VMS 26.3.0 authenticated DNF repository GPG-key property command injection to root (7.2)

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] IPConfigure Orchid VMS 26.3.0 authenticated DNF repository GPG-key property command injection to root (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:53:12 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in
IPConfigure Orchid VMS, installed as Orchid Recorder, version 26.3.0.

Type: OS command injection (CWE-78, with CWE-20 bearing on it because no
character validation exists anywhere on the path; CWE-250 bears on the
result). The server property package.dnf.repo.gpg_key, the URL or path of
the GPG key signing the vendor RPM repository, is written through the
authenticated management REST API and persisted to the server properties
file untouched. On service start or restart the package-management thread
formats it into the unquoted command template rpm --import {} and hands the
result to popen, that is to a shell. Every shell metacharacter in the value,
separators, pipes, backticks, command substitutions and redirections, is
interpreted as command syntax. The shipped service unit carries no user
directive, so the injected command runs as uid 0. The injection fires during
thread initialization and repeats on every subsequent boot until the
property is corrected.

Scoring. Dual-scored, with the primary reading named first:
- PRIMARY, 7.2 High, CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H. The write
  endpoint requires the config permission, which the vendor's own shipped
  OpenAPI role table grants in base scope to exactly one role,
  Administrator, so the privilege prerequisite is administrative.
- CONDITIONAL, 9.8 Critical,
  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, for installations that still
  accept the administrator credential the vendor's own installer declares as
  the packaged default; on such a deployment no privilege has to be obtained
  at all. This is the deployment-conditional reading, not the headline.
The advisory also discloses, and deliberately does not adopt, an
intermediate 8.8 reading carried by our own earlier research record paired
with a low-privilege metric: the arithmetic is correct for that vector but
that privilege level contradicts the shipped role table. A scope-changed
reading is rejected and not claimed.

Impact: arbitrary command execution as uid 0 on a video management server
with one authenticated request plus the restart that request itself causes;
read and rewrite of the recorded video archive, that is of physical-security
evidence; persistence through the service unit or loaded libraries; and
lateral reach from a host that by design spans camera networks. This is a
post-authentication finding: the unauthenticated surface was exhausted, with
nearly every specified path requiring authentication, the few unauthenticated
endpoints parameterless and read-only, and traversal and bypass attempts all
rejected. Debian-family deployments take the APT branch and never reach this
sink; RHEL-family deployments are affected.

Verification boundary, stated plainly. A real installation of the vendor's
Debian bundle inside a Linux container, driven purely through the documented
HTTP API with the installer-default credential; three independent root-owned
marker artifacts were produced and command substitution was demonstrably
evaluated on the target. One departure from stock is declared: the DNF code
path was entered by presenting the Debian-family container as RHEL-family and
supplying the repository directory and template files the code requires,
which a native RHEL-family host provides by itself. No native RHEL host was
exploited, no container escape was attempted or claimed, and only the 26.3.0
bundle was installed and executed.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/ipconfigure-orchid-vms-dnf-gpg-key-command-injection

Project archive (ongoing disclosure series):
  https://github.com/Exploit-Garbage/0day-Rubbish

The vendor has been notified through the corporate contact address published
on its own site, as no security-specific intake is published. No
vulnerability identifier has been assigned to this finding yet.

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **[0day-rubbish] IPConfigure Orchid VMS 26.3.0 authenticated DNF repository GPG-key property command injection to root (7.2)** *disclosure via Fulldisclosure (Oct 06)*

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