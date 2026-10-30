---
title: [0day-rubbish] Raritan PX3 PDU G4 firmware 4.3.14 command injection in the ping and traceroute diagnostics through an inverted hostname-validation return check (8.8)
url: https://seclists.org/fulldisclosure/2026/Oct/54
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:39.457412
---

# [0day-rubbish] Raritan PX3 PDU G4 firmware 4.3.14 command injection in the ping and traceroute diagnostics through an inverted hostname-validation return check (8.8)

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

[![Previous](/images/left-icon-16x16.png)](56)
[By Date](date.html#54)
[![Next](/images/right-icon-16x16.png)](57)

[![Previous](/images/left-icon-16x16.png)](56)
[By Thread](index.html#54)
[![Next](/images/right-icon-16x16.png)](57)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Raritan PX3 PDU G4 firmware 4.3.14 command injection in the ping and traceroute diagnostics through an inverted hostname-validation return check (8.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:39:44 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the
Raritan PX3 PDU G4, firmware version 4.3.14, the intelligent rack power
distribution unit from Raritan, a Legrand company (United States). A
low-privilege authenticated session converts one diagnostics request into
operating-system command execution in the product's web-service context,
because the hostname validation that is supposed to gate the ping and
traceroute commands produces the correct rejection verdict and the caller then
executes on it anyway.

Type and root cause. CWE-78, OS command injection, with CWE-20 co-equal,
in the diagnostics service of /lib/libisys.so.1.0. The firmware is an aarch64
embedded Linux image whose web tier is a custom 1.8 MB C++ daemon, /bin/httpd,
built on an IDL-RPC framework: an authentication subsystem the binary refers
to as pp::aaa, a JSON-RPC name service, and seventy-five service namespaces,
all behind per-method authentication. The two diagnostics implementations,
isys::net::diag::ping at 0x5a988 and isys::net::diag::traceRoute at 0x5ab64,
do not perform network operations themselves: they assemble shell command
strings from the operator-supplied hostname and execute them through /bin/sh,
via pp::BackgroundCommand::open(bgCmd, "/bin/sh", argv) at 0x36170, reached
through runShellCommandAndGetResults() at 0x36094, which logs the command it
is about to run. The templates are ping -c <count> -W <timeout> <HOST> 2>&1
and traceroute -w <timeout> -m 30 <HOST> 2>&1, with ping6 and traceroute6
variants; the neighbouring string table carries "ping", "ping6", "traceroute",
"traceroute6", "2>&1" and the source file name "DiagnosticsImpl.cpp".

The defect is a returned verdict consumed with the wrong comparison. The
validation function, validateAndResolveHostName() at 0x5a3f4, is not a stub:
it walks the hostname character by character, explicitly rejects the percent
sign and every character above the ASCII colon, cross-checks that the host
resolves through the resolver service, and returns one constant, three, on
every rejection path - the rejection block converges at the load of that
constant and returns at 0x5a54c. Both consumers evaluate the verdict with an
unsigned strictly-greater branch: a return of three is not strictly greater
than three, so it falls through, and the rejected hostname is spliced into the
shell template verbatim. The result is an injection whose success condition is
the validator working exactly as designed: a semicolon is caught by the
character loop, a dollar or parenthesis survives the loop but fails
resolution, and all of them - caught or unresolved - flow into the command
template. A host value of 1.1.1.1;id>/tmp/marker;# keeps the ping segment
syntactically complete, runs the injected statement as a second shell
statement, and the trailing hash comments out the template's 2>&1 suffix; the
subshell form and a newline-separated form ride the same rejection path; the
traceroute template arms the second entry point identically. The image
contains a strict fully-qualified-hostname validator in libnetwork.so, but
the web daemon does not import it and the diagnostics library neither links
nor loads it on this code path.

The request that reaches the sink looks like this, transmitted as one JSON
body over the authenticated RPC channel:

```
{
  "jsonrpc": "2.0",
  "method": "net.Diagnostics.ping",
  "params": {
    "host": "1.1.1.1;id>/tmp/marker;#",
    "count": 1,
    "timeout": 1
  },
  "id": 2
}
```

The same attacker string rides the hostname argument of the corresponding CLI
commands. The 2>&1 merge suffix is an amplifier the attacker inherits for
free: whatever the injected command prints on either stream is captured by the
same mechanism that returns ping output, so the response channel doubles as
the command-output channel and no out-of-band exfiltration is needed.

Reach and privileges. The web methods sit behind the framework's per-method
authentication and no bypass of that boundary was measured. The load-bearing
privilege artifact is the shipped CLI configuration, /etc/clish/netdiag.xml:
ping and traceroute are defined with no access attribute - available to every
authenticated CLI user in this framework's grammar - while the neighbouring
netstat command carries access="admin". The vendor's own artifact therefore
documents that these two functions were deliberately placed in the
all-authenticated-users class, presumably on the theory that a ping is
harmless. On a rack PDU, management is a network service at a datacenter's
softest point, and the finding's effective audience is every monitoring
account, operations automation role and integration credential granted "just
to poll".

Severity. The published score is 8.8 High,
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H: ISS = 1 - (1 - 0.56) x (1 -
0.56) x (1 - 0.56) = 0.914816, impact = 6.42 x 0.914816 = 5.869119,
exploitability = 8.22 x 0.85 x 0.77 x 0.62 x 0.85 = 2.835255, base =
5.869119 + 2.835255 = 8.704374, rounded up to 8.8. A PR:N reading of 9.8
Critical (impact 5.869119 plus exploitability 3.887043, total 9.756162) is
rejected: no authentication bypass was measured. Two conditional readings are
published as explicitly labelled conditionals and never as the headline. The
first applies where a deployment still carries the factory default
administrative credential pair recorded in the image's configuration default
area for first-boot access: the same PR:N vector computes to 9.8 Critical for
the chain of that adjacent weakness plus this injection, and a changed
credential removes it; the default pair is disclosed as a separate weakness
and is not folded into the published vector. The second applies only to
deployments in which no low-privilege account is provisioned and every caller
holds administrator privileges: the PR:H vector computes to 7.2 High
(exploitability 1.234708 plus 5.869119, total 7.103826), and it is not the
headline because the vendor's own shipped CLI artifact grants diagnostics to
all authenticated users.

Verification method, and its boundary. Every static claim is measured from the
firmware image at instruction level: the templates, the character loop, the
converging rejection blocks, the consumers' compare-and-branch sequences, the
shell open, and the two import facts. The dynamic layer is a command-level
replication of the recovered sink semantics on an isolated research host: the
exact reconstructed templates were executed through a shell under the
semicolon, subshell and traceroute injection shapes, and each produced the
marker command's output, while a metacharacter-free control produced nothing
and the marker path was confirmed absent afterwards. What was not done: no
end-to-end exploitation through the management interface of a physical unit.
No physical unit was available, and full-system emulation was blocked by the
management daemon's dependency on the configuration daemon and the flash
...