---
title: Extracting With pngdump.py, (Sun, Jun 8th)
url: https://isc.sans.edu/diary/rss/32022
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-09
fetch_date: 2025-10-06T22:54:39.568661
---

# Extracting With pngdump.py, (Sun, Jun 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32020)
* [next](/diary/32024)

# [Extracting With pngdump.py](/forums/diary/Extracting%2BWith%2Bpngdumppy/32022/)

**Published**: 2025-06-08. **Last Updated**: 2025-06-08 05:16:10 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Extracting%2BWith%2Bpngdumppy/32022/#comments)

Inspired by Xavier's diary entry "[A PNG Image With an Embedded Gift](https://isc.sans.edu/diary/A%2BPNG%2BImage%2BWith%2Ban%2BEmbedded%2BGift/31998/)", I updated my [pngdump.py](https://github.com/DidierStevens/Beta/blob/master/pngdump.py) program to enable the extraction of chunks and extra data (similar to my other analysis tools, like pngdump.py).

Here is the analysis of the trojanized PNG file Xavier discussed:

![](https://isc.sans.edu/diaryimages/images/20250607-181104.png)

Notice that this PNG file has 11 "items": 10 valid items (1 header and 9 chunks) and one invalid item: unexpected data after the terminating chunk (IEND).

This can easily be selected with -s 11:

![](https://isc.sans.edu/diaryimages/images/20250607-181439.png)

That's the appended payload:

![](https://isc.sans.edu/diaryimages/images/20250607-181526.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Extracting%2BWith%2Bpngdumppy/32022/#comments)

* [previous](/diary/32020)
* [next](/diary/32024)

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