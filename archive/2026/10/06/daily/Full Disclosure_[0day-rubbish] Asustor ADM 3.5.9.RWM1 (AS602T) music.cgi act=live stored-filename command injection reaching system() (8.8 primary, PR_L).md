---
title: [0day-rubbish] Asustor ADM 3.5.9.RWM1 (AS602T) music.cgi act=live stored-filename command injection reaching system() (8.8 primary, PR:L)
url: https://seclists.org/fulldisclosure/2026/Oct/3
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.897893
---

# [0day-rubbish] Asustor ADM 3.5.9.RWM1 (AS602T) music.cgi act=live stored-filename command injection reaching system() (8.8 primary, PR:L)

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Asustor ADM 3.5.9.RWM1 (AS602T) music.cgi act=live stored-filename command injection reaching system() (8.8 primary, PR:L)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:52:41 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the
media handler of the ADM (ASUSTOR Data Master) management portal, verified by
static analysis on the AS602T running ADM 3.5.9.RWM1 (x86-64, first-
generation G1 firmware line, from the distributed image
ADM_X64_G1_3.5.9.RWM1_AS602T.img).

Type: OS command injection (CWE-78), enabled by an argument-quoting breakout
(CWE-88) and by an incomplete list of disallowed values (CWE-184). In the
act=live branch of usr/builtin/webman/portal/apis/fileExplorer/music.cgi the
handler composes an ffmpeg transcode command with snprintf at 0x4029a9 using
the format string at 0x4035f8, which places the stored media file path inside
a pair of literal shell double quotes, and executes the result at 0x4029b6
through As_System in libgeneral.so.0.0 (0x4509b), which is system(), that is
/bin/sh -c. The stored path arrives through the file parameter of act=add,
read by O_CGI_AGENT::Get_Param at 0x401cab, split only on comma, colon and
question mark (0x4036f7) and copied verbatim into the music-list entry field
at +0x84; the handler never imports the library's general escaping helper.
Before execution As_System calls
Try_Escaping_Characters_To_Avoid_Command_Injection (0x44f95), whose deny-list
at 0xb25da is exactly two bytes, the backtick and the dollar sign. When
neither appears the helper returns 0x72, the escape buffer stays empty and the
original string reaches the shell unmodified, so a file name of the shape
x";id>marker;#.mp3 closes the application's own quote, chains a command with a
semicolon and comments out the rest of the format string with a hash, using
neither denied byte. Because the dollar sign is escaped, command substitution
does not work, and the injected command must be free of slash, comma, colon
and question mark; the quote, semicolon, pipe, ampersand, redirection
characters and hash are never examined.

Scoring. Three readings are published with their vectors rather than one
flattering number:
- PRIMARY, 8.8 High, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H. The only
  property consulted between caller and handler on this path is session
  validity: O_CGI_AGENT::Revive_Session (0x4017b0 / 0x4017ee) is fail-closed
  and runs before any act dispatch, and nothing in the handler's entry path
  consults a role or privilege attribute.
- CONDITIONAL AND UNTESTED, 7.2 High,
  CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, for a deployment that
  confines the media library or the file explorer to the administrator role.
  No authentication of any kind took place in this research, no ADM
  permission artefact establishing that confinement was located, and the
  reading was never exercised, so it is published as a configuration-
  dependent alternative and not as an observation.
- CONSIDERED AND REJECTED, the unauthenticated vector
  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, which would compute to 9.8.
  It is not claimed: the session gate is fail-closed, the eleven
  pre-authentication portal interfaces enumerated during this research
  contain no As_System or As_Popen sink, and two independent sweeps of the
  unauthenticated surface, HTTP and non-HTTP, both concluded the sink is not
  reachable without a session.

A factory default administrator credential pair (CWE-798) also exists in this
build and is reported as a separate issue. It is not the vector used here and
it justifies no metric value above.

Impact: command execution in the CGI process's identity on a storage
appliance, which reaches every volume, share and snapshot the device hosts,
including other users' home shares and backup data landed on the device,
because no privilege separation exists between the portal role and the file
system; stored data can be modified or destroyed, firmware-update staging
files replaced, persistent implants installed in the root filesystem or in
scheduled tasks, and configuration and credential stores rewritten; the
device can be stopped, rebooted, its shares unmounted, or its data encrypted
or wiped. Where the portal is published to the internet for remote access, one
valid portal credential is the only barrier between an internet-based attacker
and that outcome. CVSS scope stays Unchanged: vulnerable and impacted
components sit inside one security authority.

Verification boundary, stated plainly, and it is narrower than the finding may
first appear. No physical AS602T was used, no whole-system emulation of ADM
was achieved, and no request was ever sent to a device: login.cgi, upload.cgi
and music.cgi were never addressed over the network, so every request and
response shape published comes from static analysis, and end-to-end HTTP
exploitation against a NAS is not claimed. The executed evidence is a faithful
C replication of the sink semantics, reproducing the format string, the
argument order, the 1024-byte buffer bound and the backslash-parity counting
logic of the escaping helper including the 0x72 return, compiled and run as
uid 0 on a generic x86-64 Linux analysis host: the quote-breakout payload
produced a 39-byte root-owned marker containing uid=0(root) gid=0(root)
groups=0(root), while a command-substitution control payload, which shows the
escaper does work on the dollar sign, and a benign file name produced nothing.
uid 0 was measured only in that harness; the on-device CGI process identity
was never measured and root on the appliance is an inference from how handlers
of this class commonly run on network-attached storage. Neither the real
music.cgi binary nor the real libgeneral.so.0.0 was executed. The static chain
was independently re-derived from the raw disassembly by a second analyst,
including the sink, the call site, the register mapping (rcx the fixed ffmpeg
literal, r8 the stored path at +0x84, xmm0 the seek time), the identity of
As_System and the two-byte deny-list, and an adversarial falsification pass
over four angles could not refute any link.

Affected scope: ADM 3.5.9.RWM1 on AS602T is verified; ADM 4.0.7.RVG1 on
AS1002T (ARM Marvell 88F6820) is cross-checked at code and command level,
music.cgi importing As_System and Get_Param but not Get_Escaped_String_General
with a byte-identical -i "%s" sink format, and the constructed command
producing a root marker under ARM user-mode emulation with that build's own
root filesystem, which is not a demonstration that its HTTP surface behaves
identically; other ADM builds older than 5.1.2 on other models are unverified
candidates that this advisory does not report as affected; and in the newer
ADM 5.1.4 build compared during this research As_System and As_Popen remain
exported at the same offsets but have no callers, with command execution moved
to Execute_Command_File and Execute_Command_Line (fork plus execv plus an
argument tokeniser, no shell), so that build was recorded as having no
equivalent remote code execution. No modern ADM release was run dynamically
and nothing here implies that any current release is v...