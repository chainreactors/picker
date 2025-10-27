---
title: Russian RomCom Attacks Target Ukrainian Government with New SingleCamper RAT Variant
url: https://thehackernews.com/2024/10/russian-romcom-attacks-target-ukrainian.html
source: The Hacker News
date: 2024-10-18
fetch_date: 2025-10-06T18:57:31.592446
---

# Russian RomCom Attacks Target Ukrainian Government with New SingleCamper RAT Variant

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

# [Russian RomCom Attacks Target Ukrainian Government with New SingleCamper RAT Variant](https://thehackernews.com/2024/10/russian-romcom-attacks-target-ukrainian.html)

**Oct 17, 2024**Ravie LakshmananThreat Intelligence / Malware

[![SingleCamper RAT Variant](data:image/png;base64... "SingleCamper RAT Variant")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5dMTeOMD0V9jeonYAOxkOu9M4lAA-Hvi9oN0h1aTACQPCwNLArQEHwP6blMwOx4Kts5HQhMTl3k7mZmG7-5FYeaCq0-FyvzwH4D6cIBhG4hNYCsSO9oWeF0VbGMtFV6RIn8fYXke7U5pLxP6VPMgWzfl6kJ7fdfJ389xb-hVRlNJHRnc8KpoinckFho9Z/s790-rw-e365/attack.png)

The Russian threat actor known as RomCom has been linked to a new wave of cyber attacks aimed at Ukrainian government agencies and unknown Polish entities since at least late 2023.

The intrusions are characterized by the use of a variant of the [RomCom RAT](https://thehackernews.com/2023/10/new-peapod-cyberattack-campaign.html) dubbed SingleCamper (aka [SnipBot](https://thehackernews.com/2024/09/transportation-companies-hit-by.html) or RomCom 5.0), said Cisco Talos, which is monitoring the activity cluster under the moniker UAT-5647.

"This version is loaded directly from the registry into memory and uses a loopback address to communicate with its loader," security researchers Dmytro Korzhevin, Asheer Malhotra, Vanja Svajcer, and Vitor Ventura [noted](https://blog.talosintelligence.com/uat-5647-romcom/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

RomCom, also tracked as Storm-0978, Tropical Scorpius, UAC-0180, UNC2596, and Void Rabisu, has engaged in multi-motivational operations such as ransomware, extortion, and targeted credential gathering since its emergence in 2022.

It's been assessed that the operational tempo of their attacks has increased in recent months with an aim to set up long-term persistence on compromised networks and exfiltrate data, suggesting a clear espionage agenda.

To that end, the threat actor is said to be "aggressively expanding their tooling and infrastructure to support a wide variety of malware components authored in diverse languages and platforms" such as C++ (ShadyHammock), Rust (DustyHammock), Go ([GLUEEGG](https://thehackernews.com/2024/07/ukrainian-institutions-targeted-using.html)), and Lua ([DROPCLUE](https://thehackernews.com/2024/07/ukrainian-institutions-targeted-using.html)).

The attack chains start with a spear-phishing message that delivers a downloader -- either coded in C++ (MeltingClaw) or Rust (RustyClaw) -- which serves to deploy the ShadyHammock and DustyHammock backdoors, respectively. In parallel, a decoy document is displayed to the recipient to maintain the ruse.

While DustyHammock is engineered to contact a command-and-control (C2) server, run arbitrary commands, and download files from the server, ShadyHammock acts as a launchpad for SingleCamper as well as listening for incoming commands.

Despite's ShadyHammock additional features, it's believed that it's a predecessor to DustyHammock, given the fact that the latter was observed in attacks as recently as September 2024.

SingleCamper, the latest version of RomCom RAT, is responsible for a wide range of post-compromise activities, which entail downloading the PuTTY's Plink tool to establish remote tunnels with adversary-controlled infrastructure, network reconnaissance, lateral movement, user and system discovery, and data exfiltration.

"This specific series of attacks, targeting high profile Ukrainian entities, is likely meant to serve UAT-5647's two-pronged strategy in a staged manner – establish long-term access and exfiltrate data for as long as possible to support espionage motives, and then potentially pivot to ransomware deployment to disrupt and likely financially gain from the compromise," the researchers said.

"It is also likely that Polish entities were also targeted, based on the keyboard language checks performed by the malware."

The disclosure comes as the Computer Emergency Response Team of Ukraine (CERT-UA) warned of cyber attacks mounted by a threat actor called [UAC-0050](https://thehackernews.com/2024/01/uac-0050-group-using-new-phishing.html) to steal funds as well as sensitive information using various malware families like Remcos RAT, SectopRAT, Xeno RAT, Lumma Stealer, Mars Stealer, and Meduza Stealer.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"UAC-0050's financial theft activities primarily involve stealing funds from the accounts of Ukrainian enterprises and private entrepreneurs after obtaining unauthorized access to the computers of accountants through remote control tools, such as Remcos and TEKTONITRMS," CERT-UA [said](https://cert.gov.ua/article/6281009).

"During the September - October 2024 period, UAC-0050 made at least 30 such attempts. These attacks involve forming fake financial payments through remote banking systems, with amounts varying from tens of thousands to several million UAH."

CERT-UA has also revealed that it observed attempts to distribute malicious messages via @reserveplusbot account on the Telegram message app that aim to deploy the Meduza Stealer malware under the pretext of installing a "special software."

"The account @reserveplusbot is posing as a Telegram bot to imitate the technical support of the 'Reserve+,' which is an app that enables conscripts and reservists to update their data remotely instead of going to the draft offices," the agency [said](https://cert.gov.ua/article/6281018). "It should be noted that such an account was indeed listed as one of the technical support contacts of 'Reserve+' in May 2024."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](...