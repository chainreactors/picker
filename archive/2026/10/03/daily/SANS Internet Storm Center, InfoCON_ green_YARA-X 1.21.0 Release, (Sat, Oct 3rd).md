---
title: YARA-X 1.21.0 Release, (Sat, Oct 3rd)
url: https://isc.sans.edu/diary/rss/33392
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-03
fetch_date: 2026-10-04T07:37:59.106258
---

# YARA-X 1.21.0 Release, (Sat, Oct 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33388)

Click HERE to learn more about classes Didier is teaching for SANS

# [YARA-X 1.21.0 Release](/forums/diary/YARAX%2B1210%2BRelease/33392/)

**Published**: 2026-10-03. **Last Updated**: 2026-10-03 14:40:21 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARAX%2B1210%2BRelease/33392/#comments)

[YARA-X's 1.21.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.21.0) release brings 5 improvements and 4 bugfixes.

One improvement is allowing stdin for CLI option --scan-list.

This allows one to generate a list of folders to scan, and pass it via a pipe. Like this example (Windows) to scan all folders with "sample" in their name:

```

dir /s /b /a:d c:\*samples* | yr.exe scan --scan-list - rules.yara
```

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/YARAX%2B1210%2BRelease/33392/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33388)

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