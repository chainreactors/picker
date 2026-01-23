---
title: Filling the Most Common Gaps in Google Workspace Security
url: https://thehackernews.com/2026/01/filling-most-common-gaps-in-google.html
source: The Hacker News
date: 2026-01-22
fetch_date: 2026-01-23T03:33:36.325183
---

# Filling the Most Common Gaps in Google Workspace Security

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

# [Filling the Most Common Gaps in Google Workspace Security](https://thehackernews.com/2026/01/filling-most-common-gaps-in-google.html)

**The Hacker News**Jan 22, 2026Email Security / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjppNAJYCOHh4mqdL3GuJ4elABk4wn-ciw9V6oYuZ8Sdb0LllyS_YRl6YXX-I_eaMDcVG8Zt9X42HbFVlmEb0umu4D4nelT-qOpG7ZtYSz0t-wbngKFalwdDHW4VHUlNXfMUswtSCx4WptHTAoKHJo94vWXVjSq4cGRP4FyN1P35n8dc8_dl-2yi3jFePU/s1600-e365/main.png)

Security teams at agile, fast-growing companies often have the same mandate: secure the business without slowing it down. Most teams inherit a tech stack optimized for breakneck growth, not resilience. In these environments, the security team is the helpdesk, the compliance expert, and the incident response team all rolled into one.

Securing the cloud office in this scenario is all about finding leverage: identifying the strategic control points that drive the most resilience without adding operational overhead.

Google Workspace provides an excellent security foundation, but its native tooling has inherent limitations, and relying on the default configurations can cause headaches. To build a truly resilient program, there are some common-sense first steps teams can take to secure Workspace natively, before intelligently augmenting the platform where its capabilities fall short.

## Secure email, the primary attack vector and largest archive

Email remains the most reliable target for attackers, as an initial attack method, as a vector to other connected apps and systems, and as a target for sensitive data. While Gmail's default security is solid at catching some threats, it often struggles with targeted threats and sophisticated social engineering and payload-less attacks.

### The gaps in native protection

* **BEC and Targeted spear phishing:** business email compromise (BEC) attacks often contain no malicious links or attachments, instead relying on social engineering that bypasses traditional defenses.
* **Environmental context**: Google doesn't know who your VIPs are, which partners you work with, or how frequently you receive invoices from vendors, making it difficult to flag subtle anomalies worth scrutinizing.
* **Data archive at rest:** for most companies, email is the largest repository of sensitive data. If an account is compromised, the attacker has access to years of confidential conversations, attachments, contracts, and more.

### How to improve Gmail's security today

While Google can't provide all the capabilities of a modern email security platform, there are steps you can take to ensure your core Gmail configurations are as secure as possible.

* **Turn on advanced scanning:** enable Google's enhanced pre-delivery message scanning and malware protection to ensure you're making the most of Google's capabilities.
* **Implement basic email hygiene:** configure SPF, DKIM, and DMARC. These protocols prove your emails are actually from you, and are critical for preventing domain spoofing.
* **Automate future settings:** ensure the "Apply future recommended settings automatically" option is checked to stay current as Google rolls out more security updates.

## Move beyond authentication to manage access

Multi-factor authentication (MFA) is the single most important control you can implement today, but it's not a magic bullet. Your access control can't stop at the login page.

### Too many windows and side doors

* **Malicious OAuth access:** compromised tokens, illicit consent grants, man-in-the-middle attacks, or simple misconfigurations can allow attackers access that appears perfectly legitimate to security tooling.
* **Legacy access:** protocols like IMAP and POP don't natively support MFA, and App Passwords can be circumvented.
* **Detection gaps:** Google can alert on suspicious sign-ins, but connecting that signal to other suspicious activity across the environment is a manual, time-consuming process.

### Harden your access control immediately

* **Enforce strong MFA:** not all MFA is created equal. At the very least, disable SMS or phone calls as MFA authentication methods. Ideally, adopt phishing-resistant methods like physical security keys or Yubikeys.
* **Disable legacy protocols:** turn off POP and IMAP access for all users within the Gmail settings.
* **Deny by default for OAuth:** require users to request access to unconfigured third-party apps rather than granting access by default.

## The next steps to proactive, modern security

A properly-configured Google Workspace offers a solid foundation for securing a fast-growing company. But as your company grows, your attack surface grows with it. For lean security teams who need to maximize their efficiency and their effectiveness, the end goal isn't just to have the right settings; it's to have visibility across all of Google Workspace, with detection and response capabilities to detect subtle signs of compromise if an account is breached.

Material Security builds on Google's foundation, providing visibility and context that Workspace lacks natively across the emails, files, and accounts within your environment.

### Advanced email protection

[Material's inbound protection](https://material.security/product/email?utm_source=third-party&utm_medium=blog&utm_campaign=20260122-the-hacker-news) combines threat research with AI, user report automation, and custom detection rules to provide multi-layered coverage to catch and remediate sophisticated threats. Granular automated remediations protect the entire organization from the first detection or user report, and automatically triage and respond to user-reported phishing.

Material is also the only platform on the market that protects sensitive email content, automatically detecting, classifying, and securing sensitive emails and attachments behind an MFA prompt, protecting critical information even in a breach.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGvs9NBRwiutOnXkKpbKLSPCt1Vcz2mWs-Kpb0smn0k3Akgq-EjYO7ic4zoAyoaKGsd0jL9jry7b7UsS5pGcfgLezFdIVKz6IiA0QmWTKOvrYIGlygVJAIGmPYlJn21bVShNmBHSp-7MpY7AFTTxtUvN8x7DmIfYK_96NjLN0gKTePNSMQIhmceiuTT4w/s1600-e365/1.png)

### Context-aware account security

A richer set of signals across the entire cloud office enables Material to detect and [stop account takeovers](https://materi...