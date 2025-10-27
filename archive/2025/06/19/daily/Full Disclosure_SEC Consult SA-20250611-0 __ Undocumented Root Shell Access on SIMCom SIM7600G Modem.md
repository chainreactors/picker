---
title: SEC Consult SA-20250611-0 :: Undocumented Root Shell Access on SIMCom SIM7600G Modem
url: https://seclists.org/fulldisclosure/2025/Jun/17
source: Full Disclosure
date: 2025-06-19
fetch_date: 2025-10-06T22:57:10.790710
---

# SEC Consult SA-20250611-0 :: Undocumented Root Shell Access on SIMCom SIM7600G Modem

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250611-0 :: Undocumented Root Shell Access on SIMCom SIM7600G Modem

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Jun 2025 14:35:36 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250611-0 >
=======================================================================
              title: Undocumented Root Shell Access
            product: SIMCom - SIM7600G Modem
 vulnerable version: Firmware Revision: LE20B03SIM7600M21-A
      fixed version: -
         CVE number: CVE-2025-26412
             impact: Medium
           homepage: https://www.simcom.com
              found: 2023-11-20
                 by: Constantin Schieber-Knöbl (Office Vienna)
                     Stefan Schweighofer (Office Vienna)
                     Steffen Robertz
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Founded in 2002, SIMCom Wireless Solutions Limited has been committed to
providing a variety of wireless modules and solutions including 5G, 4G,
LPWA, LTE-A, smart module, automotive module, 3G, 2G and GNSS for 20 years.
According to the latest M2M report by ABI Research Inc., a well-known
U.S. market research company, SIMCom has made the largest shipments of
wireless module for 4 consecutive years."

Source: https://www.simcom.com/about.html

Business recommendation:
------------------------
The vendor was unresponsive to multiple communication attempts during over one
year of responsible disclosure after submitting our advisory to them, see the
timeline below.

It is unknown to us whether a patch is available. Customers of SIMCom are urged
to reach out to their contact person at SIMCom or distributors to demand a patch
which removes the backdoor command.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues and verify the removal of the backdoor command.

Vulnerability overview/description:
-----------------------------------
1) Undocumented Root Shell Access (CVE-2025-26412)
The SIMCom SIM7600G modem supports an undocumented AT command, which allows
an attacker to execute system commands with root permission on the modem.

An attacker needs either physical access or remote shell access to a device
that interacts directly with the modem via AT commands.

Proof of concept:
-----------------
1) Undocumented Root Shell Access (CVE-2025-26412)
The SIMCom SIM7600G modem supports an undocumented AT command, which
allows an attacker to execute commands with root permissions on the modem.
For this example the tool mmcli is used to communicate with the modem.
The following example shows how the AT command "AT+CSHELL" can be used to
execute system commands on the SIM7600G modem by a physically connected
attacker:

# mmcli --modem=1 --command='AT+CSHELL="id"'
response: '+CSHELL: uid=0(root) gid=0(root)'

Vulnerable / tested versions:
-----------------------------
The following firmware version has been tested on a SIMCom modem, that
was integrated in a 3rd-party device:
* Firmware Revision: LE20B03SIM7600M21-A

The vendor did not respond to our questions, which firmware revisions or
other products are affected. It is assumed that more firmware revisions
are affected.

Vendor contact timeline:
------------------------
2024-05-28: Contacting vendor through support () simcom com; no response.
2024-10-22: Contacting vendor again, vendor asks about where our company
            is located and where we purchased the modules.
            Explaining that we are a security consulting company and that
            we analyzed a product using the SIMCom modem.
2024-10-23: Vendor responds that they can't support us directly and the
            vendor of the 3rd-party product needs to contact their supplier/
            distributor.
            Answering them, that we found a security issue in their product
            and that our request was not for support nor help and the security
            issue affects all of SIMCom's customers. Asking for a security
            contact again. No response.
2024-11-13: Contacting vendor again if they received our previous email.
            Communicating advisory release after deadline on 11th December.
2024-11-18: SIMCom EU sales director contacts us, asking for details and that
            "their cellular modules work in 100% controlled environments and
            conform to all standards, if there are any security issues those
            will be related to the SIM or network provider."
            Sending technical advisory draft to SIMCom.
            No further response from vendor.
2024-12-10: Asking for a status update. No response.
2025-02-04: Asking for a status update again, scheduling advisory release.
            No response (except out of office until 6th February)
2025-02-11: Asking for status update again, reserving CVE-2025-26412, again
            out of office response until 19th February. No response.
            Attempting contact via different channels to our contact persons
            (via LinkedIn - profile was viewed, but other than that, no response)
2025-02-28: Last attempt, final communication of advisory release for next week.
            Providing recommendations to the vendor regarding the mandatory
            requirements of the Cyber Resilience Act in the future for security
            researcher communication. Receiving out of office reply (for 26th return).
2025-02-28: Vendor responds that they are aware of our request, but fail to understand
            where this request has been originated and are unable to determine the
            urgency and importance. SIMCom is aware of the CRA.
2025-03-02: Explaining everything again (CVD process, contact attempts in May/October
            2024 through support, etc.). Receiving out of office reply again until
            17th March 2025.
2025-03-03: SIMCom answers that our request could "not be associated with any customer
            or tangible market activity" and resources won't get assigned. Suggests
            conversation with third-party, where we identified the issue.
2025-03-03: Contacting third-party, informing them about the SIMCom status and asking
            them how they want to proceed.
2025-03-06: Third-party informs us that a test firmware is available where a password
            can be set for the shell.
2025-03-07: Following up with the 3rd party about "hard-coded passwords", aligning next
            steps
2025-03-07: Contacting SIMCom again and detailing the whole CVD process again and future
            alignment, asking for the firmware version of the fix and providing
            recommendations regarding the hard-coded password fix:
            Inform all customers about the new solution and provide updated firmware,
            make the password changeable for integrators etc, properly document t...