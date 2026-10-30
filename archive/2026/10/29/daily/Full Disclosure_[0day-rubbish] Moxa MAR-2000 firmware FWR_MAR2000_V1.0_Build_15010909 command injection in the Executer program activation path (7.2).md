---
title: [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 command injection in the Executer program activation path (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/52
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:40.682932
---

# [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 command injection in the Executer program activation path (7.2)

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

[![Previous](/images/left-icon-16x16.png)](51)
[By Date](date.html#52)
[![Next](/images/right-icon-16x16.png)](53)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#52)
[![Next](/images/right-icon-16x16.png)](53)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Moxa MAR-2000 firmware FWR\_MAR2000\_V1.0\_Build\_15010909 command injection in the Executer program activation path (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:38:41 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the Moxa
MAR-2000 series industrial 4G/LTE cellular router, firmware image
FWR_MAR2000_V1.0_Build_15010909, from Moxa Inc. (Taiwan). An authenticated
administrator converts one stored configuration field into arbitrary command
execution as the identity of the product's model process, because the
Executer model builds the launch command of an operator program as a shell
string whose program-argument column is never validated by any layer of the
backend. This is one of three independent command injection findings
documented for this product and released together as a set.

Type and root cause. CWE-78, OS command injection, with CWE-20 co-equal, in
the Executer model at /home/model/system/executer/executer.py inside the
ARM Debian 6.0.8 root filesystem of the firmware, which runs the vendor's
MIRF (Mobile Intelligent Routing Framework) stack: a Node.js Express 4.0
management application on port 80 bound to all interfaces, the express-sanji
middleware bridging REST resources onto a local MQTT broker, and Python 2.6
model scripts that persist configuration and act on it. The model stores
one row per operator program in an SQLite table whose columns include
fileName and argument. On activation it assembles the command as
str(execute_file) + " " + str(argument) and launches it with
subprocess.Popen(full_command, shell=True, preexec_fn=os.setsid), where the
row's argument bytes are concatenated verbatim and shell=True delegates the
parsing to /bin/sh: semicolons, background operators, pipes, backticks and
command substitution all have their ordinary meaning. The value's
provenance is a database column set by an HTTP request: the row writer is
generic, taking every key of the PUT /api/v1/system/executer/program/<id>
request's data object and committing it with a plain SQL
UPDATE ... SET ... statement, with no per-column semantics anywhere on the
write path. The only gate on execution is a liveness check - the file must
exist under the user-program directory - and the product's own multipart
upload route, POST /api/v1/system/executer/program, satisfies it: the upload
applies only a filename normalisation, with no allowed-type list and no file
filter. The chain is therefore: log in, upload a benign script through the
product's own route, store "; <command>; #" in the row's argument field, and
activate the row with PUT /api/v1/system/executer/activatedProgram carrying
programId and runBit 1. The shell runs the uploaded script first, the
semicolon ends it, the injected statement runs, and the trailing hash
comments out the rest of the line. The same model contains a second,
structurally identical sink in its deletion path: it builds
"rm -rf %s" from the row's unvalidated fileName column and executes it with
subprocess.call(..., shell=True), guarded only by a comparison of the raw
value against a single slash, which blocks exactly one value and nothing
else, and requires no upload and no activation.

The two-request chain looks like this after login:

```
[1] POST /api/v1/system/executer/program      multipart, benign script
    -> stored under the user-program directory
[2] PUT  /api/v1/system/executer/program/<id>
    {"data": {"fileName": "<uploaded basename>",
              "argument": "; <command>; #"}}
    -> generic row writer commits both columns verbatim (SQLite)
[3] PUT  /api/v1/system/executer/activatedProgram
    {"data": {"programId": <id>, "runBit": 1}}
    -> Popen("<dir>/<file> ; <command>; #", shell=True)
```

Authentication and reach. The validateUser middleware is the only
authentication check on the REST surface: it requires a server-side session
for every non-GET method, and login is POST /api/login compared against
bcrypt-hashed entries in the SQLite user table. Past that check there is no
second authorisation layer - the message bridge performs no permission
translation and the broker leg carries no identity - so the product's single
documented role, the device administrator, is the whole security boundary.
The listener binds all interfaces on port 80 in the shipped firmware; no
WAN exposure is assumed anywhere in the published rating.

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
of 8.8 High is published only as the arithmetic of the rejected variant. The
score provenance is disclosed in public: the research record behind this
advisory carried 8.8 for all three same-product findings, that figure is the
arithmetic of a PR:L vector, no artefact shows a lower-privileged product
role, and every published number was recomputed from its own vector - which
lowered the researchers' own figure by 1.6 points. A Scope-Changed reading
computes to 9.1 and is deliberately not published, because the model
process belongs to the same single-purpose appliance authority, and
commanding the appliance's own operating system through its management
plane is the product's design rather than an escape.

Verification method, and its boundary. Two evidence classes carry the
finding, kept separate in the published advisory. The firmware's own
application sources establish the entry path, the storage semantics and the
exact sink construction, read from the shipped files. The dynamic layer is
a sink-level replication on an isolated cloud Linux sandbox: the model's
exact concatenation with the shell=True launch, carrying a benign upload
stand-in, an injection payload and a benign control; with the payload in the
argument position a marker file containing uid=0(root) was created, and the
control produced the benign program launch and nothing else. The deletion
construction was replicated with the same method and also produced its
marker. The boundary is stated plainly: end-to-end detonation against
powered-on hardware is outside this research record, and the identity of the
model process on the device was neither measured nor claimed - uid=0(root)
is the replication sandbox's identity and nothing broader rests on it.

Impact. Arbitrary command execution as the identity of the Python model
process, begun by one authenticated configuration write and one activation
request, with no memory corruption and no protocol manipulation in the
chain. The command line is a stored configuration value that persists across
reboots and re-executes on every activati...