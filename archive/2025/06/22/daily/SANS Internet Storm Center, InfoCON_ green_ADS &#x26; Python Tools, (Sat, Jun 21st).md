---
title: ADS &#x26; Python Tools, (Sat, Jun 21st)
url: https://isc.sans.edu/diary/rss/32058
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-22
fetch_date: 2025-10-06T22:53:09.201157
---

# ADS &#x26; Python Tools, (Sat, Jun 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32054)
* [next](/diary/32062)

# [ADS & Python Tools](/forums/diary/ADS%2BPython%2BTools/32058/)

**Published**: 2025-06-21. **Last Updated**: 2025-06-21 10:13:41 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/ADS%2BPython%2BTools/32058/#comments)

Ehsaan Mavani talks about Alternate Data Streams (ADS) in diary entry "[Alternate Data Streams ? Adversary Defense Evasion and Detection [Guest Diary]](https://isc.sans.edu/diary/Alternate%2BData%2BStreams%2BAdversary%2BDefense%2BEvasion%2Band%2BDetection%2BGuest%2BDiary/31990/)".

I'm taking this as an opportunity to remind you that Python tools on Windows and an NTFS disk, can access alternate data streams.

Like my tool [cut-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/cut-bytes.py), here I use it to show the content of the Mark-of-the-Web stored inside the Zone.Identifier ADS:

![](https://isc.sans.edu/diaryimages/images/20250621-113910.png)

You just need to type a colon (:) followed by the ADS name after the filename.

I didn't have to code this in Python for Windows, it's default behavior.

I did code ADS features in my [FileScanner tool](https://blog.didierstevens.com/programs/filescanner/). It's not written in Python, but in C for Windows, and I coded features to enumerate and scan alternate data streams.

If you give it a file to scan, it will scan the file content, and also the content of all of its alternate data streams. Like with this download with a MotW:

![](https://isc.sans.edu/diaryimages/images/20250621-113931.png)

![](https://isc.sans.edu/diaryimages/images/20250621-113952.png)

And if you give it a folder or a drive to scan, it will also enumerate and scan all alternate data streams.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/ADS%2BPython%2BTools/32058/#comments)

* [previous](/diary/32054)
* [next](/diary/32062)

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