---
title: Are Forgotten AD Service Accounts Leaving You at Risk?
url: https://thehackernews.com/2025/06/are-forgotten-ad-service-accounts.html
source: The Hacker News
date: 2025-06-18
fetch_date: 2025-10-06T23:00:31.690114
---

# Are Forgotten AD Service Accounts Leaving You at Risk?

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

# [Are Forgotten AD Service Accounts Leaving You at Risk?](https://thehackernews.com/2025/06/are-forgotten-ad-service-accounts.html)

**Jun 17, 2025**The Hacker NewsPassword Security / Active Directory

[![Forgotten AD Service Accounts](data:image/png;base64... "Forgotten AD Service Accounts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlKliwvQajerwFgtDLluOtPONwkusQQO0-VqrfDRmr1zHgA8DiLQODtWU7KqrAW5xM2ZD578sEXryQ8ikUkN698a2hxEElLBvkskFKqBQe8iuB59qYJ4DgnCaU4WObUjf__Fe1d7DXWtAeccFLww5lXBLAtqd2rvKg91P3e-PA5-sY89Ou241Gei1QZRM/s790-rw-e365/AD.jpg)

For many organizations, Active Directory (AD) service accounts are quiet afterthoughts, persisting in the background long after their original purpose has been forgotten. To make matters worse, these orphaned service accounts (created for legacy applications, scheduled tasks, automation scripts, or test environments) are often left active with non-expiring or stale passwords.

It's no surprise that AD service accounts often evade routine security oversight. Security teams, overwhelmed by daily demands and lingering technical debt, often overlook service accounts (unlinked to individual users and rarely scrutinized) allowing them to quietly fade into the background. However, this obscurity makes them prime targets for attackers seeking stealthy ways into the network. And left unchecked, forgotten service accounts can serve as silent gateways for attack paths and lateral movement across enterprise environments. In this article, we'll examine the risks that forgotten AD service accounts pose and how you can reduce your exposure.

## Uncover and inventory the forgotten

As the old cybersecurity adage goes, you can't protect what you can't see. This holds especially true for AD service accounts. Gaining visibility is the first step to securing them, but orphaned or unmonitored service accounts often operate silently in the background, escaping notice and oversight. These forgotten service accounts are especially problematic, as they've played a central role in some of the most damaging breaches in recent years. In the case of the [2020 SolarWinds attack](https://specopssoft.com/blog/solarwinds-hack-weak-password-solarwinds123-cause/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article), compromised service accounts were instrumental in helping threat actors navigate targeted environments and access sensitive systems.

Once attackers gain a foothold through phishing or social engineering, their next move typically involves hunting for service accounts to exploit and using them to elevate privileges and move laterally through the network. Fortunately, administrators have a variety of techniques available to identify and uncover forgotten or unmonitored AD service accounts:

* Query AD for service principal name (SPN)-enabled accounts, which are typically used by services to authenticate with other systems.
* Filter for accounts with non-expiring passwords, or those that haven't logged in for an extended period.
* Scan scheduled tasks and scripts for hard-coded or embedded credentials that reference unused accounts.
* Review group membership anomalies, where service accounts may have inherited elevated privileges over time.
* Audit your Active Directory. You can run a read-only scan today with Specops' free AD auditing tool: [Specops Password Auditor](https://specopssoft.com/product/specops-password-auditor/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article)

## A real-world example: Botnet exploits forgotten accounts

In early 2024, security researchers discovered a [botnet of over 130,000 devices](https://specopssoft.com/blog/botnet-microsoft-password-spraying/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) targeting Microsoft 365 service accounts in a massive password-spraying campaign. The attackers bypassed multi-factor authentication (MFA) by abusing basic authentication, an outdated authentication scheme still enabled in many environments. Because these attacks didn't trigger typical security alerts, many organizations were unaware they were compromised. This example is just one of many that highlight the importance of securing service accounts and eliminating legacy authentication mechanisms.

## Privilege creep leads to silent escalation

Even service accounts that were initially created with minimal permissions can become dangerous over time. This scenario, known as privilege creep, occurs when accounts accumulate permissions due to system upgrades, role changes, or nested group memberships. What starts as a low-risk utility account can quietly evolve into a high-impact threat, capable of accessing critical systems without anyone realizing it.

Security teams should therefore review service account roles and permissions on a regular basis; if access isn't actively managed, even well-intentioned configurations can drift into risky territory.

## Key practices for securing AD service accounts

Effective AD service account management requires a deliberate, disciplined approach, as these logins are high-value targets that require proper handling. Here are [some best practices](https://specopssoft.com/blog/service-account-security-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral&utm_content=article) that form the backbone of a strong AD service account security strategy:

### Enforce least privilege

Grant only the permissions absolutely necessary for each account to function. Avoid placing service accounts in broad or powerful groups like Domain Admins.

### Use managed service accounts and group managed service accounts

Managed service accounts (MSAs) and group managed service accounts (gMSAs) provide automatic password rotation and cannot be used for interactive logins—this makes them safer than traditional user accounts and easier to maintain securely.

### Audit regular...