---
title: Not All Sandboxes Are for Children: How to Secure Your SaaS Sandbox
url: https://thehackernews.com/2022/10/not-all-sandboxes-are-for-children-how.html
source: The Hacker News
date: 2022-10-21
fetch_date: 2025-10-03T20:33:15.708578
---

# Not All Sandboxes Are for Children: How to Secure Your SaaS Sandbox

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

# [Not All Sandboxes Are for Children: How to Secure Your SaaS Sandbox](https://thehackernews.com/2022/10/not-all-sandboxes-are-for-children-how.html)

**Oct 20, 2022**The Hacker News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKwTAQRX-lSHb8mUXTtmveNwDZ4kH1YWeqKj6g3esXyruWtKog0Htu8tr1pUMY6zgnNVVZPOf0jwz6Ev7s4V8P0aDjbANDT4zkooXpEAdcVAAILEZsDbEykOt3rLTRSJoziBwS3210sztMGhCFsP5QK8Ps708PI0G_72-7nQzj5KTFgEwKXAlIJqGT/s790-rw-e365/as.jpg)

When creating a Sandbox, the mindset tends to be that the Sandbox is considered a place to play around, test things, and there will be no effect on the production or operational system. Therefore, people don't actively think they need to worry about its security. This mindset is not only wrong, but extremely dangerous.

When it comes to software developers, their version of sandbox is similar to a child's playground — a place to build and test without breaking any flows in production. Meanwhile, in the world of cybersecurity, the term 'sandbox' is used to describe a virtual environment or machine used to run suspicious code and other elements.

Many organizations use a Sandbox for their SaaS apps — to test changes without disrupting the production SaaS app or even to connect new apps (much like a software developer's Sandbox). This common practice often leads to a false sense of security and in turn a lack of thought for its security implications. This article will walk you through what is a SaaS sandbox, why it is vulnerable, and how to secure it.

[*Learn how you can gain visibility and control over your SaaS sandbox and app stack.*](https://www.adaptive-shield.com?utm_source=TheHackerNews&utm_medium=content_syndication&utm_campaign=THN_secure_sandbox1)

## Cybersecurity & SaaS Sandbox Fundamentals

A *cybersecurity* sandbox allows separation of the protected assets from the unknown code, while still allowing the programmer and app owner to see what happens once the code is executed. The same security concepts are used when creating a *SaaS* Sandbox — it duplicates the main instance of SaaS including its data. This allows playing around with the SaaS app, without influencing or damaging the operational SaaS — in production.

Developers can use the sandbox to test the API, install add-ons, connect other applications, and more — without worrying about it affecting the actual users of the organization. Admins can change configurations, test SaaS features, change roles, and more. This allows the user to better understand how the changes to the SaaS will go before implementing it on an operational, and critical, SaaS instance. This also allows time to create guidelines, train staff, build workflows, and more.

All in all, using a Sandbox is a great concept for all software and SaaS usage; but like all great things in the world of SaaS, the problem is that there is a major security risk lurking within.

## Sandbox Security Real-World Risks & Realities

A large private hospital inadvertently [revealed data of 50,000 patients](https://www.haaretz.com/israel-news/tech-news/2021-08-29/ty-article/.premium/data-of-50-000-israelis-leaked-from-israels-largest-private-hospital/0000017f-f964-d318-afff-fb67d4130000) when they built a demo site (i.e a Sandbox) to test a new appointment-setting system. They used the real database of the medical center, leaving patients' data exposed.

Often a Sandbox is created using real data, occasionally even a complete clone of the production environment, with its customizations. Other times, the Sandbox is directly connected to a production database. If an attacker manages to penetrate the Sandbox because of lax security, they will gain access to troves of information. (This leakage of information can be problematic especially if you are an EU company or processing EU data because of GDPR. If you are processing medical information in the USA or for a USA company, you can be in violation of HIPPA.)

[*Learn how an SSPM can help you automate the security for your SaaS sandbox.*](https://www.adaptive-shield.com?utm_source=TheHackerNews&utm_medium=content_syndication&utm_campaign=THN_secure_sandbox2)

Even organizations that use synthetic data, which is recommended for all companies, can still be at risk for an attack. An attacker can use the Sandbox for reconnaissance to gain insight on how an organization sets up its security features and its possible weak spots. Since the Sandbox reflects to some degree how the operational system is configured, an attacker can use this knowledge to penetrate the production system.

## How to Secure Your SaaS Sandbox

The solution for the problem of the non-secure Sandbox is rather simple – secure the Sandbox step-by-step as if it was a production system.

**Step 1.** Manage and control access to a Sandbox and limit users' access to the Sandbox. For example, not every user that has access to production should also have access to the Sandbox. Controlling which users can create and access a Sandbox is the first step for keeping your SaaS environment secure.

**Step 2.** Implement the same security settings that are configured within the operational system to the Sandbox version; from requiring MFA to implementing SSO and IDP. Many SaaS apps have additional security features that are tailor-made for that specific SaaS app and should be mirrored in the Sandbox. For example, Salesforce has unique security features such as: Content Sniffing Protection, Default Data Sensitivity Levels, Authentication Through Custom Domain, and so on.

**Step 3.** Remove production data and replace it with synthetic (i.e., made up) data. Sandboxes are typically used for testing changes in configurations, processes, flows (such as APEX), and more. They don't require real data for testing changes - any data with the same format can be sufficient. Therefore, avoid copying the production data and use Data Mask instead.

**Step 4.** Keep your Sandbox inline with security improvements done in the production environment. Often a ...