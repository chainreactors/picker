---
title: Legacy May Kill, (Sun, Aug 3rd)
url: https://isc.sans.edu/diary/rss/32166
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-04
fetch_date: 2025-10-07T00:16:09.135453
---

# Legacy May Kill, (Sun, Aug 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32162)
* [next](/diary/32170)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Legacy May Kill](/forums/diary/Legacy%2BMay%2BKill/32166/)

**Published**: 2025-08-03. **Last Updated**: 2025-08-03 20:13:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Legacy%2BMay%2BKill/32166/#comments)

Just saw something that I thought was long gone. The username "pop3user" is showing up in our telnet/ssh logs. I don't know how long ago it was that I used POP3 to retrieve e-mail from one of my mail servers. IMAP and various webmail systems have long since replaced this classic email protocol. But at least this one attacker is counting on someone still having a "pop3user" configured.

The passwords attempted are the classics "pop3user" and "123456". The sole IP address scanning for this username is 193.32.162.157. The IP address is part of AS47890, which is managed by Unmanaged (I am not making this up..)

> route:          193.32.162.0/24
> origin:         AS47890
> mnt-by:         UNMANAGED
> mnt-by:         ro-btel2-1-mnt
> created:        2022-11-21T17:07:38Z
> last-modified:  2022-11-21T17:07:38Z
> source:         RIPE

The website for unmanaged.uk is blank, the network is probably unmanaged... not a fan of blocklists, but I would consider AS47890 a good candidate for a block.

pop3 still being used (maybe?), unmanaged networks... why are we wasting time trying to worry about 0-days?

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[2 comment(s)](/diary/Legacy%2BMay%2BKill/32166/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32162)
* [next](/diary/32170)

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