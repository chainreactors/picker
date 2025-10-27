---
title: Beneath the MASQUE - a dive into Network Relay technology on Apple platforms
url: https://jedda.me/beneath-the-masque-network-relay-on-apple-platforms/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-09
fetch_date: 2025-10-06T22:54:37.589667
---

# Beneath the MASQUE - a dive into Network Relay technology on Apple platforms

## [![Jedda Wignall](https://jedda.me/content/images/2023/11/Jedda.svg)](https://jedda.me)

Menu

**[Jedda Wignall](/author/jedda/)**

May 30, 2025  **·**  39 min read

# Beneath the MASQUE - a dive into Network Relay technology on Apple platforms

A technology that Apple describes as a "[**modern alternative to VPNs**](https://support.apple.com/en-au/guide/deployment/dep91a6e427d/web)", is in production use today on [**hundreds of millions of devices**](https://support.apple.com/en-au/102602)and has been [**embraced by some of the largest players**](https://blog.cloudflare.com/zero-trust-warp-with-a-masque/) on the internet. Sounds intriguing, but outside of select big tech and academics, how much do we really know about it?

At WWDC in 2023, Apple presented [**Ready, set, relay**](https://developer.apple.com/videos/play/wwdc2023/10002/); an introductory session which included a call to *"*[*start replacing*](https://developer.apple.com/videos/play/wwdc2023/10002/?time=718) *the use of VPNs with relays that are easier to manage and provide a more seamless user experience".* During this session, [Cisco Secure](https://blogs.cisco.com/security/youve-heard-the-security-service-edge-sse-story-before-but-we-re-wrote-it) received an explicit callout as an example of a relay service designed to facilitate access to a private enterprise server. We are now almost 2 years removed, and have only seen a small additional number of [commercial](https://smallstep.com/product/saas-apps/index.html) [offerings](https://learn.jamf.com/en-US/bundle/jamf-connect-documentation-current/page/Private_Access.html) that explicitly lead with relay technologies, and only very sparse discourse that usually remains extremely theoretical in nature. In particular, I'm surprised that we haven't seen more community discussion or questioning about prescriptive implementations of this technology, and hopefully, this article can kick off some interesting conversations within the Apple admins community at large.

![](https://jedda.me/content/images/2025/05/Header.drawio.png)

A recreation of an incredibly simple graphic from Apple's [****Ready, Set, Relay****](https://developer.apple.com/videos/play/wwdc2023/10002/) session. As I hope you'll see through this article, in some ways this is an obvious oversimplification, and in other ways, not at all. At its core, it really should (and can) be this simple.

In this article, I'll try to introduce some of the concepts and history behind Network Relay technologies as well as dive into an open-source implementation using [Envoy proxy](https://www.envoyproxy.io). Through this, we'll explore some of the current limitations and implementation considerations and discuss some interesting use cases both today and into the future. And yes - we will even get to integrate with and show off an **awesome use case** for [Managed Device Attestation](https://jedda.me/managed-device-attestation-a-technical-exploration/); one of my favourite topics!

Much has been written about the underpinnings of MASQUE & relay technologies, so this article won't go too deep down into the [OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) but will instead focus on the practical implementation realities and possibilities around Network Relay on Apple platforms. If you want a deeper understanding of the underlying transports, intention and guts of the protocols, then there are a few companion pieces that I have enjoyed and are definitely worth reading (and can even be consumed first if you are genuinely interested in a comprehensive technical deep dive):

* Cloudflare - [**A Primer on Proxies**](https://blog.cloudflare.com/a-primer-on-proxies/) & the follow-up [**Unlocking QUIC’s proxying potential with MASQUE**](https://blog.cloudflare.com/unlocking-quic-proxying-potential/)
* Smallstep **-** [**Why we prefer MASQUE Relays**](https://smallstep.com/blog/masque-relays-vs-vpns/)
* APNIC -[**Hiding behind MASQUEs**](https://blog.apnic.net/2023/03/23/hiding-behind-masques/) (this one goes a little more into the privacy implications and Oblivious DNS and HTTP)

As I think you'll see, this topic is a wide-ranging maze that can lead you off on all sorts of garden paths as you traverse the server infrastructure, the network and the behaviour of the client, amongst other futurist concepts and dreams for the web. Consequently, this article ended up fairly long form in an attempt not to assume too much knowledge and appeal to a wider audience of Apple admins, Infosec and network folks. If you just want to see some cool examples, there will be no hurt feelings if you skip down the page.

For the most part, this is a written piece, but for the technical examples, I've included videos that better show off how relays operate across macOS, iOS and the proxy infrastructure. As I was writing this, I realised it's almost impossible to fully show off Network Relay on the client and server side simultaneously just by presenting some log entries and dry configurations. So with all that, strap in, [put on some appropriate background music](https://www.youtube.com/watch?v=a3jwPhPT2AI&ab_channel=Pollux) and let's dive in together to Network Relay on Apple platforms!

---

## 📖 A brief history of HTTP

**In the beginning, there was HTTP/1.0** (well, technically [0.9](https://www.w3.org/Protocols/HTTP/AsImplemented.html)) - a simple, text-based protocol built on top of TCP. It did exactly what the early web needed: fetch and deliver static documents, one request at a time. HTTP/1.1 followed with important upgrades, including persistent connections, basic pipelining, and the introduction of the [CONNECT method](https://datatracker.ietf.org/doc/html/rfc2616#section-9.9), a feature that enabled early proxying scenarios.

Despite these improvements, HTTP/1.1 still had critical limitations, and these were particularly exposed when being used as part of a proxy. Persistent connections and pipelining reduced overhead, but also exposed a key bottleneck: [**head-of-line blocking**](https://en.wikipedia.org/wiki/Head-of-line_blocking). The concept here is pretty simple - with multiple requests sharing a single TCP connection, and a need to send and receive in a specific order, a single slow or delayed response could stall everything behind it. This made proxying inefficient and unreliable, especially under high load or poor network conditions.

![](https://jedda.me/content/images/2025/05/Pipelining-2.png)

A simplified representation of HTTP/1 pipelining and its impact on Head of Line Blocking. A client requests 4 resources (HTML, CSS, JS, images, etc.) from a HTTP server - these must be processed in order, so if B is very slow, the client must wait for C and D (even if they would be individually quicker to access).

Additionally, traditional HTTP proxies were built for one job: handling HTTP traffic. They could do so either explicitly (by being configured on the client) or transparently (on an upstream middle-box device such as a firewall), and in the case of HTTPS traffic, often terminated TLS and deliberately [man-in-the-middled](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) client traffic. As such, this style of proxy was (and [very much still](https://docs.fortinet.com/document/fortigate/6.2.16/cookbook/300428/explicit-web-proxy) is) commonly used for caching, filtering, or outbound access control.

[HTTP/2](https://www.cloudflare.com/learning/performance/http2-vs-http1.1/) wasn’t standardised until 2015 - almost 16 years after HTTP/1.1. It marked a significant departure from its predecessors, moving from a text-based protocol to a more efficient binary format, which allowed for more efficient parsing and improved performance. This also introduced connection multiplexing, which allowed multiple requests and responses to be sent over a single connection at the same time without blocking one another, helping to mitigate **some** of the head-of-lin...