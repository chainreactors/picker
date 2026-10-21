---
title: [0day-rubbish] TRENDnet TV-IP302PI firmware 1.02.38 authenticated NTP server-address OS command injection to root command execution via a shell-form system() call (7.2 High, PR:H)
url: https://seclists.org/fulldisclosure/2026/Oct/34
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:03.357144
---

# [0day-rubbish] TRENDnet TV-IP302PI firmware 1.02.38 authenticated NTP server-address OS command injection to root command execution via a shell-form system() call (7.2 High, PR:H)

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

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] TRENDnet TV-IP302PI firmware 1.02.38 authenticated NTP server-address OS command injection to root command execution via a shell-form system() call (7.2 High, PR:H)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:31:46 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in TRENDnet
TV-IP302PI firmware 1.02.38, the closed-source IP surveillance camera from
TRENDnet (United States). The camera's application daemon is shipped at
/hunt/hunt_server: an ARM 32-bit EABI5 version 5TE soft-float binary,
dynamically linked against /lib/ld-linux.so.3, 4.5 MB and stripped. Its own
string pool carries hunt_camera, HuntAudioConverter, HuntDataDirect and
PPPoE_TV-IP302PI next to the TRENDnet brand identifier, which identifies the
image as built on a Hunt Electronic camera platform OEM'd into this model. That
provenance matters twice: it tells an operator that the same construction may
exist in other products built on the same platform, and it tells a reader that
this finding is specific to that platform's binary, its configuration-key name
and its command template rather than to a generic NTP client.

Type and root cause. OS command injection, CWE-78 primary, with CWE-20 improper
input validation, and CWE-250 and CWE-269 contributing for the privilege shape.
An authenticated administrator who sets the NTP server address has the value
stored verbatim into the configuration parameter c64_Ntp_Server, at offset 0x9c
inside the configuration structure. The only validation applied on the way in is
a length cap: 48 bytes (0x30, via func_0x002a9ae0) on the HTTP form path and 64
bytes on the ONVIF SOAP path. No character is rejected. That same offset is later
read back by the time-synchronisation path, formatted with %s, unquoted and
unescaped, into the command template

    /hunt/msntp -ts %d -r %s &

and handed to system(), which runs the string through /bin/sh -c. The shell
re-parses it, so a semicolon, a $(...) command substitution or a backtick pair
inside what is supposed to be a time-server address terminates the NTP client
invocation and starts an arbitrary command in the daemon's own context. That
context is uid=0(root): the web tier performs no privilege drop, the boa
configuration file shipped in the image declares none, and the runtime
configuration model recovered from the binary contains no unprivileged identity
for the web tier to switch to. There is therefore no privilege-escalation stage
in this chain and none is claimed or needed.

The chain, link by link, with the offsets from the shipped binary.

Link 1 is a configuration write. The parameter table maps the HTTP form field to
the key c64_Ntp_Server, whose set callback at 0x2b668c compares the incoming
value against the stored one, returns early if they match, and otherwise copies
it into the slot. The decompiled shape is a bare strcpy. On a change the callback
raises a configuration event, event 2, through func_0x001ecddc. That event is how
the rest of the daemon learns that time synchronisation needs re-doing, and it is
also why the write itself is the trigger: in the ordinary case no second request
and no wait for a scheduled resynchronisation is required.

Link 2 is command construction. The event handler at 0x371d88, registered inside
fcn.002b700c, and the builder at 0x2760d0, called from the call site at 0x286264,
both read the same offset config+0x9c that link 1 wrote, and format it:

    snprintf(buf, 0x100,
             *p_fmt_at_0x3ded60,  /* "/hunt/msntp -ts %d -r %s &" */
             *(cfg + 0xe4),       /* the -ts flag: server-derived */
             cfg + 0x9c);         /* the address: attacker-supplied */
    func_0x001efbac(handle, 10, buf);   /* enqueue for the worker */

There is no quoting of any kind around the %s. The -ts flag comes from cfg+0xe4
and is not attacker-controlled; the address argument is, completely. That the
write offset and the read offset are the same value is the load-bearing detail of
the static half of this work, because it is what ties the tainted input to the
tainted argument without anyone having to guess at a structure layout.

Link 3 is execution. The enqueue helper func_0x001efbac hands the finished string
to a queue worker that calls system(buf). The identification of system() as the
final executor is STATIC evidence and is reported as such: system is referenced
through the GOT entry at 0xc274, and that GOT slot is what distinguishes a
system() call site from an execve call site with a prepared argv. No dynamic
observation in this research watched the worker choose between the two forms.
Under an argv-form invocation the address would have reached msntp as one
argument element and every shell metacharacter inside it would have been inert
text passed to a resolver, which is exactly why that distinction is the whole
vulnerability rather than an implementation detail.

Two protocols write one slot, so this is one vulnerability with two sources rather
than two vulnerabilities. On the HTTP path the value arrives as POST parameter
NtpIP to apply.cgi or SetTime.cgi inside an authenticated session. On the ONVIF
path the same slot is written by the tds:SetNTP handler at 0x286218-0x286264,
which applies its own 64-byte length check, no content check, and then calls
fcn.002760d0 directly, so on that route the sink sits one call from the entry
point instead of being reached through the event dispatch. A fix applied only to
the HTTP form leaves the ONVIF entry point open, and the ONVIF path's larger cap
is the more comfortable carrier for a longer payload.

What validation is present and what is absent. Present: a length cap and nothing
else. Absent: any parse of the value as an address, no inet_aton or inet_pton, no
hostname-syntax check followed by re-serialisation of the resolved name; no
character allow-list, although for a time-server field the correct alphabet is
roughly [A-Za-z0-9._:-], which excludes every metacharacter in this chain; no
deny-list for the semicolon, pipe, ampersand, dollar sign, backtick, parentheses,
angle brackets, newline, carriage return or quote characters, so nothing rejects
even the crudest payload; no quoting or escaping at the interpolation site; and no
argv-form invocation of /hunt/msntp, which alone would have removed the shell from
the picture and made all four preceding items unnecessary. The shape of the defect
in one line: the value is checked for how long it is and never for what it is. A
length cap of that kind exists to protect a fixed-size configuration slot from
overrunning, and on that job it appears to work. Forty-eight bytes admits every
injection form used in this research several times over, the shortest of which is
17 bytes.

One sanitization-shaped behaviour that is not one is worth knowing before
reproducing this: the set callback's strcmp early-return suppresses the change
event when the new value is byte-identical to the stored one, so posting the same
payload twice does not re-fire the sink. Vary the payload between attempts, for
example by changing the marker filename, which costs one byte and changes nothing
about the finding.

Authentication, and what is credited. Th...