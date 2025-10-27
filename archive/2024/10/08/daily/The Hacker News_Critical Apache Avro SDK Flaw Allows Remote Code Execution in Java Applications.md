---
title: Critical Apache Avro SDK Flaw Allows Remote Code Execution in Java Applications
url: https://thehackernews.com/2024/10/critical-apache-avro-sdk-flaw-allows.html
source: The Hacker News
date: 2024-10-08
fetch_date: 2025-10-06T18:54:32.889041
---

# Critical Apache Avro SDK Flaw Allows Remote Code Execution in Java Applications

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

# [Critical Apache Avro SDK Flaw Allows Remote Code Execution in Java Applications](https://thehackernews.com/2024/10/critical-apache-avro-sdk-flaw-allows.html)

**Oct 07, 2024**Ravie LakshmananOpen Source / Software Security

[![Apache Avro SDK Flaw](data:image/png;base64... "Apache Avro SDK Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimvfO88LsksXxECevwu3KpOVTzDPzH0yZ2dsd5qG47U_IU8Lov_hiVgbpOmm79NNjJmFCb4T0FM9AlYhQmBsaIudeVjlY291XFW3SvR-OtoxSQFzNexfNsnmCzdzueLw0S7HusyfOaqHoWALzbXOGAerREQ9JR2HqxDYdcAPqLwjfRsTPNi_O_xed9MX6B/s790-rw-e365/apache-avro.png)

A critical security flaw has been disclosed in the Apache Avro Java Software Development Kit (SDK) that, if successfully exploited, could allow the execution of arbitrary code on susceptible instances.

The flaw, tracked as [CVE-2024-47561](https://github.com/advisories/GHSA-r7pg-v2c8-mfg3) (CVSS score: 9.3), impacts all versions of the software prior to 1.11.4.

"Schema parsing in the Java SDK of Apache Avro 1.11.3 and previous versions allows bad actors to execute arbitrary code," the project maintainers [said](https://lists.apache.org/thread/c2v7mhqnmq0jmbwxqq3r5jbj1xg43h5x) in an advisory released last week. "Users are recommended to upgrade to [version 1.11.4](https://avro.apache.org/blog/2024/09/22/avro-1.11.4/) or 1.12.0, which fix this issue."

Apache Avro, analogous to Google's Protocol Buffers ([protobuf](https://protobuf.dev)), is an open-source project that provides a language-neutral [data serialization framework](https://avro.apache.org/docs/) for large-scale data processing.

The Avro team notes that the vulnerability affects any application if it allows users to provide their own Avro schemas for parsing. Kostya Kortchinsky from the Databricks security team has been credited with discovering and reporting the security shortcoming.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As mitigations, it's recommended to sanitize schemas before parsing them and avoid parsing user-provided schemas.

"CVE-2024-47561 affects Apache Avro 1.11.3 and previous versions while de-serializing input received via avroAvro schema," Mayuresh Dani, Manager, manager of threat research at Qualys, said in a statement shared with The Hacker News.

"Processing such input from a threat actor leads to execution of code. Based on our threat intelligence reporting, no PoC is publicly available, but this vulnerability exists while processing packages via [ReflectData and SpecificData directives](https://issues.apache.org/jira/browse/AVRO-3985) and can also be exploited via Kafka."

"Since Apache Avro is an open-source project, it is used by many organizations. Based on publicly available data, a majority of these organizations are located in the U.S. This definitely has a lot of security implications if left unpatched, unsupervised and unprotected."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data security](https://thehackernews.com/search/label/data%20security)[Data Serialization](https://thehackernews.com/search/label/Data%20Serialization)[Java](https://thehackernews.com/search/label/Java)[Open Source](https://thehackernews.com/search/label/Open%20Source)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software development](https://thehackernews.com/search/label/software%20development)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](http...