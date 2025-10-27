---
title: Vietnamese Hackers Use PXA Stealer, Hit 4,000 IPs and Steal 200,000 Passwords Globally
url: https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html
source: The Hacker News
date: 2025-08-05
fetch_date: 2025-10-07T00:51:12.627740
---

# Vietnamese Hackers Use PXA Stealer, Hit 4,000 IPs and Steal 200,000 Passwords Globally

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

# [Vietnamese Hackers Use PXA Stealer, Hit 4,000 IPs and Steal 200,000 Passwords Globally](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html)

**Aug 04, 2025**Ravie LakshmananMalware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg19Q0x1iwBfZhRlu8WnfWaMBFmqaXBtlkCatgyGCOVj68dD8DmKLfmIbKcEX7ZDtuqoSktRrgoL2j-HIL7iogsygeLXMuq05sE9SDiqWr71HX_wKHbGwnqCX6f6yjSWD7PzzOH_A1UKVvW6Q_WOH0PkdYW-5tSLY1i1ggAxRDi6AXTG23VkaKfvpLjYA_q/s790-rw-e365/passwords.jpg)

Cybersecurity researchers are calling attention to a new wave of campaigns distributing a Python-based information stealer called PXA Stealer.

The malicious activity has been assessed to be the work of Vietnamese-speaking cybercriminals who monetize the stolen data through a subscription-based underground ecosystem that automates the resale and reuse via Telegram APIs, according to a joint report published by Beazley Security and SentinelOne and shared with The Hacker News.

"This discovery showcases a leap in tradecraft, incorporating more nuanced anti-analysis techniques, non-malicious decoy content, and a hardened command-and-control pipeline that frustrates triage and attempts to delay detection," security researchers Jim Walter, Alex Delamotte, Francisco Donoso, Sam Mayers, Tell Hause, and Bobby Venal [said](https://www.sentinelone.com/labs/ghost-in-the-zip-new-pxa-stealer-and-its-telegram-powered-ecosystem/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The campaigns have infected over 4,000 unique IP addresses spanning 62 countries, including South Korea, the United States, the Netherlands, Hungary, and Austria. Data captured via the stealer includes more than 200,000 unique passwords, hundreds of credit card records, and more than 4 million harvested browser cookies.

PXA Stealer was [first documented](https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html) by Cisco Talos in November 2024, attributing it to attacks targeting government and education entities in Europe and Asia. It's capable of harvesting passwords, browser autofill data, information from cryptocurrency wallets and financial institutions.

Data stolen by the malware using Telegram as an exfiltration channel is fed into criminal platforms like Sherlock, a purveyor of stealer logs, from where downstream threat actors can purchase the information to engage in cryptocurrency theft or infiltrate organizations for follow-on purposes, fueling a cybercriminal ecosystem that runs at scale.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidM1Jass_odVBIfg4pa3LX_gUeagPfQA1_ljruNazZayH25zQ9F1-2gwATU7ssaanjmRT_2f3i7r5_WoaW67nfYu4LLANymx23rrp-ZmoGyj99AWNCBOM0n1-GY8u1hnKugGnhgbi-kzaG08F06TmHRmF2roaHqpDazyLx6OeEsC8q24C3iVjyPtLhMnUa/s2600/bs.jpg)

Campaigns distributing the malware in 2025 have witnessed a steady tactical evolution, with the threat actors employing DLL side-loading techniques and elaborate staging layers in an effort to fly under the radar.

The malicious DLL takes care of conducting the rest of the steps in the infection sequence, ultimately paving the way for the deployment of the stealer, but not before taking steps to display a decoy document, such as a copyright infringement notice, to the victim.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The stealer is an updated version boasting capabilities to extract cookies from Chromium-based web browsers by injecting a DLL into running instances with an aim to defeat [app-bound encryption safeguards](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html). It also plunders data from VPN clients, cloud command-line interface (CLI) utilities, connected fileshares, and applications like Discord.

"PXA Stealer uses the BotIDs (stored as TOKEN\_BOT) to establish the link between the main bot and the various ChatID (stored as CHAT\_ID)," the researchers said. "The ChatIDs are Telegram channels with various properties, but they primarily serve to host exfiltrated data and provide updates and notifications to the operators."

"This threat has since matured into a highly evasive, multi-stage operation driven by Vietnamese-speaking actors with apparent ties to an organized cybercriminal Telegram-based marketplace that sells stolen victim data."

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

[browser security](https://thehackernews.com/search/label/browser%20security)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DLL side-loading](https://thehackernews.com/search/label/DLL%20side-loading)[Malware](https://thehackernews.com/search/label/Malware)[Python](https://thehackernews.com/search/label/Python)[SentinelOne](https://thehackernews.com/search/label/SentinelOne)[Telegram](https://thehackernews.com/search/label/Telegram)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https...