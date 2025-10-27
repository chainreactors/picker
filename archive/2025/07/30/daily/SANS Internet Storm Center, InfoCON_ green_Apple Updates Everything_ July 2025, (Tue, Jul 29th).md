---
title: Apple Updates Everything: July 2025, (Tue, Jul 29th)
url: https://isc.sans.edu/diary/rss/32154
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-30
fetch_date: 2025-10-06T23:55:39.585971
---

# Apple Updates Everything: July 2025, (Tue, Jul 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32152)
* [next](/diary/32158)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Apple Updates Everything: July 2025](/forums/diary/Apple%2BUpdates%2BEverything%2BJuly%2B2025/32154/)

**Published**: 2025-07-29. **Last Updated**: 2025-07-29 21:24:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BUpdates%2BEverything%2BJuly%2B2025/32154/#comments)

Apple today released updates for iOS, iPadOS, macOS, watchOS, tvOS, and visionOS. This is a feature release, but it includes significant security updates. Apple patches a total of 89 different vulnerabilities. None of these vulnerabilities has been identified as exploited.

Apple's vulnerability descriptions are not very telling. Most vulnerabilities are likely DoS issues, causing a system or individual subsystems to crash. There are a few privilege escalation and sandbox escape vulnerabilities that Apple addressed in this update. Vulnerabilities identified as memory corruption or heap corruption may lead to code execution, but the exact scope is difficult to ascertain from Apple's limited information.

There are a few "interesting" vulnerabilities:

CVE-2025-43217: Privacy Indicators for microphone or camera access may not be correctly displayed. This, likely, refers to the green dot displayed next to the control center, not the physical LED used by some Apple laptops.

CVE-2025-43240: A download's origin may be incorrectly associated. A "Mark of the Web" issue? Apple uses extended file attributes for this. Sadly, no details to review existing downloads.

For macOS, security-only updates are available for versions back to Ventura (macOS 13). For iOS/iPad OS, updates are available for 18 and 17.

| iOS 18.6 and iPadOS 18.6 | iPadOS 17.7.9 | macOS Sequoia 15.6 | macOS Sonoma 14.7.7 | macOS Ventura 13.7.7 | watchOS 11.6 | tvOS 18.6 | visionOS 2.6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-24119:** An app may be able to execute arbitrary code out of its sandbox or with certain elevated privileges.  Affects Finder | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-24188:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects Safari | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-24220:** An app may be able to read a persistent device identifier.  Affects Sandbox Profiles | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-24224:** A remote attacker may be able to cause unexpected system termination.  Affects Kernel | | | | | | | |
|  | x |  |  | x |  |  |  |
| **CVE-2025-31229:** Passcode may be read aloud by VoiceOver.  Affects Accessibility | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2025-31243:** An app may be able to gain root privileges.  Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-31273:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2025-31275:** A sandboxed process may be able to launch any installed app.  Affects MediaRemote | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-31276:** Remote content may be loaded even when the 'Load Remote Images' setting is turned off.  Affects Mail Drafts | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2025-31278:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-31279:** An app may be able to fingerprint the user.  Affects Find My | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2025-31280:** Processing a maliciously crafted file may lead to heap corruption.  Affects Model I/O | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-31281:** Processing a maliciously crafted file may lead to unexpected app termination.  Affects Model I/O | | | | | | | |
| x |  | x |  |  |  | x | x |
| **CVE-2025-43184:** A shortcut may be able to bypass sensitive Shortcuts app settings.  Affects Shortcuts | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-43185:** An app may be able to access protected user data.  Affects Voice Control | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-43186:** Parsing a file may lead to an unexpected app termination.  Affects afclip | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2025-43187:** Running an hdiutil command may unexpectedly execute arbitrary code.  Affects Disk Images | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43188:** A malicious app may be able to gain root privileges.  Affects DiskArbitration | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-43189:** A malicious app may be able to read kernel memory.  Affects WebContentFilter | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2025-43191:** An app may be able to cause a denial-of-service.  Affects Admin Framework | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43192:** Account-driven User Enrollment may still be possible with Lockdown Mode turned on.  Affects Managed Configuration | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2025-43193:** An app may be able to cause a denial-of-service.  Affects SecurityAgent | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43194:** An app may be able to modify protected parts of the file system.  Affects PackageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43195:** An app may be able to access sensitive user data.  Affects CoreServices | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43196:** An app may be able to gain root privileges.  Affects libxpc | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43197:** An app may be able to access sensitive user data.  Affects Single Sign-On | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43198:** An app may be able to access protected user data.  Affects Dock | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2025-43199:** A malicious app may be able to gain root privileges.  Affects Core Services | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43202:** Processing a file may lead to memory corruption.  Affects libnetcore | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2025-43206:** An app may be able to access protected user data.  Affects System Settings | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2025-43209:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects ICU | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-43210:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.  Affects CoreMedia | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2025-43211:** Processing web content may lead to a denial-of-service.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-43212:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2025-43215:** Processing a maliciously crafted image may result in disclosure of process memory.  Affects Model I/O | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2025-43216:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2025-43217:** Privacy Indicators for microphone or camera access may not be correctly displayed.  Affects Accessibility | | | | | | ...