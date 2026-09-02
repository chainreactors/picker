---
title: Attackers Steal METR API Key and Consume AI Credits Worth About $600,000
url: https://thehackernews.com/2026/09/attackers-steal-metr-api-key-and.html
source: The Hacker News
date: 2026-09-01
fetch_date: 2026-09-02T06:41:52.893052
---

# Attackers Steal METR API Key and Consume AI Credits Worth About $600,000

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attackers Steal METR API Key and Consume AI Credits Worth About $600,000](https://thehackernews.com/2026/09/attackers-steal-metr-api-key-and.html)

**Ravie Lakshmanan**Sep 01, 2026Cyber Attack / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2b-1gQHvYc7ZLc86QFtZ2LoJ7zFalpJtSy_e_laxiM_f4Ftnhuvp5eCJZRSk2NL_0tZAZAl2z1UPYfOBSTbdGOPOZexgt3GkuUqsrZPgFB2F-qG2Ir_c7Ioj6zcJVdWjzBo90HpcObPWan5eID2df6OXyn3F7-LRpdOvO8TfiZSp8L2j89p2UbsDi3zM4/s1700-nu-rw-lo-l85-e365/metr.jpg)

METR (short for Model Evaluation and Threat Research and pronounced "Meter"), a research non-profit that evaluates frontier artificial intelligence (AI) models for their ability to carry out long-horizon, agentic tasks, disclosed that it suffered "two notable security incidents" where external actors attempted to gain unauthorized access to its systems.

No sensitive information is believed to have been accessed as a result of these incidents, it said, adding that a version of its findings was shared with AI companies it works with prior to public disclosure. The attacks have not been attributed to any known threat actor or group, nor did they involve AI agents breaking into its evaluations.

"In March 2026, attackers stole an API key for inference on public models and consumed a substantial amount of credits," METR [said](https://metr.org/blog/2026-08-31-security-update/#our-approach-to-security). "In May 2026, we observed attackers systematically probing our publicly accessible infrastructure, including an unsuccessful attempt to access internal data via an inadvertently exposed endpoint."

### The March Incident

According to METR, one of its researchers with no sensitive access is said to have used agents running on a personal EC2 instance that was intentionally made publicly accessible behind Google authentication. The instance contained an API key for METR's general-access (public models) account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

However, the "vibe-coded app" suffered from a "[fail-open vulnerability](https://owasp.org/www-community/Improper_Error_Handling)" that silently disabled authentication, causing the agent orchestration dashboard to be exposed to the public internet for several days.

"From our analysis, we suspect that the attacker found the instance by looking through recently-registered websites (e.g., in certificate transparency lists) to find vibe-coded sites with high-signal keywords relating to LLMs or agents, for purposes of harvesting potentially exposed model provider API keys," METR explained.

Once the system was identified, the threat actor prompted an agent directly to reveal its model provider API key, added an SSH key for persistent access, and used the stolen credentials to consume a significant amount of API credits on publicly-available models over a period of three weeks.

METR said the accrued credits would have racked up approximately $600,000 in bills had it not been provided to the non-profit for free by the model provider. It did not name the AI company.

It also noted that the illicit usage was not immediately caught because it runs large-scale evaluations and experiments that typically consume a high volume of tokens and the fact that there were no caps on token spend. Following the incident, METR said it has updated its security policies around putting METR credentials or data on non-METR infrastructure or devices, improved monitoring, and added spend alerts to keys where possible.

### The May Incident

The second attack observed in May 2026 has been described as a "sustained external attack campaign" orchestrated by a likely financially motivated threat actor to obtain unlawful access to frontier AI models.

"We observed the attackers systematically probing our publicly accessible infrastructure, with heavy use of agents to automate vulnerability discovery, including by credential stuffing authentication providers, attempting OAuth token grants, scanning newly deployed services, and attempting to phish staff," METR said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

Around the same time, the research entity said it inadvertently exposed a read-only SQL query mechanism built into its [public transcript viewer](https://transcripts.metr.org/). Although the queries were scoped to public data by default, a bug in the component could have been exploited to access unpublished evaluation data.

In addition, the database "accidentally included" sensitive model data, despite the fact that it was supposed to contain only data from non-sensitive models. METR said it became aware of the issue only after an independent security researcher discovered and reported it, resulting in the API being taken offline.

"The attackers had probed this endpoint in passing as part of their broader campaign, but the evidence shows no indication that they discovered the exploit or accessed any non-public data," METR said.

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

[artificial intelligence](https://thehackernews.com/search/label/arti...