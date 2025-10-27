---
title: Scans for RDP Gateways, (Wed, Oct 30th)
url: https://isc.sans.edu/diary/rss/31398
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-31
fetch_date: 2025-10-06T18:57:57.117644
---

# Scans for RDP Gateways, (Wed, Oct 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31390)
* [next](/diary/31400)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Scans for RDP Gateways](/forums/diary/Scans%2Bfor%2BRDP%2BGateways/31398/)

**Published**: 2024-10-30. **Last Updated**: 2024-10-30 23:08:30 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BRDP%2BGateways/31398/#comments)

RDP is one of the most prominent entry points into networks. Ransomware actors have taken down many large networks after initially entering via RDP. Credentials for RDP access are often traded by “initial access brokers".

I noticed today an uptick in scans for "/RDWeb/Pages/en-US/login.aspx" . This is often used to expose RDP gateways, and there are even well-known Google dorks that assist in finding these endpoints. The scans I observed today are spread between several hundred IP addresses, none of which "sticks out" as more frequent than others. This could indicate a large botnet being used to scan for this endpoint.

There are three variations of this URL being used, all with the same effect of detecting the presence of an RDP gateway:

> /RDWeb
> /RDWeb/Pages/en-US/login.aspx
> /RDWeb/Pages/

The first two are used the most, and the third (/RDWeb/Pages/) is used very little.

This data is from a subset of our honeypots that appears particularly attractive to these scans. The idea isn't new, but it appears that some group has "rediscovered" it.

![Graph showing scans per day for RDWeb with a significant increase these last 3 days.](https://isc.sans.edu/diaryimages/images/Screenshot%202024-10-30%20at%207_04_52%E2%80%AFPM.png)

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2Bfor%2BRDP%2BGateways/31398/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31390)
* [next](/diary/31400)

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