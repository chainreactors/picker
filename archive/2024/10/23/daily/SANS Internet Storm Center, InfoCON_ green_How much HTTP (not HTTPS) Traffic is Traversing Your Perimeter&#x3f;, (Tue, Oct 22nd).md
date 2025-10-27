---
title: How much HTTP (not HTTPS) Traffic is Traversing Your Perimeter&#x3f;, (Tue, Oct 22nd)
url: https://isc.sans.edu/diary/rss/31372
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-23
fetch_date: 2025-10-06T18:59:40.420350
---

# How much HTTP (not HTTPS) Traffic is Traversing Your Perimeter&#x3f;, (Tue, Oct 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31362)
* [next](/diary/31376)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [How much HTTP (not HTTPS) Traffic is Traversing Your Perimeter?](/forums/diary/How%2Bmuch%2BHTTP%2Bnot%2BHTTPS%2BTraffic%2Bis%2BTraversing%2BYour%2BPerimeter/31372/)

**Published**: 2024-10-22. **Last Updated**: 2024-10-22 16:33:35 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/How%2Bmuch%2BHTTP%2Bnot%2BHTTPS%2BTraffic%2Bis%2BTraversing%2BYour%2BPerimeter/31372/#comments)

Back in June of 2010, The Electronic Frontier Foundation (EFF) released the first beta release of the "HTTPS Everywhere" plugin [1]. Even then, most websites offered HTTPS. But unlike today, HTTP was often still the default, and HTTPS was not always implemented across the entire site.

The world has changed quite a bit since then. Today, browsers are expected to attempt to connect via HTTPS first, and non-TLS connections are the exceptions. New protocols like QUIC went as far as to no longer define a "clear text" version. Few websites offer any content without TLS.

I looked at recent traffic in my network to identify connections that are using HTTP in the clear and only found very few:

* A weather station connected to my network reporting weather to Weather Underground uses HTTP instead of HTTPS. IMHO, it's not a big deal as the data is public. Of course, an attacker could manipulate it, but the weather station is not receiving, just sending. Another service used by the same weather station (Weathercloud) is also sending data in the clear.
* Ubuntu Updates. There have been many discussions in the community if these downloads should take advantage of HTTPS, but so far, the cost of implementing HTTPS is seen as too high. The updates themselves are digitally signed. There is a privacy issue, as requesting updates will leak information about what systems you have running on your network and how they are configured.
* OCSP responses. It may be ironic that the Online Certificate Status Protocol (OCSP) is not using TLS. But again, the overhead of TLS was perceived as too large. This could, however, cause privacy issues in revealing what certificates you are verifying. OCSP is somewhat on its way out, with certificate revocation lists (CRLs) being fashionable again and currently the only required means of certificate validation.

[1] https://www.eff.org/deeplinks/2010/06/encrypt-web-https-everywhere-firefox-extension

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[2 comment(s)](/diary/How%2Bmuch%2BHTTP%2Bnot%2BHTTPS%2BTraffic%2Bis%2BTraversing%2BYour%2BPerimeter/31372/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31362)
* [next](/diary/31376)

### Comments

I have been having this "Fight" this our network/firewall guys. Number 2 (win 11) and 3 are causing problems and they want to add a proxy server just for them.

#### Arthur

#### Oct 22nd 2024 11 months ago

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