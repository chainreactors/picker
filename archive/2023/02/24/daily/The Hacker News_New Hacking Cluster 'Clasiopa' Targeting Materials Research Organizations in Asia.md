---
title: New Hacking Cluster 'Clasiopa' Targeting Materials Research Organizations in Asia
url: https://thehackernews.com/2023/02/new-hacking-cluster-clasiopa-targeting.html
source: The Hacker News
date: 2023-02-24
fetch_date: 2025-10-04T07:59:54.068969
---

# New Hacking Cluster 'Clasiopa' Targeting Materials Research Organizations in Asia

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

# [New Hacking Cluster 'Clasiopa' Targeting Materials Research Organizations in Asia](https://thehackernews.com/2023/02/new-hacking-cluster-clasiopa-targeting.html)

**Feb 23, 2023**Ravie LakshmananMalware / Threat Intel

[![Hacking](data:image/png;base64... "Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhM6xi9ZZf_nOMmDWmMmM9mSnhwF9qJA6-CeKN76zzjiMD_Ar1KF-b23PRNxm9lL6SdPmSXcjCXWFucjuft2E2C3aqmmXug6k0WbcNvfgJLEaRB5GStYAOYn5u7TdN6RVN74QwRqtgIH_ZkDqMADYxPWtwZu9psFYlfRs9MJddJ13lJ_vxN2LMBJyML/s790-rw-e365/Materials-Research.png)

Materials research organizations in Asia have been targeted by a previously unknown threat actor using a distinct set of tools.

Symantec, by Broadcom Software, is tracking the cluster under the moniker **Clasiopa**. The origins of the hacking group and its affiliations are currently unknown, but there are hints that suggest the adversary could have ties to India.

This includes references to "SAPTARISHI-ATHARVAN-101" in a custom backdoor and the use of the password "iloveindea1998^\_^" for a ZIP archive.

It's worth noting that [Saptarishi](https://en.wikipedia.org/wiki/Saptarishi), meaning "Seven sages" in Sanskrit, refers to a group of seers who are revered in Hindu literature. [Atharvan](https://en.wikipedia.org/wiki/Atharvan) was an ancient Hindu priest and is believed to have co-authored one of the four [Vedas](https://en.wikipedia.org/wiki/Vedas), a collection of religious scriptures in Hinduism.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"While these details could suggest that the group is based in India, it is also quite likely that the information was planted as false flags, with the password in particular seeming to be an overly obvious clue," Symantec said in a [report](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clasiopa-materials-research) shared with The Hacker News.

Also unclear is the exact means of initial access, although it's suspected that the cyber incursions take advantage of brute-force attacks on internet-facing servers.

Some of the key hallmarks of the intrusions involve clearing system monitor (Sysmon) and event logs as well as the deployment of the multiple backdoors, such as Atharvan and a modified version of the open source [Lilith RAT](https://github.com/werkamsus/Lilith), to gather and exfiltrate sensitive information.

Atharvan is further capable of contacting a hard-coded command-and-control (C&C) server to retrieve files and run arbitrary executables on the infected host.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The hard-coded C&C addresses seen in one of the samples analyzed to date was for Amazon AWS South Korea (Seoul) region, which is not a common location for C&C infrastructure," Symantec pointed out.

Judging by its tools and tactics, the group's chief motive appears to be achieving persistent access to victim machines without being detected and carrying out information theft.

The disclosure comes a day after the cybersecurity firm took the wraps off another hitherto undocumented threat group known as [Hydrochasma](https://thehackernews.com/2023/02/hydrochasma-new-threat-actor-targets.html) that has been observed targeting shipping companies and medical laboratories in Asia.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Indian Hackers](https://thehackernews.com/search/label/Indian%20Hackers)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.c...