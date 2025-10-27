---
title: Extracting Files Embedded Inside Word Documents, (Tue, Dec 3rd)
url: https://isc.sans.edu/diary/rss/31486
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-04
fetch_date: 2025-10-06T19:41:43.465144
---

# Extracting Files Embedded Inside Word Documents, (Tue, Dec 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31484)
* [next](/diary/31488)

# [Extracting Files Embedded Inside Word Documents](/forums/diary/Extracting%2BFiles%2BEmbedded%2BInside%2BWord%2BDocuments/31486/)

**Published**: 2024-12-03. **Last Updated**: 2024-12-03 07:13:50 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Extracting%2BFiles%2BEmbedded%2BInside%2BWord%2BDocuments/31486/#comments)

I found a [sample](https://www.virustotal.com/gui/file/21d66da2e2506afa8d351e3ce34d1f9a4de6d8305168c0c302987710d83a12b9) that is a Word document with an embedded executable. I'll explain how to extract the embedded executable with my tools.

First I check with [file-magic.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/file-magic.py):

![](https://isc.sans.edu/diaryimages/images/20241201-191919.png)

The identification says Word 2007+, so this is an [![](https://en.wikipedia.org/wiki/Office_Open_XML)OOXML](https://en.wikipedia.org/wiki/Office_Open_XML) document. These are ZIP containers that can be analyzed with [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py) to take a look inside:

![](https://isc.sans.edu/diaryimages/images/20241201-191942.png)

Stream 6 (oleObject1.bin) is an OLE object that embeds the executable. There's no need to extract that OLE file from the OOXML container, [oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py) can handle this:

![](https://isc.sans.edu/diaryimages/images/20241201-192002.png)

The O indicator for stream A2 tells us that this stream is the OLE data structure embedding the executable.

Selecting this stream and using option -i gives us info about the OLE contained, and the contained file:

![](https://isc.sans.edu/diaryimages/images/20241201-192058.png)

This metadata gives you the names of the embedded file and it hashes, allowing me to look it up directly on VirusTotal, for example: [3d5fe12c0aa783252431834ed8e370102f47df65165680824b9287faa88e088a](https://www.virustotal.com/gui/file/3d5fe12c0aa783252431834ed8e370102f47df65165680824b9287faa88e088a).

The file can also be extracted with option -e:

![](https://isc.sans.edu/diaryimages/images/20241201-192129.png)

Malicious Word documents like these don't execute the embedded file when the document is opened: that requires social engeneering to entice the use to double-click the embedded file.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Extracting%2BFiles%2BEmbedded%2BInside%2BWord%2BDocuments/31486/#comments)

* [previous](/diary/31484)
* [next](/diary/31488)

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