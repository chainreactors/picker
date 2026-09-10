---
title: Scans for Proxmox Servers, (Wed, Sep 9th)
url: https://isc.sans.edu/diary/rss/33324
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-09
fetch_date: 2026-09-10T06:52:30.005473
---

# Scans for Proxmox Servers, (Wed, Sep 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33320)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for Proxmox Servers](/forums/diary/Scans%2Bfor%2BProxmox%2BServers/33324/)

**Published**: 2026-09-09. **Last Updated**: 2026-09-09 17:46:24 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BProxmox%2BServers/33324/#comments)

About a week ago, Proxmox published an advisory revealing a vulnerability in older versions of Proxmox VE, its flagship Virtual Environment product. The vulnerability only affects version 7, which has not been supported for a couple of years now.

But it appears that the vulnerability may have caught the attention of some attackers and researchers. We do see a bump in scans for port 8006, and also some additional brute force traffic. For example, brute force requests like:

> `POST /api2/json/access/ticket HTTP/1.1
> Host: [redacted]:8006
> User-Agent: Go-http-client/1.1
> Content-Length: 37
> Content-Type: application/x-www-form-urlencoded
> Accept-Encoding: gzip`
>
> `password=Ww778899&username=root%40pam`

The PVE proxy log will log failed login attempts with a 401 status code:

> `::ffff:62.60.130.193 - - [09/09/2026:15:26:14 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
> ::ffff:62.60.130.193 - - [09/09/2026:15:28:04 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
> ::ffff:62.60.130.193 - - [09/09/2026:15:28:08 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
> ::ffff:62.60.130.193 - - [09/09/2026:15:29:49 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
> ::ffff:62.60.130.193 - - [09/09/2026:15:29:52 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
> ::ffff:62.60.130.193 - - [09/09/2026:15:31:33 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
> ::ffff:62.60.130.193 - - [09/09/2026:15:31:36 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50`

You may also see the less commonly used 308 status code if the attacker does not use TLS on their first attempt and instead sends a POST request (as shown above). A 308 access code allows a client to change the request method after following the redirect. 301 and 302 status codes require the same method for the follow-up request.

Other scans I have seen:

Classic Fingerprinting

> `/pve2/images/logo-128.png???????`

And a POST request to `/api2/extjs/access/ticket`. This endpoint behaves differently from the prior endpoint. It always returns 200, but the JSON payload will contain the login failed messages. These are trickier to analyze because the proxy log does not indicate the outcome of authentication. A return payload size of 77 bytes should indicate failure.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [proxmox](/tag.html?tag=proxmox)

[0 comment(s)](/diary/Scans%2Bfor%2BProxmox%2BServers/33324/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33320)

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