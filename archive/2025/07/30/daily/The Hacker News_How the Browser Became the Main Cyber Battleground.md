---
title: How the Browser Became the Main Cyber Battleground
url: https://thehackernews.com/2025/07/how-browser-became-main-cyber.html
source: The Hacker News
date: 2025-07-30
fetch_date: 2025-10-06T23:57:42.351880
---

# How the Browser Became the Main Cyber Battleground

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

# [How the Browser Became the Main Cyber Battleground](https://thehackernews.com/2025/07/how-browser-became-main-cyber.html)

**Jul 29, 2025**The Hacker NewsEndpoint Protection / Identity Management

[![Cyber Battleground](data:image/png;base64... "Cyber Battleground")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHkNFpltbfrUNjDkYsT4_gGAdkCS6JDebJCY-naQ0meC6LcUw8qH4XseTWBuJsAx4eBDeZlJMnsLN7B82Ix-7ykAjsKy1GEt6Vylh_0XWNaY9VbNxe5kv4GY6BLINqTAJieCX4-44EmGCeRWZJKghEj_Xt__vjJ3xaygnXZQk49RythF3kdzayeEVwKp0/s790-rw-e365/main.png)

Until recently, the cyber attacker methodology behind the biggest breaches of the last decade or so has been pretty consistent:

* Compromise an endpoint via software exploit, or social engineering a user to run malware on their device;
* Find ways to move laterally inside the network and compromise privileged identities;
* Repeat as needed until you can execute your desired attack — usually stealing data from file shares, deploying ransomware, or both.

But attacks have fundamentally changed as networks have evolved. With the SaaS-ification of enterprise IT, core business systems aren't locally deployed and centrally managed in the way they used to be. Instead, they're logged into over the internet, and accessed via a web browser.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7NqDjMWmdDixOcyLCIHmeS9yCtuCaGW6wDDZtUyRVSTS1f5dTWEYoYdUHFZX50DS16FADK_Y9LkZDwU7TxFXPP7ud4CqRzpGN7UGlNQgH2xAy26_qFb_J23q1D5SBOuI4wj54ueKfjLXfTaE9kQwL4NHgm_jptxYTJ6N9VCG1Di0Dr-mQPIpJJ8FgUIM/s790-rw-e365/1.png) |
| Attacks have shifted from targeting local networks to SaaS services, accessed through employee web browsers. |

Under the shared responsibility model, the part that's left to the business consuming a SaaS service is mostly constrained to how they manage identities — the vehicle by which the app is accessed and used by the workforce. It's no surprise that this has become the soft underbelly in the crosshairs of attackers.

We've seen this time and again in the biggest breaches of recent years, with the highlights including the massive [Snowflake campaign in 2024](https://pushsecurity.com/blog/snowflake-retro/) and the [2025 crime wave attributed to Scattered Spider](https://pushsecurity.com/blog/key-takeaways-from-the-scattered-spider-attacks-on-insurance-firms/).

These attacks are so successful because while attackers have moved with the changes to enterprise IT, security hasn't really kept up.

## **The browser is the new battleground — and a security blind spot**

Taking over workforce identities is the first objective for attackers looking to target an organization, and the browser is the place where the attacks against users happen. This is because it's where these digital identities are created and used — and their credentials and sessions live. This is what the attacker wants to get their hands on.

Stolen credentials can be used as part of targeted attacks or in broader credential stuffing (cycling known username and credential pairs against various apps and platforms), while stolen session tokens can be used to log in directly to an active session, bypassing the authentication process.

There are a few different techniques that attackers can use to get access to these identities. Attackers harvest stolen credentials from various places — **data breach dumps**, **mass** **credential** **phishing campaigns,** **infostealer logs**, even **malicious browser extensions** that they've tricked an employee into installing. In fact, the cyber crime ecosystem itself has shifted on its axis to cater to this, with hackers specifically taking on the role of harvesting credentials and establishing account access for others to exploit.

The high-profile [Snowflake](https://pushsecurity.com/blog/snowflake-retro/) breaches in 2024 signalled a watershed moment in the shift to identity-driven breaches, where attackers logged into accounts across hundreds of customer tenants using stolen credentials. One of the primary sources of the stolen credentials used in the attacks were infostealer logs dating back to 2020 — breached passwords that hadn't been rotated or mitigated with MFA.

Infostealers are notable because they're an endpoint malware attack designed to harvest credentials and session tokens (primarily from the browser) to enable the attacker to then log into those services… through their own web browser. **So, even today's endpoint attacks are seeing the attacker pivot back into the browser in order to get to identities — the key to the online apps and services where exploitable data and functionality now resides.**

## **Attacks in the browser vs. on the browser**

There's an important distinction to be made between attacks that happen in the browser, vs. those happening against the browser itself.

There's growing consensus that **the browser is the new endpoint**. But the analogy isn't perfect — the reality is that web browsers have a comparatively limited attack surface compared to the complexity of the traditional endpoint — comparing something like Google Chrome with a Windows OS seems a very unbelievable concept.

Attacks that target the browser itself as a mechanism to compromise identities are few and far between. One of the more obvious vectors is using malicious browser extensions — so, scenarios in which a user has either:

* Been lured into installing an already malicious extension, or
* Is using a browser extension that is later compromised by an attacker

But the problem of malicious extensions is something you solve once, and then move on. The reality is that users should not be installing random browser extensions, and given the risk, you should:

* Lock down your environment to allow only a handful of essential extensions.
* Monitor for indicators that an extension you trust is compromised.

This doesn't apply in an environment where you give users full access to install whatever extensions they choose. **But if the browser is the new e...