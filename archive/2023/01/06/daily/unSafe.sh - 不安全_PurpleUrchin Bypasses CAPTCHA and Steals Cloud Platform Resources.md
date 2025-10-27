---
title: PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform Resources
url: https://buaq.net/go-144336.html
source: unSafe.sh - 不安全
date: 2023-01-06
fetch_date: 2025-10-04T03:08:23.536390
---

# PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform Resources

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

![](https://8aqnet.cdn.bcebos.com/bdd0b81d6688d44237771de948a2b625.jpg)

PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform Resources

By and Nathaniel Quist January 5, 2023 at 6:00 AM Categ
*2023-1-5 22:0:40
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-144336.htm)
阅读量:37
收藏*

---

By and [Nathaniel Quist](https://unit42.paloaltonetworks.com/author/nathaniel-quist/ "Posts by Nathaniel Quist")

January 5, 2023 at 6:00 AM

Category: [Cloud](https://unit42.paloaltonetworks.com/category/cloud/)

Tags: [Automated Libra](https://unit42.paloaltonetworks.com/tag/automated-libra/), [CAPTCHA](https://unit42.paloaltonetworks.com/tag/captcha/), [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/), [containers](https://unit42.paloaltonetworks.com/tag/containers/), [cryptomining](https://unit42.paloaltonetworks.com/tag/cryptomining/), [DevOps](https://unit42.paloaltonetworks.com/tag/devops/), [Freejacking](https://unit42.paloaltonetworks.com/tag/freejacking/), [GitHub](https://unit42.paloaltonetworks.com/tag/github/), [Prisma Cloud](https://unit42.paloaltonetworks.com/tag/prisma-cloud/), [PurpleUrchin](https://unit42.paloaltonetworks.com/tag/purpleurchin/), [security feature bypass](https://unit42.paloaltonetworks.com/tag/security-feature-bypass/)

![A pictorial representation of PurpleUrchin and cryptomining. Included are the Palo Alto Networks and Unit 42 logos.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Unit42-blog-2by1-characters-r4d1-2020_Cryptocurrency-v1.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/purpleurchin-steals-cloud-resources/)

Unit 42 researchers perform a deep dive into Automated Libra, the cloud threat actor group behind the freejacking campaign PurpleUrchin. Automated Libra is a South African-based freejacking group that primarily targets cloud platforms offering limited-time trials of cloud resources in order to perform their cryptomining operations.

Freejacking is the process of using free (or limited-time) cloud resources to perform cryptomining operations.

**Key Points:**

* In order to take advantage of the limited resources offered by free trials, the actors heavily leveraged DevOps automation techniques such as continuous integration and continuous development (CI/CD). They accomplished this by containerizing user account creations on cloud platforms and through automating their cryptomining operations.
* We collected more than 250 GB of container data created for the PurpleUrchin operation and discovered that the threat actors behind this campaign were creating three to five GitHub accounts every minute during the peak of their operations in November 2022.
* We also found that some of the automated account creation cases bypassed CAPTCHA images using simple image analysis techniques. We also identified the creation of more than 130,000 user accounts created on various cloud platform services like [Heroku](https://www.heroku.com/), [Togglebox](https://www.togglebox.com/) and [GitHub](https://github.com/).
* We found evidence of unpaid balances on some of these cloud service platforms from several of the created accounts. This finding suggests that the actors created fake accounts with stolen or fake credit cards.
* With this finding, we assess that the actors behind PurpleUrchin operations stole cloud resources from several cloud service platforms through a tactic Unit 42 researchers call “Play and Run.” This tactic involves malicious actors using cloud resources and refusing to pay for those resources once the bill arrives.

Palo Alto Networks customers receive protection from the events listed within the blog through the Prisma Cloud container vulnerability scanning and runtime protection policies.

| **Related Unit 42 Topics** | [Cryptomining](https://unit42.paloaltonetworks.com/tag/cryptomining/), [containers](https://unit42.paloaltonetworks.com/tag/containers/), [DevOps](https://unit42.paloaltonetworks.com/tag/devops/), [Prisma Cloud](https://unit42.paloaltonetworks.com/tag/prisma-cloud/) |
| --- | --- |

[A New Play and Run Tactic](#post-126345-_jxyx5n27hqr0)

The PurpleUrchin cryptomining campaign, first [uncovered in October 2022](https://sysdig.com/blog/massive-cryptomining-operation-github-actions/), is characterized as a freejacking operation. While doing our own investigation of this threat actor, Unit 42 researchers found evidence that PurpleUrchin threat actors employed Play and Run tactics, using cloud resources and not paying the cloud platform vendor’s resource bill.

PurpleUrchin actors performed these Play and Run operations through the creation and use of fake accounts, with falsified or potentially stolen credit cards. These fake accounts held a pending unpaid balance. Although one of the largest unpaid balances we found was $190 USD, we suspect the unpaid balances in other fake accounts and cloud services used by the actors could have been much larger due to the scale and breadth of the mining operation.

Unit 42 researchers analyzed more than 250 GB of data that included container data as well as system access logs by the actor (with geolocation information), and hundreds of indicators of compromise (IoCs). The IoCs collected during this research are published in the [Unit 42 ATOM](https://unit42.paloaltonetworks.com/atoms/automated-libra/) for Automated Libra.

The infrastructure architecture employed by the actors uses CI/CD techniques, in which each individual software component of an operation is placed within a container. This container operates within a modular architecture within the larger mining operation.

CI/CD architectures provide highly modular operational environments, allowing some components of an operation to fail, be updated, or even be terminated and replaced, without affecting the larger environment.

By analyzing the collected container data, we traced the actor’s activity back to August 2019. Their activity was spread across several cloud providers and crypto exchanges.

We also found that the actors have a preference for using cloud services via traditional virtual service providers (VSPs). Many traditional VSPs extend their service portfolio to include cloud-related services, such as Cloud Application Platform (CAP) and Application Hosting Platform (AHP). Some of the cloud service providers that offer CAP and AHP services that were targeted by the PurpleUrchin actors include [Heroku](https://www.heroku.com/) and [Togglebox](https://www.togglebox.com/), among others.

Unit 42 researchers identified more than 40 individual crypto wallets and seven different cryptocurrencies or tokens being used within the PurpleUrchin operation. We also identified that specific containerized components of the infrastructure the actors created were not only designed to perform mining functionality, but they also automated the process of trading the collected cryptocurrencies across several crypto trading platforms such as CRATEX ExchangeMarket, crex24 and Luno.

The actor operations on GitHub used a combination of Play and Run and freejacking tactics. The likely reason the actors used GitHub is due to its decreased resistance in account creation. The actors were able to leverage a weakness within the CAPTCHA check on GitHub, which we discuss in more detail in the [following section](#post-126345-_y06fhon8fwix).

The actors automatically created GitHub accounts at an average rate of three to five accounts per minute. Once the actors had established their account base, they began their freejacking activity.

Each of the GitHub accounts was subsequently involved in a P...