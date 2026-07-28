---
title: Java Spring Boot "heapdump" scans, (Mon, Jul 27th)
url: https://isc.sans.edu/diary/rss/33188
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-27
fetch_date: 2026-07-28T05:00:03.676918
---

# Java Spring Boot "heapdump" scans, (Mon, Jul 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33184)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Java Spring Boot "heapdump" scans](/forums/diary/Java%2BSpring%2BBoot%2Bheapdump%2Bscans/33188/)

**Published**: 2026-07-27. **Last Updated**: 2026-07-27 10:04:51 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Java%2BSpring%2BBoot%2Bheapdump%2Bscans/33188/#comments)

Spring Boot exposes the endpoint "/actuator/heapdump" to collect debug information. By default, the endpoint will return a file heapdump.hprof, which includes a binary heapdump that can be used to analyze the current state of the application. Non-Java readers may be familiar with a similar concept, core dumps, which are produced by binaries to expose a memory image at the time the software crashes. "heapdumps" are the Java analog to "core-dumps". The heapdump often includes secrets used by the application to connect to backend systems. API keys, database passwords, and other sensitive data may be exposed in the heapdump.

The requests we are seeing use a slightly different URL: "/admin-api/actuator/heapdump". I am not sure if the "/admin-api/" prefix is associated with a particular application, but it is a reasonable configuration and may be used by multiple applications.

The full request we are seeing:

> `GET /admin-api/actuator/heapdump HTTP/1.1
> Host: 68.77.136.94
> User-Agent: python-requests/2.34.2
> Accept-Encoding: gzip, deflate
> Accept: */*
> Connection: keep-alive
> Authorization: Basic YWRtaW46YWRtaW4=`

The base64-encoded authorization string decodes to "admin:admin," a typical default username and password. The location of the management endpoints is typically configured in your application.yml file with:

> `management.endpoints.web.base-path=/admin-api/actuator`

Since this is used by Spring Boot, you should be able to restrict access more effectively with Spring Security. But the attacker obviously assumes that authentication is configured and just relies on a weak password.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [java heapdump spring boot](/tag.html?tag=java heapdump spring boot)

[0 comment(s)](/diary/Java%2BSpring%2BBoot%2Bheapdump%2Bscans/33188/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33184)

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