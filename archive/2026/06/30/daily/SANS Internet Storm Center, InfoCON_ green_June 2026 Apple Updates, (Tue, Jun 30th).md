---
title: June 2026 Apple Updates, (Tue, Jun 30th)
url: https://isc.sans.edu/diary/rss/33114
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-30
fetch_date: 2026-07-01T06:24:32.619879
---

# June 2026 Apple Updates, (Tue, Jun 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33110)
* [next](/diary/33118)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [June 2026 Apple Updates](/forums/diary/June%2B2026%2BApple%2BUpdates/33114/)

**Published**: 2026-06-30. **Last Updated**: 2026-06-30 09:31:27 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/June%2B2026%2BApple%2BUpdates/33114/#comments)

Apple released updates for iOS/iPadOS, macOS, and Safari on Monday. There have been no updates for other Apple operating systems (visionOS, watchOS, tvOS). Usually, Apple updates all products at the same time.

Most of the vulnerabilities affect the web browser (WebKit, libxslt, WebRTC, and Web Extension). Only four of the vulnerabilities are not directly related to web content: Three Kernel issues and one vulnerability in the IOGPUFamily.

None of the vulnerabilities is labeled as "exploited".

| iOS 26.5.2 and iPadOS 26.5.2 | macOS Tahoe 26.5.2 | Safari 26.5.2 |
| --- | --- | --- |
| **CVE-2026-39868:** An app may be able to cause unexpected system termination or corrupt kernel memory.  Affects Kernel | | |
| x | x |  |
| **CVE-2026-43676:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43700:** Processing maliciously crafted web content may disclose sensitive user information.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43701:** A malicious website may be able to process restricted web content outside the sandbox.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43703:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects libxslt | | |
| x | x |  |
| **CVE-2026-43704:** A malicious web extension may be able to cause an unexpected process crash.  Affects Web Extensions | | |
| x | x | x |
| **CVE-2026-43705:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43706:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects libxslt | | |
| x | x |  |
| **CVE-2026-43707:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43708:** A malicious website may exfiltrate data cross-origin.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43712:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43713:** Visiting a website may leak sensitive data.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43715:** Processing maliciously crafted web content may lead to memory corruption.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43716:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43718:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebRTC | | |
| x | x | x |
| **CVE-2026-43720:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit Canvas | | |
| x | x | x |
| **CVE-2026-43721:** A malicious website may be able to silently hijack clipboard data.  Affects WebKit Storage | | |
| x | x | x |
| **CVE-2026-43722:** An app may be able to leak sensitive kernel state.  Affects Kernel | | |
| x | x |  |
| **CVE-2026-43724:** An app may be able to cause unexpected system termination or write kernel memory.  Affects Kernel | | |
| x | x |  |
| **CVE-2026-43725:** A malicious website may be able to process restricted web content outside the sandbox.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43727:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43732:** Processing maliciously crafted web content may disclose sensitive user information.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43735:** A malicious website may exfiltrate data cross-origin.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43740:** Processing maliciously crafted web content may result in the disclosure of process memory.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43742:** Processing maliciously crafted web content may lead to an unexpected process crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43743:** An app may be able to cause unexpected system termination.  Affects IOGPUFamily | | |
| x | x |  |
| **CVE-2026-43745:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebKit | | |
| x | x | x |
| **CVE-2026-43746:** Processing maliciously crafted web content may lead to an unexpected Safari crash.  Affects WebRTC | | |
| x | x | x |

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [iOS ipados macOS](/tag.html?tag=iOS ipados macOS) [apple](/tag.html?tag=apple)

[0 comment(s)](/diary/June%2B2026%2BApple%2BUpdates/33114/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33110)
* [next](/diary/33118)

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