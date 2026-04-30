---
title: Today's Odd Web Requests, (Wed, Apr 29th)
url: https://isc.sans.edu/diary/rss/32934
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-29
fetch_date: 2026-04-30T05:30:28.242791
---

# Today's Odd Web Requests, (Wed, Apr 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32930)
* [next](/diary/32936)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Today's Odd Web Requests](/forums/diary/Todays%2BOdd%2BWeb%2BRequests/32934/)

**Published**: 2026-04-29. **Last Updated**: 2026-04-29 13:11:41 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Todays%2BOdd%2BWeb%2BRequests/32934/#comments)

Today, two different "new" requests hit our honeypots. Both appear to be recon requests and not associated with specific vulnerabilities. But as always, please let me know if you have additional information

1 - Broadcom API Gateway

> GET /bam/restart/if/required
> Host: [redacted]:8080
> Connection: close

This request is targeting a Broadcom API Gateway endpoint. As is, the request should not cause any problems, but the response may indicate if a Broadcom API Gateway is used, and it could lead to follow-up attacks.

2 - ESP32

> `GET /esps/
> host: [redcated]:8080
> user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
> connection: close
> accept: */*
> accept-language: en
> accept-encoding: gzip`

The path "/esps/" is associated with ESP32 devices. The ESP32 platform is a low-cost system-on-a-chip (SOC) device that is frequently used in IoT devices or even in various home automation projects. The URL '/esps/' may be associated with uploading firmware, but I have not yet seen any follow-up attacks.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [broadcom](/tag.html?tag=broadcom) [esp32](/tag.html?tag=esp32)

[0 comment(s)](/diary/Todays%2BOdd%2BWeb%2BRequests/32934/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32930)
* [next](/diary/32936)

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