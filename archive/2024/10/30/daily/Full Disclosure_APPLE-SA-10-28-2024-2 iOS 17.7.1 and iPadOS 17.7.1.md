---
title: APPLE-SA-10-28-2024-2 iOS 17.7.1 and iPadOS 17.7.1
url: https://seclists.org/fulldisclosure/2024/Oct/10
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:20.032950
---

# APPLE-SA-10-28-2024-2 iOS 17.7.1 and iPadOS 17.7.1

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-2 iOS 17.7.1 and iPadOS 17.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:15:52 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-2 iOS 17.7.1 and iPadOS 17.7.1

iOS 17.7.1 and iPadOS 17.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121567.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: The issue was addressed with improved authentication.
CVE-2024-44274: Rizki Maulana (rmrizki.my.id), Matthew Butler, Jake
Derouin

CoreText
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Managed Configuration
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44258: Hichem Maloufi, Christian Mina, Ismail Amzdak

MobileBackup
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: A logic issue was addressed with improved file handling.
CVE-2024-44252: Nimrat Khalsa, Davis Dai, James Gill
(@jjtech@infosec.exchange)

Safari
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Maliciously crafted web content may violate iframe sandboxing
policy
Description: A custom URL scheme handling issue was addressed with
improved input validation.
CVE-2024-44155: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Safari Downloads
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An attacker may be able to misuse a trust relationship to
download malicious content
Description: This issue was addressed through improved state management.
CVE-2024-44259: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

SceneKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: A buffer overflow was addressed with improved size
validation.
CVE-2024-44144: 냥냥

SceneKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to heap
corruption
Description: This issue was addressed with improved checks.
CVE-2024-44218: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Shortcuts
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: A malicious app may use shortcuts to access restricted files
Description: A logic issue was addressed with improved checks.
CVE-2024-44269: an anonymous researcher

Siri
Available for: iPhone XS and later, iPad Pro 13-inch, iP...