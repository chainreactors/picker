---
title: SEC Consult SA-20250226-0 :: Multiple vulnerabilities in Siemens A8000 CP-8050 & CP-8031 PLC
url: https://seclists.org/fulldisclosure/2025/Feb/19
source: Full Disclosure
date: 2025-02-28
fetch_date: 2025-10-06T20:47:39.618721
---

# SEC Consult SA-20250226-0 :: Multiple vulnerabilities in Siemens A8000 CP-8050 & CP-8031 PLC

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250226-0 :: Multiple vulnerabilities in Siemens A8000 CP-8050 & CP-8031 PLC

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 26 Feb 2025 09:51:35 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250226-0 >
=======================================================================
              title: Multiple Vulnerabilities
            product: Siemens A8000 CP-8050 PLC
                     Siemens A8000 CP-8031 PLC
 vulnerable version: <05.40 for Vulnerability 1, <05.30 for Vulnerability 2
      fixed version: 05.40 for Vulnerability 1, 05.30 for Vulnerability 2
         CVE number: CVE-2024-39601, CVE-2024-53832
             impact: High
           homepage: https://www.siemens.com
              found: 2023-04-03
                 by: Stefan Viehboeck (Office Vienna)
                     Steffen Robertz (Office Vienna)
                     Gerhard Hechenberger (Office Vienna)
                     Constantin Schieber-Knoebl (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We are a technology company focused on industry, infrastructure,
transport, and healthcare. From more resource-efficient factories,
resilient supply chains, and smarter buildings and grids, to cleaner
and more comfortable transportation as well as advanced healthcare,
we create technology with purpose adding real value for customers."

Source: https://new.siemens.com/global/en/company/about.html

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of
the product conducted by security professionals to identify and resolve
potential further security issues.

Vulnerability overview/description:
-----------------------------------
1) Firmware Downgrade (CVE-2024-39601)
The PLC allows the downgrade to previous firmware versions. Therefore,
an attacker is able to downgrade to a firmware version with known
vulnerabilities (e.g., RCE) and exploit them on the PLC, which may
lead to leaking data or backdoored devices. A user account or physical
access is required for firmware upgrades/downgrades.

2) Firmware Update Decryption via Secure Element Oracle (CVE-2024-53832)
The PLC includes a secure element which is connected via an unencrypted
SPI bus. By connecting to this SPI bus, the password for the secure
element authentication can be observed. This allows an attacker to use
the secure element outside of the PLC as an oracle and leads to the
possibility to decrypt all encrypted update files.

Proof of concept:
-----------------
1) Firmware Downgrade (CVE-2024-39601)
A firmware upgrade/downgrade can be triggered in multiple ways, here,
the SICAM WEB interface was used. The current firmware version can be
viewed at "Applications" -> "Installed applications" and was
"CPCI85 04.93" at start. After successfully installing the firmware
file "CPCI8504.F92" via the hamburger menu entry
"Update" -> "Update firmware ..." at the top left corner, the current
firmware version shows "CPCI85 04.92". The downgrade was successful.

2) Firmware Update Decryption via Secure Element Oracle (CVE-2024-53832)
The PLC uses a VaultIC405 secure element in a SOIC8 package connected
via SPI. Its pinout can be seen below:

          +-----------+
SPI_MOSI =| *         |= SPI_MISO
     GND =|  VaultIC  |= VCC
 !SPI_SS =|    405    |= NC
!SPI_SEL =|           |= SPI_SCK
          +-----------+

When connecting to the SPI bus, cleartext data can be read. E.g., the
SubmitPassword command, which looks as follows:

| 0x00 0x00 0x10 0x80 0x20 | UserID | RoleID | Password length | Password | Checksum |

Reverse engineering the communication, the used credentials can be
identified as "SiemensUser", ID 1, Role 2. For decrypting updates, the
algorithm "CIP_RSAES_PKCS" is used. After setting the algorithm, data
can be sent to the secure element, the data is decrypted using the
secure element's private key, and the data can be read from the secure
element. This knowledge now allows to use the secure element as oracle
to decrypt updates. For this, the VaultIC shared library
/lib/libvaultic_api_4xx.so was loaded together with a custom library
in between (using LD_PRELOAD) from a custom C program, which was
executed on a Raspberry Pi using the SPI kernel driver to communicate
with the connected secure element.

Every firmware update file contains multiple encrypted archive files,
which are encrypted using a different, random, RSA encrypted AES key.
However, all AES keys can be decrypted using the secure element oracle.
For the following example, the "SICORE_KERNEL_V04.MB_arm.ear" archive
from the "CPCI8504.F93" update archive was used. Extracted, it contains
two files:
* AES encrypted package "SICORE_KERNEL_V04.MB_arm.ipk.enc"
* RSA encrypted AES key "SICORE_KERNEL_V04.MB_arm.ipk.key"
The .key file content is shown below:
-----------------------------------------------------------------------
00000000: 588c f4b8 50c9 27a9 6fcd 7aee 787d 87e2 ...."./uZ.....k{
[...]
000000f0: c3c0 ec53 c671 8024 748f e7ee 2e5f d6b6 ...S.q.$t...._..
-----------------------------------------------------------------------
Using the secure element oracle, the .key file can be decrypted as
"key.bin" file below:
-----------------------------------------------------------------------
00000000: 027a XXXX XXXX XXXX XXXX XXXX XXXX XXXX .z.0XXXXXXXXXXXX
00000010: XXXX XXXX XXXX XXXX XXXX XXXX XXXX 28e4 XXXXXXXXXXXX^r(.
-----------------------------------------------------------------------

The decryption was reverse engineered from the "IDEC00.elf" binary on the
PLC and turned out to be AES in CTR mode. A small C program "decrypt"
was written to decrypt the .enc file with a given key, using the OpenSSL
"CRYPTO_ctr128_encrypt" function. It was used as follows:
-----------------------------------------------------------------------
$ ./decrypt SICORE_KERNEL_V04.MB_arm.ipk.enc out.ipk key.bin
key 02 7a XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX 28 e4
filesize 5131094 bytes
-----------------------------------------------------------------------
The created out.ipk file is now a valid IPK software archive. The first
few bytes are given below:
-----------------------------------------------------------------------
00000000: 213c 6172 6368 3e0a 6465 6269 616e 2d62 !<arch>.debian-b
00000010: 696e 6172 792f 2020 3136 3736 3930 3936 inary/ 16769096
00000020: 3736 2020 3020 2020 2020 3020 2020 2020 76  0    0
00000030: 3130 3036 3434 2020 3520 2020 2020 2020 100644 5
00000040: 2020 600a 322e 300d 0a0a 636f 6e74 726f   `.2.0...contro
00000050: 6c2e 7461 722e 677a 2f20 3136 3736 3930 l.tar.gz/ 167690
-----------------------------------------------------------------------
The archive contains a control.tar.gz, data.tar.gz, and a debian-binary
file and can be opened with an archive...