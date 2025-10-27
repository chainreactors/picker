---
title: Burp Suite roadmap update: January 2023
url: https://buaq.net/go-146871.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:02:59.379452
---

# Burp Suite roadmap update: January 2023

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

![](https://8aqnet.cdn.bcebos.com/cdac82b74caa49f33ae106fe1fe8860b.jpg)

Burp Suite roadmap update: January 2023

Matt Atkinson |27 January 2023 at
*2023-1-27 22:48:49
Author: [portswigger.net(查看原文)](/jump-146871.htm)
阅读量:40
收藏*

---

Matt Atkinson |
27 January 2023 at 14:48 UTC

![Burp Suite roadmap 2023](https://portswigger.net/cms/images/fb/00/9f33-article-2023-road-map-article.png)

Believe it or not, it's January once again. And this can mean only one thing - it's time to update you on the changes we've got in store for [Burp Suite](https://portswigger.net/burp) over the next six months.

But this edition of the Burp roadmap also comes with a slight caveat - because this year we can neither confirm nor deny that we may also have a few surprises up our collective sleeves. [Watch this space](https://twitter.com/PortSwigger) to stay in the know.

## Burp Scanner

[Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) is used in Burp Suite Enterprise Edition, Burp Suite Professional, and now (to a slightly more limited extent) in our free CI/CD product,  [Dastardly](https://portswigger.net/burp/dastardly). It enables tens of thousands of users to scan the modern web both efficiently and effectively.

But PortSwigger isn't exactly known for resting on its laurels, and the first half of 2023 is looking good for Burp Scanner users in terms of releases. Over the next six months, you'll see Burp Scanner gain yet more automated capability - and an exciting new way to customize your scans.

Done **Support for popups in recorded login sequences** - The 2022.12.4 release added support for recorded login sequences that open new windows or tabs. This enables you to run [authenticated scans](https://portswigger.net/burp/vulnerability-scanner/authenticated-scanning) on websites with login mechanisms that require you to interact with popups, such as Microsoft and Amazon's SSO services.

Done **Revamped browser powered scanning** - The 2022.12.4 release fundamentally changed the way that [Burp Scanner navigates using its built-in browser](https://portswigger.net/blog/browser-powered-scanning-2-0). This improves scanning of applications that make heavy use of client-side JavaScript for navigation, and lays a strong foundation for further development of the scanner.

WIP **Declarative scan checks** - Work is progressing on a new framework to add scan checks to Burp Scanner using a simplified language we've created specifically for this purpose. This will enable you to create custom scan checks more easily (without writing a BApp extension).

WIP **React form handling** - Work is progressing on improving the way Burp Scanner handles forms when scanning single page applications (SPAs) built on React. Specifically, this will improve Burp Scanner's handling of input elements that do not have an enclosing form tag.

Added **Improved scanning of JavaScript frameworks** - Further to the improvements we have already made to Burp Scanner's coverage of applications built using the React library, we will continue to develop our capabilities in this area, and include apps built using Angular, Vue.js, and other frameworks.

Added **Seed scan from uploaded API definition** - We will give Burp Scanner the ability to ingest an API definition as part of its launch process. It will use this API definition to seed its scan - enhancing Burp Suite's ability to [scan APIs and microservices](https://portswigger.net/burp/vulnerability-scanner/api-security-testing).

Added **GraphQL scan checks** - We will give Burp Scanner the ability to check for a number of security vulnerabilities relating to APIs using the GraphQL language.

Added **Access control scan checks** - We give Burp Scanner the ability to check for a number of security vulnerabilities relating to [access control](https://portswigger.net/web-security/access-control).

Note that Burp Suite Enterprise Edition and Burp Suite Professional both contain Burp Scanner and will benefit from its roadmap.

## Burp Suite Enterprise Edition

As I write, [Burp Suite Enterprise Edition](https://portswigger.net/burp/enterprise) is now sitting at well over 1,000 subscribers. But as well as users, 2022 saw Enterprise Edition gain some powerful new features - like the ability to replay recorded login sequences. And with the plans outlined in this roadmap, 2023 is shaping up to be another cracker.

This year, you'll see some efficient new ways to scale scanning across your whole web portfolio. And further improvements to Burp Suite Enterprise Edition's already [class-leading scanning engine](#burp-scanner) will take its ability to scan the modern web to the next level.

Done **Export scan results in XML** - The 2022.11 release added the ability to export scan results from Burp Suite Enterprise Edition in XML format - enabling easier integration with systems such as Defect Dojo and other vulnerability management tools.

Done **Replay of recorded login sequences** - The 2022.10 release added support for recorded login replays in Burp Suite Enterprise Edition. This enables you to make sure that [Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) can log in successfully when carrying out [authenticated scans](https://portswigger.net/burp/vulnerability-scanner/authenticated-scanning).

Done **Licence key rollover** - The 2022.10 release brought rolling license key renewals to Burp Suite Enterprise Edition. If you renew your license before it expires, we now automatically update your license key information.

Done **Improved user onboarding** - The 2022.9 release brought a number of improvements to the onboarding process - including the ability to quickly set up a scan of [PortSwigger's deliberately vulnerable website](https://portswigger.net/blog/gin-and-juice-shop-put-your-scanner-to-the-test), to see an example of scan results.

WIP **Hourly metered billing** - Work is progressing on enabling Burp Suite Enterprise Edition users to pay for scans as and when they use them - further simplifying the process of scanning web portfolios at scale.

WIP **CI/CD inversion of control** - Work is progressing on enabling Burp Suite Enterprise Edition users to start a scanning machine in a container (controlled by a CI system, for example). This will make it possible to run Enterprise Edition from within any CI/CD environment - much like our recently released free CI/CD product, [Dastardly](https://portswigger.net/burp/dastardly).

Added **Improve site setup** - We will make it easier to set up sites in Burp Suite Enterprise Edition. This work will include enabling you to define the scope of a scan more easily.

Added **Pre-built Amazon Machine Images (AMIs)** - We will provide pre-built AMIs for Burp Suite Enterprise Edition, enabling you to auto-generate a suitable EC2 instance. This will make it easier to get Burp Suite Enterprise Edition running on AWS.

Added **Supply-Chain Levels for Software Artifacts (SLSA) Level 2** - Burp Suite Enterprise Edition will be certified to SLSA Level 2 - addressing customer requirements.

Note that the [Burp Scanner roadmap](#burp-scanner) described above also applies to Burp Suite Enterprise Edition.

## Burp Suite Professional

The last 12 months have been huge for [Burp Suite Professional](https://portswigger.net/burp/pro). It's now got a brand new API - opening up new ways to tailor it to your every need - as well as some slick UI changes, to enable more efficient testing.

2023 will see us further develop these themes - by bringing you loads of new UI and customization options. And that's not to mention the [Burp Scanner roadmap](#burp-scanner) - ...