---
title: Do Attackers Pay More Attention to IPv6&#x3f;, (Sat, Jul 29th)
url: https://isc.sans.edu/diary/rss/30076
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-30
fetch_date: 2025-10-04T11:53:47.893225
---

# Do Attackers Pay More Attention to IPv6&#x3f;, (Sat, Jul 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30074)
* [next](/diary/30078)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Do Attackers Pay More Attention to IPv6?](/forums/diary/Do%2BAttackers%2BPay%2BMore%2BAttention%2Bto%2BIPv6/30076/)

**Published**: 2023-07-29. **Last Updated**: 2023-07-29 13:13:52 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Do%2BAttackers%2BPay%2BMore%2BAttention%2Bto%2BIPv6/30076/#comments)

IPv6 has always been a hot topic! Available for years, many ISP's deployed IPv6 up to their residential customers. In Belgium, we were for a long time, the top-one country with IPv6 deployment because all big players provided IPv6 connectivity. In today's operating systems, IPv6 will be used first if your computer sees "RA" packets (for "router advertisement" [[1](https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol)]) and can get an IPv6 address. This will be totally transparent. That's why many people think that they don't use IPv6 but they do!

To access online resources, a host will try to resolve a domain or hostname by generating "A" or "AAAA" DNS requests. A malware that relies on the host resolver doesn't need to know if the C2 is available via IPv4, IPv6 or both!

I'm wondering for a long time why attackers do not pay more attention to IPv6 connectivity because it could be less hardened or not monitored at all! How many security controls rely on regexes to catch IPv4 addresses only?

Today, I found a malicious Python script that creates a footprint of the victim (usual behaviour) but, this time, it also try to get the IPv6 of the victim's computer:

```

def get_ipv6_address():
    try:
        i6_s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        i6_s.connect(("2001:4860:4860::8888", 80))
        i6s_s = i6_s.getsockname()[0]
        i6_s.close()
        return i6s_s
    except socket.error:
        return None
```

(The tested IPv6 address is Google public DNS)

Does it mean that attackers will pay more attention to IPv6? Let's see in the future!

[1] <https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [IPv6](/tag.html?tag=IPv6) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/Do%2BAttackers%2BPay%2BMore%2BAttention%2Bto%2BIPv6/30076/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30074)
* [next](/diary/30078)

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