---
title: Emotet Rises Again: Evades Macro Security via OneNote Attachments
url: https://thehackernews.com/2023/03/emotet-rises-again-evades-macro.html
source: The Hacker News
date: 2023-03-21
fetch_date: 2025-10-04T10:11:56.954503
---

# Emotet Rises Again: Evades Macro Security via OneNote Attachments

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

# [Emotet Rises Again: Evades Macro Security via OneNote Attachments](https://thehackernews.com/2023/03/emotet-rises-again-evades-macro.html)

**Mar 20, 2023**Ravie LakshmananEndpoint Security / Email Security

[![Emotet OneNote Attachments](data:image/png;base64... "Emotet OneNote Attachments")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimtIyXQ0OSVDy8K3bJIQLidFb62Elg-imTXGPzQkNTTZKGkv7G3DD0HOlPaskyZ8Az-fbS6N3nCkJ0mWNz97-6k8bQzU6oD3UQIubvDSPhVUsHUfMTI1ssZ94U9VAqz45vvWyOiiLuqwPXg8o1ZVUdlZx3E2Yy-TukPhXlWmmDbmWNplDQ9SD65-Lg/s790-rw-e365/emotet.png)

The notorious Emotet malware, in its [return after a short hiatus](https://cofense.com/blog/emotet-sending-malicious-emails-after-three-month-hiatus/), is now being distributed via [Microsoft OneNote email attachments](https://thehackernews.com/2023/02/post-macro-world-sees-rise-in-microsoft.html) in an attempt to bypass macro-based security restrictions and compromise systems.

[Emotet](https://thehackernews.com/2023/01/emotet-malware-makes-comeback-with-new.html), linked to a threat actor tracked as Gold Crestwood, Mummy Spider, or TA542, continues to be a potent and resilient threat despite attempts by law enforcement to take it down.

A [derivative](https://www.blackberry.com/us/en/solutions/endpoint-security/ransomware-protection/dridex) of the [Cridex](https://securelist.com/dridex-a-history-of-evolution/78531/) [banking worm](https://services.global.ntt/en-au/insights/blog/dridex-and-emotet-infrastructure-overlaps) – which was [subsequently](https://community.broadcom.com/symantecenterprise/viewdocument/dridex-and-how-to-overcome-it?CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68) [replaced](https://www.cisa.gov/news-events/cybersecurity-advisories/aa19-339a) by [Dridex](https://thehackernews.com/2023/01/dridex-malware-now-attacking-macos.html) around the same time GameOver Zeus was disrupted in 2014 – Emotet has [evolved](https://www.spamhaus.org/news/article/806/emotet-is-disrupted-but-the-malware-it-installed-lives-on) into a "monetized platform for other threat actors to run malicious campaigns on a pay-per-install (PPI) model, allowing theft of sensitive data and ransom extortion."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While Emotet infections have acted as a [conduit](https://www.attackiq.com/2023/02/17/emulating-emotet/) to deliver Cobalt Strike, IcedID, Qakbot, Quantum ransomware, and TrickBot, its return in late 2021 was [facilitated](https://thehackernews.com/2021/12/140000-reasons-why-emotet-is.html) by means of TrickBot.

"Emotet is known for extended periods of inactivity, often occurring multiple times per year, where the botnet maintains a steady-state but does not deliver spam or malware," Secureworks [notes](https://www.secureworks.com/research/threat-profiles/gold-crestwood) in its profile of the actor.

[![OneNote Attachments](data:image/png;base64... "OneNote Attachments")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNdJh87bPreCdIFDkmO9OQTrVH3Ju-huUkLI4-uYYICe4UU9rtbLen9EFB-ywanvKu6I2sNvB8HWJIe9lvo0nvl7EPU1QuNz6tgqT5q-7Agl44cSRjYuDWjZQSn1krEtZVqd1bjUaE0lUCsvO8TL-2T9YRQ4iD8AUoqeZIkGrGwXcc2uJCn4mVyXRU/s790-rw-e365/oen.png)

The dropper malware is commonly distributed through spam emails containing malicious attachments. But with Microsoft taking steps to block macros in downloaded Office files, OneNote attachments have emerged as an appealing [alternative pathway](https://www.huntress.com/blog/addressing-initial-access).

"The OneNote file is simple but yet effective at social engineering users with a fake notification stating that the document is protected," Malwarebytes [disclosed](https://www.malwarebytes.com/blog/threat-intelligence/2023/03/emotet-onenote) in a new alert. "When instructed to double-click on the View button, victims will inadvertently double-click on an embedded script file instead."

[![Emotet OneNote Attachments](data:image/png;base64... "Emotet OneNote Attachments")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5YQcvdyGPP5ruNnyzhcszcgeb2j9LFRUVjvUWK_KKsBFJ795mNsKOIaxV1EKZkPDH2oVTS-1gleTYB62pjBzUuQExljkWWa6DiQ3s-w3O9wE5iUqOeVEJZqaANd6SapL--mFgvN9j3zrUy_jLzBsuY-0gEKUcSR625w5hJXwEPDpNY5065D-yBsvQcA/s790-rw-e365/unit.png)

The Windows Script File (WSF) is engineered to retrieve and execute the Emotet binary payload from a remote server. Similar findings have been echoed by [Cyble](https://blog.cyble.com/2023/03/17/recent-emotet-spam-campaign-utilizing-new-tactics/), [IBM X-Force](https://exchange.xforce.ibmcloud.com/threats/guid%3A7ad7053de0ccf1eb06b272bd3deb0fa5), and Palo Alto Networks [Unit 42](https://twitter.com/Unit42_Intel/status/1636739251277647874).

That said, Emotet still continues to use booby-trapped documents containing macros to deliver the malicious payload, employing social engineering lures to entice users into enabling macros to activate the attack chain.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Such documents have been observed to leverage a technique called decompression bomb to conceal a very large file (over 550 MB) within ZIP archive attachments to fly under the radar, according to multiple reports from [Cyble](https://blog.cyble.com/2023/03/10/emotet-strikes-again-resuming-spamming-operations/), [Deep Instinct](https://www.deepinstinct.com/blog/emotet-again-the-first-malspam-wave-of-2023), [Hornetsecurity](https://www.hornetsecurity.com/en/press-releases/dangerous-new-instance-of-emotet/), and [Trend Micro](https://www.trendmicro.com/en_us/research/23/c/emotet-returns-now-adopts-binary-padding-for-evasion.html).

This is achieved by [padding 00-byte](https://attack.mitre.org/techniques/T1027/001/) at the end of the document to artificially inflate the file size so as to exceed the limitations imposed by anti-malware solutions.

The latest development is a sign of the operators' flexibility and agility in switching attachment types for initial delivery to evade...