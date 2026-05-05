---
title: DShield Honeypot Update, (Mon, May 4th)
url: https://isc.sans.edu/diary/rss/32948
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-04
fetch_date: 2026-05-05T05:04:09.273963
---

# DShield Honeypot Update, (Mon, May 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/32944)
* [next](/diary/32950)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [DShield Honeypot Update](/forums/diary/DShield%2BHoneypot%2BUpdate/32948/)

**Published**: 2026-05-04. **Last Updated**: 2026-05-04 14:23:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/DShield%2BHoneypot%2BUpdate/32948/#comments)

This week, I will release a few updates to our DShield honeypot. The update should happen automatically if you have "automatic updates" enabled on your system. There will be two major changes:

### Compatibility with Ubuntu 26.04 / new versions of Raspberry Pi OS

Ubuntu released version 26.04 LTS about a week ago. It will pretty much work already, but I made some adjustments if you are using the "minimum server install". 24.04 will continue to be supported. There have been some issues with 26.04, particularly with some tools that were converted to Rust. You will be ok staying with 24.04 LTS for now. Earlier versions of Ubuntu (22.04, 20.04) will no longer be supported.

Whenever you upgrade your operating system to a new major version, I recommend you reinstall the honeypot from scratch. You may want to retain the "dshield.ini" file to simplify the reinstall. Reinstalling from scratch ensures that all required dependencies are installed.

For older Ubuntu versions, Python dependencies make support rather difficult. For in-place upgrades, I will try to maintain compatibility as much as possible, but new installs should use either 24.04 or 26.04.

The next update will also fix any issues with new versions of Raspberry Pi OS. The goal is to maintain compatibility with the 32- and 64-bit versions of "trixie" and "bookworm".  Testing for Raspberry Pi OS is a bit more complex because it requires physical devices. If anybody has a good way to virtualize Raspberry Pi OS: Please let me know :)

### Updating Cowrie

The next update will also include an updated version of Cowrie. We have fallen quite a bit behind, and I hope to add some new features. If you currently do not see any Cowrie (ssh/telnet) logs in your account, please update your API key ("Auth Key"). Some older API keys are not compatible with the current version of Cowrie. Newer keys are random hexadecimal strings, while older keys are base64 encoded random strings.

As always, please use our [contact form](https://isc.sans.edu/contact.html) if you are running into any problems.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [honeypot dshield](/tag.html?tag=honeypot dshield)

[0 comment(s)](/diary/DShield%2BHoneypot%2BUpdate/32948/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32944)
* [next](/diary/32950)

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