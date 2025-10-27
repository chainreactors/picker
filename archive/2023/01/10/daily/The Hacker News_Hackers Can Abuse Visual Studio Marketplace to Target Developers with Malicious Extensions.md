---
title: Hackers Can Abuse Visual Studio Marketplace to Target Developers with Malicious Extensions
url: https://thehackernews.com/2023/01/hackers-distributing-malicious-visual.html
source: The Hacker News
date: 2023-01-10
fetch_date: 2025-10-04T03:28:30.276632
---

# Hackers Can Abuse Visual Studio Marketplace to Target Developers with Malicious Extensions

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

# [Hackers Can Abuse Visual Studio Marketplace to Target Developers with Malicious Extensions](https://thehackernews.com/2023/01/hackers-distributing-malicious-visual.html)

**Jan 09, 2023**Ravie LakshmananSupply Chain / CodeSec

[![Malicious Visual Studio Extensions](data:image/png;base64... "Malicious Visual Studio Extensions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQYImd3jK7QwDHl0yksrSJhjJxODxFjqIOInHUdbSHQQ23AoxW5lCMCkTqScOJpoB6EcdJ2BI7lkaF2_3_HSAqlMowFUNNFuvOUeI9WThP2DiWjArnPYPE2r3f2WiFo9bS_rSgH327u5x_HcZ_bIloRlxVGc0HzdqqtKpL4338VBHqfQ9DZzKkARzT/s790-rw-e365/Visual-studio-malware-code.png)

A new attack vector targeting the Visual Studio Code extensions marketplace could be leveraged to upload rogue extensions masquerading as their legitimate counterparts with the goal of mounting supply chain attacks.

The technique "could act as an entry point for an attack on many organizations," Aqua security researcher Ilay Goldman [said](https://blog.aquasec.com/can-you-trust-your-vscode-extensions) in a report published last week.

VS Code extensions, curated via a [marketplace](https://marketplace.visualstudio.com/vscode) made available by Microsoft, allow developers to add programming languages, debuggers, and tools to the VS Code source-code editor to augment their workflows.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"All extensions run with the privileges of the user that has opened the VS Code without any sandbox," Goldman said, explaining the potential risks of using VS Code extensions. "This means that the extension can install any program on your computer including ransomwares, wipers, and more."

To that end, Aqua found that not only is it possible for a threat actor to impersonate a popular extension with small variations to the URL, the marketplace also allows the adversary to use the same name and extension publisher details, including the project repository information.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1oU5CENFffRtNTLzO7MgP2d1C0a0fgU64bOW-S1Sz-gY5AkW_DoN-vzHTL2XPNU45jKNniW0Beb457nCXLVcoP1_QqYdq4xjo7jNVrtj5haROBvuglgGQ-oE46o8yei8MPsg9ACYzwEzwVCw9D28OWvaccLbQnmRBGMb34255aF2jV1jKRPHxe6Lt/s790-rw-e365/code.png)

While the method doesn't allow the number of installs and the number of stars to be replicated, the fact that there are no restrictions on the other identifying characteristics means it could be used to deceive developers.

The research also discovered that the verification badge assigned to authors could be trivially bypassed as the check mark only proves that the extension publisher is the actual owner of a domain.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK2qN5UHktvOziLWlv8OGCLupe4OLKzCyBqpK_ij0tYgUsAUvDu7CBcOAID-ZXVx9LXLqS5p_qm7Vo1FpTVrmR3bCzmHJxI5mHnXVuc875LPXEtwC16y_OOYnQLfpLMTmz1hCK5amReX-SmOY8PpI1frsak6lLxTHZqSCKf2G8cbgpltSiiy7tYWYB/s790-rw-e365/map.png)

In other words, a malicious actor could buy any domain, register it to get a verified check mark, and ultimately upload a trojanized extension with the same name as that of a legitimate one to the marketplace.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A proof-of-concept (PoC) extension masquerading as the [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) code formatting utility racked up over 1,000 installations within 48 hours by developers across the world, Aqua said. It has since been [taken down](https://marketplace.visualstudio.com/items?itemName=espenp.pretier-vscode).

This is not the first time concerns have been raised about software supply chain threats in the VS Code extensions marketplace.

In May 2021, enterprise security firm Snyk [uncovered](https://thehackernews.com/2021/05/newly-discovered-bugs-in-vscode.html) a number of security flaws in popular VS Code extensions with millions of downloads that could have been abused by threat actors to compromise developer environments.

"Attackers are constantly working to expand their arsenal of techniques allowing them to run malicious code inside the network of organizations," Goldman said.

## Update

A Microsoft spokesperson has shared the following statement with The Hacker News, noting that it [provides tools](https://code.visualstudio.com/blogs/2021/07/06/workspace-trust) for users to flag malicious extensions identified in the Marketplace. It also confirmed that the PoC add-on has been removed.

*This technique involves the use of social engineering tactics to convince a victim to download a malicious extension. To help keep customers safe and protected, we scan extensions for viruses and malware before they are uploaded to the Marketplace and we check that an extension has a Marketplace certificate and verifiable signature prior to being installed. To help make informed decisions, we recommend consumers review information, such as domain verification, ratings and feedback to prevent unwanted downloads.*

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malw...