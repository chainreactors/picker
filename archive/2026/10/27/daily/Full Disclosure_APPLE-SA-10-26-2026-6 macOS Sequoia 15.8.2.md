---
title: APPLE-SA-10-26-2026-6 macOS Sequoia 15.8.2
url: https://seclists.org/fulldisclosure/2026/Oct/43
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:41.446890
---

# APPLE-SA-10-26-2026-6 macOS Sequoia 15.8.2

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

[![Previous](/images/left-icon-16x16.png)](42)
[By Date](date.html#43)
[![Next](/images/right-icon-16x16.png)](44)

[![Previous](/images/left-icon-16x16.png)](42)
[By Thread](index.html#43)
[![Next](/images/right-icon-16x16.png)](44)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-6 macOS Sequoia 15.8.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:41:59 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-6 macOS Sequoia 15.8.2

macOS Sequoia 15.8.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149523.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate
Available for: macOS Sequoia
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28991: Seiji Sakurai (@HeapSmasher)

Accelerate Framework
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86971: an anonymous researcher

Accounts
Available for: macOS Sequoia
Impact: A malicious application may be able to bypass Privacy
preferences
Description: A logging issue was addressed with improved data redaction.
CVE-2026-113898: Bhaswanth Chigurupati

afpfs
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause unexpected system
termination or corrupt kernel memory
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-64767: Dave G.

APFS
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112525: We Muftihaturrahmah, Aswin Kumar Gokula Kannan, Ruslan
Dautov, Peter Malone

APFS
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112536: Ruslan Dautov, Thomas Guillem, Narendra Singh (@_3P1C),
Kwak Kiyong (@Pwnkai23), Song Nuri, Thanatos Tian (HKPolyU) & wgg with
Diffract

App Store
Available for: macOS Sequoia
Impact: A remote attacker may be able to break out of the WebContent
sandbox
Description: This issue was addressed with improved input validation.
CVE-2026-112690: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

Apple Intelligence
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-86920: Johan Wahyudi

Apple Neural Engine
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84595: tamdao

Apple Neural Engine
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112696: Jaeyeong Lee

AppleAVD
Available for: macOS Sequoia
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112416: an anonymous researcher, Meta Red Team X - Nik
Tsytsarkin, Narendra Singh (@_3P1C), Hcamael and 章鱼哥@aipy
(aipyaipy.com), Dohyeon An @PILAB Technology, Inc

AppleAVD
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt process memory
Description: An out-of-bounds write was addressed with improved input
validation.
CVE-2026-112415: Rahul Raj, Hcamael and 章鱼哥@aipy (aipyaipy.com)

AppleAVD
Available for: macOS Sequoia
Impact: A malicious app may be able to break out of its sandbox
Description: An information leakage was addressed with additional
validation.
CVE-2026-112704: Josh Maine of Calif.io

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A malicious app may be able to read or write to protected files
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-112539: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

AppleRAID
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-112531: Chanwit Muenprakoddee (ChemIndy)

ArchiveService
Available for: macOS Sequoia
Impact: An app may bypass Gatekeeper checks
Description: A logic issue was addressed with improved state management.
CVE-2026-86937: YingMuo (@YingMuo) of DEVCORE Research Team, Paul
Montgomery (@nullevent)

ArchiveService
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may bypass Gatekeeper
checks
Description: A logic issue was addressed with improved checks.
CVE-2026-112568: an anonymous researcher

Audio
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112546: lunar815, Nathaniel Oh (@calysteon), Piotr Jerzy
Duszynski, an anonymous researcher, Surej Sekhar, r3pwnx (@r3pwnx), Lily
Cohl (@GenericCoding)

Audio
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with additional entitlement
checks.
CVE-2026-112675: Lakshay Sharma (MrW0r57), Abodi Dawoud

AVEVideoEncoder
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112705: Marco Schmitt, Andrey Chernykh, Josh Maine of Calif.io

AVEVideoEncoder
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-112689: Franco Belman at Blackwing Intelligence

AVEVideoEncoder
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112470: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112468: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112469: Hcamael and 章鱼哥@aipy (aipyaipy.com)

AVEVideoEncoder
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2026-112466: Hcamael and 章鱼哥@aipy (aipyaipy.com)

BOM
Available for: macOS Sequoia
Impact: A maliciously crafted ZIP archive may bypass Gatekeeper checks
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-84610: Murray Mike, Andreas Jaegersberger & Ro Achterberg of
Nosebeard Labs

BOM
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to heap
corruption
Description: An out-of-bounds write issue was addressed w...