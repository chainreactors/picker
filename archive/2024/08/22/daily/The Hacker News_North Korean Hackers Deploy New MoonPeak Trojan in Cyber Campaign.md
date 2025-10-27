---
title: North Korean Hackers Deploy New MoonPeak Trojan in Cyber Campaign
url: https://thehackernews.com/2024/08/north-korean-hackers-deploy-new.html
source: The Hacker News
date: 2024-08-22
fetch_date: 2025-10-06T18:06:15.415295
---

# North Korean Hackers Deploy New MoonPeak Trojan in Cyber Campaign

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

# [North Korean Hackers Deploy New MoonPeak Trojan in Cyber Campaign](https://thehackernews.com/2024/08/north-korean-hackers-deploy-new.html)

**Aug 21, 2024**Ravie LakshmananCyber Espionage / Malware

[![Cyber Campaign](data:image/png;base64... "Cyber Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6O5VVJRO_ykPp_XGDmggfq6ceilNzvPj8QVMLu-t7xb311-CrWgBWS7xat89vPUn9nYqSNx0mTgcE0jfmVdZAYQvdJtjXhgJLWPohjizdnHL7vHitCnZpcUz6VRueiLlvo9UXbKMGuotO_ojEyo9_nCaU1L_D8QQJDLJxVHW9NN-7MSWWhtbdkrt98Aga/s790-rw-e365/northkorean.png)

A new remote access trojan called **MoonPeak** has been discovered as being used by a state-sponsored North Korean threat activity cluster as part of a new campaign.

Cisco Talos attributed the malicious cyber campaign to a hacking group it tracks as UAT-5394, which it said exhibits some level of tactical overlaps with a known nation-state actor codenamed [Kimsuky](https://thehackernews.com/2024/08/university-professors-targeted-by-north.html).

MoonPeak, under active development by the threat actor, is a variant of the open-source [Xeno RAT](https://thehackernews.com/2024/02/open-source-xeno-rat-trojan-emerges-as.html) malware, which was [previously deployed](https://asec.ahnlab.com/en/74034/) as part of phishing attacks that were designed to retrieve the payload from actor-controlled cloud services like Dropbox, Google Drive, and Microsoft OneDrive.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the key features of Xeno RAT include the ability to load additional plugins, launch and terminate processes, and communicate with a command-and-control (C2) server.

Talos said the commonalities between the two intrusion sets either indicate UAT-5394 is actually Kimsuky (or its sub-group) or it's another hacking crew within the North Korean cyber apparatus that borrows its toolbox from Kimsuky.

Key to realizing the campaign is the use of new infrastructure, including C2 servers, payload-hosting sites, and test virtual machines, that have been created to spawn new iterations of MoonPeak.

"The C2 server hosts malicious artifacts for download, which is then used to access and set up new infrastructure to support this campaign," Talos researchers Asheer Malhotra, Guilherme Venere, and Vitor Ventura [said](https://blog.talosintelligence.com/moonpeak-malware-infrastructure-north-korea/) in a Wednesday analysis.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMaxviqLz3JIcbCOaxamHdIsU8ovwfGcdpVV2Hxzw9lRidZx2XYyGZ8sooZvX5Z6mcb1lcZYbmDqZ4xDzaOGtAl3QfT7L8MotaLyZ6eyfs7mwmKQAJiS8uh-k1rdIVVOdwsw9oaC3p8fzvg8wG9KCnqtkzg4txAh5jgUmThZmgx6RdvgjJ7-PXWxhNY0jH/s790-rw-e365/talos.png)

"In multiple instances, we also observed the threat actor access existing servers to update their payloads and retrieve logs and information collected from MoonPeak infections."

The shift is seen as part of a broader pivot from using legitimate cloud storage providers to setting up their own servers. That said, the targets of the campaign are currently not known.

An important aspect to note here is that "the constant evolution of MoonPeak runs hand-in-hand with new infrastructure set up by the threat actors" and that each new version of the malware introduces more obfuscation techniques to thwart analysis and changes to the overall communication mechanism to prevent unauthorized connections.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Simply put, the threat actors ensured that specific variants of MoonPeak only work with specific variants of the C2 server," the researchers pointed out.

"The timelines of the consistent adoption of new malware and its evolution such as in the case of MoonPeak highlights that UAT-5394 continues to add and enhance more tooling into their arsenal. The rapid pace of establishing new supporting infrastructure by UAT-5394 indicates that the group is aiming to rapidly proliferate this campaign and set up more drop points and C2 servers."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Malware](https://thehackernews.com/search/label/Malware)[North Korea](https://thehackernews.com/search/label/North%20Korea)[Phishing](https://thehackernews.com/search/label/Phishing)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[State-Sponsored](https://thehackernews.com/search/label/State-Sponsored)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Ente...