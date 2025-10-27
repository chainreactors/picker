---
title: Brute-Force ZIP Password Cracking with zipdump.py: FP Fix, (Sun, Jul 16th)
url: https://isc.sans.edu/diary/rss/30032
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-17
fetch_date: 2025-10-04T11:53:25.033432
---

# Brute-Force ZIP Password Cracking with zipdump.py: FP Fix, (Sun, Jul 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30030)
* [next](/diary/30038)

# [Brute-Force ZIP Password Cracking with zipdump.py: FP Fix](/forums/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy%2BFP%2BFix/30032/)

**Published**: 2023-07-16. **Last Updated**: 2023-07-16 08:22:25 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy%2BFP%2BFix/30032/#comments)

In diary entry "[Brute-Force ZIP Password Cracking with zipdump.py](https://isc.sans.edu/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy/29948)" I wrote the following:

*zipdump can also generated false positives. ZIP files that can be openened with a guessed password through the zipfile/pyzipper API, may still throw an error when the full content is actually read:*

*![](https://isc.sans.edu/diaryimages/images/20230618-095648.png)*

*![](https://isc.sans.edu/diaryimages/images/20230618-100647.png)*

*This is something I will fix in an upcoming version.*

I fixed this in [version 0.0.27](https://blog.didierstevens.com/2023/07/16/update-zipdump-py-version-0-0-27/). Whenever a password is found, zipdump.py will decode the full content of the file to check for CRC32 errors.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy%2BFP%2BFix/30032/#comments)

* [previous](/diary/30030)
* [next](/diary/30038)

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