---
title: 6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026
url: https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:35.361764
---

# 6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

![cybersecurity](data:image/svg+xml;base64...)

# [6 Reasons Why Device Code Phishing is the Fastest-Growing Threat of 2026](https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html)

**The Hacker News**Jul 31, 2026Phishing / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiamJN4Z-p-XmpB_1nwgfCMj2JvWAmGP4avhjI3pBYb11kgANQy4wQf2DQ4VGJEXom4eZCFoqVozP4aJPPtpGufYrEe5E9xkebmctud6KO7NZEfNCiT14ln7CmZA1bB3m6HYNdiUnShVsIpr03SYa7jlZWnbml9R1HbqECSbnUH0DTqyETz1fpiNIqhExw/s1700-e365/push-main.jpg)

Device code phishing - the abuse of the OAuth 2.0 device authorization grant to steal access tokens - has evolved from a niche red-team technique to an industrial-scale threat in under six months.

Designed for input-constrained devices like smart TVs, printers, and so on, the device authorization login flow has been adopted by a wide range of apps and use-cases that it wasn't originally intended for - most commonly CLI logins.

Researchers first described the attack vector in 2020, but it took until 2024 before nation-state actors like Storm-2372 started using it in the wild. By 2025, ShinyHunters was using device code phishing against Salesforce tenants at scale, then in February 2026, the EvilTokens kit arrived and criminal adoption skyrocketed. By April, [Microsoft was reporting 10 to 15 entirely new campaigns every 24 hours](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/). Barracuda counted [7 million attacks in four weeks](https://blog.barracuda.com/2026/04/23/threat-spotlight-device-code-phishing). The FBI issued a [standalone advisory on Kali365](https://www.ic3.gov/PSA/2026/PSA260521), the first US federal agency PSA about a specific phishing-as-a-service kit.

Push Security added device code phishing to its [Browser & Identity Attacks Matrix](https://pushsecurity.com/resources/browser-identity-attacks-matrix/?utm_campaign=48884538-FY27Q3_sponsored-posts&utm_source=the-hacker-news&utm_content=article) back in 2023 and now tracks more than 25 distinct device code phishing kits in the wild and counting. Entering the second half of 2026, there's no sign of the pace slowing.

Push recently ran a [deep-dive webinar on device code phishing](https://pushsecurity.com/resources/device-code-phishing?utm_campaign=48884538-FY27Q3_sponsored-posts&utm_source=the-hacker-news&utm_content=article) covering the attack mechanics, a live demonstration of a custom-built phishing kit, and what comes next. Here are six takeaways that security teams should have on their radar.

## **1. It defeats every form of MFA, including passkeys**

Device code phishing doesn't attack the login flow. It attacks what happens after login - the authorization layer. In most cases, the victim is already signed into their Microsoft account when they encounter the phishing page. They copy a short code, enter it on the legitimate Microsoft device login page, pick their account from a dropdown, and click allow. That's the entire attack.

Passkeys, hardware security keys, enforced phishing-resistant MFA - none of it makes a difference, because the device code flow is separate from the authentication mechanism. The attack exploits the fact that proving your identity and granting access to an application are two different things, and most security controls only protect the first.

## **2. The PhaaS ecosystem has fully industrialized it**

Device code phishing is no longer a specialist technique. It's a standard feature in the phishing-as-a-service catalog. Tycoon2FA, which Push previously tracked as the most common AiTM phishing kit in the wild, [added device code phishing to its framework](https://pushsecurity.com/blog/device-code-phishing/?utm_campaign=48884538-FY27Q3_sponsored-posts&utm_source=the-hacker-news&utm_content=article) in May. Kali365 offers both AiTM and device code phishing in a single platform.

Some security firms are reporting that the structural similarities between kits are evidence of the ecosystem forking and fragmenting. But based on what we've seen, kits built independently using similar LLM instructions can look just as alike (more on this below).

Regardless, the capabilities these kits offer keep getting better: for example, [ARToken](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/) ships with PRT persistence, mailbox access, BEC automation, and SharePoint exfiltration packaged as product features for paying operators.

The commercialization pattern mirrors what happened with AiTM phishing: a technique moves from a research curiosity to nation-state espionage to a criminal commodity, each stage accelerating faster than the last. But device code phishing completed that entire journey in a matter of months - a compression that reflects both the maturity of the existing PhaaS market and the speed at which AI-assisted development lets new capabilities get built and distributed.

## **3. Attackers are vibe-coding new kits faster than defenders can catalog them**

Push now tracks more than 25 distinct device code phishing kits in the wild - a number that would have been inconceivable before this year. For context, a brand-new AiTM phishing kit appearing in the wild used to be a significant event that happened once every few months. Having 25+ kit families emerge this year alone reflects a fundamental change in how phishing tools get built.

AI-assisted development has collapsed the barrier to entry. Many of the kits Push tracks share structural similarities like similar layout patterns and similar code architecture, because they were generated by LLMs responding to similar prompts. Push VP R&D [Luke Jennings](https://www.linkedin.com/in/luke-jennings-042b5619b/) spun up his own kit to demonstrate just how easy it is.

## **4. It's not just a Microsoft problem**

99% of the device code phishing Push detects today targets Microsoft, but the webinar demonstrates why that won't last. The OAuth 2.0 device authorization grant is a cross-platform standard, and any application that implements it is a potential target.

Nation-state actors have already used device code phishing against Salesforce in targeted campaigns. The ShinyHunters Salesforce campaign, which compromised [over 1...