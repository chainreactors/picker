---
title: Apple Patches iOS and macOS, (Mon, Aug 17th)
url: https://isc.sans.edu/diary/rss/33254
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-17
fetch_date: 2026-08-18T02:53:41.133937
---

# Apple Patches iOS and macOS, (Mon, Aug 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33252)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Patches iOS and macOS](/forums/diary/Apple%2BPatches%2BiOS%2Band%2BmacOS/33254/)

**Published**: 2026-08-17. **Last Updated**: 2026-08-17 20:26:39 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Apple%2BPatches%2BiOS%2Band%2BmacOS/33254/#comments)

Apple today released updates for iOS/iPadOS (26 and 18) and macOS 26. This update fixes 108 vulnerabilities and comes about two weeks after the much smaller macOS update that addressed the single screen-sharing vulnerability. This vulnerability did not affect iOS/iPadOS.

None of the vulnerabilities has been exploited so far. There are a few WebKit vulnerabilities, but no standalone Safari patch for older operating systems. 87 of the vulnerabilities affect only iOS 18, making this more of an iOS 18 release than one for the newer operating systems. Only six vulnerabilities affect all three OSs released today. All 6 vulnerabilities affect WebKit.

Apple's vulnerability summary notes that the vulnerabilities patched in today's VisionOS release will be enumerated at a later date.

| iOS 26.6.1 and iPadOS 26.6.1 | iOS 18.7.10 and iPadOS 18.7.10 | macOS Tahoe 26.6.2 |
| --- | --- | --- |
| **CVE-2026-28958:** An app may be able to access sensitive user data.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-28973:** A malicious app may be able to break out of its sandbox.  Affects libc | | |
|  | x |  |
| **CVE-2026-28984:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-28990:** Processing a maliciously crafted image may corrupt process memory.  Affects ImageIO | | |
|  | x |  |
| **CVE-2026-28996:** An app may be able to access sensitive user data.  Affects Storage | | |
|  | x |  |
| **CVE-2026-39868:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-39877:** An app may be able to disclose kernel memory.  Affects IOSkywalkFamily | | |
|  | x |  |
| **CVE-2026-43661:** Processing a maliciously crafted image may corrupt process memory.  Affects ImageIO | | |
|  | x |  |
| **CVE-2026-43663:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43667:** An attacker in a privileged network position may be able to cause a denial-of-service.  Affects AirDrop | | |
|  | x |  |
| **CVE-2026-43673:** Processing a maliciously crafted audio file may corrupt process memory.  Affects CoreAudio | | |
|  | x |  |
| **CVE-2026-43676:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43700:** Processing maliciously crafted web content may disclose sensitive user information.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43701:** A malicious website may be able to process restricted web content outside the sandbox.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43705:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43708:** A malicious website may exfiltrate data cross-origin.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43711:** Processing a maliciously crafted video file may lead to unexpected app termination.  Affects CoreMedia | | |
|  | x |  |
| **CVE-2026-43714:** A malicious app may be able to access protected user data.  Affects Foundation | | |
|  | x |  |
| **CVE-2026-43717:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebRTC | | |
|  | x |  |
| **CVE-2026-43720:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit Canvas | | |
|  | x |  |
| **CVE-2026-43722:** An app may be able to leak sensitive kernel state.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43723:** An app may be able to gain root privileges.  Affects MediaRemote | | |
|  | x |  |
| **CVE-2026-43724:** An app may be able to cause unexpected system termination or write kernel memory.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43725:** A malicious website may be able to process restricted web content outside the sandbox.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43727:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43729:** Processing a maliciously crafted image may corrupt process memory.  Affects Model I/O | | |
|  | x |  |
| **CVE-2026-43731:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43735:** A malicious website may exfiltrate data cross-origin.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43738:** Processing a maliciously crafted asset catalog may result in disclosure of process memory.  Affects CoreUI | | |
|  | x |  |
| **CVE-2026-43742:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43744:** Processing an audio stream in a maliciously crafted media file may terminate the process.  Affects CoreAudio | | |
|  | x |  |
| **CVE-2026-43745:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
|  | x |  |
| **CVE-2026-43754:** An app may be able to leak sensitive kernel state.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43757:** An app may be able to cause unexpected system termination.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43769:** An app may be able to cause unexpected system termination.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43776:** Processing a maliciously crafted file may lead to unexpected app termination or arbitrary code execution.  Affects AppleDouble | | |
|  | x |  |
| **CVE-2026-43778:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43794:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43796:** An app may be able to read a persistent device identifier.  Affects Game Center | | |
|  | x |  |
| **CVE-2026-43797:** An app may be able to access information about a user's contacts.  Affects Contacts | | |
|  | x |  |
| **CVE-2026-43800:** An app may be able to access sensitive user data.  Affects Siri | | |
|  | x |  |
| **CVE-2026-43801:** An app may be able to access sensitive user data.  Affects App Store | | |
|  | x |  |
| **CVE-2026-43802:** An app may be able to cause unexpected system termination.  Affects CoreVideo | | |
|  | x |  |
| **CVE-2026-43803:** A remote attacker may be able to cause unexpected system termination.  Affects CoreAudio | | |
|  | x |  |
| **CVE-2026-43807:** A malicious accessory may be able to cause unexpected app termination.  Affects MobileAccessoryUpdater | | |
|  | x |  |
| **CVE-2026-43810:** A remote user may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | |
|  | x |  |
| **CVE-2026-43811:** An app may be able to modify protected parts of the file system.  Affects Books | | |
|  | x |  |
| **CVE-2026-43812:** An app may be able to cause unexpected system termination.  Affects Pro Res | | |
|  | x |  |
| **CVE-2026-43818:** Processing a maliciously crafted image may lead to arbitrary code execution.  Affects ImageIO | | |
|  | x |  |
| **CVE-2026-43821:** An app may be able to read files outside of its sandbox.  Affects WebKit Process Model |...