---
title: A Secure User Authentication Method – Planning is More Important than Ever
url: https://thehackernews.com/2023/01/a-secure-user-authentication-method.html
source: The Hacker News
date: 2023-01-17
fetch_date: 2025-10-04T04:05:29.900415
---

# A Secure User Authentication Method – Planning is More Important than Ever

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

# [A Secure User Authentication Method – Planning is More Important than Ever](https://thehackernews.com/2023/01/a-secure-user-authentication-method.html)

**Jan 16, 2023**The Hacker NewsIdentity Management / MFA

[![Identity Management](data:image/png;base64... "Identity Management")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnm-tdcKpbuusG4xn1UJKu8KCHJ5Isqb_fBD32dIYJh6OMpO0W9fvFIRiJt9gc2jYq_IdgxTXBpvncIxJgCy382ANwHriQ34Tb1EgkNqQEnfKU0HSxJjbsy9VTVSBtGm2Kf7Ra7MNOTt1gknUQKFGu9DFuuv4IsUw1fhPGTMbRBF9Y6na5dhbzFkqo/s790-rw-e365/Specops-uReset.png)

When considering authentication providers, many organizations consider the ease of configuration, ubiquity of usage, and technical stability. Organizations cannot always be judged on those metrics alone. There is an increasing need to evaluate company ownership, policies and the stability, or instability, that it brings.

## How Leadership Change Affects Stability

In recent months, a salient example is that of Twitter. The Twitter platform has been around since 2006 and is used by millions worldwide. With many users and a seemingly robust authentication system, organizations used Twitter as a primary or secondary authentication service.

Inconsistent leadership and policies mean the stability of a platform is subject to change, which is especially true with Twitter as of late. The ownership change to Elon Musk precipitated widespread changes to staffing and policies. Due to those changes, [a large portion of staff was let go](https://www.cnn.com/2022/11/03/tech/twitter-layoffs/index.html), but this included many individuals responsible for the technical stability of the platform.

This culminated in an outage of [Twitter's SMS two-factor authentication](https://www.wired.com/story/twitter-two-factor-sms-problems/). With delayed or non-existent texts, many users could not log in to Twitter. This affected systems that relied on Twitter as their primary and secondary authentication provider.

Not limited to authentication issues, with the changes come a renewed concern over the safety and privacy of user data. Twitter has been under an FTC consent decree from past problems surrounding user data, and a [good portion of the staff](https://slate.com/technology/2022/11/twitter-security-trust-safety-ftc.html) responsible for compliance has been let go. Even if the authentication provider stays up, it may leave an organization in an uncomfortable position regarding the state of their stored on Twitter's servers.

## Strategies for Authentication Service Stability

Using a platform's well-established and robust authentication service can save organizations time and money over implementing their own. Cutting out third-party platforms is typically not feasible or even recommended. Instead, proactive planning is essential if an organization needs to maintain stability and security with its authentication platforms.

It's crucial to ask and answer the following questions when considering how your organization's authentication service would handle potential disruptions in authentication providers.

* Does the organization's authentication service support multiple identity providers?
* If a provider is unavailable, is there a backup provider, and how quickly can providers be switched?
* What is the disruption to users? Will they be logged out of current sessions, or will it be seamless and take effect on the next login?
* If MFA is configured, what are the available options? Are there multiple methods to verify the user, and if one is removed, does that degrade authentication services?

If an organization chose Twitter as a source of two-factor authentication, it might find that recent events indicate a necessary change. If so, the switch could be made easier if multiple MFA platforms were already available and configured.

If an organization can choose the active authentication system based on current needs, then even the problems shown with a major platform such as Twitter would be mitigated, and the organization's users would see little change.

### Offering Multiple MFA Options

To understand how this works in practice, one can look to Microsoft. With Azure, once MFA is configured, you can offer several options or limit the available verification methods. Instead of an SMS, you could receive a phone call or use a hardware token. If you offer all 3, you won't be locked out of your account if a specific service is unavailable.

Nearly identical is Google Workspace, where you can offer one or more authentication options. If you enable more than one, you will not lose the ability to authenticate your users in the event of a service failure. Both Microsoft and Google could be more flexible. Neither offers the full range of options to integrate with services like Twitter.

An example of a system that offers a myriad of options is Okta. By enabling Social Logins, you can allow users to log in via popular services such as Facebook or Twitter. But it's recommended that you back that social login with an MFA configuration that could include such options as SMS, authenticator applications, or a hardware device such as a Yubikey.

## Mitigating Authentication Instability with Specops uReset

An organization may find itself uncomfortable with changes to its authentication provider. If so, implementing a product, such as [Specops uReset](https://specopssoft.com/product/specops-ureset/?utm_source=thehackernews.com&utm_medium=referral&utm_campaign=na_2023_thehackernews&utm_content=guest-post), takes the reliance on a problematic authentication platform off the table, at least for password resets.

The flexibility to choose from multiple weighted authentication providers makes a problematic provider easy to remove while leaving the ability for users and service desk workers to reset a password. Change the weighting to offset the loss of the previously used provider, and your users can quickly get back to work!

Since multiple providers are in use, you can have end-users utilize a combination of tru...