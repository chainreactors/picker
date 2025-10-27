---
title: New TgToxic Banking Trojan Variant Evolves with Anti-Analysis Upgrades
url: https://thehackernews.com/2025/02/new-tgtoxic-banking-trojan-variant.html
source: The Hacker News
date: 2025-02-28
fetch_date: 2025-10-06T20:47:53.735591
---

# New TgToxic Banking Trojan Variant Evolves with Anti-Analysis Upgrades

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

# [New TgToxic Banking Trojan Variant Evolves with Anti-Analysis Upgrades](https://thehackernews.com/2025/02/new-tgtoxic-banking-trojan-variant.html)

**Feb 27, 2025**Ravie LakshmananCybercrime / Android

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLtDUL3VrW1kKnFf-G6X3-AWiYmYqtE8JXTyqDzDS27caafmjeHFQp7TTDdWx_D-PkwnkXMS4v2CRv0zNOapx_iQRv6HtBWliIj_eAYRpou_RWzlR-bhD3X9mUYs0851G-jYBuxt_T21tbXRUjZ_-R7iqQ6xzdl-tem0qKIyaDWtmFBtOgCkQUvsLl6KaT/s790-rw-e365/bankingreojan.png)

Cybersecurity researchers have discovered an updated version of an Android malware called **TgToxic** (aka ToxicPanda), indicating that the threat actors behind it are continuously making changes in response to public reporting.

"The modifications seen in the TgToxic payloads reflect the actors' ongoing surveillance of open source intelligence and demonstrate their commitment to enhancing the malware's capabilities to improve security measures and keep researchers at bay," Intel 471 [said](https://intel471.com/blog/android-trojan-tgtoxic-updates-its-capabilities) in a report published this week.

TgToxic was [first documented](https://thehackernews.com/2023/02/enigma-vector-and-tgtoxic-new-threats.html) by Trend Micro in early 2023, describing it as a banking trojan capable of stealing credentials and funds from crypto wallets as well as bank and finance apps. It has been detected in the wild since at least July 2022, mainly focusing on mobile users in Taiwan, Thailand, and Indonesia.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Then in November 2024, Italian online fraud prevention firm Cleafy [detailed](https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html) an updated variant with wide-ranging data-gathering features, while also expanding its operational scope to include Italy, Portugal, Hong Kong, Spain, and Peru. The malware is assessed to be the work of a Chinese-speaking threat actor.

Intel 471's latest analysis has found that the malware is distributed via dropper APK files likely via SMS messages or phishing websites. However, the exact delivery mechanism remains unknown.

Some of the notable improvements include improved emulator detection capabilities and updates to the command-and-control (C2) URL generation mechanism, underscoring ongoing efforts to sidestep analysis efforts.

"The malware conducts a thorough evaluation of the device's hardware and system capabilities to detect emulation," Intel 471 said. "The malware examines a set of device properties including brand, model, manufacturer and fingerprint values to identify discrepancies that are typical of emulated systems."

Another significant change is the shift from hard-coded C2 domains embedded within the malware's configuration to using forums such as the Atlassian community developer forum to create bogus profiles that include an encrypted string pointing to the actual C2 server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtCYaqTHpDVwTRddUKsMBnDssk6dfS6qBxvEhhdrbF5Gbv059qOtkJt2AjngmIwQsruL9t327c7KQILJPZI-yfS2JSdZRdG3jHCCcF7ZlrcznIzFNJxfWnjDN1-7i9I3_S14na0fDli67CWddUP5tf7DvwbHoy9vlCgTcBn4NLPthWuh6D7OOegPeXirCw/s790-rw-e365/flow-attack.png)

The TgToxic APK is designed to randomly select one of the community forum URLs provided in the configuration, which serves as a [dead drop resolver](https://thehackernews.com/2022/12/researchers-uncover-new-drokbk-malware.html) for the C2 domain.

The technique offers several advantages, foremost being that it makes it easier for threat actors to change C2 servers by simply updating the community user profile to point to the new C2 domain without having to issue any updates to the malware itself.

"This method considerably extends the operational lifespan of malware samples, keeping them functional as long as the user profiles on these forums remain active," Intel 471 said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Subsequent iterations of TgToxic discovered in December 2024 go a step further, relying on a domain generation algorithm (DGA) to create new domain names for use as C2 servers. This makes the malware more resilient to disruption efforts as the DGA can be used to create several domain names, allowing the attackers to switch to a new domain even if some are taken down.

"TgToxic stands out as a highly sophisticated Android banking trojan due to its advanced anti-analysis techniques, including obfuscation, payload encryption, and anti-emulation mechanisms that evade detection by security tools," Approov CEO Ted Miracco said in a statement.

"Its use of dynamic command-and-control (C2) strategies, such as domain generation algorithms (DGA), and its automation capabilities enable it to hijack user interfaces, steal credentials, and perform unauthorized transactions with stealth and resilience against countermeasures."

### Update

Following the publication of the story, a Google spokesperson shared the below statement with The Hacker News -

*Based on our current detection, no apps containing this malware are found on Google Play. Android users are automatically protected against known versions of this malware by* [*Google Play Protect*](https://support.google.com/googleplay/answer/2812853?hl=en)*, which is on by default on Android devices with Google Play Services. Google Play Protect can warn users or block apps known to exhibit malicious behavior, even when those apps come from sources outside of Play.*

*(The story was updated after publication to include a response from Google.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#lin...