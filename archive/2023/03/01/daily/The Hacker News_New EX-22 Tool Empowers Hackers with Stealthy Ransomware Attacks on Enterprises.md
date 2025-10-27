---
title: New EX-22 Tool Empowers Hackers with Stealthy Ransomware Attacks on Enterprises
url: https://thehackernews.com/2023/02/new-ex-22-tool-empowers-hackers-with.html
source: The Hacker News
date: 2023-03-01
fetch_date: 2025-10-04T08:23:26.820123
---

# New EX-22 Tool Empowers Hackers with Stealthy Ransomware Attacks on Enterprises

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

# [New EX-22 Tool Empowers Hackers with Stealthy Ransomware Attacks on Enterprises](https://thehackernews.com/2023/02/new-ex-22-tool-empowers-hackers-with.html)

**Feb 28, 2023**Ravie LakshmananRansomware / Malware

[![EXFILTRATOR-22](data:image/png;base64... "EXFILTRATOR-22")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggVSva7AM9PsLolqeklSUqnzACpwTWcqJcLoZhkrxypwPPHCShvWRScQI2kAQV_0TynXPUlv2iHNdj-Y7sP4d-eImc5pJ3EWB6w08QPz6A6sRpBZZeAvT6ofrRBJdZ5waNqHVu26NF26vb65lbH0RZgZaau7tJDwehLGfTXZaCCxLhx6Z9oLlaU-vS/s790-rw-e365/post.png)

A new post-exploitation framework called EXFILTRATOR-22 (aka EX-22) has emerged in the wild with the goal of deploying ransomware within enterprise networks while flying under the radar.

"It comes with a wide range of capabilities, making post-exploitation a cakewalk for anyone purchasing the tool," CYFIRMA [said](https://www.cyfirma.com/outofband/exfiltrator-22-an-emerging-post-exploitation-framework/) in a new report.

Some of the notable features include establishing a reverse shell with elevated privileges, uploading and downloading files, logging keystrokes, launching ransomware to encrypt files, and starting a live VNC (Virtual Network Computing) session for real-time access.

It's also equipped to persist after system reboots, perform lateral movement via a worm, view running processes, generate cryptographic hashes of files, and extract authentication tokens.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity firm assessed with moderate confidence that threat actors responsible for creating the malware are operating from North, East, or Southeast Asia and are likely former affiliates of the [LockBit ransomware](https://thehackernews.com/2022/11/amadey-bot-spotted-deploying-lockbit-30.html) enterprise.

Advertised as a fully undetectable malware on Telegram and YouTube, EX-22 is offered for $1,000 a month or $5,000 for lifetime access. Criminal actors purchasing the toolkit are provided a login panel to access the EX-22 server and remotely control the malware.

[![post-exploitation framework](data:image/png;base64... "post-exploitation framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4p3lX-cBfqCo_45Gku2gdasAJYyjPWL1xS9qIwi8Np39lalYyaBitQQBpfyeE_7aZCaVIfX__cP3D9KxGW3B18xQL-HX4Maadw5DTfcYuueiugxOc1-5_YO7POIHCqPTw_UB67yNCBHlsZ9Ek2xy_GW1GUineOvWEKcNcKAh0Ju2gKf0sV2NvRg-c/s790-rw-e365/EX-22.png)

Since its first appearance on November 27, 2022, the malware authors have continuously iterated the toolkit with new features, indicating active development work.

The connections to LockBit 3.0 arise from technical and infrastructure overlaps, with both malware families utilizing the same [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting) mechanism for hiding command-and-control (C2) traffic.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The post-exploitation-framework-as-a-service (PEFaaS) model is the latest tool available for adversaries looking to maintain covert access to compromised devices over an extended period of time.

It also joins other frameworks like [Manjusaka](https://thehackernews.com/2022/08/chinese-hackers-using-new-manjusaka.html) and [Alchimist](https://thehackernews.com/2022/10/new-chinese-malware-attack-framework.html) as well as [legitimate and open source alternatives](https://thehackernews.com/2023/02/threat-actors-adopt-havoc-framework-for.html) such as Cobalt Strike, Metasploit, Sliver, Empire, Brute Ratel, and Havoc that have been co-opted for malicious ends.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Ransoware](https://thehackernews.com/search/label/Ransoware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target A...