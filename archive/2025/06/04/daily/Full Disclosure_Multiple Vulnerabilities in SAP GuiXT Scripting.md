---
title: Multiple Vulnerabilities in SAP GuiXT Scripting
url: https://seclists.org/fulldisclosure/2025/Jun/3
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:34.197051
---

# Multiple Vulnerabilities in SAP GuiXT Scripting

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# Multiple Vulnerabilities in SAP GuiXT Scripting

---

*From*: Michał Majchrowicz via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 3 Jun 2025 10:30:28 +0200

---

```
Security Advisory

Vulnerabilities reported to vendor: March 13, 2025
Vendor requested additional information: March 20, 2025
Additional information provided to vendor: March 22, 2025
Vendor confirmed the reported issues but rejected them: March 31, 2025
Additional information provided to vendor: May 6, 2025
Vendor confirmed the reported issues but rejected them: May 15, 2025
Vendor closed the tickets for all reported issues: May 16, 2025
Public disclosure: June 3, 2025

Summary:

Multiple vulnerabilities have been discovered in SAP GuiXT scripting, which
could allow an attacker to perform remote code execution, steal NTLM
hashes, conduct Client-side Request Forgery attacks, and launch
Denial-of-Service (DoS) attacks. These vulnerabilities arise from insecure
design principles and insufficient security checks within the SAP GuiXT
application's handling of scripts.

Official documentation describes (spelling original) how network shares can
configured for GuiXT scripting:

“Storing scripts on a network file share is used by developers, testing
teams and end-users. This method allows for the easy set up and use of
scripts while at the same time enabling centralized management. Access to
the scripts can be managed by using network policies and the network
traffic can be reduced by using GuiXT’s File Replication option.
However, using a network file share also has potential problems. The main
one is that using a network fiel share introduces another dependency into
the GuiXT environment. Additional replication must also be set up if
different servers are being used across the WAN. And all users must have
the requisite privileges set up for them to access the scripts.
Example of a network file share in the GuiXT.ini file:

Directory1 \\Demoserver\\GuiXT\\scripts”

Security issues arising from such configuration are not documented.
Furthermore, our tests indicate that these scripts can even bypass numerous
antivirus software solutions.

Affected Software:
SAP GuiXT scripting in SAP GUI FrontEnd
Vulnerabilities:
1. Insecure Design in GuiXT Scripting
Description: The SAP GuiXT application allows loading scripts from remote
locations specified in the configuration file (`guixt.ini`) or the
registry. This enables an attacker to trick a user into pointing the
application to a malicious server, leading to the automatic loading and
execution of attacker-controlled scripts upon login or transaction opening.
The scripts can be obfuscated to bypass antivirus solutions and execute
arbitrary commands without the user's knowledge. Additionally, NTLM hashes
are sent to the remote location with each script load attempt, allowing for
credential theft.
Impact: Remote Code Execution, NTLM Hash Theft, Backdoor Installation
2. SAP GUI NTLM Hash Hijacking via UNC Paths in GuiXT Scripts
Description: The `Include` directive in GuiXT scripts allows the use of UNC
paths. An attacker with write access to a shared directory can inject a
malicious script that uses an `Include` directive to point to an
attacker-controlled UNC path, capturing the user's NTLM hash when the
associated transaction is opened.
Impact: NTLM Hash Theft, Credential Compromise
3. Client-Side Request Forgery
Description: The `Include` directive supports various protocols (SMB, FTP,
HTTP). An attacker can exploit this to perform requests to internal or
external servers by including a malicious HTTP URL in a GuiXT script. This
can lead to Client-Side Request Forgery attacks where requests are sent
from the victim's machine to other services.
Impact: Client-Side Request Forgery, Data Exfiltration
4. Denial of Service (DoS)
Description: The SAP GUI application does not validate the size of
downloaded scripts and performs downloads in the main thread. An attacker
can provide a very large script file via a remote location, causing the
application to become unresponsive and unusable until the download
completes.
Impact: Denial of Service, Application Unavailability

Possible Vendor Mitigations:
Restrict Script Locations: Ensure that only trusted directories are
specified for loading GuiXT scripts in the `guixt.ini` file and registry.
Input Validation: Implement strict validation for script paths to prevent
loading from untrusted or remote locations.
Disable UNC Paths: If possible, disable the use of UNC paths in the
`Include` directive.
Protocol Restrictions: Limit the protocols allowed in the `Include`
directive to only necessary protocols.
File Size Validation: Implement file size checks for downloaded scripts to
prevent large file downloads that cause DoS.
Thread Management: Perform script downloads in a background thread to avoid
blocking the main application thread.
User Education: Educate users about the risks of changing script locations
in SAP GUI settings and opening `.reg` files from untrusted sources.
Official Documentation Update: Update official documentation to explicitly
warn users about the security risks associated with changing script
locations in SAP GUI settings and opening `.reg` files from untrusted
sources.
Workaround:
Avoid using remote script locations for SAP GuiXT scripting. Store scripts
locally in secure directories.
Be cautious when opening `.reg` files or clicking links that could change
SAP GUI settings.
Issues discovered by:

Michał Majchrowicz, Marcin Wyczechowski, and Paweł Zdunek - members of the
AFINE Team.

Disclaimer:

This advisory is provided for informational purposes only. It is the
responsibility of the users and administrators to take appropriate measures
to secure their systems.

References:
https://afine.com/research/
https://afine.com/blog/
https://www.guixt.com/guixt/guixt_installation
SAP Consulting Note 3602957

—
Michał Majchrowicz / Offensive Security Engineer / PhD eWPTX
PGP: D52A 5289 8256 006D 5E05 BAC6 79EA 0072 F4E1 9D57

AFINE sp. z o.o.
Al. Jerozolimskie 146C, 02-305 Warszawa
https://www.afine.com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **Multiple Vulnerabilities in SAP GuiXT Scripting** *Michał Majchrowicz via Fulldisclosure (Jun 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap...