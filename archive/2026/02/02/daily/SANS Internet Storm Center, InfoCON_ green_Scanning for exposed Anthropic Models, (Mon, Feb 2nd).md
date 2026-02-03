---
title: Scanning for exposed Anthropic Models, (Mon, Feb 2nd)
url: https://isc.sans.edu/diary/rss/32674
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-02
fetch_date: 2026-02-03T04:11:08.294792
---

# Scanning for exposed Anthropic Models, (Mon, Feb 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32668)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Scanning for exposed Anthropic Models](/forums/diary/Scanning%2Bfor%2Bexposed%2BAnthropic%2BModels/32674/)

**Published**: 2026-02-02. **Last Updated**: 2026-02-02 15:14:47 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scanning%2Bfor%2Bexposed%2BAnthropic%2BModels/32674/#comments)

Yesterday, a single IP address ([204.76.203.210](/ipinfo.html?ip=204.76.203.210)) scanned a number of our sensors for what looks like an anthropic API node. The IP address is known to be a Tor exit node.

The requests are pretty simple:

> `GET /anthropic/v1/models
> Host: 67.171.182.193:8000
> X-Api-Key: password
> Anthropic-Version: 2023-06-01`

It looks like this is scanning for locally hosted Anthropic models, but it is not clear to me if this would be successful. If anyone has any insights, please let me know. The API Key is a commonly used key in documentation, and not a key that anybody would expect to work.

At the same time, we are also seeing a small increase in requests for "/v1/messages". These requests have been more common in the past, but the URL may be associated with Anthropic (it is, however, somewhat generic, and it is likely other APIs use the same endpoint. These requests originate from [154.83.103.179](/ipinfo.html?ip=154.83.103.179), an IP address with a bit a complex geolocation and routing footprint.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [anthorpic ai](/tag.html?tag=anthorpic ai)

[0 comment(s)](/diary/Scanning%2Bfor%2Bexposed%2BAnthropic%2BModels/32674/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32668)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)