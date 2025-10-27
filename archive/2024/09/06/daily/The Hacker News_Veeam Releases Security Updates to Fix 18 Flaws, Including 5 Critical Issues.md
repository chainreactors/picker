---
title: Veeam Releases Security Updates to Fix 18 Flaws, Including 5 Critical Issues
url: https://thehackernews.com/2024/09/veeam-releases-security-updates-to-fix.html
source: The Hacker News
date: 2024-09-06
fetch_date: 2025-10-06T18:31:42.920291
---

# Veeam Releases Security Updates to Fix 18 Flaws, Including 5 Critical Issues

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

# [Veeam Releases Security Updates to Fix 18 Flaws, Including 5 Critical Issues](https://thehackernews.com/2024/09/veeam-releases-security-updates-to-fix.html)

**Sep 05, 2024**Ravie LakshmananThreat Prevention / Software Security

[![Security Updates](data:image/png;base64... "Security Updates")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdip9IYP6cNKA_KdsebCvrAzTD5QUDAmcgfvIwbbOQzJO3VamggahgxDjt0bw7fERvVgy37xmNd9sjvWUclJZM0CpFJ60ML1efMsW4DGFyD-d_eHKBT8v3KNCqKDGqIRmqusB3Pyh8Q4cXD0UsyCq2wCG_XalalX_cqqCn5DZr2hTLoGHaEDvpWw00SEwk/s790-rw-e365/veeam.jpg)

Veeam has [shipped](https://www.veeam.com/kb4649) security updates to address a total of 18 security flaws impacting its software products, including five critical vulnerabilities that could result in remote code execution.

The list of shortcomings is below -

* **CVE-2024-40711 (CVSS score: 9.8)** - A vulnerability in Veeam Backup & Replication that allows unauthenticated remote code execution.

* **CVE-2024-42024 (CVSS score: 9.1)** - A vulnerability in Veeam ONE that enables an attacker in possession of the Agent service account credentials to perform remote code execution on the underlying machine

* **CVE-2024-42019 (CVSS score: 9.0)** - A vulnerability in Veeam ONE that allows an attacker to access the NTLM hash of the Veeam Reporter Service service account

* **CVE-2024-38650 (CVSS score: 9.9)** - A vulnerability in Veeam Service Provider Console (VPSC) that allows a low privileged attacker to access the NTLM hash of the service account on the server

* **CVE-2024-39714 (CVSS score: 9.9)** - A vulnerability in VPSC that permits a low-privileged user to upload arbitrary files to the server, resulting in remote code execution on the server

In addition, the September 2024 updates address 13 other high-severity flaws that could permit privilege escalation, multi-factor authentication (MFA) bypass, and execute code with elevated permissions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

All the issues have been addressed in the below versions -

* Veeam Backup & Replication 12.2 (build 12.2.0.334)
* Veeam Agent for Linux 6.2 (build 6.2.0.101)
* Veeam ONE v12.2 (build 12.2.0.4093)
* Veeam Service Provider Console v8.1 (build 8.1.0.21377)
* Veeam Backup for Nutanix AHV Plug-In v12.6.0.632
* Veeam Backup for Oracle Linux Virtualization Manager and Red Hat Virtualization Plug-In v12.5.0.299

With flaws in Veeam software Users becoming a [lucrative target](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html) for threat actors to serve ransomware, users are advised to update to the latest version as soon as possible to mitigate potential threats.

### Update

Cybersecurity firm Rapid7, in an analysis, [said](https://www.rapid7.com/blog/post/2024/09/09/etr-multiple-vulnerabilities-in-veeam-backup-and-replication/) more than 20% of its "incident response cases in 2024 so far have involved Veeam being accessed or exploited in some manner, typically once an adversary has already established a foothold in the target environment."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[ransomware](https://thehackernews.com/search/label/ransomware)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Risk management](https://thehackernews.com/search/label/Risk%20management)[software security](https://thehackernews.com/search/label/software%20security)[Threat Prevention](https://thehackernews.com/search/label/Threat%20Prevention)

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

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "S...