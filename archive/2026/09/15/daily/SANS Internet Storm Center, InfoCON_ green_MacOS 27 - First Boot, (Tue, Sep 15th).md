---
title: MacOS 27 - First Boot, (Tue, Sep 15th)
url: https://isc.sans.edu/diary/rss/33340
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-15
fetch_date: 2026-09-16T07:06:12.865627
---

# MacOS 27 - First Boot, (Tue, Sep 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33336)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [MacOS 27 - First Boot](/forums/diary/MacOS%2B27%2BFirst%2BBoot/33340/)

**Published**: 2026-09-15. **Last Updated**: 2026-09-15 15:23:45 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/MacOS%2B27%2BFirst%2BBoot/33340/#comments)

I have not done this type of diary in a while: What traffic will you see from a system on boot, before a user logs in? I just took a quick look at macOS 27 "Golden Gate" to see what traffic you should expect. Here are some of the highlights:

I captured about 300 packets. This was likely inflated for this particular system as it connected via Wi-Fi and wired network interfaces. Each network interface will do its own DHCP/IP discovery during boot. I only used router advertisements for IPv6, not DHCPv6.

### IPv6 Neighbor Discovery - Duplicate Address Discovery

As it is supposed to, macOS 27 does standard compliant duplicate address discovery before accepting an IPv6 address. It does use ICMPv6 nonces to prevent some spoofing DoS attacks:

> `:: > ff02::1:ff8f:bd1c ICMPv6 86  Neighbor Solicitation for fe80::14e5:ff56:308f:bd1c
> Internet Control Message Protocol v6
>     Type: Neighbor Solicitation (135)
>     Code: 0
>     Checksum: 0xd8bb [correct]
>     [Checksum Status: Good]
>     Reserved: 00000000
>     Target Address: fe80::14e5:ff56:308f:bd1c
>     ICMPv6 Option (Nonce)
>         Type: Nonce (14)
>         Length: 1 (8 bytes)
>         Nonce: 30480a0a9b7c`

### DNS Traffic

macOS 27 resolved these hostnames during boot:

* `_dns.resolver.arpa (SVCB)`
  Discover secre (DNS over HTTPS...) DNS resolvers
* `1-courier.push.apple.com`???????, `1-courier.sandbox.push.apple.com`
  Used for Apple push messaging
* `126.2.5.10.in-addr.arpa`
  reverse resolve the local IP address
* `albert.apple.com`
  This hostname is used by Apple for device activation (do not block it, and it does certificate pinning, so do not TLS intercept it)
* `appleid.apple.com`
  verifying Apple ID associated with the system
* `ipv4only.arpa`
  For IPv6-only networks, this record resolves to a NAT64 IPv6 prefix that can be used to reach IPv4-only services. (RFC 7050 and RFC 8880)
* `www.apple.com`
  Used to discover captive portals.

### TCP Options

TCP options have not changed for a few years now in macOS. macOS 27 still uses the somewhat more conservative window scale of "6". It also still uses ECN and random timestamps.

I recorded four TCP connection during boot:

1. TLS to "albert.apple.com" (HTTPS on port 443, IPv4).
2. OCSP connection to ocsp.digicert.com to verify the "albert.apple.com" certificate (HTTP on port 80, IPv6)
3. TLS to "init.push.apple.com" (port 443)
4. TLS connection to courier.push.apple.com (port 5223)

### Multicast DNS

Just like prior macOS versions, macOS 27 does advertise any services via multicast DNS on port 5353/udp

### User Agents

During boot, the only visible user-agent is contained in the OCSP request: com.apple.trustd/3.0. The user agent is the same as prior versions of macOS. The user agent for Safari is:

Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0 Safari/605.1.15

The version of Safari is indicated as "27.0", but oddly enough, the OS version states "Intel Mac OS X 10\_15\_7" (this was collected from a Mac with "M" CPU).

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [macOS](/tag.html?tag=macOS)

[0 comment(s)](/diary/MacOS%2B27%2BFirst%2BBoot/33340/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33336)

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