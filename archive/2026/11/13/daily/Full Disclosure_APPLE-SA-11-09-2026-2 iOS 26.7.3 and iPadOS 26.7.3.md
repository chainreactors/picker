---
title: APPLE-SA-11-09-2026-2 iOS 26.7.3 and iPadOS 26.7.3
url: https://seclists.org/fulldisclosure/2026/Nov/25
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.480697
---

# APPLE-SA-11-09-2026-2 iOS 26.7.3 and iPadOS 26.7.3

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-2 iOS 26.7.3 and iPadOS 26.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:05:14 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-2 iOS 26.7.3 and iPadOS 26.7.3

iOS 26.7.3 and iPadOS 26.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149716.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

Bluetooth
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

Messages
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

rapportd
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

This update is available through iTunes and Software Update on your iOS
device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes from
https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is presented
to the user when the iOS device is docked. We recommend applying the
update immediately if possible. Selecting Don't Install will present the
option the next time you connect your iOS device.

The automatic update process may take up to a week depending on the
day that iTunes or the device checks for updates. You may manually
obtain the update via the Check for Updates button within iTunes, or
the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About.
* The version after applying this update will be "iOS 26.7.3 and iPadOS
26.7.3".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryPB4ACgkQ4Ifiq8DH
7PXYag/+PMESTE8NlyoMlXmKvN0HtIH0SAp8h+rVY8JoFAzvwzqyHcL9nsqINxv9
pGuU0KDANmgIZCb7jXtZkx1JkENx9GgbKwW8rpc4804czzrJzHNmGZwG3Ose8RmN
nWlUpDY7M7KxW0wrhp18n3O/YaIQ99PhnnWYLWa4KzSGi7cnxSuFma8+TK7BLYvg
9qa0QAVOBGVPn3b7mzDif6WmRG5lurB276YpB+TcGHHKC3lBDOCWimCUgFdu3j9A
2LcQNzbNeX2i9uBlOxYDxr6cKPjrWwWngJHskMhjwxkLu3F8Vwe0++hCajNwawFO
imgvTx5IeFobB4FYg4s663mlHaMYEZ75jU/iEhSrr7hWPYcadFOA0Mz7zagX9aR7
fFQLzDzskMcSldffDlHPUVqS1HF5ctXzykGtAmskBEWoFITTqJbseHaGsPCrsuRC
TBbh7wh0OdgH+QQF50pYvmHgxPMb3P783xVWu7EVsELJCR1i2bV7QnUndryzCrsk
n3tjtEexd32jLp8Qi3lHG9nMIdCK5MRN4JzePrZ9r9ufB4hUv9wuDxm946ix1RwO
ueWB+bNh4Ob0xppV1NeCq9+F7yOZ3M97S2dro7Tgziyd4md6xy3N0PCcq6V5eU7w
7SBEYLuQnn45vCHdM53nyxuCDSY1x2AOBemzXKpeEjubF9etpeI=
=v4+T
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

### Current thread:

* **APPLE-SA-11-09-2026-2 iOS 26.7.3 and iPadOS 26.7.3** *Apple Product Security via Fulldisclosure (Nov 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

...