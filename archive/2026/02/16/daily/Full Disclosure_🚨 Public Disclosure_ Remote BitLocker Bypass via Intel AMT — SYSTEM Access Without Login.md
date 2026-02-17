---
title: 🚨 Public Disclosure: Remote BitLocker Bypass via Intel AMT — SYSTEM Access Without Login
url: https://seclists.org/fulldisclosure/2026/Feb/15
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.978760
---

# 🚨 Public Disclosure: Remote BitLocker Bypass via Intel AMT — SYSTEM Access Without Login

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# 🚨 Public Disclosure: Remote BitLocker Bypass via Intel AMT — SYSTEM Access Without Login

---

*From*: Darsh Naik <darsh.naik53 () gmail com>
*Date*: Sun, 15 Feb 2026 10:26:38 +0530

---

```
🔓 The Attack Path — No Login, SYSTEM Access

1. Boot into setup.exe (via USB, PXE, or OOBM like Intel vPro).
2. Click “Repair your computer” → Enter WinRE.
3. Press Shift + F10 → SYSTEM-level Command Prompt.
4. From there, attacker can:
   - Run `net user` to create new admin accounts
   - Use `diskpart` to wipe or reformat drives
   - Use `manage-bde -off` or `bcdedit` to disable BitLocker
   - Replace `utilman.exe` to bypass login
   - Implant persistence or backdoors

🧠 Why BitLocker Doesn’t Save You

- BitLocker is inactive in Setup or WinRE — the OS hasn’t loaded, and the
BitLocker driver isn’t running.
- If BitLocker is TPM-only (no PIN/USB), the drive is already unlocked at
boot.
- TPM 2.0 *can* block key release — but only if:
  - Secure Boot is enforced
  - PCR bindings are tightly configured
  - Boot order is locked
  - USB/PXE boot is disabled
  - OOBM is secured

Most orgs don’t meet all those conditions. Even if BitLocker triggers
recovery, an attacker can still wipe the drive or implant malware.
```

> ```
> CVE-2025-26637 and tools like BitUnlocker show how these vectors are
> ```

```
being actively explored.

🧨 “But We Have Immutable Backups”

That protects data availability — not system integrity.

If I implant malware or create a hidden admin account, you’ll restore into
a compromised environment. Immutable backups don’t detect or prevent:
- Credential theft
- Persistence
- Backdoored reboots
- Silent compromise of trust

🌐 Remote Risk: OOBM

With Intel vPro, I can:
- Mount virtual media
- Boot into Setup or WinRE
- Execute all of the above remotely, without touching the device

Intel’s own docs highlight how vPro enables remote boot and media mounting
— a dream for IT, and a gift for attackers if misconfigured.

🧱 This Isn’t About “Wasting Access”

It’s about how Microsoft’s own tooling enables unauthenticated SYSTEM
access in environments that are supposed to be secure.

If your only defense is “well, that’s by design,” then the design *is* the
vulnerability.

🔒 BIOS/UEFI Passwords: A Broken Mitigation

Microsoft may argue that setting a BIOS/UEFI password mitigates this
attack. But in practice, this “defense” is deeply flawed:

- **No visual feedback**: Users can’t see what they’re typing — no
asterisks, no characters, nothing.
- **No Caps Lock indicator**: If Caps Lock is on, users won’t know — and
their input silently fails.
- **No support for special characters**: Most firmware restricts input to
basic alphanumeric characters.
- **Short password limits**: Many systems cap passwords at 8–16 characters.
- **No brute-force protection**: Some BIOS/UEFI setups don’t lock out after
failed attempts.

The result? Users get scared, fumble their input, and retreat to normal
boot — where the system is already unlocked and vulnerable. The illusion of
security becomes the attack vector.

If this is the only mitigation, then the system is fundamentally broken.

— Darsh
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **🚨 Public Disclosure: Remote BitLocker Bypass via Intel AMT — SYSTEM Access Without Login** *Darsh Naik (Feb 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")