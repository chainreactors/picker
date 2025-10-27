---
title: iOS Activation Flaw Enables Pre-User Device Compromise and	Identity Exposure (iOS 18.5)
url: https://seclists.org/fulldisclosure/2025/Jun/27
source: Full Disclosure
date: 2025-07-02
fetch_date: 2025-10-06T23:58:23.011316
---

# iOS Activation Flaw Enables Pre-User Device Compromise and	Identity Exposure (iOS 18.5)

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# iOS Activation Flaw Enables Pre-User Device Compromise and Identity Exposure (iOS 18.5)

---

*From*: josephgoyd via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 26 Jun 2025 06:11:49 +0000

---

```
Title: iOS Activation Flaw Enables Pre-User Device Compromise

Reported to Apple: May 19, 2025
Reported to US-CERT: May 19, 2025
US-CERT Case #: VU#346053
Vendor Status: Silent
Public Disclosure: June 26, 2025

------------------------------------------------------------------------
Summary
------------------------------------------------------------------------

A critical vulnerability exists in Apple’s iOS activation pipeline that
allows remote XML payload injection *before* the user ever interacts
with the device.

During factory setup, iPhones contact:

https://humb.apple.com/humbug/baa

This provisioning endpoint returns unsigned `.plist` configuration
payloads — accepted without cryptographic verification or source
authentication.

An attacker positioned on the network (or in any upstream infrastructure
path) can inject arbitrary XML configuration data that SetupAssistant
will silently process. These changes persist through reboot and affect
system trust, network behavior, and identity provisioning — *before any
user touches the screen.*

------------------------------------------------------------------------
Context
------------------------------------------------------------------------

This disclosure is based on forensic reconstruction of a **real-world
attack observed in the wild**.

These files were extracted from a live device that exhibited
compromise behavior during initial activation. The artifacts presented
here are part of a post-event forensic reconstruction — **not
simulated**, emulated, or crafted artificially.

The compromise occurred during normal SetupAssistant operation, with
no jailbreak, developer tools, or device modifications present.

------------------------------------------------------------------------
Tested Device
------------------------------------------------------------------------

- iPhone running iOS 18.5 (latest as of June 2025)
- Restored to factory settings
- Activated using standard consumer setup flow
- No MDM enrollment or dev profile present

------------------------------------------------------------------------
Impact
------------------------------------------------------------------------

- Remote injection of provisioning configuration before user control
- Persistent `.plist` file modifications affecting:
- Cloud identity frameworks
- Trust and network defaults
- Activation and Apple service behaviors
- System logs show `.plist` entries written and processed before setup
- **Other `.plist` files** can be similarly injected and silently applied
- All occurs pre-setup, pre-consent, and without user awareness

This undermines trust in the provisioning path for:
- Consumers
- Enterprises
- Regulated and government environments

Relevant regulatory exposure includes:
- GDPR / CCPA (privacy violations before consent)
- CMMC 2.0 / NIST 800-171 (loss of provisioning integrity)
- FedRAMP / FISMA (unauthenticated system configuration)

------------------------------------------------------------------------
Technical Summary
------------------------------------------------------------------------

- SetupAssistant connects to `humb.apple.com/humbug/baa` during activation
- This endpoint returns a `.plist` (XML) payload
- Payload is **not signed, not authenticated, and not verified**
- Device accepts and applies it as system configuration
- The following were observed:
- `mobileactivationd.log`: full provisioning POST/response
- `com.apple.bird.plist`: persisted identity config before user input
- Other config files can be similarly injected and silently accepted

------------------------------------------------------------------------
Artifacts
------------------------------------------------------------------------

Attached:
1. `mobileactivationd.log` — provisioning session from activation
2. `com.apple.bird.plist` — identity-related configuration written pre-setup

These files are **unaltered and timestamped**, captured from a real device
during activation after observed anomalous behavior.

------------------------------------------------------------------------
Recommendations
------------------------------------------------------------------------

- Enforce digital signature checks for activation payloads
- Require authentication and origin validation for provisioning endpoints
- Apply strict XML schema validation to all `.plist` responses
- Halt logging of identity-related configuration during SetupAssistant
- Release urgent patch (iOS 18.5.1) to harden client-side provisioning logic

------------------------------------------------------------------------
Timeline
------------------------------------------------------------------------

May 19, 2025 Reported to Apple and US-CERT
June 23, 2025 US-CERT opened case VU#346053
June 26, 2025 Public disclosure

------------------------------------------------------------------------
Researcher
------------------------------------------------------------------------

Joseph Raymond Goydish II

------------------------------------------------------------------------
```

**Attachment:
[mobileactivationd log .pdf](att-27/mobileactivationd_log__pdf.bin)**
*Description:*

**Attachment:
[com.apple.bird.pdf](att-27/com_apple_bird_pdf.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **iOS Activation Flaw Enables Pre-User Device Compromise and Identity Exposure (iOS 18.5)** *josephgoyd via Fulldisclosure (Jun 30)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insec...