---
title: X-Request-Purpose: Identifying "research" and bug bounty related scans&#x3f;, (Thu, Oct 30th)
url: https://isc.sans.edu/diary/rss/32436
source: SANS Internet Storm Center, InfoCON: green
date: 2025-10-30
fetch_date: 2025-10-31T03:14:54.115814
---

# X-Request-Purpose: Identifying "research" and bug bounty related scans&#x3f;, (Thu, Oct 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32432)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [X-Request-Purpose: Identifying "research" and bug bounty related scans?](/forums/diary/XRequestPurpose%2BIdentifying%2Bresearch%2Band%2Bbug%2Bbounty%2Brelated%2Bscans/32436/)

**Published**: 2025-10-30. **Last Updated**: 2025-10-30 13:22:19 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/XRequestPurpose%2BIdentifying%2Bresearch%2Band%2Bbug%2Bbounty%2Brelated%2Bscans/32436/#comments)

This week, I noticed some new HTTP request headers that I had not seen before:

> X-Request-Purpose: Research

and

> `X-Hackerone-Research: plusultra
> X-Bugcrowd-Ninja: plusultra
> X-Bug-Hunter: true`

The purpose of these headers appears to be to identify them as being sent as part of a bug bounty. Some companies request the use of these headers as part of their bug bounty. For example, see Web.com's Bugcrowd page [1]. If you see these headers, there is a good chance that the request was sent as part of a bug bounty. At the same time, it is a bit odd that we see these in our honeypots. But some of our honeypots are part of corporate networks, and it is possible that they are in scope for a bug bounty. If the header is genuine, the username of the researcher would be "plusultra". On the other hand, there is no guarantee. Anybody may send this header.

The idea of sending a header like this makes some sense. This way, it is easier for a company to contact a researcher in case the scans are causing any issues. From a defensive point of view, you should probably just ignore these requests. I would not treat them any differently from any request without the header. Blocking requests with these headers does not make a lot of sense, nor does allowing them. Just block (or allow them) based on the remainder of the request.

And, for any website out there that doesn't have it yet: Setting up a /.well-known/security.txt file makes a lot of sense [2].

[1] https://bugcrowd.com/engagements/webdotcom-vdp
[2] https://datatracker.ietf.org/doc/rfc9116/

![x-hackerone-research, x-brugcrowd-ninja, x-bug-hunter headers](https://isc.sans.edu/diaryimages/images/Screenshot%202025-10-30%20at%209_20_36%E2%80%AFAM.png)

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [bugbountry http headers](/tag.html?tag=bugbountry http headers)

[0 comment(s)](/diary/XRequestPurpose%2BIdentifying%2Bresearch%2Band%2Bbug%2Bbounty%2Brelated%2Bscans/32436/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32432)

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