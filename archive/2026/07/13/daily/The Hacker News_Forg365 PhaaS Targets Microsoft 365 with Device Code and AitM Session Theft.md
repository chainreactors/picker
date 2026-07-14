---
title: Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft
url: https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
source: The Hacker News
date: 2026-07-13
fetch_date: 2026-07-14T04:48:21.138768
---

# Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft](https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html)

**Ravie Lakshmanan**Jul 13, 2026Email Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlR-dy6ENZN5NKa1_sViQqXH6fEfEROkwjKV9vTowPmCu_nOALJ89JzGg-ueVJMCAqDHHozMZGd8oWbIlAQDTI8anEd6A2ZK0MdBN_FiShR3UoHGL6Cf0Gbhv8dY9RkVlZxpOCmks29u8Fnmx-JcytGZlnKC_9EuColvIMY4Y5IXH91aRaN5HOgjvvSPEo/s1700-e365/ms-device-code1.jpg)

A new phishing-as-a-service (PhaaS) operation called **Forg365** is using a combination of [device code phishing](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html), adversary-in-the-middle (AitM) tactics, antibot evasion, artificial intelligence (AI)-assisted lure creation, and post-compromise mailbox operations targeting Microsoft 365 accounts.

Distributed via Telegram and costing $400 a month (or $3,800 per year), attack chains leverage phishing lures that make use of legitimate email delivery infrastructure, such as Amazon Simple Email Service (Amazon SES) and Twilio SendGrid, to imitate a redirection chain that blends into regular email traffic before it ends in Forg365-controlled domains.

"The panel exposes a mature operator workflow: accounts, links, invitations, OAuth app configuration, redirect links, SVG generation, campaign sending, SMTP profiles, SMTP rotation, AI email generation, token vaulting, account intelligence, keyword alerts, viewer links, and browser-extension support," ZeroBAC [said](https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas).

The email security company said the PhaaS kit is best understood as similar to the [Kali365](https://thehackernews.com/2026/05/threatsday-bulletin-claude-security.html#kali365-targets-microsoft-365) (aka Octopi365 and Freedom365) and [Sneaky 2FA](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html) ecosystem, reflecting the industrialization of the business model, which is now combining bringing together lure creation, delivery, evasion, token/session handling, and post-compromise operations under a subscription-based setup that allows even threat actors with little-to-no technical expertise to orchestrate phishing campaigns with minimal effort and at scale.

Attack chains using Forg365 have been observed using business document-themed or remittance approval lures to trick recipients into clicking on malicious links. The sender domain uses Amazon SES for delivery, while the message body contains SendGrid-hosted images or tracking resources.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Customers who successfully complete Telegram registration utilize an operator panel accessible over the clearnet ("logfriend[.]com/login"), from where they can generate lures, set up campaigns, and manage captured tokens.

"Forg365 includes a device-auth phishing branch that presents a Microsoft-styled verification code page and pushes the victim into a legitimate Microsoft Authentication Broker sign-in flow," ZeroBAC explained. "The victim sees real Microsoft authentication surfaces, but the code authorizes an attacker-controlled session."

For AitM phishing, the platform employs route tokens, session cookies, and traffic classification to determine whether to serve phishing content or a benign decoy. If a VPN connection is detected, the kit redirects to innocuous decoy content instead of exposing the phishing pages.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOTm-A07kB-4lDl0mxEhEansYs4m3wMQFiz8iqBJajQgGbf21EJ8kDR6qDMxX8Y1nxOgPx8wbFakbp89yxqVq96oysQ240zu45sVk1Z0soEZHabmcy_KisCgjjP5Jfz5-iejktTBasPI0cEBG606sfhPK2zOJBmA7_Scn-xOov1gxWmK9myfiCHocEVcFn/s1700-e365/forg.png)

A notable aspect of the Forg365 platform is that it offers an extension named ForgCookie for Chromium-based browsers like Google Chrome, Microsoft Edge, and Brave that is designed for continued access to the compromised accounts. Described as an "automatic SSO cookie refresh for Microsoft services," the add-on acts as an intermediary between the token acquisition and browser access by cycling through the steps listed below -

* Requests account data from the Forg365 backend
* Calls the cookie-generation endpoint for a selected account
* Clears Microsoft session cookies
* Injects the generated refresh-token credential cookie into the Microsoft login domain
* Triggers a silent OAuth flow
* Captures resulting Microsoft cookies across Microsoft domains

Forg365's extends beyond simple credential and token harvesting to facilitate a wide array of post-compromise actions, including monitoring for specific keywords in compromised email accounts and drafting a message response to a particular email thread using assistance from AI.

"The result is a platform that lowers the skill threshold while increasing operational consistency. Less experienced affiliates can use prebuilt templates, while more capable operators can customize landing pages, rotate infrastructure, manage tokens, generate cookie material, and monitor compromised accounts," ZeroBAC said.

The disclosure coincides with the discovery of various campaigns that have been found to employ phishing kits for credential theft -

* Sending [fake Microsoft account activity alerts](https://zerobec.com/blog/sneaky-2fa-returns-trusted-sender-tenant-branded-microsoft-365-replay) from a legitimate-but-compromised third-party SaaS sender account to direct users to Sneaky 2FA-style phishing pages to launch a redirection chain that leads to the final phishing host, but not before performing checks to decide whether the visitor is a real user.
* Using phishing emails that direct recipients to a website hosted on Canva, which then triggers the device code phishing flow to hijack Microsoft accounts using the [Kali65 phishing kit](https://www.h...