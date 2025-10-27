---
title: iOS 18.6 - Undocumented TCC Access to Multiple Privacy Domains	via preflight=yes
url: https://seclists.org/fulldisclosure/2025/Aug/5
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:15.352558
---

# iOS 18.6 - Undocumented TCC Access to Multiple Privacy Domains	via preflight=yes

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# iOS 18.6 - Undocumented TCC Access to Multiple Privacy Domains via preflight=yes

---

*From*: josephgoyd via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 17 Aug 2025 19:11:51 +0000

---

```
TITLE: Undocumented TCC Access to Multiple Privacy Domains via 'preflight=yes' in iOS 18.6
AUTHOR: Joseph Goydish II
DISCOVERY DATE: 2025-08-13
DEVICE: iPhone 14 Pro Max
OS VERSION: iOS 18.6 (non-jailbroken, stock)
SEVERITY: High
ACCESS: USB debugging or local log access
IMPACT: Silent, undocumented system access to sensitive user data across multiple TCC domains

-------------------------------------------------------------------------------

SUMMARY:

On iOS 18.6, the system daemon 'tccd' silently initiates TCCAccessRequest calls with the flag
'preflight=yes' across **multiple** privacy-protected domains including Contacts, Camera, FaceID,
Microphone, Calendar, Reminders, Bluetooth, and App Tracking Transparency (ATT).

These accesses:
- Occur without user interaction
- Do not trigger any permission prompt
- Are not associated with any user-facing app (client_dict=(null))
- Originate from internal Apple daemons (daemon_dict=<private>)
- Are invisible in Privacy Settings

This appears to be a systemic, undocumented telemetry or policy enforcement mechanism operating below the app layer,
capable of silently querying or accessing sensitive user data.

-------------------------------------------------------------------------------

CONFIRMED TCC DOMAINS ACCESSED:

TCC Service | Data Affected | Notes
----------------------------|----------------------------------|---------------------------------------------
kTCCServiceAddressBook | Contacts | Silent access to full address book
kTCCServiceCamera | Camera | Camera readiness/init observed
kTCCServiceFaceID | Face ID Biometric | Biometric usage without user consent
kTCCServiceMicrophone | Microphone | Accessed 7+ times in sequence
kTCCServiceCalendar | Calendar events & metadata | Silent background access
kTCCServiceReminders | Reminders | Previously documented
kTCCServiceBluetoothAlways | Bluetooth permissions | Often used for proximity tracking
kTCCServiceUserTracking | ATT / Identifier state | May indicate fingerprinting or telemetry

-------------------------------------------------------------------------------

PATTERN OBSERVATIONS:

- All access uses 'preflight=yes' → Bypasses standard TCC permission dialog
- All logs show client_dict=(null) → No app involvement
- daemon_dict=<private> → Internal Apple system process, redacted
- Microphone and FaceID are accessed multiple times in rapid succession

-------------------------------------------------------------------------------

EXAMPLES PER DOMAIN:

Contacts:
default 2025-08-13 16:53:35.953290 -0400 tccd AUTHREQ_CTX: msgID=2607.2, function=TCCAccessRequest,
service=kTCCServiceAddressBook, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Camera:
default 2025-08-13 16:53:36.038834 -0400 tccd AUTHREQ_CTX: msgID=66.13, function=TCCAccessRequest,
service=kTCCServiceCamera, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Face ID:
default 2025-08-13 16:53:43.620143 -0400 tccd AUTHREQ_CTX: msgID=109.13, function=<private>, service=kTCCServiceFaceID,
preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Microphone (repeated access):
default 2025-08-13 16:53:38.531850 -0400 tccd AUTHREQ_CTX: msgID=107.272, function=TCCAccessRequest,
service=kTCCServiceMicrophone, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Calendar:
default 2025-08-13 16:54:17.052257 -0400 tccd AUTHREQ_CTX: msgID=2284.90, function=TCCAccessRequest,
service=kTCCServiceCalendar, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Reminders:
default 2025-08-13 16:54:36.348792 -0400 tccd AUTHREQ_CTX: msgID=2284.97, function=TCCAccessRequest,
service=kTCCServiceReminders, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

Bluetooth:
default 2025-08-13 16:53:52.320858 -0400 tccd AUTHREQ_CTX: msgID=1651.1, function=TCCAccessRequest,
service=kTCCServiceBluetoothAlways, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

User Tracking:
default 2025-08-13 16:53:47.996844 -0400 tccd AUTHREQ_CTX: msgID=116.726, function=<private>,
service=kTCCServiceUserTracking, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>

-------------------------------------------------------------------------------

IMPACT:

- Covert access to biometric, microphone, calendar, and contact data
- Not visible or controllable via Privacy Settings
- User cannot audit, deny, or revoke this access
- Suggests behavioral profiling or device telemetry below user awareness
- Potentially violates GDPR/CCPA data processing regulations

-------------------------------------------------------------------------------

RISK SUMMARY PER DOMAIN:

Domain | Sensitivity | Risk
-------------|-------------|---------------------------------------------
Contacts | High | Names, emails, numbers silently queried
Camera | Critical | Could allow passive activation checks
Microphone | Critical | Background audio or readiness tracking
FaceID | High | Silent biometric usage
Calendar | Med-High | Event metadata, routines, appointments
Reminders | Medium | Personal planning data
Bluetooth | Medium | Location via beacon proximity
UserTracking | High | ATT state read; user fingerprinting risk

-------------------------------------------------------------------------------

REPRODUCIBILITY:

1. Use a clean iOS 18.6 device (non-jailbroken)
2. Connect it via USB to macOS
3. Open Console.app
4. Apply filter: subsystem == "com.apple.TCC"
5. Observe logs containing:
- function=TCCAccessRequest
- preflight=yes
- client_dict=(null)
- daemon_dict=<private>

-------------------------------------------------------------------------------

CONCLUSION:

These logs indicate a covert telemetry or policy enforcement system in iOS that interfaces
directly with the TCC (Transparency, Consent, and Control) framework — outside the user’s control.

There is no public documentation or API contract that explains this access.

If intentional, it undermines the platform’s stated privacy guarantees.
If unintentional, it represents a design flaw with regulatory implications.

-------------------------------------------------------------------------------

CONTACT:

Joseph Goydish
Email: josephgoyd () proton me
LinkedIn: https://www.linkedin.com/in/josephg007/

-------------------------------------------------------------------------------
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **iOS 18.6 - Undocumented TCC Access to Multiple Privacy Domains via preflight=yes** *josephgoyd via Fulldisclosure (Aug 18)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)
...