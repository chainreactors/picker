---
title: Russian ELECTRUM Tied to December 2025 Cyber Attack on Polish Power Grid
url: https://thehackernews.com/2026/01/russian-electrum-tied-to-december-2025.html
source: The Hacker News
date: 2026-01-28
fetch_date: 2026-01-29T04:05:59.477629
---

# Russian ELECTRUM Tied to December 2025 Cyber Attack on Polish Power Grid

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

# [Russian ELECTRUM Tied to December 2025 Cyber Attack on Polish Power Grid](https://thehackernews.com/2026/01/russian-electrum-tied-to-december-2025.html)

**Ravie Lakshmanan**Jan 28, 2026Critical Infrastructure / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpzZ7e4dYy-hpTfbR7szq9J8RcMD40YfqgkKsvCTqBy-LIR2HtA3D4gY0i_-yiitA72t97lJlC4cW3klbAsJB6BBxxfOXDjhf68Z9RNF2GDYwWxPkdzSYTIcgQZzXg_0hCSqYOPI4nI8Wq3NHj5DrgwQ0RpdEZGJ1hMteDuOBNDxn-sXuzj57K9K-QKhz0/s1700-e365/powergrid.jpg)

The "coordinated" cyber attack targeting multiple sites across the [Polish power grid](https://thehackernews.com/2026/01/new-dynowiper-malware-used-in-attempted.html) has been attributed with medium confidence to a Russian state-sponsored hacking crew known as [ELECTRUM](https://www.dragos.com/blog/2015-ukraine-power-grid-attack-lessons-in-defense).

Operational technology (OT) cybersecurity company Dragos, in a new intelligence brief published Tuesday, described the late December 2025 activity as the first major cyber attack targeting distributed energy resources (DERs).

"The attack affected communication and control systems at combined heat and power (CHP) facilities and systems managing the dispatch of renewable energy systems from wind and solar sites," Dragos [said](https://5943619.hs-sites.com/hubfs/Reports/dragos-2025-poland-attack-report.pdf). "While the attack did not result in power outages, adversaries gained access to operational technology systems critical to grid operations and disabled key equipment beyond repair at the site."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

It's worth pointing out that [ELECTRUM](https://www.dragos.com/threat/electrum) and [KAMACITE](https://www.dragos.com/threat/kamacite) share overlaps with a cluster referred to as [Sandworm](https://thehackernews.com/2023/11/russian-hackers-sandworm-cause-power.html) (aka APT44 and Seashell Blizzard). KAMACITE focuses on establishing and maintaining initial access to targeted organizations using spear-phishing, stolen credentials, and exploitation of exposed services.

Beyond initial access, the threat actor performs reconnaissance and persistence activities over extended periods of time as part of efforts to burrow deep into target OT environments and keep a low profile, signaling a careful preparatory phase that precedes actions executed by ELECTRUM targeting the industrial control systems.

"Following access enablement, ELECTRUM conducts operations that bridge IT and OT environments, deploying tooling within operational networks, and performs ICS-specific actions that manipulate control systems or disrupt physical processes," Dragos [said](https://5943619.hs-sites.com/hubfs/Reports/electrum-kamacite-ten-years-adversary-tradecraft-intel-report-01-26.pdf). "These actions have included both manual interactions with operator interfaces and the deployment of purpose-built ICS malware, depending on the operational requirements and objectives."

Put differently, the two clusters have clear separation of roles and responsibilities, enabling flexibility in execution and facilitating sustained OT-focused intrusions when conditions are favourable. As recently as July 2025, KAMACITE is said to have engaged in scanning activity against industrial devices located in the U.S.

Although no follow-on OT disruptions have been publicly reported to date, this highlights an operational model that is not geographically constrained and facilitates early-stage access identification and positioning.

"KAMACITE's access-oriented operations create the conditions under which OT impact becomes possible, while ELECTRUM applies execution tradecraft when timing, access, and risk tolerance align," it explained. "This division of labor enables flexibility in execution and allows OT impact to remain an option, even when it is not immediately exercised. This extends risk beyond discrete incidents and into prolonged periods of latent exposure."

Dragos said the Poland attack targeted systems that facilitate communication and control between grid operators and DER assets, including assets that enable network connectivity, allowing the adversary to successfully disrupt operations at about 30 distributed generation sites.

The threat actors are assessed to have breached Remote Terminal Units (RTUs) and communication infrastructure at the affected sites using exposed network devices and exploited vulnerabilities as initial access vectors. The findings indicate that the attackers possess a deep understanding of electrical grid infrastructure, allowing them to disable communications equipment, including some OT devices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

That said, the full scope of the malicious actions undertaken by ELECTRUM is unknown, with Dragos noting that it's unclear if the threat actor attempted to issue operational commands to this equipment or focused solely on disabling communications.

The Poland attack is also assessed to be more opportunistic and rushed than a precisely planned operation, allowing the hackers to take advantage of the unauthorized access to inflict as much damage as possible by wiping Windows-based devices to impede recovery, resetting configurations, or attempting to permanently brick equipment. The majority of the equipment is targeted at grid safety and stability monitoring, per Dragos.

"This incident demonstrates that adversaries with OT-specific capabilities are actively targeting systems that monitor and control distributed generation," it added. "The disabling of certain OT or industrial control system (ICS) equipment beyond repair at the site moved what could have been seen as a pre-positioning attempt by the adversary into an attack."

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
[**Share on Twitter](#l...