---
title: From IP packets to HTTP: the many faces of our Oxy framework
url: https://buaq.net/go-156155.html
source: unSafe.sh - 不安全
date: 2023-03-31
fetch_date: 2025-10-04T11:13:34.226831
---

# From IP packets to HTTP: the many faces of our Oxy framework

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/574a7eb216bbfc8193e96843dd989d8a.jpg)

From IP packets to HTTP: the many faces of our Oxy framework

Loading...
*2023-3-30 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-156155.htm)
阅读量:29
收藏*

---

Loading...

* [![Nuno Diegues](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/04/xlarge-1.jpg)](https://blog.cloudflare.com/author/nuno/)

![From IP packets to HTTP: the many faces of our Oxy framework](https://blog.cloudflare.com/content/images/2023/03/image2-27.png)

We have recently [introduced Oxy](https://blog.cloudflare.com/introducing-oxy/), our Rust-based framework for proxies powering many Cloudflare services and products. Today, we will explain why and how it spans various layers of the [OSI model](https://en.wikipedia.org/wiki/OSI_model), by handling directly raw IP packets, TCP connections and UDP payloads, all the way up to application protocols such as HTTP and SSH.

### On-ramping IP packets

An application built on top of Oxy defines — in a configuration file — the on-ramps that will accept ingress traffic to be proxied to some off-ramp. One of the possibilities is to on-ramp raw IP packets. But why operate at that layer?

The answer is: [to power Cloudflare One](https://blog.cloudflare.com/introducing-cloudflare-one/), our network offering for customers to extend their private networks — such as offices, data centers, cloud networks and roaming users — with the Cloudflare global network. Such private networks operate based on [Zero Trust principles](https://blog.cloudflare.com/stronger-bridge-to-zero-trust/), which means every access is authenticated and authorized, contrasting with legacy approaches where you can reach every private service after authenticating once with the Virtual Private Network.

To effectively extend our customer’s private network into ours, we need to support arbitrary protocols that rely on the Internet Protocol (IP). Hence, we on-ramp Cloudflare One customers’ traffic at (OSI model) layer 3, as a stream of IP packets. Naturally, those will often encapsulate TCP streams and UDP sessions. But nothing precludes other traffic from flowing through.

### IP tunneling

Cloudflare’s operational model dictates that [every service, machine and network](https://blog.cloudflare.com/how-cloudflares-architecture-allows-us-to-scale-to-stop-the-largest-attacks/) be operated in an homogeneous way, usable by every one of our customers the same way. We essentially have a gigantic multi-tenanted system. Simply on-ramping raw IP packets does not suffice: we must always move the IP packets within the scope of the tenant they belong to.

This is why we introduced the concept of IP tunneling in Oxy: every IP packet handled has context associated with it; at the very least, the tenant that it belongs to. Other arbitrary contexts can be added, but that is up to each application (built on top of Oxy) to define, parse and consume in its Oxy hooks. This allows applications to [extend and customize](https://blog.cloudflare.com/introducing-oxy/) Oxy’s behavior.

You have probably heard of (or even used!) [Cloudflare Zero Trust WARP](https://blog.cloudflare.com/warp-for-desktop/): a client software that you can install on your device(s) to create virtual private networks managed and handled by Cloudflare. You begin by authenticating with your Cloudflare One account, and then the software will on-ramp your device’s traffic through the nearest Cloudflare data center: either to be upstreamed to Internet public IPs, or to other Cloudflare One connectors, such as [another WARP device](https://blog.cloudflare.com/warp-to-warp/).

Today, WARP routes the traffic captured in your device (e.g. your smartphone) via a WireGuard tunnel that is terminated in a server in the nearest Cloudflare data center. That server then opens an IP tunnel to an Oxy instance running on the same server. To convey context about that traffic, namely the [identity of the tenant](https://blog.cloudflare.com/gateway-swg-3/), some context must be attached to the IP tunnel.

For this, we use a [Unix SOCK\_SEQPACKET](https://man7.org/linux/man-pages/man7/unix.7.html), which is a datagram-oriented socket exposing a connection-based interface with reliable and ordered delivery — it only accepts connections locally within the machine where it is bound to. Oxy receives the context in the first datagram, which the application parses — could be any format the application using Oxy desires. Then all subsequent datagrams are assumed to be raw self-describing IP packets, with no overhead whatsoever.

Another example are the on-ramps of [Magic WAN](https://blog.cloudflare.com/magic-wan-firewall/), such as [GRE](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-gre-tunneling/) or [IPsec](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-ipsec/) tunnels, which also bring raw IP packets from customer’s networks to Cloudflare data centers. Unlike WARP, where its IP packets are decapsulated in user space, for GRE and IPsec we rely on the Linux kernel to do the job for us. Hence, we have no state whatsoever between two consecutive IP packets coming from the same customer, as the Linux kernel is routing them independently.

To accommodate the differences between IP packet handling in user space and the kernel, Oxy differentiates two types of IP tunnels:

* *Connected IP tunnels* — as explained for WARP above, where the context is passed once, in the first datagram of the IP Tunnel SEQPACKET connection
* *Unconnected IP tunnels* — used by Magic WAN, where each IP packet is encapsulated (using GUE, i.e. [Generic UDP Encapsulation](https://datatracker.ietf.org/meeting/91/materials/slides-91-nvo3-1)) to accommodate the context and unconnected UDP sockets are used

Encapsulating every IP packet comes at the cost of extra CPU usage. But moving the packet around to and from an Oxy instance does not change much regardless of the encapsulation, as we do not have [MTU limitations](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-mtu/) inside our data centers. This way we avoid causing IP packet fragmentation, whose reassembly takes a toll on CPU and Memory usage.

### Tracking IP flows

Once IP packets arrive to Oxy, regardless of how they on-ramp, we must decide what to do with them. We decided to rely on the idea of IP flows, as that is inherent to most protocols: a point to point interaction will generally be bounded in time and follow some type of state machine, either known by the transport or by the application protocol.

We perform flow tracking to detect IP flows. When handling an on-ramped IP packet, we parse its IP header and possible transport (i.e. OSI Model layer 4) header. We use the excellent [etherparse Rust crate](https://crates.io/crates/etherparse) for this purpose, which parses the flow signature, with a source and destination IP address, ports (optional) and protocol. We then look up whether there is already a known IP flow for that signature: if so, then the packet is proxied through the path already determined for that flow towards its off-ramp. If the flow is new, then its upstream route is computed and memoized for future packets. This is in essence what routers do, and to some extent Oxy handling of IP packets is meant to operate as a router.

The interesting thing about tracking IP flows is that we can now expose their lifetime events to the application built on top of Oxy, via its hooks. Applications can then use these events for interesting operations, such as:

* Applying Zero Trust principles b...