---
title: Google Exposes Vishing Group UNC6040 Targeting Salesforce with Fake Data Loader App
url: https://thehackernews.com/2025/06/google-exposes-vishing-group-unc6040.html
source: The Hacker News
date: 2025-06-05
fetch_date: 2025-10-06T22:56:05.440485
---

# Google Exposes Vishing Group UNC6040 Targeting Salesforce with Fake Data Loader App

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

# [Google Exposes Vishing Group UNC6040 Targeting Salesforce with Fake Data Loader App](https://thehackernews.com/2025/06/google-exposes-vishing-group-unc6040.html)

**Jun 04, 2025**Ravie Lakshmanan Threat Intelligence / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0oL5c_oWT1LeMbEUw8SldxA0SH9eLyEiAnAyHsDf04Zj4BF0MtaSTREfGyxXBYcnhVh-8UGSbv7oDZ6bF5YK9ML13rMqWaFKiUzM1VaOH-tgD92MCcTNVodoLr-alA2rUl8b3-xxESNZYwrxO1Le-scp9WzYigWz0oXoupSX4s12oragLQK5BzW2lP2UR/s790-rw-e365/sales.jpg)

Google has disclosed details of a financially motivated threat cluster that it said "specializes" in voice phishing (aka [vishing](https://www.guidepointsecurity.com/blog/this-caller-does-not-exist-using-ai-to-conduct-vishing-attacks/)) campaigns designed to breach organizations' Salesforce instances for large-scale data theft and subsequent extortion.

The tech giant's threat intelligence team is tracking the activity under the moniker **UNC6040**, which it said exhibits characteristics that align with threat groups with ties to an online cybercrime collective known as [The Com](https://thehackernews.com/2025/05/dragonforce-exploits-simplehelp-flaws.html).

"Over the past several months, UNC6040 has demonstrated repeated success in breaching networks by having its operators impersonate IT support personnel in convincing telephone-based social engineering engagements," the company [said](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion) in a report shared with The Hacker News.

This approach, Google's Threat Intelligence Group (GTIG) added, has had the benefit of tricking English-speaking employees into performing actions that give the threat actors access or lead to the sharing of valuable information such as credentials, which are then used to facilitate data theft.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

GTIG told The Hacker News that a limited number of organizations were affected as part of the active campaign, with the "opportunistic" attacks targeting approximately 20 entities across hospitality, retail, education, and various other sectors across the Americas and Europe.

A noteworthy aspect of UNC6040's activities involves the use of a modified version of Salesforce's [Data Loader](https://developer.salesforce.com/tools/data-loader) that victims are deceived into authorizing so as to connect to the organization's Salesforce portal during the vishing attack. Data Loader is an application used to import, export, and update data in bulk within the Salesforce platform.

Specifically, the attackers guide the target to visit Salesforce's connected app setup page and approve the modified version of the Data Loader app that carries a different name or branding (e.g., "My Ticket Portal") from its legitimate counterpart. This action grants them unauthorized access to the Salesforce customer environments and exfiltrate data.

Beyond data loss, the attacks serve as a stepping stone for UNC6040 to move laterally through the victim's network, and then access and harvest information from other platforms such as Okta, Workplace, and Microsoft 365.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9joDAKngnzkaCNevwynx2DCgBnUnfKySOwcvXVKTmAG7bxNe_hbuxMjMzTbZTA6UUlyznVv6PEv4avjsxBw19CnB4ooB0cSE0x4SqgQMDCGxjyQfgf1R7K1pIO97YGwQ6snf9fgVQvaS9mU4GMu_ZNGvbtuQibuNhpma6PbtWp6mhTagIzGQPNvylBieR/s790-rw-e365/path.png)

Select incidents have also involved extortion activities, but only "several months" after the initial intrusions were observed, indicating an attempt to monetize and profit off the stolen data presumably in partnership with a second threat actor.

"During these extortion attempts, the actor has claimed affiliation with the well-known hacking group ShinyHunters, likely as a method to increase pressure on their victims," Google said.

UNC6040's overlaps with groups linked to The Com stem from the [targeting of Okta credentials](https://thehackernews.com/2023/09/okta-warns-of-social-engineering.html) and the use of social engineering via IT support, a tactic that has been embraced by [Scattered Spider](https://thehackernews.com/2024/07/17-year-old-linked-to-scattered-spider.html), another financially motivated threat actor that's part of the loose-knit organized collective.

Google-owned Mandiant, in a technical overview of vishing and the social engineering attacks, pointed out the distinct objectives of Scattered Spider and UNC6040 – i.e., the former's focus on account takeover for broad network access versus UNC6040's targeted theft of Salesforce data – underscore the "diverse risks" stemming from vishing.

The company said the threat actors conducting vishing campaigns also weaponize automated phone systems that have pre-recorded messages and interactive menus to glean more information about the targets they are looking to penetrate.

These phone services enable an attacker to "anonymously" identify common issues faced by end users, names of internal applications, additional phone numbers for specific support teams, and, sometimes, alerts about company-wide technical issues.

"Effective social engineering campaigns are built upon extensive reconnaissance," Nick Guttilla from the Mandiant Incident Response team [said](https://cloud.google.com/blog/topics/threat-intelligence/technical-analysis-vishing-threats/?e=48754805). "Prevalence of in-person social interactions has diminished and remote IT structures, such as an outsourced service desk, has normalized employees' engagement with external or less familiar personnel. As a result, threat actors continue to use social engineering tactics"

The vishing campaign hasn't gone unnoticed by Salesforce, which, in March 2025, warned of threat actors using social engineering tactics to impersonate IT support personnel over the phone and trick its customers' employees into giving away their credentials or approving the modif...