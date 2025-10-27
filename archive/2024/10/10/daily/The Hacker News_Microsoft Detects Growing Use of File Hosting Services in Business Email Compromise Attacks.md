---
title: Microsoft Detects Growing Use of File Hosting Services in Business Email Compromise Attacks
url: https://thehackernews.com/2024/10/microsoft-detects-growing-use-of-file.html
source: The Hacker News
date: 2024-10-10
fetch_date: 2025-10-06T18:59:00.223822
---

# Microsoft Detects Growing Use of File Hosting Services in Business Email Compromise Attacks

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

# [Microsoft Detects Growing Use of File Hosting Services in Business Email Compromise Attacks](https://thehackernews.com/2024/10/microsoft-detects-growing-use-of-file.html)

**Oct 09, 2024**Ravie LakshmananEnterprise Security / Identity Theft

[![Business Email Compromise Attacks](data:image/png;base64... "Business Email Compromise Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgc71bvcvF0hZUe4jbeVxiiO6oLKTjl5tnfdfC4U3CvvQMxvjuH6gyuU6BWub1iluITDr0YwtP-gPLVgc4_fzyhnhe66tsjOGAKVvzgud_Xuxjh1Vo4xEI14IzumyxA4ex2bsULbAeNjZLjhVonEq0ZTnSmR8g7o_lUM-kX0o_CFNZsFHYWkI2O-w-6iP49/s790-rw-e365/phishing.png)

Microsoft is [warning](https://www.microsoft.com/en-us/security/blog/2024/10/08/file-hosting-services-misused-for-identity-phishing/) of cyber attack campaigns that abuse legitimate file hosting services such as SharePoint, OneDrive, and Dropbox that are widely used in enterprise environments as a defense evasion tactic.

The end goal of the campaigns are broad and varied, allowing threat actors to compromise identities and devices and conduct business email compromise ([BEC](https://thehackernews.com/2023/06/microsoft-uncovers-banking-aitm.html)) attacks, which ultimately result in financial fraud, data exfiltration, and lateral movement to other endpoints.

The weaponization of legitimate internet services (LIS) is an increasingly popular risk vector adopted by adversaries to blend in with legitimate network traffic in a manner such that it often bypasses traditional security defenses and complicates attribution efforts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The approach is also called [living-off-trusted-sites](https://thehackernews.com/2024/01/threat-actors-increasingly-abusing.html) (LOTS), as it leverages the trust and familiarity of these services to sidestep email security guardrails and deliver malware.

Microsoft said it has been observing a new trend in phishing campaigns exploiting legitimate file hosting services since mid-April 2024 that involve files with restricted access and view-only restrictions.

[![Business Email Compromise Attacks](data:image/png;base64... "Business Email Compromise Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisFKEH7wZ5JVFwhuGNFlqCs94M_Ki4-oPdxTHDu3xghyphenhyphenA0BQM0EzSc0ZdMmWcQ65NCyU9eFYqNiX_jXB7wMRZ5ADLICTXq_0yOCqjkpFbXSxA2FPPI8PCcocpa1kdFdRH7HshrC6utCU0cANXmnIyCHkiVSPl2f2KE9x-tNuigg0YnsfCpU-PXvF_VwDvl/s790-rw-e365/ms.png)

Such attacks often begin with the compromise of a user within a trusted vendor, leveraging the access to stage malicious files and payloads on the file hosting service for subsequent sharing with a target entity.

"The files sent through the phishing emails are configured to be accessible solely to the designated recipient," it said. "This requires the recipient to be signed in to the file-sharing service — be it Dropbox, OneDrive, or SharePoint — or to re-authenticate by entering their email address along with a one-time password (OTP) received through a notification service."

What's more, the files shared as part of the phishing attacks are set to "view-only" mode, preventing the ability to download and detect embedded URLs within the file.

A recipient who attempts to access the shared file is then prompted to verify their identity by providing their email address and a one-time password sent to their email account.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Once they are successfully authorized, the target is instructed to click on another link to view the actual contents. However, doing so redirects them to an adversary-in-the-middle ([AitM](https://thehackernews.com/2023/08/phishing-as-service-gets-smarter.html)) phishing page that steals their password and two-factor authentication (2FA) tokens.

This not only enables the threat actors to seize control of the account, but also use it to perpetuate other scams, including BEC attacks and financial fraud.

[![Business Email Compromise Attacks](data:image/png;base64... "Business Email Compromise Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiOSGbsR6ffdAbZJyypnVPWcKGdMIKlxMbzRw8Qe6eQsVKHeKfnwYPgUCnVLC1T8IgAmgvN5kM35SOHJJ6iHQokJ8oYPvrGDual-eBgiu3aTF_9N5LUK23d-ZvduU82LcwlyNGZhs-GH-pmgqaBq-baNH0XvbrWAwNgLrskc0lX2j1dv-DE8fcqhiDut6G/s790-rw-e365/chart.png)

"While these campaigns are generic and opportunistic in nature, they involve sophisticated techniques to perform social engineering, evade detection, and expand threat actor reach to other accounts and tenants," the Microsoft Threat Intelligence team said.

The development comes as Sekoia detailed a new AitM phishing kit called Mamba 2FA that's sold as phishing-as-a-service (PhaaS) to other threat actors to conduct [email phishing campaigns](https://any.run/cybersecurity-blog/analysis-of-the-phishing-campaign/) that propagate HTML attachments impersonating Microsoft 365 login pages.

The kit, which is offered on a subscription basis for $250 per month, supports Microsoft Entra ID, AD FS, third-party SSO providers, and consumer accounts. Mamba 2FA has been actively put to use since November 2023.

"It handles two-step verifications for non-phishing-resistant MFA methods such as one-time codes and app notifications," the French cybersecurity company [said](https://blog.sekoia.io/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem/). "The stolen credentials and cookies are instantly sent to the attacker via a Telegram bot."

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
[**...