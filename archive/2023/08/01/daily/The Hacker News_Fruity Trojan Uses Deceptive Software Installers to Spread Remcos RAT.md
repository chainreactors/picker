---
title: Fruity Trojan Uses Deceptive Software Installers to Spread Remcos RAT
url: https://thehackernews.com/2023/07/fruity-trojan-uses-deceptive-software.html
source: The Hacker News
date: 2023-08-01
fetch_date: 2025-10-06T17:04:45.830780
---

# Fruity Trojan Uses Deceptive Software Installers to Spread Remcos RAT

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

# [Fruity Trojan Uses Deceptive Software Installers to Spread Remcos RAT](https://thehackernews.com/2023/07/fruity-trojan-uses-deceptive-software.html)

**Jul 31, 2023**Ravie LakshmananMalware / Cyber Threat

[![Remcos RAT](data:image/png;base64... "Remcos RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS9df08MM3ZFQgUocF_XT4BLydgJh2wiA7aK9QE61-2HsGaDT0Z8cf4pnv7ie5taHHdx23ms27EZj4FYSHwDKqS8VV9TtDVcVtf9qBXZFpZ4gzxI7TgnkPHOrWh0WDe8BBIMaJJIfvoVsM7u76k4wF-6oQA9B2J6qdGWZbSYO-U1zFRd4d4XMZ6Jg6dh9y/s790-rw-e365/hack.jpg)

Threat actors are creating fake websites hosting trojanized software installers to trick unsuspecting users into downloading a downloader malware called Fruity with the goal of installing remote trojans tools like Remcos RAT.

"Among the software in question are various instruments for fine-tuning CPUs, graphic cards, and BIOS; PC hardware-monitoring tools; and some other apps," cybersecurity vendor Doctor Web [said](https://news.drweb.com/show/?i=14728&lng=en) in an analysis.

"Such installers are used as a decoy and contain not only the software potential victims are interested in, but also the trojan itself with all its components."

The exact initial access vector used in the campaign is unclear but it could potentially range from phishing to drive-by downloads to malicious ads. Users who land on the fake site are prompted to download a ZIP installer package.

The installer, besides activating the standard installation process, stealthily drops the Fruity trojan, a Python-based malware that unpacks an MP3 file ("Idea.mp3") to load an image file ("Fruit.png") to activate the multi-stage infection.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This image file uses the steganography method to hide two executables (.dll libraries) and the shellcode for the next-stage initialization inside it," Doctor Web said.

Fruity is also designed to bypass antivirus detection on the compromised host and ultimately launch the Remcos RAT payload using a technique called [process doppelgänging](https://attack.mitre.org/techniques/T1055/013/).

[![Fruity Trojan](data:image/png;base64... "Fruity Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRr5GRjd4kSdHHBLeqkb4eAite-UyyEgmItnxeuUYgor_pyd8p8MVMeR883nr_iPNPj1LlTC-BYWbfl3iYnEwCta1ubcfqrGt6SL3ChcbPcsDRQpLV8t2UBNswLlb7iLFe0ffWe26l1PnO89sujli18B5z1RlOHGvK8uf5Hj2ELXx_csB6zckTh2bLVcMg/s790-rw-e365/python.jpg)

That said, the attack sequence could be exploited to distribute all kinds of malware, which makes it imperative that users stick to downloading software only from trustworthy sources.

The development comes as Bitdfender [disclosed](https://www.bitdefender.com/blog/hotforsecurity/bitdefender-labs-warns-of-agent-tesla-phishing-campaign/) details of a malspam campaign delivering the Agent Tesla malware to harvest sensitive data from compromised endpoints.

It also follows a surge in malvertising operations that have targeted customers and businesses with tainted software boosted via ads on search engines.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes a new wave of attacks dubbed [Nitrogen](https://thehackernews.com/2023/07/new-malvertising-campaign-distributing.html) in which fraudulent ISO archives are distributed using bogus ads that impersonate download pages for applications such as AnyDesk, WinSCP, Cisco AnyConnect, Slack, and TreeSize.

"This malvertising campaign leads to the propagation of the infection after initial exposure," Bitdefender researchers Victor Vrabie and Alexandru Maximciuc [said](https://www.bitdefender.com/blog/labs/abusing-the-ad-network-threat-actors-now-hacking-into-companies-via-search/).

"For as long as they dwell in the victim's network, the attackers' primary goal is to obtain credentials, set up persistence on important systems and exfiltrate data, with extortion as the end goal."

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

[BIOS](https://thehackernews.com/search/label/BIOS)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-f...