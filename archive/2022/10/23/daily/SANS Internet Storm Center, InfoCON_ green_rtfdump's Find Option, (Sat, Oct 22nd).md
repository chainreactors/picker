---
title: rtfdump's Find Option, (Sat, Oct 22nd)
url: https://isc.sans.edu/diary/rss/29174
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-23
fetch_date: 2025-10-03T20:42:28.093796
---

# rtfdump's Find Option, (Sat, Oct 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29170)
* [next](/diary/29176)

# [rtfdump's Find Option](/forums/diary/rtfdumps%2BFind%2BOption/29174/)

**Published**: 2022-10-22. **Last Updated**: 2022-10-22 20:30:51 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/rtfdumps%2BFind%2BOption/29174/#comments)

Due to the nature of the RTF language, malicious RTF files can be very obfuscated.

To the point that my tool [rtfdump.py](https://blog.didierstevens.com/2022/10/22/update-rtfdump-py-version-0-0-12/) and [Philippe](https://twitter.com/decalage2)'s tool [rtfobj](https://github.com/decalage2/oletools/wiki/rtfobj) don't find embedded objects:

![](https://isc.sans.edu/diaryimages/images/20221022-212931.png)

![](https://isc.sans.edu/diaryimages/images/20221022-212957.png)

To analyze a heavily obfuscated RTF maldoc like this one ([1c8cfccd2e45ea898125a62686ee97a1e923dfbbc8652889027d46b04aa5dc75](https://bazaar.abuse.ch/sample/1c8cfccd2e45ea898125a62686ee97a1e923dfbbc8652889027d46b04aa5dc75/)), one needs to use rtfdump.py's different options to select the most suspicious items and try to decode them.

To try to automate part of this manual process, I implemented option -F:

![](https://isc.sans.edu/diaryimages/images/20221022-213018.png)

With option -F, rtfdump searches through all items with hexadecimal strings, tries to decode them (combining -H and -S) looking for OLE files (files that start with D0CF11E0).

You can direct rtfdump to search for other types of files by using option --findcutexpression:

![](https://isc.sans.edu/diaryimages/images/20221022-213035.png)

But here, with option -F, one ole file was found. Let's pipe it into [oledump.py](https://blog.didierstevens.com/programs/oledump-py/):

![](https://isc.sans.edu/diaryimages/images/20221022-213054.png)

It contains one stream. Let's use option --storages to view the storages, and option -E "%CLSID% %CLSIDDESC%" to view the class ids:

![](https://isc.sans.edu/diaryimages/images/20221022-213510.png)

![](https://isc.sans.edu/diaryimages/images/20221022-213539.png)

It's an equation stream. Let's take a look at the content of the stream:

![](https://isc.sans.edu/diaryimages/images/20221022-213557.png)

01 is a line record (IIRC) and 08 is a font record. That's where the [exploit](https://isc.sans.edu/forums/diary/Dissecting%2Ba%2BCVE201711882%2BExploit/24272/) starts:

![](https://isc.sans.edu/diaryimages/images/20221022-213649.png)

![](https://isc.sans.edu/diaryimages/images/20221022-213707.png)

![](https://isc.sans.edu/diaryimages/images/20221022-213740.png)

Let's extract the complete content of this stream, write it to disk, and have [scdbg](http://sandsprite.com/blogs/index.php?uid=7&pid=152) analyze this 32-bit shellcode:

![](https://isc.sans.edu/diaryimages/images/20221022-213757.png)

![](https://isc.sans.edu/diaryimages/images/20221022-213829.png)

The [downloaded file is a PE file: Formbook](https://bazaar.abuse.ch/sample/dbb94e1600394c42f2ded11d1611b02c2536bf0334f3e5ece1fe309b76fdb560/).

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [rtf](/tag.html?tag=rtf) [equation](/tag.html?tag=equation) [formbook](/tag.html?tag=formbook) [scdbg](/tag.html?tag=scdbg)

[0 comment(s)](/diary/rtfdumps%2BFind%2BOption/29174/#comments)

* [previous](/diary/29170)
* [next](/diary/29176)

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