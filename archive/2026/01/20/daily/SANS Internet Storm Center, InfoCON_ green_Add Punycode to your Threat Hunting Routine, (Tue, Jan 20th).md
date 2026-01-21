---
title: Add Punycode to your Threat Hunting Routine, (Tue, Jan 20th)
url: https://isc.sans.edu/diary/rss/32640
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-20
fetch_date: 2026-01-21T03:33:21.870841
---

# Add Punycode to your Threat Hunting Routine, (Tue, Jan 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32636)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Add Punycode to your Threat Hunting Routine](/forums/diary/Add%2BPunycode%2Bto%2Byour%2BThreat%2BHunting%2BRoutine/32640/)

**Published**: 2026-01-20. **Last Updated**: 2026-01-20 10:01:58 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Add%2BPunycode%2Bto%2Byour%2BThreat%2BHunting%2BRoutine/32640/#comments)

IDNs or “International Domain Names” have been with us for a while now (see RFC3490[[1](https://datatracker.ietf.org/doc/html/rfc3490)]). They are (ab)used in many attack scenarios because.. it works! Who can immediately spot the difference between:

```

https://youtube.com/
```

And:

```

https://youtube.com/
```

The magic is to replace classic characters by others that look almost the same. In the example above, the letter “o” has been replaced by Greek character “o”.

If they are very efficient for attackers, they remain below the radar in many organizations. To avoid issues when printing unusual characters, Punycode[[2](https://en.wikipedia.org/wiki/Punycode)] helps to encode them in plain characters. The example above will be encoded as:

```

xn--yutube-wqf.com
```

This format is based on:

* “xn--“ : the common prefix for all IDNs requests.
* “yutube.com”: The normal ASCII characters
* “wqf” : The Punycode encoded version of the Unicode character

Python can decode them easily:

```

$ python3
Python 3.12.3 (main, Jan  8 2026, 11:30:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> domain = "xn--yutube-wqf.com"
>>> decoded = domain.encode("ascii").decode("idna")
>>> print(decoded)
y?utube.com
>>> for c in decoded:
...     print(f"{c} -> {ord(c)}")
...
y -> 121
? -> 1086
u -> 117
t -> 116
u -> 117
b -> 98
e -> 101
. -> 46
c -> 99
o -> 111
m -> 109
>>>
```

You can see the value of “o” is not “usual” (not in the ASCII range). They are plenty of online tools that can (de|en)code Punycode[[3](https://regery.com/en/domains/tools/punycode-decoder)].

If not all IDNs are suspicious, they are not very common and deserve some searches in your logs. If you already collect your DNS resolver logs (I hope you do!), it’s easy to search for such domains:

```

$ grep "xn--" queries.log*
queries.log:19-Jan-2026 19:54:38.399 queries: info: client @0x999999999999 192.168.255.13#47099 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log:20-Jan-2026 04:38:25.877 queries: info: client @0x999999999999 192.168.255.13#49850 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 15:22:11.741 queries: info: client @0x9999999999 192.168.255.13#60763 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 17:27:23.127 queries: info: client @0x99999999999 192.168.255.13#44141 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 22:54:36.841 queries: info: client @0x99999999999 192.168.255.13#35963 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
```

The detected Punycode domain is decoded to:

![](https://isc.sans.edu/diaryimages/images/isc-20260120-1.png)

Another good proof that DNS is a goldmine for threat hunting!

[1] <https://datatracker.ietf.org/doc/html/rfc3490>
[2] <https://en.wikipedia.org/wiki/Punycode>
[3] <https://regery.com/en/domains/tools/punycode-decoder>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Threat Hunting](/tag.html?tag=Threat Hunting) [IDN](/tag.html?tag=IDN) [Punycode](/tag.html?tag=Punycode) [Domain](/tag.html?tag=Domain) [Log](/tag.html?tag=Log)

[0 comment(s)](/diary/Add%2BPunycode%2Bto%2Byour%2BThreat%2BHunting%2BRoutine/32640/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32636)

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