---
title: SEC Consult SA-20250521-0 :: Multiple Vulnerabilities in eCharge Hardy Barth cPH2 and cPP2 charging stations
url: https://seclists.org/fulldisclosure/2025/May/23
source: Full Disclosure
date: 2025-05-29
fetch_date: 2025-10-06T22:37:02.885952
---

# SEC Consult SA-20250521-0 :: Multiple Vulnerabilities in eCharge Hardy Barth cPH2 and cPP2 charging stations

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250521-0 :: Multiple Vulnerabilities in eCharge Hardy Barth cPH2 and cPP2 charging stations

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 May 2025 12:23:08 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250521-0 >
=======================================================================
              title: Multiple Vulnerabilities
            product: eCharge Hardy Barth cPH2 and cPP2 charging stations
 vulnerable version: 2.2.0
      fixed version: Not available
         CVE number: CVE-2025-27803, CVE-2025-27804, CVE-2025-48413,
                     CVE-2025-48414, CVE-2025-48415, CVE-2025-48416,
                     CVE-2025-48417
             impact: critical
           homepage: https://www.echarge.de/
              found: 2023-11-13 (first findings)
                 by: Stefan Viehböck (Office Linz)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Parallel to the master school, the young entrepreneur founded the sideline
business "Elektrohandel Hardy Barth", which was already changed into a
full-time business with the name "EDV- und Elektrotechnik Hardy Barth"
three years later.
Today, we successfully manage our company with over 80 employees, which
currently specializes in 5 specialist areas on the market."

Source: https://www.echarge.de/

Business recommendation:
------------------------
The products are affected by serious vulnerabilities exploitable via both
physical access and unauthenticated network access, posing serious risks that
can result in system compromise, data breaches, and operational disruption in
EV charging infrastructures.

SEC Consult recommends charge point operators (CPOs) to take active measures
to minimize risk until all identified vulnerabilities have been fully
resolved and a comprehensive security review is conducted by independent
security professionals. These measures include physically securing all
charging stations, implementing video surveillance to deter and detect
unauthorized access, isolating and segmenting the devices from other critical
network infrastructure, enforcing strict firewalling rules, and disabling
remote access interfaces unless absolutely necessary. Where remote access is
required, strong authentication and VPNs should be used. Continuous
monitoring of logs and network activity is also strongly advised.

Note: SEC Consult did not analyze OCPP (Open Charge Point Protocol) as an
attack vector in the context of these vulnerabilities. CPOs should consider
this in their risk assessment and security architecture.

Despite being notified via a responsible disclosure, the vendor did not
provide any fixes over a period of 160 days. We decided to publish this
vulnerability now to enable mitigations against attacks.

Vulnerability overview/description:
-----------------------------------
1) Missing Authentication (CVE-2025-27803)
The device does not implement any authentication for the web interface or the
MQTT server. An attacker who has network access to the device immediately gets
administrative access to the device and can perform arbitrary administrative
actions and reconfigure the device or potentially gain access to sensitive data.

2) Multiple OS Command Injection Vulnerabilities (CVE-2025-27804)
Several OS command injection vulnerabilities exist in the device firmware
in the /var/salia/mqtt.php script. By publishing a specially crafted message to a
certain MQTT topic arbitrary OS commands can be executed with root permissions.

3) OS Backdoor User "root" (CVE-2025-48413)
The `/etc/passwd` and `/etc/shadow` files reveal hard-coded password
hashes for the "root" user. The credentials are shipped with the update
files. There is no option for deleting or changing their passwords for an enduser.

An attacker can use the credentials to log into the device. Authentication can
be performed via the SSH backdoor (see issue #6) or likely via physical access
(UART shell).

4) Backdoor Functionality via Web Interface (CVE-2025-48414)
There are several scripts in the web interface that are accessible via undocumented
hard-coded credentials. The scripts provide access to additional administrative/debug
functionality and are likely intended for debugging during development. The functionality
was not analyzed in detail, but of course it provides additional attack surface.

5) Backdoor Functionality via USB Drive (CVE-2025-48415)
A USB backdoor feature can be triggered by attaching a USB drive that contains
specially crafted "salia.ini" files. The .ini file can contain several "commands"
that could be exploited by an attacker to export or modify the device configuration,
enable an SSH backdoor (issue #6) or perform other administrative actions. Ultimately,
this backdoor also allows arbitrary execution of OS commands.

6) Backdoor Functionality via SSH (CVE-2025-48416)
An OpenSSH daemon listens on TCP port 22. There is a hard-coded entry in the
"/etc/shadow" file in the firmware image for the "root" user (see issue #3).
However, in the default SSH configuration the "PermitRootLogin" is disabled, preventing
the root user from logging in via SSH. This configuration can be bypassed/changed
by an attacker through multiple paths.

7) Hard-Coded Certificate and Private Key for HTTPS Web Interface (CVE-2025-48417)
The certificate and private key used for providing transport layer security for
connections to the web interface (TCP port 443) is hard-coded in the firmware and are
shipped with the update files. An attacker can use the private key to perform
man-in-the-middle attacks against users of the admin interface. The files are
located in /etc/ssl (e.g. salia.local.crt, salia.local.key and salia.local.pem)

There is no option to upload/configure custom TLS certificates.

Proof of concept:
-----------------
The proof of concepts have been removed as there are no fixes available.

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test as well as the publication of this advisory:
* eCharge Hardy Barth cPH2 and cPP2 Firmware Version 2.2.0

Vendor contact timeline:
------------------------
2023-11 and 2023-12: First findings discovered and reported to mutual customer.
2024-11-26: Contacting vendor via multiple mailboxes and various other
            personal vendor email addresses.
2024-11-27: Direct contact answers to submit our advisory, they are already
            working on other identified security issues for release 2.3.0.
2024-12-02: Sending security advisory to vendor.
2024-12-16: Asking for a status update.
2024-12-16: Vendor is occupied with other internal tasks and does not
            have time to take a look at our advisory before some time in
            the first half of Q1/2025.
2025-01-29: Vendor informs us in a detailed response that their analysis is complete
            and issu...