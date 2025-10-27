---
title: Malicious PyPI Package Posing as Solana Tool Stole Source Code in 761 Downloads
url: https://thehackernews.com/2025/05/malicious-pypi-package-posing-as-solana.html
source: The Hacker News
date: 2025-05-14
fetch_date: 2025-10-06T22:31:24.695718
---

# Malicious PyPI Package Posing as Solana Tool Stole Source Code in 761 Downloads

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

# [Malicious PyPI Package Posing as Solana Tool Stole Source Code in 761 Downloads](https://thehackernews.com/2025/05/malicious-pypi-package-posing-as-solana.html)

**May 13, 2025**Ravie LakshmananSupply Chain Attack / Blockchain

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2azRPxhef9xvwAxh5fwqM9gLcDcz7-fvYnAUYVfWc8KvYiN7TrPaMCieMW82gAsFLQ63J8V9EnhbEAGogUTv6IVBgf5Csz5AWpv-Inh5EklGePPkSGX86LDt4cD3GVeDAq1V61Cjs8nI_t0huDtSoAPScEy42kS2TQ309bYts2dOpENZV2ZOSxBK29KGk/s790-rw-e365/pip.jpg)

Cybersecurity researchers have discovered a malicious package on the Python Package Index (PyPI) repository that purports to be an application related to the Solana blockchain, but contains malicious functionality to steal source code and developer secrets.

The package, named solana-token, is no longer available for download from PyPI, but not before it was [downloaded 761 times](https://pepy.tech/projects/solana-token). It was [first published](https://secure.software/pypi/packages/solana-token/versions) to PyPI in early April 2024, albeit with an entirely different version numbering scheme.

"When installed, the malicious package attempts to exfiltrate source code and developer secrets from the developer's machine to a hard-coded IP address," ReversingLabs researcher Karlo Zanki [said](https://www.reversinglabs.com/blog/same-name-different-hack-pypi-package-targets-solana-developers) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In particular, the package is designed to copy and exfiltrate the source code contained in all the files in the Python execution stack under the guise of a blockchain function named "register\_node()."

This unusual behavior suggests that the attackers are looking to exfiltrate sensitive crypto-related secrets that may be hard-coded in the early stages of writing a program incorporating the malicious function in question.

It's believed that developers looking to create their own blockchains were the likely targets of the threat actors behind the package. This assessment is based on the package name and the functions built into it.

[![Malicious PyPI Package](data:image/png;base64... "Malicious PyPI Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmDVcpjfITy6B2MG4UMJ3aL65eOFkQRb2rhSnAQLMgJO1hyOjrNDn9p4VJsvdTp1PWowdu4QwHFdK1f0BeujQBzAKKq_MhQrZean6gHvj3pBUQPnwbPIemSrdvA9SY3P8M1CpKXRS-jUswLEzsqhNXaE9MmbOFt-ff8uW7aXXFndcMUMARs6c-hQgWDV_C/s790-rw-e365/code.png)

The exact method by which the package may have been distributed to users is currently not known, although it's likely to have been promoted on developer-focused platforms.

If anything, the discovery underscores the fact that cryptocurrency continues to be one of the most popular targets for supply chain threat actors, necessitating that developers take steps to scrutinize every package before using it.

"Development teams need to aggressively monitor for suspicious activity or unexplained changes within both open source and commercial, third-party software modules," Zanki said. "By stopping malicious code before it is allowed to penetrate secure development environments, teams can prevent the kind of destructive supply chain attacks."

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[Code Theft](https://thehackernews.com/search/label/Code%20Theft)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[Solana](https://thehackernews.com/search/label/Solana)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexi...