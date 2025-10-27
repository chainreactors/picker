---
title: New ‘Plague’ PAM Backdoor Exposes Critical Linux Systems to Silent Credential Theft
url: https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html
source: The Hacker News
date: 2025-08-05
fetch_date: 2025-10-07T00:51:16.046764
---

# New ‘Plague’ PAM Backdoor Exposes Critical Linux Systems to Silent Credential Theft

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

# [New 'Plague' PAM Backdoor Exposes Critical Linux Systems to Silent Credential Theft](https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html)

**Aug 04, 2025**Ravie LakshmananThreat Detection / SSH Security

[![Linux Malware](data:image/png;base64... "Linux Malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiziSnhw1qNzQPj39V2sFAPQgt6kisCM8X5iTIaQMNFqsOamClZ5DoR57A_hinmlCs1XfTSWBqI-AUY0_KeNXvAgmzWJqxGXe6WWVHjHuH0z0Q-SgHOL9uYctIUbGshfH9F3cK0MvEbrTe9PsaZdnjZgbcygEaIN-ReR5A0esrVRO2RMT_Jo5lZinjI6-5C/s790-rw-e365/linux-malware.jpg)

Cybersecurity researchers have flagged a previously undocumented Linux backdoor dubbed **Plague** that has managed to evade detection for a year.

"The implant is built as a malicious [PAM](https://www.redhat.com/en/blog/pluggable-authentication-modules-pam) (Pluggable Authentication Module), enabling attackers to silently bypass system authentication and gain persistent SSH access," Nextron Systems researcher Pierre-Henri Pezier [said](https://www.nextron-systems.com/2025/08/01/plague-a-newly-discovered-pam-based-backdoor-for-linux/).

Pluggable Authentication Modules refers to a suite of shared libraries used to manage user authentication to applications and services in Linux and UNIX-based systems.

Given that PAM modules are loaded into privileged authentication processes, a rogue PAM can [enable](https://www.nextron-systems.com/2025/05/30/stealth-in-100-lines-analyzing-pam-backdoors-in-linux/) theft of user credentials, bypass authentication checks, and remain undetected by security tools.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity company said it uncovered multiple Plague artifacts uploaded to VirusTotal since July 29, 2024, with none of them detected by antimalware engines as malicious. What's more, the presence of several samples signals active development of the malware by the unknown threat actors behind it.

Plague boasts of four prominent features: Static credentials to allow covert access, resist analysis and reverse engineering using anti-debugging and string obfuscation; and enhanced stealth by erasing evidence of an SSH session.

This, in turn, is accomplished by unsetting environment variables such as [SSH\_CONNECTION and SSH\_CLIENT](https://en.wikibooks.org/wiki/OpenSSH/Client_Applications) using unsetenv, and redirecting [HISTFILE](https://www.redhat.com/en/blog/history-command) to /dev/null to prevent shell command logging, in order to avoid leaving an audit trail.

"Plague integrates deeply into the authentication stack, survives system updates, and leaves almost no forensic traces," Pezier noted. "Combined with layered obfuscation and environment tampering, this makes it exceptionally hard to detect using traditional tools."

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

[Antivirus](https://thehackernews.com/search/label/Antivirus)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cyber Threat Intelligence](https://thehackernews.com/search/label/cyber%20Threat%20Intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[Nextron Systems](https://thehackernews.com/search/label/Nextron%20Systems)[reverse engineering](https://thehackernews.com/search/label/reverse%20engineering)[ssh security](https://thehackernews.com/search/label/ssh%20security)[threat detection](https://thehackernews.com/search/label/threat%20detection)

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

[![⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More")

⚡ Weekl...