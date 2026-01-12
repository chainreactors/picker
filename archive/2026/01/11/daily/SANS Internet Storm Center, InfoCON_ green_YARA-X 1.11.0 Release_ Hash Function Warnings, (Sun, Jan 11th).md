---
title: YARA-X 1.11.0 Release: Hash Function Warnings, (Sun, Jan 11th)
url: https://isc.sans.edu/diary/rss/32616
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-11
fetch_date: 2026-01-12T03:37:52.649955
---

# YARA-X 1.11.0 Release: Hash Function Warnings, (Sun, Jan 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32614)

# [YARA-X 1.11.0 Release: Hash Function Warnings](/forums/diary/YARAX%2B1110%2BRelease%2BHash%2BFunction%2BWarnings/32616/)

**Published**: 2026-01-11. **Last Updated**: 2026-01-11 11:10:24 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARAX%2B1110%2BRelease%2BHash%2BFunction%2BWarnings/32616/#comments)

[YARA-X's 1.11.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.11.0) release brings a new feature: hash function warnings.

When you write a YARA rule to match a cryptographic hash (either the full file content or a part of it), what's actually going on are string comparisons:

![](https://isc.sans.edu/diaryimages/images/20260111-120140.png)

Function hash.sha256 returns a string (the hexadecimal SHA256 hash it calculated) and that is compared to a literal string that is the hash you want to find.

If you make a mistake in your literal string hash (for example: unintentionally add an extra space), then the match will fail.

But YARA-X will now show a warning like this:

![](https://isc.sans.edu/diaryimages/images/20260111-120202.png)

Another example is where you mixup hashes: you provide a SHA1 literal string hash, and it should be a SHA256.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/YARAX%2B1110%2BRelease%2BHash%2BFunction%2BWarnings/32616/#comments)

* [previous](/diary/32614)

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