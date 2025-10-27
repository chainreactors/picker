---
title: APPLE-SA-09-16-2024-2 macOS Sequoia 15
url: https://seclists.org/fulldisclosure/2024/Sep/33
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:31.591483
---

# APPLE-SA-09-16-2024-2 macOS Sequoia 15

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](34)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-2 macOS Sequoia 15

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:06:25 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-2 macOS Sequoia 15

macOS Sequoia 15 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121238.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to leak sensitive user information
Description: The issue was addressed with improved checks.
CVE-2024-44129

Accounts
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved permissions logic.
CVE-2024-44153: Mickey Jin (@patch1t)

Accounts
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-44188: Bohdan Stasiuk (@Bohdan_Stasiuk)

APFS
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: A malicious app with root privileges may be able to modify the
contents of system files
Description: The issue was addressed with improved checks.
CVE-2024-40825: Pedro Tôrres (@t0rr3sp3dr0)

APNs
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app with root privileges may be able to access private
information
Description: This issue was addressed with improved data protection.
CVE-2024-44130

App Intents
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to access sensitive data logged when a
shortcut fails to launch another app
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44182: Kirin (@Pwnrin)

AppleGraphicsControl
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: A memory initialization issue was addressed with improved
memory handling.
CVE-2024-44154: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppleGraphicsControl
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2024-40845: Pwn2car working with Trend Micro Zero Day Initiative
CVE-2024-40846: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2024-44164: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-40837: Kirin (@Pwnrin)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to access sensitive user data
Description: The issue was addressed with additional code-signing
restrictions.
CVE-2024-40847: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An attacker may be able to read sensitive information
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40848: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An app may be able to modify protected parts of the file system
Description: A library injection issue was addressed with additional
restrictions.
CVE-2024-44168: Claudio Bozzato and Francesco Benvenuto of Cisco Talos

AppleVA
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: An application may be able to read restricted memory
Description: The issue was addressed with improved memory handling.
CVE-2024-27860: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative
CVE-2024-27861: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppleVA
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and iMac Pro (2017 and later)
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2024-40841: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

AppSandbox
Available for: Mac Studio (2022 and later), iMac (2019 and later), Mac
Pro (2019 and later), Mac Mini (2018 and later), MacBook Air (2020 and
later), MacBook Pro (2018 and later), and ...