---
title: APPLE-SA-10-26-2026-5 macOS Tahoe 26.7.2
url: https://seclists.org/fulldisclosure/2026/Oct/36
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:39.686347
---

# APPLE-SA-10-26-2026-5 macOS Tahoe 26.7.2

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](48)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-5 macOS Tahoe 26.7.2

---

*From*: KC Chambers via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:41:40 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-5 macOS Tahoe 26.7.2

macOS Tahoe 26.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149522.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate Framework
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86971: an anonymous researcher

Accounts
Available for: macOS Tahoe
Impact: A malicious application may be able to bypass Privacy
preferences
Description: A logging issue was addressed with improved data redaction.
CVE-2026-113898: Bhaswanth Chigurupati

AirPort
Available for: macOS Tahoe
Impact: An app may be able to read sensitive location information
Description: An authorization issue was addressed with improved state
management.
CVE-2026-112551: Nguyen Duc Anh of Noventiq, Sindre Sorhus

APFS
Available for: macOS Tahoe
Impact: Mounting a maliciously crafted disk image may cause unexpected
system termination or corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84496: 준우 이, Maher Azzouzi, Jonathan Bar Or (@yo_yo_yo_jbo),
Marco Schmitt, Nathaniel Oh (@calysteon), Aswin Kumar Gokulakannan,
Narendra Singh (@_3P1C), Thanatos Tian (HKPolyU) & wgg with Diffract,
Jakob Pammer, an anonymous researcher, Bhuwan Bhetwal, Kwak kiyong
(@Pwnkai23), Song nuri

APFS
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112525: We Muftihaturrahmah, Aswin Kumar Gokula Kannan, Ruslan
Dautov, Peter Malone

APFS
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112536: Ruslan Dautov, Thomas Guillem, Narendra Singh (@_3P1C),
Kwak Kiyong (@Pwnkai23), Song Nuri, Thanatos Tian (HKPolyU) & wgg with
Diffract

App Store
Available for: macOS Tahoe
Impact: An app may be able to bypass network restrictions
Description: This issue was addressed with improved checks.
CVE-2026-112467: Sindre Sorhus

App Store
Available for: macOS Tahoe
Impact: A remote attacker may be able to break out of the WebContent
sandbox
Description: This issue was addressed with improved input validation.
CVE-2026-112690: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

Apple Intelligence
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-86920: Johan Wahyudi

Apple Neural Engine
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84595: tamdao

Apple Neural Engine
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112696: Jaeyeong Lee

AppleAVD
Available for: macOS Tahoe
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112416: an anonymous researcher, Meta Red Team X - Nik
Tsytsarkin, Narendra Singh (@_3P1C), Hcamael and 章鱼哥@aipy
(aipyaipy.com), Dohyeon An @PILAB Technology, Inc

AppleAVD
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
corrupt process memory
Description: An out-of-bounds write was addressed with improved input
validation.
CVE-2026-112415: Rahul Raj, Hcamael and 章鱼哥@aipy (aipyaipy.com)

AppleAVD
Available for: macOS Tahoe
Impact: A malicious app may be able to break out of its sandbox
Description: An information leakage was addressed with additional
validation.
CVE-2026-112704: Josh Maine of Calif.io

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: A malicious app may be able to read or write to protected files
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-112539: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

AppleRAID
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-112531: Chanwit Muenprakoddee (ChemIndy)

Archive Utility
Available for: macOS Tahoe
Impact: An attacker with root privileges may be able to access protected
user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-86939: Lance Cain - Senior Security Researcher at SpecterOps
Inc.

ArchiveService
Available for: macOS Tahoe
Impact: An app may bypass Gatekeeper checks
Description: A logic issue was addressed with improved state management.
CVE-2026-86937: YingMuo (@YingMuo) of DEVCORE Research Team, Paul
Montgomery (@nullevent)

ArchiveService
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may bypass Gatekeeper
checks
Description: A logic issue was addressed with improved checks.
CVE-2026-112568: an anonymous researcher

Audio
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112546: lunar815, Nathaniel Oh (@calysteon), Piotr Jerzy
Duszynski, an anonymous researcher, Surej Sekhar, r3pwnx (@r3pwnx), Lily
Cohl (@GenericCoding)

Audio
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with additional entitlement
checks.
CVE-2026-112675: Lakshay Sharma (MrW0r57), Abodi Dawoud

AVEVideoEncoder
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112705: Marco Schmitt, Andrey Chernykh, Josh Maine of Calif.io

AVEVideoEncoder
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-112689: Franco Belman at Blackwing Intelligence

AVEVideoEncoder
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112470: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112468: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112469: Hcamael an...