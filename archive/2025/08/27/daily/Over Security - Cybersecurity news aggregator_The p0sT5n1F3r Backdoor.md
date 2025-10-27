---
title: The p0sT5n1F3r Backdoor
url: https://blog.kartone.ninja/the-p0st5n1f3r-backdoor/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:48:58.937053
---

# The p0sT5n1F3r Backdoor

[Kartone Infosec Blog](https://blog.kartone.ninja)

* [Home](https://blog.kartone.ninja/)
* [About me](https://blog.kartone.ninja/aboutme/)

By [Mario Ciccarelli](/author/mario/)
in
[malware analysis](https://blog.kartone.ninja/tag/malware-analysis/)
—
16 Oct 2019

# The p0sT5n1F3r Backdoor

P0sT5n1F3r, a stealthy Apache backdoor built to sniff HTTPS traffic. Undetected by anti-malware platforms, the module used RC4 encryption to hide its activities. Reverse engineering revealed the key, exposing a targeted payload designed to steal credit card data.

![The p0sT5n1F3r Backdoor](/content/images/size/w1200/2025/08/postsniffer.jpg)

How does a malicious backdoor designed to sniff sensitive HTTPS traffic go completely undetected?

During an IR case, we found and dissected a highly targeted malware sample, a custom Apache module we call`p0sT5n1F3r`.

This threat was specifically engineered for its target's environment and was rated 100% clean by all major security vendors due to its extensive use of custom encryption.

This report details the reverse engineering journey, from the initial static analysis to the critical breakthrough: cracking its custom RC4 encryption scheme. This discovery allowed us to unveil its true purpose—intercepting financial transaction data—and even uncover a hidden HTML interface used by the attackers.

Read the [full technical deep dive](https://blog.kartone.ninja/content/files/report.pdf) to learn how this threat was unmasked.

[Previous issue

#### WannaCry, two years later: a deep look into its code](/malware-analysis-a-wannacry-sample-found-in-the-wild-2/)

[Next issue

#### Project Sodinokibi](/project-sodinokibi/)

Kartone Infosec Blog © 2025

[Powered by Ghost](https://ghost.org/)