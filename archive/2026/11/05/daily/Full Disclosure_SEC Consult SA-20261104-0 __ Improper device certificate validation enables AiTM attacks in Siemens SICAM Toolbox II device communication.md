---
title: SEC Consult SA-20261104-0 :: Improper device certificate validation enables AiTM attacks in Siemens SICAM Toolbox II device communication
url: https://seclists.org/fulldisclosure/2026/Nov/12
source: Full Disclosure
date: 2026-11-05
fetch_date: 2026-11-06T08:41:45.756562
---

# SEC Consult SA-20261104-0 :: Improper device certificate validation enables AiTM attacks in Siemens SICAM Toolbox II device communication

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20261104-0 :: Improper device certificate validation enables AiTM attacks in Siemens SICAM Toolbox II device communication

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Nov 2026 08:24:01 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20261104-0 >
=======================================================================
              title: Improper device certificate validation enables AiTM attacks
            product: Siemens SICAM Toolbox II device communication
 vulnerable version: <V07.11
      fixed version: V07.11
         CVE number: CVE-2024-31853, CVE-2024-31854
             impact: High
           homepage:https://www.siemens.com/en-us/products/sicam/toolbox-ii/
              found: 2023-10-16
                 by: Stefan Viehböck
                     Constantin Schieber-Knöbl (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Siemens SICAM Toolbox II - Engineering software for SICAM RTUs.
SICAM TOOLBOX II provides all functions for integrated and standard
engineering throughout the entire plant, e.g.: Data collection, data
modeling, configuration, and parameterization. Engineering of process
information for the automation and central control-room systems.
SICAM TOOLBOX II is an ideal tool for plants and systems of all sizes."

Source:https://www.siemens.com/global/en/products/energy/energy-automation-and-smart-grid/substation-automation/engineering-software-for-sicam-rtus-sicam-toolbox-ii.html

Business recommendation:
------------------------
The vendor provides a patched version V07.11 or higher since July 2025.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Improper device certificate validation enables AiTM attacks (CVE-2024-31853, CVE-2024-31854)
The SICAM Toolbox II connects with supported devices via an HTTPS connection
(TCP port 443, TLS1.2). The Toolbox II software uses a hard-coded client
certificate issued by the same Siemens CA when connecting to a device. Each
device uses a device-specific certificate issued by a Siemens CA
("SICAM1703-Access-V1") as a server certificate. The certificate is
generated/signed during the production process. The common name is the device
serial number.

Due to a vulnerability in the certificate validation during the TLS connection,
an attacker can perform an adversary-in-the-middle-attack.

The Toolbox II software only checks if the certificate was issued by the
trusted CA, but does not check if the certificate is actually issued to the target
device (e.g. by checking the certificate common name against an expected
value). It is even possible to use the hard-coded Toolbox II client certificate
instead of an actual device-specific certificate.

This attack can be used to steal RTU connection passwords, process data or modify
the device configuration.

Proof of concept:
-----------------
1) Improper device certificate validation enables AiTM attacks (CVE-2024-31853, CVE-2024-31854)
An attacker requires the private key of any certificate issued by the
"SICAM1703-Access-V1" CA for successful exploitation.

The most simple way to exploit the vulnerability is to extract the
certificate/private key pair from the Toolbox II software. The P12 container
can be found in the satzp.exe executable (located in /EMII/BIN/). The P12 file
is stored in obfuscated form and de-obfuscated at runtime when establishing new
TLS connections. Furthermore the P12 container is protected by a passphrase which
is stored in obfuscated form as well.

Unlike a regular device-specific certificate, the common name of this
certificate is "ToolboxII" and the extended key usage is "TLS Web Client
Authentication".

Alternatively an attacker could also extract a device-specific certificate
private key from a device (from the VaultIC chip).

Below is the Toolbox II client certificate and the corresponding private key
(redacted).

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 2 (0x2)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = DE, ST = Deutschland, L = Berlin, O = Siemens AG, OU = Energy Automation, CN = SICAM1703-Access-V1
        Validity
            Not Before: Jan  1 01:01:01 2011 GMT
            Not After : Dec 31 23:59:59 9999 GMT
        Subject: C = DE, ST = Deutschland, L = Berlin, O = Siemens AG, OU = Energy Automation, CN = ToolboxII
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:eb:56:a3:40:86:72:42:42:ca:1c:6c:25:41:11:
                    09:1d:20:ad:79:71:14:94:5c:02:a0:95:a6:ce:26:
                    1f:30:e2:21:9e:39:30:66:35:0c:df:77:e5:60:0b:
                    76:89:66:4a:08:f1:27:65:84:fc:d9:f1:b0:a3:b4:
                    4b:cf:dc:30:da:93:2b:74:e8:ac:3e:c5:5b:00:dd:
                    a9:03:79:f6:38:c5:1a:26:87:51:dd:1c:ad:72:b6:
                    c2:97:4c:62:f1:82:aa:86:e7:79:c9:82:b9:53:5b:
                    8d:40:26:76:1d:b0:03:2f:ce:ec:6e:f2:4a:af:79:
                    f3:e1:67:8b:c0:52:3b:f1:3e:dc:0d:8f:a4:f8:20:
                    e5:92:e3:ff:97:2b:34:a8:90:2c:79:42:3a:d0:e8:
                    ff:0d:d0:98:64:a8:5f:76:5f:e3:d8:bd:3e:85:3d:
                    49:33:ab:ae:54:5c:2a:2d:70:d0:95:3f:aa:cb:2d:
                    bf:34:f3:a2:f9:ae:17:a9:97:8f:a3:e2:ad:ad:f2:
                    ab:55:57:5b:04:56:b8:26:c3:fc:04:81:c9:ea:f5:
                    83:34:25:4a:22:9e:d5:73:6e:a4:d4:96:5b:65:3f:
                    cc:9d:97:df:6e:62:49:ae:a4:f2:4a:28:04:65:7d:
                    3d:7a:af:ba:69:49:75:32:a0:51:f0:93:69:fd:da:
                    eb:d1
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Alternative Name:
                email:support.energy () siemens com
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment, Data Encipherment
            X509v3 Extended Key Usage: critical
                TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
         21:15:68:6e:5c:34:80:a7:95:d5:a9:fa:62:64:6f:16:63:c5:
         8f:d6:42:c3:d3:dc:41:b4:98:e1:9c:13:47:d0:c7:c6:6c:66:
         a5:27:1e:b2:f1:99:5b:17:cc:63:78:2e:d5:26:84:8a:58:68:
         81:ee:f9:4f:0a:46:09:ec:23:77:e2:d6:f9:51:31:80:34:c3:
         9f:e5:45:01:e4:e9:5e:2e:94:08:ea:80:7b:1b:25:01:95:32:
         5c:6b:5b:30:8c:a5:5c:e4:b2:99:2a:83:22:ee:82:55:6e:d6:
         38:57:8e:37:54:53:89:03:8d:1a:26:2c:15:a2:d9:6f:88:c5:
         b0:a4:4b:e8:85:43:9d:25:c1:f4:eb:c0:b0:14:d0:7f:32:d7:
         d1:54:34:28:7d:a7:59:ff:35:25:9f:33:df:18:8f:1f:74:cd:
         c2:51:a0:06:35:d2:4d:c5:c3:b2:3e:b4:b0:05:fb:30:d1:c1:
    ...