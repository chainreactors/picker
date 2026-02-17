---
title: APPLE-SA-02-11-2026-4 macOS Sequoia 15.7.4
url: https://seclists.org/fulldisclosure/2026/Feb/24
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.200112
---

# APPLE-SA-02-11-2026-4 macOS Sequoia 15.7.4

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

# APPLE-SA-02-11-2026-4 macOS Sequoia 15.7.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:04:13 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-4 macOS Sequoia 15.7.4

macOS Sequoia 15.7.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126349.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An injection issue was addressed with improved validation.
CVE-2026-20624: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20625: Mickey Jin (@patch1t), Ryan Dowd (@_rdowd)

Compression
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-43403: Mickey Jin (@patch1t)

CoreAudio
Available for: macOS Sequoia
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

GPU Drivers
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected system termination
or read kernel memory
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2026-20620: Murray Mike

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: macOS Sequoia
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

Kernel
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: This issue was addressed with improved checks.
CVE-2026-20626: Keisuke Hosoda

libexpat
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

libnetcore
Available for: macOS Sequoia
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libxpc
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2026-20667: an anonymous researcher

Mail
Available for: macOS Sequoia
Impact: Turning off "Load remote content in messages” may not apply to
all mail previews
Description: A logic issue was addressed with improved checks.
CVE-2026-20673: an anonymous researcher

Multi-Touch
Available for: macOS Sequoia
Impact: A malicious HID device may cause an unexpected process crash
Description: The issue was addressed with improved bounds checks.
CVE-2025-43533: Google Threat Analysis Group
CVE-2025-46300: Google Threat Analysis Group
CVE-2025-46301: Google Threat Analysis Group
CVE-2025-46302: Google Threat Analysis Group
CVE-2025-46303: Google Threat Analysis Group
CVE-2025-46304: Google Threat Analysis Group
CVE-2025-46305: Google Threat Analysis Group

PackageKit
Available for: macOS Sequoia
Impact: An attacker with root privileges may be able to delete protected
system files
Description: This issue was addressed through improved state management.
CVE-2025-46310: Mickey Jin (@patch1t)

Remote Management
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20614: Gergely Kalman (@gergely_kalman)

Sandbox
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20628: Noah Gregory (wts.dev)

Security
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause a denial-of-service
Description: A logic issue was addressed with improved checks.
CVE-2025-46290: Bing Shi, Wenchao Li and Xiaolong Bai of Alibaba Group,
and Luyi Xing of Indiana University Bloomington

Shortcuts
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20653: Enis Maholli (enismaholli.com)

Siri
Available for: macOS Sequoia
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: An authorization issue was addressed with improved state
management.
CVE-2026-20662: Vivek Dhar, ASI (RM) in Border Security Force, FTR HQ
BSF Kashmir

Spotlight
Available for: macOS Sequoia
Impact: A sandboxed app may be able to access sensitive user data
Description: The issue was addressed with additional restrictions on the
observability of app states.
CVE-2026-20680: an anonymous researcher

Spotlight
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed with improved checks.
CVE-2026-20612: Mickey Jin (@patch1t)

StoreKit
Available for: macOS Sequoia
Impact: An app may be able to identify what other apps a user has
installed
Description: A privacy issue was addressed with improved checks.
CVE-2026-20641: Gongyu Ma (@Mezone0)

System Settings
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20619: Asaf Cohen

UIKit
Available for: macOS Sequoia
Impact: An app may be able to bypass...