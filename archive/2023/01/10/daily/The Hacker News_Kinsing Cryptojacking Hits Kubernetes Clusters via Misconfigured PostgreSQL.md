---
title: Kinsing Cryptojacking Hits Kubernetes Clusters via Misconfigured PostgreSQL
url: https://thehackernews.com/2023/01/kinsing-cryptojacking-hits-kubernetes.html
source: The Hacker News
date: 2023-01-10
fetch_date: 2025-10-04T03:28:21.516739
---

# Kinsing Cryptojacking Hits Kubernetes Clusters via Misconfigured PostgreSQL

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

# [Kinsing Crypto Malware Hits Kubernetes Clusters via Misconfigured PostgreSQL](https://thehackernews.com/2023/01/kinsing-cryptojacking-hits-kubernetes.html)

**Jan 09, 2023**Ravie LakshmananKubernetes / Cryptojacking

[![Kinsing Cryptojacking](data:image/png;base64... "Kinsing Cryptojacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipp97ofle-w8JdZjotEsuSYpK7tXS-MgqyuPdIEnwmnzIn8s28Bw8yRtVlR8tR0SM38euM9nH84aLDWftrfCmSK-mN8QrXJPEWUButPsXrsUtt9xXUZ-1X1oY1yxwZK9AjjJDFYkcjpQqdJRIMlQ9QmbF6fRqSsqDyBVKVMnRGlwr5l8Ov5QC9I86T/s790-rw-e365/bitcoing.png)

The threat actors behind the **Kinsing** cryptojacking operation have been spotted exploiting misconfigured and exposed PostgreSQL servers to obtain initial access to Kubernetes environments.

A second initial access vector technique entails the use of vulnerable images, Sunders Bruskin, security researcher at Microsoft Defender for Cloud, [said](https://techcommunity.microsoft.com/t5/microsoft-defender-for-cloud/initial-access-techniques-in-kubernetes-environments-used-by/ba-p/3697975) in a report last week.

Kinsing has a [storied history](https://thehackernews.com/2022/09/hackers-targeting-weblogic-servers-and.html) of targeting [containerized environments](https://www.trendmicro.com/en_my/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html), often leveraging misconfigured open Docker daemon API ports as well as abusing newly disclosed exploits to drop cryptocurrency mining software.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The threat actor, in the past, has also been discovered [employing a rootkit](https://www.trendmicro.com/en_us/research/20/k/analysis-of-kinsing-malwares-use-of-rootkit.html) to hide its presence, in addition to terminating and uninstalling competing resource-intensive services and processes.

Now according to Microsoft, misconfigurations in [PostgreSQL servers](https://unit42.paloaltonetworks.com/pgminer-postgresql-cryptocurrency-mining-botnet/) have been co-opted by the Kinsing actor to gain an initial foothold, with the company observing a "large amount of clusters" infected in this manner.

[![Kinsing Cryptojacking Attacks](data:image/png;base64... "Kinsing Cryptojacking Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUmil_Dxfy8CmuoeYsBibm8C09UnnUXGO9U3tbrNgOf7VLTel5cTdWzryc4bAjs8Jz6SnZgMtn5vpEIKlzfP3NEf1BJfj7IrWQGYsJdYNNf7yFHInv8tBUfEqflS3o2bu1SxyRKmpxxxC2CFa4utf8f6KnEpnAO9UfVnrr4Sqolzy_zO2lesaFtYA5/s790-rw-e365/CLUSTER.png)

The misconfiguration relates to a [trust authentication setting](https://www.postgresql.org/docs/current/auth-trust.html), which could be abused to connect to the servers sans any authentication and achieve code execution should the option be set up to accept connections from any IP address.

"In general, allowing access to a broad range of IP addresses is exposing the PostgreSQL container to a potential threat," Bruskin explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The alternative attack vector targets servers with vulnerable versions of PHPUnit, Liferay, WebLogic, and Wordpress that are susceptible to remote code execution in order to run malicious payloads.

What's more, a recent "widespread campaign" involved the attackers scanning for open [default WebLogic port 7001](https://docs.oracle.com/middleware/1213/core/ASADM/portnums.htm#ASADM432), and if found, executing a shell command to launch the malware.

"Exposing the cluster to the Internet without proper security measures can leave it open to attack from external sources," Bruskin said. "In addition, attackers can gain access to the cluster by taking advantage of known vulnerabilities in images."

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

[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[Docker](https://thehackernews.com/search/label/Docker)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[PostgreSQL](https://thehackernews.com/search/label/PostgreSQL)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 ...