---
title: Microsoft Access VBA, (Mon, May 25th)
url: https://isc.sans.edu/diary/rss/33012
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-25
fetch_date: 2026-05-26T06:11:04.186814
---

# Microsoft Access VBA, (Mon, May 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33010)
* [next](/diary/33014)

Click HERE to learn more about classes Didier is teaching for SANS

# [Microsoft Access VBA](/forums/diary/Microsoft%2BAccess%2BVBA/33012/)

**Published**: 2026-05-25. **Last Updated**: 2026-05-25 14:14:58 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BAccess%2BVBA/33012/#comments)

Microsoft Access files (Microsoft Office's Database) can contain VBA code.

But they are not ole or OOXML files. You can't analyze them with [oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py):

![](https://isc.sans.edu/diaryimages/images/20260525-151257.png)

Neither do they contain an embedded OLE file:

![](https://isc.sans.edu/diaryimages/images/20260525-152941.png)

Microsoft does not publish official documentation for the Microsoft Access file format, like it does for CFB (ole) and OOXML.

That inspired me to add support for VBA compression to my [search-for-compression.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/search-for-compression.py) tool.

search-for-compression.py is a tool that searches through binary files, looking for data that is ZLIB compressed. I've now added the option to search for compressed VBA code too. That is done with option -t:

![](https://isc.sans.edu/diaryimages/images/20260525-155505.png)

There are 3 entries. The first 2 decompress to binary data (01 00 04 ...). These are similar to dir streams in ole files. dir streams specify VBA project properties, project references, and module properties. They can be dumped:

![](https://isc.sans.edu/diaryimages/images/20260525-161133.png)

The 3th one starts with ASCII data (Attritut). This is VBA code that can be selected and dumped:

![](https://isc.sans.edu/diaryimages/images/20260525-155904.png)

This example is simple, because it's just an empty database that I created for this diary entry.

Real samples are a bit more complex. I'll cover some examples in an upcoming diary entry.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Microsoft%2BAccess%2BVBA/33012/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33010)
* [next](/diary/33014)

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