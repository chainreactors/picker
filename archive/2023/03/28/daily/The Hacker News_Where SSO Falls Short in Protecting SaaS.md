---
title: Where SSO Falls Short in Protecting SaaS
url: https://thehackernews.com/2023/03/where-sso-falls-short-in-protecting-saas.html
source: The Hacker News
date: 2023-03-28
fetch_date: 2025-10-04T10:56:02.629120
---

# Where SSO Falls Short in Protecting SaaS

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

# [Where SSO Falls Short in Protecting SaaS](https://thehackernews.com/2023/03/where-sso-falls-short-in-protecting-saas.html)

**Mar 27, 2023**The Hacker NewsSaaS Security

[![SaaS](data:image/png;base64... "SaaS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEho-xJnUKKozBWEWukiv4VljG3dRUujqSanUOEc3yWj_uyELw28wYvDy6cTt2gbg7d8mLEiCdAjYyob89FPTA6g4cdT0JKSTap0NX6bpLB1Wa2kcgFDMNBhKitcU8KIcxAD6uJERMKFKumabCjDFYIVDj2kJQLbX-AEkZUDTsLuxWzzE-IGFyHzfWce/s790-rw-e365/sso.png)

Single sign-on (SSO) is an authentication method that allows users to authenticate their identity for multiple applications with just one set of credentials. From a security standpoint, SSO is the gold standard. It ensures access without forcing users to remember multiple passwords and can be further secured with MFA. Furthermore, an estimated 61% of attacks stem from stolen credentials. By removing usernames and passwords, the attack surface is reduced as well. SSO helps companies meet strict compliance regulations by not only enabling businesses to secure their accounts, but by helping them demonstrate that they've taken the necessary steps to meet regulatory requirements.

While SSO is an important step in securing SaaS apps and their data, having just SSOs in place to secure the SaaS stack in its entirety is not enough. SSO alone won't prevent a threat actor from accessing a SaaS app. It also won't protect SaaS apps that are onboarded without the IT team's knowledge or approval.

Organizations need to take additional steps to secure valuable data within their SaaS stack. Here are five use cases where SSO on its own falls short.

[Learn how Adaptive Shield can help you secure your entire SaaS stack.](https://www.adaptive-shield.com/?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_5gapswheressofallsshortinprotectingsaas)

## Companies Are NOT Enforcing SSO-Only Login

Nearly every SaaS app can integrate into an SSO, and most organizations enable it. Our research shows that an astounding 95% allow their employees to log into Salesforce with SSO. However, fewer than 5% of those companies require SSO login. Rather than use a proven, highly secure access governance tool, they allow employees to access their SaaS with a username and password.

SSO is most effective when companies eliminate access with local credentials. By allowing access with local credentials, companies with SSO can still be victimized by threat actors who steal credentials and log in through the front door.

## Admins Require Non-SSO Access

Even in organizations that require SSO, administrators need to be able to log in directly to the application. Most applications prefer that admins have direct login access with a username and password so they can respond to an SSO outage or other issues.

This is particularly problematic considering that Admin access is the most coveted access to threat actors. By capturing that information, cyber-criminals have full access to the entire app instance, enabling them to create new user accounts, download data, or encrypt data and hold it for ransom. Companies that rely solely on SSO for SaaS security can be blindsided by SaaS infiltrations into admin accounts using a username and password credentials.

## SSO Can't Help with Over-Permissioned or Malicious Third-Party Applications

Third-party apps integrate with hub applications to provide additional functionality or improve processes. The majority of these integrations are harmless, and improve employee productivity. However, as noted in the 2023 SaaS to SaaS Access report, 39% of apps that connect to Microsoft 365 request scopes that enable them to write, read, and delete files and emails.

Occasionally, some connected apps might be malicious and take advantage of the scoped permissions to steal or encrypt sensitive information from within the application.

SSOs have no visibility into third-party applications, their permission scopes, or their functionality. They have no way to alert security teams or app owners if a third-party application is putting the company at risk.

[Learn more about third-party app risk in the latest SaaS-to-SaaS Access Report](https://www.adaptive-shield.com/saas-to-saas-3rd-party-app-risk-report-2023?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_5gapswheressofallsshortinprotectingsaas.3)

## SSOs Should Work with a SaaS Security Posture Management Solution (SSPM)

SaaS Security is at its strongest when done in coordination with an SSO. An SSO solution, together with an SSPM solution, allows a holistic Identity and Access Governance, such as de-provisioning users — SSO handles access control and is an integral part of Identity and Access Management. SaaS Security Posture Management solutions, like Adaptive Shield, also go beyond access control, with additional layers of protection in areas where SSOs are vulnerable, as well as identifying misconfigurations, recognizing connected third-party applications, identifying device hygiene issues, and data loss management.

[Get a 15-minute demo how you can secure your SaaS stack](https://www.adaptive-shield.com/lp/request-a-demo?utm_source=TheHackerNews&utm_medium=sponsored_content&utm_campaign=thn_5gapswheressofallsshortinprotectingsaas.2)

![](data:image/png;base64...)

![The Hacker News]()

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
[**Share on Hacke...