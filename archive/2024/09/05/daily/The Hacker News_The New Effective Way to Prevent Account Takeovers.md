---
title: The New Effective Way to Prevent Account Takeovers
url: https://thehackernews.com/2024/09/the-new-effective-way-to-prevent.html
source: The Hacker News
date: 2024-09-05
fetch_date: 2025-10-06T18:30:40.740105
---

# The New Effective Way to Prevent Account Takeovers

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

# [The New Effective Way to Prevent Account Takeovers](https://thehackernews.com/2024/09/the-new-effective-way-to-prevent.html)

**Sep 04, 2024**The Hacker NewsSaaS Security / Browser Security

[![Prevent Account Takeovers](data:image/png;base64... "Prevent Account Takeovers")](https://go.layerxsecurity.com/why-account-takeover-attacks-still-succeed-and-why-the-browser-is-your-secret-weapon-in-stopping-them?utm_source=thn)

Account takeover attacks have emerged as one of the most persistent and damaging threats to cloud-based SaaS environments. Yet despite significant investments in traditional security measures, many organizations continue to struggle with preventing these attacks. A new report, "[Why Account Takeover Attacks Still Succeed, and Why the Browser is Your Secret Weapon in Stopping Them](https://go.layerxsecurity.com/why-account-takeover-attacks-still-succeed-and-why-the-browser-is-your-secret-weapon-in-stopping-them?utm_source=thn)" argues that the browser is the primary battleground where account takeover attacks unfold and, thus, where they should be neutralized. The report also provides effective guidance for mitigating the account takeover risk.

Below are some of the key points raised in the report:

## The Role of the Browser in Account Takeovers

According to the report, the SaaS kill chain takes advantage of the fundamental components that are contained within the browser. For account takeover, these include:

* **Executed Web Pages** - Attackers can create phishing login pages or use MiTM over legitimate web pages to harvest and access credentials.
* **Browser Extensions** - Malicious extensions can access and exfiltrate sensitive data.
* **Stored Credentials** - Attackers aim to hijack the browser or exfiltrate its stored credentials to access SaaS apps.

Once the user's credentials are compromised, the attacker can login to the apps and operate with impunity inside. This is a different and much shorter kill chain compared to the on-premises kill chain, which is also why traditional security measures fail to protect against it.

## Dissecting Account Takeover TTPs

The report then details the main account takeover tactics, techniques and procedures (TTPs). It analyzes how they operate, why traditional security controls are ineffective in protecting against them, and how a browser security platform can mitigate the risk.

### 1. Phishing

**The risk:** Phishing attacks abuse the way the browser executes the webpage. There are two main types of phishing attacks: a malicious login page or intercepting a legitimate one to capture session tokens.

**The protection failure:** SSE solutions and firewalls cannot protect against these attacks since the malicious web page components cannot be seen in network traffic. As a result, the phishing components are able to enter the perimeter and the user's endpoint.

**The solution:** A browser security platform provides visibility into the execution of web pages and analyzes every executed component, detecting phishing activities like credential input fields and MiTM redirection. Then, these components are disabled within the page.

### 2. Malicious Browser Extensions

**The risk:** Malicious extensions exploit the high privileges enabled by users to control the browser's activity and data, taking over stored credentials.

**The protection failure:** EDRs and EPPs often have implicit trust in browser processes, making extensions a security blind spot.

**The solution:** A browser security platform provides visibility and risk analysis of all extensions and automatically disables malicious ones.

### 3. Authentication and Access via a Login Page

**The risk:** Once the attacker obtains credentials, they can access the targeted SaaS app.

**The protection failure:** IdPs struggle to differentiate between malicious and legitimate users and MFA solutions are often not fully implemented and adopted.

**The solution:** A browser security platform monitors all stored credentials in the browser, integrates with the IdP to act as an additional authentication factor, and enforces access from the browser to prevent access through compromised credentials.

## What's Next for Security Decision Makers

The browser has become a critical attack surface for enterprises, and account takeover attacks exemplify its risk and the need to adapt the organizational security approach. LayerX has identified that a browser security solution is the key component in that shift, countering existing attack techniques that will force attackers to reevaluate their steps. [Read the full report](https://go.layerxsecurity.com/why-account-takeover-attacks-still-succeed-and-why-the-browser-is-your-secret-weapon-in-stopping-them?utm_source=thn) .

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[browser security](https://thehackernews.com/search/label/browser%20security)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Identity and Access Management](https://thehackernews.com/search/label/Identity%20and%20Access%20Management)[phishing protection](https:...