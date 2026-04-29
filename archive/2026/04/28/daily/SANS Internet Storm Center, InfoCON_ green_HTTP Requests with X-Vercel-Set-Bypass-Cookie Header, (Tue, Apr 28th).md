---
title: HTTP Requests with X-Vercel-Set-Bypass-Cookie Header, (Tue, Apr 28th)
url: https://isc.sans.edu/diary/rss/32930
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-28
fetch_date: 2026-04-29T05:13:00.571306
---

# HTTP Requests with X-Vercel-Set-Bypass-Cookie Header, (Tue, Apr 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32926)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [HTTP Requests with X-Vercel-Set-Bypass-Cookie Header](/forums/diary/HTTP%2BRequests%2Bwith%2BXVercelSetBypassCookie%2BHeader/32930/)

**Published**: 2026-04-28. **Last Updated**: 2026-04-28 13:28:45 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/HTTP%2BRequests%2Bwith%2BXVercelSetBypassCookie%2BHeader/32930/#comments)

This weekend, we saw a few requests to our honeypot that included an "X-Vercel-Set-Bypass-Cookie" header. A sample request:

> GET / HTTP/1.1
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/ \*;q=0.8
> Accept-Language: en-US,en;q=0.5
> Accept-Encoding: gzip, deflate, br
> Cache-Control: no-cache
> Pragma: no-cache
> Connection: keep-alive
> X-Vercel-Set-Bypass-Cookie: samesite-none-secure
> Upgrade-Insecure-Requests: 1
> X-Forwarded-From: 21.235.92.139
> X-Real-Iphone: 21.235.92.139
> Referer: [redacted, same as "Host" header]
> Host: [redacted]

Vercel documents the "x-vercel-protection-bypass" header(note: no "Cookie" part) as a secret that can be configured to disable certain protections during testing. This type of bypass feature is common in various platforms. In particular, web application firewall features often need to be disabled to allow higher request rates during CI/CD pipeline operations. The value set in the header is a user-configurable secret[1].

The X-Vercel-Set-Bypass-Cookie allows testing in browsers and maintains the bypass by having the server set a cookie to indicate the bypass. There are two options according to Vercel's documentation:

1. True: enables the cookie
2. samesitenone: enables the cookie, and set the same-site property to none.

I did not see the "samesite-none-secure" documented by Vercel.

The most likely intention of the header is to relax security settings, maybe even steal secrets, should Vercel expose them in the cookie. I have not had a chance to test the request against a Vercel website. Any input as to the intent is welcome.

The request was also set via an open proxy, likely to protect the attacker's identity, but it failed due to the configured proxy headers.

[1] https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [Vercel](/tag.html?tag=Vercel)

[0 comment(s)](/diary/HTTP%2BRequests%2Bwith%2BXVercelSetBypassCookie%2BHeader/32930/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32926)

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