---
title: [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 scenario ping condition command injection through the auto-executing ping thread (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/55
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:40.071159
---

# [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 scenario ping condition command injection through the auto-executing ping thread (7.2)

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

[![Previous](/images/left-icon-16x16.png)](53)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](53)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Moxa MAR-2000 firmware FWR\_MAR2000\_V1.0\_Build\_15010909 scenario ping condition command injection through the auto-executing ping thread (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:39:17 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the Moxa
MAR-2000 series industrial 4G/LTE cellular router, firmware image
FWR_MAR2000_V1.0_Build_15010909, from Moxa Inc. (Taiwan). An authenticated
administrator converts one saved monitoring-condition field into recurring,
product-scheduled arbitrary command execution, because the thread that
implements the scenario ping condition builds its command line from the
condition's stored parameter values and hands them to a shell, and no layer
of the backend inspects what those values hold. The delivery needs no second
request: the product's own scenario watchdog evaluates the condition on its
schedule, which also makes the payload recur on every evaluation cycle until
the condition is deleted. This is one of three independent command injection
findings documented for this product and released together as a set.

Type and root cause. CWE-78, OS command injection, with CWE-20 co-equal, in
the Scenario model at /home/model/scenario/scenario.py inside the ARM
Debian 6.0.8 root filesystem of the firmware, which runs the vendor's MIRF
(Mobile Intelligent Routing Framework) stack: a Node.js Express 4.0
management application on port 80 bound to all interfaces, the express-sanji
middleware bridging REST resources onto a local MQTT broker, and Python 2.6
model scripts that persist configuration and act on it. The scenario
facility is how an operator automates behaviour on a schedule; a condition
of type ping is the canonical connectivity check. A saved ping condition
carries a parameter object with ip (required), interface (defaulting to
eth0) and times (defaulting to 3). When the watchdog reaches the condition
it starts a background thread whose run method assembles

```
cmd = "ping %s -c 1 -w 5 -I %s " % (ip, interface)
subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
```

The interpolation is textual into a single string handed to /bin/sh, so the
stored bytes are parsed as command syntax, and both stored fields - ip and
interface - sit in operand positions of the same template, giving two
stored fields of one class inside one condition. The values got there
through PUT /api/v1/scenario, where the model's put handler validates only
that the submitted data object exists and is non-empty. No parameter value
is examined at any layer of the stack: not by the Express middleware, not
by the message translation, not on the broker leg, not at storage, and not
when the thread reads the condition back.

Two payload-engineering results are published with the finding because they
were measured, not intuited. The template places the stored ip value before
the -c 1 and -w 5 flags, so the naive semicolon form that works against
several other sinks does not fit here: it splits the line in front of the
count flag, leaves an unbounded ping in the foreground of the evaluating
thread, and in the replication record the marker never appeared before the
thread was torn down. The two verified forms are a command substitution,
which the shell expands during command expansion before the ping binary even
starts and whose expansion result is discarded into the ping operand, and a
newline separator, which leaves the ping its own line with the flags intact
and runs the injected text as a second command line. The failing form is
also a finding in its own right: the same unvalidated field, used with the
naive form, turns the monitoring thread into a blocked thread - a
denial-of-service lever against the product's scenario machinery.

The one-request chain looks like this after login:

```
PUT /api/v1/scenario
{"data": {"condition": [{
    "name": "connectivity_check",
    "type": "ping",
    "parameter": {
        "ip": "$(id > <marker>)",
        "interface": "eth0",
        "times": 3
    }}]}}
-> stored verbatim (the put handler checks only that data exists,
   is non-empty); the watchdog's next evaluation starts the thread
-> cmd = "ping $(id > <marker>) -c 1 -w 5 -I eth0 "
-> the shell expands the substitution before ping execs; the
   marker carries the proof, ping then exits quickly, and the
   condition re-evaluates on the next cycle
```

Authentication and reach. The validateUser middleware is the only
authentication check on the REST surface: it requires a server-side session
for every non-GET method, and login is POST /api/login compared against
bcrypt-hashed entries in the SQLite user table. The PUT that stores the
payload requires the session; past that check there is no second
authorisation layer, the broker leg carries no identity, and the model
implements no permission judgement, so the product's single documented
role, the device administrator, is the whole security boundary. The
listener binds all interfaces on port 80 in the shipped firmware; no WAN
exposure is assumed anywhere in the published rating.

Severity. The published score is 7.2 High,
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, from ISS = 0.914816, impact
5.873119, exploitability 1.234708 and base 7.107826 rounded up to 7.2,
Privileges Required High being the product's single administrator role. A
labelled conditional and never the headline: where a deployment still runs
the factory default administrator pair carried by the shipped firmware's
SQLite user table, the prerequisite collapses and the chain reads 9.8
Critical on the PR:N vector (exploitability 3.887043, base 9.760161); a
changed credential removes it, and the default pair is disclosed as a
separate weakness, never folded into the published vector. A PR:L reading
of 8.8 High is published only as the arithmetic of the rejected variant.
The score provenance is disclosed in public: the research record behind
this advisory carried 8.8 for all three same-product findings, that figure
is the arithmetic of a PR:L vector, no artefact shows a lower-privileged
product role, and every published number was recomputed from its own
vector - which lowered the researchers' own figure by 1.6 points. A
Scope-Changed reading computes to 9.1 and is deliberately not published,
because the model process belongs to the same single-purpose appliance
authority, and running scheduled monitoring through the management plane
is the product's design rather than an escape.

Verification method, and its boundary. Two evidence classes carry the
finding, kept separate in the published advisory. The firmware's own
application sources establish the scenario write path, the write handler's
validation scope and the thread construction, read from the shipped files.
The dynamic layer is a sink-level replication on an isolated cloud Linux
sandbox: the exact template with the same shell=True launch and both pipes
captured, executed under the substitution form, the newline form, the naive
semicolon form and a benign control. Both verified forms produced a marker
file containing uid=0(root); the naive form produced no marker in the tested
window, for the unbounded-ping reas...