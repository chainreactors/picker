---
title: Cursor Says Stolen Fireworks AI Key Led to Trojanized Claude Code Extension Incident
url: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html
source: The Hacker News
date: 2026-11-15
fetch_date: 2026-11-16T08:48:48.305915
---

# Cursor Says Stolen Fireworks AI Key Led to Trojanized Claude Code Extension Incident

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Cursor Says Stolen Fireworks AI Key Led to Trojanized Claude Code Extension Incident](https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html)

**Ravie Lakshmanan**Nov 15, 2026Artificial Intelligence / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg16ACawbG7rP_kT-8Boo4xdTje3BeTWyFSnNXwHhr5cvy2-1X3Ljhrc1IuZlseWd55tN8E1yjQ9ldhTnjWTU-GJBpX_Zen36YiLQGsRSRAoteqHyxx7mn_w0QgLfMKDLItA4p_jpHajucbglLnCR_zWBY_t82YvFkLa9dQFBfjP1BrTlrNdYufsGMSZiGn/s1700-nu-rw-lo-l85-e365/cursor.jpg)

The [compromise of Anthropic's official Claude Code extension](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html) on Cursor's extension marketplace was the result of the theft of an access key that was exposed in the wake of a breach targeting [Fireworks AI](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html).

"An attacker obtained an access key we had issued to Fireworks," Cursor [said](https://cursor.com/blog/security-incident-update) in a Friday update. "The key was [exposed by Fireworks](https://fireworks.ai/security/bulletins), and the attacker used it to copy data from a read-only storage bucket we used to share data with them."

The disclosure comes nearly two weeks after a [trojanized version](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html) of Anthropic's official Claude Code extension was distributed through Cursor Marketplace as a legitimate update, attempting to install a persistent SSH backdoor on affected systems.

According to the artificial intelligence (AI)-powered coding platform, the read-only storage bucket is said to have contained limited coding agent traces from sessions that were not in Privacy Mode. Privacy Mode is a [Cursor-specific setting](https://cursor.com/data-use) that, if enabled, allows users to opt out of their data being used for training purposes.

These sessions, most of which date back to 2025, were permitted to be used for model training. Among these traces were credentials that had not been edited out, exposing the API credentials of less than 0.01% of customers in the process.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The attacker, Cursor added, used these credentials as a starting point to reach select software-as-a-service (SaaS) tools used by Cursor and then access the following data -

* Select archived non-production Cursor source code repositories, including some containing business contact information
* Limited customer support data and email conversations
* Product usage metrics and contact details
* Summaries of some coding agent conversations
* Some credentials users had sent to the Cursor support team

Cursor said it took steps to deactivate the vendor's key, revoke and rotate credentials, and hunt for signs of deeper access, and contain it after "we identified further access." The company also said it temporarily disabled internal and product services, disrupting access to some Cursor features.

The next phase of the attack took place on October 29, 2026, when the attacker used a stolen credential from the exposed data of its internal system to place trojanized versions of Anthropic's Claude Code extension directly on the cache used to serve Cursor's extension marketplace.

"At most 5,000 users who requested specific cached versions of the extension on October 29 potentially received the malicious build," Cursor said. "It was available for approximately 11 hours before we removed it. We took it down, took the extension marketplace offline, and worked with the cloud service provider hosting the attacker's server to take it down."

The company said it notified affected users who installed versions 2.1.312 or 2.1.313 from the marketplace during the exposure window and helped revoke exposed credentials. It has also moved all inference traffic off Fireworks, deactivated the key issued to it, and cut off its access to all data sets we shared with it.

Furthermore, Cursor emphasized that no additional malicious activity has been detected since November 1, 2026.

There is no evidence that the incident impacted users who had enabled Privacy Mode, customer code repositories, Cursor's own production environment, Cursor app and its official updates, its other apps, or any other extension or plugin downloaded from Cursor Marketplace.

### Uber Also Impacted by Fireworks Incident

The development comes as Uber confirmed unknown threat actors stole thousands of drivers' license information after obtaining internal credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"On October 9, 2026, a service provider notified Uber that an unauthorized third-party had compromised the service provider's internal credentials and used them to access Uber's account with the service provider," the company [said](https://oag.ca.gov/ecrime/databreach/reports/sb24-632751?7194ef805fa2d04b0f7e8c9521f97343) in a filing with the U.S. state of California. "On October 13, 2026, our investigation determined that the unauthorized party had used the compromised credentials to access Uber data connected to the service provider."

Although the name of the provider was not disclosed, TechCrunch [reported](https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/) that the provider in question is Fireworks AI. Uber has not disclosed how many users were impacted by the breach. Last week, online productivity startup Notion also confirmed its data was stolen in the Fireworks AI hack.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

S...