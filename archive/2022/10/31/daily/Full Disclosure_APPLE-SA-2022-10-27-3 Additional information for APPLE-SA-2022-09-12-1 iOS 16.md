---
title: APPLE-SA-2022-10-27-3 Additional information for APPLE-SA-2022-09-12-1 iOS 16
url: https://seclists.org/fulldisclosure/2022/Oct/39
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:07.564073
---

# APPLE-SA-2022-10-27-3 Additional information for APPLE-SA-2022-09-12-1 iOS 16

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

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
[![Next](/images/right-icon-16x16.png)](40)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
[![Next](/images/right-icon-16x16.png)](40)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-3 Additional information for APPLE-SA-2022-09-12-1 iOS 16

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:16 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-3 Additional information for APPLE-SA-2022-09-12-1 iOS 16

iOS 16 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213446.

Accelerate Framework
Available for: iPhone 8 and later
Impact: Processing a maliciously crafted image may lead to arbitrary
code execution
Description: A memory consumption issue was addressed with improved
memory handling.
CVE-2022-42795: ryuzaki
Entry added October 27, 2022

AppleAVD
Available for: iPhone 8 and later
Impact: An app may be able to cause a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32827: Antonio Zekic (@antoniozekic), Natalie Silvanovich of
Google Project Zero, and an anonymous researcher
Entry added October 27, 2022

AppleAVD
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: This issue was addressed with improved checks.
CVE-2022-32907: Natalie Silvanovich of Google Project Zero, Antonio
Zekic (@antoniozekic) and John Aakerblom (@jaakerblom), ABC Research
s.r.o, Yinyi Wu, Tommaso Bianco (@cutesmilee__)
Entry added October 27, 2022

Apple Neural Engine
Available for: iPhone 8 and later
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2022-32858: Mohamed Ghannam (@_simo36)
Entry added October 27, 2022

Apple Neural Engine
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32898: Mohamed Ghannam (@_simo36)
CVE-2022-32899: Mohamed Ghannam (@_simo36)
CVE-2022-32889: Mohamed Ghannam (@_simo36)
Entry added October 27, 2022

Apple TV
Available for: iPhone 8 and later
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved handling of
caches.
CVE-2022-32909: Csaba Fitzl (@theevilbit) of Offensive Security
Entry added October 27, 2022

Contacts
Available for: iPhone 8 and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2022-32854: Holger Fuhrmannek of Deutsche Telekom Security

Crash Reporter
Available for: iPhone 8 and later
Impact: A user with physical access to an iOS device may be able to
read past diagnostic logs
Description: This issue was addressed with improved data protection.
CVE-2022-32867: Kshitij Kumar and Jai Musunuri of Crowdstrike
Entry added October 27, 2022

DriverKit
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32865: Linus Henze of Pinauten GmbH (pinauten.de)
Entry added October 27, 2022

Exchange
Available for: iPhone 8 and later
Impact: A user in a privileged network position may be able to
intercept mail credentials
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32928: an anonymous researcher
Entry added October 27, 2022

GPU Drivers
Available for: iPhone 8 and later
Impact: An application may be able to execute arbitrary code with
kernel privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-26744: an anonymous researcher
Entry added October 27, 2022

GPU Drivers
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32903: an anonymous researcher
Entry added October 27, 2022

ImageIO
Available for: iPhone 8 and later
Impact: Processing an image may lead to a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2022-1622
Entry added October 27, 2022

Image Processing
Available for: iPhone 8 and later
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2022-32913: Yiğit Can YILMAZ (@yilmazcanyigit)
Entry added October 27, 2022

IOGPUFamily
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32887: an anonymous researcher
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32914: Zweig of Kunlun Lab
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32866: Linus Henze of Pinauten GmbH (pinauten.de)
CVE-2022-32911: Zweig of Kunlun Lab
Entry updated October 27, 2022

Kernel
Available for: iPhone 8 and later
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-32864: Linus Henze of Pinauten GmbH (pinauten.de)

Kernel
Available for: iPhone 8 and later
Impact: An application may be able to execute arbitrary code with
kernel privileges.
Description: The issue was addressed with improved bounds checks.
CVE-2022-32917: an anonymous researcher

Maps
Available for: iPhone 8 and later
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32883: Ron Masas, breakpointhq.com

MediaLibrary
Available for: iPhone 8 and later
Impact: A user may be able to elevate privileges
Description: A memory corruption issue was addressed with improved
input validation.
CVE-2022-32908: an anonymous researcher

Notifications
Available for: iPhone 8 and later
Impact: A user with physical access to a device may be able to access
contacts from the lock screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-32879: Ubeydullah Sümer
Entry added October 27, 2022

Photos
Available for: iPhone 8 and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved data protection.
CVE-2022-32918: an anonymous researcher, Jugal Goradia of Aastha
Technologies, Srijan Shivam Mishra of The Hack Report, Evan Ricafort
(evanricafort.com) of Invalid Web Security, Amod Raghunath Patwardhan
of Pune, India, Ashwani Rajput of Nagarro Software Pvt. Ltd
Entry added October 27, 2022

Safari
Available for: iPhone 8 and later
Impact: Visiting a malicious website may lead to address bar spoofing
Description: This issue was addressed with improved checks.
CVE-2022-32795: Narendra Bhati of ...