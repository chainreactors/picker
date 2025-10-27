---
title: Web Searches For Archives, (Sun, Sep 14th)
url: https://isc.sans.edu/diary/rss/32282
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-15
fetch_date: 2025-10-02T20:10:19.522042
---

# Web Searches For Archives, (Sun, Sep 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32276)
* [next](/diary/32286)

# [Web Searches For Archives](/forums/diary/Web%2BSearches%2BFor%2BArchives/32282/)

**Published**: 2025-09-14. **Last Updated**: 2025-09-14 21:58:04 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Web%2BSearches%2BFor%2BArchives/32282/#comments)

Johannes wrote a diary entry "[Increasing Searches for ZIP Files](https://isc.sans.edu/diary/Increasing%2BSearches%2Bfor%2BZIP%2BFiles/32242/)" where he analyzed the increase of requests for ZIP files (like backup.zip, web.zip, ...) for our web honeypots.

I took a look at my logs, and noticed that too. But it's not only ZIP files, but other archives too:

|  |
| --- |
| **Type** |
| zip |
| rar |
| 7z |
| gz |
| tar |

I even had requests for .tar.zip files.

And when it comes to backup files, the following non-archive types are also popular requests:

|  |
| --- |
| **Filename** |
| backup.sql |
| backup.json |
| backup.bak |
| backup.sh |

Looking at the User Agent Strings for these requests, none indicated that these scans were performed by researchers.

And comparing the source IPs of these requests with our [researchers list](https://isc.sans.edu/diary/31964): not a single match.

So it's safe to say that these scans are done with malicious intent, and that you should take Johannes' advice and don't have these types of files on your web servers, and even better, have some policy to avoid this.

Update: I also had request for a file with the IPv4 address of my server (like 12.34.56.78.zip).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Web%2BSearches%2BFor%2BArchives/32282/#comments)

* [previous](/diary/32276)
* [next](/diary/32286)

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