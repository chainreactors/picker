---
title: [0day-rubbish] Royal Render 9.1.26b: default-unauthenticated job submission on rrServer TCP 7773 reaches worker-side shell execution as the worker identity, measured root (8.1 High)
url: https://seclists.org/fulldisclosure/2026/Oct/33
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:03.669552
---

# [0day-rubbish] Royal Render 9.1.26b: default-unauthenticated job submission on rrServer TCP 7773 reaches worker-side shell execution as the worker identity, measured root (8.1 High)

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](34)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Royal Render 9.1.26b: default-unauthenticated job submission on rrServer TCP 7773 reaches worker-side shell execution as the worker identity, measured root (8.1 High)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:31:31 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Royal
Render 9.1.26b, the closed-source render-farm job manager for VFX and
animation studios from Binary Alchemy (proprietor Holger Schoenberger) of
Ludwigsburg, Germany. Royal Render
is a different product from the Royal Server gateway sold by Royal Apps GmbH
of Austria; the two are unrelated companies sharing one word in their names,
and this disclosure concerns the German render manager only.

The product's central scheduler, rrServer, shipped as the rrServerconsole
binary, listens on TCP 7773 and speaks a custom binary protocol that is not
HTTP. In the state the product ships in, it performs no identity check on a
connection at all. That is the vendor's own documentation speaking, not an
observation of a test instance: the help page shipped inside the
installation tree at files/help/Authorization.html states "By default, the
rrServer does NOT check for a valid user if you connect to the rrServer".
Authorization is an opt-in feature, either a submission whitelist or an
authorization-required-for-all-connections switch, and the
sub/cfg_global/globalconfig.ini that the vendor's own rrSetup_linux
installer writes leaves both off, with nTCPRequiresAuth=false and an empty
nAuthWhiteList. The primary classification is CWE-306 with CWE-1188 co-equal
and CWE-73, plus CWE-250, CWE-284 and CWE-1392 contributing.

Type and root cause. Among the shipped job types is one named Execute with
renderer name Once, defined in render_apps/_config/E01__ExecuteOnce.cfg,
which declares SceneFileExtension= *.bat;*.sh; and whose Linux command line
is the template CommandLine_Lx= <EndsWith(<Scene> , .sh) source >  "<Scene>"
<AdditionalCommandlineParam>. For a scene path ending in .sh the worker
resolves that template to source "<Scene>" and runs it in its own shell, in
the current shell rather than as a child process. The scene path reaches the
worker as the length-prefixed UTF-16LE dataset field execOnce.file inside the
compressed job record, and nothing between the socket and the shell
constrains it: no principal exists by default against which a job type could
be filtered, there is no allow-list or canonicalisation against a project
root, no owner or mount check, and no signature of the file being sourced.
The verified submission record is 1387 bytes, a 340-byte header carrying a
little-endian uint32 at offset 0x0e equal to the exact compressed length of
the trailing block, 1047, another at offset 0x12 equal to its exact
decompressed size, 55252, a uint16 length prefix of 23 at 0x1b followed by
the submitter hostname at 0x1d, and a zlib stream with header 78 5e from
offset 0x154. Decompressed, the record holds the job type Execute at offset
32, the renderer fragment ;Once at 596, the server version text rr9.1.26b at
3688, the scene path /tmp/rr_clean_poc.sh as a 20-character UTF-16LE string
at offset 3792, and the key execOnce.file at offsets 7818 and 8324. The
scheduler accepted the credential-free record and answered with a normal
346-byte functional reply rather than a rejection or a challenge.

Execution identity, reported as measured. The worker built and ran source
"/tmp/rr_clean_poc.sh". The marker file produced was 34 bytes, owned
root:root, and a sibling file captured the identity output
uid=0(root) gid=0(root) groups=0(root). Root was reached because the worker
process in the verification deployment was started from a root shell, and
the product enforces no privilege separation between the identity that
receives a job and the identity that executes it, so the honest claim is
arbitrary shell execution as the worker's identity. No shipped artefact
fixes a non-root default worker identity and none mandates root; the ceiling
is deployment-dependent, and the advisory says so wherever the identity
matters.

Verification boundary. Static work was documentary and wire-level rather
than disassembly-based: the shipped job-type configuration, the shipped
Python SDK, and the captured submission record with its decompressed job
data. Dynamic work was a live detonation against an installation made with
the vendor's rrSetup_linux installer with the configuration left as
installed, unlicensed and therefore in two-client demonstration mode, with
the authorization key observed to govern behaviour. The chain was driven
end to end from a second client host on a different network segment, in its
own network namespace with a private-range source address and a hostname
foreign to the scheduler, so remote reachability is demonstrated across a
network boundary rather than argued from a bind address. Two properties of
the run were supplied by the research harness and are stated as such: the
scene script's content and its presence at a worker-readable path, because
the job record carries a path and never file content and no primitive over
TCP 7773 was demonstrated that delivers bytes; and the worker's root start.
The all-interface bind of port 7773 was measured on the test instance, with
no shipped artefact stating the default bind in either direction.

Scoring. The published headline is 8.1 High,
CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H, from ISS = 0.914816, Impact at
S:U = 5.873119 and Exploitability = 2.221167, base 8.094286 rounded up.
Attack complexity carries the one precondition the researchers did not
obtain from the product: the record names a path, so attacker-chosen commands
need a script at a worker-readable path, which the harness placed in the
verified run. A conditional reading of 9.8 Critical at AC:L is published
labelled conditional, applying only where an attacker can also write to the
shared render storage the product's own scene-distribution model uses, or
where a structural command-injection observation is confirmed; neither
branch was detonated, so 9.8 is not the headline. Further labelled
conditionals cover a changed-scope reading at 9.1 and 10.0, an
authorization-enabled reading published at all four privilege and complexity
combinations, 8.8, 7.5, 7.2 and 6.6, and a management-network-only reading at
7.5 and 8.8. One structural observation is published as inference and not as
a finding: <AdditionalCommandlineParam> is appended outside the template's
quoting, so shell metacharacters in it would be interpreted by the worker's
shell; the verified record contains no such field in ASCII or UTF-16LE, it
was not executed, and it raises no published score.

Impact. One anonymous submission reaches whichever worker is idle, so the
primitive fans out to the whole farm and to every mount each worker holds;
the executed command inherits the worker's full identity and environment.
Independently of execution, the verified record carries the product's own
destructive post-processing tasks PPDeleteJob and PPDeletebroken, so an
anonymous submitter can also enqueue and destroy queue state. Detection is
weak by construction because every packet is ...