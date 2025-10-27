---
title: How AitM Phishing Attacks Bypass MFA and EDR—and How to Fight Back
url: https://thehackernews.com/2024/08/how-to-stop-aitm-phishing-attack.html
source: The Hacker News
date: 2024-08-30
fetch_date: 2025-10-06T18:09:20.960656
---

# How AitM Phishing Attacks Bypass MFA and EDR—and How to Fight Back

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

# [How AitM Phishing Attacks Bypass MFA and EDR—and How to Fight Back](https://thehackernews.com/2024/08/how-to-stop-aitm-phishing-attack.html)

**Aug 29, 2024**The Hacker NewsIdentity Protection / Online Threat

[![AitM Phishing Attacks](data:image/png;base64... "AitM Phishing Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNBBgTuCUTvvb2i-7H0n4K2g_5iSW-hzyh_FG1Y7YWdtT1suSemyMWWABitQmomg9yCgYM3_Zk3yeMFzmgSb4-FBwaVAu46-R6TEe7hyrTe3_3e-FRbDaw4af482bUK7IpCOVcy0aJGhozhZs97CoruNWPwc5RGVyIj2r1tOJs4VU90dpW8G0oEYB48Mg/s790-rw-e365/main.png)

Attackers are increasingly using new phishing toolkits (open-source, commercial, and criminal) to execute adversary-in-the-middle (AitM) attacks.

AitM enables attackers to not just harvest credentials but steal live sessions, allowing them to bypass traditional phishing prevention controls such as MFA, EDR, and email content filtering.

In this article, we're going to look at what AitM phishing is, how it works, and what organizations need to be able to detect and block these attacks effectively.

## What is AitM phishing?

AitM phishing is a technique that uses dedicated tooling to act as a proxy between the target and a legitimate login portal for an application.

As it's a proxy to the real application, the page will appear exactly as the user expects, because they are logging into the legitimate site – just taking a detour via the attacker's device. For example, if accessing their webmail, the user will see all their real emails; if accessing their cloud file store then all their real files will be present, etc.

This gives AitM an increased sense of authenticity and makes the compromise less obvious to the user. However, because the attacker is sitting in the middle of this connection, they are able to observe all interactions and also take control of the authenticated session to gain control of the user account.

While this access is technically temporary (since the attacker is unable to reauthenticate if prompted) in practice authenticated sessions can often last as long as 30 days or more if kept active. Additionally, there are a wide range of persistence techniques that allow an attacker to maintain some level of access to the user account and/or targeted application indefinitely.

## How do AitM toolkits work?

Let's consider the two main techniques that are used to implement AitM phishing: Reverse web proxies (classic AitM) and Browser-in-the-Middle (BitM) techniques. There are two main variants of AitM toolkits:

### **Reverse web proxy:**

This is arguably the most scalable and reliable approach from an attacker's point of view. When a victim visits a malicious domain, HTTP requests are passed between the victim's browser and the real site via the malicious site. When the malicious site receives an HTTP request, it forwards this request to the legitimate site it is impersonating, receives the response, and then forwards that on to the victim.

Open-source tools that demonstrate this method include Modlishka, Muraena, and the ever-popular Evilginx. In the criminal world, there are also similar private toolsets available that have been used in many breaches in the past.

### **BitM:**

Rather than act as a reverse web proxy, this technique tricks a target into directly controlling the attacker's own browser remotely using desktop screen sharing and control approaches like VNC and RDP. This enables the attacker to harvest not just the username and password, but all other associated secrets and tokens that go along with the login.

In this case, the victim isn't interacting with a fake website clone or proxy. They are literally remotely controlling the attacker's browser to log in to the legitimate application without realizing. **This is the virtual equivalent of an attacker handing their laptop to their victim, asking them to login to Okta for them, and then taking their laptop back afterwards.** Thanks very much!

Practically speaking, the most common approach for implementing this technique is using the open-source project noVNC, which is a JavaScript-based VNC client that allows VNC to be used in the browser. Probably the most well-known example of an offensive tool implementing this is EvilnoVNC, which spins up Docker instances of VNC and proxies access to them, while also logging keystrokes and cookies to facilitate account compromise.

> If you want to know more about SaaS-native attack techniques, [check out this blog post.](https://pushsecurity.com/blog/saas-attack-techniques/?utm_source=hnews&utm_medium=paid&utm_content=feature)

## Phishing is nothing new – so what's changed?

Phishing is one of the oldest cyber security challenges facing organizations, with some description of identity/phishing attacks having been [the top attack vector since at least 2013](https://www.verizon.com/business/resources/T78/reports/data-breach-investigation-report_2015.pdf). But, both the capabilities of phishing tools, and their role in how today's attacks play out, have changed significantly.

As we've already mentioned, AitM toolkits are primarily a way for attackers to circumvent controls like MFA to take over workforce identities – granting access to a vast spectrum of business apps and services accessed over the internet.

The reality is that we're now in a new era of cyber security, where **identity is the new perimeter**. This means that identities are the lowest-hanging fruit for attackers to pick at when looking for a way into a would-be victim.

|  |
| --- |
| [![AitM phishing](data:image/png;base64... "AitM phishing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj08qVVXISGjVeQFU_84rrGrybrhUu-9QWxVb3odYjTGQZ4V1ajG2yHwdkq8zITpnQL-edOQ0WGWfkbKcppxTmI24QtE2DZ3Ne-qAzKeHvSgdJhpWhu3fphHrjGAR5DyuoWmToe0uQSzAu0i7Nmh0fHsNSfB8ZeyT5Wzr4BNawWHbNfIZ1w27INdPKyxQQ/s790-rw-e365/2-Identity-is-the-new-perimeter.png) |
| The digital perimeter for organizations has shifted as business IT has evolved away from centralized networks to web-based services and application...