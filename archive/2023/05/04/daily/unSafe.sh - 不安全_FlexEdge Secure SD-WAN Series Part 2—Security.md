---
title: FlexEdge Secure SD-WAN Series Part 2—Security
url: https://buaq.net/go-161510.html
source: unSafe.sh - 不安全
date: 2023-05-04
fetch_date: 2025-10-04T11:38:36.795184
---

# FlexEdge Secure SD-WAN Series Part 2—Security

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

![]()

FlexEdge Secure SD-WAN Series Part 2—Security

As organizations scale and enhance connectivity, robust network security becomes crucial. Force
*2023-5-3 20:34:27
Author: [www.forcepoint.com(查看原文)](/jump-161510.htm)
阅读量:22
收藏*

---

As organizations scale and enhance connectivity, robust network security becomes crucial. Forcepoint Secure SD-WAN ensures secure operations by integrating IKEv2, AES-GCM, and enterprise-grade security technologies like intrusion prevention and anti-spoofing. Its comprehensive approach safeguards cloud, remote locations, and user networks, enabling uninterrupted business growth.

**Each gateway has its own identity**

The Forcepoint SD-WAN orchestrator enhances network security by assigning a distinct identifier to each gateway, increasing protection. This identifier is shared with other gateways within the network, enabling strong security measures. If a gateway is compromised, the SD-WAN orchestrator promptly eliminates it from the configuration, preventing connections to other gateways. Additionally, the Forcepoint SD-WAN orchestrator notifies other gateways of the removal, eliminating the compromised gateway from the network to maintain a secure environment.

**Wildcards not required**

Some vendors with dynamic full mesh solutions rely on “wildcard shared secrets” or “wildcard certificates” to authenticate gateways. Especially in configuration models where unique identity of each gateway is not utilized, using wildcards becomes the only available option. However, this introduces a security vulnerability. Since the same wildcard certificate authenticates multiple gateways, if one gateway is compromised, it can imitate uncompromised gateways undetected and gain control over other gateways in the network. This highlights the importance of implementing individual gateway identities to mitigate such risks and ensure robust network security.

Forcepoint SD-WAN orchestrator prioritizes strong security authentication measures and does not rely on wildcards. When a shared secret is utilized, it is only used for authentication between a specific gateway and the orchestrator. To further enhance security, each gateway generates a unique public and private key for authentication. This key authentication is securely transmitted to the SD-WAN orchestrator via a protected channel, which then shares the information with other gateways in the network. This comprehensive approach ensures secure authentication across all components involved, preventing gateways from accessing any secrets that could enable them to mimic or control other gateways.

**Anti-spoofing and traffic filtering**

The Forcepoint SD-WAN orchestrator employs effective anti-spoofing measures by managing and communicating the authorized addresses for newly added gateways. This information is shared among all gateways in the network, preventing bypassing of traffic filtering. Each gateway within the Forcepoint SD-WAN orchestrator solution possesses robust traffic filtering and intrusion detection capabilities, ensuring selective acceptance of traffic from Forcepoint SD-WAN.

In our next post, we describe how the Forcepoint SD-WAN orchestrator delivers 24/7 service even during maintenance or link failure.

文章来源: https://www.forcepoint.com/blog/x-labs/flexedge-secure-sd-wan-series-part-2-security
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)