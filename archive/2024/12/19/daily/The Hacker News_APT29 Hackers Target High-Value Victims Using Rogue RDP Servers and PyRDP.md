---
title: APT29 Hackers Target High-Value Victims Using Rogue RDP Servers and PyRDP
url: https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html
source: The Hacker News
date: 2024-12-19
fetch_date: 2025-10-06T20:00:45.501072
---

# APT29 Hackers Target High-Value Victims Using Rogue RDP Servers and PyRDP

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

# [APT29 Hackers Target High-Value Victims Using Rogue RDP Servers and PyRDP](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html)

**Dec 18, 2024**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyW25hMDzDaduXghIqBnOlnsbINi4FctEWHUFSfnnRFjOv6NYXNsz3UzCGm-IXtOHTsw5NkF-fxVTz1QlZokbmDseeAhyh3tD5v4A_HAxFK3iOifs3zl9xa8qZVz3VCapHCe4uJaqVtzUHCbPLVCKElwyCUV7sMl3qeWbiCiRwu2KLi5jISzDo4amlnRm-/s790-rw-e365/rdp.png)

The Russia-linked APT29 threat actor has been observed repurposing a legitimate red teaming attack methodology as part of cyber attacks leveraging malicious Remote Desktop Protocol (RDP) configuration files.

The activity, which has targeted governments and armed forces, think tanks, academic researchers, and Ukrainian entities, entails adopting a "rogue RDP" technique that was [previously documented](https://www.blackhillsinfosec.com/rogue-rdp-revisiting-initial-access-methods/) by Black Hills Information Security in 2022, Trend Micro said in a report.

"A victim of this technique would give partial control of their machine to the attacker, potentially leading to data leakage and malware installation," researchers Feike Hacquebord and Stephen Hilt [said](https://www.trendmicro.com/en_us/research/24/l/earth-koshchei.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity company is tracking the threat group under its own moniker Earth Koshchei, stating preparations for the campaign began as early as August 7-8, 2024. The RDP campaigns were also [spotlighted](https://thehackernews.com/2024/10/cert-ua-identifies-malicious-rdp-files.html) by the Computer Emergency Response Team of Ukraine (CERT-UA), Microsoft, and Amazon Web Services (AWS) back in October.

The spear-phishing emails were designed to deceive recipients into launching a malicious RDP configuration file attached to the message, causing their machines to connect to a foreign RDP server through one of the group's 193 RDP relays. An estimated 200 high-profile victims were targeted in a single day, indicative of the scale of the campaign.

The attack method outlined by Black Hill entails the use of an open-source project called [PyRDP](https://github.com/GoSecure/pyrdp) – described as a Python-based "Monster-in-the-Middle (MitM) tool and library" – in front of the actual adversary-controlled RDP server to minimize the risk of detection.

Thus, when a victim opens the RDP file, codenamed HUSTLECON, from the email message, it initiates an outbound RDP connection to the PyRDP relay, which then redirects the session to a malicious server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyUVk1Zva99t4QP62NvLXT2zal8yqMuXP0hBuNNuYvLcgpW32Wqw00DJHYLCPx5CEj0tXtq-ieFRVuIdOi_MeFez3KX2bOrrudpPnwitFGDar42GeQcsvEu98006hKzWDKCgoP13tAbtyMQpCS1RIARCY8Sd8y88K3lVc3Kpk9tI3LLpWPqcS6GG9xW67X/s790-rw-e365/attacker.png)

"Upon establishing the connection, the rogue server mimics the behavior of a legitimate RDP server and exploits the session to carry out various malicious activities," the researchers said. "A primary attack vector involves the attacker deploying malicious scripts or altering system settings on the victim's machine."

On top of that, the PyRDP proxy server enables the attacker to gain access to the victim's systems, perform file operations, and inject malicious payloads. The attack culminates with the threat actor leveraging the compromised RDP session to exfiltrate sensitive data, including credentials and other proprietary information, via the proxy.

What's notable about this attack is that the data collection is facilitated by means of a malicious configuration file without having to deploy any custom malware, thereby allowing the threat actors to fly under the radar.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another characteristic that deserves a mention is the use of anonymization layers like TOR exit nodes to control the RDP servers, as well as residential proxy providers and commercial VPN services to access legitimate mail servers that were employed to send the spear-phishing emails.

"Tools like PyRDP enhance the attack by enabling the interception and manipulation of RDP connections," the researchers added. "PyRDP can automatically crawl shared drives redirected by the victim and save their contents locally on the attacker's machine, facilitating seamless data exfiltration."

"Earth Koshchei uses new methodologies over time for their espionage campaigns. They not only pay close attention to old and new vulnerabilities that help them in getting initial access, but they also look at the methodologies and tools that red teams develop."

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

[APT29](https://thehackernews.com/search/label/APT29)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Malware](https://thehackernews.com/search/label/...