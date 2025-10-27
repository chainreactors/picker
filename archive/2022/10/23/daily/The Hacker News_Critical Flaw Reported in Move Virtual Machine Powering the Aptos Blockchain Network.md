---
title: Critical Flaw Reported in Move Virtual Machine Powering the Aptos Blockchain Network
url: https://thehackernews.com/2022/10/critical-flaw-reported-in-move-virtual.html
source: The Hacker News
date: 2022-10-23
fetch_date: 2025-10-03T20:42:27.188099
---

# Critical Flaw Reported in Move Virtual Machine Powering the Aptos Blockchain Network

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Critical Flaw Reported in Move Virtual Machine Powering the Aptos Blockchain Network](https://thehackernews.com/2022/10/critical-flaw-reported-in-move-virtual.html)

**Oct 22, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglc_p8CP_eyxz3DqgEQ0RCLJ--v5NbVapIc1gock5FmJpeJifUF4mNGQtbECB5AkB_eAuUL64Ow_OF78jn10e41eCt4QxUn7IUUS4sRwQcU532z1UsAeiCjn9YsvmxKPvrB838nn-fubLVrhOJHCwVBPlko_bX-7r_k6-d9jZWRd_elFVQHIL0bilK/s790-rw-e365/aptos-blockchain-network.jpg)

Researchers have disclosed details about a now-patched critical flaw in the Move virtual machine that powers the Aptos blockchain network.

The vulnerability "can cause Aptos nodes to crash and cause denial of service," Singapore-based Numen Cyber Labs [said](https://medium.com/numen-cyber-labs/analysis-of-the-first-critical-0-day-vulnerability-of-aptos-move-vm-8c1fd6c2b98e) in a technical write-up published earlier this month.

Aptos is a [new entrant](https://aptoslabs.medium.com/aptos-autumn-is-here-92a8d904eb49) to the blockchain space, which [launched](https://www.coindesk.com/business/2022/10/19/aptos-token-opens-for-trading-after-blockchains-rocky-debut/) its [mainnet](https://academy.binance.com/en/glossary/mainnet) on October 17, 2022. It has its roots in the Diem stablecoin payment system proposed by Meta (née Facebook), which also introduced a short-lived digital wallet called [Novi](https://about.fb.com/news/2020/05/welcome-to-novi/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The network is built using a platform-agnostic programming language known as [Move](https://github.com/move-language/move), a Rust-based system that's [designed](https://developers.diem.com/docs/technical-papers/move-paper/) to implement and execute [smart contracts](https://thehackernews.com/2022/01/sailfish-system-to-find-state.html) in a secure [runtime environment](https://ethereum.org/en/developers/docs/evm/), also known as the Move Virtual Machine (aka [MoveVM](https://aptos.dev/guides/move-guides/move-on-aptos/)).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioKCdN1lOU1kZfDhz92uyQL1NGVLnIWESslBHCSseE5iJcuDN2PZeK0M6RQSAIPHwuFdZHv84eIj08tm2_ldQJHaPoKJ-0sPmy4vkK2MxAr7S7O8xmtAv4TxXOIuC2cZuRvC4It5FPkx1SZbqnvTjLbaXuFKcTzeOZ0oAUzFKyd0fhVTwRjsVeOXaG/s790-rw-e365/malware.jpg)

The [vulnerability](https://github.com/move-language/move/commit/566ace5a9ec01e0e685f4bfba79072fe635a6cb2) identified by Numen Cyber Labs is rooted in the Move language's verification module ("[stack\_usage\_verifier.rs](https://github.com/move-language/move/blob/main/language/move-bytecode-verifier/src/stack_usage_verifier.rs)"), a component that validates the [bytecode instructions](https://en.wikipedia.org/wiki/Bytecode) prior to its execution in MoveVM.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, it relates to an [integer overflow vulnerability](https://cwe.mitre.org/data/definitions/190.html) in the [stack-based](https://en.wikipedia.org/wiki/Stack-oriented_programming) Web3 programming language that could result in undefined behavior and therefore crashes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCZ_FUUnu4gJBU-zghMMdhuf_TTFWEGvMdoyeRT6jQCXCBCri32xKuj2FHbmj4ndvY2ixToSvJ9h0DvVG5Z6O7TxWS3pT9wNxgTet_1DZYkaDD4UXX5pGIjtcF3nfd9CxILJVo0BgTd1MhvpJqzQJO9srUNG7kQeKVjvdsfwSoa-wiXKVWaIvcSxdB/s790-rw-e365/patch.jpg)

"Since this vulnerability occurs in the Move execution module, for nodes on the chain, if the bytecode code is executed, it will cause a [Denial-of-Service] attack," the cybersecurity firm explained.

"In severe cases, the Aptos network can be completely stopped, which will cause incalculable damage, and have a serious impact on the stability of the node."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Aptos](https://thehackernews.com/search/label/Aptos)[Blockchain](https://thehackernews.com/search/label/Blockchain)[Numen Cyber Labs](https://thehackernews.com/search/label/Numen%20Cyber%20Labs)[Virtual Machine](https://thehackernews.com/search/label/Virtual%20Machine)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc...