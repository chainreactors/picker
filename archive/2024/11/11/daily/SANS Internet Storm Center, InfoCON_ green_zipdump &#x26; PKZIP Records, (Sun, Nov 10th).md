---
title: zipdump &#x26; PKZIP Records, (Sun, Nov 10th)
url: https://isc.sans.edu/diary/rss/31428
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-11
fetch_date: 2025-10-06T19:16:26.890657
---

# zipdump &#x26; PKZIP Records, (Sun, Nov 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31426)
* [next](/diary/31430)

# [zipdump & PKZIP Records](/forums/diary/zipdump%2BPKZIP%2BRecords/31428/)

**Published**: 2024-11-10. **Last Updated**: 2024-11-10 15:14:06 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/zipdump%2BPKZIP%2BRecords/31428/#comments)

In yesterday's diary entry "[zipdump & Evasive ZIP Concatenation](https://isc.sans.edu/diary/zipdump%20%26%20Evasive%20ZIP%20Concatenation/31426)" I showed how one can inspect the PKZIP records that make up a ZIP file.

My tool [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py) can also inspect the data of PKZIP file records, and decompress it (not decrypt it).

To select the data of a PKZIP file record, use option -s data. Here we also use option -a to do a hex-ascii dump of the data:

![](https://isc.sans.edu/diaryimages/images/20241110-084718.png)

When option -d is used (to perform a binary dump), only the raw data is send to stdout, no other metadata:

![](https://isc.sans.edu/diaryimages/images/20241110-085753.png)

And when option -s decompress is used, the data is decompressed (only INFLATE is supported):

![](https://isc.sans.edu/diaryimages/images/20241110-085816.png)

These options could also be helpful for corrupt ZIP files.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/zipdump%2BPKZIP%2BRecords/31428/#comments)

* [previous](/diary/31426)
* [next](/diary/31430)

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