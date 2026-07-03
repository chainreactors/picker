---
title: pwnlift: symlink following and TOCTOU in privileged upload	handler allow arbitrary file write as root
url: https://seclists.org/fulldisclosure/2026/Jul/10
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:58.712454
---

# pwnlift: symlink following and TOCTOU in privileged upload	handler allow arbitrary file write as root

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# pwnlift: symlink following and TOCTOU in privileged upload handler allow arbitrary file write as root

---

*From*: Greg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 27 Jun 2026 11:36:46 +0000

---

```
1. Advisory information
-----------------------
Title:  Symlink following and TOCTOU in pwnlift upload handler allow arbitrary file write as root
Advisory: https://github.com/GregDurys/security-advisories
GHSA: GHSA-2v7v-rhpw-m9w4
CVE: CVE-2026-56815
Class:  CWE-59 (Improper Link Resolution Before File Access),
CWE-367 (Time-of-check Time-of-use Race Condition)
CVSS:  7.8 (High) - CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
Date:  2026-06-27
Author:  Greg Durys <https://github.com/GregDurys>

2. Affected software
--------------------
Project:  pwnlift
Repository: https://github.com/rasta-mouse/pwnlift
Runtime:  .NET / Blazor (ASP.NET Core, Kestrel)
Component:  pwnlift/Components/Pages/Home.razor
Tested:  commit 211f2b3 (2025-08-29)
Fix: d7a95449d9ee1ea09ec1529286685f6187afbbed (merged 2026-06-18),
(initial remediation e3eddac addresses CWE-59 but not CWE-367)

3. Testing scope
----------------
All exploitation testing was performed in a local testbed. The known
affected downstream lab deployment has been mitigated by removing the
privileged sudo entry. The upstream follow-up fix has been merged.

4. Summary
----------
pwnlift is a small .NET/Blazor file upload server. Its upload handler
constructs the destination path from the caller's working directory
(Directory.GetCurrentDirectory()) and writes uploaded files without
validating symlinks, canonicalising paths, or sanitising filenames.

When pwnlift runs as root via sudo without a cwd= directive, a local
user can exploit this in two ways:

  (a) Symlink following (CWE-59): pre-stage an Uploads symlink
      pointing at a privileged directory. The elevated process follows
      the symlink and writes uploaded files into the target.

  (b) TOCTOU bypass of initial fix (CWE-367): the initial fix added
      a ReparsePoint check and StartsWith containment. Because the
      destination is still caller-controlled, a race script alternates
      Uploads between a real directory (passes the check) and a symlink
      (catches the write). The StartsWith check has a separate flaw:
      prefix matching without a trailing separator means
      /tmp/Uploads-evil passes StartsWith("/tmp/Uploads").

Both variants achieve arbitrary file write as root. For example,
writing to a privileged configuration path such as /etc/sudoers.d/
can grant the attacker full passwordless sudo.

5. Remediation
--------------
Replace Directory.GetCurrentDirectory() with AppContext.BaseDirectory.
Enforce path containment with Path.GetRelativePath rather than
StartsWith. Retain the ReparsePoint check as defence in depth. Ensure
the application directory and Uploads are root-owned and not writable
by lower-privileged users. If Uploads already exists as a symlink,
remove and recreate it as a real directory before applying ownership
changes.

6. Disclosure timeline
----------------------
2026-04-30  Privileged deployment observed during normal lab usage
2026-05-07  Initial contact with upstream maintainer
2026-05-08  Reproduced end-to-end in local testbed; reported to upstream maintainer and downstream deployment operator
2026-05-12  Initial fix committed upstream (e3eddac) with reporter credit
2026-05-19  Downstream operator declined CVE on CNA scope grounds
2026-05-20  TOCTOU bypass reproduced and reported to maintainer
2026-05-28  Downstream operator confirmed lab patched, sudo removed
2026-05-30  CVE requested via GHSA
2026-06-09  GitHub rejected CVE request
2026-06-09  GHSA re-review requested
2026-06-15  CVE request submitted to MITRE
2026-06-18  Follow-up fix merged upstream; CVE re-requested via GHSA
2026-06-19  GitHub rejected second CVE request
2026-06-22  GHSA advisory published without a CVE
2026-06-23  Advisory posted to oss-security
2026-06-23  MITRE assigned CVE-2026-56815

7. Current status
-----------------
Downstream deployment: patched (sudo entry removed, 28 May 2026)
Upstream final fix: merged (d7a9544, 18 June 2026)
CVE: CVE-2026-56815 (assigned by MITRE, 23 June 2026)

8. References
-------------
- https://github.com/rasta-mouse/pwnlift
- https://github.com/rasta-mouse/pwnlift/commit/e3eddaca42b4b3e9c69f2d7aa024b6c82e27a5a2
- https://github.com/rasta-mouse/pwnlift/commit/d7a95449d9ee1ea09ec1529286685f6187afbbed
- https://github.com/rasta-mouse/pwnlift/security/advisories/GHSA-2v7v-rhpw-m9w4
- https://www.openwall.com/lists/oss-security/2026/06/23/2
- https://github.com/GregDurys/security-advisories
- https://payloadforge.io/beyond-crto-pwnlift/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **pwnlift: symlink following and TOCTOU in privileged upload handler allow arbitrary file write as root** *Greg via Fulldisclosure (Jul 02)*

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