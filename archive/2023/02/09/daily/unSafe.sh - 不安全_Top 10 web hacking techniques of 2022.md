---
title: Top 10 web hacking techniques of 2022
url: https://buaq.net/go-148549.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:12.334983
---

# Top 10 web hacking techniques of 2022

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

![](https://8aqnet.cdn.bcebos.com/54d9e6d2bb81413af9c61f22bf59b8a5.jpg)

Top 10 web hacking techniques of 2022

Published: 08 February 2023 at 14:20 UTC
*2023-2-8 22:20:30
Author: [portswigger.net(查看原文)](/jump-148549.htm)
阅读量:71
收藏*

---

![James Kettle](https://portswigger.net/content/images/profiles/callout_james_kettle_112px.png)

* **Published:** 08 February 2023 at 14:20 UTC
* **Updated:** 08 February 2023 at 16:09 UTC

![](https://portswigger.net/cms/images/b6/fe/1e2d-article-hacking-tech-2022-results_article.png)

Welcome to the Top 10 Web Hacking Techniques of 2022, the [16th edition](https://portswigger.net/research/top-10-web-hacking-techniques) of our annual community-powered effort to identify the most important and innovative web security research published in the last year.

Since publishing our [call for nominations](https://portswigger.net/research/top-10-web-hacking-techniques-of-2022-nominations-open) in January, you've submitted a record 46 nominations, and cast votes to single out 15 final-round candidates. Over the last two weeks, an expert panel of researchers [Nicolas Grégoire](https://twitter.com/Agarri_FR), [Soroush Dalili](https://twitter.com/irsdl), [Filedescriptor](https://twitter.com/filedescriptor), and  [myself](https://twitter.com/albinowax) have analysed, conferred and voted on the 15 finalists, to bring you the final top 10 new web hacking techniques of 2022. As usual, we haven't excluded our own research, but panellists can't vote for anything they're affiliated with.

This year, for the third year running, there's been a noticeable improvement in the number of quality nominations. While outright novel techniques and class-breaks have gotten rarer, there's more people pushing at the boundaries and sharing their findings than ever. It's great to see the research ecosystem flourishing, even if it makes it harder to select a top ten!

Before we begin the countdown, I should note that any attempt to compress a year of research into a top ten list is going to leave valuable techniques overlooked. If you're hungry for knowledge, I highly recommend reading the [entire nomination list](https://portswigger.net/research/top-10-web-hacking-techniques-of-2022-nominations-open).

From the final ten, two key themes stand out - single-sign on, and request smuggling. Let's take a closer look!

#### 10 - Exploiting Web3's Hidden Attack Surface: Universal XSS on Netlify's Next.js Library

As we find ways to shovel ever more complexity into our software, even websites that look static can hide serious vulnerabilities. In [Exploiting Web3's Hidden Attack Surface](https://samcurry.net/universal-xss-on-netlifys-next-js-library/), [Sam Curry](https://twitter.com/samwcyo) tears apart numerous cryptocurrency sites with a blend of XSS, SSRF and cache poisoning originating from Netlify's Next.js library. We're eager to see if the methodology and cryptocurrency ecosystem insights fuel further discoveries in this field.

#### 9 - Practical client-side path-traversal attacks

Sometimes a vulnerability class can be quite visible, but remain overlooked for years due to low apparent severity.

In [Practical client-side path-traversal attacks](https://mr-medi.github.io/research/2022/11/04/practical-client-side-path-traversal-attacks.html), [Medi](https://twitter.com/medi_0ne) explores a website behaviour that's very common - placing user input inside a request path - and demonstrates a clear pathway to real impact. This behaviour has surfaced in exploit chains a few times over the years but this post shows it's time to recognise it as a vulnerability in its own right. This cousin of client-side parameter pollution has [already inspired a follow-up](https://erasec.be/blog/client-side-path-manipulation/) that uses it for CSRF, and we're sure more will come.

#### 8 - Psychic Signatures in Java

The catchily-named [Psychic Signatures in Java](https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/) by [Neil Madden](https://infosec.exchange/%40neilmadden) shows a critical and really very simple attack using the number 0 to forge ECDSA signatures, undermining the cryptographic foundation of numerous core web technologies including JWT and SAML.

This use of an ancient crypto attack to topple modern web tech is a great reminder that you don't always need a complex attack to achieve massive impact - and as nice as abstractions are, sometimes it's worth looking further down the stack.

#### 7 - Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes

Back in 2019, one of the nominations for the top 10 was an article [theorising about the exploitation potential of HTTP hop-by-hop headers](https://portswigger.net/research/top-10-web-hacking-techniques-of-2019-nominations-open#:~:text=Abusing%20HTTP%20hop%2Dby%2Dhop%20request%20headers), and calling for further research on the topic. Three years later, [Worldwide Server-side Cache Poisoning on All Akamai Edge Nodes](https://medium.com/%40jacopotediosi/worldwide-server-side-cache-poisoning-on-all-akamai-edge-nodes-50k-bounty-earned-f97d80f3922b) makes use of this concept for massive impact and a whole lot of bug bounties, establishing the technique as essential knowledge for web hackers and server implementers alike.

We also appreciate how [Jacopo Tediosi](https://twitter.com/jacopotediosi) throws some rare light into the world of pain people using advanced techniques can encounter when trying to get their bug bounty reports triaged.

#### 6 - Making HTTP header injection critical via response queue poisoning

Ever wondered why people sometimes inject a HTTP response header, but then refer to it as 'Response Splitting' even though they never actually split the response? In [Making HTTP header injection critical via response queue poisoning](https://portswigger.net/research/making-http-header-injection-critical-via-response-queue-poisoning), I explore the long-forgotten response-splitting technique with a high-impact, high-payout case study.

As noted by filedescriptor, "It seems like there's an infinite amount of anomalies among proxies that bring you an infinite amount of Request Smuggling techniques"... more on that later.

#### 5 - Bypassing .NET Serialization Binders

In 2020, the .NET SerializationBinder documentation changed the statement "SerializationBinder can also be used for security" to "SerializationBinder can not be used for security".

From this simple teaser, [Bypassing .NET Serialization Binders](https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html) by [Markus Wulftange](https://twitter.com/mwulftange) delves into why, ultimately building exploits for DevExpress and Microsoft Exchange as case-studies. This research cites an exceptional amount of documentation and related research, making it a great gateway into .NET serialization innards.

Quality research like this often inspires action, and it turns out Soroush has already built on it and integrated the results into [YSoSerial.Net](https://github.com/pwntester/ysoserial.net). You'll be left wondering what security-critical documentation has changed since you last read it.

#### 4 - Hacking the Cloud with SAML

Just like OAuth, you can't discuss SSO without discussing SAML. While some SAML vulnerabilities are all too well-known, [Hacking the Cloud with SAML](https://www.youtube.com/watch?v=WHn-6xHL7mI) by [Felix Wilhelm](https://twitter.com/_fel1x) shines in showing how terrifyingly expansive SAML's attack-surface is. This culminates with an XML document that uses an integer truncation bug to trigger arbitrary bytecode execution when Java attempts t...