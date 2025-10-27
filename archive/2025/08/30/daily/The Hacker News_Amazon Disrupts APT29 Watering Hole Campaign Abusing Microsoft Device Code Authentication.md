---
title: Amazon Disrupts APT29 Watering Hole Campaign Abusing Microsoft Device Code Authentication
url: https://thehackernews.com/2025/08/amazon-disrupts-apt29-watering-hole.html
source: The Hacker News
date: 2025-08-30
fetch_date: 2025-10-07T00:50:20.248263
---

# Amazon Disrupts APT29 Watering Hole Campaign Abusing Microsoft Device Code Authentication

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

# [Amazon Disrupts APT29 Watering Hole Campaign Abusing Microsoft Device Code Authentication](https://thehackernews.com/2025/08/amazon-disrupts-apt29-watering-hole.html)

**Aug 29, 2025**Ravie LakshmananThreat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKYZ5DLUHPr8ka-gN-66F-UM32FyEHFG-zXbjosHjQQDFT5AWRGWMwyyVCzU0HWoD-M7XErgpJumbsKwGKGzDsIz8BZlcBQ4iZYgWO_ShEi-jWnHHgGp-1gopfPnSGsl3F7m_zbTtk7lvz3PNFblrzvdH9Pc0lD7X5dDuGcqJMMmC6hptcp8-vVsInXrx3/s790-rw-e365/ms-code.jpg)

Amazon on Friday said it flagged and disrupted what it described as an opportunistic watering hole campaign orchestrated by the Russia-linked APT29 actors as part of their intelligence gathering efforts.

The campaign used "compromised websites to redirect visitors to malicious infrastructure designed to trick users into authorizing attacker-controlled devices through Microsoft's device code authentication flow," Amazon's Chief Information Security Officer CJ Moses [said](https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/).

APT29, also tracked as BlueBravo, Cloaked Ursa, CozyLarch, Cozy Bear, Earth Koshchei, ICECAP, Midnight Blizzard, and The Dukes, is the name assigned to a state-sponsored hacking group with ties to Russia's Foreign Intelligence Service (SVR).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In recent months, the prolific threat actor has been [linked](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html) to attacks leveraging malicious Remote Desktop Protocol (RDP) configuration files to target Ukrainian entities and exfiltrate sensitive data.

Since the start of the year, the adversarial collective has been observed adopting various phishing methods, including [device code phishing](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html) and [device join phishing](https://thehackernews.com/2025/04/russian-hackers-exploit-microsoft-oauth.html), to obtain unauthorized access to Microsoft 365 accounts.

As recently as June 2025, Google [said](https://thehackernews.com/2025/06/russian-apt29-exploits-gmail-app.html) it observed a threat cluster with affiliations to APT29 weaponizing a Google account feature called application-specific passwords to gain access to victims' emails. The highly targeted campaign was attributed to UNC6293.

The latest activity identified by Amazon's threat intelligence team underscores the threat actor's continued efforts to harvest credentials and gather intelligence of interest, while simultaneously sharpening their tradecraft.

"This opportunistic approach illustrates APT29's continued evolution in scaling their operations to cast a wider net in their intelligence collection efforts," Moses said.

The attacks involved APT29 compromising various legitimate websites and injecting JavaScript that redirected approximately 10% of visitors to actor-controlled domains, such as findcloudflare[.]com, that mimicked Cloudflare verification pages to give an illusion of legitimacy.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In reality, the end goal of the campaign was to entice victims into entering a legitimate device code generated by the threat actor into a sign-in page, effectively granting them access to their Microsoft accounts and data. This technique was [detailed](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html) by both Microsoft and Volexity back in February 2025.

The activity is also noteworthy for incorporating various evasion techniques, such as Base64 encoding to conceal malicious code, setting cookies to prevent repeated redirects of the same visitor, and shifting to new infrastructure when blocked.

Amazon told The Hacker News that it doesn't have additional information on how many websites were compromised as part of this effort, and how these sites were hacked in the first place. The tech giant also noted that it was able to link the domains used in this campaign with infrastructure previously attributed to APT29.

"Despite the actor's attempts to migrate to new infrastructure, including a move off AWS to another cloud provider, our team continued tracking and disrupting their operations," Moses said. "After our intervention, we observed the actor register additional domains such as cloudflare.redirectpartners[.]com, which again attempted to lure victims into Microsoft device code authentication workflows."

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

[amazon](https://thehackernews.com/search/label/amazon)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Malware](https://thehackernews.com/search/label/Malware)[Microsoft 365](https://thehackernews.com/search/label/Microsoft%20365)[Phishing](https://thehackernews.com/search/label/Phishing)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://theh...