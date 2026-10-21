---
title: [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the formWlanMP manufacturing-test handler, root command execution (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/28
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:05.408021
---

# [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the formWlanMP manufacturing-test handler, root command execution (7.2)

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the formWlanMP manufacturing-test handler, root command execution (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:30:16 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the
Edimax BR-6478AC, firmware image BR6478AC_v2.20.bin, the dual-band AC1750 SOHO
wireless router from Edimax Technology Co., Ltd. (Taiwan). A single
authenticated POST to a manufacturing radio-calibration route that is still
registered in production firmware reaches system() with thirty raw request
fields interpolated into one command line, and the web server process that
executes it runs as root.

Type and root cause. CWE-78, OS command injection, in the formWlanMP handler
of bin/webs, the embedded GoAhead-style HTTP server that serves the management
interface on TCP port 80. The binary is ELF 32-bit big-endian MIPS, MIPS-I,
uClibc, stripped, 762904 bytes, SHA256
ec39c0f9332361e37ab92f1999ac5f00f5742dd6db75f7cb26c0652cfedb32a1, from a
SquashFS root filesystem of roughly 2.3 MB with an internal build timestamp
from 2015. The registration websFormDefine("formWlanMP", ...) at 0x477a1c
publishes POST /goform/formWlanMP, whose handler at 0x462a24 reads thirty
radio automatic-test-equipment and EEPROM calibration fields through
websGetVar at 0x412a7c, reached via the function-pointer table entry at
0x4c6b18: ateFunc, ateGain, ateTxCount, ateChan, ateRate, ateMacID,
e2pTxPower1 through e2pTxPower7, e2pTx2Power1 through e2pTx2Power7,
ateTxFreqOffset, ateMode, ateBW, ateAntenna, e2pTxFreqOffset, e2pTxPwDeltaB,
e2pTxPwDeltaG, e2pTxPwDeltaMix, e2pTxPwDeltaN and readE2P, plus a submit-url
field. Every one of them is formatted, raw, into a single command line by
sprintf at 0x462fd0 using the format string at 0x4a0d98,

/bin/rftest_old.sh %s %s ...    (thirty %s conversions)

and the result is handed to system(buf) at 0x46308c, whose PLT stub sits at
0x490020 with relocation 0x18b. Between websGetVar and system there is no
validation of any kind: no atoi, no inet_aton, no strchr, no isdigit, no
strcspn, no character filter, no length check beyond buffer capacity, no
argument quoting and no switch to an argv-style exec. The only transformation
on the path is cosmetic: an empty field is replaced with the literal word null
so that argument positions stay aligned. That is filler, not a filter, and it
removes no shell metacharacter.

system() is not an exec of the named program; it is fork plus execl of /bin/sh
with -c, so the entire shell grammar is available to the payload and no
quoting exists to escape out of. Command substitution with $(...) is evaluated
during expansion, before the simple command is looked up, which is the payload
used here; backticks are equivalent; a semicolon terminates the current
command; a pipe or an ampersand turns the line into a pipeline or a background
job, with a trailing hash neutralising the rest of the format string; and an
embedded newline is a command separator that websGetVar does not strip,
because it removes only a trailing one. A field value of ateFunc=$(id >
/tmp/marker) therefore runs id first.

The shipped root filesystem contains rftest.sh but not rftest_old.sh, so the
command word in the constructed line does not resolve and the shell exits 127.
This looks like a mitigation and is not one: expansion precedes program
lookup, so the injected command has already executed by the time the shell
reports the missing script. The replication run reproduced exactly that exit
status alongside a correctly written marker file. The practical consequence
for anyone auditing this handler family is that no deny-list approach can
succeed here, because the payload space is the whole shell grammar and the
interpolation is unquoted; only removing the interpolation or removing the
shell helps.

Authentication and reach. The route requires a valid administrative session in
normal operation. The gate auth_authorize at 0x404d00 reads configuration
object 0x1bc, the setup-wizard flag, through apmib_get; once the device is
past setup the security store at 0x4c7004, a single / entry of type Basic
registered from the directive "Auth / /etc/boa/boa.passwd" by the Auth handler
at 0x40814c, covers every /goform/ path with HTTP Basic authentication. The
product has no second, lower-privileged role: one realm entry, one password
file, one account, an Allow directive handler in this build that is a
non-functional stub answering "This version of Boa doesn't support access
controls", and a shipped configuration carrying one Auth directive and no
Allow directive. Privileges Required is therefore High, not Low.
/goform/formWlanMP is not one of the four routes carrying a post-boot uptime
gate (/mp.asp, /goform/mp, /advanced_management.asp and
/goform/formAdvManagement, which redirect to /index.asp once /proc/uptime
exceeds 600 seconds), so unlike the neighbouring manufacturing route it is
reachable at any time while the device is running.

Execution identity. The calling process is webs and webs is root, because the
shipped etc/boa/boa.conf declares User root, the same file whose AddType
application/x-httpd-cgi asp entry binds .asp pages as CGI. The server is
started by the boot path cleanlog.sh:131 invoked from init.sh:1115 during
early init, writes /var/run/webs.pid, which on this root filesystem requires
root to create, and performs no setuid, chroot, namespace or capability drop.
The landing identity is uid=0(root) and no privilege escalation is involved:
the executing process is already root.

Scope of the pattern. This is one instance of a broad construction rather than
an isolated slip. A count of the shipped registration table found 91
/goform/form* handlers, of which roughly 85 reach a system() or popen() call.
Two further sinks were examined and are reported without a score: the
uptime-gated manufacturing route /goform/mp, which is exploitable in principle
but confined to a 600-second post-boot window and carries the same
factory-test character, and the miniigd UPnP IGD daemon on UDP and TCP port
52869, whose SOAP surface has a command sink that is unauthenticated but
LAN-only under the shipped firewall policy. Four candidates that yielded no
established request-controlled path to command execution are named as excluded
rather than dropped silently: formrefresh, formAutoFWupgrade,
formPreventionSetup and wscd.

Severity. The published score is 7.2 High,
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, from ISS = 1 - 0.44^3 =
0.914816, Impact at S:U = 6.42 x 0.914816 = 5.873119, Exploitability = 8.22 x
0.85 x 0.77 x 0.27 x 0.85 = 1.234708 and Base = Roundup(5.873119 + 1.234708) =
Roundup(7.107826) = 7.2. The provenance of that number is disclosed because it
is a correction: the research notes behind this work carried 8.8 written next
to a PR:H vector, and 8.8 is the arithmetic of PR:L rather than of PR:H, so
the figure was recomputed from the vector and published at 7.2, lowering the
researchers' own number by 1.6 points. Four further readings are printed with
their arithmetic. Privileges Required Low is rejected at 8.8 High, from
Exploitability 2.8352...