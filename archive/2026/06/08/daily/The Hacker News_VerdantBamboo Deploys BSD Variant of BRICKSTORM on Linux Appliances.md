---
title: VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances
url: https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html
source: The Hacker News
date: 2026-06-08
fetch_date: 2026-06-09T06:03:51.228141
---

# VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances](https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html)

**Ravie Lakshmanan**Jun 08, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhni0Ay24Jcfz-LCxqQ8xD9rJais13OOnt5cfz9XtZY-4LzlGgyVY9S2Cu7V0Uo9JMjIxfyTMk8oOeaPHcIkkYnw4RMiLgYFuiS2CyHd9JAihJsC7SQ-wtm8K545YuACojNwKRfsYBXLWe8s3u1evEVjyGLI2WM9KwAYyWur_XrpPfQRF8s4CzXP8c_OU01/s1700-e365/chinese.jpg)

A China-nexus cyber espionage group has been observed deploying a BSD variant of a known backdoor called BRICKSTORM, as well as two other malware families codenamed PLENET (aka [GRIMBOLT](https://thehackernews.com/2026/02/dell-recoverpoint-for-vms-zero-day-cve.html)) and AGENTPSD to target Linux systems.

The activity has been attributed by Volexity to a threat cluster it tracks as **[VerdantBamboo](https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/)**, which it said [overlaps](https://thehackernews.com/2025/12/cisa-reports-prc-hackers-using.html) with hacking groups known as Clay Typhoon (Microsoft), UNC5221 (Google), and Warp Panda (CrowdStrike).

The cybersecurity company said it discovered the intrusion during an incident response engagement in September 2025, when it emerged that the adversary had compromised an unnamed victim's Egnyte Storage Sync system by exploiting a local privilege escalation flaw to deploy BRICKSTORM. The issue was addressed in Storage Sync [version 13.13](https://helpdesk.egnyte.com/hc/en-us/articles/43855328739469-Storage-Sync-V-13-13-Miscellaneous-Improvements), released in March 2026.

"The appliance had periodically been accessed by VerdantBamboo via IP addresses assigned through the victim organization's web SSL VPN," researchers Damien Cash, Paul Rascagneres, Steven Adair, and Tom Lancaster said in a technical report published last week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The threat actor used the malware's proxying capabilities deployed on the Storage Sync system, along with compromised credentials, to access the victim's Microsoft 365 (M365) environment."

It's assessed that these steps were undertaken to blend in with legitimate network traffic and evade Conditional Access policies, with the initial compromise occurring at least 18 months before.

Following the initial remediation, VerdantBamboo is said to have staged a return, breaching the same organization by using stolen administrative credentials to connect to the firewall, and then abusing that access to configure web SSL VPN access to the device, connect to other systems, and deploy additional malware to a Synology Network Attached Storage (NAS) appliance.

Further investigation has since uncovered that the threat actor had in fact compromised the victim organization's Managed Services Provider (MSP), specifically infecting its MSP's pfSense firewall with a BSD variant of BRICKSTORM around the same time the victim's Storage Sync system was also breached.

It's believed that the victim was compromised through the threat actor's breach of the MSP. The two malware families deployed to the NAS appliance over SSH are as follows -

* PLENET (aka GRIMBOLT), a cross-platform backdoor developed in .NET Core and a new version of BRICKSTORM compiled using native ahead-of-time (AOT) compilation. It supports interactive shell, remote command execution, file manipulation, and command-and-control (C2) server switching.
* AGENTPSD, a Python-based reverse shell that likely functions as a fallback in case the primary implant ceases to function

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

It's worth noting that the use of PLENET in the wild was reported by Google earlier this February in connection with attacks mounted by a suspected China-nexus threat cluster dubbed UNC6201 that exploited a vulnerability in Dell RecoverPoint for Virtual Machines (CVE-2026-22769, CVSS score: 10.0) as a zero-day since mid-2024.

"VerdantBamboo is a highly sophisticated threat actor that seeks to leverage a combination of living-off-the-land techniques and malware deployment on systems that traditionally do not or cannot run EDR software," Volexity said.

"This threat actor appears to have good knowledge of proprietary appliances, allowing them to deploy malware with customized persistence mechanisms. They also appear to have operational security discipline aimed at leveraging a limited number of domains and IP addresses per victim and setting up customized implant naming and persistence on a per-device basis."

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

[china](https://thehackernews.com/search/label/china), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [linux](https://thehackernews.com/search/label/linux), [Managed Service Provider](https://thehackernews.com/search/label/Managed%20Service%20Provider), [pfSense](https://thehackernews.com/search/label/pfSense)

⚡ Top Stories This Week

[![Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](dat...