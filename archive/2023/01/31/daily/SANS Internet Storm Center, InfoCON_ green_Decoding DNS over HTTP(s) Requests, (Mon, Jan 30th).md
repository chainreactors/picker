---
title: Decoding DNS over HTTP(s) Requests, (Mon, Jan 30th)
url: https://isc.sans.edu/diary/rss/29488
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-31
fetch_date: 2025-10-04T05:15:36.316103
---

# Decoding DNS over HTTP(s) Requests, (Mon, Jan 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29484)
* [next](/diary/29490)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Decoding DNS over HTTP(s) Requests](/forums/diary/Decoding%2BDNS%2Bover%2BHTTPs%2BRequests/29488/)

**Published**: 2023-01-30. **Last Updated**: 2023-01-30 16:51:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Decoding%2BDNS%2Bover%2BHTTPs%2BRequests/29488/#comments)

I have written before about scans for DNS over HTTP(s) (DoH) servers. DoH is now widely supported in different browsers and recursive resolvers. It has been an important piece in the puzzle to evade various censorship regimes, in particular, the "Big Chinese Firewall". Malware has at times used DoH, but often uses its own HTTP(s) based resolvers that do not necessarily comply with the official DoH standard.

Just today, one of our honeypots received the following requests from various IPs:

`GET /?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /dns-query?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /doh?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /doh/family-filter?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /doh/secure-filter?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /query?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1
GET /resolve?dns=DUIBAAABAAAAAAAABWJhaWR1A2NvbQAAAQAB HTTP/1.1`

The different URLs correspond to various common implementations of DoH. The most common default appears to be "/dns-query" (BIND and Unbound). This is also the endpoint used by the RFC. Some DNS servers (for example, Power DNS) use "/" as the default.

The payload is a Base64 encoded DNS message:

`00000000: 0d42 0100 0001 0000 0000 0000 0562 6169  .B...........bai
00000010: 6475 0363 6f6d 0000 0100 01              du.com.....`

0d42 - Query ID
0100 - Recursion desired flag set
0001 - One Query
0000 - No Answers
0000 - No Authority Records
0000 - No Additional Records
0562 6169 6475 0363 6f6d 00 baidu.com
0001 - Internet Zone
0001 - A Records

So in short: An "A" records query for baidu.com. If you see any requests like this in your logs: Don't worry about it too much. I wouldn't consider it some simple recognizance. They are unlikely to "attack" your server even if you have a DNS over HTTPS resolver running. However, they may use it to anonymize their requests which may also trigger some alerts if they are attempting to look up suspect hostnames. This traffic may also lead to resource issues if you have a smaller server.

I did earlier today add DoH responses to some of my honeypots, so we will see if anything changes.

---

Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [dns](/tag.html?tag=dns) [doh](/tag.html?tag=doh)

[1 comment(s)](/diary/Decoding%2BDNS%2Bover%2BHTTPs%2BRequests/29488/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29484)
* [next](/diary/29490)

### Comments

For those looking to rate-limit or filter DNS queries, give dnsdist a look. It's a pretty lightweight dns loadbalancer/proxy that can do a lot of customized filtering and rate limiting. At my last job we used to do protocol layer DDoS filtering on a production setup handling thousands of DNS queries per second.

#### Cool Fire

#### Jan 31st 2023 2 years ago

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