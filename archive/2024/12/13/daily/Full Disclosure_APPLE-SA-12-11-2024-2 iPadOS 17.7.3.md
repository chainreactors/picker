---
title: APPLE-SA-12-11-2024-2 iPadOS 17.7.3
url: https://seclists.org/fulldisclosure/2024/Dec/6
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:41:04.286505
---

# APPLE-SA-12-11-2024-2 iPadOS 17.7.3

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-12-11-2024-2 iPadOS 17.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 16:35:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-12-11-2024-2 iPadOS 17.7.3

iPadOS 17.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121838.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

FontParser
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54486: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54500: Junsung Lee working with Trend Micro Zero Day Initiative

Kernel
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An attacker may be able to create a read-only memory mapping
that can be written to
Description: A race condition was addressed with additional validation.
CVE-2024-54494: sohybbyk

Kernel
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to leak sensitive kernel state
Description: A race condition was addressed with improved locking.
CVE-2024-54510: Joseph Ravichandran (@0xjprx) of MIT CSAIL

Kernel
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44245: an anonymous researcher

libarchive
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing a malicious crafted file may lead to a denial-of-
service
Description: The issue was addressed with improved memory handling.
CVE-2024-44201: Ben Roeder

libexpat
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: A remote attacker may cause an unexpected app termination or
arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-45490

libxpc
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An app may be able to gain elevated privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-44225: 风沐云烟(@binary_fmyy)

Passwords
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An attacker in a privileged network position may be able to
alter network traffic
Description: This issue was addressed by using HTTPS when sending
information over the network.
CVE-2024-54492: Talal Haj Bakry and Tommy Mysk of Mysk Inc. (@mysk_co)

Safari
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: On a device with Private Relay enabled, adding a website to the
Safari Reading List may reveal the originating IP address to the website
Description: The issue was addressed with improved routing of Safari-
originated requests.
CVE-2024-44246: Jacob Braun

SceneKit
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing a maliciously crafted file may lead to a denial of
service
Description: The issue was addressed with improved checks.
CVE-2024-54501: Michael DePlante (@izobashi) of Trend Micro's Zero Day
Initiative

VoiceOver
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: An attacker with physical access to an iPadOS device may be able
to view notification content from the lock screen
Description: The issue was addressed by adding additional logic.
CVE-2024-54485: Abhay Kailasia (@abhay_kailasia) from C-DAC
Thiruvananthapuram India

WebKit
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278497
CVE-2024-54479: Seunghyun Lee

WebKit
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved memory
handling.
WebKit Bugzilla: 282661
CVE-2024-54505: Gary Kwong

Additional recognition

Proximity
We would like to acknowledge Junming C. (@Chapoly1305) and Prof. Qiang
Zeng of George Mason University for their assistance.

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
"iPadOS 17.7.3".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmdaAb4ACgkQX+5d1TXa
IvoPKhAAzKInTF72fCgLwcX1fvzKEVxPIi8u5YGCTG6eCpCMkQdRiOulZPniUTqV
h43iNPCR4kBdjMiEtqzFq66poJrzF4pYIDuonaU3IOLxXmqGkl0XHR6yGk+ufMy+
NKrdKHn/CDUo/6HnBQEBD/zBjChmekE9Cg4fCUatmFmQmS0pFDT9EgLmFan5t40I
GewW+2sHj1GLfF9/rw4379iOruWVG2FJTT2z2DihmEDW+e/d/hwyHFS5VsJ0dSvE
fvBHL5cBJJ6YZZ6AsfSVvt3DLDaw8edY6oiI6+gbHOuFGANdE0IcACHmr+qcMXCl
BCAkity+K5Hq8AWY8J82k0QQhZ6SVzwiCjpM+MUu0C2j9UsU3HA/uRXnjHGKuYUs
LkhldTLQ+8LNZTCAwrNNhjRYimJ7yDvSCYmB5zC6nv0FdlTPvVfNaPVRKXargfQ4
klWNXJ+0R1k7Ncx8uspdrQ4bsu7ou2C16QdiMgupvvPgaxnrq8txFRf+BHjWEwpO
p+xVPo4PmUyTK...