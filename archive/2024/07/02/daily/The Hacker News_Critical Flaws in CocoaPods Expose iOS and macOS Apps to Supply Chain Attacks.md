---
title: Critical Flaws in CocoaPods Expose iOS and macOS Apps to Supply Chain Attacks
url: https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html
source: The Hacker News
date: 2024-07-02
fetch_date: 2025-10-06T17:46:56.890938
---

# Critical Flaws in CocoaPods Expose iOS and macOS Apps to Supply Chain Attacks

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

# [Critical Flaws in CocoaPods Expose iOS and macOS Apps to Supply Chain Attacks](https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html)

**Jul 01, 2024**Ravie LakshmananSupply Chain / Software Security

[![Supply Chain Attacks](data:image/png;base64... "Supply Chain Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy4XMLqZptCkn7ifIbKGNRWsYao93PQLI_x3x8VZigNo90bYOFGmw4jFFboOxaUu6Qvb2pXPGk_s6FEaz17DOyhSYIQ2ptN60p6yN5WJHX6I5PoAWaZaCHjJTOnsk3QoGzNOp16Nd8dw9C3RRfC4Pis3Ia0Z9jY5TdQ8anlENDdRuRzNGvjfnKayb-rEMJ/s790-rw-e365/Supply-Chain-Attack.gif)

A trio of security flaws has been uncovered in the [CocoaPods](https://cocoapods.org/) dependency manager for Swift and Objective-C Cocoa projects that could be exploited to stage software supply chain attacks, putting downstream customers at severe risks.

The vulnerabilities allow "any malicious actor to claim ownership over thousands of unclaimed pods and insert malicious code into many of the most popular iOS and macOS applications," E.V.A Information Security researchers Reef Spektor and Eran Vaknin [said](https://www.evasec.io/blog/eva-discovered-supply-chain-vulnerabities-in-cocoapods) in a report published today.

The Israeli application security firm said the three issues have since been [patched](https://blog.cocoapods.org/CocoaPods-Trunk-RCEs-2023/) by CocoaPods as of October 2023. The project maintainers also reset all user sessions at the time in response to the disclosures.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

One of the vulnerabilities is [CVE-2024-38368](https://github.com/CocoaPods/CocoaPods/security/advisories/GHSA-j483-qm5c-7hqx) (CVSS score: 9.3), which makes it possible for an attacker to abuse the "[Claim Your Pods](https://blog.cocoapods.org/Claim-Your-Pods/)" process and take control of a package, effectively allowing them to tamper with the source code and introduce malicious changes. However, this required that all prior maintainers have been removed from the project.

The roots of the problem go back to 2014, when a migration to the [Trunk server](https://blog.cocoapods.org/CocoaPods-Trunk/) left thousands of packages with unknown (or [unclaimed](https://cocoapods.org/owners/7)) owners, permitting an attacker to use a public API for claiming pods and an email address that was available in the CocoaPods source code ("unclaimed-pods@cocoapods.org") to take over control.

The second bug is even more critical ([CVE-2024-38366](https://github.com/CocoaPods/CocoaPods/security/advisories/GHSA-x2x4-g675-qg7c), CVSS score: 10.0) and takes advantage of an insecure email verification workflow to run arbitrary code on the Trunk server, which could then be used to manipulate or replace the packages.

Also identified in the service is a second problem in the email address verification component ([CVE-2024-38367](https://github.com/CocoaPods/CocoaPods/security/advisories/GHSA-52gf-m7v9-m333), CVSS score: 8.2) that could entice a recipient into clicking on a seemingly-benign verification link, when, in reality, it reroutes the request to an attacker-controlled domain in order to gain access to a developer's session tokens.

Making matters worse, this can be upgraded into a zero-click account takeover attack by spoofing an HTTP header – i.e., modifying the [X-Forwarded-Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) header field – and taking advantage of misconfigured email security tools.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"We have found that almost every pod owner is registered with their organizational email on the Trunk server, which makes them vulnerable to our zero-click takeover vulnerability," the researchers said.

This is not the first time CocoaPods has come under the scanner. In March 2023, Checkmarx [revealed](https://zero.checkmarx.com/this-is-how-i-hijacked-cocoapods-subdomain-using-github-pages-4e368e849022) that an abandoned sub-domain associated with the dependency manager ("cdn2.cocoapods[.]org") could have been hijacked by an adversary via GitHub Pages with an aim to host their payloads.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security)[Code Injection](https://thehackernews.com/search/label/Code%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Dependency Management](https://thehackernews.com/search/label/Dependency%20Management)[Developer Tools](https://thehackernews.com/search/label/Developer%20Tools)[iOS](https://thehackernews.com/search/label/iOS)[MacOS](https://thehackernews.com/search/label/MacOS)[mobile security](https://thehackernews.com/search/label/mobile%20security)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Inciden...