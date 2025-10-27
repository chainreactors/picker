---
title: APPLE-SA-09-15-2025-5 macOS Tahoe 26
url: https://seclists.org/fulldisclosure/2025/Sep/53
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:50.217901
---

# APPLE-SA-09-15-2025-5 macOS Tahoe 26

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

[![Previous](/images/left-icon-16x16.png)](52)
[By Date](date.html#53)
[![Next](/images/right-icon-16x16.png)](54)

[![Previous](/images/left-icon-16x16.png)](52)
[By Thread](index.html#53)
[![Next](/images/right-icon-16x16.png)](54)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-5 macOS Tahoe 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:34:18 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-5 macOS Tahoe 26

macOS Tahoe 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125110.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Airport
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to read sensitive location information
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43208: Csaba Fitzl (@theevilbit) of Kandji, Kirin (@Pwnrin)

AMD
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2025-43312: ABC Research s.r.o.

AppKit
Available for: Mac Pro (2019), iMac (27-inch, 2020), MacBook Pro
(16-inch, 2019), and MacBook Pro (13-inch, 2020, Four Thunderbolt 3
ports)
Impact: An app may be able to access protected user data
Description: The issue was resolved by blocking unsigned services from
launching on Intel Macs.
CVE-2025-43321: Mickey Jin (@patch1t)

Apple Neural Engine
Available for: Mac Studio (2022 and later), iMac (2021 and later), Mac
mini (2020 and later), MacBook Air with Apple silicon (2020 and later),
and MacBook Pro with Apple silicon (2020 and later), Mac Pro (2023)
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43344: an anonymous researcher

Apple Online Store Kit
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31268: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access protected user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-43331: Mickey Jin (@patch1t), Kirin (@Pwnrin), Claudio Bozzato
and Francesco Benvenuto of Cisco Talos

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43317: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43340: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access sensitive user data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43337: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

AppSandbox
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43285: Zhongquan Li (@Guluisacat), Mickey Jin (@patch1t)

ATS
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43330: Bilal Siddiqui

Audio
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43346: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Bluetooth
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon (2020 and later), MacBook Pro (16-inch, 2019), MacBook Pro
(13-inch, 2020, Four Thunderbolt 3 ports), and MacBook Pro with Apple
silicon (2020 and later)
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks to prevent
unauthorized actions.
CVE-2025-43307: Dawuge of Shuffle Team

Bluetooth
Available for: Mac Studio (2022 and later), iMac (2020 and later), Mac
Pro (2019 and later), Mac mini (2020 and later), MacBook Air with Apple
silicon...