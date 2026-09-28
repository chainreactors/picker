---
title: [0day-rubbish] MultiTech Conduit AEP 6.3.6 Authenticated import_config filename command injection to root RCE (7.2)
url: https://seclists.org/fulldisclosure/2026/Sep/77
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:57:00.894027
---

# [0day-rubbish] MultiTech Conduit AEP 6.3.6 Authenticated import_config filename command injection to root RCE (7.2)

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

[![Previous](/images/left-icon-16x16.png)](76)
[By Date](date.html#77)
[![Next](/images/right-icon-16x16.png)](78)

[![Previous](/images/left-icon-16x16.png)](76)
[By Thread](index.html#77)
[![Next](/images/right-icon-16x16.png)](78)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] MultiTech Conduit AEP 6.3.6 Authenticated import\_config filename command injection to root RCE (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 04:54:58 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in MultiTech
Conduit AEP (models mtcdt / mtcdtip / mtcdtiphp), IoT gateways running mLinux on
ARM 32-bit.

Type: authenticated OS command injection (CWE-78) through the uploaded filename
of the admin-only upload_config command. The management API is served by lighttpd
on TCP 8080 and proxied to the proprietary FastCGI daemon /usr/bin/rcell_api. The
import_config handler wraps the client-supplied filename in single quotes to
build import_config '<filename>' and runs it through MTS::System::cmd, which
disassembly confirms is popen(cmd, "r"), that is /bin/sh -c. The multipart parser
strips only surrounding double quotes and reduces the value to a basename; single
quotes are never escaped, so a filename of x'; <CMD> ;# breaks out of the quoting.

Scoring. Single base score, not dual-scored:
- 7.2 High, CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H. PR:H because
  command/upload_config is granted only in the administrator permission profile.

Impact: root command execution on a gateway that bridges constrained field devices
with IP infrastructure (the daemon runs as uid 0), giving full filesystem read,
configuration rewrite, persistence and pivot. The injected command output is
redirected rather than echoed, so the injection is blind at the protocol level and
confirmation rests on a server-side artefact.

Authentication: authenticated administrator. No factory default credentials exist;
the administrator account is provisioned by the deployer at commissioning. An
exhaustive review of the unauthenticated surface found no route to this sink
without a valid admin session, so the finding is scoped as post-authentication.

Verification boundary, stated plainly. Verified end to end by emulation only:
the root filesystem extracted from the AEP 6.3.6 firmware image was run under
qemu-arm-static inside a chroot and started through its angel supervisor, with no
physical Conduit device used at any point. Against the running daemon in socket
mode with an admin session established from a non-loopback REMOTE_ADDR, the upload
returned {"code":200,"status":"success","type":"upload"} and produced a root-owned
marker containing uid=0(root) gid=0(root) groups=0(root), while a benign filename
returned HTTP 400 and created nothing. AEP 6.3.0 is evidenced by patch diff (the
import_config handler is unchanged); the claimed range 6.3.0 through 6.3.6 follows
from that endpoint comparison and the intermediates were not each executed.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/multitech-conduit-import-config-command-injection

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

[![Previous](/images/left-icon-16x16.png)](76)
[By Date](date.html#77)
[![Next](/images/right-icon-16x16.png)](78)

[![Previous](/images/left-icon-16x16.png)](76)
[By Thread](index.html#77)
[![Next](/images/right-icon-16x16.png)](78)

### Current thread:

* **[0day-rubbish] MultiTech Conduit AEP 6.3.6 Authenticated import\_config filename command injection to root RCE (7.2)** *disclosure via Fulldisclosure (Sep 26)*

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