---
title: SEC Consult SA-20250429-0 :: Multiple Vulnerabilities in HP Wolf Security Controller and more
url: https://seclists.org/fulldisclosure/2025/May/18
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:41.099232
---

# SEC Consult SA-20250429-0 :: Multiple Vulnerabilities in HP Wolf Security Controller and more

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250429-0 :: Multiple Vulnerabilities in HP Wolf Security Controller and more

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 8 May 2025 08:52:35 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < publishing date 20250429-0 >
Combined Security Advisory for Sure Access Enterprise and Sure Click Enterprise
=======================================================================
              title: Multiple Vulnerabilities
            product: HP Wolf Security Controller / HP Sure Access Enterprise /
                     HP Sure Click Enterprise
 vulnerable version: HP Wolf Security Controller 4.3.127.238 & 4.4.155.291,
                     HP Wolf Sure Click Enterprise Client Version 4.3.11.45 with
                     Extensionpack Sure Access Enterprise 8.0.125,
                     HP Wolf Sure Click 4.4.3.274
      fixed version: TODO
         CVE number: TODO
             impact: High
           homepage: https://www.hp.com/us-en/security/enterprise-pc-security.html
              found: 2022-09-15 (Sure Access) & 2023-08-18 (Sure Click)
                 by: Daniel Hirschberger (Office Bochum)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"HP Sure Access Enterprise uses hardware-enforced virtualization-based security
to isolate critical applications running on Microsoft Windows clients. The
zero-trust solution is deployed on the user’s PC, beneath the operating system
(OS) layer, where it creates a hardware-protected virtual machine (VM) that is
completely isolated from the Windows OS. Through this innovative approach, the
solution secures a number of key assets, including memory and CPU state, disk
structures, keyboard input, display outputs, and network traffic.
Even if a user’s endpoint is compromised, it won’t pose any risk to the remote
application and the sensitive data it contains, allowing users to work securely
on multiple remote Privileged Access Workstations (PAWs) from a single device.
The user can only access the application through the hardware-protected VM,
which remains isolated from the Windows OS—and any malware that might attack it."

Source: https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA7-6965ENW

"HP Sure Click Enterprise stops attacks and protects your endpoints by creating
micro–virtual machines (micro-VMs) that secure end-user tasks, from surfing the
web to opening email and downloading attachments. High-risk tasks are completely
isolated inside the micro-VM. When a task is closed, the micro-VM—and any threat
it contained—is disposed of without any breach.  Sure Click Enterprise is
powered by hardware-enforced isolation technology that uses virtualization-based
security on the host to contain threats inside individual, disposable micro-
VMs. This approach dramatically decreases attack surfaces, while preserving
familiar user workflows."

Source: https://h20195.www2.hp.com/v2/getpdf.aspx/4AA7-6963ENW.pdf

Business recommendation:
------------------------
The vendor does not provide a patch because according to HP, the issues are
configuration-related or limitations or out of scope of the products themselves.
See statements below.

Customers must check if they are enforcing authentication with TLS Client
Certificates for Sure Access, Sure Click and the HP Wolf Security Controller.
This is the intended and recommended configuration according to HP. Links to
their configuration guidelines can be found at the bottom in the "Solution"
section

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

General information:
--------------------
SEC Consult conducted penetration tests on Sure Access in 2022 and on Sure Click
in 2023 and established a contact with HP afterwards. After several rounds of
emails and meetings with the product development team, the scope and limitations
of Sure Access and Sure Click were made clear. This advisory combines the result
of those penetration tests.

In summary, most of the issues we identified as a vulnerability are not in
the scope or attacker model of Sure Access/Sure Click. Several issues can be
prevented by correctly configuring both products, e.g., enforcing authentication
with TLS Client Certificates, according to HP.

The identified issues will be categorized into the affected product, followed by
the classification if it is a real vulnerability or a misconfiguration.

Statement from HP
-----------------------------------

HP sent us a statement which can be summarized as follows:

Sure Click Enterprise considers the following out-of-scope:
- Malicious users
- Local administrators
- Malicious servers or infrastructure/server admins

Sure Access Enterprise considers the following out-of-scope:
- Malicious users with direct access to Sure Access Enterprise Apps and
  credentials to use them
- Malicious infrastructure/server admins
- Service availability on the endpoint
- Protection of resources which are not explicitly enrolled into Sure Access
  Enterprise

Vulnerability overview/description:
-----------------------------------
1) HP Wolf Security Controller

a) Misconfiguration
Missing Authentication and Authorization on the deviceAPI

Clients routinely contact the Security Controller server to refresh their
policies and send device logs to it.
Unfortunately, calling functions on the deviceAPI does neither require
authentication nor authorization.
Thus, clients can perform arbitrary deviceAPI actions which leads to further
vulnerabilities.

b) Vulnerability: Missing CSRF Protection
The deviceAPI does not implement CSRF protection. This means that an
attacker who knows the internal IP of the Security Controller can prepare a
malicious link and trick users in the internal network to call arbitrary
deviceAPI functions.

c) Misconfiguration: Unauthorized Access to other Applications
The Security Controller allows defining 'Applications' and assigning them to
individual devices or device groups. These applications are mostly HTTP(S), SSH
or RDP connections to specific hosts. When such an application is opened, a new
micro-VM is spawned, the requested connection is established in the micro-VM and
the resulting UI is rendered in a separate window.
Because the deviceAPI does neither require authentication nor authorization, an
attacker can fetch any application from the server and subsequently access it.

d) Vulnerability: Missing Anti-Automation Protection
Because of missing anti-automation measures an attacker can call the /register/
endpoint of the deviceAPI repeatedly and burn through the available licenses.
This is not an issue in itself because the product still works even if all
licenses are used up.
Nonetheless, in combination with the next vulnerability an attacker is able
to generate a considerable amount of bogus logs in a short time...