---
title: Apple iOS 17.2.1 - Screen Time Passcode Retrieval (Mitigation	Bypass)
url: https://seclists.org/fulldisclosure/2024/Sep/51
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:26:13.264254
---

# Apple iOS 17.2.1 - Screen Time Passcode Retrieval (Mitigation	Bypass)

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

[![Previous](/images/left-icon-16x16.png)](50)
[By Date](date.html#51)
[![Next](/images/right-icon-16x16.png)](52)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
[![Next](/images/right-icon-16x16.png)](52)

![](/shared/images/nst-icons.svg#search)

# Apple iOS 17.2.1 - Screen Time Passcode Retrieval (Mitigation Bypass)

---

*From*: Patrick via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Sep 2024 04:09:51 +0000

---

```
Document Title:
===============
Apple iOS 17.2.1 - Screen Time Passcode Retrieval (Mitigation Bypass)

Release Date:
=============
2024-09-24

Affected Product(s):
====================
Vendor: Apple Inc.
Product: Apple iOS 17.2.1 (possibly all < 18.0 excluding 18.0)

References:
====================
VIDEO PoC: https://www.youtube.com/watch?v=vVvk9TR7qMo

The vulnerability has been patched in the latest release of the operating
system (iOS 18.0).

Abstract Advisory Information:
==============================
A mitigation bypass / privilege escalation flaw has been discovered in Apple's
iOS Screen Time functionality, granting one access to modify the restrictions.

It allows a local attacker to acquire the Screen Time Passcode by bypassing the
anti-bruteforce protections on the four-digit Passcode, and in consequence
gaining total control over Screen Time (Parental Control) settings.

Common Weakness Enumeration
====================================
CWE-307: Improper Restriction of Excessive Authentication Attempts
CWE-799: Improper Control of Interaction Frequency

Exploitation Technique:
=======================
Local

Severity Level:
===============
Moderate

Discovery Status:
=================
Full Disclosure

Technical Details & Description:
================================
1. The Screen Time Passcode input is generally immune to bruteforce attacks,
and the following document reveals a weakness in the implementation of these
mitigations.

2. The Passcode always consists of four digits, therefore the range of values
an attacker needs to check is low.

3. The usage of an external HID, particularly a keyboard,
whether one connected through USB-C, Lightning or Bluetooth, simplifies and
enhances the speed and practicality of the brute force attack.

4. In nearly all cases, the Screen Time Passcode input form is fortified with
strict mitigations, such as time delay imposed upon reaching
a certain threshold of subsequent failed attempts.

5. This can be noticed when one attempts to manually guess the Passcode in
"Settings > Screen Time", where multiple consecutive failed attempts trigger
the anti-bruteforce mitigation.

6. The aforementioned mitigation is akin to the one in the Screen Lock input,
with increasingly long delays after every block, making it a solid mitigation
against bruteforce attacks.

7. In one case, such mitigations are absent, enabling rapid bruteforce attacks
against a low-complexity, four-digit input, suggesting a CWE-307 vulnerability.

8. Because of this case, all the other protections of the Screen Time Passcode
in practice become null and void.

9. It is possible to create an user friendly, cross-platform software, that
would allow children, or other people under Screen Time, to easily acquire
the code to its settings.

10. It is often the case that such codes are exactly the same on every device
associated with one iCloud account, extending the impact to other devices.

Proof of Concept (PoC):
=======================
Assumptions: Screen Time is enabled, and the Screen Time Passcode is set.

1. Open "Settings"
2. Go to "General"
3. Scroll down to "Erase Content and Settings"
4. Once prompted, choose "Erase Content and Settings" again.
5. Agree with the dialogue, proceed further.
6. Press the red button asking for confirmation of the erasure.
7. Enter the current Device Passcode or Password.
8. Now you will be asked to enter the Screen Time Passcode (if one is set).
This four digit input form is vulnerable to unlimited bruteforce attacks.
9. Once the correct Passcode is provided, the "Uploading Data to iCloud"
screen should appear.
10. The moment it happens, go back IMMEDIATELY (use the arrow on the upper left
corner of the screen to stop the process before it begins erasing data)
11. The device erasure process should now be stopped.
12. The Screen Time Passcode should now be well-known.

VIDEO PoC: https://www.youtube.com/watch?v=vVvk9TR7qMo

Security Risk:
==============
The security risk is estimated as moderate, and context dependent.

Abuse of this vulnerability results in full control over tScreen Time settings
imposed on the device, making it possible to disarm all the restrictions.

It is worth mentioning, that the Passcode could be shared among other devices
associated with the same iCloud account. If this is the case, the impact of
the vulnerability becomes more significant.

Example restrictions provided by Screen Time, that could be then deactivated:

- Harmful content protection (adult / traumatizing content, malicious websites)
- Restrictions on communication with strangers
- Device usage time limits (Downtime, daily usage limits).
- Camera, location and microphone access permissions for specific applications.
- Device activity monitoring and reporting.
- Application-specific usage time limits.
- Application-specific functionality limits.
- Security settings that require the Screen Time Passcode to access and modify.
- and possibly more...

The attack, when executed properly:
- can be repeated, in case the Screen Time Passcode gets changed by the parent.
- can be used to change the Passcode to an arbitrary one, or disable it.
- can be used to shut down all the system parental control settings on the,
device, and possibly acquire similar power against other synchronized devices.
- gives one the silent knowledge of the Passcode, which makes it more stealthy
and detection resilient.

There are no known protections against this attack, other than an upgrade of
all the devices running on vulnerable versions, to the latest version.

Solution - Fix & Patch:
=======================
Patched in iOS 18.0, despite not being acknowledged by the vendor.
Fixed with a silent rate-limit enforced on the vulnerable input.

Vulnerability Disclosure Timeline:
==================================
2023-12-21: The vulnerability has been reported to the vendor.
2023-12-23: The vendor has refused to acknowledge the vulnerability.
2023-12-27: The vulnerability has been reported again, more details included,
and real-world impact scenarios, complete with a clear video demonstration.
2024-01-02: The vendor has refused to acknowledge the vulnerability once again.
2024-09-16: The vulnerability has been patched in the next major release
of the vulnerable system (iOS 18.0).
2024-09-24: Full disclosure of the vulnerability.

Credits & Authors:
==================
SivertPL (kroppoloe () protonmail ch)
```

**Attachment:
[writeup.txt](att-51/writeup.txt)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](50)
[By Date](date.html#51)
[![Next](/images/right-icon-16x16.png)](52)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
[![Next](/images/right-icon-16x16.png)](52)

### Current thread:

* **Apple iOS 17.2.1 - Screen Time Passcode Retrieval (Mitigation Bypass)** *P...