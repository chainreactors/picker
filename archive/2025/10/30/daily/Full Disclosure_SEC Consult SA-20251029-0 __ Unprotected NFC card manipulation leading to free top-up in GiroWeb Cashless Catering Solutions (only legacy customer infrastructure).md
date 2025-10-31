---
title: SEC Consult SA-20251029-0 :: Unprotected NFC card manipulation leading to free top-up in GiroWeb Cashless Catering Solutions (only legacy customer infrastructure)
url: https://seclists.org/fulldisclosure/2025/Oct/32
source: Full Disclosure
date: 2025-10-30
fetch_date: 2025-10-31T03:14:41.281869
---

# SEC Consult SA-20251029-0 :: Unprotected NFC card manipulation leading to free top-up in GiroWeb Cashless Catering Solutions (only legacy customer infrastructure)

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#32)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20251029-0 :: Unprotected NFC card manipulation leading to free top-up in GiroWeb Cashless Catering Solutions (only legacy customer infrastructure)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 29 Oct 2025 07:33:15 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20251029-0 >
=======================================================================
              title: Unprotected NFC card manipulation leading to free top-up
            product: GiroWeb Cashless Catering Solutions
 vulnerable version: Only legacy customer infrastructure using outdated
                     Legic Prime or other insecure NFC cards
      fixed version: -
         CVE number: -
             impact: critical
    vendor homepage: https://giro-web.com/zahlungssysteme/
              found: 2022-12-20
                 by: Steffen Robertz
                     Christian Hager (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
(German) "GiroWeb ist ein Verbund aus 6 IT-Systemhäusern mit dem Fokus auf
Entwicklung, Installation und Betreuung von digitalen Kassen- und Zahlungssystemen.
Dazu zählen z.B. Online-Bestellsysteme, Smartphone-Apps, Aufwerter und
RFID-Kartenleser. Die GiroWeb Gruppe betreut deutschlandweit Projekte in den
Marktsegmenten Business-Catering und Education-Catering. Seit 30 Jahren liefern
wir unseren Kunden professionelle Lösungen und Dienstleistungen vor Ort."

Source: https://giro-web.com/giroweb-team/

Business recommendation:
------------------------
The vendor did not respond to our communication attempts and only communicated
with German BSI CERT-Bund, see timeline below. Hence, we are unaware of the
exact affected legacy solutions.

The vendor explicitly mentioned to CERT-Bund that they only use the existing
hardware of their customers and therefore those customers are responsible for
issuing secure cards and that it is not a security issue in GiroWeb solutions.

SEC Consult attempted to inform the vendor via CERT-Bund that this vulnerability
could potentially be resolved directly in GiroWeb. To do this, the account balance
would have to be stored directly in a database and validated when a withdrawal
is made. However, as direct communication was not possible, SEC Consult did not
receive a response and can therefore only assume that the problem is due to
outdated cards being used at legacy customer infrastructure.

In case of affected end users / customers, we urge them to update their
infrastructure to use secure cards and contact GiroWeb directly to work
on a solution to mitigate the known security issue of using vulnerable cards.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Unprotected NFC card manipulation leading to free top-up
The account balance is stored on an insecure NFC card. This means the card
can be read and written back. By manipulating the right field, one can
"create money out of thin air" and use it to pay for goods, or transfer
the fake sum back to the attacker's bank account.

Proof of concept:
-----------------
1) Unprotected NFC card manipulation leading to free top-up
GiroPay offers the usage of different card types. The tested solution was based
on Legic Prime NFC tags. Thus, all contents can be read if one owns the correct
hardware (e.g. a Proxmark device). By carefully observing changes in card dumps,
one can identify fields that store the cash value of the card.

Legic Prime tags use obfuscation to hide the cards data. In order to extract
the cleartext data, one has to XOR each byte of the dump with the CRC of the
UID (4th byte of dump). Afterwards, the Giroweb structure has to be identified in
the dump. This is done by calculating the CRC8-Mifare-MAD checksum over all
possible Giroweb structures. Only one should calculate a correct CRC. The stored
credit amount is a two byte value stored at the struct offset 5. The amount is
stored in cents. Thus, the most that the card can be charged up to is 655.35€.

After modifying this value, the checksum of the Giroweb struct has to be
recalculated. The data can then be written back to the tag and used to pay for
goods or to charge the credit back to a bank account.

The following Python script was developed to modify the data. It requires a dump
file created with `pm3 -c "hf legic dump"`. This will generate a .bin file
containing the obfuscated card data. Then call the script with e.g.:
`python giroweb_cash_mod.py -i hf-legic-DEADBEEF-dump.bin -d -m 1337 -o hf-legic-DEADBEEF-more-money.bin`

The output file can then be rewritten to the card with
`pm3 -c "hf legic restore -f hf-legic-DEADBEEF-more-money.bin"`.

giroweb_cash_mod.py Python script:
---------------------------------------
<PoC removed>
---------------------------------------

Vulnerable / tested versions:
-----------------------------
According to GiroWeb, some of their customers are still using outdated /
insecure cards and are therefore vulnerable. Exact versions or the
infrastructure in use are unknown.

Vendor contact timeline:
------------------------
Initially, those issues were already found late 2022 and verified again in 2023.
Our customer wanted to do the coordination internally, but communication was slow
hence we are proceeding with the CVD process again in 2025.

2025-02-04: Contacting vendor through support-nord () giro-web com; No response.
2025-02-19: Contacting vendor through support-nord () giro-web com and info-nord () giro-web com;
            No response
2025-03-03: Asking for an update; no response
2025-03-18: Asking for an update; no response
2025-03-25: Escalating to BSI/CERT-Bund
2025-03-27: CERT-Bund, they won't handle the CVD, because the LEGIC prime tags are
            already known as insecure. They will submit the details to the vendor.
2025-03-28: Explaining to CERT-Bund that it might be possible to cash out ~600 Euro
            daily through this attack and that fraud detection should be implemented
            in case it isn't. Asking for a contact at GiroWeb to discuss further details.
2025-04-16: CERT-Bund has established contact with the vendor.
2025-04-30: CERT-Bund answers that GiroWeb does not want to establish a direct contact
            with us. They submitted further details of our advisory to the vendor and
            our intentions to publish it.
2025-05-19: Asking if there is further information from the vendor, otherwise we would
            plan to release our advisory.
2025-06-10: Asking for a status update.
2025-06-16: CERT-Bund responds that the vendor has sent the details to their development
            team. The vendor also requested a meeting with CERT-Bund to discuss the
            vulnerability and potential mitigation. Requested postpone...