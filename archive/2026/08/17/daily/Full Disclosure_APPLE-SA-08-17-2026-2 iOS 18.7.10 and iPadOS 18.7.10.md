---
title: APPLE-SA-08-17-2026-2 iOS 18.7.10 and iPadOS 18.7.10
url: https://seclists.org/fulldisclosure/2026/Aug/38
source: Full Disclosure
date: 2026-08-17
fetch_date: 2026-08-18T02:53:48.614151
---

# APPLE-SA-08-17-2026-2 iOS 18.7.10 and iPadOS 18.7.10

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-08-17-2026-2 iOS 18.7.10 and iPadOS 18.7.10

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 17 Aug 2026 15:00:58 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-08-17-2026-2 iOS 18.7.10 and iPadOS 18.7.10

iOS 18.7.10 and iPadOS 18.7.10 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/148287.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker with physical access may be able to access sensitive
user data during iPhone Mirroring
Description: This issue was addressed through improved state management.
CVE-2026-64732: Jorge Welch (@jorgwelch)

AirDrop
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in a privileged network position may be able to
cause a denial-of-service
Description: A reachable assertion was addressed with improved input
validation.
CVE-2026-43667: Arash Ale Ebrahim from SCy-Phy research group of CISPA
Helmholtz Center for Information Security

APFS
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote user may be able to cause unexpected system termination
or corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-64695: Narendra Singh (@_3P1C), Peter Malone

App Store
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2026-43801: Rahul Raj

AppleDouble
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination or arbitrary code execution
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-43776: Peter Malone, Nicolas Rabrenovic, Irvin Wang

Audio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-64725: Seonung Park, ALTV!ST (altvi.st/)

AVEVideoEncoder
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A buffer overflow was addressed with improved size
validation.
CVE-2026-64747: Franco Belman at Blackwing Intelligence

AVEVideoEncoder
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-64762: Franco Belman at Blackwing Intelligence, Dun

BackgroundAssets
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to delete files for which it does not have
permission
Description: A permissions issue was addressed with improved validation.
CVE-2026-64707: YingQi Shi (@Mas0nShi) of DBAppSecurity's WeBin lab

Books
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to modify protected parts of the file system
Description: A race condition was addressed with improved checks.
CVE-2026-43811: Rodolphe Brunetti (@eisw0lf) of Lupus Nova

Contacts
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to add contacts without user authorization
Description: An authorization issue was addressed with improved
validation.
CVE-2026-64746: Rodolphe Brunetti (@eisw0lf) of Lupus Nova, Daniel
Febrero

Contacts
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted contact may leak sensitive data
Description: The issue was addressed with improved checks.
CVE-2026-64734: Daniel Williams

Contacts
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access information about a user's contacts
Description: This issue was addressed with improved checks.
CVE-2026-43797: Arni Hardarson (Neonix Security)

CoreAudio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted audio file may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43673: Anonymous working with TrendAI Zero Day Initiative

CoreAudio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43744: ret2happy, Mathis Mansière, an anonymous researcher

CoreAudio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote attacker may be able to cause unexpected system
termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43803: Rahul Raj

CoreMedia
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: A memory corruption issue was addressed with improved
memory handling.
CVE-2026-43711: James Duffy (@0x4A616D657344)

CoreUI
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted asset catalog may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43738: Peter Malone

CoreVideo
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43802: an anonymous researcher

curl
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Authentication credentials may be sent to a server on another
origin
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2026-3784
CVE-2026-3783

Foundation
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A malicious app may be able to access protected user data
Description: The issue was addressed with improved input sanitization.
CVE-2026-43714: an anonymous researcher

FrontBoard
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: This issue was addressed by using HTTPS when sending
information over the network.
CVE-2026-64742: Huỳnh Tấn Ngàn

Game Center
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A malicious app may be able to break out of its sandbox
Description: A parsing issu...