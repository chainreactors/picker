---
title: Researchers Uncover 'LLMjacking' Scheme Targeting Cloud-Hosted AI Models
url: https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html
source: The Hacker News
date: 2024-05-11
fetch_date: 2025-10-06T17:19:11.256437
---

# Researchers Uncover 'LLMjacking' Scheme Targeting Cloud-Hosted AI Models

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

# [Researchers Uncover 'LLMjacking' Scheme Targeting Cloud-Hosted AI Models](https://thehackernews.com/2024/05/researchers-uncover-llmjacking-scheme.html)

**May 10, 2024**Ravie LakshmananVulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8sh-XmpsFwYT_aLaIqq4Tzn_W8HiANHxel6Vyy2-hLUvNgqpex97k8qG7SE8xPouPjkPpF-RuctUUeURbv0wg8sR-RUBFStCYplZP56arpce9kZ0rg8rb_bMRMFGV3Q_u5h3PUxznvpjiCljMNt33Yk2IcleXBku1rS0K6saao9m6MTqHsFiMDmcvdkJ-/s790-rw-e365/app.png)

Cybersecurity researchers have discovered a novel attack that employs stolen cloud credentials to target cloud-hosted large language model (LLM) services with the goal of selling access to other threat actors.

The attack technique has been codenamed **LLMjacking** by the Sysdig Threat Research Team.

"Once initial access was obtained, they exfiltrated cloud credentials and gained access to the cloud environment, where they attempted to access local LLM models hosted by cloud providers," security researcher Alessandro Brucato [said](https://sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack/). "In this instance, a local Claude (v2/v3) LLM model from Anthropic was targeted."

The intrusion pathway used to pull off the scheme entails breaching a system running a vulnerable version of the Laravel Framework (e.g., [CVE-2021-3129](https://thehackernews.com/2024/04/10-year-old-rubycarp-romanian-hacker.html)), followed by getting hold of Amazon Web Services (AWS) credentials to access the LLM services.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Among the tools used is an [open-source Python script](https://github.com/kingbased/keychecker) that checks and validates keys for various offerings from Anthropic, AWS Bedrock, Google Cloud Vertex AI, Mistral, and OpenAI, among others.

"No legitimate LLM queries were actually run during the verification phase," Brucato explained. "Instead, just enough was done to figure out what the credentials were capable of and any quotas."

The keychecker also has integration with another open-source tool called [oai-reverse-proxy](https://gitgud.io/khanon/oai-reverse-proxy) that functions as a reverse proxy server for LLM APIs, indicating that the threat actors are likely providing access to the compromised accounts without actually exposing the underlying credentials.

"If the attackers were gathering an inventory of useful credentials and wanted to sell access to the available LLM models, a reverse proxy like this could allow them to monetize their efforts," Brucato said.

Furthermore, the attackers have been observed querying logging settings in a likely attempt to sidestep detection when using the compromised credentials to run their prompts.

The development is a departure from attacks that focus on prompt injections and model poisoning, instead allowing attackers to monetize their access to the LLMs while the owner of the cloud account foots the bill without their knowledge or consent.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Sysdig said that an attack of this kind could rack up over $46,000 in LLM consumption costs per day for the victim.

"The use of LLM services can be expensive, depending on the model and the amount of tokens being fed to it," Brucato said. "By maximizing the quota limits, attackers can also block the compromised organization from using models legitimately, disrupting business operations."

Organizations are recommended to enable detailed logging and monitor cloud logs for suspicious or unauthorized activity, as well as ensure that effective vulnerability management processes are in place to prevent initial access.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Laravel Framework](https://thehackernews.com/search/label/Laravel%20Framework)[Large language model](https://thehackernews.com/search/label/Large%20language%20model)[LLMjacking](https://thehackernews.com/search/label/LLMjacking)[reverse engineering](https://thehackernews.com/search/label/reverse%20engineering)[threat detection](https://thehackernews.com/search/label/threat%20detection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Pack...