---
title: Apple Updates Everything: May 2025 Edition, (Mon, May 12th)
url: https://isc.sans.edu/diary/rss/31942
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-13
fetch_date: 2025-10-06T22:30:46.972188
---

# Apple Updates Everything: May 2025 Edition, (Mon, May 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31940)
* [next](/diary/31946)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Updates Everything: May 2025 Edition](/forums/diary/Apple%2BUpdates%2BEverything%2BMay%2B2025%2BEdition/31942/)

**Published**: 2025-05-12. **Last Updated**: 2025-05-12 20:30:06 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2BEverything%2BMay%2B2025%2BEdition/31942/#comments)

Apple released its expected update for all its operating systems. The update, in addition to providing new features, patches 65 different vulnerabilities. Many of these vulnerabilities affect multiple operating systems within the Apple ecosystem.

Of note is CVE-2025-31200. This vulnerability is already exploited in "targeted attacks". Apple released patches for this vulnerability in mid-April for its current operating Systems (iOS 18, macOS 15, tvOS 18, and visionOS 2). This update includes patches for older versions of macOS and iPadOS/iOS.

| iOS 18.5 and iPadOS 18.5 | iPadOS 17.7.7 | macOS Sequoia 15.5 | macOS Sonoma 14.7.6 | macOS Ventura 13.7.6 | watchOS 11.5 | tvOS 18.5 | visionOS 2.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-24097:** An app may be able to read arbitrary file metadata.  Affects AirDrop | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-24111:** An app may be able to cause unexpected system termination.  Affects Display | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-24142:** An app may be able to access sensitive user data.  Affects Notification Center | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-24144:** An app may be able to leak sensitive kernel state.  Affects Kernel | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2025-24155:** An app may be able to disclose kernel memory.  Affects WebContentFilter | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-24213:** A type confusion issue could lead to memory corruption.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-24220:** An app may be able to read a persistent device identifier.  Affects Sandbox Profiles | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-24222:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects BOM | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-24223:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-24225:** Processing an email may lead to user interface spoofing.  Affects Mail Addressing | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2025-24258:** An app may be able to gain root privileges.  Affects DiskArbitration | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-24259:** An app may be able to retrieve Safari bookmarks without an entitlement check.  Affects Parental Controls | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-24274:** A malicious app may be able to gain root privileges.  Affects Mobile Device Service | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-30440:** An app may be able to bypass ASLR.  Affects Libinfo | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-30442:** An app may be able to gain elevated privileges.  Affects SoftwareUpdate | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-30443:** An app may be able to access user-sensitive data.  Affects Found in Apps | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-30448:** An attacker may be able to turn on sharing of an iCloud folder without authentication.  Affects iCloud Document Sharing | | | | | | | |
| x | x |  | x | x |  |  | x |
| **CVE-2025-30453:** A malicious app may be able to gain root privileges.  Affects DiskArbitration | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-31196:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.  Affects CoreGraphics | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2025-31200:** Processing an audio stream in a maliciously crafted media file may result in code execution. Apple is aware of a report that this issue may have been exploited in an extremely sophisticated attack against specific targeted individuals on versions of iOS released before iOS 18.4.1..  Affects CoreAudio | | | | | | | |
|  |  |  |  |  | x |  |  |
| **CVE-2025-31204:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | | | | | | |
| x |  |  |  |  | x | x | x |
| **CVE-2025-31205:** A malicious website may exfiltrate data cross-origin.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2025-31206:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-31207:** An app may be able to enumerate a user's installed apps.  Affects FrontBoard | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2025-31208:** Parsing a file may lead to an unexpected app termination.  Affects CoreAudio | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-31209:** Parsing a file may lead to disclosure of user information.  Affects CoreGraphics | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-31210:** Processing web content may lead to a denial-of-service.  Affects FaceTime | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2025-31212:** An app may be able to access sensitive user data.  Affects Core Bluetooth | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2025-31213:** An app may be able to access associated usernames and websites in a user's iCloud Keychain.  Affects Security | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2025-31214:** An attacker in a privileged network position may be able to intercept network traffic.  Affects Baseband | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2025-31215:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-31217:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-31218:** An app may be able to observe the hostnames of new network connections.  Affects NetworkExtension | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-31219:** An attacker may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-31220:** A malicious app may be able to read sensitive location information.  Affects Weather | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2025-31221:** A remote attacker may be able to leak memory.  Affects Security | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-31222:** A user may be able to elevate privileges.  Affects mDNSResponder | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2025-31224:** An app may be able to bypass certain Privacy preferences.  Affects Sandbox | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-31225:** Call history from deleted apps may still appear in spotlight search results.  Affects Call History | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2025-31226:** Processing a maliciously crafted image may lead to a denial-of-service.  Affects ImageIO | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-31227:** An attacker wi...