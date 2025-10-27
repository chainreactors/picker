---
title: Investigating Anonymous VPS services used by Ransomware Gangs
url: https://blog.bushidotoken.net/2025/02/investigating-anonymous-vps-services.html
source: Over Security - Cybersecurity news aggregator
date: 2025-02-15
fetch_date: 2025-10-06T20:37:58.108674
---

# Investigating Anonymous VPS services used by Ransomware Gangs

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### Investigating Anonymous VPS services used by Ransomware Gangs

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[February 14, 2025](https://blog.bushidotoken.net/2025/02/investigating-anonymous-vps-services.html "permanent link")

One of the challenges with investigating cybercrime is the
infrastructure the adversaries leverage to conduct attacks. Cybercriminal
infrastructure has evolved drastically over the last 25 years, which now involves
hijacking web services, content distribution networks (CDNs), residential
proxies, fast flux DNS, domain generation algorithms (DGAs), botnets of IoT
devices, the Tor network, and all sorts of nested services.

This blog shall investigate a small UK-based hosting provider
known as BitLaunch as an example of how challenging it can be to tackle
cybercriminal infrastructure. Research into this hosting provider revealed that
they appear to have a multi-year history of cybercriminals using BitLaunch to
host command-and-control (C2) servers via their [Anonymous
VPS](https://bitlaunch.io/blog/bitlaunch-cryptocurrency-anonymous-vps/) service.

The year-on-year growing number of CobaltStrike C2 servers
hosted on BitLaunch’s services could be an indicator of tacit collusion with
cybercriminals through the facilitation of cheap and quick to procurement of
VPSs that end up being used to launch ransomware attacks on all sorts of
victims, including hospitals, schools, governments, companies, and charities.

The concept of aiding and abetting criminal activity in law is
essentially when an individual or an organisation intentionally assists,
facilitates, or encourages a crime. In this case, it would be aiding and
abetting the creation of cybercriminal infrastructure. If a hosting provider
ignores clear red flags (e.g., cryptocurrency payments from known illicit
sources or use of servers for illegal activities), they might still be held criminally
liable under wilful blindness under certain laws.

In the past, authorities have taken down bulletproof hosting
(BPH) providers that knowingly support cybercrime, such as CyberBunker and
LolekHost. In February 2025, the UK government also [sanctioned](https://www.gov.uk/government/news/new-uk-sanctions-target-russian-cybercrime-network)
a Russia-based BPH known as ZSERVERS (aka XHOST) for facilitating LockBit
attacks.

A podcast version of the blog is available [here](https://www.youtube.com/watch?v=xX25GPYYr98).

*Update: This blog was updated with a statement from BitLaunch (see the end of this blog).*

## Who is BitLaunch aka BL Networks aka BLNWX?

Active since at least 2017, BitLaunch (also known as BL
Networks or BLNWX) is a virtual private server (VPS) reseller whose autonomous
system number (ASN) is [AS399629](https://bgp.tools/as/399629#asinfo).
Up to 48 IPv4 networks [belong](https://networksdb.io/autonomous-system/AS399629) to BitLaunch
which are used to "instantly launch a Linux or Windows VPS” where
customers can “pay hourly with Bitcoin, Litecoin, and Ethereum, with no firm
commitments." BitLaunch also supports their customers via a [command-line (CLI)
tool](https://developers.bitlaunch.io/docs/cli-tool-blcli) and a [Python
library](https://github.com/BitLaunchIO/pybitlaunch). BitLaunch has another name, however, in their [legal terms and conditions](https://bitlaunch.io/legal/fullterms/)
they go by Liber Systems and have their own separate [website](https://www.liber.co.uk/).

## Why focus on BitLaunch?

BitLaunch is quite interesting as they present themselves as
a UK-based company run by two local UK businessmen. Their “anonymous Bitcoin
VPS” service is regularly abused for all sorts of cybercriminal activities. What
triggered this research was the fact that their nickname “BLNWX” was regularly
reappearing in cyber threat intelligence (CTI) vendor reports on ransomware and
other cybercriminal campaigns. It is also worth highlighting that while BitLaunch own their
own IP networks, they are a VPS reseller as well who works with DigitalOcean,
Linode, and Vultr, as shown from their website below.

![A screenshot of a computer  AI-generated content may be incorrect.](data:image/png;base64...)

## One website that reviews so-called “offshore services” (offshore[.]cat) has listed BitLaunch as being a “verified” offshore hoster that accepts cryptocurrency, only requires email request confirmation to open an account, and is described as allowing anyone to “create VPSs in seconds, using crypto” making them an attractive hoster for cybercriminals. Their service paired with their CLI tools and Python libraries makes it super easy to stand up C2 servers rapidly. [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjv1-pV3DhHS3U8w6_nMtsmvId1pOfluWLzAuIkXMicBE6YlqFDmB_YGXAIUanm3gRmdP8pt3E5D0wN5NeOXmS2XT5EhrDCNpHacRXHV6Vg1l5yzfEciiv-kgojQOrE8cU5oESFcSfhW__mOB5K6KN2djoe3_y4o0q7bRnrOlkQjZk8kPEa5OmmYZ71fiZj/s16000/offshore_cat.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjv1-pV3DhHS3U8w6_nMtsmvId1pOfluWLzAuIkXMicBE6YlqFDmB_YGXAIUanm3gRmdP8pt3E5D0wN5NeOXmS2XT5EhrDCNpHacRXHV6Vg1l5yzfEciiv-kgojQOrE8cU5oESFcSfhW__mOB5K6KN2djoe3_y4o0q7bRnrOlkQjZk8kPEa5OmmYZ71fiZj/s1158/offshore_cat.png)

## Command and Control (C2) infrastructure on BLNWX

Significant numbers of CobaltStrike C2s among other hacking
tools and malware families have been discovered on BitLaunch. I would like to
thank the owner of the [C2IntelFeedsBot (@drb\_ra)](https://x.com/drb_ra)
account on X/Twitter who assisted with this research by providing their feed of
C2 servers discovered on BitLaunch.

The image below shows a sampling of the known C2 servers
hosted with BitLaunch between 2021 and 2025. The most notable part of this
diagram is the number of CobaltStrike C2 servers in particular. Cobalt Strike
is a well-known C2 framework used by organised cybercriminal groups to launch
ransomware attacks. It is also favoured by state-sponsored threat groups as
well.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0KYlmWTe7r6T7QkSU8z0NqUnmVfg0mywxLJfon5fBqhpOse9DPfohfDYrNfdOStNhgtj48H4HfEi9QbGypFUVRlyyhYJYuEOCPA4qFUxHV2Od4pV45EIdJoZ3dWQbNz5kOWCdkdf_K8MaY3sxjEOFnF64lgJ_M7-TjCzCznA4llRXRlwaA5uVLXn3b0X7/s16000/BitLaunch%20C2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0KYlmWTe7r6T7QkSU8z0NqUnmVfg0mywxLJfon5fBqhpOse9DPfohfDYrNfdOStNhgtj48H4HfEi9QbGypFUVRlyyhYJYuEOCPA4qFUxHV2Od4pV45EIdJoZ3dWQbNz5kOWCdkdf_K8MaY3sxjEOFnF64lgJ_M7-TjCzCznA4llRXRlwaA5uVLXn3b0X7/s1201/BitLaunch%20C2.png)

Over the last few years, several dozen C2 servers have been
identified by the [C2IntelFeedsBot](https://x.com/drb_ra) and each
year, the number of C2s has continued to grow as more cybercriminals identify
BitLaunch as a preferable service to support their ransomware campaigns.

The image below displays the totals calculated between “2021-06-26
12:33:41" and "2025-02-05 18:46:10." It is not a complete
picture by any means, but this independently verifiable data gives a decent
idea of the rate at which BitLaunch is being used by cybercriminals, with each
year since 2022 has trended upwards.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsYHh8LqsX0ZNJGiES-yW93QmHuRixA5MC7g6pch0X9yED5Q7HnUKABVK6zeIV_OmwwDytkmJNe_KuEFLneJXz40eM_H0CNPSj_xLg2lFrTkCXDYZCt3L71ZA2zyQudGqh1LRwMjMZO-yKVFC8aEhPqdvA9orANCInHgtPVDcKik8KVpMBv_LiLOwtuzz9/s16000/C2_numbers.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsYHh8LqsX0ZNJGiES-yW93QmHuRixA5MC7g6pch0X9yED5Q7HnUKABVK6zeIV_OmwwDytkmJNe_KuEFLneJXz40eM_H0CNPSj_xLg2lFrTkCXDYZCt3L71ZA2zyQudGqh1LRwMjMZO-yKVFC8aEhPqdvA9orANCInHgtPVDcKik8KVpMBv_LiLOwtuzz9/s945/C2_numbers.png)

One of the interesting things about CobaltStrike is that it
is a commercial offensive security tool (OST). It is issued to legitimate
customers through licenses, which have a unique watermark. While there have
been several cracked v...