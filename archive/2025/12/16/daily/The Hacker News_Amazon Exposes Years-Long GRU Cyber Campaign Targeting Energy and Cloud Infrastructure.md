---
title: Amazon Exposes Years-Long GRU Cyber Campaign Targeting Energy and Cloud Infrastructure
url: https://thehackernews.com/2025/12/amazon-exposes-years-long-gru-cyber.html
source: The Hacker News
date: 2025-12-16
fetch_date: 2025-12-17T03:20:28.125938
---

# Amazon Exposes Years-Long GRU Cyber Campaign Targeting Energy and Cloud Infrastructure

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Amazon Exposes Years-Long GRU Cyber Campaign Targeting Energy and Cloud Infrastructure](https://thehackernews.com/2025/12/amazon-exposes-years-long-gru-cyber.html)

**Dec 16, 2025**Ravie LakshmananCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmP5wc4kQ_fstR7DVyxpp7nwoP36IRuDO6oBSyghPEx9VCjLCy2LPOoIYBHvfUELKpnhUQTWFtfCW8RiceJj5qgDVJpptVCfGNA9eeOi0vvbPCX9FFxF-kcTRnZN49Gqw0x71mloL7e2gN-I0lW0pFIkttwupJhJp5LMWc94ozebd-Yu9k-b8CUpJvFDpY/s790-rw-e365/russian.gif)

Amazon's threat intelligence team has [disclosed](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-russian-cyber-threat-group-targeting-western-critical-infrastructure/) details of a "years-long" Russian state-sponsored campaign that targeted Western critical infrastructure between 2021 and 2025.

Targets of the campaign included energy sector organizations across Western nations, critical infrastructure providers in North America and Europe, and entities with cloud-hosted network infrastructure. The activity has been attributed with high confidence to Russia's Main Intelligence Directorate (GRU), citing infrastructure overlaps with [APT44](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html), which is also known as FROZENBARENTS, Sandworm, Seashell Blizzard, and Voodoo Bear.

The activity is notable for using as initial access vectors misconfigured customer network edge devices with exposed management interfaces, as N-day and zero-day vulnerability exploitation activity declined over the time period – indicative of a shift in attacks aimed at critical infrastructure, the tech giant said.

"This tactical adaptation enables the same operational outcomes, credential harvesting, and lateral movement into victim organizations' online services and infrastructure, while reducing the actor's exposure and resource expenditure," CJ Moses, Chief Information Security Officer (CISO) of Amazon Integrated Security, said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The attacks have been found to leverage the following vulnerabilities and tactics over the course of five years -

* 2021-2022 - Exploitation of WatchGuard Firebox and XTM flaw ([CVE-2022-26318](https://www.assetnote.io/resources/research/diving-deeper-into-watchguard-pre-auth-rce-cve-2022-26318)) and targeting of misconfigured edge network devices
* 2022-2023 - Exploitation of Atlassian Confluence flaws ([CVE-2021-26084](https://thehackernews.com/2021/09/us-cyber-command-warns-of-ongoing.html) and [CVE-2023-22518](https://thehackernews.com/2023/11/alert-effluence-backdoor-persists.html)) and continued targeting of misconfigured edge network devices
* 2024 - Exploitation of Veeam flaw ([CVE-2023-27532](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html)) and continued targeting of misconfigured edge network devices
* 2025 - Sustained targeting of misconfigured edge network devices

The intrusion activity, per Amazon, singled out enterprise routers and routing infrastructure, VPN concentrators and remote access gateways, network management appliances, collaboration and wiki platforms, and cloud-based project management systems.

These efforts are likely designed to facilitate credential harvesting at scale, given the threat actor's ability to position themselves strategically on the network edge to intercept sensitive information in transit. Telemetry data has also uncovered what has been described as coordinated attempts aimed at misconfigured customer network edge devices hosted on Amazon Web Services (AWS) infrastructure.

"Network connection analysis shows actor-controlled IP addresses establishing persistent connections to compromised EC2 instances operating customers' network appliance software," Moses said. "Analysis revealed persistent connections consistent with interactive access and data retrieval across multiple affected instances."

In addition, Amazon said it observed credential replay attacks against victim organizations' online services as part of attempts to obtain a deeper foothold into targeted networks. Although these attempts are assessed to be unsuccessful, they lend weight to the aforementioned hypothesis that the adversary is grabbing credentials from compromised customer network infrastructure for follow-on attacks.

The entire attack plays out as follows -

* Compromise the customer network edge device hosted on AWS
* Leverage native packet capture capability
* Gather credentials from intercepted traffic
* Replay credentials against the victim organizations' online services and infrastructure
* Establish persistent access for lateral movement

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The credential replay operations have targeted energy, technology/cloud services, and telecom service providers across North America, Western and Eastern Europe, and the Middle East.

"The targeting demonstrates sustained focus on the energy sector supply chain, including both direct operators and third-party service providers with access to critical infrastructure networks," Moses noted.

Interestingly, the intrusion set also shares [infrastructure overlaps](https://github.com/bitdefender/malware-ioc/blob/master/2025_11_04-curlycomrades-iocs.csv) (91.99.25[.]54) with another cluster tracked by Bitdefender under the name [Curly COMrades](https://thehackernews.com/2025/11/hackers-weaponize-windows-hyper-v-to.html), which is believed to be operating with interests that are aligned with Russia since late 2023. This has raised the possibility that the two clusters may represent complementary operations within a broader campaign undertaken by GRU.

"This potential operational division, where one cluster focuses on network access and initial compromise while another handles host-based persistence and evasion, aligns with GRU operational patterns of specialized subclusters supporting broader campaign objectives...