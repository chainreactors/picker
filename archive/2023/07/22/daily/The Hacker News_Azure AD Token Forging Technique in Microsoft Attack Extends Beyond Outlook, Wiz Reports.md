---
title: Azure AD Token Forging Technique in Microsoft Attack Extends Beyond Outlook, Wiz Reports
url: https://thehackernews.com/2023/07/azure-ad-token-forging-technique-in.html
source: The Hacker News
date: 2023-07-22
fetch_date: 2025-10-04T11:57:59.325270
---

# Azure AD Token Forging Technique in Microsoft Attack Extends Beyond Outlook, Wiz Reports

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

# [Azure AD Token Forging Technique in Microsoft Attack Extends Beyond Outlook, Wiz Reports](https://thehackernews.com/2023/07/azure-ad-token-forging-technique-in.html)

**Jul 21, 2023**Ravie LakshmananEmail Security / Cyber Attack

[![Azure Active Directory](data:image/png;base64... "Azure Active Directory")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGsPoSyu2HG3abZ2cWch2qqjzVmIy0ogJ_rX9N6xzPnHO5gUW5dPfzzoMvGcPLAavXQblFhTdw2XsICn6ijvuSLxMKJZWM95kwIglqsa7ZDR8XOLercqMjaMHBwAgH4Zb1D2sVg--F5nAugYc8wBEw6p90EFCycyOLFSeRJLh_m7dHSiBTZALwk0TiRhWJ/s790-rw-e365/ms.jpg)

The recent attack against [Microsoft's email infrastructure](https://thehackernews.com/2023/07/microsoft-expands-cloud-logging-to.html) by a Chinese nation-state actor referred to as Storm-0558 is said to have a broader scope than previously thought.

According to cloud security company Wiz, the inactive Microsoft account (MSA) consumer signing key used to forge Azure Active Directory (Azure AD or AAD) tokens to gain illicit access to Outlook Web Access (OWA) and Outlook.com could also have allowed the adversary to forge access tokens for various types of Azure AD applications.

This [includes](https://www.wiz.io/blog/storm-0558-compromised-microsoft-key-enables-authentication-of-countless-micr) every application that supports personal account authentication, such as OneDrive, SharePoint, and Teams; customers applications that support the "Login with Microsoft functionality," and multi-tenant applications in certain conditions.

"Everything in the world of Microsoft leverages Azure Active Directory auth tokens for access," Ami Luttwak, chief technology officer and co-founder of Wiz, said in a statement. "An attacker with an AAD signing key is the most powerful attacker you can imagine, because they can access almost any app – as any user. This is a 'shape shifter' superpower."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Microsoft, last week, [disclosed](https://thehackernews.com/2023/07/microsoft-bug-allowed-hackers-to-breach.html) the token forging technique was exploited by Storm-0558 to extract unclassified data from victim mailboxes, but the exact contours of the cyber espionage campaign remains unknown.

The Windows maker said it's still investigating as to how the adversary managed to acquire the MSA consumer signing key. But it's unclear if the key functioned as a master key of sorts to unlock access to data belonging to nearly two dozen organizations.

Wiz's analysis fills in some of the blanks, with the company discovering that "all Azure personal account v2.0 applications depend on a list of [8 public keys](https://login.microsoftonline.com/consumers/discovery/v2.0/keys), and all Azure multi-tenant v2.0 applications with Microsoft account enabled depend on a list of [7 public keys](https://login.microsoftonline.com/common/discovery/v2.0/keys)."

[![Azure Active Directory](data:image/png;base64... "Azure Active Directory")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghUDgoU-VKCs9ViiHpRNmx3Upb_pPJtFJCdNWm0TwxGOyEsxJ4ZGEXJWoahYOjL2_5PjzsadjnIZ1L3Jw87COYyBVCMMLrJRFbklaaZFK4pdP3L6bDS-4VasUlVvCClB0DwJiO2li7_HgT5sUVWiJXXKCTGHz3wliFOvdqdzquUfvZMuYDw8dI-TnGFxVn/s790-rw-e365/wiz.jpg)

It further found that Microsoft replaced one of the the listed public keys (thumbprint: "d4b4cccda9228624656bff33d8110955779632aa") that had been present [since at least 2016](https://web.archive.org/web/20160801114452/https%3A/login.microsoftonline.com/common/discovery/v2.0/keys) sometime between June 27, 2023, and July 5, 2023, around the same period the company said it had revoked the MSA key.

"This led us to believe that although the compromised key acquired by Storm-0558 was a private key designed for Microsoft's MSA tenant in Azure, it was also able to sign OpenID v2.0 tokens for multiple types of Azure Active Directory applications," Wiz said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Storm-0558 seemingly managed to obtain access to one of several keys that were intended for signing and verifying AAD access tokens. The compromised key was trusted to sign any OpenID v2.0 access token for personal accounts and mixed-audience (multi-tenant or personal account) AAD applications."

This effectively meant that the loophole could theoretically enable malicious actors to forge access tokens for consumption by any application that depends on the Azure identity platform.

Even worse, the acquired private key could have been weaponized to forge tokens to authenticate as any user to an affected application that trusts Microsoft OpenID v2.0 mixed audience and personal-accounts certificates.

"Identity provider's signing keys are probably the most powerful secrets in the modern world," Wiz security researcher Shir Tamari said. "With identity provider keys, one can gain immediate single hop access to everything, any email box, file service, or cloud account."

### Update

When reached for comment, Microsoft shared the following statement with The Hacker News -

*Many of the claims made in this blog are speculative and not evidence-based. We recommend that customers review our blogs, specifically our* [*Microsoft Threat Intelligence blog*](https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/)*, to learn more about this incident and investigate their own environments using the Indicators of Compromise (IOCs) that we've made public. We’ve also recently* [*expanded security logging*](https://www.microsoft.com/en-us/security/blog/2023/07/19/expanding-cloud-logging-to-give-customers-deeper-security-visibility/) *availability, making it free for more customers by default, to help enterprises manage an increasingly complex threat landscape.*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ...