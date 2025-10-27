---
title: Webshells Hiding in .well-known Places, (Thu, Sep 25th)
url: https://isc.sans.edu/diary/rss/32320
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-26
fetch_date: 2025-10-02T20:44:37.542787
---

# Webshells Hiding in .well-known Places, (Thu, Sep 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32316)
* [next](/diary/32324)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Webshells Hiding in .well-known Places](/forums/diary/Webshells%2BHiding%2Bin%2Bwellknown%2BPlaces/32320/)

**Published**: 2025-09-25. **Last Updated**: 2025-09-25 14:24:49 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Webshells%2BHiding%2Bin%2Bwellknown%2BPlaces/32320/#comments)

Ever so often, I see requests for files in .well-known recorded by our honeypots. As an example:

> ```
>
> GET /.well-known/xin1.php?p
> Host: [honeypot host name]
> ```

The file names indicate that they are likely looking for webshells. In my opinion, the reason they are looking in .well-known is that this makes a decent place to hide webshells without having them overwritten by an update to the site.

The .well-known directory is meant to be used for various informational files [1], and for example, for ACME TLS challenges. As a result, it is the only directory or file starting with "." that must be accessible via the web server. But it is also "hidden" to Unix command line users. I have written about the various legitimate users of .well-known before [2].

We also see some requests for PHP files in the acme-challenge subdirectory, as well as the pki-challenge subdirectory:

Here are some of the more common, but not "standard" URLs in .well-known hit in our honeypots:

/.well-known/pki-validation/about.php
/.well-known/about.php
/.well-known/acme-challenge/cloud.php
/.well-known/acme-challenge/about.php
/.well-known/pki-validation/xmrlpc.php
/.well-known/acme-challenge/index.php

[1] https://datatracker.ietf.org/doc/html/rfc8615
[2] https://isc.sans.edu/diary/26564

 --
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|![image of an http request to .well-known/xin1.php?p](https://isc.sans.edu/diaryimages/images/Screenshot%202025-09-25%20at%207_23_18%E2%80%AFAM.png)

Keywords: [webshells](/tag.html?tag=webshells) [wellknown](/tag.html?tag=wellknown)

[0 comment(s)](/diary/Webshells%2BHiding%2Bin%2Bwellknown%2BPlaces/32320/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/32316)
* [next](/diary/32324)

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