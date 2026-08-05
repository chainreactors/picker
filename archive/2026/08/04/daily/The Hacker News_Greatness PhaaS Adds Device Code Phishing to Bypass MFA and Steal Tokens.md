---
title: Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens
url: https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html
source: The Hacker News
date: 2026-08-04
fetch_date: 2026-08-05T04:59:29.431542
---

# Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens

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

![cybersecurity](data:image/svg+xml;base64...)

# [Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens](https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html)

**Ravie Lakshmanan**Aug 04, 2026Phishing / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8YRyOCSodUbPpWMicgOiuGbEQWDBmu_W-47PAUFkS7yKEQe4Do6svH4cQb-U0tC53C9mqq8ijjlG9gwuzyqYfNwtS61WxvNxIgk1dVC7wX598rncb_MgQ5t4yxc8NUYVdb6PT5cu7ZXJ7w3KaYG_7vtU5xixHel1jSADbtR-GC1bmngZPArXw-NjkTH1x/s1700-e365/Greatness.jpg)

The commercial phishing-as-a-service (PhaaS) toolkit known as **Greatness** has become the latest crimeware solution to add support for device code phishing, a [rapidly growing](https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html) cyber threat that [abuses](https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html) the legitimate OAuth 2.0 Device Authorization Grant to bypass Multi-Factor Authentication (MFA) and seize control of user accounts.

"Greatness supports AiTM [adversary-in-the-middle] credential and token theft, device code phishing, and OAuth consent abuse, all from the same operator panel and shared backend infrastructure," ZeroBEC [said](https://zerobec.com/blog/greatness-phaas-aitm-and-device-code-phishing) in a report shared with The Hacker News detailing the PhaaS kit's latest capabilities.

"The platform now supports AiTM token theft, device code phishing, OAuth consent abuse, and multiple target platforms, including iCloud, Yahoo, and Google Workspace. This evolution reflects the broader trend of PhaaS platforms expanding from simple credential harvesting to integrated attack ecosystems."

The phishing platform was [first publicly documented](https://thehackernews.com/2023/05/new-phishing-as-service-platform-lets.html) by Cisco Talos in May 2023, highlighting how threat actors are incorporating it in their attacks to target Microsoft 365 business users since at least mid-2022.

Designed as a way to lower the [barrier of entry for cybercrime](https://thehackernews.com/2024/05/new-tricks-in-phishing-playbook.html), access to Greatness is facilitated through a subscription available on its public-facing Telegram channel (@GreatnessPage) that has more than 3,250 subscribers and serves as a central hub for announcements and feature updates.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Aspiring cybercriminals can obtain a subscription starting from $289 per month, up from the $120 per month figure [reported](https://thehackernews.com/2024/01/malicious-ads-on-google-target-chinese.html) back in January 2024. The subscription provides access to an operator that includes a dashboard with campaign statistics, domain configuration, CAPTCHA selection, and over 11 downloadable lure templates covering voicemail, document sharing, and QR codes, among others.

Operator registration, license provisioning, and support are offered via a dedicated Telegram bot (@gr8managerbot), while licenses can be procured or renewed by sending a message to the "@greatnessmgr" account, the developer handle that oversees operator support and platform development.

In a [post](https://t.me/GreatnessPage/125) shared in November 2025, the operators of the Telegram channel claim that Greatness keeps stolen cookies safe and secure via one-way hash protection and that the information can be extracted only by the customers with their Telegram account 2FA code.

*When you logged in with your telegram account and you insert 2FA in your side will create a token that only can access your logs so be sure only person can access is you as you see all info is hashed. Only way is accessing your telegram account so keep it safe and everything will be fine!*

*The most important thing for any service user is privacy. We respect all users' privacy because we have been in this business for 8 years and prioritize everything to provide you the best experience. Unlike others, we are always honest with our customers.*

Those who purchase a subscription by providing their Telegram chat ID and a bot API token can access the panel through a login page that requires a user ID and a 9-character license key to access the dashboard. Upon successful registration, customers are provisioned an operator-specific domain in the format: "api-[token].[base-domain]."

The dashboard is a one-stop shop that offers comprehensive campaign statistics, including the cookies captured and a heat map of victims. It also includes a links configuration page to select their phishing domain, CAPTCHA type, background theme, and the method for saving cookies, while the attachments section provides more than 11 downloadable and ready-to-use phishing lure templates that are packaged as ZIP files.

"Observed templates include: AudioLogin, ChatAssistance, WindowsExplorer, Voicemail, OneDrive, QR, VideoPlayer, and additional variants," ZeroBEC said. "Each template contains pre-built HTML, PDF redirectors, SVGs, and letter templates, lowering the barrier to entry so operators do not need to build lures from scratch."

Victims who end up interacting with a booby-trapped link embedded in the phishing email traverse through a five-stage redirect chain that implements anti-analysis protections, User-Agent fingerprinting, and a CAPTCHA gate, before taking them to the final destination, which can be either an AitM proxy or a device code endpoint.

The [device code phishing branch](https://blog.barracuda.com/2026/04/16/threat-spotlight-tycoon-2fa-scattered-everywhere) is a new addition to Greatness, allowing cybercriminals to leverage the OAuth device authorization grant flow to silently obtain tokens without user interaction.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOAHPHtHealarRuLqRBdjHny1bKMiOdEMFxIMIzw9gasI3Tk7MwVZJmYoZloQ4-g5yUyN_UjicJD37RoB2AabRGXYMbf6GQtpu93DeJHloU3CDOtvxgcn4ef8vZIrJRNX6CXsltA9m_GY9FLLsOKBnJcq0ERXt1T6tG6gG-EvvEzUk_SXXaBUYdKjschQ0/s1700-e365/bar.jpg)

"The first big shift was adversary-in-the-middle phishing, where a proxy site sits between the user and Microsoft and relays the login in real time to capture the session cookie," Trend Micro [said](https://www.trendmicro.com/en_us/research/26/g/device-code-ph...