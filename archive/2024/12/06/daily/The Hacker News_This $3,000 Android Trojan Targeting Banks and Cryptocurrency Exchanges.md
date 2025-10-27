---
title: This $3,000 Android Trojan Targeting Banks and Cryptocurrency Exchanges
url: https://thehackernews.com/2024/12/this-3000-android-trojan-targeting.html
source: The Hacker News
date: 2024-12-06
fetch_date: 2025-10-06T19:45:30.572168
---

# This $3,000 Android Trojan Targeting Banks and Cryptocurrency Exchanges

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

# [This $3,000 Android Trojan Targeting Banks and Cryptocurrency Exchanges](https://thehackernews.com/2024/12/this-3000-android-trojan-targeting.html)

**Dec 05, 2024**Ravie LakshmananCryptocurrency / Mobile Security

[![Android Trojan](data:image/png;base64... "Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbPZP74p5tgDHJM3FLaCd3WuHGJn-xRnKy1I2scD0ZD5sF1gr75IG1XmH4ZjtHIdk-Hfekbx8ODv6aJ9zG7N3Y2bMRHNFrxVZCIr3QoCDk2-pJYpSv7b-ezN-zHn0661uvBFyfB7Wx8q1mteQwqBxg9WBe0RXOdIk5At-gv87ylfQKQz1pyKLBxDccbJeJ/s790-rw-e365/android.png)

As many as 77 banking institutions, cryptocurrency exchanges, and national organizations have become the target of a newly discovered Android remote access trojan (RAT) called **DroidBot**.

"DroidBot is a modern RAT that combines hidden VNC and overlay attack techniques with spyware-like capabilities, such as keylogging and user interface monitoring," Cleafy researchers Simone Mattia, Alessandro Strino, and Federico Valentini [said](https://www.cleafy.com/cleafy-labs/droidbot-insights-from-a-new-turkish-maas-fraud-operation).

"Moreover, it leverages dual-channel communication, transmitting outbound data through [MQTT](https://mqtt.org) and receiving inbound commands via HTTPS, providing enhanced operation flexibility and resilience."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Italian fraud prevention company said it discovered the malware in late October 2024, although there is evidence to suggest that it has been active since at least June, operating under a malware-as-a-service (MaaS) model for a monthly fee of $3,000.

[![Android Trojan](data:image/png;base64... "Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCvETMHSWhLpmKpyhyphenhyphenn2yh6av8ynb99cfg2Jmog_iiGc7kfSq_TyZLShm5xuPWjwq0XWqUpfIRxig0st4M6DvFLgXyrvrTlGMnQDxTJYWoY0gihCm59_UJp_Mj7Ejr2IG5EzdHCnkUNR-zp45StjfQySemlJLwT1yBC82QBemfivEj69Qi3HHl5juVzSZJ/s790-rw-e365/chrome.png)

No less than 17 affiliate groups have been identified as paying for access to the offering. This also includes access to a web panel from where they can modify the configuration to create custom APK files embedding the malware, as well as interact with the infected devices by issuing various commands.

Campaigns leveraging DroidBot have been primarily observed in Austria, Belgium, France, Italy, Portugal, Spain, Turkey, and the United Kingdom. The malicious apps are disguised as generic security applications, Google Chrome, or popular banking apps.

While the malware leans heavily on abusing [Android's accessibility services](https://thehackernews.com/2024/11/new-android-banking-malware-toxicpanda.html) to harvest sensitive data and remotely control the infected devices, it stands apart for leveraging two different protocols for command-and-control (C2).

[![Android Trojan](data:image/png;base64... "Android Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZx8ghs0GDnjkAoWwPI08fOHgHyehFBikKOpGS9GZF7qVoWtNkXNxWdVnX6oorzlfthZp8o2snmp0m_s9Z5byPlR_5mTH8F34J4K6hM4imDwW1mICZu21Ntf5HsvAtG3ccjMGEEwleRmofkIWe9m5nORfEWpHDEKBSLCIDZ2SCQBJfm6gVBah6htT3rwAz/s790-rw-e365/android.png)

Specifically, DroidBot employs HTTPS for inbound commands, whereas outbound data from infected devices is transmitted using a messaging protocol called MQTT.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This separation enhances its operational flexibility and resilience," the researchers said. "The MQTT broker used by DroidBot is organised into specific topics that categorise the types of communication exchanged between the infected devices and the C2 infrastructure."

The exact origins of the threat actors behind the operation are not known, although an analysis of the malware samples has revealed that they are Turkish speakers.

"The malware presented here may not shine from a technical standpoint, as it is quite similar to known malware families," the researchers noted. "However, what really stands out is its operational model, which closely resembles a Malware-as-a-Service (MaaS) scheme – something not commonly seen in this type of threat."

### Update

Following the publication of the story, Google shared the below statement with The Hacker News -

*"Based on our current detection, no apps containing this malware are found on Google Play. Android users are automatically protected against known versions of this malware by* [*Google Play Protect*](https://support.google.com/googleplay/answer/2812853?hl=en)*, which is on by default on Android devices with Google Play Services. Google Play Protect can warn users or block apps known to exhibit malicious behavior, even when those apps come from sources outside of Play."*

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

[Accessibility Services](https://thehackernews.com/search/label/Accessibility%20Services)[Android](https://thehackernews.com/search/label/Android)[Banking](https://thehackernews.com/search/label/Banking)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fraud Prevention](https://t...