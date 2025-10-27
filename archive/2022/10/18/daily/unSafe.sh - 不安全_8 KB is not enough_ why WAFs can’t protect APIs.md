---
title: 8 KB is not enough: why WAFs can’t protect APIs
url: https://buaq.net/go-131336.html
source: unSafe.sh - 不安全
date: 2022-10-18
fetch_date: 2025-10-03T20:04:24.379742
---

# 8 KB is not enough: why WAFs can’t protect APIs

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

![](https://8aqnet.cdn.bcebos.com/528f18b57bf0af19c583136f9c03cfbe.jpg)

8 KB is not enough: why WAFs can’t protect APIs

WAFs were a top-notch security instrument a decade ago, but now they are not. They fail to pr
*2022-10-17 22:28:41
Author: [lab.wallarm.com(查看原文)](/jump-131336.htm)
阅读量:52
收藏*

---

WAFs were a top-notch security instrument a decade ago, but now they are not. They fail to protect APIs. Meanwhile, the number of API-specific vulnerabilities grew more than twofold in 2022. According to a [report](https://www.wallarm.com/resources/q2-2022-api-vulnerability-exploit-full-report) by Wallarm, many such vulnerabilities have critical severity, and 33% are immediately exploited. But companies still heavily rely on WAFs, so many services turn out to be highly insecure and prone to data breaches. Consider this: an average data breach cost [hit](https://www.ibm.com/security/data-breach) 4.35 million dollars in 2022, and it’s ever-growing!

To save money and reputation, use a more reliable API security tool rather than a default cloud WAF. If you are not convinced yet, here we describe three limitations that make your default WAF ineffective, which are not usually discussed.

## Web & API Security

The use of APIs is [skyrocketing](https://www.gartner.com/en/newsroom/press-releases/2021-10-18-gartner-identifies-the-top-strategic-technology-trends-for-2022), and the number of exposed flaws in business logic is growing proportionally. The reason lies in the difference between microservices and monolithic architecture, which previously dominated the field.

When a monolithic app receives a request from a user, the response is computed within the internal infrastructure and without interacting on the network. Only one endpoint per request is exposed. It’s the opposite for microservices: they interact online all the time via internal APIs to compute the response. Of course, they can be deployed on a dedicated server and won’t need to communicate on the network, but it’s costly and doesn’t make sense since microservices are specially designed for the cloud.

APIs provide access to many functions previously hidden inside a monolith, which implies many newly exposed flaws attackers can use. But it’s not only the attack surface that matters for securing your APIs! Let’s dig into it.

## Limitations of WAFs in API Security

There are a few pros and many cons to using a default cloud WAF in API security. It’s well known that WAFs cannot effectively deal with functional attacks. Yet, many crucial limitations are rarely discussed. Let’s explore them one by one.

### Nested Encodings

Your WAF is there to match incoming requests to the patterns of bad. [WAFs](https://www.wallarm.com/what/waf-meaning) need to know what fraudulent requests look like. To teach them, you provide regular expressions for strings like “eval(” or “base64\_” to be grepped in requests. When the payload is encoded, you add encoded analogs of fraudulent strings to your rule set. However, things get tricky if your payload is encoded multiple times. You need to add a set of matching strings for each encoding level. In turn, it leads to increased request processing time or time out. The latter is a disaster: users don’t like when they don’t get what they are looking for.

### Data Protocols Parsing

Often, online traffic is built in a Russian-doll manner: protocols go on top of other protocols. There are many of them above HTTP. For example, in gRPC, data is encapsulated and exchanged via HTTP2.

To reconstruct and check the payload, the WAF needs to know how these protocols are structured. Some WAFs support protocol parsing, but often it is limited to REST APIs and JSON data. Meanwhile, other popular API protocols like [gRPC](https://www.wallarm.com/what/the-concept-of-grpc), [GraphQL](https://www.wallarm.com/what/what-is-graphql-definition-with-example), [WebSocket](https://www.wallarm.com/what/a-simple-explanation-of-what-a-websocket-is), and [SOAP](https://www.wallarm.com/what/differences-soap-vs-rest#what_is_soap__) are disregarded.

Among the most popular cloud WAFs, Cloudflare supports more protocols than others. The WebSocket protocol is an oldie but goodie, but WAFs, except Cloudflare, don’t support it! It doesn’t come as a surprise because security is one of the company’s biggest focuses. Yet, Cloudflare cannot parse GraphQL, which is rapidly gaining popularity. Strange.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **AWS WAF** | **Cloudflare** | **Google Armor** | **Azure WAF** |
| **GraphQL** | -/[+](https://catalog.us-east-1.prod.workshops.aws/workshops/67662c95-2007-4281-ae51-5313cd7caa67/en-US/lab2/4-secure-with-waf) only for httpflood and tokens restrictions | – | – | – |
| **REST API** | [+](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) | + | + | + |
| **SOAP** | – | + | – | – |
| **JSON-RPC** | + | + | + | + |
| **gRPC** | – | [+](https://support.cloudflare.com/hc/en-us/articles/360050483011-Understanding-Cloudflare-gRPC-support)/- no inspection for malicious payloads | – | – |
| **WebSocket** | [–](https://repost.aws/questions/QUcbocc8jnSHS7v1AQFCOqJQ?threadID=324733) | [+](https://support.cloudflare.com/hc/en-us/articles/200169466-Using-Cloudflare-with-WebSockets)/- no inspection for malicious payloads | – | – |

**Cloud WAFs’ protocol support table**

AWS WAF is the only one to protect GraphQL APIs, and it has done so [since 2020](https://aws.amazon.com/about-aws/whats-new/2020/10/aws-appsync-adds-support-for-aws-waf/). Amazon adopts a forward-looking strategy but leaves behind old solutions, like the SOAP protocol, which is still used in many legacy solutions migrating to the cloud.

Only one protocol can be parsed by all these default WAFs – the REST API. But there’s an important caveat you need to know.

## Checked Request Size Limitation

The size of the scanned payload in a WAF is always limited to the request’s first bytes. This fact still is widely overlooked and leads to weak security measures: an attacker can bypass all WAF checks at once by putting the malicious code further in the request body.

Can WAFs offer us a solution in case of oversized payloads? There are two ways a WAF can react: block the request immediately or pass it further without checking the bytes after the limit. Each WAF adopts a different strategy by default, so you need to check the settings before using your WAF to ensure it behaves as expected.

But blocking isn’t an intelligent solution: at least some of your APIs may receive legitimate yet big requests. To solve this, you can allow bigger requests for specific URIs. Still, the setup procedure is not obvious because of the rules hierarchy, and the initial concern becomes valid again: anything exceeding the limit may lead to an attack.

There’s no point in expecting AWS, Google, or other cloud providers to drop the checked payload limit. If it’s not in place, intentionally oversized requests can overload servers. Also, legitimate big requests would time out because of the time-consuming checks.

|  |  |
| --- | --- |
|  | **Maximum inspected request body size** |
| AWS WAF | 8 KB |
| Cloudflare | 128 KB |
| Google Armor | 8 KB |
| Azure WAF | [128 KB](https://learn.microsoft.com/en-us/answers/questions/300050/waf-request-size-128-kb.html) |

**The request body size limitation table**

The limitation was not as crucial in the early days of the internet. Previously, requests mainly featured form submissions and were relatively small. Even if a user attached a file, it was uploaded in chunks due to bandwidth and throughput limita...