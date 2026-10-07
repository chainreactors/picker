---
title: [0day-rubbish] Circutor LineEds 24.11.14-r0 unauthenticated pwrstudio events.xml shellExecute command injection (9.8)
url: https://seclists.org/fulldisclosure/2026/Oct/4
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.779474
---

# [0day-rubbish] Circutor LineEds 24.11.14-r0 unauthenticated pwrstudio events.xml shellExecute command injection (9.8)

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Circutor LineEds 24.11.14-r0 unauthenticated pwrstudio events.xml shellExecute command injection (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:52:58 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the pwrstudio
daemon shipped in Circutor LineEds (Line Energy Data System) industrial energy gateway
firmware 24.11.14-r0, engine variant pss0. Circutor S.A. is in Spain; the appliance sits
between metering and power-quality instrumentation on one side and an energy-management
or SCADA back office on the other.

Type: operating-system command injection (CWE-78) reached without authentication
(CWE-306). Those two are the classes recorded in the research; the advisory's own
classification additionally maps CWE-285, because the permission gate fails open in two
independent ways, and CWE-20, because the events document is accepted with no schema
validation, as contributing weaknesses, with CWE-250/CWE-269 recorded as bearing on
remediation priority rather than on the defect.

Root cause: the daemon's event engine loads its configuration from events.xml, exposed at
/services/user/events.xml over the management HTTP interface. An event may carry a
shellExecute action whose command and parameter elements are concatenated by
XCEventActionShellExecute::Execute (FUN_00548414) with the wide-string format "%ls %ls"
stored at 0x7cc2d0, converted from wide to narrow, and passed to system() at call site
0x5484bc. Nothing between the socket and the sink neutralises shell metacharacters: no
quoting, no filtering, no allowlist. The format string is the whole reason the injection
works the way it does - two %ls conversions separated by a single space mean the sink
performs concatenation rather than argument separation, so command and parameter become one
shell word sequence with no quoting boundary between them; a payload needs only a statement
separator, not a quote escape. The defect is at that concatenation rather than in the XML
parser, which performs a pure element-to-field copy and is behaving correctly.

Exploitation is two HTTP requests with no delivery precondition of any kind. Step one
writes an event definition into /services/user/events.xml carrying an always-true
condition so it enters the live set on every evaluation pass, a deliberately invalid
command token so the first shell statement fails harmlessly, and a parameter of the form
semicolon, command, semicolon, hash - yielding a shell line such as
"x ;id >/tmp/circutor_eds_vuln_rce_marker;#". Step two requests the restart.xml route,
which makes the engine reload the document through XCEventDriver::LoadXml (FUN_0020acac),
build the action object, evaluate the condition and dispatch Execute. There is no race, no
memory-layout dependency, no file to pre-place on the target and no dependence on another
vulnerability, and because the intermediate state is a file the product itself persists,
the two steps can be separated in time arbitrarily. The binary is compiled with
CONFIG_NO_HASP, so no licence-dongle gate stands between a written event and the shell
action. The image is a non-PIE EXEC, so every offset quoted is a fixed file-and-memory
address reproducible against the same build with no relocation arithmetic.

Unauthenticated classification, and it does not rest on a configuration assumption. The
product implements authorization as a per-handler gate rather than as a dispatcher
middleware stage: the gate is one function, FUN_001a93cc, invoked with a permission
constant by whichever handler chooses to invoke it. A cross-reference census of that
function in the shipped binary records 197 call sites, all individual action handlers, all
inside the address range 0x1aexxx to 0x1bfxxx. Both handlers in this chain fall outside it:
the restart handler FUN_001e3554 at 0x1e3554 and the events write handler FUN_0023ace0 at
0x23ace0. The gate is therefore structurally incapable of authorizing either, because it is
never invoked on their paths. The restart handler's only guard is FUN_001a955c, a
three-instruction predicate testing that the request-context fields at +0x34 and +0x4c are
both non-null; those are the request and response object pointers installed
unconditionally by the dispatcher's own setup routine FUN_001add40, which the route entry
at 0x76a480 names at offset +0x0c, ahead of the handler at +0x10. It tests object presence,
not credentials. One honest tension is published rather than smoothed over: the events write
handler and its dispatcher contain no authorization call that we could find, yet the handler
is recorded as capable of both 401 and 200 outcomes and we could not determine what selects
the 401 branch - so a credential-required conditional score is carried alongside the
primary rating precisely to account for that unresolved path.

A second, configuration-independent defect is documented in the same advisory. The gate's
own logic returns success with no check of any kind when the permission constant is not
0x15, and returns success when enforcement is toggled off, so it fails open in two
independent ways for the 197 handlers that do call it. This chain does not depend on that
defect, and the advisory deliberately makes no claim that any specific other route is a
second path to command execution; it is reported as a separate finding for vendor review.

Two claims carried by the research record are deliberately NOT published as fact. First,
that security enforcement is off by default: no shipped artifact supports the default value
- nothing inside the image, no value read from the extracted root filesystem, not the
contents of the engine.xml package, and no vendor documentation of the factory setting. The
unauthenticated classification does not depend on it, because neither route in the chain
invokes the gate at all; the default matters only for the alternative reloadCfg.xml
trigger, whose reload action does call the gate with permission 0x15, and that variant is
treated as conditional. Second, that pwrstudio runs as root on a device: the observed
uid=0(root) is the privilege of the root-run emulation harness, and the device-side account
is inferred from the daemon's ownership of the restart, reload and upgrade routes, since no
init script or service unit was extracted. Neither caveat alters the impact metrics.

Scoring. Four readings were priced and all four are published, two of them as not adopted:
- PRIMARY, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- CONDITIONAL, 8.8 High, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H, applying where a
  deployment rejects anonymous configuration writes - enforcement enabled, or the events
  handler's unresolved 401 branch active - so that any valid operator credential suffices.
  Nothing else in the chain changes.
- NOT ADOPTED, 10.0 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H - the Scope
  Changed reading a reviewer who counts the appliance OS as a realm distinct from the
  management daemon would apply. We do not adopt it: the command executes inside the
  authority the vulnerable component already holds and no sandbox, container,
  virtualisation boundary or separate se...