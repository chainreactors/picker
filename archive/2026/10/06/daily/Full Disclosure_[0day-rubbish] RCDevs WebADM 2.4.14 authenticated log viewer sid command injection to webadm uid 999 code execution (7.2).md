---
title: [0day-rubbish] RCDevs WebADM 2.4.14 authenticated log viewer sid command injection to webadm uid 999 code execution (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/7
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.435707
---

# [0day-rubbish] RCDevs WebADM 2.4.14 authenticated log viewer sid command injection to webadm uid 999 code execution (7.2)

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] RCDevs WebADM 2.4.14 authenticated log viewer sid command injection to webadm uid 999 code execution (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:53:47 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in RCDevs WebADM
2.4.14, Freeware Edition, the closed-source IAM/MFA management platform from RCDevs
Security SA (Luxembourg) that fronts the vendor's OpenOTP, SpanKey and TiQR
authentication products.

Type: OS command injection (CWE-78, with CWE-20 and CWE-116 contributing, and
CWE-732/CWE-276 and CWE-250 added for two auxiliary conditions). The administrator
console log viewer admin/logfile_viewer.php interpolates the sid GET parameter,
percent-decoded once and with no escaping of any kind, into the single-quoted shell
command grep -E '<sid>' <logfile> | tail -n 10000 which the page hands to PHP's
popen(). A single apostrophe closes the quoted grep pattern, everything after it is
parsed by /bin/sh as command text, and the trailing quote pair re-opens an empty
quoted string that swallows the remainder of the pipeline. There is no escapeshellarg,
no escapeshellcmd, no quote stripping, no charset allow-list and no length cap on the
recorded path; the absence of a filter, not the bypass of one, is the root cause.
Commands execute as the webadm service account, uid=999(webadm) gid=999(webadm)
groups=999(webadm), the identity the webadm-httpd workers run under with no privilege
drop configured. Root was not achieved, is not claimed, and no privilege escalation
was attempted.

The endpoint does not echo command output into its HTTP response, so confirmation is
out-of-band: the injected command appends a line to /opt/webadm/logs/webadm.log and
the same endpoint reads that file back over HTTPS when asked for a different log
selector. This also means the finding is self-verifying rather than interpretive.
The published advisory reproduces the identity string but deliberately not the
per-run marker token or the container hostname from the run, since both are artefacts
of one execution on one host.

Scoring. One score is published: 7.2 High, CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H.
That vector computes to 7.107826 raw and is taken to 7.2 by the CVSS ceiling-to-tenth
Roundup, which is why a calculator reporting 7.1 is not in disagreement with anything
but with the specification's rounding rule. Our research record carried a higher base
score beside this same PR:H vector, and that pairing cannot compute; the higher figure
is the base score of the PR:L variant, which asserts that an authenticated principal
below administrator reaches the sink. This research did not support that assertion:
the session is issued by an LDAP bind as the administrator DN, the no-cookie negative
control never reached popen(), and no lower-privileged console role was documented.
The advisory therefore publishes 7.2 alone and leaves PR:L as an open question about
the product's role model, to be amended if an auditor- or help-desk-class role can
open this viewer in a shipped or supported configuration. Scope Changed was
considered and rejected: under S:C the same vector would compute to 9.1, but the
injected command runs as the same identity, on the same host, with the same backend
access the vulnerable application already holds, so no authorization boundary is
crossed. No unauthenticated reading is published. License registration was required
to bring the console up, the record documents no vendor-shipped default administrator
credential, and this research did not establish whether one exists, so no PR:N figure
is claimed on evidence the record does not carry.

Authentication: post-authentication console administrator. Eleven endpoints reachable
without a console session were examined in full, plus two independent adversarial
passes tasked specifically with breaking the "a session is required" conclusion. That
sweep found no shell sink and no file-write sink reachable from unauthenticated input;
every include hit was a static framework bootstrap; the certificate signing daemon on
port 5000 carries no shell strings; and the mail() transport keeps recipients off the
command line, removing the notification path as an injection route. The advisory
publishes that disposition table so the negative result is auditable. Unauthenticated
remote code execution was not reached and none is claimed.

Impact: arbitrary OS command execution as the webadm application account on the host
that runs an identity platform, which is why the qualitative weight exceeds what the
number alone conveys. From uid 999 an attacker can read and rewrite platform
configuration under /opt/webadm, including the httpd and PHP configuration defining
routing, authentication domains and backend connectivity - a persistence path that
survives a service restart without touching the operating system; reach the directory
backend on the local LDAP listener and the application database on the local MariaDB
listener with the credentials the application itself carries, which for an MFA
platform means user records, OTP state and second-factor enrolments, so modification
can disable, redirect or re-enrol a user's second factor; interact with the
certificate signing daemon from inside the trust boundary where its network-level
protections no longer apply; write to product logs, supporting both anti-forensics
and the observation channel this exploit uses; and disrupt availability of the console
and of the authentication path it fronts, locking out users of every relying
application. Everything gained sits inside the authorization domain the application
already occupies, hence Scope Unchanged, but the content of that domain is the
identity infrastructure of whatever WebADM was deployed to protect.

Verification boundary, stated plainly. All dynamic work was performed against a
Docker container running WebADM 2.4.14 Freeware Edition, reached over TLS on the
container's HTTPS listener by a pure-standard-library Python client, driven from the
container host, and recorded across four independent runs that each used their own
marker and all returned the same uid 999 identity. The container's published ports
were mapped to loopback addresses and no request crossed a network boundary, so
remote reachability is argued from the product's own binding configuration for an
admin console vhost that exists to be reached over a network, not measured from a
separate host. The application ships as a Blowfish-encrypted opcache file_cache corpus
that only the vendor's custom webadm-runphp interpreter (PHP 8.2.30, ZTS) decodes at
load time, so there is no plaintext PHP on disk: the decoder was located in that
interpreter by following cross-references to the container magic, the parser and the
decryption were reimplemented offline, and 315 files were recovered. That recovery
yields the literal string layer, not vendor source text, so the sink construction in
the advisory is labelled as a reconstruction from decoded string literals plus
observed behaviour, confirmed by the executed result. Exactly one command shape was
executed and only that shape is claimed - a single echo carrying three command
...