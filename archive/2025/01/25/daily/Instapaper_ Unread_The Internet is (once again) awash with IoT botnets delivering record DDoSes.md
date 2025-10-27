---
title: The Internet is (once again) awash with IoT botnets delivering record DDoSes
url: https://arstechnica.com/security/2025/01/the-internet-is-once-again-awash-with-iot-botnets-delivering-record-ddoses/
source: Instapaper: Unread
date: 2025-01-25
fetch_date: 2025-10-06T20:13:41.863334
---

# The Internet is (once again) awash with IoT botnets delivering record DDoSes

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

THE IDEAL DDOS TOOL

# The Internet is (once again) awash with IoT botnets delivering record DDoSes

Bigger, badder DDoSes are flooding the Internet. Dismal IoT security is largely to blame.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Jan 22, 2025 10:10 am
| [50](https://arstechnica.com/security/2025/01/the-internet-is-once-again-awash-with-iot-botnets-delivering-record-ddoses/#comments "50 comments")

[![Person in black hood with laptop trying to cyberattack.](https://cdn.arstechnica.net/wp-content/uploads/2022/12/ddos-for-hire-300x167.jpg)
![Person in black hood with laptop trying to cyberattack.](https://cdn.arstechnica.net/wp-content/uploads/2022/12/ddos-for-hire.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2022/12/ddos-for-hire.jpg)

Credit:
Getty Images

Credit:
Getty Images

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

We’re only three weeks into 2025, and it’s already shaping up to be the year of Internet of Things-driven DDoSes. Reports are rolling in of threat actors infecting thousands of home and office routers, web cameras, and other Internet-connected devices.

Here is a sampling of research released since the first of the year.

## Lax security, ample bandwidth

A [post](https://blog.cloudflare.com/ddos-threat-report-for-2024-q4/) on Tuesday from content-delivery network Cloudflare reported on a recent distributed denial-of-service attack that delivered 5.6 terabits per second of junk traffic—a new record for the largest DDoS ever reported. The deluge, directed at an unnamed Cloudflare customer, came from 13,000 IoT devices infected by a variant of Mirai, a potent piece of malware with a [long history](https://arstechnica.com/information-technology/2016/09/why-the-silencing-of-krebsonsecurity-opens-a-troubling-chapter-for-the-net/) of delivering massive DDoSes of once-unimaginable sizes.

The same day, security company Qualys published [research](https://blog.qualys.com/vulnerabilities-threat-research/2025/01/21/mass-campaign-of-murdoc-botnet-mirai-a-new-variant-of-corona-mirai) detailing a "large-scale, ongoing operation" dubbed the Murdoc Botnet. It exploits vulnerabilities to install a Mirai variant, primarily on AVTECH Cameras and Huawei HG532 routers. Late Tuesday afternoon, searches like [this one](https://en.fofa.info/result?qbase64=Ym9keT0ibXVyZG9jX2JvdG5ldCI%3D) indicated devices on more than 1,500 IP addresses were compromised, up from a figure of 1,300 reported a few hours earlier by Qualys. These devices are also waging DDoSes. It’s unknown if Cloudflare and Qualys are reporting on the same botnet.

Last week, security company Trend Micro [said](https://www.trendmicro.com/en_us/research/25/a/iot-botnet-linked-to-ddos-attacks.html) it also found an IoT botnet. The botnet, which is driven by variants of Mirai and a similar malware family known as Bashlite, has been delivering large-scale DDoSes since the end of last year, primarily to targets in Japan.

A [report](https://blogs.infoblox.com/threat-intelligence/one-mikro-typo-how-a-simple-dns-misconfiguration-enables-malware-delivery-by-a-russian-botnet/) early last week from security firm Infoblox revealed a botnet comprising 13,000 devices—mostly routers manufactured by MikroTik—that researchers likened to “a large cannon, poised and ready to unleash a barrage of malicious activities.” The primary activity Infoblox has observed from this botnet is a flood of malicious spam emails that attempt to trick recipients into executing malicious file attachments.

On January 7, researchers at China-based security firm Xlab [said](https://blog.xlab.qianxin.com/gayfemboy-en/) they've been tracking an IoT botnet since last February. The botnet, named with an offensive term, was mostly unremarkable until later in the year when it began targeting zero-day and recently fixed n-day vulnerabilities to infect more devices. By November, it began exploiting a [zero-day](https://vulncheck.com/blog/four-faith-cve-2024-12856?ref=blog.xlab.qianxin.com) in industrial routers sold by Four-Faith and unknown vulnerabilities in routers sold by Neterbit and in smart home devices from Vimar. The botnet comprises on average 15,000 compromised devices, mostly located in China, the United States, Iran, Russia, and Turkey. Threat actors are using it to wage DDoSes.

IoT devices are an ideal DDoS tool from the standpoint of an attacker. They typically ship running a version of Linux that is missing months, if not years, of security updates; infections are difficult to detect; and the devices often have lots of available bandwidth. In 2016—when IoT botnets were a new phenomenon—they were observed delivering DDoSes as high as 1Tbps, a [once-unimaginable size](https://arstechnica.com/information-technology/2016/09/botnet-of-145k-cameras-reportedly-deliver-internets-biggest-ddos-ever/). Cloudflare’s revelation on Tuesday that it observed and blocked an IoT botnet delivering a DDoS more than five times bigger indicates that these attacks continue to grow more potent.

A Cloudflare spokesperson said in an email that the attack was delivered not just by IoT devices but also virtual machines hosted inside cloud environments. The hybrid approach may be one example of the growing evolution of botnets in the race to create larger DDoSes.

The most effective way to protect IoT devices from compromise is to replace all default passwords with long, randomly generated ones that are unique to each device. Turning off remote management is also a good move when possible. And as always, installing security updates promptly is a must.

[![Photo of Dan Goodin](https://cdn.arstechnica.net/wp-content/uploads/2018/10/Dang.jpg)](https://arstechnica.com/author/dan-goodin/)

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at [here](https://infosec.exchange/%40dangoodin) on Mastodon and [here](https://bsky.app/profile/dangoodin.bsky.social) on Bluesky. Contact him on Signal at DanArs.82....