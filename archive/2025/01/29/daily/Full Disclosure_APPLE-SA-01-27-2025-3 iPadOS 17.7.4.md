---
title: APPLE-SA-01-27-2025-3 iPadOS 17.7.4
url: https://seclists.org/fulldisclosure/2025/Jan/14
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:51.448718
---

# APPLE-SA-01-27-2025-3 iPadOS 17.7.4

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-3 iPadOS 17.7.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:52:33 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-3 iPadOS 17.7.4

iPadOS 17.7.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122067.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: A remote attacker may cause an unexpected application
termination or arbitrary code execution
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24137: Uri Katz (Oligo Security)

ARKit
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24127: Minghao Lin (@Y1nKoc), babywu, and Xingwei Lin of
Zhejiang University

CoreAudio
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24161: Google Threat Analysis Group
CVE-2025-24160: Google Threat Analysis Group
CVE-2025-24163: Google Threat Analysis Group

CoreMedia
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple(HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreRoutine
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to determine a userâ€™s current location
Description: The issue was addressed with improved checks.
CVE-2025-24102: Kirin (@Pwnrin)

ICU
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-54478: Gary Kwong

ImageIO
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

Kernel
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-24118: Joseph Ravichandran (@0xjprx) of MIT CSAIL

Kernel
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A validation issue was addressed with improved logic.
CVE-2025-24159: pattern-f (@pattern_F_)

LaunchServices
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2025-24117: Michael (Biscuit) Thomas (@biscuit () social lol)

libxslt
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
CVE-2025-24166: Ivan Fratric of Google Project Zero

Managed Configuration
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-24104: Hichem Maloufi, Hakim Boukhadra

QuartzCore
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved checks.
CVE-2024-54497: Anonymous working with Trend Micro Zero Day Initiative

SceneKit
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-24149: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Additional recognition

CoreAudio
We would like to acknowledge Google Threat Analysis Group for their
assistance.

CoreMedia Playback
We would like to acknowledge Song Hyun Bae (@bshyuunn) and Lee Dong Ha
(Who4mI) for their assistance.

Static Linker
We would like to acknowledge Holger Fuhrmannek for their assistance.

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is
presented to the user when the iOS device is docked. We recommend
applying the update immediately if possible. Selecting
Don't Install will present the option the next time you connect
your iOS device.

The automatic update process may take up to a week depending on
the day that iTunes or the device checks for updates. You may
manually obtain the update via the Check for Updates button
within iTunes, or the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version after applying this update will be
"iPadOS 17.7.4".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmeYAQcACgkQX+5d1TXa
IvpSTQ//ZBt4r5R4oae9Hp85WJyDyj9k0hYrraf/p/kKQNF+DCFPTfHIZOykjE6u
vOyyQvi+qRfpE0c0sBJcEfwof2W1fKUInPFwrj7zOZ0sV2W6YCH+0Fx7MGFjkxb5
ujvKoC1fB8HXGm+yiH8m/ApFTjRxZKhEAKJCPMLdmh1EJMRnBu9Dqc62FUq54ibg
kvA9YJZC4CqbwYcteEw1ArexQ511WOwUJhVWuiTYzmAGivIoWtSzUyNWm8OUDXSB
QanLEMngEgVmC0k3qxVmmMNbQ8ArGVUt/JJeK3tOmPLQEOlIWF9lRS5Tx8Gw67M1
48/na0xBFugggNN+WL71Tm5BJrbHT8Ds39SVIr2lEMRL6SVs1mv6sr0TgF93xRXU
kBdwLR1gLfylnfRiz9+M...