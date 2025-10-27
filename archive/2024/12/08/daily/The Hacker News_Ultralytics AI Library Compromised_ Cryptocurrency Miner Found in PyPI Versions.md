---
title: Ultralytics AI Library Compromised: Cryptocurrency Miner Found in PyPI Versions
url: https://thehackernews.com/2024/12/ultralytics-ai-library-compromised.html
source: The Hacker News
date: 2024-12-08
fetch_date: 2025-10-06T19:38:47.661221
---

# Ultralytics AI Library Compromised: Cryptocurrency Miner Found in PyPI Versions

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

# [Ultralytics AI Library Compromised: Cryptocurrency Miner Found in PyPI Versions](https://thehackernews.com/2024/12/ultralytics-ai-library-compromised.html)

**Dec 07, 2024**Ravie LakshmananSupply Chain Attack / Cryptocurrency

[![Ultralytics AI Library](data:image/png;base64... "Ultralytics AI Library")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiwGzm-uhA-fUukarCR70p2AjVlLaDAqM808eTYqzsTkWrcmTUQy-GjyYzBlgVMjj2anUJWqcOsyFG_PUUucWzziAA0j49hTPGovuJsk29bvknPvFrWls74Th58D1fi0mjx9v2tc6vsEsdGT9XNTD_JAubQpWlmfx4in6a777xjMxF8uNy3ig4k-YeIWyz/s790-rw-e365/python.png)

In yet another software supply chain attack, it has come to light that two versions of a popular Python artificial intelligence (AI) library named [ultralytics](https://github.com/ultralytics/ultralytics) were compromised to deliver a cryptocurrency miner.

The versions, 8.3.41 and 8.3.42, [have since been removed](https://pypi.org/project/ultralytics/#history) from the Python Package Index (PyPI) repository. A subsequently [released version](https://github.com/ultralytics/ultralytics/releases/tag/v8.3.43) has introduced a security fix that "ensures secure publication workflow for the Ultralytics package."

The project maintainer, Glenn Jocher, confirmed on GitHub that the two versions were infected by malicious code injection in the PyPI deployment workflow after [reports](https://github.com/ultralytics/ultralytics/issues/18027) [emerged](https://github.com/ultralytics/ultralytics/issues/18030) that installing the library led to a [drastic spike in CPU usage](https://github.com/ltdrdata/ComfyUI-Impact-Pack/issues/843), a telltale sign of cryptocurrency mining.

The most notable aspect of the attack is that bad actors managed to compromise the build environment related to the project to insert unauthorized modifications after the completion of the code review step, thus leading to a discrepancy in the source code published to PyPI and the GitHub repository itself.

"In this case intrusion into the build environment was achieved by a more sophisticated vector, by exploiting a known GitHub Actions Script Injection," ReversingLabs' Karlo Zanki [said](https://www.reversinglabs.com/blog/compromised-ultralytics-pypi-package-delivers-crypto-coinminer), adding the issue in "ultralytics/actions" was [flagged](https://github.com/ultralytics/actions/security/advisories/GHSA-7x29-qqmq-v6qc) by security researcher [Adnan Khan](https://github.com/ultralytics/ultralytics/issues/18027#issuecomment-2521578169), according to an advisory released in August 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This could allow a threat actor to craft a malicious pull request and to enable the retrieval and execution of a payload on macOS and Linux systems. In this instance, the [pull](https://github.com/ultralytics/ultralytics/pull/18018) [requests](https://github.com/ultralytics/ultralytics/pull/18020) originated from a GitHub account named [openimbot](https://github.com/openimbot), which claims to be associated with the [OpenIM SDK](https://www.openim.io/en).

ComfyUI, which has Ultralytics as one of its dependencies, [said](https://blog.comfy.org/comfyui-statement-on-the-ultralytics-crypto-miner-situation/) it has updated ComfyUI manager to warn users if they are running one of the malicious versions. Users of the library are advised to update to the latest version.

"It seems that the malicious payload served was simply an XMRig miner, and that the malicious functionality was aimed at cryptocurrency mining," Zanki said. "But it is not hard to imagine what the potential impact and the damage could be if threat actors decided to plant more aggressive malware like backdoors or remote access trojans (RATs)."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Cryptomining](https://thehackernews.com/search/label/Cryptomining)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub](https://thehackernews.com/search/label/GitHub)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Mali...