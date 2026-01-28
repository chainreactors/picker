---
title: SEC Consult SA-20260126-1 :: Multiple Critical Vulnerabilities in dormakaba Access Manager
url: https://seclists.org/fulldisclosure/2026/Jan/23
source: Full Disclosure
date: 2026-01-27
fetch_date: 2026-01-28T03:35:24.789968
---

# SEC Consult SA-20260126-1 :: Multiple Critical Vulnerabilities in dormakaba Access Manager

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
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260126-1 :: Multiple Critical Vulnerabilities in dormakaba Access Manager

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Jan 2026 10:21:48 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260126-1 >
=======================================================================
              title: Multiple Critical Vulnerabilities
            product: dormakaba Access Manager
 vulnerable version: Multiple firmware and hardware revisions (details below)
      fixed version: Multiple firmware and hardware revisions (details below)
         CVE number: CVE-2025-59097, CVE-2025-59098, CVE-2025-59099,
                     CVE-2025-59100, CVE-2025-59101, CVE-2025-59102,
                     CVE-2025-59103, CVE-2025-59104, CVE-2025-59105,
                     CVE-2025-59106, CVE-2025-59107, CVE-2025-59108
             impact: critical
           homepage:https://www.dormakaba.com/
              found: 2024-03-18
                 by: Clemens Stockenreitner (Office Vienna)
                     Werner Schober (Office Vienna)
                     Supported by the HW Lab Vienna
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"The Kaba exos 9300 basic system is the cornerstone of your access
management solution. Use it to resolves all your basic employees,
system, user and peripheral management tasks and initiate targeted
security measures as required. [...] "

Source:https://www.dormakaba.com/gb-en/offering/products/electronic-access-data/corporate-access-control-solutions/dormakaba-exos-9300-base-system--ka_500000

Business recommendation:
------------------------
The vendor provides multiple patches which should be installed immediately.
More details can be found at the following locations:
- Solution at the end of this advisory
- SEC Consult blog post:https://r.sec-consult.com/dormakaba
- Vendor website / security page:https://www.dormakabagroup.com/en/security-advisories
- Your dormakaba partner

Tested Architecture Overview
-----------------------------------
The tested system is the enterprise grade physical access system from
dormakaba. The tested system consists of the following components:

------------------------------
dormakaba exos 9300
------------------------------
Exos 9300 is a piece of software based on C# running on a central Windows server with
an MSSQL, or Oracle database as central storage.
Exos consists of multiple modules (e.g. basis, employee management, key depot, access,
visitor management, 3rd party management). Exos is used to centrally manage users,
keys, cards as well as the configuration of the access manager. Devices in the
exos environment are addressed using a special addressing scheme. The address scheme
described in the following table is going to be important.

┌────────────────────┬───────────────────────────┬───────────────┬───────────────────────────────────────────┬───────────────────────────┬───────────────────┐
│         I          │            01             │      00       │                    01                     │
  00             │        00         │
├────────────────────┼───────────────────────────┼───────────────┼───────────────────────────────────────────┼───────────────────────────┼───────────────────┤
│ Port Type          │ Communication Hub Address │ Port Address  │ Access Hub Address                        │ 00 =
Door Manager         │ Datapoint Address │
│ I = Access Manager │ Values: 01-99             │ Values: 00-99 │ Values: 00-99                             │ 01 =
Access Point         │ Values: 00-20     │
│ B = Serial         │                           │               │ Fixed to 01 for Access Hubs with Ethernet │ 02 =
Turnstile            │                   │
│ C = Modem          │                           │               │                                           │ 03 = IO
Controller        │                   │
│ E = Ethernet       │                           │               │                                           │ Fixed to
00 in most cases │                   │
│ R = remote         │                           │               │                                           │
                 │                   │
└────────────────────┴───────────────────────────┴───────────────┴───────────────────────────────────────────┴───────────────────────────┴───────────────────┘

------------------------------
dormakaba Access Manager
------------------------------
The access manager is a component that is configured via exos. The configuration
between exos and access manager is exchanged via a SOAP interface. Per default
the data exchange is unencrypted. Encryption is only available starting with
access manager hardware release K7.
The access manager is a custom piece of hardware with multiple inputs and outputs.
The device offers the following interfaces:
- Digital Inputs
- 3x DC Output Relays
- 2x RS-232
- 1x RS-485 (Used to connect to access manager extension systems e.g. Kaba 9125)
- 1x RJ45
- 1x Micro USB
- 2x Coax (Used to connect registration units e.g. 9001, 9002)

The tested hardware was an access manager 9200-k5 running Windows CE embedded,
and an access manager 9200-k7 running Linux.

------------------------------
dormakaba Registration Unit
------------------------------
dormakaba registration units can be either a Legic/Mifare card reader,
or a PIN pad used to enter a PIN to deactivate alarming systems, or as
an additional authentication.

------------------------------
Electric lock
------------------------------
The lock used for the tested setup is an Assa Abloy/effeff Profix 118. The lock
is simply controlled via a relay contact connected to the Access Manager. As
soon as a user successfully authenticates with a registration unit,
the relay connected to the lock is switched and the door opens.

The system is depicted in the following diagram.

          ┌─────────┐
          │         │
          │exos 9300│              ┌──────────┐  ┌──────────┐
          │         │              │ Reg Unit │  │ Pin Pad  │
          └────┬────┘              │   ┌──┐   │  │  x x x   │
               │                   │   │┼┼│   │  │  x x x   │
Ethernet──────►│                   │   └──┘   │  │  x x x   │
               │                   │   9001   │  │   9002   │
          ┌────┴────┐              └─────┬────┘  └─────┬────┘
          │ Access  │                    │             │
          │ Manager ├────────────────────┴─────────────┘
          │  9200   │        ▲
          └────┬────┘        │
               │           Coax
               │
  DC Relay───► │
               │
            ┌──┴──┐
            │     │
            │     │
            │     │
            │    ─┤◄──────Electric Lock
            │     │
            │     │
            └─────┘

Vulnerability overview/description:
-----------------------------------
1) Unauthenticated SOAP API (CVE-2025-59097)
The ...