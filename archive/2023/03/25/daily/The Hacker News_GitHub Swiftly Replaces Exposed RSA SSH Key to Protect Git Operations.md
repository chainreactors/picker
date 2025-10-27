---
title: GitHub Swiftly Replaces Exposed RSA SSH Key to Protect Git Operations
url: https://thehackernews.com/2023/03/github-swiftly-replaces-exposed-rsa-ssh.html
source: The Hacker News
date: 2023-03-25
fetch_date: 2025-10-04T10:40:20.059718
---

# GitHub Swiftly Replaces Exposed RSA SSH Key to Protect Git Operations

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

# [GitHub Swiftly Replaces Exposed RSA SSH Key to Protect Git Operations](https://thehackernews.com/2023/03/github-swiftly-replaces-exposed-rsa-ssh.html)

**Mar 24, 2023**Ravie LakshmananCloud Security / Programming

[![GitHub](data:image/png;base64... "GitHub")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk3OKasXJGY_C-awuyFiwivTCjDnDkQLWfk4bkADICpmvUaA28fu-XABcQRcIDkW92dIN_yFx9O48LjT6eymeuNqsmNALBcTaXMIvUbiz87yMkRQ6kQsgqhKpSkxiDx1Vlefc3e3rS1juMcrbRfQ_k5hDFDK9jNAyks6fUHFwYNfUNJWtVlCkRoYsB/s790-rw-e365/github.png)

Cloud-based repository hosting service GitHub said it took the step of replacing its RSA SSH host key used to secure Git operations "out of an abundance of caution" after it was briefly exposed in a public repository.

The activity, which was carried out at 05:00 UTC on March 24, 2023, is said to have been undertaken as a measure to prevent any bad actor from impersonating the service or eavesdropping on users' operations over SSH.

"This key does not grant access to GitHub's infrastructure or customer data," Mike Hanley, chief security officer and SVP of engineering at GitHub, [said](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/) in a post. "This change only impacts Git operations over SSH using RSA."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The move does not impact Web traffic to GitHub.com and Git operations performed via HTTPS. No change is required for ECDSA or Ed25519 users.

The Microsoft-owned company said there is no evidence that the exposed SSH private key was exploited by adversaries. It did not disclose how long the secret was exposed.

It further emphasized that the "issue was not the result of a compromise of any GitHub systems or customer information." It blamed it on an "inadvertent publishing of private information."

It also noted GitHub Actions users may see failed workflow runs if they are using [actions/checkout](https://github.com/actions/checkout) with the ssh-key option, adding it's in the process of updating the action across all tags.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes nearly two months after GitHub [revealed](https://thehackernews.com/2023/01/github-breach-hackers-stole-code.html) that unknown threat actors managed to exfiltrate encrypted code signing certificates pertaining to some versions of GitHub Desktop for Mac and Atom apps.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[GitHub](https://thehackernews.com/search/label/GitHub)[source code hosting](https://thehackernews.com/search/label/source%20code%20hosting)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware")

Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.html)

[![Urgent: Cisco ASA Zero-Day Duo Under Attack; CISA Triggers Emergency Mitigation Directive](data:image/svg+xml;base64... "Urgent: Cisco ASA Zero-Day Duo Under At...