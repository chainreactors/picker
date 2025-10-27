---
title: New Feature: Daily Trends Report, (Mon, Aug 4th)
url: https://isc.sans.edu/diary/rss/32170
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-05
fetch_date: 2025-10-07T00:49:14.681778
---

# New Feature: Daily Trends Report, (Mon, Aug 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32166)
* [next](/diary/32174)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [New Feature: Daily Trends Report](/forums/diary/New%2BFeature%2BDaily%2BTrends%2BReport/32170/)

**Published**: 2025-08-04. **Last Updated**: 2025-08-05 02:52:01 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/New%2BFeature%2BDaily%2BTrends%2BReport/32170/#comments)

I implemented a new report today, the "Daily Trends" report. It summarizes noteworthy data received from our honeypot. As with everything, it will improve if you provide feedback :)

There are two ways to receive the report:

1. E-Mail: Sign up at https://isc.sans.edu/notify.html
2. JSON/HTTP: You may also just download the raw JSON data for the report at https://isc.sans.edu/feeds/trends.json

The sections of the report:

* Top 10 newly registered domains, based on our domain score (the higher, the more suspect)
* Top 10 URLs: The top 10 newly seen URLs from our web honeypot.
* Top 10 New SSH/Telnet usernames: Usernames our Cowrie honeypots have not seen before.
* Top 10 Trending ports

The layout will be refined for sure. Let me know I the data is useful.

Can't receive the email? E-mail delivery has always been an issue, which is why we offer the JSON report as well.

[![daily trends reports snippet ](https://isc.sans.edu/diaryimages/images/Screenshot%202025-08-04%20at%201_39_58%E2%80%AFPM.png)](https://isc.sans.edu/diaryimages/images/Screenshot%202025-08-04%20at%201_39_58%E2%80%AFPM.png)

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Social Media/Contact Links](https://jbu.me)|

Keywords: [report](/tag.html?tag=report) [trends](/tag.html?tag=trends)

[0 comment(s)](/diary/New%2BFeature%2BDaily%2BTrends%2BReport/32170/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32166)
* [next](/diary/32174)

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