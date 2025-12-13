---
title: New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale
url: https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html
source: The Hacker News
date: 2025-12-12
fetch_date: 2025-12-13T03:16:31.345149
---

# New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [New Advanced Phishing Kits Use AI and MFA Bypass Tactics to Steal Credentials at Scale](https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html)

**Dec 12, 2025**Ravie LakshmananMalware / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4a8r1ltQRVAHGAuHpS5vuzkIAKVgEgZQt0hi_nLCDg6akixRXUC_2sswGCHs8tFV2oLmaZd-YAwL-Yu09qMZMC64PZ2EQNycGfpxLzqwqGXaf1mPfKRZtx4XWLOKPXc1uyH_zVni2tBfNkiOUQL0Cdy4qqTRGu99eo6jDQbNq6O1-lvaZ8ZmKI3r9EG0c/s790-rw-e365/1000039728.jpg)

Cybersecurity researchers have documented four new phishing kits named **BlackForce, GhostFrame, InboxPrime AI, and Spiderman** that are capable of facilitating credential theft at scale.

BlackForce, first detected in August 2025, is designed to steal credentials and perform Man-in-the-Browser ([MitB](https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html)) attacks to capture one-time passwords (OTPs) and bypass multi-factor authentication (MFA). The kit is sold on Telegram forums for anywhere between €200 ($234) and €300 ($351).

The kit, according to [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/technical-analysis-blackforce-phishing-kit) researchers Gladis Brinda R and Ashwathi Sasi, has been used to impersonate over 11 brands, including Disney, Netflix, DHL, and UPS. It's said to be in active development.

"BlackForce features several evasion techniques with a blocklist that filters out security vendors, web crawlers, and scanners," the company said. "BlackForce remains under active development. Version 3 was widely used until early August, with versions 4 and 5 being released in subsequent months."

Phishing pages connected to the kit have been found to use JavaScript files with what has been described as "[cache busting](https://www.keycdn.com/support/what-is-cache-busting)" hashes in their names (e.g., "index-[hash].js"), thereby forcing the victim's web browser to download the latest version of the malicious script instead of using a cached version.

In a typical attack using the kit, victims who click on a link are redirected to a malicious phishing page, after which a server-side check filters out crawlers and bots, before serving them a page that's designed to mimic a legitimate website. Once the credentials are entered on the page, the details are captured and sent to a Telegram bot and a command-and-control (C2) panel in real-time using an HTTP client called [Axios](https://thehackernews.com/2025/09/axios-abuse-and-salty-2fa-kits-fuel.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhsdbOJUYShGTVO1SPA_Q34p28W5QP9rYwjZbmbWgBuaw_El1kI3ypHrIMzNwEoe7kJf0KbjZ57iDCcEYOstLeFHcViFCwQOhpVhlUQ91FkNPc40SyY-GHrrWBXJ1eHpcPVVats18s0a39U3eUMnY7eKkYzdyPUxMu55IfW6mV4ScDVciyQ1I5o98vPV0W/s2600/zz.jpg)

When the attacker attempts to log in with the stolen credentials on the legitimate website, an MFA prompt is triggered. At this stage, the MitB techniques are used to display a fake MFA authentication page to the victim's browser through the C2 panel. Should the victim enter the MFA code on the bogus page, it's collected and used by the threat actor to gain unauthorized access to their account.

"Once the attack is complete, the victim is redirected to the homepage of the legitimate website, hiding evidence of the compromise and ensuring the victim remains unaware of the attack," Zscaler said.

### GhostFrame Fuels 1M+ Stealth Phishing Attacks

Another nascent phishing kit that has gained traction since its discovery in September 2025 is GhostFrame. At the heart of the kit's architecture is a simple HTML file that appears harmless while hiding its malicious behavior within an embedded iframe, which leads victims to a phishing login page to steal Microsoft 365 or Google account credentials.

"The iframe design also allows attackers to easily switch out the phishing content, try new tricks or target specific regions, all without changing the main web page that distributes the kit," Barracuda security researcher Sreyas Shetty [said](https://blog.barracuda.com/2025/12/04/threat-spotlight-ghostframe-phishing-kit). "Further, by simply updating where the iframe points, the kit can avoid being detected by security tools that only check the outer page."

Attacks using the GhostFrame kit commence with typical phishing emails that claim to be about business contracts, invoices, and password reset requests, but are designed to take recipients to the fake page. The kit uses anti-analysis and anti-debugging to prevent attempts to inspect it using browser developer tools, and generates a random subdomain each time someone visits the site.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

The visible outer pages come with a loader script that's responsible for setting up the iframe and responding to any messages from the HTML element. This can include changing the parent page's title to impersonate trusted services, modifying the site favicon, or redirecting the top-level browser window to another domain.

In the final stage, the victim is sent to a secondary page containing the actual phishing components through the iframe delivered via the constantly changing subdomain, thereby making it harder to block the threat. The kit also incorporates a fallback mechanism in the form of a backup iframe appended at the bottom of the page in the event the loader JavaScript fails or is blocked.

### InboxPrime AI Phishing Kit Automates Email Attacks

If BlackForce follows the same playbook as other traditional phishing kits, InboxPrime AI goes a step further by leveraging artificial intelligence (AI) to automate mass mailing campaigns. It's advertised on a 1,300-member-strong Telegram channel under a malware-as-a-service (MaaS) subscription model for $1,000, granting purchasers a perpetual license and full access to the source code.

"It is designed to mimic real human emailing behavior and even leverages Gmail's web interface to ev...