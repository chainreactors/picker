---
title: SEC Consult SA-20250211-0 :: Multiple vulnerabilities in Wattsense Bridge
url: https://seclists.org/fulldisclosure/2025/Feb/9
source: Full Disclosure
date: 2025-02-14
fetch_date: 2025-10-06T20:39:33.183819
---

# SEC Consult SA-20250211-0 :: Multiple vulnerabilities in Wattsense Bridge

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
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250211-0 :: Multiple vulnerabilities in Wattsense Bridge

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 11 Feb 2025 09:01:08 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250211-0 >
=======================================================================
              title: Multiple vulnerabilities
            product: Wattsense - Wattsense Bridge
 vulnerable version: Wattsense Bridge
                      * Hardware Revision: WSG-EU-SC-14-00, 20230801
                      * Firmware Revision: Wattsense (Wattsense minimal)
                                           5.7.2 ws-box-v1.3
      fixed version: Issue 2&3 >=6.4.1, Issue 4 >=6.1.0
         CVE number: CVE-2025-26408, CVE-2025-26409, CVE-2025-26410
                     CVE-2025-26411
             impact: high
           homepage: https://www.wattsense.com
              found: 2023-11-20
                 by: Constantin Schieber-Knöbl (Office Vienna)
                     Stefan Schweighofer (Office Vienna)
                     Steffen Robertz (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Buildings in the EU are responsible for 40% of our energy consumption and
36% of greenhouse gas emissions.
At Wattsense, we believe that to reduce those hard-hitting numbers and
positively change our environment, we must bring technology, mostly reserved
for new or large facilities, to smaller and medium-sized buildings.
Wattsense gives property owners the power to make their buildings more
sustainable."

Source: https://www.wattsense.com/about

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
For the vulnerabilities 1-4 the following impact arises, if one of these
vulnerabilities is successfully exploited.
An attacker with physical access to the device can control the measurements
and switching behavior of the device by e.g., installing a backdoor for
later remote access. Since the Wattsense Bridge can trigger actions on
physical devices, safety violations and physical damages are possible.

1) Access to JTAG Interface (CVE-2025-26408)
The JTAG interface can be accessed with physical access to the PCB.
After connecting to the interface, full access to the device is
possible. This enables an attacker to extract information, modify
and debug the device's firmware.

2) Access to Bootloader and Shell Over Serial Interface (CVE-2025-26409)
A serial interface can be accessed with physical access to the PCB. After
connecting to the interface, access to the bootloader is possible,
as well as a Linux login prompt. The bootloader access can be used to gain
a root shell on the device.

3) Weak Hardcoded Credentials (CVE-2025-26410)
The firmware of all devices contain the same hardcoded user and
root credentials. The user password can be easily recovered via password
cracking attempts. The recovered credentials can be used to log into
the device via the login shell that is exposed by the serial interface,
described in the previous vulnerability "2) Access to Bootloader and
Shell Over Serial Interface".

4) Authenticated Arbitrary Python File Upload via Plugin Manager (CVE-2025-26411)
An authenticated attacker is able to use the Plugin Manager of the web
interface to upload malicious python files to the device. This enables an
attacker to gain remote root access to the device. An attacker needs a
valid user account on the Wattsense web interface, where valid Wattsense
Bridge devices are configured, to be able to conduct this attack.

Proof of concept:
-----------------
1) Access to JTAG Interface (CVE-2025-26408)
The unlocked JTAG interface is exposed on the stamp hole expansion interface
of the system on module (SoM) processing PCB (Myirtech MYC-Y6ULX) and is
documented in the related datasheet. By soldering the appropriate pins
(TMS, TCK, TDI, TDO, TRST) to the PCB, the JTAG port is accessible by an
adaptor. The MOD pin can be left unconnected and enables software debug
features when no high signal is provided with a pull-up.
The Segger J-Link PRO JTAG adaptor is used to connect. The debugging software
OpenOCD can then be used to manipulate and read the firmware. This grants an
attacker with physical access to the device full control of the device.

2) Access to Bootloader and Shell Over Serial Interface (CVE-2025-26409)
The serial interface on the Wattsense Bridge can be accessed by connecting to
the following pin header (GND, TX, RX) that is present on the PCB:

--------|
 +-+    |
 |o|GND |
 |o|RX  |
 |o|TX  |
 +-+    |
       Micro USB Port
        |

A serial-USB adaptor (e.g., FT232 based board) can be used to access the
serial interface. The following settings on an arbitrary terminal-program
are necessary:
 * Voltage: 3.3V
 * Speed: 115200 Baud
 * Symbol-ratio: 8 Data Bits 1 Stop Bit (8N1)

After a successful connection, the bootloader is available by pressing any
key at startup. With the resulting U-Boot command shell, the environment
variables of the boot process can be modified. This allows an attacker
to launch a root shell during the boot process:

=> setenv mmcargs "setenv bootargs console=${console},${baudrate} root=${mmcpath} ${mmcroot}
${raucslot} init=/bin/sh"
=> boot

An attacker is now able to remount the file system to be readable and writeable
in the root shell:

# mount -o remount, rw /

At this point an attacker can for example backdoor the device with a new root
user by appending a line to the /etc/passwd file. Now the boot environment
needs to be reset to the previous state. After starting the device, a Linux
login prompt is presented, where the newly created backdoor account can
then be used to login into the system.

3) Weak Hardcoded Credentials (CVE-2025-26410)
The firmware on all devices includes the same hardcoded user and root password
hash. The user password hash can easily be cracked with the password cracking
tool john:

$ john shadow
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cracked 1 password hash
No password hashes left to crack (see FAQ)

$ john --show shadow
wattsense:wattsense::0:99999:7:::
1 password hash cracked, 0 left

The user's password can then be used for example to also log into the system
as a normal user via the vulnerability described in "2) Access to Bootloader
and Shell Over Serial Interface".

4) Authenticated Arbitrary Python File Upload via Plugin Manager (CVE-2025-26411)
The "Plugin Manager" feature of the Wattsense web interface allows an
authenticated attacker to upload malicious python files to the Wattsense
bridge. With the following...