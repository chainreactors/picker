---
title: Geolocation and Starlink, (Tue, Jan 21st)
url: https://isc.sans.edu/diary/rss/31612
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-22
fetch_date: 2025-10-06T20:13:04.334842
---

# Geolocation and Starlink, (Tue, Jan 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31608)
* [next](/diary/31616)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Geolocation and Starlink](/forums/diary/Geolocation%2Band%2BStarlink/31612/)

**Published**: 2025-01-21. **Last Updated**: 2025-01-21 15:40:20 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Geolocation%2Band%2BStarlink/31612/#comments)

![](https://isc.sans.edu/diaryimages/images/starlinklogo.jpeg)Until now, satellite internet access has been more of a niche solution for internet access. But with the wide availability of Starlink, this is changing. Starlink's performance and price are competitive for many rural users to forgo solutions like cellular or slower DSL speeds if they are available at all.

Starlink offers a substantially different type of service from most "traditional" satellite networks. Traditional satellite networks use a small number of satellites in high orbits, connecting to a handful of ground stations. The ground station issues the IP address, and each ground station may cover a large geographic area, often exceeding individual countries. The IP address of a satellite user identifies the ground station location, not the user's location. Starlink, on the other hand, uses satellites in low earth orbit. The network can forward traffic among satellites, but typically, the satellite will attempt to pass the traffic to the closest base station in view. Due to the low orbit, each satellite only "sees" a relatively small area, and the ground station is usually within a couple hundred miles of the user.

It appears that Starlink is using AS 14593 and 27277. The first one is the one that is used for customer traffic. The second one seems to be used for the internal corporate network.

AS 14593 advertises 696 different prefixes [HE]. Most are small (/23 and /24). This is typical for a newer company like SpaceX that had to "cobble together" IP address space and couldn't get a large allocation. Starlink does not offer a publicly routable address to customers for regular consumer plans. Instead, it uses "carrier-grade NAT". The customer will receive a 100.64.0.0/10 address per RFC 6598 [CGNAT]. By default, the Starlink router will issue 192.168/16 addresses to the user's equipment unless the router is configured in bridge mode (or bypass mode).

The CGNAT address is later translated to a publicly routable address at the ground station. Starlink does support PTR records for its customer IPs and uses the following hostname scheme:

customer.[ground station identifier].pop.starlinkisp.net

Forward resolution for these hostnames does not work. This is likely configured to avoid issues with customers attempting to run mail servers. The "ground stations identifier" appears to follow the following format:

4 digits: City identifier

3 digits: Region (Country or the State, followed by 'X', for US-based ground stations)

1 digit: number

For example:

Non-US Locations:

> `customer.mnlaphl1.pop.starlinkisp.net - Manila, Philipines
> customer.acklnzl1.pop.starlinkisp.net - Aukland, New Zealand
> customer.sydyaus1.pop.starlinkisp.net - Sydney, Australia`

US Locations:

> `customer.sttlwax1.pop.starlinkisp.ne - Seattle, WA
> customer.chcoilx1.pop.starlinkisp.net - Chicago, IL
> customer.mmmiflx1.pop.starlinkisp.net - Miami, FL`

All IPs associated with a particular ground station will receive the same hostname. Starlink customers often experience issues with geofencing. The same is true for other satellite providers. Websites blocking Starlink may not use up-to-date IP to location databases, or they consider all satellite users "suspect". Based on the Starlink architecture, there is always a chance that a customer will show up with the "wrong" location if their data was routed within the satellite constellation before being sent to the ground. This is, in particular, true for off-shore users. Based on various compliance issues or interpretations of these issues, sites may choose to block Starlink outright.

Starlink also offers IPv6 to its customers. Reverse resolution for Starlink-associated IPv6 addresses follow the same scheme as for IPv4.

[HE] https://bgp.he.net/AS14593#\_prefixes
[CGNAT] https://datatracker.ietf.org/doc/html/rfc6598

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [geolocation](/tag.html?tag=geolocation) [starlink](/tag.html?tag=starlink)

[1 comment(s)](/diary/Geolocation%2Band%2BStarlink/31612/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31608)
* [next](/diary/31616)

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