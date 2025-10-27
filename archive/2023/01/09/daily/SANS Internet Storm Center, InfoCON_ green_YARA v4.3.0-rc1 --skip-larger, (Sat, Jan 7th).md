---
title: YARA v4.3.0-rc1 --skip-larger, (Sat, Jan 7th)
url: https://isc.sans.edu/diary/rss/29410
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-09
fetch_date: 2025-10-04T03:22:02.436268
---

# YARA v4.3.0-rc1 --skip-larger, (Sat, Jan 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29408)
* [next](/diary/29412)

# [YARA v4.3.0-rc1 --skip-larger](/forums/diary/YARA%2Bv430rc1%2Bskiplarger/29410/)

**Published**: 2023-01-07. **Last Updated**: 2023-01-08 09:14:22 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARA%2Bv430rc1%2Bskiplarger/29410/#comments)

YARA [release candidate 1 for version 4.3.0](https://github.com/VirusTotal/yara/releases/tag/v4.3.0-rc1) brings a Windows fix for the [--skip-larger option](https://github.com/VirusTotal/yara/pull/1678).

IIRC, the --skip-larger option was introduced about a year ago, and allows one to specify a filesize to skip files. Files larger than the given size would no be scanned during a directory scan.

Unfortunately, this feature was not implemented in the Windows version of YARA, but now it is.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [update](/tag.html?tag=update) [yara](/tag.html?tag=yara)

[0 comment(s)](/diary/YARA%2Bv430rc1%2Bskiplarger/29410/#comments)

* [previous](/diary/29408)
* [next](/diary/29412)

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

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)