---
title: MintsLoader Drops GhostWeaver via Phishing, ClickFix — Uses DGA, TLS for Stealth Attacks
url: https://thehackernews.com/2025/05/mintsloader-drops-ghostweaver-via.html
source: The Hacker News
date: 2025-05-03
fetch_date: 2025-10-06T22:29:47.297549
---

# MintsLoader Drops GhostWeaver via Phishing, ClickFix — Uses DGA, TLS for Stealth Attacks

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

# [MintsLoader Drops GhostWeaver via Phishing, ClickFix — Uses DGA, TLS for Stealth Attacks](https://thehackernews.com/2025/05/mintsloader-drops-ghostweaver-via.html)

**May 02, 2025**Ravie LakshmananMalware / Threat Intelligence

[![MintsLoader Drops GhostWeaver via Phishing, ClickFix](data:image/png;base64... "MintsLoader Drops GhostWeaver via Phishing, ClickFix")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi81FeI7YdCsovdKQp8OxHtIcKoCrJidtDHkcJiFGHnc75PuS4FfVT9sFIYNtE66oD8iu4g2pxgBeXhx9r8_43wEtJFqvLoNInKrV_h6G02fBzJ-ydd9xIxgAFUiuHsmtx-6x_PgYBr4cBm-Pg9o2dLEfypyBUEMjLudetl8VdlCq3uvlLWIUU0wRjYMRJp/s790-rw-e365/phishing.jpg)

The malware loader known as **MintsLoader** has been used to deliver a PowerShell-based remote access trojan called GhostWeaver.

"MintsLoader operates through a multi-stage infection chain involving obfuscated JavaScript and PowerShell scripts," Recorded Future's Insikt Group [said](https://www.recordedfuture.com/research/uncovering-mintsloader-with-recorded-future-malware-intelligence-hunting) in a report shared with The Hacker News.

"The malware employs sandbox and virtual machine evasion techniques, a domain generation algorithm (DGA), and HTTP-based command-and-control (C2) communications."

Phishing and drive-by download campaigns distributing [MintsLoader](https://thehackernews.com/2025/01/mintsloader-delivers-stealc-malware-and.html) have been detected in the wild since early 2023, per [Orange Cyberdefense](https://github.com/cert-orangecyberdefense/mintsloader). The loader has been observed delivering various follow-on payloads like StealC and a modified version of the Berkeley Open Infrastructure for Network Computing (BOINC) client.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware has also been put to use by threat actors operating e-crime services like [SocGholish](https://www.darktrace.com/blog/socgholish-from-loader-and-c2-activity-to-ransomhub-deployment) (aka FakeUpdates) and [LandUpdate808](https://thehackernews.com/2025/05/fake-security-plugin-on-wordpress.html) (aka TAG-124), distributing via phishing emails targeting the industrial, legal, and energy sectors and fake browser update prompts.

[![MintsLoader Drops GhostWeaver via Phishing, ClickFix](data:image/png;base64... "MintsLoader Drops GhostWeaver via Phishing, ClickFix")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-rTtkJUvG1Qa2qYCS5umLq5VkS0-z15v4Fr_FvwMPHPlfci4t8z_IWxl2m1wc69jS2CKoG5iW8lLhjPvTU-I1yBWnHh7i3fUfFagSKi7mb11WaYciNEyRTCi8wfFpWPQznl6ZVU51jFt794JFyqp3CJLQJ3hd2MsCo-2-BfQukgkqjRpRjJDQ2ubSP9Fx/s790-rw-e365/malware.png)

In a notable twist, recent attack waves have employed the increasingly prevalent social engineering tactic called ClickFix to trick site visitors into copying and executing malicious JavaScript and PowerShell code. The links to ClickFix pages are distributed via spam emails.

"Although MintsLoader functions solely as a loader without supplementary capabilities, its primary strengths lie in its sandbox and virtual machine evasion techniques and a DGA implementation that derives the C2 domain based on the day it is run," Recorded Future said.

[![Uses DGA, TLS for Stealth Attacks](data:image/png;base64... "Uses DGA, TLS for Stealth Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA9ekyZA8MjNVwbun9BwoQKLtqGQfJxSYsnDUgn7DFhVeF8aO4G9XOLgCBrzAfVlcGRsqoz-iWwMzf-Z8n5mh-x0C1AWrWQXLwcuqtgOHrmCiJBWLonmmguGBDCDJSaXkj7o8Nm4oDD7nBU7OymN5jD4wC8BM-ROncuhRYn1eEEBng1tm96zJ-FKUJ_-Sq/s790-rw-e365/phishing.png)

These features, coupled with obfuscation techniques, enable threat actors to hinder analysis and complicate detection efforts. The primary responsibility of the malware is to download the next-stage payload from a DGA domain over HTTP by means of a PowerShell script.

GhostWeaver, according to a [report](https://trac-labs.com/dont-ghost-the-socgholish-ghostweaver-backdoor-574154dd9983) from TRAC Labs earlier this February, is designed to maintain persistent communication with its C2 server, generate DGA domains based on a fixed-seed algorithm based on the week number and year, and deliver additional payloads in the form of plugins that can steal browser data and manipulate HTML content.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Notably, GhostWeaver can deploy MintsLoader as an additional payload via its sendPlugin command. Communication between GhostWeaver and its command-and-control (C2) server is secured through TLS encryption using an obfuscated, self-signed X.509 certificate embedded directly within the PowerShell script, which is leveraged for client-side authentication to the C2 infrastructure," Recorded Future said.

The disclosure comes as Kroll [revealed](https://www.kroll.com/en/insights/publications/cyber/rapid-evolution-of-clearfake-delivery) attempts made by threat actors to secure initial access through an ongoing campaign codenamed [CLEARFAKE](https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html) that leverages ClickFix to lure victims into running MSHTA commands that ultimately deploy the Lumma Stealer malware.

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
[**Shar...