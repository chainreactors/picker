---
title: Evolution of API Security – A Practical Guide to Addressing API Threats in 2023
url: https://buaq.net/go-132789.html
source: unSafe.sh - 不安全
date: 2022-10-27
fetch_date: 2025-10-03T20:58:22.987355
---

# Evolution of API Security – A Practical Guide to Addressing API Threats in 2023

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

![](https://8aqnet.cdn.bcebos.com/ae4cb0612dee8b6d9d1e684d77769b14.jpg)

Evolution of API Security – A Practical Guide to Addressing API Threats in 2023

The kind of API security scenarios we witnessed today were never like this from the beginning
*2022-10-26 23:32:16
Author: [lab.wallarm.com(查看原文)](/jump-132789.htm)
阅读量:39
收藏*

---

The kind of API security scenarios we witnessed today were never like this from the beginning of time.  It has gone to extra lengths to become responsive and productive as it’s now.

*How was it in the beginning?*

*What changes has it faced?*

*What more can we expect in the future?*

If this is what bothers you, let’s have a look at this post as it explains the evolution of API security through the years.

## API Is Omnipresent

Before we delve deeper into API evolution, let’s understand how it’s prevailing.  A recent report revealed that nearly 1.7 billion active APIs will be there by the end of 2030. Be it web or mobile, apps are going to be fully dependent on APIs.

![APIs & Apps are Exploding](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/APIs-Apps-are-Exploding.jpeg?resize=770%2C460&ssl=1)

See how APIs are distributed across the industry. Private and customized APIs have the largest market share as they lead to need-based development.

As APIs are everywhere, related risks are not less.  With the rise of API, API threats and vulnerabilities also increased.  This is what we meant.

![API security risk is high](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/API-security-risk-is-high.jpeg?resize=770%2C368&ssl=1)

API security risk is high

## API Security – What Rests In History

Let’s begin with understanding the beginning of [API protection](https://www.wallarm.com/what/api-security-tutorial). The concern about improved API security was always there. But, it got accelerated when the official API vulnerability was announced. It all began in 1998 with the identification of CVE-1999-0270 vulnerability. It existed in the Performer API Search Tool and permitted attackers to gain access to random files.

![First API Exploit](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/the-first-API-exploit.jpeg?resize=770%2C373&ssl=1)

First API Exploit

It was the beginning and the world witnessed many more API threats including CVE-2022-29464, which is the latest addition to the list. A handful of WSO2 products permit unrestricted file upload that aids further in RCE.

![latest API exploit](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/latest-API-exploit.jpeg?resize=770%2C385&ssl=1)

latest API exploit

In an era driven [by API](https://www.wallarm.com/what/what-is-api), it’s not wise to let these loopholes create a rucksack. Presently, 5 novel exploits are coming into the picture every day.

![New API exploit report](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/New-API-exploit-report1.jpeg?resize=770%2C611&ssl=1)

New API exploit report

## What We Had Until Now

Presently, we have solutions like WAF, [API gateway](https://www.wallarm.com/what/the-concept-of-an-api-gateway) management, and API security to protect the APIs.  Are they useful? Yes. Are they perfect? No. Let’s explain what made us say this.

API Gateway management is great as it provides rate limiting; we can’t expect much as there is no access control and threat discovery. API security sounds impressive on paper but lacks hugely when it comes to protecting APIs in real time.

## What Is Wrong With Legacy WAF Solutions?

[WAF](https://www.wallarm.com/what/waf-meaning) came into being a viable solution to protect web apps and APIs and we must admit that it was doing a great job until today. With the evolution of API and its related threats, legacy WAFs are falling short with a huge margin and are not able to match the pace of your developer.

They lack API protocol support, real-time API threat detection, keep API endpoints unprotected, and lack PII discovery abilities. Let’s understand it in a better way. Also, don’t forget to check out how cutting-edge Wallarm WAF is filling its caveats.

First, we need to mention that its usage is too labor extensive as it demands constant configuration and will require API specs upload for protection. On the contrary to this, modern Wallarm has everything that requires API protection. While legacy WAF fails to process API calls, Wallarm WAF can process any kind of API. [REST or SOAP](https://www.wallarm.com/what/differences-soap-vs-rest), GraphQL, or gRPC, you name it and [Wallarm WAF](https://www.wallarm.com/product/cloud-waf) will be able to handle it.

The cherry on the cake is that it won’t bog you down with specs and configurations. It demands almost zero API specs.

Present-day API handling scenario demands a wide range of protocols. Sadly, there is hardly anything impressive offered with legacy WAF. This keeps your API development sluggish. Wallarm WAF does a great job on this front. For over 5 years, this WAF is receiving the best API protocols support and updates.

Recently, it supports [Websockets](https://www.wallarm.com/what/a-simple-explanation-of-what-a-websocket-is), [gRPC](https://www.wallarm.com/what/the-concept-of-grpc), and [GraphQL API protocols](https://www.wallarm.com/what/what-is-graphql-definition-with-example) and support for other API protocols is possible in near future. With this option, you enjoy the soundest protection against recent threats.

Have we discussed how poor auto-scaling is with legacy WAF? Yes, auto-scaling is at its worst with this option. The lack of proper threat detection techniques also caused high false positives.

These troubles are easily fixed with Wallarm WAF which scales up and down in a blink of an eye. As it comes with native Kubernetes support scaling is possible in K8 services and ecosystem.

To deal with the false positives issue, Wallarm has used the RegExp-free attack detection technique, which is known for the least possible false positive incidences.

Try installing a classic WAF as an inline solution and it’ll start working as a reverse proxy. Wallarm WAF is not like this. It comes with native inline support and is easy to be installed as an out-of-the box deployment.

This is just the tip of the iceberg. The more you know a legacy WAF, the more issues will come to the surface. In short, the traditional WAFs are not capable to handle what modern-era API security demands.

Thankfully, Wallarm WAF is there that seamlessly fixes all these loopholes of legacy WAF and shows up as a viable and workable WAF tool that modern-day API users can adopt.

![False Positive nightmare](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2022/10/False-Positive-nightmare.jpeg?resize=770%2C367&ssl=1)

False Positive nightmare

## Set Your Eyes On These For Future API Security

What we have today is already a bit flawed and will fail to address future API concerns. Be ready for the future by adopting these practices.

* **Do extensive [API discovery](https://www.wallarm.com/what/api-discovery)**

Make sure you know what APIs you have and need protection. Zombie API, Shadow API, Rogue API, or any other API should be in your knowledge. If you are aware of every single API then only can protect it.

* **Classify data and do constant risk assessment**

Discovery every single sensitive data and tag them. Use a tool like Wallarm to spot the risks such data have. Assess without fail. The early detection, the better the protection.

* **Have full security control**

Make sure you know your API portfolio, can easily detect common threats, mitigate threats early, and provide th...