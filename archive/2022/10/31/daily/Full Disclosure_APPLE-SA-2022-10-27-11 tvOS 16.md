---
title: APPLE-SA-2022-10-27-11 tvOS 16
url: https://seclists.org/fulldisclosure/2022/Oct/47
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:57.086210
---

# APPLE-SA-2022-10-27-11 tvOS 16

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

[![Previous](/images/left-icon-16x16.png)](46)
[By Date](date.html#47)
[![Next](/images/right-icon-16x16.png)](48)

[![Previous](/images/left-icon-16x16.png)](46)
[By Thread](index.html#47)
[![Next](/images/right-icon-16x16.png)](48)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-11 tvOS 16

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:48 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-11 tvOS 16

tvOS 16 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213487.

Accelerate Framework
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Processing a maliciously crafted image may lead to arbitrary
code execution
Description: A memory consumption issue was addressed with improved
memory handling.
CVE-2022-42795: ryuzaki

AppleAVD
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: This issue was addressed with improved checks.
CVE-2022-32907: Natalie Silvanovich of Google Project Zero, Antonio
Zekic (@antoniozekic) and John Aakerblom (@jaakerblom), ABC Research
s.r.o, Yinyi Wu, Tommaso Bianco (@cutesmilee__)

GPU Drivers
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32903: an anonymous researcher

ImageIO
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Processing an image may lead to a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2022-1622

Image Processing
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2022-32913: Yiğit Can YILMAZ (@yilmazcanyigit)

Image Processing
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: This issue was addressed with improved checks.
CVE-2022-32949: Tingting Yin of Tsinghua University
Entry added October 27, 2022

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-32864: Linus Henze of Pinauten GmbH (pinauten.de)

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32866: Linus Henze of Pinauten GmbH (pinauten.de)
CVE-2022-32911: Zweig of Kunlun Lab

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32914: Zweig of Kunlun Lab

MediaLibrary
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: A user may be able to elevate privileges
Description: A memory corruption issue was addressed with improved
input validation.
CVE-2022-32908: an anonymous researcher

Notifications
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: A user with physical access to a device may be able to access
contacts from the lock screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-32879: Ubeydullah Sümer

Sandbox
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to modify protected parts of the file
system
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32881: Csaba Fitzl (@theevilbit) of Offensive Security

SQLite
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: A remote user may be able to cause a denial-of-service
Description: This issue was addressed with improved checks.
CVE-2021-36690

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
WebKit Bugzilla: 241969
CVE-2022-32886: P1umer(@p1umer), afang(@afang5472),
xmzyshypnc(@xmzyshypnc1)

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
WebKit Bugzilla: 242047
CVE-2022-32888: P1umer (@p1umer)

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 242762
CVE-2022-32912: Jeonghoon Shin (@singi21a) at Theori working with
Trend Micro Zero Day Initiative

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: The issue was addressed with improved UI handling.
WebKit Bugzilla: 242762
CVE-2022-32891: @real_as3617, an anonymous researcher

Wi-Fi
Available for: Apple TV 4K, Apple TV 4K (2nd generation), and Apple
TV HD
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2022-32925: Wang Yu of Cyberserval

Additional recognition

AppleCredentialManager
We would like to acknowledge @jonathandata1 for their assistance.

Identity Services
We would like to acknowledge Joshua Jones for their assistance.

Kernel
We would like to acknowledge an anonymous researcher for their
assistance.

Sandbox
We would like to acknowledge Csaba Fitzl (@theevilbit) of Offensive
Security for their assistance.

UIKit
We would like to acknowledge Aleczander Ewing for their assistance.

WebKit
We would like to acknowledge an anonymous researcher for their
assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting "Settings ->
System -> Software Update -> Update Software."  To check the current
version of software, select "Settings -> General -> About."
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNbKpUACgkQ4RjMIDke
NxmVqQ//euIvh3eN5tjkLRIDWFgteGsdR3O6GXKVcZvCiOI7EdmCksA7/3uIo3m2
wAXO/XJB5GDbxwHpyIlaN6eSlQnAhUTeYuDZGTyyUKwRmyj0oYu0IQw9C1xrGefA
LDEqYiTwx7sQnuC6ijirFdHSO0uM+YEHCm0OZ4v2dGBJKAdIFN/5b0jq6/Y9NnWL
EHSL5BLhOOEBxWoi4K2tbbE+ty8+Zqk0GrUJxaWQ7vCKPD8Ts2sNb7JAAVu5WQ...