---
title: Oxy: Fish/Bumblebee/Splicer subsystems to improve reliability
url: https://buaq.net/go-159675.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:31.369858
---

# Oxy: Fish/Bumblebee/Splicer subsystems to improve reliability

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

![](https://8aqnet.cdn.bcebos.com/90f48bdaf20836843315b10c5686d356.jpg)

Oxy: Fish/Bumblebee/Splicer subsystems to improve reliability

Loading...
*2023-4-20 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-159675.htm)
阅读量:31
收藏*

---

Loading...

* [![Quang Luong](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/13181907.png)](https://blog.cloudflare.com/author/quang/)
* [![Chris Branch](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2017/03/IQJFZVny.jpg)](https://blog.cloudflare.com/author/chris/)

![Oxy: Fish/Bumblebee/Splicer subsystems to improve reliability](https://blog.cloudflare.com/content/images/2023/04/image3-7.png)

At Cloudflare, we are building proxy applications on top of [Oxy](https://blog.cloudflare.com/introducing-oxy/) that must be able to handle a *huge* amount of traffic. Besides high performance requirements, the applications must also be resilient against crashes or reloads. As the framework evolves, the complexity also increases. While migrating WARP to support soft-unicast ([Cloudflare servers don't own IPs anymore](https://blog.cloudflare.com/cloudflare-servers-dont-own-ips-anymore/)), we needed to add different functionalities to our proxy framework. Those additions increased not only the code size but also resource usage and states required to be [preserved between process upgrades](https://blog.cloudflare.com/oxy-the-journey-of-graceful-restarts/).

To address those issues, we opted to split a big proxy process into smaller, specialized services. Following the Unix philosophy, each service should have a single responsibility, and it must do it well. In this blog post, we will talk about how our proxy interacts with three different services - Splicer (which pipes data between sockets), Bumblebee (which upgrades an IP flow to a TCP socket), and Fish (which handles layer 3 egress using soft-unicast IPs). Those three services help us to improve system reliability and efficiency as we migrated WARP to support soft-unicast.

![](https://blog.cloudflare.com/content/images/2023/04/image2-8.png)

### Splicer

Most transmission tunnels in our proxy forward [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) without making any modifications. In other words, given two sockets, the proxy just relays the data between them: read from one socket and write to the other. This is a common pattern within Cloudflare, and we reimplement very similar functionality in separate projects. These projects often have their own tweaks for buffering, flushing, and terminating connections, but they also have to coordinate long-running proxy tasks with their process restart or upgrade handling, too.

Turning this into a service allows other applications to send a long-running proxying task to Splicer. The applications pass the two sockets to Splicer and they will not need to worry about keeping the connection alive when restart. After finishing the task, Splicer will return the two original sockets and the original metadata attached to the request, so the original application can inspect the final state of the sockets - [for example using TCP\_INFO](https://blog.cloudflare.com/when-tcp-sockets-refuse-to-die/) - and finalize audit logging if required.

### Bumblebee

Many of Cloudflare’s on-ramps are IP-based (layer 3) but most of our services operate on [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) or [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) sockets (layer 4). To handle TCP termination, we want to create a *kernel* TCP socket from IP packets received from the client (and we can later forward this socket and an upstream socket to Splicer to proxy data between the eyeball and origin). Bumblebee performs the upgrades by spawning a thread in an anonymous network namespace with [unshare](https://man7.org/linux/man-pages/man2/unshare.2.html) syscall, NAT-ing the IP packets, and using a tun device there to perform TCP three-way handshakes to a listener. You can find a more detailed write-up on how we upgrade an IP flows to a TCP stream [here](https://blog.cloudflare.com/from-ip-packets-to-http-the-many-faces-of-our-oxy-framework/).

In short, other services just need to pass a socket carrying the IP flow, and Bumblebee will upgrade it to a TCP socket, no user-space TCP stack involved! After the socket is created, Bumblebee will return the socket to the application requesting the upgrade. Again, the proxy can restart without breaking the connection as Bumblebee pipes the IP socket while Splicer handles the TCP ones.

### Fish

Fish forwards IP packets using [soft-unicast](https://blog.cloudflare.com/cloudflare-servers-dont-own-ips-anymore/) IP space without upgrading them to layer 4 sockets. We previously implemented packet forwarding on shared IP space using iptables and conntrack. However, IP/port mapping management is not simple when you have many possible IPs to egress from and variable port assignments. Conntrack is highly configurable, but applying configuration through iptables rules requires careful coordination and debugging iptables execution can be challenging. Plus, relying on configuration when sending a packet through the network stack results in arcane failure modes when conntrack is unable to rewrite a packet to the exact IP or port range specified.

Fish attempts to overcome this problem by rewriting the packets and configuring conntrack using the netlink protocol. Put differently, a proxy application sends a socket containing IP packets from the client, together with the desired soft-unicast IP and port range, to Fish. Then, Fish will ensure to forward those packets to their destination. The client’s choice of IP address does not matter; Fish ensures that egressed IP packets have a unique five-tuple within the root network namespace and performs the necessary packet rewriting to maintain this isolation. Fish’s internal state is also survived across restarts.

### The Unix philosophy, manifest

To sum up what we are having so far: instead of adding the functionalities directly to the proxy application, we create smaller and reusable services. It becomes possible to understand the failure cases present in a smaller system and design it to exhibit reliable behavior. Then if we can remove the subsystems of a larger system, we can apply this logic to those subsystems. By focusing on making the smaller service work correctly, we improve the whole system's reliability and development agility.

Although those three services’ business logics are different, you can notice what they do in common: receive sockets, or file descriptors, from other applications to allow them to restart. Those services can be restarted without dropping the connection too. Let’s take a look at how graceful restart and file descriptor passing work in our cases.

### File descriptor passing

We use Unix Domain Sockets for interprocess communication. This is a common pattern for inter-process communication. Besides sending raw data, unix sockets also allow passing file descriptors between different processes. This is essential for our architecture as well as graceful restarts.

![](https://blog.cloudflare.com/content/images/2023/04/image4-6.png)

There are two main ways to transfer a file descriptor: using pid\_getfd syscall or [SCM\_RIGHTS](https://blog.cloudflare.com/know-your-scm_rights/). The latter is the better choice for us here as the use cases gear toward the proxy application “giving” the sockets instead of the microse...