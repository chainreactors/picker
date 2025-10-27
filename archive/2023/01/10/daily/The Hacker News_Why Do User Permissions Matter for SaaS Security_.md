---
title: Why Do User Permissions Matter for SaaS Security?
url: https://thehackernews.com/2023/01/why-do-user-permissions-matter-for-saas.html
source: The Hacker News
date: 2023-01-10
fetch_date: 2025-10-04T03:28:24.087357
---

# Why Do User Permissions Matter for SaaS Security?

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

# [Why Do User Permissions Matter for SaaS Security?](https://thehackernews.com/2023/01/why-do-user-permissions-matter-for-saas.html)

**Jan 09, 2023**The Hacker NewsSaaS Security / SSPM Solution

[![SaaS Security](data:image/png;base64... "SaaS Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqpz_v6Yfp5vepVN-k8ZFoVsrmJRs3ck6734B9aQYgS9HTtFpsxBabbXckaZK2LeVrTU2KjVRqYBR7skxZW-LZZ8JJp5UYNwnT6iRmxQ_g5Tgusxm4lOHhiM4VPkb8XjcL_xWTBw2gi02r0GR8tSLHo1BB7YQNca0hKFEbXPY5jwGqxXJ87VNF6OP2/s790-rw-e365/SAAS.png)

Earlier this year, threat actors infiltrated [Mailchimp](https://mailchimp.com/march-2022-security-incident/?ref=newsroom), the popular SaaS email marketing platform. They viewed over 300 Mailchimp customer accounts and exported audience data from 102 of them. The breach was preceded by a successful phishing attempt and led to malicious attacks against Mailchimp's customers' end users.

Three months later, Mailchimp was hit with [another attack](https://mailchimp.com/august-2022-security-incident/?ref=newsroom). Once again, an employee's account was breached following a successful phishing attempt.

While the identity of the Mailchimp accounts that had been compromised wasn't released, it's easy to see how user permission settings could have played a role in the attack. Once threat detectors breached the system, they had the access needed to utilize an internal tool that enabled them to find the data they were looking for. The attack ended when security teams were able to terminate user access, although data which had already been downloaded remained in the threat actor's hands.

Introducing user permissions, through role-based account control (RBAC), could have severely limited the damage caused by the breach. Had the rule of least privilege been applied, it's likely that the breached account would not have afforded access to the internal tools that were used in the attack. Furthermore, reduced access might have completely prevented the attack or limited the number of affected accounts to far fewer than the 100 which were ultimately compromised.

***Protect SaaS data as if your company's future depends on it.*** [***Schedule a demo for more.***](https://www.adaptive-shield.com/lp/request-a-demo?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_whydouserpermissionsmatterforsecurity1)

## What Are User Permissions?

SaaS user permissions allow app owners to limit a user's resources and actions based on the user's role. Called RBAC, it is the permission set that grants read or write access, assigns privileges to high-level users, and determines access levels to company data.

## What is the Purpose of the "Rule of Least Privilege"?

The rule of least privilege is an important security concept that provides the least amount of access needed for users to perform their job functions. In practice, it reduces the attack surface by limiting high-level access to a few privileged individuals. If a low-privilege user account is breached, the threat actor would have less access to sensitive data contained within the application.

***Are your SaaS apps following the rule of least privilege?*** [***Schedule a demo to learn more.***](https://www.adaptive-shield.com/lp/request-a-demo?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_whydouserpermissionsmatterforsecurity2)

## Why Do User Permissions Matter for Security?

App administrators frequently grant full access to team members, particularly when dealing with a small user group. As business users rather than security professionals, they don't always recognize the degree of risk in granting those access permissions. Furthermore, they prefer to give full authorization rather than be asked for specific permissions later on.

Unfortunately, this approach can put sensitive data records at risk. User permissions help define the exposed data in the event of a breach. By protecting data behind a permission set, threat actors that access a user identity are limited to the data available to their victim.

Loose user permissions also make it easier for threat actors to carry out automated attacks. Having multiple users with wide API permissions makes it easier for cybercriminals to breach a SaaS app and either automate ransomware or steal data.

## Why Are User Access Reviews Important?

User access reviews are essentially audits that look at users and their access. They show security team members and app owners the degree of access each user has and allows them to adjust permission levels as needed.

This is important, as it helps identify users who may have switched roles or teams within the company but retained an unnecessary level of permissions, or alerts security teams regarding employees whose actions have deviated from normal behaviors to include suspicious behavior. Furthermore, it helps identify former employees who still have access and high-privilege permissions.

Access Reviews should take place at predetermined intervals, ensuring that unnecessary permissions are identified within a set time frame.

## Conclusion

User permissions are often a misunderstood security feature. It protects organizations from both external attacks and internal data-sharing errors.

An SSPM solution, like Adaptive Shield, enables effective user permission management, giving security personnel and app owners the confidence to know the extent of any user permission and see that user's SaaS security hygiene. This real-time view of users is far more effective than User Access Audits, which only present a snapshot view of the users' permissions at a specific moment in time.

***Looking for more visibility into your Saas users?*** [***Schedule a demo today for full visibility.***](https://www.adaptive-shield.com/lp/request-a-demo?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_whydouserpermissionsmatterforsecurity3)

![](data:image/png;base64...)

![The Hacker News]()

Found this article interesting? This article is a contributed ...