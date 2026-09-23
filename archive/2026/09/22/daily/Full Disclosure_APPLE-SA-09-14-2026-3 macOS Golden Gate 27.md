---
title: APPLE-SA-09-14-2026-3 macOS Golden Gate 27
url: https://seclists.org/fulldisclosure/2026/Sep/55
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:25.749115
---

# APPLE-SA-09-14-2026-3 macOS Golden Gate 27

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-14-2026-3 macOS Golden Gate 27

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 14 Sep 2026 15:06:19 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-14-2026-3 macOS Golden Gate 27

macOS Golden Gate 27 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149035.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate Framework
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: Processing a maliciously crafted image may lead to unexpected
process termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86882: Peter Malone

Accessibility
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
CVE-2026-43664: Stuart Wallace, Ilya Andr (andrd3v), Rosyna Keller of
Totally Not Malicious Software, CJ Vana, David Strnadel, Daniel Febrero,
Asaf Cohen, Gongyu Ma (@Mezone0), Jian Lee (@speedyfriend433)

Accounts
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: A malicious application may be able to bypass Privacy
preferences
Description: An authorization issue was addressed with improved state
management.
CVE-2026-65404: Arni Hardarson (Neonix Security), Vinay Kumar Rasala
(Xplo8E) from Appknox, Stuart Wallace, 이재영

APFS
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An application may be able to access restricted files
Description: A permissions issue was addressed with improved path
validation.
CVE-2026-86910: an anonymous researcher

APFS
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84523: Cem Onat Karagun, an anonymous researcher

App Store
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: A local app may be able to read a persistent account identifier
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-86888: Zhongcheng Li (CK01)

AppKit
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-84587: an anonymous researcher

Apple Account
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: A malicious application may be able to leak sensitive user
information
Description: An information disclosure issue was addressed with improved
state management.
CVE-2026-84586: Prashan Samarathunge, Zhongcheng Li (CK01)

Apple Account
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to use the Sign In With Apple authentication
flow to access the user's Apple Account
Description: An authentication issue was addressed with improved state
management.
CVE-2026-20683: Dem0ns (@天府简易信工作室), Abdelhak Kherroubi, Jasminder Pal
Singh, Lehan Dilusha Jayasingha (Sri Lanka)

Apple Intelligence
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to bypass Apple Intelligence security prompts
Description: A permissions issue was addressed with improved state
management.
CVE-2026-84601: Nick Cook, Sentry Flag

Apple Neural Engine
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to cause unexpected system termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-65408: tamdao

AppleAVD
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-65407: Franco Belman at Blackwing Intelligence

AppleDouble
Available for: MacBook Neo (2026), MacBook Air with Apple silicon (2020
and later), MacBook Pro with Apple silicon (2020 and later), iMac with
Apple silicon (2021 and later), Mac mini with Apple silicon (2020 and
later), Mac Studio (2022 and later), and Mac Pro with Apple silicon
(2023)
Impact: Mounting a disk image with maliciously crafted files may lead t...