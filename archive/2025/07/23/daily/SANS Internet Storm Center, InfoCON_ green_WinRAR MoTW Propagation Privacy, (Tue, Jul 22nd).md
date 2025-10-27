---
title: WinRAR MoTW Propagation Privacy, (Tue, Jul 22nd)
url: https://isc.sans.edu/diary/rss/32130
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-23
fetch_date: 2025-10-06T23:51:24.680320
---

# WinRAR MoTW Propagation Privacy, (Tue, Jul 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32128)
* [next](/diary/32136)

# [WinRAR MoTW Propagation Privacy](/forums/diary/WinRAR%2BMoTW%2BPropagation%2BPrivacy/32130/)

**Published**: 2025-07-22. **Last Updated**: 2025-07-22 04:05:56 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/WinRAR%2BMoTW%2BPropagation%2BPrivacy/32130/#comments)

Since WinRAR 7.10, not all Mark-of-The-Web data (stored in the Zone.Identifier Alternate Data Stream) is propagated when you extract a file from an archive.

Take my DidierStevensSuite.zip file that I downloaded with a browser in normal mode. It has the following Zone.Identifier ADS:

![](https://isc.sans.edu/diaryimages/images/20250714-132110.png)

Not only does it have a ZoneId field that indicates the origin of the file (3 = Internet), but it also has ReferredUrl and HostUrl fields that tell use from where the file was downloaded.

If we now open this zip file with WinRAR (version 7.10 or later) and extract one or more files (I extract file AnalyzePESig-crt-x64.exe):

![](https://isc.sans.edu/diaryimages/images/20250714-132200.png)

Many archive utilities like WinRAR will propagate the MoTW information: it means that they copy the Zone.Identifier ADS from the downloaded archive to the extracted files.

But if we take a look at the Zone.Identifier ADS from extracted file AnalyzePESig-crt-x64.exe, we see that the ReferredUrl and HostUrl fields have disappeared:

![](https://isc.sans.edu/diaryimages/images/20250714-132230.png)

That's because since version 7.10, WinRAR has a privacy feature that redacts the Zone.Identifier information: only the ZoneId field is propagated, not the other fields.

This is a default setting that can be disabled (Zone value only):

![](https://isc.sans.edu/diaryimages/images/20250714-132305.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/WinRAR%2BMoTW%2BPropagation%2BPrivacy/32130/#comments)

* [previous](/diary/32128)
* [next](/diary/32136)

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