---
title: [0day-rubbish] Exasol Database 7.1.30 docker-db form: shipped default SYS credential to PYTHON3 UDF os.popen command execution as uid=500(exadefusr), output returned in-band (8.8)
url: https://seclists.org/fulldisclosure/2026/Oct/30
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:04.764454
---

# [0day-rubbish] Exasol Database 7.1.30 docker-db form: shipped default SYS credential to PYTHON3 UDF os.popen command execution as uid=500(exadefusr), output returned in-band (8.8)

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Exasol Database 7.1.30 docker-db form: shipped default SYS credential to PYTHON3 UDF os.popen command execution as uid=500(exadefusr), output returned in-band (8.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:30:46 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Exasol
Database 7.1.30, the in-memory MPP analytical database from Exasol AG
(Germany), examined in its docker-db single-container deployment form. The SQL
engine is a proprietary C implementation named EXASolution, the server process
is exacts, clients speak a proprietary binary SQL protocol on port 8563 rather
than HTTP, TLS terminates on that port with a self-signed certificate carrying
no subjectAltName, and the vendor's console client exaplus ships inside the
image. Three further services share the container: ConfD, an HTTPS JSON-RPC
management daemon on 443; BucketFS, an HTTP file service observed on 2580; and
an OpenSSH server on 22. The image as pulled is about 6 GB and is distributed
through Docker Hub.

One fact about this deployment form belongs at the top rather than at the
bottom, because it explains why the research is public now instead of being
held for a patch. Exasol's own upstream repository warns that the docker
distribution is an open source project that is not officially supported by
Exasol; that the base image is an end-of-life CentOS 7 release; that official
support for docker-db 7 is no longer available and that users should move to a
newer release line; that the repository now only contains documentation while
the binaries are distributed through Docker Hub; that issues are disabled; and
that the project is mainly intended for automatic testing of Exasol
deployments. None of that reduces the mechanism, because the credential is a
property of the shipping database and the script engine is a supported core
feature of the product rather than a container add-on. It does mean that on
the vendor's own statements no fix is planned for this deployment form, so
there was no patch to coordinate around and holding the finding would have
left operators exposed without warning. Only version 7.1.30 in this deployment
form was executed. Other 7.1.x releases, the supported non-container
installation and the vendor's newer release line share the mechanism, a
constant SYS credential plus an unrestricted script language in the UDF
engine, and are plausibly affected; none was tested, that is stated as an
explicitly labelled inference, and no version range is claimed.

Type and root cause. Two defects, separable but jointly decisive, classified
as CWE-1392 use of default credentials (primary) and CWE-94 improper control
of generation of code (co-equal), with CWE-798 hard-coded credentials, CWE-78
OS command injection, CWE-1188 insecure default initialization and CWE-250
execution with unnecessary privileges recorded alongside, and CWE-284 and
CWE-862 reported separately for the absent source-address restriction on 8563
and the absent authorisation distinction for script creation. Neither
separately reported item raises a metric. Leg one on its own is a data breach.
Leg two on its own is a documented feature. The pair produces an entry point
that required no provisioning decision by anyone, because nobody ever created
the account an attacker uses, and that converts SQL-layer administrative
access into operating-system command execution with the command output
returned in-band through the ordinary result set.

The credential is the vendor's own published text, not a leak and not an
inference. The upstream docker-db README publishes it under the heading
"Connecting to the Database", instructing the reader to authenticate with
username sys and password exasol. Two image-internal CI test scripts use the
same pair against a freshly initialised database on the same port:
basic_test.sh:112 carries $X -c n11:8563 -u sys -P exasol -jdbcparam
validateservercertificate=0 and basic_sc_test.sh:98 uses -u sys -P exasol as
well. Those two files are not in the current upstream repository, which now
carries documentation only, so they are cited as artifacts observed inside the
7.1.30 image at /usr/opt/EXASuite-7/EXAClusterOS-7.1.30/docker/test/ and not
as repository contents. Nothing rotates the constant, and that was traced
rather than assumed: the running controller process command line carries no
-defaultSysPasswordHash argument; the [DB:DB1] stanza of EXAConf carries no
DefaultSysPasswdHash key; db_jobs.py:104 sets self.sys_passwd_text =
secrets.token_hex(20), which generates an additional random password rather
than replacing the built-in one; database.py:57 passes -defaultSysPasswordHash
only when EXAConf configures it explicitly; and the container's init-sc path
does not configure it. Nothing in the container's start path presents a
first-login change-password step, sets a must-change flag on the SYS account
or refuses service while the constant remains in place, and the README carries
guidance about persistent volumes, hugepages, resource limits and license
mounting with no instruction to change the SYS password; that absence is as
load-bearing as the presence of the constant. The conclusion, corrected once
during the research before being accepted, is that the accepted value is a
built-in default of the database engine rather than a hash handed to it by the
container initialiser, and both the built-in value and the generated random
are accepted, which is why random generation in the provisioning code is not a
defence. The contrast the product supplies is what makes this a defect rather
than a design choice: Exasol generated per-deployment randoms for two of its
three service credentials, the ConfD AuthenticationToken and the BucketFS
WritePasswd, and did not do so for the most privileged one, and an attacker
must read EXAConf to recover either random while sys / exasol is a constant
every installation shares and the documentation prints.

The sink, in full:

    CREATE SCHEMA IF NOT EXISTS poc_schema;
    OPEN SCHEMA poc_schema;
    CREATE OR REPLACE PYTHON3 SCALAR SCRIPT poc_udf()
      RETURNS VARCHAR(2000000) AS
    import os
    def run(ctx):
        out = os.popen("id").read()
        return 'RCE_OUT:' + out
    /
    SELECT poc_udf();

Three properties make this a sink rather than a curiosity. The os module is
importable with no declaration, allow-list or capability request. The command
string is an ordinary Python literal built from what the caller supplied, so
shell metacharacters, pipelines and quoting all work, and the measured round
used cat /etc/passwd | head -3 whose pipeline was honoured by the shell
os.popen starts. And the return value crosses the trust boundary back to the
caller through the ordinary result set, which removes the need for any
separate exfiltration channel. Sanitisation over what the body does is absent:
no module allow-list or deny-list, no policy forbidding os or subprocess, no
capability gate, no per-statement approval, no audit prompt and no privilege
beyond SYS itself. What does exist is well-formedness checking rather than a
security control: the engine validates the language alias, submitt...