---
title: zipdump.py: Metadata Encoding, (Fri, Jul 31st)
url: https://isc.sans.edu/diary/rss/33202
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-31
fetch_date: 2026-08-01T05:13:33.845320
---

# zipdump.py: Metadata Encoding, (Fri, Jul 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33198)

Click HERE to learn more about classes Didier is teaching for SANS

# [zipdump.py: Metadata Encoding](/forums/diary/zipdumppy%2BMetadata%2BEncoding/33202/)

**Published**: 2026-07-31. **Last Updated**: 2026-07-31 09:22:19 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/zipdumppy%2BMetadata%2BEncoding/33202/#comments)

I was asked for help with a problem similar to the following.

Here is a ZIP file, analyzed with [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py):

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-12-13.png)

The filename you see, is in Simplified Chinese:

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-36-07.png)

zipdump.py relies on the zipfile or [pyzipper](https://pypi.org/project/pyzipper/) Python modules to parse the given ZIP file, and have the metadata (filenames and comments) decoded correctly.

If this ZIP file would be corrupt or malformed, so that it can not be parsed by these Python modules, then you can still try to use zipdump -f option to locate individual ZIP records:

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-15-50.png)

As I don't know which encoding has been used for the metadata (filenames and comments), I display the filename as a Python byte string and not as a string. If the filename is simple ASCII, it will be readable (like the extension .vir here), but if it is utf-8, for example Simplified Chinese, then you'll just see hexadecimal values.

And that is why I added a new option: --metadata\_encoding. With this new option, you can specify a codec, that will be used to convert bytes into strings when option -f is used. Like this:

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-20-03.png)

So here I use codec utf-8, because the filename is encoded in utf-8. How do I know this? Well, in the ZIP specification, the metadata is either ASCII (CP437 to be precise) or UTF-8 encoded. So when you check the flags, you'll know which encoding to use:

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-20-52.png)

Flag 0x0800 means that encoding utf-8 is used. I've also added a feature that decodes the flag bits into readable text, as can be seen in the screenshot above.

If you specify another codec, like latin, for this specific ZIP file, the filenames will be decoded incorrectly:

![](https://isc.sans.edu/diaryimages/images/2026-07-30_15-21-36.png)

Option --metadata\_encoding can also be used when you don't use option -f, however, module pyzipper does not support this (there's a [PR](https://github.com/danifus/pyzipper/pull/38)) and in module zipfile the flags take precedence.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/zipdumppy%2BMetadata%2BEncoding/33202/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33198)

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