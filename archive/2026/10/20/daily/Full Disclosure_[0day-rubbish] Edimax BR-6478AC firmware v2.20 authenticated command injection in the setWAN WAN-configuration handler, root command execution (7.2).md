---
title: [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the setWAN WAN-configuration handler, root command execution (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/29
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:05.086756
---

# [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the setWAN WAN-configuration handler, root command execution (7.2)

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Edimax BR-6478AC firmware v2.20 authenticated command injection in the setWAN WAN-configuration handler, root command execution (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:30:31 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the
Edimax BR-6478AC, firmware image BR6478AC_v2.20.bin, the dual-band AC1750 SOHO
wireless router from Edimax Technology Co., Ltd. (Taiwan). A single
authenticated POST that looks like an ordinary WAN settings submission reaches
system() with a request-controlled username interpolated unquoted into a shell
command line, behind a sanitiser that inspects exactly one character, and the
web server process that executes it runs as root.

Type and root cause. CWE-78, OS command injection, in the setWAN
WAN-configuration handler of bin/webs, the embedded GoAhead-style HTTP server
that serves the management interface on TCP port 80. The binary is ELF 32-bit
big-endian MIPS, MIPS-I, uClibc, stripped, 762904 bytes, SHA256
ec39c0f9332361e37ab92f1999ac5f00f5742dd6db75f7cb26c0652cfedb32a1, from a
SquashFS root filesystem of roughly 2.3 MB with an internal build timestamp
from 2015. The registration websFormDefine("setWAN", ...) at 0x478484, handler
at 0x441cec and name string at 0x4a6250, publishes POST /goform/setWAN. Inside
the handler the WAN mode is read from the request and dispatched:
websGetVar(wp, "wanMode", "") at 0x441d3c, atoi at 0x441d44, apmib_set(0x102,
&wanMode) at 0x441d54, then addiu v1, zero, 2 at 0x441d60 and beq v0, v1,
0x441e74 at 0x441d6c. On the PPP branch, wanMode 2, the username field is
taken from the request by websGetVar for pppUserName, whose name string is at
0x4953f4, copied with strcpy at 0x441e94 into a fixed stack buffer, measured
with strlen at 0x441ea8, and scanned by an inline byte loop between 0x441ebc
and 0x441ee4 whose only comparison is addiu a0, zero, 0x3b, a semicolon.
Finding one, the loop writes a NUL and stops. That single-character scan is
the entire sanitisation on the path. The value then goes into sprintf at
0x441ee8 using the format string at 0x49a510,

    echo %s > /tmp/UserName

and from there into system(buf2) at 0x441f1c, reached through the PLT slot at
0x4c6d60, which hands the line to /bin/sh -c. A pipe, an ampersand, a
backtick, a dollar sign with parentheses and an embedded newline are never
inspected, so a username containing no semicolon reaches the shell untouched.
The verified payload is a username of |id > /tmp/marker #, which builds the
command line

    echo |id > /tmp/marker # > /tmp/UserName

The shell treats the hash as a comment that swallows the sink's own redirect
and runs id as the right-hand side of a pipeline, so the injected command
executes and the file the handler was supposed to write is never created.

The defence that arrives too late. An escape loop that replaces a hash with a
backslash-escaped hash does exist in this handler, running between 0x441f4c
and 0x441fb0. Two facts dispose of it. First, the instruction order: the loop
is after system() at 0x441f1c and there is no branch back to it. Second, the
buffer: the loop writes into the configuration buffer at sp+0x18, which is
what apmib_set(0x6d, ...) stores at 0x44200c, not the buffer handed to the
shell. The developer escaped the hash character for the value that gets stored
and escaped nothing for the value that gets executed, which is a defensible
priority if the threat model is a hash in a stored username breaking some
later script that reads the configuration, and no defence at all against this
sink. The dynamic replication confirms the consequence: the hash in the
injected username reaches the shell as a comment and the sink's own redirect
never fires.

The sanitiser audit, and one trap for anyone re-reading the decompilation.
Between websGetVar and system the only operations on the value are strcpy at
0x441e94, strlen at 0x441ea8, the inline immediate-0x3b scan and the unquoted
sprintf at 0x441ee8. No regex call, no inet_aton, no isdigit, no isalnum, no
strchr, no strcspn, no vendor validation helper and no custom validator
appears on that path. The inet_aton calls that do exist in this function, at
0x441dd0 and 0x441e14, belong to the static-IP branch, wanMode 1, reached via
the branch at 0x441d8c; the wanMode 2 comparison sends execution straight to
the PPP branch and never enters that code. A quick read of the decompilation
therefore misleads, because the function as a whole does contain address
validation while the path that matters contains none.

One root cause, three reachable parameters. The same construction appears
three times in this handler, each selected by a value the request supplies:
pppUserName on wanMode 2, with the sink region 0x441e74 to 0x441f1c and
configuration object 0x6d written after the sink; pptpUserName on wanMode 3,
from 0x4420d0 onward, configuration object 0xf3; and L2TPUserName on wanMode
6, from 0x44246c onward, configuration object 0x128. All three use the same
immediate-0x3b scan, the same echo format string and the same system() call
shape. The wanMode 2 path was verified instruction by instruction and
replicated dynamically; the other two are reported from reading the same
handler, which is a structural claim rather than a demonstrated one. A patch
confined to the PPP path leaves the PPTP and L2TP paths injectable.

A static comparison against a second model, offered as a lead and not as a
finding. A second Edimax firmware image, BR-6208AC_V2_1.03, carries a
different webs build, ELF 32-bit MSB MIPS-I, 816568 bytes, SHA256
3ad10a41d11c8cd59185eab6c9ce67b18cd2118942eb2201f48540d7846a0328, whose setWAN
implementation matches instruction for instruction: handler at 0x448710,
websGetVar for pppUserName at 0x4488b8, strcpy at 0x4488bc, the same inline
immediate-0x3b scan at 0x4488dc to 0x4488fc, the same sprintf into
/tmp/UserName at 0x448920 with its format string at 0x4a6954, system() at
0x448940, the same three parameters on the same three wanMode values, and the
same single-realm Basic authentication model behind the same configuration
flag. The differing addresses and binary size come from a different product
build; the vulnerable path itself does not differ. The reasonable inference is
a shared source component in the vendor's router software base. That model was
not tested, nothing was executed from that image, no score covers it, and it
is not an exploited finding on it.

Scope of the pattern. A count of the shipped registration table found 91
/goform/form* handlers, of which roughly 85 reach a system() or popen() call,
so the architectural root cause is a management server that builds shell
command lines by string interpolation rather than one careless field.
/goform/setWAN is not one of the four routes carrying a post-boot uptime gate
(/mp.asp, /goform/mp, /advanced_management.asp and /goform/formAdvManagement,
which redirect to /index.asp once /proc/uptime exceeds 600 seconds), so it is
reachable at any time the device is up.

Authentication and reach. The route requires a valid administrative session in
normal operation. The gate auth_authorize at 0x404d00 reads configuration
object...