---
title: APPLE-SA-11-09-2026-1 iOS 27.2.1 and iPadOS 27.2.1
url: https://seclists.org/fulldisclosure/2026/Nov/24
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.605220
---

# APPLE-SA-11-09-2026-1 iOS 27.2.1 and iPadOS 27.2.1

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-1 iOS 27.2.1 and iPadOS 27.2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:04:05 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-1 iOS 27.2.1 and iPadOS 27.2.1

iOS 27.2.1 and iPadOS 27.2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149715.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

App Intents
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-113963: László Várady

Bluetooth
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

Messages
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
generation and later
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

rapportd
Available for: iPhone 11 and later, iPad Pro 12.9-inch 4th generation
and later, iPad Pro 11-inch 2nd generation and later, iPad Air 4th
generation and later, iPad 9th generation and later, and iPad mini 6th
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
* The version after applying this update will be "iOS 27.2.1 and iPadOS
27.2.1".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryO+oACgkQ4Ifiq8DH
7PVB0w/7B8C0dM+CLasYq4ddK2/zJz112cQCiFR0fOAj/BENZaB+ZBJleCR+2AB5
kOrdaYZwDRaUlts6Ceap8BCUQZN1mt9pFiFZHnmQHJgZvhz4Sz9LGsJBG5mlDsXQ
65AlLTHKhxxoeH2HsMYCvzDyvMpnfPu7PgKpMdtOVyzglwVFbJqZHfKzLuoc9NFm
dVRGkThmvaKfYUWy8zmoBF2sWiFA+bbYiaJkeqsp04QgDJpipLZi48kvrSbDxWvh
uWGb7df/NA2TB6v8f0ZNZizlN3x+e4eADNPIBsC/Nn0/J/XK80s702Rk/YzVfkOr
wd0ylLy23LbB3ygneEKUlEmE7L5OMuJd9Q8y5rlOU600tRqpv91Koft1OzNoT8p9
fU34EAtzmZH4kpoAsFB65JTJ1ET380p92ZUMJjJbcAWcb4IyFacZEWpn1QDQlBkX
mStLLLW8fxEHW0BuaaDY9i1Kx3zXbtd7iBrP8LTW7cVToW1l5V3Q1uhk5xkdNxqJ
tBKDiVy4z6xZvrcNXZmk98HA4mDbYAMJlR6YOVtktgD8oNuawjOlyi/EHmVlPZSe
g+qYn2UcZruJricFne3sqQE9hSqjHiW8mhIQQgJ+tjtAmHc6eEKNJxkD6fNfDTYk
OrlKQbaUJLZSU1H/97o85ryFB2capJ8atBl8t/VFxwURU60J/uI=
=73gd
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* *...