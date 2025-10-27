---
title: Introducing Proactive API Leak Management
url: https://buaq.net/go-146247.html
source: unSafe.sh - 不安全
date: 2023-01-20
fetch_date: 2025-10-04T04:21:17.849707
---

# Introducing Proactive API Leak Management

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

![](https://8aqnet.cdn.bcebos.com/488f1d0b2d3cecae2e926e9e6b8d2d1a.jpg)

Introducing Proactive API Leak Management

Read the press release announcing the early release of Wallarm API Leak ManagementThe rec
*2023-1-19 22:2:14
Author: [lab.wallarm.com(查看原文)](/jump-146247.htm)
阅读量:32
收藏*

---

*Read the [press release](https://lab.wallarm.com/?p=11844) announcing the early release of Wallarm API Leak Management*

The recent surge in hacks involving leaked API Keys and other API secrets such as credentials, passwords, certificates, tokens and encryption keys has put everyone involved on notice – organizations need a way to discover, remediate and provide on-going protection against hacks in the event of a leak.

The Wallarm API Leak Management solution, now in early release, provides a comprehensive answer to this problem by automatically discovering leaked API keys and secrets, implementing controls to block their use, and monitoring any follow-on attacks. This allows organizations to prevent unauthorized access to sensitive data and to protect their internal operations and end customers from unauthorized use of that data.

If you’re concerned about this issue and want immediate help, we are offering a complimentary API Leaks Assessment. [**Register to get yours today**](https://www.wallarm.com/api-leak-management-early-release)!

### API Leak Issues Are Getting Worse

In recent months the industry has been abuzz with news about attacks involving leaked API keys and other API secrets. For instance:

* **CircleCI** posted an [advisory](https://circleci.com/blog/january-4-2023-security-alert/) in early January regarding a presumed breach of their systems, potentially putting 1000s of organizations at risk.
* **Slack** [notified](https://slack.com/intl/en-gb/blog/news/slack-security-update) the development community on New Year’s Eve that some Slack employee tokens were stolen and misused to gain access to their GitHub repository.
* **LastPass** finally [admitted](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/) on Dec 22nd that an earlier breach back in August, in which credentials and keys were obtained, allowed an adversary nearly unfettered access to a cloud-based backup system, putting end users’ password vaults at risk.
* **Travis CI** continues to have issues, with the latest coming from researchers who [reported last summer](https://arstechnica.com/information-technology/2022/06/credentials-for-thousands-of-open-source-projects-free-for-the-taking-again/) that they had found over 73,000 tokens, secrets, and various credentials.

While API Key leakage incidents are not new, they seem to be accelerating now. Why?

* Engineering teams are on ever-tightening schedules, which means shipping faster with less QA coverage.
* Tech stacks are getting more complicated – securing both legacy and modern APIs, supporting more authentication/authorization methods, enabling more tooling diversity used by different teams, and covering more environments – which leads to mistakes and accidental leakage.
* Software supply chains are getting longer and more complicated, which means these leaks can occur anywhere – by your in-house teams, by your partners, by the open-source code being used, or even by your customers.

### Why Is This A Challenge?

Leakage of API keys and other secrets can happen for many reasons – due to developers’ mistakes, missing repository access controls, insecure use of public services, and data disclosure accidents by contractors, partners and users – which makes it extremely difficult to manage and protect against. It’s important because such leaks can pose a significant security threat to companies, as they can expose sensitive information, lead to account or system takeover, or worse.

Even if a leak is detected, it can be difficult to locate where the key is defined and revoke it in a timely manner. And it can be challenging to determine if the token was (mis)used before or after revocation, and to track any actions taken with the leaked information. These issues can be time-consuming and resource-intensive to address, making prevention an important consideration.

### Proactive Approach by Wallarm

Today, Wallarm is introducing our new proactive API Leak Management capability, part of our [End-to-End API Security](https://www.wallarm.com/product/api-security-overview) bundle. Now in early release, the API Leak Management capability will provide alerts when a leak is detected, and enable you to quickly and easily block the leaked key through the interface.

You also have access to a registry of all detected leaks, allowing you to keep track of and manage potential security risks. This will not only save you time and effort, but also provides you with the peace of mind of knowing that you have a security control in place against leaks of API keys and other secrets.

There are three main scenarios:

* **Detect**. Wallarm automatically scans 20+ public sources for API secrets leaks: public repositories, mobile apps, Pastebin, and many other ways.
* **Remediate**. Once a leak is detected, Wallarm automatically revokes and blocks requests with compromised tokens, and tracks them across your entire API portfolio.
* **Control.** Wallarm also continuously tracks and blocks any subsequent use of these leaked API keys and other secrets.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/01/APIL-230105-dashboard_01.png?resize=770%2C394&ssl=1)

### Unique Solution

The Wallarm API Leak Management solution is integrated with other Wallarm capabilities – including [API Discovery](https://www.wallarm.com/product/api-discovery), [API Threat Prevention](https://www.wallarm.com/product/api-threat-prevention), and [Cloud-Native WAAP](https://www.wallarm.com/product/wallarm-waap). Customers get full-spectrum visibility, detection, and protection for their entire web application and API portfolio, regardless of protocol or environment, via our [API Security Platform](https://www.wallarm.com/product/api-security-platform) to reduce tool sprawl and cost while improving risk management and supporting innovation.

As the CISO of a large US enterprise said after getting a sneak peek, “I have to give Wallarm all the credit and praise for finding our API leaks, an issue we’ve been working relentlessly on for some time now. And the ability to deliver all this capability on a single platform is certainly unique in our estimation.”

### Availability

Existing customers who are interested in taking advantage of early access to the Wallarm API Leak Management can reach out directly to our customer supportteam or their account executive.

### Complimentary API Leaks Assessment

Get a thorough understanding of your risk exposure due to leaked API keys and other secrets by registering for our free API Leaks Assessment. We will scour out 20+ sources for any leaked API keys and other secrets – all with no impact on your APIs themselves. We expect to get a full report on your risk exposure due to leaked API keys and other secrets within 72 hours, pending confirmation of your domain ownership.

[**Register your interest now**](https://www.wallarm.com/api-leak-management-early-release)!

文章来源: https://lab.wallarm.com/introducing-proactive-api-leak-management/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)