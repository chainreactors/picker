---
title: MacOS Patches (and Safari, TVOS, VisionOS, WatchOS), (Fri, Mar 8th)
url: https://isc.sans.edu/diary/rss/30726
source: SANS Internet Storm Center, InfoCON: green
date: 2024-03-09
fetch_date: 2025-10-04T12:12:30.699117
---

# MacOS Patches (and Safari, TVOS, VisionOS, WatchOS), (Fri, Mar 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30722)
* [next](/diary/30730)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [MacOS Patches (and Safari, TVOS, VisionOS, WatchOS)](/forums/diary/MacOS%2BPatches%2Band%2BSafari%2BTVOS%2BVisionOS%2BWatchOS/30726/)

**Published**: 2024-03-08. **Last Updated**: 2024-03-08 00:45:00 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/MacOS%2BPatches%2Band%2BSafari%2BTVOS%2BVisionOS%2BWatchOS/30726/#comments)

After patching iOS and iPadOS a few days ago, Apple patched the rest of its lineup today, most notably macOS. These updates include the two 0-days patched for iOS. Interestingly, we also see three vulnerabilities addressed specifically for VisionOS, Apple's latest operating system. One of the VisionOS vulnerabilities affects Personas, a feature only available in VisionOS.

NOTE: Apple amended its list of vulnerabilities for iOS/iPadOS. Many of the vulnerabilities below also affect iOS. The initial release only noted four different vulnerabilities.

Apple security bulletin URL: https://support.apple.com/en-us/HT201222

| Safari 17.4 | macOS Sonoma 14.4 | macOS Ventura 13.6.5 | macOS Monterey 12.7.4 | watchOS 10.4 | tvOS 17.4 | visionOS 1.1 |
| --- | --- | --- | --- | --- | --- | --- |
| **CVE-2024-23273 [moderate]**  Safari Private Browsing  This issue was addressed through improved state management.  Private Browsing tabs may be accessed without authentication | | | | | | |
| x | x |  |  |  |  |  |
| **CVE-2024-23252 [moderate]**  WebKit  The issue was addressed with improved memory handling.  Processing web content may lead to a denial-of-service | | | | | | |
| x | x |  |  |  |  |  |
| **CVE-2024-23254 [moderate]**  WebKit  The issue was addressed with improved UI handling.  A malicious website may exfiltrate audio data cross-origin | | | | | | |
| x | x |  |  | x | x | x |
| **CVE-2024-23263 [other]**  WebKit  A logic issue was addressed with improved validation.  Processing maliciously crafted web content may prevent Content Security Policy from being enforced | | | | | | |
| x | x |  |  | x | x | x |
| **CVE-2024-23280 [moderate]**  WebKit  An injection issue was addressed with improved validation.  A maliciously crafted webpage may be able to fingerprint the user | | | | | | |
| x | x |  |  | x | x |  |
| **CVE-2024-23284 [other]**  WebKit  A logic issue was addressed with improved state management.  Processing maliciously crafted web content may prevent Content Security Policy from being enforced | | | | | | |
| x | x |  |  | x | x | x |
| **CVE-2024-23291 [moderate]**  Accessibility  A privacy issue was addressed with improved private data redaction for log entries.  A malicious app may be able to observe user data in log entries related to accessibility notifications | | | | | | |
|  | x |  |  | x | x |  |
| **CVE-2024-23276 [moderate]**  Admin Framework  A logic issue was addressed with improved checks.  An app may be able to elevate privileges | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23227 [important]**  Airport  This issue was addressed with improved redaction of sensitive information.  An app may be able to read sensitive location information | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23233 [moderate]**  AppleMobileFileIntegrity  This issue was addressed with improved checks.  Entitlements and privacy permissions granted to this app may be used by a malicious app | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2024-23269 [important]**  AppleMobileFileIntegrity  A downgrade issue affecting Intel-based Mac computers was addressed with additional code-signing restrictions.  An app may be able to modify protected parts of the file system | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23288 [moderate]**  AppleMobileFileIntegrity  This issue was addressed by removing the vulnerable code.  An app may be able to elevate privileges | | | | | | |
|  | x |  |  | x | x |  |
| **CVE-2024-23277 [moderate]**  Bluetooth  The issue was addressed with improved checks.  An attacker in a privileged network position may be able to inject keystrokes by spoofing a keyboard | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2024-23247 [moderate]**  ColorSync  The issue was addressed with improved memory handling.  Processing a file may lead to unexpected app termination or arbitrary code execution | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23248 [moderate]**  ColorSync  The issue was addressed with improved memory handling.  Processing a file may lead to a denial-of-service or potentially disclose memory contents | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2024-23249 [moderate]**  ColorSync  The issue was addressed with improved memory handling.  Processing a file may lead to a denial-of-service or potentially disclose memory contents | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2024-23250 [moderate]**  CoreBluetooth - LE  An access issue was addressed with improved access restrictions.  An app may be able to access Bluetooth-connected microphones without user permission | | | | | | |
|  | x |  |  | x | x |  |
| **CVE-2024-23244 [moderate]**  Dock  A logic issue was addressed with improved restrictions.  An app from a standard user account may be able to escalate privilege after admin user login | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23205 [moderate]**  ExtensionKit  A privacy issue was addressed with improved private data redaction for log entries.  An app may be able to access sensitive user data | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2022-48554 [moderate]**  file  This issue was addressed with improved checks.  Processing a file may lead to a denial-of-service or potentially disclose memory contents | | | | | | |
|  | x |  |  | x | x |  |
| **CVE-2024-23253 [moderate]**  Image Capture  A permissions issue was addressed with additional restrictions.  An app may be able to access a user's Photos Library | | | | | | |
|  | x |  |  |  |  |  |
| **CVE-2024-23270 [important]**  Image Processing  The issue was addressed with improved memory handling.  An app may be able to execute arbitrary code with kernel privileges | | | | | | |
|  | x | x | x |  | x |  |
| **CVE-2024-23257 [important]**  ImageIO  The issue was addressed with improved memory handling.  Processing an image may result in disclosure of process memory | | | | | | |
|  | x | x | x |  |  | x |
| **CVE-2024-23258 [critical]**  ImageIO  An out-of-bounds read was addressed with improved input validation.  Processing an image may lead to arbitrary code execution | | | | | | |
|  | x |  |  |  |  | x |
| **CVE-2024-23286 [critical]**  ImageIO  A buffer overflow issue was addressed with improved memory handling.  Processing an image may lead to arbitrary code execution | | | | | | |
|  | x | x | x | x | x | x |
| **CVE-2024-23234 [important]**  Intel Graphics Driver  An out-of-bounds write issue was addressed with improved input validation.  An app may be able to execute arbitrary code with kernel privileges | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23266 [important]**  Kerberos v5 PAM module  The issue was addressed with improved checks.  An app may be able to modify protected parts of the file system | | | | | | |
|  | x | x | x |  |  |  |
| **CVE-2024-23235 [important]**  Kernel  A race condition was addressed with additional validation.  An app may be able to access user-sensitive data | | | | | | |
|  | x |  |  | x | x | x |
| **CVE-2024-23265 [important]**  Kernel  A memory corruption vulnerability was addressed with improved lock...