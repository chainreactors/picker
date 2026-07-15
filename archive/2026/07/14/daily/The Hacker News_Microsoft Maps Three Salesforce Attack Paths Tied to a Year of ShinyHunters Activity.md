---
title: Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity
url: https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:50:00.878104
---

# Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity

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

# [Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity](https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html)

**Swati Khandelwal**Jul 14, 2026SaaS Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu2gmOSckwOqmlhqAYdrlHfRuTsOJIi7dr9cFZosLQAJeoJxcUVQ9PvibcfnCsBdPWvfJRRrxoS8nx9yTt9NtDNCwVCFavEt7tQT0viD7AwGvUjhu-_k0B2J4KBSAJ-5GUGFZHCTSyOuW4I082lHoUkbsbH33tsIeo3gm71_CkjMd_bcAN7i4xPvMnefA/s1700-e365/salesforce-attack-path.jpg)

Attackers whose methods line up with the data-extortion group [ShinyHunters](https://thehackernews.com/2025/08/cybercrime-groups-shinyhunters.html) have spent the past year walking into corporate Salesforce environments without exploiting a single flaw in the platform.

The way in has been the trust the organization had already extended, usually through the OAuth connections that tie Salesforce to the apps and third-party vendors around it.

In [research published July 13](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/), Microsoft mapped the campaigns, which ran from mid-2025 into mid-2026, to three distinct techniques. It also worked with Salesforce to roll out new detection and governance tooling aimed at addressing the activity authentication logs miss.

That is what makes this hard to catch. When the access comes from a real user who approved a connected app, or from an integration the company already trusts, the traffic reads as ordinary use, and sign-in and authentication monitoring barely registers it.

What matters is what the app or account does once it is in, and that is exactly what most Salesforce logging was not built to show.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Microsoft groups the activity into three intrusion paths:

* **vishing calls** that trick employees into approving a malicious connected app,
* **stolen OAuth tokens** from compromised software vendors, and
* **misconfigured guest access** to Salesforce sites.

Each maps onto a Salesforce incident from the past year, and Microsoft says it saw the activity across tenants in industries including retail, education, and manufacturing.

## The phone call

The first path is the one that kicked off the whole run. Starting in mid-2025, the actors placed voice-phishing (vishing) calls posing as IT support and talked employees through Salesforce's OAuth consent screen, getting them to authorize an attacker-controlled connected app dressed up as Salesforce's own Data Loader tool.

Once consent was granted, the app could make API calls as that user, letting the attackers enumerate the org's Salesforce data, hold persistent access to CRM records, and hunt for credentials that might open the door to other SaaS platforms.

No malware, no stolen password replay. Just a phone call and a consent click.

This is the campaign Google's Threat Intelligence Group (GTIG) and Mandiant [documented in mid-2025](https://thehackernews.com/2025/06/google-exposes-vishing-group-unc6040.html), tracking the initial access as UNC6040 and the follow-on extortion as UNC6240, both of which kept claiming to be ShinyHunters to lean harder on victims.

Google confirmed one of its own corporate Salesforce instances was hit in June 2025, with the attackers taking largely public business contact data before Google cut them off. The same wave was publicly linked to breaches at Chanel and Pandora, with Adidas, Qantas, Allianz Life, and several LVMH brands also named as targets.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7YDSJQ_TsC_gjpz2bXw9np3RrGoSxobdk_hteDYF_6icbsyxAkTyokULK1EvsjrwM2NJQfiEocJ6gTS3mWMIWcJDtar8NfrpvyM1zmkxP161qPNy5zO0ZWG3p66erRigS-yL0CP1TLsca9lrLtFFTAMkEvqExYA0X6Eti0Ll5E4pWy0VY2qpYNcK75hc/s1700-e365/ms-chain.jpg)

Mandiant's advice to defenders was blunt: these calls exploit a help desk's instinct to be helpful, standard identity checks often do not apply, and the safe move is to hang up and call back on a known-good channel.

## Stolen tokens from trusted vendors

The second path skips the employee entirely. Instead of phishing a user, the attackers compromise a third-party vendor whose app already holds OAuth access to its customers' Salesforce orgs, steal the connection secrets or tokens, and use them to query and export data across many downstream instances at once.

Because the traffic comes from an approved integration, it does not trigger sign-in alarms and blends into normal automation.

Microsoft points to three incidents here. The August 2025 [Salesloft Drift compromise](https://thehackernews.com/2025/09/salesloft-takes-drift-offline-after.html) is the biggest and the clearest: attackers stole OAuth and refresh tokens tied to the Drift AI chat integration and turned them against Salesforce customer environments.

Google estimated that the Drift token theft potentially exposed more than 700 organizations, among them Cloudflare, Zscaler, Palo Alto Networks, Proofpoint, PagerDuty, and Tanium. Google tracks the cluster as UNC6395; Cloudflare's Cloudforce One calls it GRUB1.

Salesloft later traced the root cause to the attacker's access to its GitHub account as early as March 2025, which was used to reach Drift's AWS environment and harvest the tokens. The operators were there for secrets, running SOQL queries to sift through support cases and other objects for AWS keys, Snowflake tokens, and passwords, then deleting their query jobs to slow down anyone investigating.

The November 2025 [Gainsight incident](https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html) ran the same play against a different vendor. Salesforce pulled Gainsight-published apps after spotting unusual API activity, and GTIG tied the campaign to ShinyHunters affiliates across more than 200 affected Salesforce instances.

The people ...