---
title: VLC's Check For Updates: No Updates&#x3f;, (Mon, Dec 5th)
url: https://isc.sans.edu/diary/rss/29300
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-06
fetch_date: 2025-10-04T00:36:17.204723
---

# VLC's Check For Updates: No Updates&#x3f;, (Mon, Dec 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29298)
* [next](/diary/29304)

# [VLC's Check For Updates: No Updates?](/forums/diary/VLCs%2BCheck%2BFor%2BUpdates%2BNo%2BUpdates/29300/)

**Published**: 2022-12-05. **Last Updated**: 2022-12-05 16:58:49 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[3 comment(s)](/diary/VLCs%2BCheck%2BFor%2BUpdates%2BNo%2BUpdates/29300/#comments)

When Johannes mentioned a [VLC update](https://www.videolan.org/security/sb-vlc3018.html) (version 3.0.18) on [Thursday's Stormcast](https://isc.sans.edu/podcastdetail.html?id=8272), I started VLC and let it check for updates: it reported that I had the latest version. But I knew I didn't.

Saturday I checked again, still no updates. So I started Wireshark, let VLC do an update check, and saw this:

![](https://isc.sans.edu/diaryimages/images/20221204-125526.png)

![](https://isc.sans.edu/diaryimages/images/20221204-125602.png)

An HTTP request is made to host update.videolan.org path /vlc/status-win-x64. The reply says 3.0.16 is the latest version.

That's why I get no updates when VLC does the check.

The same is true for 32-bit VLC.

I informed the Videolan team.

Update: the version files are updated:

![](https://isc.sans.edu/diaryimages/images/20221205-153225.png)

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [update](/tag.html?tag=update) [vlc](/tag.html?tag=vlc)

[3 comment(s)](/diary/VLCs%2BCheck%2BFor%2BUpdates%2BNo%2BUpdates/29300/#comments)

* [previous](/diary/29298)
* [next](/diary/29304)

### Comments

Wait, wait, wait... You say VLC servers provide update URL over an unencrypted channel?

#### Pyth0n

#### Dec 5th 2022 2 years ago

Alternatively one can download directly from videolan.org if one doesn't mind that the items are signed by expired keys...

#### viviane

#### Dec 5th 2022 2 years ago

Seems to be at .18 now.

#### Terry

#### Dec 5th 2022 2 years ago

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