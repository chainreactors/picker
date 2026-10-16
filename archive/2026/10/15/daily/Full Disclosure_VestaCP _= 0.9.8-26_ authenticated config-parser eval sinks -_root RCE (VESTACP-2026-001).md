---
title: VestaCP <= 0.9.8-26: authenticated config-parser eval sinks ->	root RCE (VESTACP-2026-001)
url: https://seclists.org/fulldisclosure/2026/Oct/26
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:49.037340
---

# VestaCP <= 0.9.8-26: authenticated config-parser eval sinks ->	root RCE (VESTACP-2026-001)

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# VestaCP <= 0.9.8-26: authenticated config-parser eval sinks -> root RCE (VESTACP-2026-001)

---

*From*: Bryan Ramirez via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 06 Oct 2026 19:23:03 -0400

---

```
Advisory ID:   VESTACP-2026-001 / GHSA-m2mc-xwq7-pw72
Product:       Vesta Control Panel (VestaCP)
Versions:      <= 0.9.8-26 (unmaintained since 2019-09; no upstream fix exists)
Severity:      Critical - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H = 9.9
CWE:           CWE-78 (OS Command Injection), CWE-95 (Eval Injection)
Reporter:      Bryan Ramirez - SYSDOP LLC <security () sysdop com>

SUMMARY
-------
VestaCP stores per-account objects (domains, cron jobs, DNS, mail, users) as
KEY='value' lines under $USER_DATA/*.conf. The shared shell library
func/main.sh - sourced by every v-* administration script, all of which run
as root - parses those lines with `eval`, so the assignments land in the
calling shell's environment.

Values in those files are controllable by an authenticated panel user (cron
command fields, domain/alias fields, DNS and mail records, names/comments).
Any value that lands with an unescaped single quote breaks out of the quoted
assignment and injects arbitrary shell, executed as root the next time any
v-* script parses that object - which happens on routine panel operations
and on cron-driven sync jobs, without further interaction.

This is the same sink class published for VestaCP's downstream fork HestiaCP
as GHSA-w3mx-xq85-8qqc (config parser eval -> root RCE, fixed in 1.9.5),
GHSA-cr7q-frhq-xw4v and GHSA-5fpv-c8rg-x6r3 (unquoted cron argument ->
crontab injection). Hestia patched the class in the fork; VestaCP itself
never received an advisory or a fix and remains deployed worldwide - notably
in VPS templates (e.g. Virtualizor images) still offered by hosting
providers today.

AFFECTED SINKS (func/main.sh, 0.9.8-26)
-------------------------------------
is_object_value_empty, is_object_value_exist, get_object_value,
update_object_value, add_object_key: eval "$object" over a grep'd conf line.
search_objects, sync_cron_jobs: eval $line per matching line.
ARGUMENTS builder: eval echo \$${I} (also a latent glob-expansion bug).
is_format_valid: eval arg=\$$arg_name.
bin/v-add-cron-job: echo $7 unquoted -> raw newlines land in the crontab
(GHSA-5fpv class).

The central pattern (verbatim shape in stock 0.9.8-26):

    object=$(grep "$2='$3'" $USER_DATA/$1.conf)
    eval "$object"

EXPLOITATION
------------
1. Attacker holds an ordinary authenticated VestaCP account (hosting
   customer) or any write path landing data in ~/conf/*.conf (panel fields
   bypassing %quote% escaping, backup/restore, API/import paths).
2. A crafted value containing an unescaped ' is stored, e.g. a cron CMD:
   CMD='x'; id > /tmp/pwned; #
3. On the next root-run v-* invocation parsing the object, the eval runs
   the injected commands as root.

Impact: tenant-to-host escape - full root on the node, exposing every site,
mailbox and database of every account it hosts.

A self-contained PoC simulating the vulnerable parse and the hardened parser
neutralizing it is published in the repository (poc/poc-eval-sink.sh).

ADDITIONAL FINDING
------------------
While certifying equivalence of the hardened parser (1,165 field comparisons
against real confs): the stock `eval echo $4` path performs glob expansion -
a literal `*` in a field expands to a directory listing instead of returning
verbatim. The non-eval parser returns `*` correctly: the replacement is
equivalent and fixes a latent parsing bug.

MITIGATION
----------
No upstream fix exists (abandonware). Operators still running VestaCP should:

1. Replace the eval parser with a non-eval key/value parser - the repository
   includes a drop-in parse_object_kv_list (strict KEY='value' regex +
   `declare -g` assignment; values become literals, never executed) plus a
   porting recipe for all eval sites (mitigation/non-eval-parser.sh).
2. Enforce %quote%/%dots% escaping on every v-* entry point ingesting user
   data; quote every expansion (echo "$7" in v-add-cron-job).
3. Restrict the panel port by firewall/IP allow-list; monitor
   $USER_DATA/*.conf for unexpected writes.
4. Migrate to a maintained control panel.

TIMELINE
--------
2019-09    Last upstream VestaCP release (0.9.8-26); project abandoned.
2026-08    Sinks identified, PoC confirmed and remediation developed during
           a defensive security audit of production hosting infrastructure.
2026-10-06 Public disclosure (GitHub Security Advisory + this post);
           CVE requested via MITRE.

VENDOR CONTACT
--------------
None possible - no active maintainer, no published security contact,
inactive community. Disclosed publicly for the install base still running
VestaCP in production.

REFERENCES
----------
GHSA: https://github.com/sysdopllc/vestacp-config-eval-rce/security/advisories/GHSA-m2mc-xwq7-pw72
Repository (advisory, PoC, mitigation):
  https://github.com/sysdopllc/vestacp-config-eval-rce
Related HestiaCP advisories (same class, fixed downstream):
  https://github.com/hestiacp/hestiacp/security/advisories/GHSA-w3mx-xq85-8qqc
  https://github.com/hestiacp/hestiacp/security/advisories/GHSA-cr7q-frhq-xw4v
  https://github.com/hestiacp/hestiacp/security/advisories/GHSA-5fpv-c8rg-x6r3

--
Bryan Ramirez
SYSDOP LLC
security () sysdop com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **VestaCP <= 0.9.8-26: authenticated config-parser eval sinks -> root RCE (VESTACP-2026-001)** *Bryan Ramirez via Fulldisclosure (Oct 15)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)*...