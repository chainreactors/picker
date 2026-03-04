---
title: Investigating Windows File System Artifacts Under C:\Windows
url: https://blog.elcomsoft.com/2026/03/investigating-windows-file-system-artifacts-under-cwindows/
source: ElcomSoft blog
date: 2026-03-03
fetch_date: 2026-03-04T04:02:22.051634
---

# Investigating Windows File System Artifacts Under C:\Windows

«…Everything you wanted to know about password recovery, data decryption, mobile & cloud forensics…»

* [Home](/)
* [Categories](/products.html)
  + [General](https://blog.elcomsoft.com/category/general/)
  + [Elcomsoft News](https://blog.elcomsoft.com/category/elcom-news/ "Elcomsoft news")
  + [Mobile](https://blog.elcomsoft.com/category/mobile-devices/ "All about mobile devices and technologies")
  + [Security](https://blog.elcomsoft.com/category/old/security/)
  + [Software](https://blog.elcomsoft.com/category/old/software/)
* [Tags](/events.html)
  + [EIFT](https://blog.elcomsoft.com/tag/eift/ "EIFT")
  + [iOS](https://blog.elcomsoft.com/tag/ios/ "iOS")
  + [Elcomsoft iOS Forensic Toolkit](https://blog.elcomsoft.com/tag/elcomsoft-ios-forensic-toolkit/ "Elcomsoft iOS Forensic Toolkit")
  + [iCloud](https://blog.elcomsoft.com/tag/icloud/ "iCloud")
  + [Elcomsoft Phone Breaker](https://blog.elcomsoft.com/tag/elcomsoft-phone-breaker/ "Elcomsoft Phone Breaker")
  + [EDPR](https://blog.elcomsoft.com/tag/edpr/ "EDPR")
  + [EPB](https://blog.elcomsoft.com/tag/epb/ "EPB")
  + [password recovery](https://blog.elcomsoft.com/tag/password-recovery/ "password recovery")
  + [Apple](https://blog.elcomsoft.com/tag/apple/ "Apple")
  + [checkm8](https://blog.elcomsoft.com/tag/checkm8/ "checkm8")
* [Tips & Tricks](/partners/index.html)
  + [Perfect Acquisition: The True Physical Acquisition](https://blog.elcomsoft.com/2026/02/perfect-acquisition-the-true-physical-acquisition/ "Perfect Acquisition: The True Physical Acquisition")
  + [Perfect Acquisition With Passcode Unlock for A8/A8X Devices](https://blog.elcomsoft.com/2026/02/perfect-acquisition-with-passcode-unlock-for-a8-a8x-devices/ "Perfect Acquisition With Passcode Unlock for A8/A8X Devices")
  + [Introducing Elcomsoft Quick Triage](https://blog.elcomsoft.com/2025/12/introducing-elcomsoft-quick-triage/ "Introducing Elcomsoft Quick Triage")
  + [Breaking Barriers: First Full File System Extraction from Apple TV 4K Running tvOS 26](https://blog.elcomsoft.com/2025/11/breaking-barriers-first-full-file-system-extraction-from-apple-tv-4k-running-tvos-26/ "Breaking Barriers: First Full File System Extraction from Apple TV 4K Running tvOS 26")
  + [Which Versions of iOS Are Supported, and Why "It Depends" Is The Best Answer](https://blog.elcomsoft.com/2025/11/which-versions-of-ios-are-supported-and-why-it-depends-is-the-best-answer/ "Which Versions of iOS Are Supported, and Why \"It Depends\" Is The Best Answer")
  + [Don’t Be a Louvre: How Weak Passwords and Unpatched Software Encourage Breaches](https://blog.elcomsoft.com/2025/11/dont-be-a-louvre-how-weak-passwords-and-unpatched-software-encourage-breaches/ "Don’t Be a Louvre: How Weak Passwords and Unpatched Software Encourage Breaches")
  + [Exploring iPadOS, tvOS and audioOS 17 and 18 Devices: File System and Keychain Extraction](https://blog.elcomsoft.com/2025/11/exploring-ipados-tvos-and-audioos-17-and-18-devices-file-system-and-keychain-extraction/ "Exploring iPadOS, tvOS and audioOS 17 and 18 Devices: File System and Keychain Extraction")
  + [All USB Cables Are Equal, But Some Are More Equal Than Others](https://blog.elcomsoft.com/2025/10/all-usb-cables-are-equal-but-some-are-more-equal-than-others/ "All USB Cables Are Equal, But Some Are More Equal Than Others")
  + [Effective Disk Imaging: Ports, Hubs, and Power](https://blog.elcomsoft.com/2025/10/effective-disk-imaging-ports-hubs-and-power/ "Effective Disk Imaging: Ports, Hubs, and Power")
  + [Extracting Apple Unified Logs](https://blog.elcomsoft.com/2025/10/extracting-apple-unified-logs/ "Extracting Apple Unified Logs")
  + [More...](https://blog.elcomsoft.com/category/tips-tricks/ "More...")
* [Events](/events/)

* [Official site](https://www.elcomsoft.com)
* [About us](https://www.elcomsoft.com/company.html)

[![](https://blog.elcomsoft.com/wp-content/themes/elcomsoft_corp/images/avatars/elcomsoft.png)](/)

* [Home](/)
* [Categories](/products.html)
  + [General](https://blog.elcomsoft.com/category/general/)
  + [Elcomsoft News](https://blog.elcomsoft.com/category/elcom-news/ "Elcomsoft news")
  + [Mobile](https://blog.elcomsoft.com/category/mobile-devices/ "All about mobile devices and technologies")
  + [Security](https://blog.elcomsoft.com/category/old/security/)
  + [Software](https://blog.elcomsoft.com/category/old/software/)
* [Tags](/events.html)
  + [EIFT](https://blog.elcomsoft.com/tag/eift/ "EIFT")
  + [iOS](https://blog.elcomsoft.com/tag/ios/ "iOS")
  + [Elcomsoft iOS Forensic Toolkit](https://blog.elcomsoft.com/tag/elcomsoft-ios-forensic-toolkit/ "Elcomsoft iOS Forensic Toolkit")
  + [iCloud](https://blog.elcomsoft.com/tag/icloud/ "iCloud")
  + [Elcomsoft Phone Breaker](https://blog.elcomsoft.com/tag/elcomsoft-phone-breaker/ "Elcomsoft Phone Breaker")
  + [EDPR](https://blog.elcomsoft.com/tag/edpr/ "EDPR")
  + [EPB](https://blog.elcomsoft.com/tag/epb/ "EPB")
  + [password recovery](https://blog.elcomsoft.com/tag/password-recovery/ "password recovery")
  + [Apple](https://blog.elcomsoft.com/tag/apple/ "Apple")
  + [checkm8](https://blog.elcomsoft.com/tag/checkm8/ "checkm8")
* [Tips & Tricks](/partners/index.html)
  + [Perfect Acquisition: The True Physical Acquisition](https://blog.elcomsoft.com/2026/02/perfect-acquisition-the-true-physical-acquisition/ "Perfect Acquisition: The True Physical Acquisition")
  + [Perfect Acquisition With Passcode Unlock for A8/A8X Devices](https://blog.elcomsoft.com/2026/02/perfect-acquisition-with-passcode-unlock-for-a8-a8x-devices/ "Perfect Acquisition With Passcode Unlock for A8/A8X Devices")
  + [Introducing Elcomsoft Quick Triage](https://blog.elcomsoft.com/2025/12/introducing-elcomsoft-quick-triage/ "Introducing Elcomsoft Quick Triage")
  + [Breaking Barriers: First Full File System Extraction from Apple TV 4K Running tvOS 26](https://blog.elcomsoft.com/2025/11/breaking-barriers-first-full-file-system-extraction-from-apple-tv-4k-running-tvos-26/ "Breaking Barriers: First Full File System Extraction from Apple TV 4K Running tvOS 26")
  + [Which Versions of iOS Are Supported, and Why "It Depends" Is The Best Answer](https://blog.elcomsoft.com/2025/11/which-versions-of-ios-are-supported-and-why-it-depends-is-the-best-answer/ "Which Versions of iOS Are Supported, and Why \"It Depends\" Is The Best Answer")
  + [Don’t Be a Louvre: How Weak Passwords and Unpatched Software Encourage Breaches](https://blog.elcomsoft.com/2025/11/dont-be-a-louvre-how-weak-passwords-and-unpatched-software-encourage-breaches/ "Don’t Be a Louvre: How Weak Passwords and Unpatched Software Encourage Breaches")
  + [Exploring iPadOS, tvOS and audioOS 17 and 18 Devices: File System and Keychain Extraction](https://blog.elcomsoft.com/2025/11/exploring-ipados-tvos-and-audioos-17-and-18-devices-file-system-and-keychain-extraction/ "Exploring iPadOS, tvOS and audioOS 17 and 18 Devices: File System and Keychain Extraction")
  + [All USB Cables Are Equal, But Some Are More Equal Than Others](https://blog.elcomsoft.com/2025/10/all-usb-cables-are-equal-but-some-are-more-equal-than-others/ "All USB Cables Are Equal, But Some Are More Equal Than Others")
  + [Effective Disk Imaging: Ports, Hubs, and Power](https://blog.elcomsoft.com/2025/10/effective-disk-imaging-ports-hubs-and-power/ "Effective Disk Imaging: Ports, Hubs, and Power")
  + [Extracting Apple Unified Logs](https://blog.elcomsoft.com/2025/10/extracting-apple-unified-logs/ "Extracting Apple Unified Logs")
  + [More...](https://blog.elcomsoft.com/category/tips-tricks/ "More...")
* [Events](/products.html)

* [Official site](https://www.elcomsoft.com)
* [About us](https://www.elcomsoft.com/company.html)

|  |  |  |
| --- | --- | --- |
|  |  | [USB Device Forensics on Windows 10 and 11](https://blog.elcomsoft.com/2026/02/usb-device-forensics-on-windows-10-and-11/) » |

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

# Investigating Windows File System Artifacts Under C:\Windows

March 3rd, 2026...