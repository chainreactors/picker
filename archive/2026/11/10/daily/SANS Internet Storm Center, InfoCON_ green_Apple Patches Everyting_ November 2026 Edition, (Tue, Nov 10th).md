---
title: Apple Patches Everyting: November 2026 Edition, (Tue, Nov 10th)
url: https://isc.sans.edu/diary/rss/33506
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-10
fetch_date: 2026-11-11T08:35:37.618081
---

# Apple Patches Everyting: November 2026 Edition, (Tue, Nov 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33502)
* [next](/diary/33508)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Apple Patches Everyting: November 2026 Edition](/forums/diary/Apple%2BPatches%2BEveryting%2BNovember%2B2026%2BEdition/33506/)

**Published**: 2026-11-10. **Last Updated**: 2026-11-10 12:48:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Apple%2BPatches%2BEveryting%2BNovember%2B2026%2BEdition/33506/#comments)

On Monday, Apple released updates for iOS/iPadOS, macOS, watchOS, and visionOS. These updates fix nine different vulnerabilities. One of the vulnerabilities, CVE-2026-113971, applies only to iOS/iPadOS version 26. Several of the vulnerabilities apply to Bluetooth issues that may weaken the device pairing process.

The number of vulnerabilities Apple patches remains small, but Apple has increased the cadence of its updates.

| iOS 27.2.1 and iPadOS 27.2.1 | iOS 26.7.3 and iPadOS 26.7.3 | iOS 18.7.12 and iPadOS 18.7.12 | macOS Golden Gate 27.2.1 | macOS Tahoe 26.7.3 | macOS Sequoia 15.8.3 | watchOS 27.2.1 | watchOS 26.6.1 | visionOS 27.2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2026-113960:** A user added to an iMessage group may be able to access messages sent before they joined.  Affects Messages | | | | | | | | |
| x | x |  | x | x | x | x |  | x |
| **CVE-2026-113961:** A remote attacker may be able to join an iMessage group chat and receive its messages.  Affects Messages | | | | | | | | |
| x | x |  | x | x | x | x |  | x |
| **CVE-2026-113963:** An app may be able to access sensitive user data.  Affects App Intents | | | | | | | | |
| x |  |  |  |  |  | x |  | x |
| **CVE-2026-113964:** An attacker in Bluetooth range may be able to bypass the rate limit on pairing code attempts and pair with a device without user interaction.  Affects CoreUtils | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113965:** A malicious Bluetooth device may be able to establish a pairing without user interaction.  Affects CoreUtils | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113968:** An attacker in Bluetooth range may be able to bypass the rate limit on pairing code attempts.  Affects AirPlay | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113969:** An attacker on the same network may be able to bypass the rate limit on AirPlay pairing code attempts.  Affects rapportd | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113970:** An attacker in Bluetooth range may be able to corrupt process memory.  Affects Bluetooth | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113971:** An attacker with physical access may be able to pair a device with an AirPlay receiver from the lock screen.  Affects MediaRemote | | | | | | | | |
|  |  | x |  |  |  |  |  |  |

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [macos](/tag.html?tag=macos) [ipados](/tag.html?tag=ipados) [ios](/tag.html?tag=ios) [apple](/tag.html?tag=apple)

[2 comment(s)](/diary/Apple%2BPatches%2BEveryting%2BNovember%2B2026%2BEdition/33506/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33502)
* [next](/diary/33508)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)