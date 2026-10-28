---
title: APPLE-SA-10-26-2026-2 iOS 26.7.2 and iPadOS 26.7.2
url: https://seclists.org/fulldisclosure/2026/Oct/40
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:42.581360
---

# APPLE-SA-10-26-2026-2 iOS 26.7.2 and iPadOS 26.7.2

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

[![Previous](/images/left-icon-16x16.png)](39)
[By Date](date.html#40)
[![Next](/images/right-icon-16x16.png)](41)

[![Previous](/images/left-icon-16x16.png)](39)
[By Thread](index.html#40)
[![Next](/images/right-icon-16x16.png)](41)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-2 iOS 26.7.2 and iPadOS 26.7.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:40:52 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-2 iOS 26.7.2 and iPadOS 26.7.2

iOS 26.7.2 and iPadOS 26.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149227.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate Framework
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted image may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86971: an anonymous researcher

AccessorySetupKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A malicious app may be able to access Bluetooth without user
consent
Description: An authentication issue was addressed with improved state
management.
CVE-2026-84493: Meta Red Team X - Nik Tsytsarkin

Accounts
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A malicious application may be able to bypass Privacy
preferences
Description: A logging issue was addressed with improved data redaction.
CVE-2026-113898: Bhaswanth Chigurupati

Accounts
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker with physical access to a trust-paired device may be
able to read and write arbitrary files
Description: A path handling issue was addressed with improved
validation.
CVE-2026-112612: Johnny Franks (@0xjohnny), Daniel, KennethLi, an
anonymous researcher

App Store
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-113914: Jaebin Sim (simjabin () gmail com)

App Store
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A remote attacker may be able to break out of the WebContent
sandbox
Description: This issue was addressed with improved input validation.
CVE-2026-112690: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

Apple Intelligence
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-86920: Johan Wahyudi

AppleAVD
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112416: an anonymous researcher, Meta Red Team X - Nik
Tsytsarkin, Narendra Singh (@_3P1C), Hcamael and 章鱼哥@aipy
(aipyaipy.com), Dohyeon An @PILAB Technology, Inc

AppleAVD
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt process memory
Description: An out-of-bounds write was addressed with improved input
validation.
CVE-2026-112415: Rahul Raj, Hcamael and 章鱼哥@aipy (aipyaipy.com)

Audio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112546: lunar815, Nathaniel Oh (@calysteon), Piotr Jerzy
Duszynski, an anonymous researcher, Surej Sekhar, r3pwnx (@r3pwnx), Lily
Cohl (@GenericCoding)

AVEVideoEncoder
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112705: Marco Schmitt, Andrey Chernykh, Josh Maine of Calif.io

AVEVideoEncoder
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-112689: Franco Belman at Blackwing Intelligence

AVEVideoEncoder
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112470: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112468: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112469: Hcamael and 章鱼哥@aipy (aipyaipy.com)

AVEVideoEncoder
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination o...