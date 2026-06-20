---
title: eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun 19th)
url: https://isc.sans.edu/diary/rss/33090
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-19
fetch_date: 2026-06-20T06:14:35.355204
---

# eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33086)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address](/forums/diary/eBanking%2BPhishing%2BDelivered%2BThrough%2BIPv4Mapped%2BIPv6%2BAddress/33090/)

**Published**: 2026-06-19. **Last Updated**: 2026-06-19 08:37:34 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/eBanking%2BPhishing%2BDelivered%2BThrough%2BIPv4Mapped%2BIPv6%2BAddress/33090/#comments)

I detected an interesting phishing email this morning. It targets a major Belgian bank:

![](https://isc.sans.edu/diaryimages/images/isc-20260618-1.png)

The phishing in itself is a classic one, not relevant but the malicious link is interesting:

```

hxxp://[::ffff:5511:74be]/kWC5PHA1
```

The technique used by the attacker is to bypass simple security controls trying to extract domain names and IP addresses via simple regular expressions. The notation “[…]” tells the URL parser that what's inside is a literal IPv6 address. But it’s not a real IPv6 address. What’s the magic?

The started “::” in the address means that it can be expanded to this address:

```

0000:0000:0000:0000:0000:ffff:5511:74be
```

The trick is the fifth group (::ffff:) means that we are facing a IPv4-mapped IPv6 address. This is defined in RFC 4291[[1](https://www.rfc-editor.org/info/rfc4291/)]:

![](https://isc.sans.edu/diaryimages/images/isc-20260618-2.png)

In the URL above, the two trailing 16-bit hex groups “5511” and “74be” are just the four IPv4 octets written in hex.

| Hex | Dec |
| --- | --- |
| 0x55 | 85 |
| 0x11 | 17 |
| 0x74 | 116 |
| 0xBE | 190 |

The real URL is therefore:

```

hxxp://85[.]17[.]116[.]190/kWC5PHA1
```

Another good news from the attacker’s point of view, there is no DNS record!

When visited, this URL redirects to another link where the real phishing kit is hosted:

```

hxxps://3439-aanmelden[.]verificatie[.]qzz[.]io/mon-belfius
```

[1] <https://www.rfc-editor.org/info/rfc4291/>

**Xavier Mertens (@xme)**
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [IPv4](/tag.html?tag=IPv4) [IPv6](/tag.html?tag=IPv6) [Mapping](/tag.html?tag=Mapping) [RFC4291](/tag.html?tag=RFC4291) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/eBanking%2BPhishing%2BDelivered%2BThrough%2BIPv4Mapped%2BIPv6%2BAddress/33090/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33086)

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