---
title: Sharp Panda Using New Soul Framework Version to Target Southeast Asian Governments
url: https://thehackernews.com/2023/03/sharp-panda-using-new-soul-framework.html
source: The Hacker News
date: 2023-03-09
fetch_date: 2025-10-04T09:03:36.938257
---

# Sharp Panda Using New Soul Framework Version to Target Southeast Asian Governments

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

# [Sharp Panda Using New Soul Framework Version to Target Southeast Asian Governments](https://thehackernews.com/2023/03/sharp-panda-using-new-soul-framework.html)

**Mar 08, 2023**Ravie LakshmananAdvanced Persistent Threat

[![Sharp Panda Hackers](data:image/png;base64... "Sharp Panda Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgohm4q_lPJFXuTUSjYXa74IXswerV51V2qgq7gLxVJwPu8SIIZmsNgH1YrJEWzNP-Gb74jmiV4wCEGYeqQ7ztfvyBh3qV1TfHtr0ntqEQ-kGEjXNq8ifdJx1ljLJVaSrnWgB7v0iE6s5yQMt9G5r2cVzEqMJ5c6foodYS3TQRnRcM8nj9GmsCmDiUk/s790-rw-e365/chinese-hacker-panda.png)

High-profile government entities in Southeast Asia are the target of a cyber espionage campaign undertaken by a Chinese threat actor known as Sharp Panda since late last year.

The intrusions are characterized by the use of a new version of the Soul modular framework, marking a departure from the group's attack chains observed in 2021.

Israeli cybersecurity company Check Point [said](https://research.checkpoint.com/2023/pandas-with-a-soul-chinese-espionage-attacks-against-southeast-asian-government-entities/) the "long-running" activities have historically singled out countries such as Vietnam, Thailand, and Indonesia. Sharp Panda was [first documented](https://thehackernews.com/2021/06/experts-uncover-yet-another-chinese.html) by the firm in June 2021, describing it as a "highly-organized operation that placed significant effort into remaining under the radar."

The use of the Soul backdoor in real-world attacks was first [detailed](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-campaign-south-east-asia) by Broadcom's Symantec in October 2021 in connection to an unattributed espionage operation targeting defense, healthcare, and ICT sectors in Southeast Asia.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The implant's origins, according to [research](https://www.fortinet.com/blog/threat-research/unraveling-the-evolution-of-the-soul-searcher-malware) published by Fortinet FortiGuard Labs in February 2022, date as far back as October 2017, with the malware repurposing code from Gh0st RAT and other publicly available tools.

The attack chain documented by Check Point begins with a spear-phishing email containing a lure document that leverages the [Royal Road](https://www.domaintools.com/resources/blog/an-undersea-royal-road-exploring-malicious-documents-and-associated-malware/) Rich Text Format (RTF) weaponizer to drop a downloader by exploiting one of several vulnerabilities in the Microsoft Equation Editor.

[![Soul Hacker Framework](data:image/png;base64... "Soul Hacker Framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmQQzFYoGZKwSA8Dqaj2EosZj8rPTFyHVX9ZFR0bY0FeOwp1D0CGtXdrc2lFcNjyHN66tDrsghq1FWil349Q-eU1HOsS35pCT92-QCKIc5nGWaWShHM4XqKbL2XThZ8AKW-ppQtlYi-QuU7LutNEB1yHPD4_efvgJjEO9dtxY8pjDDAeOBnldqp1GP/s790-rw-e365/malware.png)

The downloader, in turn, is designed to retrieve a loader known as SoulSearcher from a geofenced command-and-control (C&C) server that only responds to requests originating from IP addresses corresponding to the targeted countries.

The loader is then responsible for downloading, decrypting, and executing the Soul backdoor and its other components, thereby enabling the adversary to harvest a wide range of information.

"The Soul main module is responsible for communicating with the C&C server and its primary purpose is to receive and load in memory additional modules," Check Point said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Interestingly, the backdoor configuration contains a 'radio silence'-like feature, where the actors can specify specific hours in a week when the backdoor is not allowed to communicate with the C&C server."

The findings are yet another indication of the tool sharing that's prevalent among Chinese advanced persistent threat (APT) groups to facilitate intelligence gathering.

"While the Soul framework has been in use since at least 2017, the threat actors behind it have been constantly updating and refining its architecture and capabilities," the company said.

It further noted that the campaign is likely "staged by advanced Chinese-backed threat actors, whose other tools, capabilities and position within the broader network of espionage activities are yet to be explored."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-...