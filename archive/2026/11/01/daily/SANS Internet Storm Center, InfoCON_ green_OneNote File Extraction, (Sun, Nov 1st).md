---
title: OneNote File Extraction, (Sun, Nov 1st)
url: https://isc.sans.edu/diary/rss/33478
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-01
fetch_date: 2026-11-02T08:33:32.219927
---

# OneNote File Extraction, (Sun, Nov 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33476)

Click HERE to learn more about classes Didier is teaching for SANS

# [OneNote File Extraction](/forums/diary/OneNote%2BFile%2BExtraction/33478/)

**Published**: 2026-11-01. **Last Updated**: 2026-11-01 09:12:23 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/OneNote%2BFile%2BExtraction/33478/#comments)

Recently, I had to extract embedded files from a set of OneNote files (extension .one).

My [onedump.py](https://github.com/DidierStevens/Beta/blob/master/onedump.py) tool can extract individual files, so I would have to run this many times. To avoid this, I added a new feature to my onedump.py tool: producing JSON data. [Several of my tools already have such a feature](https://isc.sans.edu/diary/Overview%2Bof%2BMy%2BTools%2BThat%2BHandle%2BJSON%2BData/31012): they produce JSON data with the content of their analysis results.

onedump's option --jsonoutput produces JSON output with the content of each embedded file found inside the OneNote file. And it can do this for many .one files in one go:

> onedump.py --jsonoutput \*.one

To write these files to disk you can use my [myjson-filter.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/myjson-filter.py) tool, like this:

> onedump.py --jsonoutput \*.one | myjson-filter.py -W hashvir

This will write all the embedded files to disk, their name will be the sha256 hash of their content plus extension .vir (hashvir).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/OneNote%2BFile%2BExtraction/33478/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33476)

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