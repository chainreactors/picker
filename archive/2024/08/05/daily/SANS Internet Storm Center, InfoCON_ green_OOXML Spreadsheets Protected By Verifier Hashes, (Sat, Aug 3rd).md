---
title: OOXML Spreadsheets Protected By Verifier Hashes, (Sat, Aug 3rd)
url: https://isc.sans.edu/diary/rss/31072
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-05
fetch_date: 2025-10-06T18:01:29.503794
---

# OOXML Spreadsheets Protected By Verifier Hashes, (Sat, Aug 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31070)
* [next](/diary/31076)

# [OOXML Spreadsheets Protected By Verifier Hashes](/forums/diary/OOXML%2BSpreadsheets%2BProtected%2BBy%2BVerifier%2BHashes/31072/)

**Published**: 2024-08-03. **Last Updated**: 2024-08-04 07:23:41 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/OOXML%2BSpreadsheets%2BProtected%2BBy%2BVerifier%2BHashes/31072/#comments)

When I wrote about the internal file format of protected spreadsheets, I mentioned a simple 16-bit hash for .xls files in diary entry "[16-bit Hash Collisions in .xls Spreadsheets](https://isc.sans.edu/diary/16bit%2BHash%2BCollisions%2Bin%2Bxls%2BSpreadsheets/31066)" and a complex hash based on SHA256 for .xlsx files in diary entry "[Protected OOXML Spreadsheets](https://isc.sans.edu/diary/Protected%2BOOXML%2BSpreadsheets/31070)".

But what happens if you open a protected spreadsheet in OLE format (.xls) and save it in OOXML format (.xlsx)?

In that exceptional case, the XML protection elements in the OOXML file will store the 16-bit hash taken from the OLE file:

![](https://isc.sans.edu/diaryimages/images/20240804-092034.png)

![](https://isc.sans.edu/diaryimages/images/20240804-092059.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/OOXML%2BSpreadsheets%2BProtected%2BBy%2BVerifier%2BHashes/31072/#comments)

* [previous](/diary/31070)
* [next](/diary/31076)

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