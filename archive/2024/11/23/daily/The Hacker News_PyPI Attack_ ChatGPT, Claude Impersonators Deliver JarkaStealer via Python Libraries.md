---
title: PyPI Attack: ChatGPT, Claude Impersonators Deliver JarkaStealer via Python Libraries
url: https://thehackernews.com/2024/11/pypi-attack-chatgpt-claude.html
source: The Hacker News
date: 2024-11-23
fetch_date: 2025-10-06T19:26:13.659868
---

# PyPI Attack: ChatGPT, Claude Impersonators Deliver JarkaStealer via Python Libraries

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

# [PyPI Attack: ChatGPT, Claude Impersonators Deliver JarkaStealer via Python Libraries](https://thehackernews.com/2024/11/pypi-attack-chatgpt-claude.html)

**Nov 22, 2024**Ravie LakshmananArtificial Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIzfbdPBufv0m7DyPt8LB2DXujgsQ8jhPvljd47O3dtQQQC9bdU4hEgz0H-jkBdkEz0OtSq1X25TAmPmZwZzSPc-c5NVeJZW2J77T2UpolvWzkQ46kP1-6DlLxGWp_vIOJtbEUCUPRjY_q633U8GGAKXGD8HwjDQX8HjtVNQJiddz7mT6p6VJZQl1Ehymp/s790-rw-e365/code.png)

Cybersecurity researchers have discovered two malicious packages uploaded to the Python Package Index (PyPI) repository that impersonated popular artificial intelligence (AI) models like OpenAI ChatGPT and Anthropic Claude to deliver an information stealer called JarkaStealer.

The packages, named [gptplus](https://clickpy.clickhouse.com/dashboard/gptplus) and [claudeai-eng](https://clickpy.clickhouse.com/dashboard/claudeai-eng), were uploaded by a user named "[Xeroline](https://pypi.org/user/Xeroline/)" in November 2023, attracting 1,748 and 1,826 downloads, respectively. Both libraries are no longer available for download from PyPI.

"The malicious packages were uploaded to the repository by one author and, in fact, differed from each other only in name and description," Kaspersky [said](https://www.kaspersky.com/blog/jarkastealer-in-pypi-packages/52640/) in a post.

The packages purported to offer a way to access GPT-4 Turbo API and Claude AI API, but harbored malicious code that initiated the deployment of the malware upon installation.

Specifically, the "\_\_init\_\_.py" file in these packages contained Base64-encoded data that incorporated code to download a Java archive file ("JavaUpdater.jar") from a GitHub repository ("github[.]com/imystorage/storage"). It also downloads the Java Runtime Environment (JRE) from a Dropbox URL if Java is not already installed on the host, before running the JAR file.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The JAR file is a Java-based information stealer called JarkaStealer that can steal a wide range of sensitive information, including web browser data, system data, screenshots, and session tokens from various applications like Telegram, Discord, and Steam.

In the final step, the collected information is archived, transmitted to the attacker's server, and then deleted from the victim's machine. JarkaStealer has been found to be offered under a malware-as-a-service (MaaS) model via a [Telegram channel](https://t.me/jarkasteal) for anywhere between $20 and $50, although its source code has been [leaked on GitHub](https://github.com/Loremas1er/JarkaSteal).

Statistics from ClickPy show that the packages were downloaded mainly by users located in the U.S., China, India, France, Germany, and Russia as part of the year-long supply chain attack campaign.

"This discovery underscores the persistent risks of software supply chain attacks and highlights the critical need for vigilance when integrating open-source components into development processes," Kaspersky researcher Leonid Bezvershenko [said](https://www.kaspersky.com/about/press-releases/kaspersky-uncovers-year-long-pypi-supply-chain-attack-using-ai-chatbot-tools-as-lure).

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

[Anthropic](https://thehackernews.com/search/label/Anthropic)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Information security](https://thehackernews.com/search/label/Information%20security)[Malware](https://thehackernews.com/search/label/Malware)[OpenAI](https://thehackernews.com/search/label/OpenAI)[Python](https://thehackernews.com/search/label/Python)[Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser In...