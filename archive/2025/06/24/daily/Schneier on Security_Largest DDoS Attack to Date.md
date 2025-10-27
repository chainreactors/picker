---
title: Largest DDoS Attack to Date
url: https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html
source: Schneier on Security
date: 2025-06-24
fetch_date: 2025-10-06T22:55:22.695190
---

# Largest DDoS Attack to Date

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Largest DDoS Attack to Date

It was a recently unimaginable [7.3 Tbps](https://arstechnica.com/security/2025/06/record-ddos-pummels-site-with-once-unimaginable-7-3tbps-of-junk-traffic/):

> The vast majority of the attack was delivered in the form of User Datagram Protocol packets. Legitimate UDP-based transmissions are used in especially time-sensitive communications, such as those for video playback, gaming applications, and DNS lookups. It speeds up communications by not formally establishing a connection before data is transferred. Unlike the more common Transmission Control Protocol, UDP doesn’t wait for a connection between two computers to be established through a handshake and doesn’t check whether data is properly received by the other party. Instead, it immediately sends data from one machine to another.
>
> UDP flood attacks send extremely high volumes of packets to random or specific ports on the target IP. Such floods can saturate the target’s Internet link or overwhelm internal resources with more packets than they can handle.
>
> Since UDP doesn’t require a handshake, attackers can use it to flood a targeted server with torrents of traffic without first obtaining the server’s permission to begin the transmission. UDP floods typically send large numbers of datagrams to multiple ports on the target system. The target system, in turn, must send an equal number of data packets back to indicate the ports aren’t reachable. Eventually, the target system buckles under the strain, resulting in legitimate traffic being denied.

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [denial of service](https://www.schneier.com/tag/denial-of-service/)

[Posted on June 23, 2025 at 7:04 AM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html#comments)

### Comments

HP •
[June 23, 2025 8:41 AM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html/#comment-446079)

Very cool

Clive Robinson •
[June 23, 2025 10:35 AM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html/#comment-446081)

@ ALL,

A simple observation,

“As bandwidth goes up and latency goes down, the data rate for a DDoS will go up to compensate.”

So 7.3 Tbps today double that by Xmas 2026…

There are a couple of solutions to DDoS,

1, Charge per packet.

Neither of which are going to be popular with users who now have,

“The Vegas Buffet mentality towards Internet service provision.

Though one thing they left out when they said,

> *“Unlike the more common Transmission Control Protocol, UDP doesn’t wait for a connection between two computers to be established through a handshake and doesn’t check whether data is properly received by the other party. Instead, it immediately sends data from one machine to another.”*

UDP is easy to spoof, because due to the way it’s designed the return IP address and port don’t have to be valid.

If people look back in history in the past instead of an IP Address a Network Address was used, thus forcing a reply to every IP address in the Network Address, and this can be a significant “force multiplier”.

In theory that should not work any more but there are other tricks that still work…

Peter A. •
[June 23, 2025 11:16 AM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html/#comment-446085)

@Clive Robinson:

I am not sure what you really mean regarding your two solutions.

Charging per packet won’t work unless strong authentication and attribution – worldwide – is implemented for every Internet connection or even user. That’s next to impossible in the current architecture – or should we go back to X.25 times or similar… paying the National Post Office for both time of connection and amount of packets transferred.

Even if we do, what do you mean to achieve?

Charging per packet? outgoing or incoming? Since the perpetrators of DDoS attacks do not use their own resources, paid by them, but stolen ones, they won’t be affected, everybody else would be charged for outgoing traffic. And the victim could be bankrupt in minutes, if not seconds, if incoming traffic is charged for. DDoSers could be even more motivated to wreak havoc – in addition to disrupting or bankrupting their target (and getting paid for it, possibly), they might be encouraged to do pure evil by making everyone and the dog pay a little extra for no gain to the perps.

Limiting bandwidth on output – I can’t see how it would help. Upload rates are already very limited for most consumer connections, and DDoSers can just spread their load thinner – as long as there’s plenty of devices to infect and recruit into botnets. On input? Input is already limited by contracts and physical links, and the whole purpose of DDoS is to saturate this limit.

Sorry, maybe I am completely missing something in your reasoning.

lurker •
[June 23, 2025 2:05 PM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html/#comment-446087)

“A total of 34,500 ports were targeted, indicating the thoroughness and well-engineered nature of the attack.”

Oh really? Carpet bombing is usually about sheer volume, not precision.

“The target system, in turn, must send an equal number of data packets back to indicate the ports aren’t reachable.”

Surely dropping unwanted packets must be more economical and secure. Besides, they already said UDP doesn’t need replies.

Some of the comments noted that this read like a slow news story. Oh, and why isn’t “past its Use by Date” QoD non-routable?

Nameless •
[June 23, 2025 2:31 PM](https://www.schneier.com/blog/archives/2025/06/largest-ddos-attack-to-date.html/#comment-446089)

I agree with @lurker:

“Surely dropping unwanted packets must be more economical and secure. Besides, they already said UDP doesn’t need replies.”

That was my first thought upon reading: “must send an equal number of data packets back to indicate the ports aren’t reachable.”

I realize the internet (both TCP and UDP, and ICMP replies) was all designed in an age when it wasn’t imagined anyone would ever possibly use any technology for malicious purposes (eye roll), so courtesy replies used to be common, expected, the norm, etc… but we’ve gone past that for many decades now and from a security standpoint nobody should ever be required to send back a reply to a packet it doesn’t recognize or expect in some way. It doesn’t even matter if it “breaks a protocol” of some kind… if you don’t recognize it as valid and need it in some way, drop it. Period. That’s the only possible responsible secure thing to do.

Unfortunately a lot of antiquated infrastructure exists out there still isn’t operating from a security standpoint even after all these decades.

Clive Robinson •
[June 23, 2025 8:17 PM](https://www.schneier.com/blo...