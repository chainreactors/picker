---
title: Scans for ESAFENET CDG 3 Document Management System Weak Logins, (Sun, Jul 26th)
url: https://isc.sans.edu/diary/rss/33184
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-26
fetch_date: 2026-07-27T05:42:38.979590
---

# Scans for ESAFENET CDG 3 Document Management System Weak Logins, (Sun, Jul 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33180)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for ESAFENET CDG 3 Document Management System Weak Logins](/forums/diary/Scans%2Bfor%2BESAFENET%2BCDG%2B3%2BDocument%2BManagement%2BSystem%2BWeak%2BLogins/33184/)

**Published**: 2026-07-26. **Last Updated**: 2026-07-26 15:26:14 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BESAFENET%2BCDG%2B3%2BDocument%2BManagement%2BSystem%2BWeak%2BLogins/33184/#comments)

ESAFENET's CDG showed up in our data before. The company focused on secure document management and data leakage prevention solutions. The "CDG" stands for "Content Data Guard", and the product appears to be mostly targeting the Chinese market [1]. Sadly, like so many security products, it suffers from basic security vulnerabilities like SQL Injection, XSS, and default passwords. We have seen scanning for ESAFENET CDG before, in particular after the cross-site scripting vulnerability was made public.

The scans we are seeing right now are going after the well-known default passwords that ESAFENET CDG ships with. Exploit scripts listing these passwords are, for example, included in a nulei template published in 2023 [2].

> `POST /CDGServer3/SystemConfig
> Host: [redacted]
> User-Agent: Mozilla/5.0 (Ubuntu; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0
> Content-Length: 73
> Accept: */*
> Accept-Language: en
> Content-Type: application/x-www-form-urlencoded
> Accept-Encoding: gzip
> Connection: close`
>
> `command=Login&help=null&verifyCodeDigit=dfd&name=secadmin&pass=Est@Spc820`

This is a typical case of a password that will likely pass many standard security checks (10 characters, upper/lower case, special characters, and numbers), but it is still terribly insecure as it is a well-known default password.

[1]  https://esafenet.com
[2] https://github.com/projectdiscovery/nuclei-templates/issues/7094

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ESAFENET cdg default login](/tag.html?tag=ESAFENET cdg default login)

[0 comment(s)](/diary/Scans%2Bfor%2BESAFENET%2BCDG%2B3%2BDocument%2BManagement%2BSystem%2BWeak%2BLogins/33184/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33180)

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