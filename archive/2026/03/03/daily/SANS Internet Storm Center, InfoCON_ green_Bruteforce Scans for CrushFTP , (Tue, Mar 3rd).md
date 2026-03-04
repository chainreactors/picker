---
title: Bruteforce Scans for CrushFTP , (Tue, Mar 3rd)
url: https://isc.sans.edu/diary/rss/32762
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-03
fetch_date: 2026-03-04T04:04:28.021565
---

# Bruteforce Scans for CrushFTP , (Tue, Mar 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32758)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Bruteforce Scans for CrushFTP](/forums/diary/Bruteforce%2BScans%2Bfor%2BCrushFTP/32762/)

**Published**: 2026-03-03. **Last Updated**: 2026-03-03 15:01:17 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Bruteforce%2BScans%2Bfor%2BCrushFTP/32762/#comments)

CrushFTP is a Java-based open source file transfer system. It is offered for multiple operating systems. If you run a CrushFTP instance, you may remember that the software has had some serious vulnerabilities: CVE-2024-4040 (the template-injection flaw that let unauthenticated attackers escape the VFS sandbox and achieve RCE), CVE-2025-31161 (the auth-bypass that handed over the crushadmin account on a silver platter), and the July 2025 zero-day CVE-2025-54309 that was actively exploited in the wild.

But what we are seeing now is not an exploit of a specific vulnerability, but rather simple brute-forcing, looking for lazily configured systems.

The requests we are seeing right now:

> `POST /WebInterface/function/?command=login&username=crushadmin&password=crushadmin HTTP/1.1
> Host: [redacted]
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36
> Content-Length: 0
> Accept-Encoding: gzip
> Connection: close`

Note that these are POST requests, but the username and password are passed as GET parameters. The body of the request is empty.

During setup, CrushFTP requires that the user configure an admin user. The username is not fixed, but "crushadmin" is one of the suggested usernames. Others are "root" and "admin". There is no default or suggested password. The attacker relies on lazy administrators who use "crushadmin" as both a username and a password.

These attacks originate from 5.189.139.225, a French IP address with a history of exploit attempts targeting simple vulnerabilities. We have seen this IP acting up since around February.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [crushftp](/tag.html?tag=crushftp)

[0 comment(s)](/diary/Bruteforce%2BScans%2Bfor%2BCrushFTP/32762/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32758)

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