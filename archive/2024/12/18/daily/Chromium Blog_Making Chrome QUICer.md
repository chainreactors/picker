---
title: Making Chrome QUICer
url: http://blog.chromium.org/2024/12/making-chrome-quicer.html
source: Chromium Blog
date: 2024-12-18
fetch_date: 2025-10-06T19:38:08.494807
---

# Making Chrome QUICer

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Making Chrome QUICer](https://blog.chromium.org/2024/12/making-chrome-quicer.html "Making Chrome QUICer")

Tuesday, December 17, 2024

In October 2020, Chrome enabled [HTTP/3 by default](https://blog.chromium.org/2020/10/chrome-is-deploying-http3-and-ietf-quic.html). HTTP/3 ([RFC 9114](https://datatracker.ietf.org/doc/html/rfc9114)) runs over IETF QUIC ([RFC9000](https://datatracker.ietf.org/doc/html/rfc9000)). Default-enabling HTTP/3 in Chrome resulted in improved performance compared not only HTTP/1 and HTTP/2, but also Google QUIC. Benefits included reduced Google search latency and fewer rebuffers for YouTube.

The journey to optimizing performance did not end when HTTP/3 was default enabled. Recent advancements include the implementation of the HTTP/3 ORIGIN frame ([RFC 9412](https://httpwg.org/specs/rfc9412.html)) and Server's Preferred Address ([RFC 9000 Section 9.6](https://datatracker.ietf.org/doc/html/rfc9000#name-servers-preferred-address)). The former enhances connection coalescing, while the latter reduces a connection's round trip time (RTT). Both features have been enabled by default in M131, which was released to Stable on 11/19.

### ORIGIN Frame

When a connection is established for a specific hostname, the server’s certificate typically contains numerous other hostnames for which the server is authoritative. However, a client cannot immediately send requests for those other hostnames on that connection without first performing a DNS lookup for the other hostname and verifying that the IP address of the connection matches the resolved address. This additional DNS resolution introduces latency and significantly reduces the likelihood of connection pooling due to potential IP mismatches. The metrics from Chrome indicate that nearly 20% of HTTP/3 connections would be unnecessary if not for this IP mismatch.

Creating a new connection, even with QUIC 0-RTT, is expensive in terms of latency, memory, and CPU usage. This is because:

* DNS resolution adds latency unless cached locally in Chrome’s DNS cache.
* Both client and server must send multiple packets to complete a QUIC handshake.
* TLS necessitates CPU-intensive asymmetric cryptography on both ends.
* The congestion controller begins in its default state, potentially leading to under or over-sending.
* 0-RTT might fail.
* Non-safe requests aren't sent via 0-RTT.
* More connections consume more memory.

Additionally, features like HTTP priorities ([RFC 9218](https://datatracker.ietf.org/doc/rfc9218/)) are only effective if there are multiple simultaneous responses to send.

The HTTP/3 ORIGIN Frame ([RFC 9412](https://httpwg.org/specs/rfc9412.html)) enables a server to indicate what domains it would like to pool onto a connection. Additionally, once the frame is received, it indicates other domains should not be pooled onto that connection, even if they are in the certificate.

### Server’s Preferred Address

In some cases, the initial server address to which the client connects is not the most efficient route. It might be behind an L4 load balancer, and connecting directly could increase stability. Particularly when using Anycast, it’s possible the server is distant from where traffic enters the network, creating a 3-legged path that increases the round trip time.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPbECfw3krb6-1DM-wQBsBpPLhcLNGwGVMzEFW_XzUpumvfQzJSvVLJfZ1iwCyowq9QRE2bwl-GsQ8eArforqyyEBadmNN2iwUP59p3Rl428qWPqaJFu2JYe9o7QsuWa20R1s_isnM7efkNIMSetkmnyhFuQOtRt1-7G_e4NNb-BSfXP-DhVB_X5c6QZ0V/s1600/Screenshot%202024-12-17%2012.07.47%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPbECfw3krb6-1DM-wQBsBpPLhcLNGwGVMzEFW_XzUpumvfQzJSvVLJfZ1iwCyowq9QRE2bwl-GsQ8eArforqyyEBadmNN2iwUP59p3Rl428qWPqaJFu2JYe9o7QsuWa20R1s_isnM7efkNIMSetkmnyhFuQOtRt1-7G_e4NNb-BSfXP-DhVB_X5c6QZ0V/s1600/Screenshot%202024-12-17%2012.07.47%20PM.png)

Once the handshake is confirmed, Server’s Preferred Address allows a server to indicate it would like the client to migrate to a different server IP. Though a QUIC connection is not bound to a single 4-tuple like TCP, this is the only type of migration in RFC9000 where the server can change its address.

So far, only Google’s [Media CDN](https://cloud.google.com/media-cdn/docs/overview) has widely enabled advertising an alternative address, but we expect more servers to adopt it soon. Testing has shown that this migration is successful over 99% of the time in Chrome and reduces average RTT by 40-80%.

Posted by Fan Yang and Ian Swett

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

[**](https://blog.chromium.org/)

[**](https://blog.chromium.org/2025/01/announcing-supporters-of-chromium-based.html "Newer Post")

[**](https://blog.chromium.org/2024/12/doubling-speedometer-scores-android.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [$200K](https://blog.chromium.org/search/label/%24200K)

  1
* [10th birthday](https://blog.chromium.org/search/label/10th%20birthday)

  4
* [abusive ads](https://blog.chromium.org/search/label/abusive%20ads)

  1
* [abusive notifications](https://blog.chromium.org/search/label/abusive%20notifications)

  2
* [accessibility](https://blog.chromium.org/search/label/accessibility)

  3
* [ad blockers](https://blog.chromium.org/search/label/ad%20blockers)

  1
* [ad blocking](https://blog.chromium.org/search/label/ad%20blocking)

  2
* [advanced capabilities](https://blog.chromium.org/search/label/advanced%20capabilities)

  1
* [android](https://blog.chromium.org/search/label/android)

  2
* [anti abuse](https://blog.chromium.org/search/label/anti%20abuse)

  1
* [anti-deception](https://blog.chromium.org/search/label/anti-deception)

  1
* [background periodic sync](https://blog.chromium.org/search/label/background%20periodic%20sync)

  1
* [badging](https://blog.chromium.org/search/label/badging)

  1
* [benchmarks](https://blog.chromium.org/search/label/benchmarks)

  1
* [beta](https://blog.chromium.org/search/label/beta)

  83
* [better ads standards](https://blog.chromium.org/search/label/better%20ads%20standards)

  1
* [billing](https://blog.chromium.org/search/label/billing)

  1
* [birthday](https://blog.chromium.org/search/label/birthday)

  4
* [blink](https://blog.chromium.org/search/label/blink)

  2
* [browser](https://blog.chromium.org/search/label/browser)

  2
* [browser interoperability](https://blog.chromium.org/search/label/browser%20interoperability)

  1
* [bundles](https://blog.chromium.org/search/label/bundles)

  1
* [capabilities](https://blog.chromium.org/search/label/capabilities)

  6
* [capable web](https://blog.chromium.org/search/label/capable%20web)

  1
* [cds](https://blog.chromium.org/search/label/cds)

  1
* [cds18](https://blog.chromium.org/search/label/cds18)

  2
* [cds2018](https://blog.chromium.org/search/label/cds2018)

  1
* [chrome](https://blog.chromium.org/search/label/chrome)

  35
* [chrome 81](https://blog.chromium.org/search/label/chrome%2081)

  1
* [chrome 83](https://blog.chromium.org/search/label/chrome%2083)

  2
* [chrome 84](https://blog.chromium.org/search/label/chrome%2084)

  2
* [chrome ads](https://blog.chromium.org/search/label/chrome%20ads)

  1
* [chrome apps](https://blog.chromium.org/search/label/chrome%20apps)

  5
* [Chrome dev](https://blog.chromium.org/search/label/Chrome%20dev)

  1
* [chrome dev summit](https://blog.chromium.org/search/label/chrome%20dev%20summit)

  1...