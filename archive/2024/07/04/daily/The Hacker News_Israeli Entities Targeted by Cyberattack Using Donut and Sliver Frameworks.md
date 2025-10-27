---
title: Israeli Entities Targeted by Cyberattack Using Donut and Sliver Frameworks
url: https://thehackernews.com/2024/07/israeli-entities-targeted-by.html
source: The Hacker News
date: 2024-07-04
fetch_date: 2025-10-06T17:48:34.370215
---

# Israeli Entities Targeted by Cyberattack Using Donut and Sliver Frameworks

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

# [Israeli Entities Targeted by Cyberattack Using Donut and Sliver Frameworks](https://thehackernews.com/2024/07/israeli-entities-targeted-by.html)

**Jul 03, 2024**Ravie LakshmananCyber Attack / Malware

[![Donut and Sliver Frameworks](data:image/png;base64... "Donut and Sliver Frameworks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX4pGK_9BbTdRoNzwTatgUjVAM8GTxv97j3N9KsrZY_7L3IAGNp4jGx2jgCodT9oPeI1f3u4N3QU64qUrnPAxj4b9h_Lu1rTU_D7lRZp_lprWC934Hgl0BJDJQlGK7O-nUFgVdWTmyzvrY5shyphenhyphennvrbukWnn4rZ0KLRHOXm2VmJHHc859px9CnvFdLmGu0z/s790-rw-e365/cyberattack.png)

Cybersecurity researchers have discovered an attack campaign that targets various Israeli entities with publicly-available frameworks like Donut and Sliver.

The campaign, believed to be highly targeted in nature, "leverage target-specific infrastructure and custom WordPress websites as a payload delivery mechanism, but affect a variety of entities across unrelated verticals, and rely on well-known open-source malware," HarfangLab [said](https://harfanglab.io/en/insidethelab/supposed-grasshopper-operators-impersonate-israeli-gov-private-companies-deploy-open-source-malware/) in a report last week.

The French company is tracking the activity under the name Supposed Grasshopper. It's a reference to an attacker-controlled server ("auth.economy-gov-il[.]com/SUPPOSED\_GRASSHOPPER.bin"), to which a first-stage downloader connects to.

This downloader, written in Nim, is rudimentary and is tasked with downloading the second-stage malware from the staging server. It's delivered by means of a virtual hard disk (VHD) file that's suspected to be propagated via custom WordPress sites as part of a drive-by download scheme.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The second-stage payload retrieved from the server is [Donut](https://github.com/TheWover/donut), a shellcode generation framework, which serves as a conduit for deploying an open-source [Cobalt Strike](https://unit42.paloaltonetworks.com/attackers-exploit-public-cobalt-strike-profiles/) alternative called [Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html).

"The operators also put some notable efforts in acquiring dedicated infrastructure and deploying a realistic WordPress website to deliver payloads," the researchers said. "Overall, this campaign feels like it could realistically be the work of a small team."

[![Donut and Sliver Frameworks](data:image/png;base64... "Donut and Sliver Frameworks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaBXjvlv8N3KpfcZEAmeE4gMaV9a8Wm-HQsCZnmMZu-xSWBYRKBe1tUjz2zdtp3ZdG7UutvPWiumkQ5lzhZfZCHEMgr4XZ9JFEvfmClnkACIsHGqH-JxvtZIfrqv9lgiw0HTJnriLR2FF6dLm39Y_F5ICRhfeA3nGdnNY5_7YpYrT0iov-MZ5-GUz_01iu/s790-rw-e365/signal-2024-06-20-053425-002.png)

The end goal of the campaign is currently unknown, although HarfangLab theorized that it could also be associated with a legitimate penetration testing operation, a possibility that raises its own set of questions surrounding transparency and the need for impersonating Israeli government agencies.

The disclosure comes as the SonicWall Capture Labs threat research team detailed an infection chain that employs booby-trapped Excel spreadsheets as a starting point to drop a trojan known as Orcinius.

"This is a multi-stage trojan that is using Dropbox and Google Docs to download second-stage payloads and stay updated," the company [said](https://blog.sonicwall.com/en-us/2024/06/new-orcinius-trojan-uses-vba-stomping-to-mask-infection/). "It contains an obfuscated VBA macro that hooks into Windows to monitor running windows and keystrokes and creates persistence using registry keys."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Israel](https://thehackernews.com/search/label/Israel)[Malware](https://thehackernews.com/search/label/Malware)[Penetration Testing](https://thehackernews.com/search/label/Penetration%20Testing)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP ...