---
title: Lost in transit: debugging dropped packets from negative header lengths
url: https://buaq.net/go-170417.html
source: unSafe.sh - 不安全
date: 2023-06-27
fetch_date: 2025-10-04T11:44:47.416287
---

# Lost in transit: debugging dropped packets from negative header lengths

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

![](https://8aqnet.cdn.bcebos.com/66ffa5b37988b6255b90dffb4b1a6f67.jpg)

Lost in transit: debugging dropped packets from negative header lengths

Loading...
*2023-6-26 21:0:56
Author: [blog.cloudflare.com(查看原文)](/jump-170417.htm)
阅读量:17
收藏*

---

Loading...

* [![Terin Stock](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/08/terin-stock.png)](https://blog.cloudflare.com/author/terin-stock/)

![Lost in transit: debugging dropped packets from negative header lengths](https://blog.cloudflare.com/content/images/2023/06/image3-29.png)

Previously, I wrote about building [network load balancers with the maglev scheduler](https://blog.cloudflare.com/high-availability-load-balancers-with-maglev/), which we use for ingress into our Kubernetes clusters. At the time of that post we were using Foo-over-UDP encapsulation with virtual interfaces, one for each Internet Protocol version for each worker node.

To reduce operational toil managing the traffic director nodes, we've recently switched to using IP Virtual Server's (IPVS) native support for encapsulation. Much to our surprise, instead of a smooth change, we instead observed significant drops in bandwidth and failing API requests. In this post I'll discuss the impact observed, the multi-week search for the root cause, and the ultimate fix.

### Recap and the change

To support our requirements we've been creating virtual interfaces on our traffic directors configured to encapsulate traffic with Foo-Over-UDP (FOU). In this encapsulation new UDP and IP headers are added to the original packet. When the worker node receives this packet, the kernel removes the outer headers and injects the inner packet back into the network stack. Each virtual interface would be assigned a private IP, which would be configured to send traffic to these private IPs in "direct" mode.

![](https://blog.cloudflare.com/content/images/2023/06/image4-24.png)

This configuration presents several problems for our operations teams.

For example, each Kubernetes worker node needs a separate virtual interface on the traffic director, and each of the interfaces requires their own private IP. The pairs of virtual interfaces and private IPs were only used by this system, but still needed to be tracked in our configuration management system. To ensure the interfaces were created and configured properly on each director we had to run complex health checks, which added to the lag between provisioning a new worker node and the director being ready to send it traffic. Finally, the header for FOU also lacks a way to signal the "next protocol" of the inner packet, requiring a separate virtual interface for IPv4 and IPv6. Each of these problems individually contributed a small amount of toil, but taken together, gave us impetus to find a better alternative.

In the time since we had originally implemented this system, IPVS has added native support for encapsulation. This would allow us to eliminate provisioning virtual interfaces (and their corresponding private IPs), and be able to use newly provisioned workers without delay.

![](https://blog.cloudflare.com/content/images/2023/06/image1-40.png)

IPVS doesn't support Foo-over-UDP as an encapsulation type. As part of this project we switched to a similar option, [Generic UDP Encapsulation](https://datatracker.ietf.org/doc/html/draft-ietf-intarea-gue-09) (GUE). This encapsulation option does include the "next protocol", allowing one listener on the worker nodes to support both IPv4 and IPv6.

### What went wrong?

When we make changes to our Kubernetes clusters, we go through several layers of testing. This change had been deployed to the traffic directors in front of our staging environments, where it had been running for several weeks. However, due to the nature of this bug, the type of traffic to our staging environment did not trigger the underlying bug.

We began a slow rollout of this change to one production cluster, and after a few hours we began observing issues reaching services behind Kubernetes Load Balancers. The behavior observed was very interesting: the vast majority of requests had no issues, but a small percentage of requests corresponding to large HTTP request payloads or gRPC had significant latency. However, large responses had no corresponding latency increase. There was no corresponding increase in latency seen to any requests to our ingress controllers, though we could observe a small drop in overall requests per second.

![](https://blog.cloudflare.com/content/images/2023/06/image6-9.png)

Through debugging after the incident, we discovered that the traffic directors were dropping packets that exceeded the Internet maximum transmission unit (MTU) of 1500 bytes, despite the packets being smaller than the actual MTU configured in our internal networks. Once dropped, the original host would fragment and resend packets until they were small enough to pass through the traffic directors. Dropping one packet is inconvenient, but unlikely to be noticed. However, when making a request with large payloads it is very likely that all packets would be dropped and need to be individually fragmented and resent.

When every packet is dropped and has to be  resent, the network latency can add up to several seconds, exceeding the request timeouts configured by applications. This would cause the request to fail. necessitating retries by applications. As more traffic directors were reconfigured, these retries were less likely to succeed, leading to slower processing and causing the backlog of queued work to increase.

As you can see this small, but consistent, number of dropped packets could cause a domino effect into much larger problems. Once it became clear there was a problem, we reverted traffic directors to their previous configuration, and this quickly restored traffic to previous levels. From this we knew something about the change caused this problem.

### Finding the culprit

With the symptoms of the issues identified, we started to try to understand the root cause. Once the root cause was understood, we could come up with a satisfactory solution.

Knowing the packets were larger than the Internet MTU, our first thought was that this was a misconfiguration of the machine in our configuration management tool. However, we found the interface MTUs were all set as expected, and there were no overriding MTUs in the routing table. We also found that sending packets from the director that exceeded the Internet MTU worked fine with no drops.

Cilium has developed a debugging tool [pwru](https://github.com/cilium/pwru), short for "packet, where are you?", that uses eBPF to aid in debugging the kernel networking state. We used pwru in our staging environment and found the location where the packet had been dropped.

```
sudo pwru --output-skb --output-tuple --per-cpu-buffer 2097152 --output-file pwru.log
```

This captures tracing data for all packets that reach the traffic director, and saves the trace data to "pwru.log". There are filters built into `pwru` to select matching packets, but unfortunately they could not be used as the packet was being modified by the encapsulation. Instead, we used grep afterwards to find a matching packet, and then filtered farther based on the pointer in the first column.

```
0xffff947712f34400      9        [<empty>]               packet_rcv netns=4026531840 mark=0x0 ifindex=4 proto=8 mtu=1600 len=1512 172.70.2.6:49756->198.51.100.150:8000(tcp)
0xffff947712f34400      9        [<empty>]                 skb_push netns=4026531840 mark=0x0 ifindex=4 proto=8 m...