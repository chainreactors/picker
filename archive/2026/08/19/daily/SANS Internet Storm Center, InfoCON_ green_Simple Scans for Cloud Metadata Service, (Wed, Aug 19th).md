---
title: Simple Scans for Cloud Metadata Service, (Wed, Aug 19th)
url: https://isc.sans.edu/diary/rss/33260
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-19
fetch_date: 2026-08-20T02:56:38.050243
---

# Simple Scans for Cloud Metadata Service, (Wed, Aug 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/33254)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Simple Scans for Cloud Metadata Service](/forums/diary/Simple%2BScans%2Bfor%2BCloud%2BMetadata%2BService/33260/)

**Published**: 2026-08-19. **Last Updated**: 2026-08-19 14:24:58 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Simple%2BScans%2Bfor%2BCloud%2BMetadata%2BService/33260/#comments)

Cloud providers typically expose a REST API at 169.254.169.254 that allows code running on virtual machines to retrieve machine-specific data. Some of the data is more or less harmless, such as the region the machine is running in or its MAC and IP addresses. However, the service may also be used to retrieve credentials for IAM roles and service account tokens.

Why 169.254.169.254, and not, for example, an RFC1918 address or loopback? RFC 1918 addresses are usually used and routed internally by cloud providers. Interfering with them would be risky and add complexity. The loopback interface is often treated differently from a normal interface, particularly in containers, and is not well-suited for traffic that must be controlled by the operating system's packet-filtering mechanisms. 169.254.169.254 is part of the link local address prefix 169.254/16 [[RFC3927](https://www.rfc-editor.org/info/rfc3927/)]. These addresses are specifically not routable, unlike RFC 1918 addresses, which may be routed locally ("The host MUST NOT send a packet with an IPv4 Link-Local destination address to any router for forwarding.").

This unique property of link-local addresses makes them ideal for addresses used multiple times , and that must never be routed. An attacker will not be able to reach out to this address remotely. But there is a "trick": the virtual machine itself can reach the metadata service, and if an attacker uses server-side request forgery (SSRF) to trick the server into sending the request, the address may be reached. The attacker could now use this SSRF vulnerability to retrieve secrets [1].

Probably the best-known breach assisted by the metadata service was Capital One, which led to a huge data leak and later to the prosecution of the attacker. Since then, we have seen attempts to exploit SSRF vulnerabilities in order to access the metadata service. But what I notied today is a widespread scan that appears to be not targeted at a particular vulnerability:

> `GET /?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/ HTTP/1.1
> Host: [redacted]
> User-Agent: Go-http-client/1.1
> Accept-Encoding: gzip`

This scan does not appear to target a specific vulnerability; it is a more generic attempt to find "some" vulnerability, and it is not clear which one. If you have any insight, please let me know :)

As far as securing the metadata service goes, Amazon used version 2 of the service following the Capital One breach. A simple "GET" request is no longer sufficient, making SSRF access highly unlikely.

Special IPv6 note: IPv6 uses fd20:ce::254, which is a unique local address, more like an RFC 1918 address instead of an IPv6 link-local fe80:: address.

[1] https://www.sans.org/blog/cloud-instance-metadata-services-imds-

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ids cloud metadata services surf](/tag.html?tag=ids cloud metadata services surf)

[0 comment(s)](/diary/Simple%2BScans%2Bfor%2BCloud%2BMetadata%2BService/33260/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33254)

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