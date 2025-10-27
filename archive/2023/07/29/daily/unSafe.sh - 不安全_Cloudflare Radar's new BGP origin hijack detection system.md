---
title: Cloudflare Radar's new BGP origin hijack detection system
url: https://buaq.net/go-173161.html
source: unSafe.sh - 不安全
date: 2023-07-29
fetch_date: 2025-10-04T11:51:08.519583
---

# Cloudflare Radar's new BGP origin hijack detection system

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

![](https://8aqnet.cdn.bcebos.com/c766cef4fc7f8f1a23fe9812f999a1c3.jpg)

Cloudflare Radar's new BGP origin hijack detection system

Loading...
*2023-7-28 21:0:26
Author: [blog.cloudflare.com(查看原文)](/jump-173161.htm)
阅读量:23
收藏*

---

Loading...

* [![Mingwei Zhang](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/07/mingwei-selfie-square.jpeg)](https://blog.cloudflare.com/author/mingwei/)
* [![Celso Martinho](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/08/Celso-Martinho.png)](https://blog.cloudflare.com/author/celso/)

![Cloudflare Radar's new BGP origin hijack detection system](https://blog.cloudflare.com/content/images/2023/07/Cloudflare-Radar-s-new-BGP-origin-hijack-detection-system.png)

[Border Gateway Protocol](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) (BGP) is the de facto inter-domain routing protocol used on the Internet. It enables networks and organizations to exchange reachability information for blocks of IP addresses (IP prefixes) among each other, thus allowing routers across the Internet to forward traffic to its destination. BGP was designed with the assumption that networks do not intentionally propagate falsified information, but unfortunately that’s not a valid assumption on today’s Internet.

Malicious actors on the Internet who control BGP routers can perform BGP hijacks by falsely announcing ownership of groups of IP addresses that they do not own, control, or route to. By doing so, an attacker is able to redirect traffic destined for the victim network to itself, and monitor and intercept its traffic. A BGP hijack is much like if someone were to change out all the signs on a stretch of freeway and reroute automobile traffic onto incorrect exits.

![](https://blog.cloudflare.com/content/images/2023/07/image11.png)

You can learn more about [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) and [BGP hijacking](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/) and its consequences in our learning center.

At Cloudflare, we have long been monitoring suspicious BGP anomalies internally. With our recent efforts, we are bringing BGP origin hijack detection to the [Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks) platform, sharing our detection results with the public. In this blog post, we will explain how we built our detection system and how people can use Radar and its APIs to integrate our data into their own workflows**.**

## What is BGP origin hijacking?

Services and devices on the Internet locate each other using IP addresses. Blocks of IP addresses are called an IP prefix (or just prefix for short), and multiple prefixes from the same organization are aggregated into an [autonomous system](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) (AS).

![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-26-at-18.26.17.png)

Using the BGP protocol, ASes announce which routes can be imported or exported to other ASes and routers from their routing tables. This is called the AS routing policy. Without this routing information, operating the Internet on a large scale would quickly become impractical: data packets would get lost or take too long to reach their destinations.

During a BGP origin hijack, an attacker creates fake announcements for a targeted prefix, falsely identifying an [autonomous systems (AS)](https://developers.cloudflare.com/radar/glossary/#autonomous-systems) under their control as the origin of the prefix.

In the following graph, we show an example where `AS 4` announces the prefix `P` that was previously originated by `AS 1`. The receiving parties, i.e. `AS 2` and `AS 3`, accept the hijacked routes and forward traffic toward prefix `P` to `AS 4` instead.

![](https://blog.cloudflare.com/content/images/2023/07/image2-15.png)

As you can see, the normal and hijacked traffic flows back in the opposite direction of the BGP announcements we receive.

If successful, this type of attack will result in the dissemination of the falsified prefix origin announcement throughout the Internet, causing network traffic previously intended for the victim network to be redirected to the AS controlled by the attacker. As an example of a famous BGP hijack attack, in 2018 [someone was able](https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/) to convince parts of the Internet to reroute traffic for AWS to malicious servers where they used DNS to redirect MyEtherWallet.com, a popular crypto wallet, to a hacked page.

## Prevention mechanisms and why they’re not perfect (yet)

The key difficulty in preventing BGP origin hijacks is that the BGP protocol itself does not provide a mechanism to validate the announcement content. In other words, the original BGP protocol does not provide any authentication or ownership safeguards; any route can be originated and announced by any random network, independent of its rights to announce that route.

To address this problem, operators and researchers have proposed the [Resource Public Key Infrastructure (RPKI)](https://en.wikipedia.org/wiki/Resource_Public_Key_Infrastructure) to store and validate prefix-to-origin mapping information. With RPKI, operators can prove the ownership of their network resources and create ROAs, short for Route Origin Authorisations, cryptographically signed objects that define which Autonomous System (AS) is authorized to originate a specific prefix.

Cloudflare [committed to support RPKI](https://blog.cloudflare.com/rpki/) since the early days of the [RFC](https://datatracker.ietf.org/doc/html/rfc6480). With RPKI, IP prefix owners can store and share the ownership information securely, and other operators can validate BGP announcements by checking the prefix origin to the information stored on RPKI. Any hijacking attempt to announce an IP prefix with an incorrect origin AS will result in invalid validation results, and such invalid BGP messages will be discarded. This validation process is referred to as route origin validation (ROV).

In order to further advocate for RPKI deployment and filtering of RPKI invalid announcements, Cloudflare has been providing a RPKI test service, [Is BGP Safe Yet?](https://isbgpsafeyet.com/), allowing users to test whether their ISP filters RPKI invalid announcements. We also provide rich information with regard to the RPKI status of individual prefixes and ASes at <https://rpki.cloudflare.com/>.

![](https://blog.cloudflare.com/content/images/2023/07/image8-1.png)

**However**, the effectiveness of RPKI on preventing BGP origin hijacks depends on two factors:

1. The ratio of prefix owners register their prefixes on RPKI;
2. The ratio of networks performing route origin validation.

Unfortunately, neither ratio is at a satisfactory level yet. As of today, July 27, 2023, only about 45% of the IP prefixes routable on the Internet are covered by some ROA on RPKI. The remaining prefixes are highly vulnerable to BGP origin hijacks. Even for the 45% prefix that are covered by some ROA, origin hijack attempts can still affect them due to the low ratio of networks that perform route origin validation (ROV). Based on our [recent study,](https://blog.cloudflare.com/rpki-updates-data/) only 6.5% of the Internet users are protected by ROV from BGP origin hijacks.

Despite the benefits of RPKI and RPKI ROAs, their effectiveness in preventing BGP origin hijacks is limited by the slow adoption and deployment of these technologies. Unt...