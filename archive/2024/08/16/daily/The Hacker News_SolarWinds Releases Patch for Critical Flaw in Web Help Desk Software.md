---
title: SolarWinds Releases Patch for Critical Flaw in Web Help Desk Software
url: https://thehackernews.com/2024/08/solarwinds-releases-patch-for-critical.html
source: The Hacker News
date: 2024-08-16
fetch_date: 2025-10-06T18:07:00.487952
---

# SolarWinds Releases Patch for Critical Flaw in Web Help Desk Software

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

# [SolarWinds Releases Patch for Critical Flaw in Web Help Desk Software](https://thehackernews.com/2024/08/solarwinds-releases-patch-for-critical.html)

**Aug 15, 2024**Ravie LakshmananEnterprise Security / Vulnerability

[![SolarWinds](data:image/png;base64... "SolarWinds")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEYVoP_P0gUrw8z0mmk_7Gx6rTXSJO3w3Tn8B0iQ8iqQNGqIQZ2sRPcVXzlByfWSYNAlGHVPrhiF7u33fHLyJGnF1hAy4rQXy26rVwEUEW8HLOx4yUP9c5JitfL9b-BvydM9ip0-pmYTZyGkw8LTTMMbGK5bw4fkHJY38mNwXcYJ5N8HygxY1A0rOIAf0A/s790-rw-e365/lock.png)

SolarWinds has released patches to address a critical security vulnerability in its Web Help Desk software that could be exploited to execute arbitrary code on susceptible instances.

The flaw, tracked as CVE-2024-28986 (CVSS score: 9.8), has been described as a deserialization bug.

"SolarWinds Web Help Desk was found to be susceptible to a Java deserialization remote code execution vulnerability that, if exploited, would allow an attacker to run commands on the host machine," the company [said](https://www.solarwinds.com/trust-center/security-advisories/cve-2024-28986) in an advisory.

"While it was reported as an unauthenticated vulnerability, SolarWinds has been unable to reproduce it without authentication after thorough testing."

The flaw impacts all versions of SolarWinds Web Help Desk including and prior to 12.8.3. It has been addressed in [hotfix version 12.8.3 HF 1](https://support.solarwinds.com/SuccessCenter/s/article/WHD-12-8-3-Hotfix-1).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Palo Alto Networks patched a high-severity vulnerability affecting Cortex XSOAR that could result in command injection and code execution.

Assigned the CVE identifier CVE-2024-5914 (CVSS score: 7.0), the shortcoming impacts all versions of Cortex XSOAR CommonScripts before 1.12.33.

"A command injection issue in Palo Alto Networks Cortex XSOAR CommonScripts Pack allows an unauthenticated attacker to execute arbitrary commands within the context of an integration container," the company [said](https://security.paloaltonetworks.com/CVE-2024-5914).

"To be exposed, an integration must make use of the ScheduleGenericPolling or GenericPollingScheduledTask scripts from the CommonScripts pack."

Also addressed by Palo Alto Networks are two moderate-severity issues listed below -

* [CVE-2024-5915](https://security.paloaltonetworks.com/CVE-2024-5915) (CVSS score: 5.2) - A privilege escalation (PE) vulnerability in the GlobalProtect app on Windows devices that enables a local user to execute programs with elevated privileges

* [CVE-2024-5916](https://security.paloaltonetworks.com/CVE-2024-5916) (CVSS score: 6.0) - An information exposure vulnerability in PAN-OS software that enables a local system administrator to access secrets, passwords, and tokens of external systems

Users are recommended to update to the latest version to mitigate potential risks. As a precautionary measure, it's also advised to revoke the secrets, passwords, and tokens that are configured in PAN-OS firewalls after the upgrade.

### Update

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://www.cisa.gov/news-events/alerts/2024/08/15/cisa-adds-one-known-exploited-vulnerability-catalog) the SolarWinds flaw CVE-2024-28986 to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, based on evidence of active exploitation. Federal agencies are required to apply the fixes by September 5, 2024.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Information security](https://thehackernews.com/search/label/Information%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software patch](https://thehackernews.com/search/label/software%20patch)[Threat Mitigation](https://thehackernews.com/search/label/Threat%20Mitigation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackern...