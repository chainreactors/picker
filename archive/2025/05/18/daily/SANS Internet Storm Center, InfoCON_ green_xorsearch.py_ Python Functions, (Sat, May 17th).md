---
title: xorsearch.py: Python Functions, (Sat, May 17th)
url: https://isc.sans.edu/diary/rss/31858
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-18
fetch_date: 2025-10-06T22:28:00.570284
---

# xorsearch.py: Python Functions, (Sat, May 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31856)
* [next](/diary/31862)

# [xorsearch.py: Python Functions](/forums/diary/xorsearchpy%2BPython%2BFunctions/31858/)

**Published**: 2025-05-17. **Last Updated**: 2025-05-17 09:22:18 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/xorsearchpy%2BPython%2BFunctions/31858/#comments)

A couple years ago I published tool [xorsearch.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xorsearch.py) for this diary entry: "[Small Challenge: A Simple Word Maldoc - Part 4](https://isc.sans.edu/diary/Small%2BChallenge%2BA%2BSimple%2BWord%2BMaldoc%2BPart%2B4/26494)".

It could be used to search for XOR-encoded text:

![](https://isc.sans.edu/diaryimages/images/20200823-204801.png)

This was a beta version, and its user interface was subject to change. The version I released recently is a rewrite, and option -t no longer exists.

To achieve a similar result with the new version of xorsearch.py, one uses now option -P (Python) and provides a Python function that filters out printable text: IsPrintable

![](https://isc.sans.edu/diaryimages/images/20250427-110427.png)

Option -D can then be used to dump the decoded data with an extra newline:

![](https://isc.sans.edu/diaryimages/images/20250427-105854.png)

Here too XOR encoding with key 0x6f reveals the hidden command.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/xorsearchpy%2BPython%2BFunctions/31858/#comments)

* [previous](/diary/31856)
* [next](/diary/31862)

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