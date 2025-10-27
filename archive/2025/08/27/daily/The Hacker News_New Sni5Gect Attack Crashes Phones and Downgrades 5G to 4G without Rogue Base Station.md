---
title: New Sni5Gect Attack Crashes Phones and Downgrades 5G to 4G without Rogue Base Station
url: https://thehackernews.com/2025/08/new-sni5gect-attack-crashes-phones-and.html
source: The Hacker News
date: 2025-08-27
fetch_date: 2025-10-07T00:50:31.968460
---

# New Sni5Gect Attack Crashes Phones and Downgrades 5G to 4G without Rogue Base Station

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

# [New Sni5Gect Attack Crashes Phones and Downgrades 5G to 4G without Rogue Base Station](https://thehackernews.com/2025/08/new-sni5gect-attack-crashes-phones-and.html)

**Aug 26, 2025**Ravie LakshmananVulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIkgJca1vtf2mEOJnQ21hV27JFIrMEfztrhDiYEwEDsWRengbYPauuyipn-l2xi0x-t5FJ3R5BEpyg9v0WY7v6fGN6w0UqxQTF92K7buuCNOEDPO79OS6palgW1ZTCKIymFZiGC9RCKtkd8QgAmQITisMpaf9_mJJtj1JNg8-NUW6J7cnCST2FvEXMneHf/s790-rw-e365/5g-hack.jpg)

A team of academics has devised a novel attack that can be used to downgrade a 5G connection to a lower generation without relying on a rogue base station (gNB).

The [attack](https://asset-group.github.io/Sni5Gect-5GNR-sniffing-and-exploitation/), per the ASSET (Automated Systems SEcuriTy) Research Group at the Singapore University of Technology and Design (SUTD), relies on a new open-source software toolkit named **Sni5Gect** (short for "Sniffing 5G Inject") that's designed to sniff unencrypted messages sent between the base station and the user equipment (UE, i.e., a phone) and inject messages to the target UE over-the-air.

The framework can be used to carry out attacks such as crashing the UE modem, downgrading to earlier generations of networks, fingerprinting, or authentication bypass, according to Shijie Luo, Matheus Garbelini, Sudipta Chattopadhyay, and Jianying Zhou.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"As opposed to using a rogue base station, which limits the practicality of many 5G attacks, SNI5GECT acts as a third-party in the communication, silently sniffs messages, and tracks the protocol state by decoding the sniffed messages during the UE attach procedure," the researchers said. "The state information is then used to inject a targeted attack payload in downlink communication."

The findings build upon a prior study from ASSET in late 2023 that led to the discovery of 14 flaws in the firmware implementation of 5G mobile network modems from MediaTek and Qualcomm, collectively dubbed [5Ghoul](https://thehackernews.com/2023/12/new-5g-modems-flaws-affect-ios-devices.html), that could be exploited to launch attacks to drop connections, freeze the connection that involves manual reboot, or downgrade the 5G connectivity to 4G.

The Sni5Gect attacks are designed to passively sniff messages during the initial connection process, decode the message content in real-time, and then leverage the decoded message content to inject targeted attack payloads.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigXrU9_zAlwUxdYo2kLLGMz9ihOedU33VfFLMBu3p9OHFAX4xl3mA987lVL0_JZdlQTz0KHCYBmMIA6FgXFPQoOFRROYFtebqtH-SzDHeInw4vXbWrIkQ36w0E8HiPNPP3Ex9n9bmHuK0zorvDCp23Q35Mqw9xFYB4hsD8spPcj_vkTDc4DKJOeOtMORTt/s790-rw-e365/sni.jpg)

Specifically, the attacks are designed to take advantage of the phase before the authentication procedure, at which point the messages exchanged between the gNB and the UE are not encrypted. As a result, the threat model does not require knowledge of the UE's credentials to sniff uplink/downlink traffic or inject messages.

"To the best of our knowledge, SNI5GECT is the first framework that empowers researchers with both over-the-air sniffing and stateful injection capabilities, without requiring a rogue gNB," the researchers said.

"For example, an attacker can exploit the short UE communication window that spans from the RACH process until the NAS security context is established. Such an attacker actively listens for any RAR message from the gNB, which provides the RNTI to decode further UE messages."

This enables the threat actor to crash the modem on the victim's device, fingerprint the targeted device, and even downgrade the connection to 4G, which has known vulnerabilities that can be exploited by the attacker to track the UE location over time.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In tests against five smartphones, including OnePlus Nord CE 2, Samsung Galaxy S22, Google Pixel 7, and Huawei P40 Pro, the study achieved 80% accuracy in uplink and downlink sniffing, and managed to inject messages with a success rate of 70-90% from a distance of up to 20 meters (65 feet).

The Global System for Mobile Communications Association (GSMA), a non-profit trade association that represents mobile network operators worldwide and develops new technologies, has acknowledged the multi-stage, downgrade attack, and assigned it the identifier CVD-2024-0096.

"We argue that SNI5GECT is a fundamental tool in 5G security research that enables not only over-the-air 5G exploitation but advancing future research on packet-level 5G intrusion detection and mitigation, security enhancements to 5G physical layer security and beyond," the researchers concluded.

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

[5G Security](https://thehackernews.com/search/label/5G%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data privacy](https://thehackernews.com/search/label/data%20privacy)[mobile security](https://thehackernews.co...