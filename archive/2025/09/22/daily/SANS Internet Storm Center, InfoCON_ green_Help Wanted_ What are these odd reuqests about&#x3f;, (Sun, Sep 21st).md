---
title: Help Wanted: What are these odd reuqests about&#x3f;, (Sun, Sep 21st)
url: https://isc.sans.edu/diary/rss/32302
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-22
fetch_date: 2025-10-02T20:30:16.728997
---

# Help Wanted: What are these odd reuqests about&#x3f;, (Sun, Sep 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32296)
* [next](/diary/32308)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Help Wanted: What are these odd requests about?](/forums/diary/Help%2BWanted%2BWhat%2Bare%2Bthese%2Bodd%2Brequests%2Babout/32302/)

**Published**: 2025-09-21. **Last Updated**: 2025-09-23 12:25:44 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Help%2BWanted%2BWhat%2Bare%2Bthese%2Bodd%2Brequests%2Babout/32302/#comments)

Looking at our web honeypot data, I came across an odd new request header I hadn't seen before: "X-Forwarded-App". My first guess was that this is yet another issue with a proxy-server bucket brigade spilling secrets when a particular "App" is connecting to it. So I dove in a bit deeper, and found requests like this:

> GET /business/appVersion/get/qr/download HTTP/1.1
> Host: [honeypot IP address]
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Trailer/93.3.3570.29
> Accept: application/json
> Accept-Language: zh-CN,zh;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,en;q=0.6
> Content-Type: application/json;charset=UTF-8
> Deviceid: 4c2e063f3def4582
> Deviceinfo: android
> License: doJn7HAfIo9xMsLbcEKD7ku40F2zWJjJOjgxwqFs\_Hec3FdkKcgKRQFCOrf-5xxI
> Phonemodel: samsung
> V: 48650
> X-Forwarded-App: app.F6syl6mB
> Accept-Encoding: gzip

This looks like a request a mobile app would send. Some of the details, like the string following "app.", change from request to request. The "License" header could be used as an API key (I modified it a bit in case this is a valid license).

Google'ing showed some APIs using an X-Forwarded-App header, but nothing specific that would match this request. Please let me know if you have any ideas what this request may be about.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [header](/tag.html?tag=header) [proxy](/tag.html?tag=proxy) [qr](/tag.html?tag=qr) [samsung](/tag.html?tag=samsung) [XForwardedApp](/tag.html?tag=XForwardedApp)

[2 comment(s)](/diary/Help%2BWanted%2BWhat%2Bare%2Bthese%2Bodd%2Brequests%2Babout/32302/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/32296)
* [next](/diary/32308)

### Comments

this looks like a bot scraping for exposed mobile-app backend endpoints and trying headerconfusion tricks.

#### Anonymous

#### Sep 21st 2025 1 week ago

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