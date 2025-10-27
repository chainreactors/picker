---
title: The Danger of IP Volatility, (Sat, Feb 15th)
url: https://isc.sans.edu/diary/rss/31688
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-16
fetch_date: 2025-10-06T20:37:24.187742
---

# The Danger of IP Volatility, (Sat, Feb 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31686)
* [next](/diary/31692)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [The Danger of IP Volatility](/forums/diary/The%2BDanger%2Bof%2BIP%2BVolatility/31688/)

**Published**: 2025-02-15. **Last Updated**: 2025-02-15 07:22:45 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/The%2BDanger%2Bof%2BIP%2BVolatility/31688/#comments)

What do I mean by “IP volatility”? Today, many organizations use cloud services and micro-services. In such environments, IP addresses assigned to virtual machines or services can often be volatile, meaning they can change or be reassigned to other organizations or users. This presents a risk for services relying on static IPs for security configurations and may introduce impersonation or data leakage issues.

This morning, I was setting up a new environment. I got a new IP address assigned by my hosting company and deployed a classic configuration: a reverse-proxy redirecting to many web services and generating Let’s Encrypt certificates.

Once the reverse proxy was in place, I started to deploy more services but detected some activity in the log (always keep an eye on your logs!) and saw this:

```

{"level":"debug","time":"2025-02-15T06:22:33Z","caller":"github.com/traefik/traefik/v3/pkg/tls/tlsmanager.go:228","message":"Serving default certificate for request: \"postmaster.xxxxxxxx.hu\""}
{"level":"debug","time":"2025-02-15T06:46:36Z","caller":"github.com/traefik/traefik/v3/pkg/tls/tlsmanager.go:228","message":"Serving default certificate for request: \"pop3.xxxxxxxx.hu\""}
{"level":"debug","time":"2025-02-15T07:04:16Z","caller":"github.com/traefik/traefik/v3/pkg/tls/tlsmanager.go:228","message":"Serving default certificate for request: \”xxxxxxxx.hu\""}
```

A quick DNS request confirmed that these hosts are resolving to my newly assigned IP!

Worse, this organization seems to still be using POP3, and a user (or a script) is still trying to fetch emails using this protocol!

Some tips:

* When you move to another hosting solution, update your DNS records
* Cleanup your DNS zones and remove unwanted entries
* Use mechanisms to preserve your IP addresses (like “Elastic IPs” provided by AWS)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Cloud](/tag.html?tag=Cloud) [DNS](/tag.html?tag=DNS) [Proxy](/tag.html?tag=Proxy) [Volatility](/tag.html?tag=Volatility) [IP](/tag.html?tag=IP)

[0 comment(s)](/diary/The%2BDanger%2Bof%2BIP%2BVolatility/31688/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31686)
* [next](/diary/31692)

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