---
title: Why Secure Data Movement Is the Zero Trust Bottleneck Nobody Talks About
url: https://thehackernews.com/2026/04/why-secure-data-movement-is-zero-trust.html
source: The Hacker News
date: 2026-04-28
fetch_date: 2026-04-29T05:13:05.464312
---

# Why Secure Data Movement Is the Zero Trust Bottleneck Nobody Talks About

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Why Secure Data Movement Is the Zero Trust Bottleneck Nobody Talks About](https://thehackernews.com/2026/04/why-secure-data-movement-is-zero-trust.html)

**The Hacker News**Apr 28, 2026Operational Technology / Data Integrity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrVD0Q_dTvO3tooHYWKp7i_lkLd6h30GSv_DDv4jIb_KZDY5heV39R01GFN6MWEq1JsilHFrd7EtDOBkmlkvXYAb7-w51A1SDN3AAiEAbuq7ZnNREakyHouZPVBMNhk_HnEOK8D7H5m51A2zcUvAvDjmPnrrzeZI_nQHFao1QbljV4ortyzuqbXsNR35c/s1700-e365/everfox.jpg)

Every security program is betting on the same assumption: once a system is connected, the problem is solved. Open a ticket, stand up a gateway, push the data through. Done.

That assumption is wrong. It is also a major reason Zero Trust programs stall.

New research my team just published puts numbers on it. The **[Cyber360: Defending the Digital Battlespace](https://info.everfox.com/cyber360-defending-the-digital-battlespace?_gl=1*1yn2vjg*_gcl_au*NDczODQ5ODExLjE3NzEyNDQ2MzI.*_ga*MTg0NTIzODA0MS4xNzQ3NzM5NDIx*_ga_HD8LC7WBBC*czE3NzcxNDkzMTQkbzE0NiRnMCR0MTc3NzE0OTMxNCRqNjAkbDAkaDYwMzY2NDExMg..*_ga_VDGYSGRN6H*czE3NzcxNDkzMTQkbzE0NSRnMCR0MTc3NzE0OTMxNCRqNjAkbDAkaDk5NTU3NzU4Mg..)** report, based on a survey of 500 security leaders in government, defense, and critical services across the U.S. and UK, found that 84% of government IT security leaders agree that sharing sensitive data across networks heightens their cyber risk. More than half - 53% - still rely on manual processes to move that data between systems. In 2026. With AI accelerating the pace of operations on both sides.

That is the Zero Trust gap nobody talks about. Not identity. Not endpoints. The movement of data itself.

## **The Threat Volume Is Rising Faster Than the Controls**

Cyber360 recorded an average of 137 attempted or successful cyberattacks per week against national security organizations in 2025, up from 127 the previous year. U.S. agencies saw the weekly rate surge 25%. Verizon's 2025 Data Breach Investigations Report tracks a similar trajectory on the enterprise side: third-party involvement in breaches doubled year over year, reaching 30% of all incidents. IBM's 2025 Cost of a Data Breach Report put the average cost of a breach spanning multiple environments at $5.05 million, roughly $1 million more than on-premises-only incidents.

The boundaries between IT and OT, between tenants, between partner and internal environments are where the money and the dwell time sit right now.

## **Connectivity Is Not the Same as Secure Data Movement**

The moment data crosses a boundary, whether between an OT network and the enterprise SOC, between a partner tenant and your cloud, or between classified and unclassified, it stops being a routing problem and becomes a trust problem. It has to be validated, filtered, and policy-controlled before anything downstream can act on it. That is where modern architectures slow down.

The Cyber360 data is blunt about where the pain is concentrated:

* 78% of respondents cited outdated infrastructure as a primary source of cyber vulnerability, specifically pointing to analog systems and manual processes as weak links.
* 49% named ensuring data integrity and preventing tampering in transit as their single biggest challenge when transferring information across classified or coalition networks.
* 45% flagged managing identity and authentication across multiple domains as their biggest access challenge.

Integrity in transit, identity across domains, and manual processes are still in the loop. That is a working description of the attack surface adversaries have been exploiting for three years.

The enterprise data tells the same story in a different language. Dragos' 2025 OT Cybersecurity Report found that 75% of OT attacks now originate as IT breaches, with roughly 70% of OT systems expected to connect to IT networks within the next year. The traditional IT/OT air gap is effectively gone. The managed file transfer breaches drive the point home. Cl0p's exploitation of MOVEit compromised more than 2,700 organizations and exposed the personal data of roughly 93 million individuals. The same playbook worked against GoAnywhere and Cleo. Every one of those incidents was, at its core, an attack on the pipes that move data between trust boundaries.

## **The Speed-vs-Security Trade-off Is a Myth**

There is a persistent belief that you can either move data fast or move it securely. Pick one.

In practice, most teams pick security and accept the delay. That works when decision cycles are measured in minutes. It does not work when they are measured in seconds, and it collapses completely when they are measured in milliseconds.

AI is accelerating on both sides. Detection and response pipelines are moving toward autonomous action. They do not wait for a gateway to finish inspecting a file. When 53% of national security organizations are still moving data manually, the delta between AI-speed demand and analog-speed supply becomes the attack surface. An AI model, whether it is running fraud detection, threat triage, or targeting analysis, is only as good as the data reaching it. When that data cannot move freely, or cannot be trusted when it arrives, the model runs on stale or partial context. The bottleneck is not the intelligence layer. It is the plumbing underneath.

## **The Role of Cross Domain Technologies**

This is where cross-domain technologies earn their place, and not as a compliance checkbox.

Done properly, they remove the forced choice between speed and security. They enforce trust at the boundary instead of after it. They let systems operate as a coordinated whole, instead of as a set of isolated islands stapled together with point-to-point integrations that attackers have now demonstrated they can dismantle at scale.

The Cyber360 research points toward a specific architectural answer: a layered model combining Zero Trust, Data Centric Security, and Cross Domain Solutions. No single framework closes the gap alone. Zero Trust governs who and what. Data-centric security governs the data itself, wherever it goes. Cross-domain solutions govern the movement between environments. Together, they let secure data sharing happen at near-real-time speed across classified, coalition, and operational bounda...