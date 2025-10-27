---
title: SolarWinds Patches 8 Critical Flaws in Access Rights Manager Software
url: https://thehackernews.com/2024/07/solarwinds-patches-11-critical-flaws-in.html
source: The Hacker News
date: 2024-07-20
fetch_date: 2025-10-06T17:45:17.730069
---

# SolarWinds Patches 8 Critical Flaws in Access Rights Manager Software

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

# [SolarWinds Patches 8 Critical Flaws in Access Rights Manager Software](https://thehackernews.com/2024/07/solarwinds-patches-11-critical-flaws-in.html)

**Jul 19, 2024**Ravie LakshmananVulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhkGdjr6XuFyh7zOoiKmBr603BuQRHYn-d89rC76oTUtmPwLIrN8qc3F3Fn0izgij4gk6FQG6DjShN6l69VIrbefNEXWA_HUPAje4FnkrpL8_TUI6rW0nzAW06yGr00p5QhFKK0nFegj1Lg1ZsYou47KqGPj99y5POV2KKEDcSNds6HRiLHPuokpTJ2O3o/s790-rw-e365/solarwinds.png)

SolarWinds has [addressed](https://www.solarwinds.com/trust-center/security-advisories) a set of critical security flaws impacting its Access Rights Manager (ARM) software that could be exploited to access sensitive information or execute arbitrary code.

Of the 13 vulnerabilities, eight are rated Critical in severity and carry a CVSS score of 9.6 out of 10.0. The remaining five weaknesses have been rated High in severity, with four of them having a CVSS score of 7.6 and one scoring 8.3.

The most severe of the flaws are listed below -

* **CVE-2024-23472** - SolarWinds ARM Directory Traversal Arbitrary File Deletion and Information Disclosure Vulnerability
* **CVE-2024-28074** - SolarWinds ARM Internal Deserialization Remote Code Execution Vulnerability
* **CVE-2024-23469** - Solarwinds ARM Exposed Dangerous Method Remote Code Execution Vulnerability
* **CVE-2024-23475** - Solarwinds ARM Traversal and Information Disclosure Vulnerability
* **CVE-2024-23467** - Solarwinds ARM Traversal Remote Code Execution Vulnerability
* **CVE-2024-23466** - Solarwinds ARM Directory Traversal Remote Code Execution Vulnerability
* **CVE-2024-23470** - Solarwinds ARM UserScriptHumster Exposed Dangerous Method Remote Command Execution Vulnerability
* **CVE-2024-23471** - Solarwinds ARM CreateFile Directory Traversal Remote Code Execution Vulnerability

Successful exploitation of the aforementioned vulnerabilities could allow an attacker to read and delete files and execute code with elevated privileges.

The shortcomings have been addressed in version 2024.3 released on July 17, 2024, following responsible disclosure as part of the Trend Micro Zero Day Initiative (ZDI).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes after the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [placed](https://thehackernews.com/2024/07/cisco-warns-of-critical-flaw-affecting.html) a high-severity path traversal flaw in SolarWinds Serv-U Path (CVE-2024-28995, CVSS score: 8.6) to its Known Exploited Vulnerabilities (KEV) catalog following reports of active exploitation in the wild.

The network security company was the victim of a [major supply chain attack](https://thehackernews.com/2021/01/heres-how-solarwinds-hackers-stayed.html) in 2020 after the update mechanism associated with its Orion network management platform was compromised by [Russian APT29 hackers](https://thehackernews.com/2021/01/fbi-cisa-nsa-officially-blames-russia.html) to distribute malicious code to downstream customers as part of a high-profile cyber espionage campaign.

The breach prompted the U.S. Securities and Exchange Commission (SEC) to [file](https://www.sec.gov/newsroom/press-releases/2023-227) a lawsuit against SolarWinds and its chief information security officer (CISO) last October alleging the company failed to disclose adequate material information to investors regarding cybersecurity risks.

However, much of the claims pertaining to the lawsuit were [thrown out](https://www.courtlistener.com/docket/67927585/securities-and-exchange-commission-v-solarwinds-corp/) by the U.S. District Court for the Southern District of New York (SDNY) on July 18, stating "these do not plausibly plead actionable deficiencies in the company's reporting of the cybersecurity hack" and that they "impermissibly rely on hindsight and speculation."

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
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[network security](https://thehackernews.com/search/label/network%20security)[software update](https://thehackernews.com/search/label/software%20update)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain]...