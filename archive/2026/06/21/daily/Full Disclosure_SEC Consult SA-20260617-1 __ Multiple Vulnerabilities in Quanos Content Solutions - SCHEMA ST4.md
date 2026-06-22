---
title: SEC Consult SA-20260617-1 :: Multiple Vulnerabilities in Quanos Content Solutions - SCHEMA ST4
url: https://seclists.org/fulldisclosure/2026/Jun/20
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:00.547189
---

# SEC Consult SA-20260617-1 :: Multiple Vulnerabilities in Quanos Content Solutions - SCHEMA ST4

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

# SEC Consult SA-20260617-1 :: Multiple Vulnerabilities in Quanos Content Solutions - SCHEMA ST4

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 17 Jun 2026 11:31:26 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260617-1 >
=======================================================================
              title: Multiple Vulnerabilities
            product: Quanos Content Solutions - SCHEMA ST4
 vulnerable version: All versions of SCHEMA ST4 on-premises
      fixed version: Not applicable, see workaround section for mitigation.
         CVE number: CVE-2026-11857, CVE-2026-11858
             impact: high
           homepage:https://quanos.com/
              found: 2025-12-19
                 by: J. Kruchem (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"SCHEMA ST4 is a component content management system for the professional
creation of technical documentation. SCHEMA ST4 is one of the most widely
used software solutions of its type and makes the entire creation process
easier and more efficient, saving costs in many areas."

Source:https://quanos.com/en/products/schema-st4/

Business recommendation:
------------------------
The vendor does not provide a patch but a workaround which requires
their customers to disable the affected "Client Update Service". Updating
the client is then only possible manually with a privileged user account.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) .NET Remoting Local Privilege Escalation Vulnerability (CVE-2026-11857)
A local privilege escalation vulnerability exists in SCHEMA ST4 due to insecure
deserialization in the .NET Remoting service.

The service is configured with TypeFilterLevel.Full and bound to local interfaces
only (named pipes), allowing a local authenticated attacker to send specially crafted
objects. This leads to arbitrary code execution in the context of the update process
with the highest SYSTEM rights. Local host access with an authenticated user session
is required for successful exploitation. Network-only exploitation is not possible.

2) Arbitrary File Overwrite Vulnerability (CVE-2026-11858)
The SCHEMA ST4 Update Service acts as a privileged helper component running as
NT Authority\SYSTEM to perform file operations requiring elevated rights.

However, it exposes a .NET Remoting interface over a Named Pipe without sufficient
access controls or authentication. This allows any local low-privileged user to
connect and invoke methods like Update(), resulting in arbitrary file
write/delete operations with SYSTEM privileges. This ultimately leads to local
privilege escalation.

Proof of concept:
-----------------
The following steps can be taken in order to exploit the identified security issue
in the updater service.

1) .NET Remoting Local Privilege Escalation Vulnerability (CVE-2026-11857)
1.1) Connect to Name Pipe
Invoking NamedPipe.ConnectToPipe("ST4Updater2") and sending pipe.Write("init")
returns a port which is used for .NET Remoting. Only local exploitation is
possible.

1.2) Send .NET Remoting payload
Use the ExploitRemotingService by James Forshaw (https://github.com/tyranid/ExploitRemotingService)
to achieve arbitrary code execution.

2) Arbitrary File Overwrite Vulnerability (CVE-2026-11858)
2.1) Connect to Named Pipe
Invoking NamedPipe.ConnectToPipe("ST4Updater2") and sending pipe.Write("init")
returns a port which is used for .NET Remoting.

2.2) Get .NET Remoting Object
Get remote object tcp://127.0.0.1:<port>/UpdateProcessCore

2.3) Create Manifest
An essential part of the exploit is creating a Manifest.rdf containing e.g.
Directory "." and file exploit.exe:<something like md5> (is not checked).
The Manifest needs to be zlib-compressed and be served via HTTP.

2.4) Create Payload
Create a zlib-compressed file (e.g. .exe, .msi, .dll, ...) name it to
your choosing like <e.g. md5> and put it into the HTTP root (like
the Manifest).

2.5) Invoke Update() from remote .NET object
Use the object from 2.2) and provide proper arguments.
Use "Newer" for writing files as system (same name will be deleted beforehands)
Use "Remove" for deleting files and/or directories (depending on Manifest)

Example:
[ Proof of Concept example removed ]

2.6) Privilege Escalation
To achieve privilege escalation e.g. write a custom HID.dll using the exploit to
C:\Program Files\Common Files\microsoft shared\ink\ then open the Microsoft
on-screen keyboard in a security context (e.g. CTRL + ALT + ENTF). The custom
commands are executed with SYSTEM privileges.

[ ST4Updater.png ]
Figure 1: Proof of concept

Vulnerable / tested versions:
-----------------------------
The following version has been tested:
* 12.0.4.0 ST4 2022 SP4 (1d4a0bde) ??? SCHEMA ST4 12.4 build 2023.02.21-1d4a0bde

According to the vendor, all versions of SCHEMA ST4 on-premises are affected.
The Cloud/SaaS deployments of SCHEMA ST4 are not affected. The Client Update
Service has been removed in the cloud architecture according to the vendor.

Vendor contact timeline:
------------------------
2025-12-19: Contacting vendor throughinfo () quanos com; no response
2026-01-13: Contacting CISO through LinkedIn. Response after 1 Minute (at 7 pm).
2026-01-14: Sending more details via email tosecurity () quanos com;
            Vendor answers that they will analyze our information and will get
            back to us.
            Asking the vendor how we should submit our security advisory.
2026-01-22: Vendor responds that the architecture of ST4 is by design and only
            exploitable within the on premises version of ST4 (not cloud/SaaS).
            Provides a workaround to disable the client update service.
2026-01-23: Updating our advisory regarding workaround, recommending to patch
            the issue, as also .NET remoting can be exploited. Asking whether
            the on premises version is EOL.
2026-01-28: Vendor responds to clarify our questions internally.
2026-02-09: Asking for a status update.
2026-02-10: Vendor is still waiting for an internal response.
2026-03-05: Asking for a status update.
2026-03-10: Vendor is still in internal clarification process.
2026-03-20: Vendor provides detailed explanation regarding "Client Update "Service",
            which already got removed in the Cloud/SaaS solution, on-premises exploitation
            is impossible in properly managed environments according to the vendor.
            As a workaround, the Update Service should be disabled. The .NET Remoting
            part only communicates in a closed VPC network within the Cloud solution.
            An attacker already needs LAN access for the on-premises version and exploitation
            is therefore limited ...