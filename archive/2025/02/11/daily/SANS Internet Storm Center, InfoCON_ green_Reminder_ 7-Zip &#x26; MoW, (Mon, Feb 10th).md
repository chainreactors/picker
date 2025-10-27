---
title: Reminder: 7-Zip &#x26; MoW, (Mon, Feb 10th)
url: https://isc.sans.edu/diary/rss/31668
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-11
fetch_date: 2025-10-06T20:47:40.782357
---

# Reminder: 7-Zip &#x26; MoW, (Mon, Feb 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31666)
* [next](/diary/31674)

# [Reminder: 7-Zip & MoW](/forums/diary/Reminder%2B7Zip%2BMoW/31668/)

**Published**: 2025-02-10. **Last Updated**: 2025-02-10 07:27:53 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Reminder%2B7Zip%2BMoW/31668/#comments)

CVE-2025-0411 is a vulnerability in 7-zip that has been [reported to be exploited in recent attacks](https://www.trendmicro.com/en_us/research/25/a/cve-2025-0411-ukrainian-organizations-targeted.html). The problem is that Mark-of-Web (MoW) isn't propagated correctly: when extracted, a file inside a ZIP file inside another ZIP file will not have the MoW propagated from the outer ZIP file.

That's good to know, but what I personally consider more important to know, is that MoW isn't propagated at all by 7-zip in its default configuration.

I wrote about this a couple years ago in diary entry "[7-Zip & MoW](https://isc.sans.edu/diary/28810)", when this new feature was introduced.

You have to enable MoW propagation in the GUI or via the registry. And that is still the case with the latest versions of 7-zip.

![](https://isc.sans.edu/diaryimages/images/20220703-123213.png)

![](https://isc.sans.edu/diaryimages/images/20220703-122506.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/Reminder%2B7Zip%2BMoW/31668/#comments)

* [previous](/diary/31666)
* [next](/diary/31674)

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