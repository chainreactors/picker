---
title: [0day-rubbish] Auerswald COMmander 6000 / 6000R 8.6D unauthenticated provisioning import zip-slip to root binary hijack and root code execution (9.8)
url: https://seclists.org/fulldisclosure/2026/Oct/13
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:53.530445
---

# [0day-rubbish] Auerswald COMmander 6000 / 6000R 8.6D unauthenticated provisioning import zip-slip to root binary hijack and root code execution (9.8)

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Auerswald COMmander 6000 / 6000R 8.6D unauthenticated provisioning import zip-slip to root binary hijack and root code execution (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:21:03 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Auerswald
COMmander 6000 and COMmander 6000R, firmware 8.6D build 128154, the
closed-source enterprise IP-PBX and unified-communications appliances from
Auerswald (Germany). Two unauthenticated HTTP requests, carrying no cookie and
no credential of any kind, yield uid=0(root) gid=0(root) groups=0(root) on an
appliance that holds extension credentials, SIP trunk credentials, call detail
records and voicemail for every user it serves.

Type and root cause. CWE-22, path traversal in the zip-slip form, inside a
root archive extraction; CWE-73, CWE-434, CWE-862 and CWE-250 contribute. The
finding is explicitly not classified as CWE-78, and this is worth stating
because it changes the fix: no command string is injected at either hop, and
every argument to every observed execve is either a compile-time constant or a
value that passed the product's own whitelist legitimately. Escaping and
character whitelisting are already implemented correctly in this product. The
missing controls are archive containment and route authorization, and a
command-injection patch would close nothing.

The chain has two hops and both are needed. Hop 1 is the write primitive: the
unauthenticated route /provisioning_data_import stores one multipart/form-data
part at /data/provisioning/import/<basename> and then spawns, as root,

    posix_spawn("../minizip/miniunz", "-o", "-x", <zip>, "-d",
                "/data/provisioning/import/")

captured verbatim from the syscall trace of the product's own process. Neither
the application nor the bundled extractor inspects archive entry names, so an
entry named ../../../opt/auerswald/hping2 escapes the extraction directory and
overwrites a root-owned mode-0755 binary with attacker bytes. Because the write
truncates an existing file, the original permission bits survive and the result
is immediately executable; there is no separate chmod primitive and none is
needed. The -o flag is what makes the replacement silent, converting the
extractor's refuse-to-clobber default into clobber-without-prompt. Hop 2 is the
consumer: a second unauthenticated request to /netdiagnostic_execute makes root
run

    /bin/sh -c "/opt/auerswald/hping2 -1 -I eth0  -c 3 <target> -p <port>"

The diagnostics handler validates the target argument against the charset
0-9A-Za-z.-:/ and that whitelist works as intended; what it cannot protect is
the bytes sitting at a path that appears as a compile-time constant in the
command. The kernel honours the attacker's #!/bin/sh shebang, and the payload's
stdout is captured into the HTTP response body, so the result is read back
directly and no out-of-band channel is involved. Both handlers live in the
vendor's own in-house FastCGI application, a 3,498,560-byte binary started by
init as root behind a stock lighttpd 1.4.64 on an ARM32 glibc embedded Linux
userland, which never drops privilege. The rootfs contains no suid or sgid
binary at all, so there is no privilege boundary between the web application
and the operating system.

How confirmation works. Request 1 is a multipart POST whose part name is equal
to the filename. That is the vendor's own client contract, recovered from the
shipped JavaScript, which appends the file object to a FormData under the
file's own name; requests built the conventional way with a fixed field name
are rejected by the application's parser, and that failure is indistinguishable
from "the server filters uploads" unless the client is read. Request 2 is an
ordinary urlencoded diagnostics POST. The payload echoes a run-unique token
plus the uid and user name to stdout, which the handler returns in the response
body, and appends the output of id to a marker file under /data/log. The
published advisory prints the identity string and the landing paths but
deliberately not the per-run token or a marker filename from a specific run,
since both are artefacts of one execution on one testbed.

What was deliberately not reproduced. No persistence was installed. The same
write primitive reaches the init-respawned service scripts under
/opt/auerswald/scripts/run-*, the lighttpd configuration and the web document
root; those targets are named as statically available so that a defender can
scope an incident, and none was fired. No configuration database, certificate,
private key, credential or call record was read or removed, and no destructive,
encrypting or exfiltrating payload is published. One elegant approach was tried
and does not work, which is recorded here because it is a reproduction trap:
overwriting the extractor itself so that the next import request executes the
payload. The slip write happens inside the currently executing extractor
process, the target file ends up zero bytes long, and the next invocation fails
with ENOEXEC. The doctrine that follows is to never overwrite a binary that is
executing the write.

A correction to our own earlier reading of this chain, published because it was
wrong and a maintainer could otherwise chase it. During this work we
hypothesised that the rejections of conventionally built uploads were caused by
the web server not spooling request bodies to an upload directory, rather than
by the part name. That hypothesis is withdrawn. mod_fastcgi forwards the body
to the backend over the FastCGI STDIN stream whether or not it spools to disk,
the application parses that stream itself, and once the part name matched the
filename the bytes were stored correctly on the first attempt. Nothing about
the web server configuration was blocking the upload, and a change that added
an upload directory directive would not have altered the outcome.

Scoring. One score is published: 9.8 Critical,
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. The Impact Sub-Score is
1 - 0.44^3 = 0.914816, Impact under Scope Unchanged is 6.42 * 0.914816 =
5.873119, Exploitability is 8.22 * 0.85 * 0.77 * 0.85 * 0.85 = 3.887043, and
the sum 9.760162 rounds up to 9.8 under the CVSS ceiling-to-tenth rule.

An alternative reading is argued in the advisory and not adopted as the
headline: Scope Changed. A network-facing management service yielding host-wide
root on an appliance that also holds call records, extension credentials and a
managed phone fleet is the kind of outcome Scope Changed was written to
express, and AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H computes to 10.0 - the
Scope-Changed impact term is 6.128026, exploitability is unchanged at
3.887043, the sum times 1.08 exceeds the maximum and is capped. We publish
Scope Unchanged because of one fact: the application is already uid 0 by
design, and the rootfs contains no suid or sgid binary because the vendor's
design never needed one, so there is no authority boundary between the web
component and the telephony component for the chain to cross. It exercises,
through a defect, an authority the vulnerable component already held.
Publishing 10.0 would attribute a bo...