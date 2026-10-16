---
title: [0day-rubbish] Maian Guardian 2.1 license generator projid command injection to www-data uid 33 code execution (7.2, PR:H)
url: https://seclists.org/fulldisclosure/2026/Oct/16
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:52.420925
---

# [0day-rubbish] Maian Guardian 2.1 license generator projid command injection to www-data uid 33 code execution (7.2, PR:H)

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Maian Guardian 2.1 license generator projid command injection to www-data uid 33 code execution (7.2, PR:H)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:21:47 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Maian
Guardian 2.1, the self-hosted licensing system for PHP applications encoded
with SourceGuardian, distributed as a closed-source commercial PHP script by
Maian Script World (United Kingdom) and verified end to end against a real
installation of that version.

Type: OS command injection (CWE-78 primary; CWE-116, CWE-20 and CWE-561
contributing; CWE-250 and CWE-732 as environmental amplifiers of the same
event). The license-generation routine builds an operating-system command line
by string interpolation and passes it to shell_exec() at
`control/classes/class.licensing.php:261` inside `guardianLicense::create()`, in
order to invoke the external SourceGuardian generator binary. Several of the
interpolated fields arrive unvalidated from the body of the administrator AJAX
operation `POST /admin/index.php?ajax-ops=generate` - projid, projkey, the
license property key and value pairs, and the encoder string - and are placed
inside double quotes rather than argument-quoted, so POSIX command substitution
still applies:

    shell_exec(mswSGLicGenPath('"', $this->settings) . " $string $output");
    $lock[] = '--projid "'  . $this->projid  . '"';   // line 112
    $lock[] = '--projkey "' . $this->projkey . '"';   // line 113

The rendered command line is therefore
`"<licpath>" --projid "<PROJID>" --projkey "<PROJKEY>" --const "<KEY>=<VALUE>"
... <output>`, where PROJID is whatever an authenticated administrator posted.
PHP hands that text to `/bin/sh -c`, and inside a double-quoted word the shell
does not treat `$(`, a backtick or a backslash as literal. A projid of `$(id)`
spawns `id` in a subshell and substitutes its output into the argument, and it
does so during expansion, before the command word is resolved - which is why a
deployment with a missing or misconfigured generator binary is still fully
exploitable.

The decisive detail is the sanitizer arrangement, and it is the whole root
cause. Three sanitizer-shaped helpers ship with the product; two of them return
their input unchanged and sit in series on the path to the shell, and the one
that correctly wraps escapeshellarg has no call site anywhere in the product:

    private function escape($data) {     return $data; }   // lines 68-70
    private function escapeArg($data) { return escapeshellarg($data); }
                                                           // lines 72-74

`escape()` is the function actually called on the way to the shell, and it does
nothing. `mswCD()` at lines 152-154 is a second `return $data;`, applied to the
property key and value immediately before `escape()`, so two no-ops are stacked
in a row on the properties path. `escapeArg()` wraps exactly the right primitive
and is dead code: a sweep of all 308 PHP files in the shipped tree found no call
site for it, which reads as a completed remediation that never landed. A fourth
helper, `escapeCmd()` around `escapeshellcmd()`, is real and is invoked, but only
from `head()`, `time_servers()` and `add_lic_info()` - never from `lock()` or
`properties()` - so it guards the fields with the least attacker control and
never sees the two that carry project identifiers. Upstream of the class the
only request-wide filter is `mswMDAM('trim', $_POST)` at
`control/functions.php:342`, which applies trim() and nothing else; there is no
character allow-list, no length cap and no metacharacter rejection anywhere
between the POST body and the shell_exec() argument.

Commands execute as the web server service account, observed as
`uid=33(www-data) gid=33(www-data) groups=33(www-data)`. No setuid transition,
wrapper, privilege drop or sandbox sits between the web worker and the child
process. Root was not reached, was not attempted, and is not claimed.

How confirmation works, and what was deliberately not reproduced. The generate
operation does not echo command output into its HTTP response: it answered HTTP
200 with its ordinary `{"status":"rdr"}` body, the response shape it produces
when the generator creates no valid license file. Proof of execution is
therefore out-of-band by construction. The injected command writes a marker file
and the same installation serves it back over HTTP; one authenticated request
executed six distinct commands into that single file, including a pipeline,
`cat /etc/passwd | head -3`, which is what separates arbitrary command execution
from one hard-coded effect. An earlier iteration of the same chain wrote its
marker outside the document root and was confirmed there first, so write
capability is stated as observed both inside and outside the web tree. The
published advisory reproduces the identity string but elides the container
hostname and the kernel build-timestamp field of the `uname -a` line, since both
are artefacts of one execution on one host rather than evidence about the
product.

Scoring. One score is published: 7.2 High,
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H. That vector computes from first
principles to ISS = 1 - (0.44 x 0.44 x 0.44) = 0.914816, Impact(S:U) =
6.42 x 0.914816 = 5.87311872, Exploitability = 8.22 x 0.85 x 0.77 x 0.27 x 0.85
= 1.234707705, base 7.107826425, taken to 7.2 by the CVSS ceiling-to-tenth
Roundup - a calculator reporting 7.1 is disagreeing with the rounding rule and
with nothing else. AV:N describes the product's exposure and not our lab's: the
chain is three HTTP requests plus one read-back against the product's single
listener, and the loopback binding in our testbed was our own safety choice, not
a product property. AC:L because nothing outside the attacker's or a normal
deployment's control is needed - ENC_DEBUG is at its shipped value 0
(`control/options.php:37`), which selects the shell_exec() branch, and the
license-generator path is a setting a functioning installation already has.

PR:H is the metric carrying the weight, and the readings on either side of it
are printed with their own vectors so the arithmetic is inspectable. Published
reason: only an installer-provisioned administrator session was demonstrated
reaching the sink. The product does keep a `guard_staff` table, so a multi-user
deployment is possible, but our review found no role or permission column that
separates license generation from any other administrator operation and no
documented staff role with a narrower capability set; every path we traced to
`guardianLicense::create()` sat behind the administrator gate with the same
operation-level CSRF check. Three alternative readings are therefore labelled and
rejected rather than hidden:

  - Unauthenticated, AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H = 9.8. Rejected: no
      unauthenticated path reaches a sink. The remote license-issuing API at
      `control/api/api-remote.php` is gated by a key randomly generated at
      install time, which was not bypassed, and the product ships no factory
      credential because the installer sets the administrator account.
  - Lower-privileg...