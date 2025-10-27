---
title: Researchers Expose SVG and PureRAT Phishing Threats Targeting Ukraine and Vietnam
url: https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html
source: The Hacker News
date: 2025-09-27
fetch_date: 2025-10-02T20:48:17.610620
---

# Researchers Expose SVG and PureRAT Phishing Threats Targeting Ukraine and Vietnam

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

# [Researchers Expose Phishing Threats Distributing CountLoader and PureRAT](https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html)

**Sep 26, 2025**Ravie LakshmananMalware / Cryptocurrency

[![SVG and PureRAT Phishing](data:image/png;base64... "SVG and PureRAT Phishing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoAlwqZyRSOLUD2jXOxiKCOPZAMh081oe9ijFtBbCQqlFj5f_lZrJGiV1gJdkuipyKN_MhD1KpjlpLUG9bXgXxsH5XnLSuvGa3myeul0PlTZ7A6qsrToao7i6Hp68F4O0SghREIqMb3ae8zsJb0PJcKWHhRHpPt9r4pSGqXdFFEIC98sn6s5ezuAuCBdRi/s790-rw-e365/phishing-malware.jpg)

A new campaign has been observed impersonating Ukrainian government agencies in phishing attacks to deliver **CountLoader**, which is then used to drop **Amatera Stealer** and **PureMiner**.

"The phishing emails contain malicious Scalable Vector Graphics (SVG) files designed to trick recipients into opening harmful attachments," Fortinet FortiGuard Labs researcher Yurren Wan [said](https://www.fortinet.com/blog/threat-research/svg-phishing-hits-ukraine-with-amatera-stealer-pureminer) in a report shared with The Hacker News.

In the attack chains documented by the cybersecurity company, the SVG files are used to initiate the download of a password-protected ZIP archive, which contains a Compiled HTML Help (CHM) file. The CHM file, when launched, activates a chain of events that culminate in the deployment of CountLoader. The email messages claim to be a notice from the National Police of Ukraine.

CountLoader, which was the subject of a [recent analysis](https://thehackernews.com/2025/09/countloader-broadens-russian-ransomware.html) by Silent Push, has been found to drop various payloads like Cobalt Strike, AdaptixC2, and PureHVNC RAT. In this attack chain, however, it serves as a distribution vector for [Amatera Stealer](https://thehackernews.com/2025/07/weekly-recap-sharepoint-breach-spyware.html#:~:text=ACRStealer%20Variant%20Distributed%20in%20New%20Attacks), a variant of ACRStealer, and PureMiner, a stealthy .NET cryptocurrency miner.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth pointing out that both PureHVNC RAT and PureMiner are part of a broader malware suite developed by a threat actor known as PureCoder. Some of the other products from the same author include -

* PureCrypter, a crypter for Native and .NET
* PureRAT (aka ResolverRAT), a successor to PureHVNC RAT
* PureLogs, an information stealer and logger
* BlueLoader, a malware that can act as a botnet by downloading and executing payloads remotely
* PureClipper, a clipper malware that substitutes cryptocurrency addresses copied into the clipboard with attacker-controlled wallet addresses to redirect transactions and steal funds

According to Fortinet, Amatera Stealer and PureMiner are both deployed as fileless threats, with the malware "executed via .NET Ahead-of-Time (AOT) compilation with process hollowing or loaded directly into memory using PythonMemoryModule."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVXopjktCbqYBoCCXLHM0Fidviz39MF2rrl-kRBCFP0yCXtexyxa4WM-qsLIydjIALmAR8A9rYtXQOIW8dyovYArM9IqlABTBWI9-IzcPBFfIrp3l8AtBaozXrnSls2KOXPyP1FVu2jBlmIajKcLkLOI5jKdkMrK8W7UveSvcmr88UzVTVmWBcKxLMnToM/s2600/python.jpeg)

Amatera Stealer, once launched, gathers system information, collects files matching a predefined list of extensions, and harvests data from Chromium- and Gecko-based browsers, as well as applications like Steam, Telegram, FileZilla, and various cryptocurrency wallets.

"This phishing campaign demonstrates how a malicious SVG file can act as an HTML substitute to initiate an infection chain," Fortinet said. In this case, attackers targeted Ukrainian government entities with emails containing SVG attachments. The SVG-embedded HTML code redirected victims to a download site."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXi-DjN8-PO6UkCp2WPHLBQO87C1S6lko2mK-TQIM49os-8OYCswOpJwB06BXPplrywWnmySFIduQpPr7xYcibOI1GqAHwOBLQM48sp0u3_IRSBc9RqOMNOjb0KK_lz9ybYub_9NPTsE8coI6Z7In8QLjem_zCtPy6yEpHiQG1_di7m3CwXvPaYyOAVN7X/s2600/hunt.jpg)

The development comes as Huntress uncovered a likely Vietnamese-speaking threat group using phishing emails bearing copyright infringement notice themes to trick recipients into launching ZIP archives that lead to the deployment of [PXA Stealer](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html), which then evolves into a multi-layered infection sequence dropping PureRAT.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This campaign demonstrates a clear and deliberate progression, starting with a simple phishing lure and escalating through layers of in-memory loaders, defense evasion, and credential theft," security researcher James Northey [said](https://www.huntress.com/blog/purerat-threat-actor-evolution). "The final payload, PureRAT, represents the culmination of this effort: a modular, professionally developed backdoor that gives the attacker complete control over a compromised host."

"Their progression from amateurish obfuscation of their Python payloads to abusing commodity malware like PureRAT shows not just persistence, but also hallmarks of a serious and maturing operator."

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
[**Share on...