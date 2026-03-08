---
title: YARA-X 1.14.0 Release, (Sat, Mar 7th)
url: https://isc.sans.edu/diary/rss/32774
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-07
fetch_date: 2026-03-08T04:07:58.088000
---

# YARA-X 1.14.0 Release, (Sat, Mar 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32768)

# [YARA-X 1.14.0 Release](/forums/diary/YARAX%2B1140%2BRelease/32774/)

**Published**: 2026-03-07. **Last Updated**: 2026-03-07 09:56:54 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARAX%2B1140%2BRelease/32774/#comments)

[YARA-X's 1.14.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.14.0) release brings 4 improvements and 2 bugfixes.

One of the improvements is a new CLI command: deps.

This command shows you the dependencies of rules.

Here is an example. Rule rule1 has no dependencies, rule rule2 depends on rule rule1 and rule rule3 depends on rule rule2:

![](https://isc.sans.edu/diaryimages/images/20260307-104924.png)

Running the deps command on these rules gives you the dependencies:

![](https://isc.sans.edu/diaryimages/images/20260307-104945.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/YARAX%2B1140%2BRelease/32774/#comments)

* [previous](/diary/32768)

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