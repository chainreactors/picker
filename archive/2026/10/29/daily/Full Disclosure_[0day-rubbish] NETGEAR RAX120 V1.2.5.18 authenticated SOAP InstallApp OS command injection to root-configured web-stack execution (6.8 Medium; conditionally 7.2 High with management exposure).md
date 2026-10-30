---
title: [0day-rubbish] NETGEAR RAX120 V1.2.5.18 authenticated SOAP InstallApp OS command injection to root-configured web-stack execution (6.8 Medium; conditionally 7.2 High with management exposure)
url: https://seclists.org/fulldisclosure/2026/Oct/57
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:39.152440
---

# [0day-rubbish] NETGEAR RAX120 V1.2.5.18 authenticated SOAP InstallApp OS command injection to root-configured web-stack execution (6.8 Medium; conditionally 7.2 High with management exposure)

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#57)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#57)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] NETGEAR RAX120 V1.2.5.18 authenticated SOAP InstallApp OS command injection to root-configured web-stack execution (6.8 Medium; conditionally 7.2 High with management exposure)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:39:59 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in NETGEAR
RAX120 (Nighthawk AX12) firmware V1.2.5.18, the WiFi 6 consumer router from
NETGEAR (United States), built on the Qualcomm IPQ8074 platform. The
administrative web plane of this firmware generation is a lighttpd server
fronting the vendor's DNI-framework CGI handler /usr/sbin/net-cgi (an
aarch64, musl, stripped image; the handler binary measures 1,042,120 bytes
and its recorded image digest begins d7035dd3), and the SOAP control plane
dispatches every action through /soap/server_XMLresp.cgi. Among those
actions is the app-installation control InstallApp of the service
urn:NETGEAR-ROUTER:service:AppSystem:1, which requires the router
administrator's session.

Type and root cause. OS command injection (CWE-78 primary, with CWE-20
co-equal for the blocklist-style improper input validation, and CWE-426
recorded as contributing without raising any metric). The operation takes a
NewAppName argument and passes it through a blocklist validator whose
"apname" mode (the routine at fcn.000407d8 in the stripped image, mode
string at 0xc3058) rejects six characters chosen with shell injection in
mind: the at-sign, the backtick, the semicolon, the double quote, the
single quote and the backslash. That set covers the classic
statement-separator and quote-context breakouts. It does not reject the
dollar sign or either parenthesis, which are the entire grammar of command
substitution. The handler then embeds the validated name, unquoted, into two
working paths (/tmp/<name>_tmp and /sw-apps/<name>, both built by direct
snprintf interpolation) and then into three shell command lines:

    system("rm -rf /sw-apps/<name>/version.txt > /dev/console")
    system("rm -rf /sw-apps/<name> > /dev/console")
    popen("rm -rf /tmp/<name>_tmp; mkdir /tmp/<name>_tmp;
          tar -zxf /tmp/<tarball> -C /tmp/<name>_tmp", "r")

Each sink executes through /bin/sh -c, so a second parse happens inside a
shell the validator never modeled. A name of the shape x$(cmd) substitutes
attacker-chosen command text before the rm words ever run, and the shell's
parser walks the whole command line with a substitution pass before
executing any word of it, so the injected command fires whether or not the
surrounding rm errors out. An intermediate string processor in the handler
walk (recorded at fcn.00079060) rewrites carriage returns and line feeds to
spaces and performs no other transformation, so no downstream mitigation
exists: the dollar sign, pipe, ampersand and every other metacharacter pass
untouched. Two gates sit ahead of the validator, a 255-character length cap
on the name and a value gate on the companion NewUpdate element, and both
are compatible with the payload, which is under 30 characters.

Execution identity. system() and popen() children inherit the identity of
the web stack that calls them, and the research record identifies, from the
firmware image's own lighttpd configuration, the server's configured
runtime user as root, so command text supplied through this handler
inherits device-root authority by product configuration. The dynamic
verification measured exactly that identity in a sink-level replication:
markers carrying uid=0(root) gid=0(root) groups=0(root) from all three
vectors, and none from a benign control name.

Authentication, credited plainly. This is not an unauthenticated finding
and no unauthenticated variant of it is claimed. The gate is identified from
the artifacts as the administrative SOAP login bound to the requesting
station's MAC address, failing closed; the chain consumes a legitimate
administrator session and neither bypasses nor forges it. It is also not a
default-credential finding: the same request succeeds whatever the
administrator password is. No second web-account tier with reach into this
service exists in any artifact examined, which is what fixes Privileges
Required at High. The product gets the gate right and the argument
construction wrong; this is a CWE-78/CWE-20 defect, not CWE-306 and not
CWE-862.

Why this handler and not a hundred others. The DNI framework also contains
an exec helper (recorded at fcn.000779f0) that runs commands through
vfork() plus execve() with an argument vector, architecturally immune to
shell injection, and large parts of the firmware use it. A census of the
shell-mediated remainder classified on the order of 150+ system() sites,
almost all of them fixed string constants loaded by address arithmetic with
no substitution, and about 54 popen() sites. The app-installation handler
is the single family in the analysed image that interpolates an
attacker-controlled SOAP argument into a shell command line, so the defect
is one handler rather than a platform-wide sloppy pattern.

The sibling platform. The same root cause was confirmed on the NETGEAR
R7800 (Nighthawk X4S), firmware V1.0.2.68: a different SoC generation
(Broadcom BCM4709), a different instruction set (32-bit ARM), a different
handler binary (recorded digest beginning c5a9f2b3) and a different
validator function whose reject set is only the double quote, the single
quote and the backslash, which is strictly more permissive than the main
model's six. The identical x$(cmd) payload passed that validator and
executed through the same handler family in that platform's own sink-level
replication, with three root markers of its own and a clean control. The
merge is argued at the level of root cause, not build identity, and the
platform differences are stated rather than smoothed over. Other models
shipping this framework's app-system code were not audited, and the vendor's
older R6700/R7000/R8000 generation runs a different self-built httpd lineage
that does not contain this handler, so no claim is made about it.

Verification boundary, stated in full, because it defines what is and is not
being claimed. No physical router was driven during verification and no
live SOAP request was fired at device hardware, at any point, in any phase
of this work. The request path, the session gate and the parameter
extraction are established at disassembly level from the shipped image. The
injection behaviour at the sink is established by a sink-level replication:
on an isolated cloud-hosted sandbox, a natively compiled C program
re-implemented the disassembled validator logic, the CRLF-normalising string
processor and all three command constructions, run with the root privilege
model the image's lighttpd configuration records for the web stack. Three
vectors, one per sink, each carrying x$(id>/tmp/<marker>) through the
replicated validator and construction, each produced a marker containing
uid=0(root) gid=0(root) groups=0(root); a benign control name traversing
the identical code path produced none. The control is the load-bearing
negative: it makes the marker creation attributable to the substitution
content alone, not to the surrounding cons...