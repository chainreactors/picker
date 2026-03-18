---
title: IPv4 Mapped IPv6 Addresses, (Tue, Mar 17th)
url: https://isc.sans.edu/diary/rss/32804
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-17
fetch_date: 2026-03-18T04:22:46.250633
---

# IPv4 Mapped IPv6 Addresses, (Tue, Mar 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32800)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [IPv4 Mapped IPv6 Addresses](/forums/diary/IPv4%2BMapped%2BIPv6%2BAddresses/32804/)

**Published**: 2026-03-17. **Last Updated**: 2026-03-17 11:36:48 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/IPv4%2BMapped%2BIPv6%2BAddresses/32804/#comments)

Yesterday, in my diary about the scans for "/proxy/" URLs, I noted how attackers are using IPv4-mapped IPv6 addresses to possibly obfuscate their attack. These addresses are defined in [RFC 4038](https://datatracker.ietf.org/doc/html/rfc4038). These addresses are one of the many transition mechanisms used to retain some backward compatibility as IPv6 is deployed. Many modern applications use IPv6-only networking code. IPv4-mapped IPv6 addresses can be used to represent IPv4 addresses in these cases. IPv4-mapped IPv6 addresses are not used on the network, but instead, translated to IPv4 before a packet is sent.

To map an IPv4 address into IPv6, the prefix "::ffff:/96" is used. This leaves the last 32 bits to represent the IPv4 address. For example, "10.5.2.1" turns into "::ffff:0a05:0201". Many applications display the last 4 bytes in decimal format to make it easier to read. For example, you will see "::ffff:10.5.2.1".

If IPv4-mapped IPv6 addresses can be used depends on the particular application. Here are a few examples, but feel free to experiment yourself:

ping6 on macOS:

> % ping6 ::ffff:0a05:0201
> PING6(56=40+8+8 bytes) ::ffff:10.5.2.147 --> ::ffff:10.5.2.1
> ping6: sendmsg: Invalid argument
> ping6: wrote ::ffff:0a05:0201 16 chars, ret=-1

Note that ping6 displays the IPv4 address in decimal format but refuses to send any packets, since they would be IPv4 packets, not IPv6.

> % ping ::ffff:0a05:0201
> ping: cannot resolve ::ffff:0a05:0201: Unknown host

Regular IPv4 ping fails to recognize the format for an IP address, and instead interprets it as a hostname, which fails.

ping6 on Linux does not return an error. It just appears to "hang," and no packets are emitted. Running strace shows:

> `sendto(3, "\200\0\0\0{\263\0\4i:\271i\0\0\0\0(\200\6\0\0\0\0\0\20\21\22\23\24\25\26\27"..., 64, 0, {sa_family=AF_INET6, sin6_port=htons(58), sin6_flowinfo=htonl(0), inet_pton(AF_INET6, "::ffff:10.5.2.1", &sin6_addr), sin6_scope_id=0}, 28) = -1 ENETUNREACH (Network is unreachable)
> recvmsg(3, {msg_namelen=28}, MSG_DONTWAIT|MSG_ERRQUEUE) = -1 EAGAIN (Resource temporarily unavailable)`

It attempts to set up an IPv6 connection based on the "AF\_INET6" argument in the inet\_pton call, but this fails for the mapped IPv4 address.

ssh, on the other hand (on MacOS and Linux) works just fine:

> $ ssh ::ffff:0a05:0201 -p 11460
> The authenticity of host '[::ffff:10.5.2.1]:11460 ([::ffff:10.5.2.1]:11460)' can't be established.

The traffic is sent properly as IPv4 traffic.

curl is kind of interesting in that it uses the IPv4-mapped IPv6 address as a host header:

> $ curl -i http://[::ffff:0a80:010b]
> HTTP/1.1 301 Moved Permanently
> Server: nginx
> Date: Tue, 17 Mar 2026 11:32:10 GMT
> Content-Type: text/html
> Content-Length: 162
> Connection: keep-alive
> Location: https://[::ffff:0a80:010b]/

I tried a couple of different web servers, and they all acted the same way. Browsers like Safari and Chrome could also use these addresses. In browsers, it may be possible to evade some filters by using IPv4-mapped IPv6 addresses when simple string matching is used. Note how in URLs the IPv6 address must be enclosed in square brackets to avoid "colon confusion".

Any ideas what else to test or how to possibly use or abuse these addresses? Remember that on the network, you will end up with normal IPv4 traffic, not IPv6 traffic using IPv4-mapped IPv6 addresses.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/IPv4%2BMapped%2BIPv6%2BAddresses/32804/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32800)

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