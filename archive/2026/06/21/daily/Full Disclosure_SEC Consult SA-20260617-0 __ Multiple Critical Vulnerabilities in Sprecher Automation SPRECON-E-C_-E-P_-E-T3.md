---
title: SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3
url: https://seclists.org/fulldisclosure/2026/Jun/19
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:00.858964
---

# SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3

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
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260617-0 :: Multiple Critical Vulnerabilities in Sprecher Automation SPRECON-E-C/-E-P/-E-T3

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 17 Jun 2026 05:51:31 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260617-0 >
=======================================================================
              title: Multiple Critical Vulnerabilities
            product: Sprecher Automation SPRECON-E-C/-E-P/-E-T3
 vulnerable version: See vulnerable versions below
      fixed version: See solution section below
         CVE number: CVE-2022-4333, CVE-2022-4332, CVE-2025-41741,
                     CVE-2025-41742, CVE-2025-41743, CVE-2025-41744
             impact: critical
           homepage:https://www.sprecher-automation.com/
              found: 2022-08-26
                 by: Steffen Robertz
                     Christian Hager (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com
=======================================================================

Vendor description:
-------------------
"Sprecher Automation provides products and solutions for power supply
and process automation. We secure critical infrastructures and optimise
complex energy and industry processes. [...]
Quality, availability and security – those are not only our customers's
requirements, but also goals we are striving for. Due to that, for example,
the hard- and software development are located in Austria and Germany.
We produce exclusively in Austria – starting with the production of
single elements, to system checks and practical inhouse testing."

Source:https://www.sprecher-automation.com/en/company

Business recommendation:
------------------------
The vendor provides updated versions as well as workaround information in
their security advisories. Users should verify whether the patches are
installed already, otherwise patch immediately.

SEC Consult highly recommends to perform a thorough security review of
the product conducted by security professionals to identify and resolve
potential further security issues.

Vulnerability overview/description:
-----------------------------------
1) Leak of Firmware Signing Private Key (CVE-2025-41741)
Sprecher signs its firmware update files to prevent an attacker from
loading manipulated update files. However, each PLC contains the
globally valid private signing key, as it is also used to sign backups.
An attacker, who obtains the key is able to ship validly signed,
modified firmware updates.

The security vulnerability has been resolved in firmware version 9 and
above. Further details can be found in the advisory of the vendor. In
previous versions the affected feature can be deactivated by the customer.
The stated key can only be used in conjunction with the backup feature.
Affected products: SPRECON-E-C/-E-P/-E CPU Modul

2) Missing Secure-Boot Mechanism (CVE-2022-4332)
The PLC is able to detect secure boot violations correctly. However,
the events are not handled properly. They only output a warning to the
boot log, but do not prevent the device's operation. Thus, anybody with
physical access to the device can modify the firmware and potentially
include backdoors.

The security vulnerability has been resolved in firmware version 8.71a and
above, as well as 8.64m. Further details can be found in the advisory
of the vendor. In current and previous versions the affected feature can be
deactivated by the customer.
Affected products: SPRECON-E-C/-E-P/-E

3) Unencrypted External Flash Memory (CVE-2022-4332)
The external flash memory can be dumped using tools such as the Xgecu
T56. This allows an attacker with physical access to read all files and
thus gain knowledge about sensitive files such as passwords and private
keys.

The security vulnerability has been resolved in firmware version 9 and above.
Further details can be found in the advisory of the vendor. In current and
previous versions the affected feature can be deactivated by the customer.
Affected products: SPRECON-E-C/-E-P/-E-T3

4) Usage of static passwords (CVE-2025-41742)
Various static passwords / key material can be discovered in the firmware.
They serve  different use cases, such as hard-coded user accounts, as well as
encryption for settings and configuration files. This allows an attacker
to decrypt configuration files, modify them and properly encrypt them
again.

According to the vendor, the documented static identity string does not serve
a security purpose in the system and is used as an identifier for maintenance.
Using the default identifier can lead to the targeted system being misidentified
during maintenance.
Affected products: SPRECON-E-C/-E-P/-E-T3

5) Hard-coded Vendor Accounts (CVE-2022-4333)
Two hard-coded vendor accounts were revealed in the devices. These
accounts are shipped with every update file and can be used by the
vendor e.g. for support access.

These documented accounts can be activated or deactivated in the configuration.
These accounts are additionally secured with 2FA in firmware version 8.71g.
Affected products: SPRECON-E-C/-E-P/-E-T3

6) Decrypt Firmware Update Files (CVE-2025-41743)
Firmware update files include hard-coded accounts from vulnerability 5 and
can be decrypted using an XOR algorithm and a static password. This
allows an attacker to further analyze PLC components as well as gaining
knowledge of private keys and hard-coded accounts without requiring
physical access to any device.

The signature and encryption mechanism have been modified and the security
vulnerability has been resolved in version 8.71 and above. Further details
can be found in the advisory of the vendor.
Affected products: SPRECON-E-C/-E-P/-E-T3

7) Insecure Transport Encryption (CVE-2025-41744)
The PLC's webserver and the connection to the Sprecher Engineering Center
software use the same static default key on all devices. An attacker who gains
access to the private key via vulnerability 3 or 6 can thus decrypt all
traffic in a man-in-the-middle position. Thus, an attacker would be
able to change configurations and read connection passwords.

According to the vendor, those certificates are only used during initial
commissioning and users can find further information to change the certificates
in the documentation/guideline "SPRECON Grundhärtung" (basic hardening).
The vendor's hardening guide makes it clear that it is both possible and
recommended to change the default certificate.
Documentation: 94.2.913.50en SPRECON Basic Hardening

Proof of concept:
-----------------
1) Leak of Firmware Signing Private Key (CVE-2025-41741)
Backups are restored by the same command flow as regular update files.
Thus, backups need to be validly signed as well. For this, Sprecher's
private key is required. The following openssl command signs the
created backup:

```
openssl dgst -sha256 -sign ${SSM_CERT}/.backup.key -passinfile:${SSM_CERT}/.pass -out
${SSM_SECURE_DIR}/image.sha256 ${SSM_SECURE_DIR}/image.zip 2>/dev/null
```

The private key and password are...