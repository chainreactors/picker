---
title: Apple Patches Everything: February 2026, (Wed, Feb 11th)
url: https://isc.sans.edu/diary/rss/32706
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-11
fetch_date: 2026-02-12T04:23:15.004842
---

# Apple Patches Everything: February 2026, (Wed, Feb 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32704)
* [next](/diary/32708)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Apple Patches Everything: February 2026](/forums/diary/Apple%2BPatches%2BEverything%2BFebruary%2B2026/32706/)

**Published**: 2026-02-11. **Last Updated**: 2026-02-11 19:36:59 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BEverything%2BFebruary%2B2026/32706/#comments)

Today, Apple released updates for all of its operating systems (iOS, iPadOS, macOS, tvOS, watchOS, and visionOS). The update fixes 71 distinct vulnerabilities, many of which affect multiple operating systems. Older versions of iOS, iPadOS, and macOS are also updated.

OF special note is CVE-2026-20700. This vulnerability has already been exploited in targeted attacks. It allows attackers who can write to memory to execute code. Two vulnerabilities patched in December are related to the same attack (CVE-2025-14174 and CVE-2025-43529).

Interesting are additional Siri/Voice Over vulnerabilities that allow access to some information on locked devices. This is a recurring issue, and you should probably turn off VoiceOver and Siri on locked devices. Another recurring and likely impossible to completely eliminate threat is applications being able to access data from other applications. To reduce the probability of exploitation, limit the Apps you install on your devices.

| iOS 26.3 and iPadOS 26.3 | iOS 18.7.5 and iPadOS 18.7.5 | macOS Tahoe 26.3 | macOS Sequoia 15.7.4 | macOS Sonoma 14.8.4 | tvOS 26.3 | watchOS 26.3 | visionOS 26.3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43338:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects ImageIO | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-43402:** An app may be able to cause unexpected system termination or corrupt process memory.  Affects WindowServer | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-43403:** An app may be able to access sensitive user data.  Affects Compression | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-43417:** An app may be able to access user-sensitive data.  Affects File Bookmark | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-43537:** Restoring a maliciously crafted backup file may lead to modification of protected system files.  Affects Books | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-46283:** An app may be able to access sensitive user data.  Affects CoreServices | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-46290:** A remote attacker may be able to cause a denial-of-service.  Affects Security | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-46305:** A malicious HID device may cause an unexpected process crash.  Affects Multi-Touch | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2025-46310:** An attacker with root privileges may be able to delete protected system files.  Affects PackageKit | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-20601:** An app may be able to monitor keystrokes without user permission.  Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20602:** An app may be able to cause a denial-of-service.  Affects WindowServer | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20603:** An app with root privileges may be able to access private information.  Affects Notification Center | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20605:** An app may be able to crash a system process.  Affects Voice Control | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-20606:** An app may be able to bypass certain Privacy preferences.  Affects UIKit | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-20608:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-20609:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.  Affects CoreMedia | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20610:** An app may be able to gain root privileges.  Affects Setup Assistant | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20611:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects CoreAudio | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20612:** An app may be able to access sensitive user data.  Affects Spotlight | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20614:** An app may be able to gain root privileges.  Affects Remote Management | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20615:** An app may be able to gain root privileges.  Affects CoreServices | | | | | | | |
| x |  | x |  | x |  |  | x |
| **CVE-2026-20616:** Processing a maliciously crafted USD file may lead to unexpected app termination.  Affects Model I/O | | | | | | | |
|  | x | x |  | x |  |  | x |
| **CVE-2026-20617:** An app may be able to gain root privileges.  Affects CoreServices | | | | | | | |
| x |  | x |  | x | x | x | x |
| **CVE-2026-20618:** An app may be able to access user-sensitive data.  Affects System Settings | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20619:** An app may be able to access sensitive user data.  Affects System Settings | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-20620:** An attacker may be able to cause unexpected system termination or read kernel memory.  Affects GPU Drivers | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20621:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Wi-Fi | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-20623:** An app may be able to access protected user data.  Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20624:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20625:** An app may be able to access sensitive user data.  Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  | x |
| **CVE-2026-20626:** A malicious app may be able to gain root privileges.  Affects Kernel | | | | | | | |
| x |  | x | x |  |  |  | x |
| **CVE-2026-20627:** An app may be able to access sensitive user data.  Affects CoreServices | | | | | | | |
| x |  | x |  | x |  | x | x |
| **CVE-2026-20628:** An app may be able to break out of its sandbox.  Affects Sandbox | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20629:** An app may be able to access user-sensitive data.  Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20630:** An app may be able to access protected user data.  Affects LaunchServices | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20634:** Processing a maliciously crafted image may result in disclosure of process memory.  Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20635:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-20638:** A user with Live Caller ID app extensions turned off could have identifying information leaked to the extensions.  Affects Call History | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-20640:** An attacker with physical access to iPhone may be a...