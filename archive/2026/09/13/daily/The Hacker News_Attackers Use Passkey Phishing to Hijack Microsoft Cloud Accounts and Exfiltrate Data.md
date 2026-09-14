---
title: Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data
url: https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html
source: The Hacker News
date: 2026-09-13
fetch_date: 2026-09-14T07:21:38.743366
---

# Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html)

**Ravie Lakshmanan**Sep 13, 2026Cloud Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZ2E2hmYwxfZ25xw5iPhCHaSDENcuEyEIaha9e_rIJCf68srth31FtjIiIlnOcEiSQDDuk2Vg-dQdNLfR753ePSoDntP3BS-MGbEH2DS8Ch5ihzhpiDZZm5UIzKCbL1vNJSwSABCYst8oG6Oa-7iBWaSF6WSTEkCJBAi9YEEwAmVEdGYvu-JWZnxwEX9ni/s1700-nu-rw-lo-l85-e365/ms-outlook.jpg)

Microsoft has disclosed details of two campaigns in which threat actors are abusing third-party email delivery infrastructure to blast financial fraud scam messages and using passkey-themed social engineering to breach cloud environments.

The first campaign, per the tech giant, [involved](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/) sending over a million scam emails between August 3 and 5, 2026, by masquerading as chief executive officers (CEOs) of various target companies, aiming to persuade accounts payable departments at those firms to initiate Automated Clearing House ([ACH](https://en.wikipedia.org/wiki/Automated_clearing_house)) transfers for a supposed ServiceNow annual subscription.

Evidence indicates that the operators behind the campaign have leveraged generative artificial intelligence (AI) to facilitate the creation of email templates and draft emails tailored to their recipients. The activity primarily singled out enterprise users in the U.S., spanning IT services, consumer goods, real estate, and discrete manufacturing sectors.

"The campaign follows steps before and during the execution of the campaign: threat actors register impersonation domains, send executive-themed payment requests through trusted infrastructure, embed fabricated invoices and supporting conversations, and attempt to convince finance personnel to initiate ACH transfers," the Microsoft Security Research team said.

"Unlike traditional invoice scams that rely on a single social engineering lure, this campaign layered executive impersonation, vendor branding, fabricated invoices, and supporting email conversations into a unified narrative intended to reduce recipient skepticism."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The spoofed email messages contained a purported "approval" of the fake invoice to trick recipients into making payments to attacker-controlled accounts. To lend a veneer of legitimacy to the deception, the threat actor included a forged email thread along with the fabricated invoice.

In a clever twist, the attackers identified CEOs, CFOs, and presidents at victim organizations and plugged their names and email addresses into the emails' signatures so that they look convincing to the targets. The campaign also heavily relied on bogus domains and content designed to impersonate trusted brands and individuals. Some of the registered domains are below -

* service-nowinc[.]com
* domainlify[.]net

### Passkey-Themed Social Engineering Leads to Cloud Compromise

The second campaign [documented](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/) by Redmond revolves around cloud-based intrusions targeting multiple accounts in which suspicious sign-ins are followed by the threat actors adding their own authentication methods, as well as high-volume Microsoft Graph activity, SharePoint and OneDrive downloads, and mailbox collection through REST APIs.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsgTA62KeChax7m4nz_mJcDR1jGwk8hPK3xTkBox0PhTtyp1MZeEhXA1YYkhnXlOnojFePzZYCrhcNcG6DH2V9PCcdqRciCAMf4CviCCGbDydN5gYJ_CIg9U3Fzllv7J3Ob3pvByrkx3Af8xwiEkkXWGtfqpNiL4U-aDOT_Ng0HMB0lYM8FW-p0PB0IrfK/s1700-nu-rw-lo-l85-e365/email-spoofed.jpg)

The activity, which has been detected since May 2026, is consistent with "automated collection from compromised cloud identities using proxy-associated infrastructure," Microsoft said.

The attack commonly begins with identity-focused social engineering. The threat actors call or message a user's personal phone number, while claiming to be from the organization's IT help desk and urging them to immediately update their passkey, multi-factor authentication (MFA), or single sign-on (SSO) configuration to avoid access disruptions.

Unsuspecting employees are redirected to counterfeit websites that mimic the legitimate Microsoft sign-in experience via SMS messages sent to their personal devices. The end goal here is to use the pretext to guide them through adversary-in-the-middle (AitM) or [device-code authentication](https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html) flows and take control of their Microsoft accounts either by capturing the credentials or unknowingly granting access on the actor's behalf.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjExN_uMYNRJdFFWHrUjkTOk-LUQBWc-wvfvLvvDAg-hVLLNPTVewWBKHdsrHnDjYR2wHFBtIDhg2_uYPdkAtFIKSpY4A9EQwil5nCzML4Lru1qIX3bAC01wJP_TBstB0ad-94NKI7CFnvvgpVeSJiSY9_7ngnD2jBJgkrEwfoLq4qMgNuek11o78D__Udz/s1700-nu-rw-lo-l85-e365/passkeys.jpg)

"The actor appears to invest heavily in pre-attack research, likely gathering information about employees and organizational structure from public sources such as social networking and professional profiling platforms," Microsoft said. "In a smaller number of cases, actors take advantage of already compromised accounts to expand their reach" by sending similar passkey-themed messages via Microsoft Teams.

What's more, the threat actor has been observed registering domains built around themes such as passkeys, SSO enrollment, account activation, and identity verification, at the same time including the target organization's n...