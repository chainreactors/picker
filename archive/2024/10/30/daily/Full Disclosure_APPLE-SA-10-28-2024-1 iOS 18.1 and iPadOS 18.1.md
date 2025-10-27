---
title: APPLE-SA-10-28-2024-1 iOS 18.1 and iPadOS 18.1
url: https://seclists.org/fulldisclosure/2024/Oct/9
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:23.106494
---

# APPLE-SA-10-28-2024-1 iOS 18.1 and iPadOS 18.1

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-1 iOS 18.1 and iPadOS 18.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:15:05 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-1 iOS 18.1 and iPadOS 18.1

iOS 18.1 and iPadOS 18.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121563.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS and later
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: The issue was addressed with improved authentication.
CVE-2024-44274: Rizki Maulana (rmrizki.my.id), Matthew Butler, Jake
Derouin

App Support
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

CoreMedia Playback
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreText
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

IOSurface
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2024-44285: an anonymous researcher

iTunes
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A remote attacker may be able to break out of Web Content
sandbox
Description: A custom URL scheme handling issue was addressed with
improved input validation.
CVE-2024-40867: Ziyi Zhou (@Shanghai Jiao Tong University), Tianxiao Hou
(@Shanghai Jiao Tong University)

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Managed Configuration
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44258: Hichem Maloufi, Christian Mina, Ismail Amzdak

MobileBackup
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: A logic issue was addressed with improved file handling.
CVE-2024-44252: Nimrat Khalsa, Davis Dai, James Gill
(@jjtech@infosec.exchange)

Pro Res
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44277: an anonymous researcher and Yinyi Wu(@_3ndy1) from Dawn
Security Lab of JD.com, Inc.

Safari Downloads
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An attacker may be able to misuse a trust relationship to
download malicious content
Description: This issue was addressed through improved state management.
CVE-2024-44259: Narendra Bhati, Manager of Cyber Securi...