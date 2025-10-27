---
title: Tracking Proxy Scans with IPv4.Games, (Thu, Aug 1st)
url: https://isc.sans.edu/diary/rss/31136
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-02
fetch_date: 2025-10-06T18:10:05.817691
---

# Tracking Proxy Scans with IPv4.Games, (Thu, Aug 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31132)
* [next](/diary/31140)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Tracking Proxy Scans with IPv4.Games](/forums/diary/Tracking%2BProxy%2BScans%2Bwith%2BIPv4Games/31136/)

**Published**: 2024-08-01. **Last Updated**: 2024-08-01 17:00:53 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Tracking%2BProxy%2BScans%2Bwith%2BIPv4Games/31136/#comments)

Today, I saw a proxy scan that was a little bit different:

> `http://ipv4.games/claim?name=gang
> http://ipv4.games/claim?name=napucan`

I wasn't familiar with ipv4.games, so of course, I had to check out the site. I liked it for a couple of reasons. First, the design is just how I think ISC should look. Second, the site's purpose is somewhat like what "hacking" was like when I first got into security. The site will track how many different IP addresses you can connect from.

![screen shot from ipv4.games](https://isc.sans.edu/diaryimages/images/Screenshot%202024-08-01%20at%2012_55_00%E2%80%AFPM.png)

There are various "leaderboards" based on the number of IP addresses or networks that a particular player was able to connect from. There appears to be no authentication or other fancy newfangled stuff. Instead, you add your username to the URL, and well, if someone else copies your username, they will just help you increase your "rank". There are also some options to associate an email address or a URL with your username.

We are seeing this URL in proxy scans because, of course, no game is fun without a bit of cheating. Or maybe it isn't even cheating but part of the game to find proxies, and have the proxies IP associated with your account. Personally, I do not consider this kind of proxy scan all that malicious. On the other hand, the IPv4.Games site may give attackers hints as to where to look for proxies, assuming many of the "claimed" IPs are proxy servers.

ipv6.games appears to be registered but not active at this time.

---

Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ipv4games](/tag.html?tag=ipv4games)

[1 comment(s)](/diary/Tracking%2BProxy%2BScans%2Bwith%2BIPv4Games/31136/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31132)
* [next](/diary/31140)

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