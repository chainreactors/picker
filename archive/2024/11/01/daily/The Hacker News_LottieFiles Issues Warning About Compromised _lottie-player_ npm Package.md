---
title: LottieFiles Issues Warning About Compromised "lottie-player" npm Package
url: https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html
source: The Hacker News
date: 2024-11-01
fetch_date: 2025-10-06T19:27:50.912848
---

# LottieFiles Issues Warning About Compromised "lottie-player" npm Package

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

# [LottieFiles Issues Warning About Compromised "lottie-player" npm Package](https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html)

**Oct 31, 2024**Ravie LakshmananCryptocurrency / Software Development

[![npm Package](data:image/png;base64... "npm Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7kXQYBmClkNkGbPgYJ3dSjWIBESNb9SzN7XvgiXSjZELhto22q1cn9gt_ZAY4qV0Ze-5mA_2hwcxWaDbpmy4p4csGfvYqMW14n58fOqN0hlBZA4VRbavVmPFgKBoytynvP5KnLeVfgSRsjxEcOOgMijKwcMYX95DruMKmA6pVMfkIJ80tOg8oyz9MBnIF/s790-rw-e365/files.png)

LottieFiles has revealed that its npm package "lottie-player" was compromised as part of a supply chain attack, prompting it to release an updated version of the library.

"On October 30th ~6:20 PM UTC - LottieFiles were notified that our popular open source npm package for the web player @lottiefiles/lottie-player had unauthorized new versions pushed with malicious code," the company [said](https://x.com/LottieFiles/status/1851848602093777273) in a statement on X. "This does not impact our dotlottie player and/or SaaS service."

LottieFiles is an animation workflow platform that enables designers to create, edit, and share animations in a JSON-based animation file format called Lottie. It's also the developer behind an npm package named [lottie-player](https://www.npmjs.com/package/%40lottiefiles/lottie-player), which allows for embedding and playing Lottie animations on websites.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

According to the company, "a large number of users using the library via third-party CDNs without a pinned version were automatically served the compromised version as the latest release."

The [malicious versions](https://github.com/LottieFiles/lottie-player/issues/254) of the package [contained code](https://forum.lottiefiles.com/t/the-problem-of-someone-elses-popup-appearing/6470) that prompted users to connect their cryptocurrency wallets, with the likely goal of draining their funds. Users who are on versions 2.0.5, 2.0.6, and 2.0.7 are recommended to update to 2.0.8.

"Versions 2.0.5, 2.0.6, 2.0.7 were published directly to https://npmjs.com over the course of an hour using a compromised access token from a developer with the required privileges," LottieFiles noted.

Software supply chain security firm Checkmarx said the attack leveraged an [npm automation token](https://github.blog/changelog/2020-10-02-npm-automation-tokens/) to bypass two-factor authentication (2FA) controls and push the rogue versions.

"Even with 2FA configured, the threat actors somehow got the npm automation token set in the CI/CD pipeline to automate version releases to publish the malicious versions 2.0.5, 2.0.6, and 2.0.7 of the npm package," security researcher Jossef Harush [said](https://checkmarx.com/blog/with-2fa-enabled-npm-package-lottie-player-taken-over-by-attackers/).

Besides releasing a fix, the three rogue versions have been unpublished from the npm package repository. LottieFiles said it has also activated its incident response plan and engaged an external incident response team to assist with the investigation.

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Incident response](https://thehackernews.com/search/label/Incident%20response)[Open Source](https://thehackernews.com/search/label/Open%20Source)[software development](https://thehackernews.com/search/label/software%20development)[Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)[Web Development](https://thehackernews.com/search/label/Web%20Development)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500%...