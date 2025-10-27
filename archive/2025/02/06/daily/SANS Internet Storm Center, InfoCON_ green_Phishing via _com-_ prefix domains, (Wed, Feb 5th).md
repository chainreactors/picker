---
title: Phishing via "com-" prefix domains, (Wed, Feb 5th)
url: https://isc.sans.edu/diary/rss/31654
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-06
fetch_date: 2025-10-06T20:39:43.413426
---

# Phishing via "com-" prefix domains, (Wed, Feb 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31650)
* [next](/diary/31658)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Phishing via "com-" prefix domains](/forums/diary/Phishing%2Bvia%2Bcom%2Bprefix%2Bdomains/31654/)

**Published**: 2025-02-05. **Last Updated**: 2025-02-05 17:50:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Phishing%2Bvia%2Bcom%2Bprefix%2Bdomains/31654/#comments)

Phishing is always a "whack the mole" like game. Attackers come up with new ways to fool victims. Security tools are often a step behind. Messages claiming to collect unpaid tolls are one current common theme among phishing (smishing?) messages. I just received another one today:

![Screenshot of a smishing message claiming to alert the recipient of unpaid tolls](https://isc.sans.edu/diaryimages/images/Screenshot%202025-02-05%20at%2012_24_34%E2%80%AFPM.png)

The FBI's Internet Crime Complaint Center warned of these types of messages last April [1]. The message was pretty easily identified as fraud by the "From" number, a phone number in the Phillipines. But I found the domain clever.

Florida's toll system is commonly referred to as "Sunpass", and the legitimate website is sunpass.com. The scammer attempted to emulate this name by using a domain that starts with "com-". An unsuspecting user may consider this a valid sunpass.com address.

So I looked at our "newly registered domains" data to see how many "com-\*" domains we have, and this prefix looks indeed popular, usually followed by a few random characters:

Here are a few example:

> com-typopn.top
> com-tyuiop.top
> com-uilqsc.top
> com-vfgbnj.top
> com-wsxder.top
> com-xyuoph.top
> com-ywbl.top
> com-yzgv.top
> com-zfrulb.top pish

Looking at the Top 10 TLDs used for these domains, the usual "dirty" gTLDs like "top" and "XYZ" stick out, but "com", "info" and "us" are also included:

| TLD | Count |
| --- | --- |
| top | 16,606 |
| com | 12,293 |
| xyz | 3005 |
| info | 2731 |
| cfd | 2413 |
| vip | 2217 |
| sbs | 1461 |
| xin | 1453 |
| us | 1245 |
| online | 1140 |

The registrations vary over time, but as of November last year, the registrations have increased somewhat.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-02-05%20at%2012_47_31%E2%80%AFPM.png)

Overall, it is likely worthwhile to add a query to your DNS logs to review lookups for these domains. I found 10% of the domains from the last few days in Phishtank. Many of the remaining were confirmed malicious as well. Luckily, many appear to have already been taken down. However, I have not spotted a valid side among the last 1,000 registered domains.

[1] https://www.ic3.gov/PSA/2024/PSA240412

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [toll](/tag.html?tag=toll) [sunpass](/tag.html?tag=sunpass) [domains](/tag.html?tag=domains) [phishing](/tag.html?tag=phishing)

[0 comment(s)](/diary/Phishing%2Bvia%2Bcom%2Bprefix%2Bdomains/31654/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31650)
* [next](/diary/31658)

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