---
title: [0day-rubbish] NUUO Crystal Server 3.19.0.85 unauthenticated upload.php PHP web-root write with fastcgi execution into server-side code execution as the web service account (9.8 Critical)
url: https://seclists.org/fulldisclosure/2026/Oct/56
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:39.766622
---

# [0day-rubbish] NUUO Crystal Server 3.19.0.85 unauthenticated upload.php PHP web-root write with fastcgi execution into server-side code execution as the web service account (9.8 Critical)

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

[![Previous](/images/left-icon-16x16.png)](55)
[By Date](date.html#56)
[![Next](/images/right-icon-16x16.png)](54)

[![Previous](/images/left-icon-16x16.png)](55)
[By Thread](index.html#56)
[![Next](/images/right-icon-16x16.png)](54)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] NUUO Crystal Server 3.19.0.85 unauthenticated upload.php PHP web-root write with fastcgi execution into server-side code execution as the web service account (9.8 Critical)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:39:30 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in NUUO
Crystal Server 3.19.0.85, the video management and NVR server software from
NUUO Inc. of Taipei (Taiwan), distributed as the Crystal virtual-machine
appliance: an Ubuntu-based OVA whose web tier is a lighttpd server fronting
a PHP application, with .php requests dispatched to /usr/bin/php-cgi through
lighttpd's fastcgi mapping. The product sits in the management plane of
physical-security and critical-infrastructure video deployments, brokering
camera registration, recorder channels and the stored management credentials
of the surveillance estate.

Type and root cause. Inside the web root recovered from the appliance disk
image, upload.php is three lines long, and the brevity is the finding: it
echoes the client-supplied filename and calls copy() with a destination
taken from that same client-supplied filename. There is no session include,
no login check, no extension filter, no MIME check, no path restriction and
no storage directory of the product's own choosing. The web server
configuration recovered from the same disk image loads no authentication
module at all, because this product's architecture delegates authentication
to each PHP file individually, and upload.php is one of the files that
never asks. Three omissions stack into one chain, each independently
sufficient to make the write dangerous: missing authentication for a
critical function (CWE-306 primary), an upload accepted without type
restriction into an executable mapping (CWE-434 co-equal), and external
control of the destination file name or path (CWE-73 contributing).

The chain. An anonymous client on any network that can reach the management
interface posts a multipart body carrying a PHP payload whose disposition
filename is the destination of the write. copy() writes the file under the
attacker-chosen name into the served document root /NU20/web/, the HTTPS
listener of the recovered configuration binding :443 across addresses with
no restriction. One fetch of the written path then hands the file to the
product's own fastcgi mapping, and the chosen PHP executes in the product's
web service context. Two requests, no credential at any point, no memory
corruption, no deserialisation gadget, no default credential and no action
by any user of the product. The write and the execution are decoupled in
time, which makes the write primitive independently useful: served pages
can be replaced, configuration and application files inside the web root
can be overwritten, and a persistent implant can be dropped into a location
the product itself serves, surviving a service restart as an ordinary file
in the served tree until an operator finds it.

Everything in the chain is a shipped default, established from artifacts
rather than from lab state: the endpoint exists in the shipped web root
(squashfs extraction, byte-exact), the endpoint requires no authentication
(absent include plus absent server-layer gate, both artifacts), the
destination is client-controlled (the copy() second argument is the
multipart filename, from the endpoint source), the destination directory
is served and executable (document root and fastcgi mapping, both from the
recovered configuration), and the listener accepts connections from any
address.

The authentication model, named for what it is. The recovered lighttpd
configuration declares its module list explicitly and loads no
authentication module; a content search of the recovered configuration for
an authentication backend, an authentication module, a valid-user
requirement and an access-denial rule returns zero hits for all four
patterns. The gate, where it exists at all, is one include statement inside
each PHP file, so the product's authentication boundary is exactly as
strong as its most forgettable file, and upload.php is that file. The
boundary claim is deliberately conservative: this handler is established
as unauthenticated by the byte-exact source plus the absent server-layer
gate, and no claim is made about other handlers in the web root, which are
named in the advisory as an audit recommendation, not as findings.

Verification boundary, stated in full, because it defines what is and is not
being claimed. No physical Crystal VM was reachable during this study, so
the verification could not be a live drive against the product's own
listener. The static half is anchored in the appliance disk image: the
OVA's VMDK was converted to a raw image, the PHP web root was carved out of
its squashfs region (653 inodes, 575 files, including the byte-exact three-
line upload.php), and the server configuration was recovered from the same
disk and read in full. The dynamic half ran on a faithful replica: the
appliance's own extracted web root, all recovered files including the real
upload.php, served with the document-root behaviour and the
unauthenticated-execution semantics of the appliance's own extracted
configuration, on the loopback interface of an isolated research host.
Three independent runs uploaded the probe file without any credential,
confirmed the landing in the document root, and returned an execution
marker together with command output on one fetch; a no-upload negative
control produced no marker (and a fetch of never-uploaded names returned
404 with nothing); and an absolute-destination variant, writing to an
absolute path inside the served root, landed and executed identically, so
the write does not depend on a working-directory coincidence. The exact
working-directory resolution of a relative destination on a shipped
appliance is the one piece this work could not observe on physical hardware,
which is why the absolute-destination result exists and why the chain does
not rest on it.

On the executing identity, because it matters for what downstream readers
should and should not claim. The command output in the replica runs
identified the invoking account of the replica's PHP server process. That
measurement is a property of the replica environment and is reported as
such: it demonstrates that executed code inherits the identity of the PHP
service. The corresponding identity on a shipped appliance, the lighttpd
/ php-cgi service account of the VM, was not observed at runtime in this
work, and no superuser claim appears anywhere in the advisory. The
execution primitive, the score and the impact statements are written to be
true whichever account that turns out to be; a reader who sees a 9.8 vector
and starts writing "root on the appliance" is jumping past the published
evidence, and this disclosure says so plainly rather than benefiting from
the inflation.

Scoring. One score is published: 9.8 Critical,
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, re-derived rather than
inherited. The arithmetic is printed so any reader can reproduce it under
the CVSS 3.1 base algorithm and its round-up-to-the-tenth rule: ISS =
1 - ...