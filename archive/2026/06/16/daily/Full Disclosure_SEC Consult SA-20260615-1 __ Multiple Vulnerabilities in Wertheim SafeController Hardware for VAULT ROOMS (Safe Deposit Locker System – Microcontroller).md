---
title: SEC Consult SA-20260615-1 :: Multiple Vulnerabilities in Wertheim SafeController Hardware for VAULT ROOMS (Safe Deposit Locker System – Microcontroller)
url: https://seclists.org/fulldisclosure/2026/Jun/9
source: Full Disclosure
date: 2026-06-16
fetch_date: 2026-06-17T07:04:07.242689
---

# SEC Consult SA-20260615-1 :: Multiple Vulnerabilities in Wertheim SafeController Hardware for VAULT ROOMS (Safe Deposit Locker System – Microcontroller)

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260615-1 :: Multiple Vulnerabilities in Wertheim SafeController Hardware for VAULT ROOMS (Safe Deposit Locker System – Microcontroller)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Jun 2026 12:07:16 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260615-1 >
=======================================================================
              title: Multiple Vulnerabilities
            product: Wertheim SafeController Hardware for VAULT ROOMS
                     (Safe Deposit Locker System – Microcontroller)
 vulnerable version: Controller 65000 - AssemblyVersion 6.11.8130.22319
                     Controller 5400 - AssemblyVersion 6.11.8130.22320
      fixed version: No fix for issue 1 & 2,
                     No information provided for issue 3
         CVE number: CVE-2026-34021, CVE-2026-34022
             impact: High
           homepage:https://wertheim-safes.com/safe-deposit-boxes/
              found: 2023-04-03
                 by: Gorazd Jank (Office Vienna)
                     Christian Hager (Office Vienna)
                     Philipp Espernberger (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"On September 1, 1852, Franz Wertheim and 85 employees began to build "fireproof safes".
Then as now, Wertheim has been successfully involved in production of safes and banking
facilities, nationally and internationally. To secure the market position and develop
new business areas, Wertheim has continuously adapted its product range over the years
as well as expanded its assortment of offerings. Today, the Wertheim Group of companies
also produces bank and object furnishings in our own joinery in Uttendorf, and
Commissioned Work has developed into an essential business area for the group. The
diversity of state-of-the-art technologies characterizes the flexibility and technical
know-how of this division."

Source:https://wertheim.at/en/company/ (2023)

Business recommendation:
------------------------
The affected HW controller 5400 is marked as end-of-life (EOL), hence there won't
be any patches provided by the vendor. The encryption algorithm for Controller 65000
cannot be improved/fixed by the vendor as well because of missing hardware support.

It is recommended to assess the business risk and switch to a supported version in case
any EOL products are used.

Vulnerability overview/description:
-----------------------------------
1) Lack of Cryptographic Protection on SafeController 5400 (CVE-2026-34021)
The serial communication between the micro controller and the server is not
cryptographically protected. An attacker who has already compromised the server or
is able to capture the traffic between the server and the micro controller is able
to sniff all RS-485 messages and use the sniffed message for replay attacks.
This weakness can be used to spoof the message "quit alarm" to continuously deactivate
the safe alarm.

2) Insufficient Transport Layer Encryption on SafeController 65000 (CVE-2026-34022)
The SafeController Family 65000 is secured with weak and custom cryptographic
algorithms with hard-coded keys. An attacker who is in an adversary-in-the-middle
position can read and decrypt the data traffic.

3) Undisclosed Vulnerability in the binary SafeController
This vulnerability was identified during a reassessment commissioned by Wertheim.
Detailed disclosure is withheld as the finding is subject to the vendor's ownership
and disclosure authority. Affected parties are advised to contact the vendor
directly for further information.

Proof of concept:
-----------------
1) Lack of Cryptographic Protection on SafeController 5400 (CVE-2026-34021)
```
Proof of concept removed because no patch will be provided
```

2) Insufficient Transport Layer Encryption on SafeController 65000 (CVE-2026-34022)
```
Proof of concept removed because no patch will be provided
```

3) Undisclosed Vulnerability in the binary SafeController
```
Proof of concept removed because of undisclosed vulnerability
```

Vulnerable / tested versions:
-----------------------------
The following versions/devices have been tested which were the latest version available
at the time of the test:
* Wertheim GmbH Safe Service for controller 65000 in AssemblyVersion 6.11.8130.22319
* Wertheim GmbH Safe Service for controller 5400 in AssemblyVersion 6.11.8130.22320

Vendor contact timeline:
------------------------
2023-06-20: Initial meeting between SEC Consult and Wertheim to discuss
            identified vulnerabilities
2023-07-23: Contacting vendor through direct email addresses received
            in the meetings, asking for encryption keys.
2023-07-31: Vendor response to send advisory unencrypted and apologizing for delays
            due to vacation time.
2023-08-07: Sending two advisories (split between HW devices and SW issues)
            to vendor, zipped with password.
2023-08-07: Vendor response: project start in September, implementation
            process planned to be finished early December. Estimation that
            rollout of patches takes another quarter (end of Q1/24).
2023-08-08: Meeting to discuss further steps.
2023-10-13: Asking for status update via email; No response received.
2023-11-30: Asking for status update via email - as no answer has yet
            been received.
2023-11-30: Vendor responds to our request with following information:
            - Currently on time - Release plan Q1/2024
            - A meeting between SEC Consult and Wertheim should take place in
              Q1 to discuss further steps, including the recheck of
              vulnerabilities.
            - Updates are provided in different ways:
              1. Customers with a support package receive the releases
                 immediately
              2. Customers without a support package receive an offer
                 to upgrade.
2024-02-16: Asking for status update and proposed dates for the planned
            meeting in Q1/2024 via email
2024-02-16: Vendor responds with following information:
            - A recheck was arranged with SEC Consult to check the mitigations
            - Recheck date planned for March 2024.
2024-02-22: Vendor has submitted an internal project plan with information
            and the status of ongoing remedial measures.
2024-02-26: Meeting with the vendor to discuss next steps and recheck date:
            - After the new review, the remaining weaknesses will be fixed and
            everything will be rolled out to customers by September 2024 at the
            latest.
2024-03-05: Recheck date finalized for end of March.
2024-03-29: Recheck conducted with the following results:
            - Vulnerability 1: Not Fixed - No patch will be provided because
              the controller is marked as End-of-Life (EOL)
            - Vulnerability 2: Not Fixed - The algorithm was not changed.
              Fur...