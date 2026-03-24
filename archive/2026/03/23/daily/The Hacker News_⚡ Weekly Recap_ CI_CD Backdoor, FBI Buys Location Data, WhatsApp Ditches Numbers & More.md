---
title: ⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers & More
url: https://thehackernews.com/2026/03/weekly-recap-cicd-backdoor-fbi-buys.html
source: The Hacker News
date: 2026-03-23
fetch_date: 2026-03-24T04:18:12.188233
---

# ⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers & More

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers & More](https://thehackernews.com/2026/03/weekly-recap-cicd-backdoor-fbi-buys.html)

**Ravie Lakshmanan**Mar 23, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe8A2RKkUN6BATGKH_48mi3J6DYVutxBllcmOiNl7N3xeqPx9sySaIFdxMxfIp5VQksSCBdRKtpNpiWUcTo5VNClmu6dbs6hoM9Ljx3QXAWEnAjKAG0Vc8JHLxGWfZkq3ORe4PgT-RgpBxhPnfMtr8UOhnjXToH-WOa6h3IVUM3HQqvgmWmMTPjKsqTkSN/s1700-e365/recap-bl.jpg)

Another week, another reminder that the internet is still a mess. Systems people thought were secure are being broken in simple ways, showing many still ignore basic advisories.

This edition covers a mix of issues: supply chain attacks hitting CI/CD setups, long-abused IoT devices being shut down, and exploits moving quickly from disclosure to real attacks. There are also new malware tricks showing attackers are becoming more patient and creative.

It’s a mix of old problems that never go away and new methods that are harder to detect. There are quiet state-backed activities, exposed data from open directories, growing mobile threats, and a steady stream of zero-days and rushed patches.

Grab a coffee, and at least skim the CVE list. Some of these are the kind you don’t want to discover after the damage is done.

## **⚡ Threat of the Week**

**[Trivy Vulnerability Scanner Breached in for Supply Chain Attack](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html)** — Attackers have [backdoored](https://labs.boostsecurity.io/articles/20-days-later-trivy-compromise-act-ii/) the widely used open-source Trivy vulnerability scanner, injecting credential-stealing malware into official releases and GitHub Actions used by thousands of CI/CD workflows. The breach has triggered a cascade of additional supply-chain compromises stemming from impacted projects and organizations not rotating their secrets, resulting in the distribution of a self-propagating worm referred to as CanisterWorm. Trivy, developed by Aqua Security, is one of the most widely used open-source vulnerability scanners, with over 32,000 GitHub stars and more than 100 million Docker Hub downloads. The Trivy compromise is the latest in a growing pattern of attacks targeting GitHub Actions and developers in general. GitHub [changed](https://github.blog/changelog/2025-11-07-actions-pull_request_target-and-environment-branch-protections-changes/) the default behavior of pull\_request\_target workflows in December 2025 to reduce the risk of exploitation.

[![BAS vs Automated Pentesting](data:image/png;base64... "BAS vs Automated Pentestingk")

## BAS vs Automated Pentesting: What Each Actually Covers (and Doesn't)

Most teams pick one without knowing what the other misses. This guide breaks down both by use case across blue, red, and purple teams so you can see where each fits and where the gaps are.](https://thehackernews.uk/breach-attack-guide-ar)
[Download Now ➝](https://thehackernews.uk/breach-attack-guide-ar)

## **🔔 Top News**

* **[DoJ Takes Down DDoS Botnets](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html)** — A cluster of IoT botnets behind some of the largest DDoS attacks ever recorded -- [AISURU](https://www.cloudflare.com/threat-intelligence/research/report/aisuru-botnet/), [Kimwolf](https://www.cloudflare.com/learning/ddos/glossary/aisuru-kimwolf-botnet/), JackSkid, and Mossad -- were wiped as part of a broad law enforcement operation. The botnets largely spread across routers, IP cameras, and digital video recorders that are often shipped with weak credentials and rarely patched. Authorities removed the command-and-control servers used to commandeer the infected nodes. Together, operators of the four botnets had amassed more than 3 million devices, which they then sold access to other criminal hackers, who then used them to target victims with DDoS attacks to knock websites and internet services offline or mask other illicit activity. Some of these DDoS attacks were aimed at U.S. Department of Defense systems and other high-value targets. No arrests were announced, but two suspects associated with AISURU/Kimwolf are said to be based in Canada and Germany. All four botnets disrupted by the operation are variants of Mirai, which had its source code leaked in 2016 and has served as the starting point for other botnets. The U.S. Justice Department said some victims of the DDoS attacks lost hundreds of thousands of dollars through remediation expenses or ransom demands from hackers who would only stop overloading websites for a price.
* **[Google Debuts New Advanced Flow for Sideloading on Android](https://thehackernews.com/2026/03/google-adds-24-hour-wait-for-unverified.html)** — Google's advanced flow for Android changes how apps from unverified developers are installed, adding friction to combat scams and malware. The feature is aimed at experienced users and allows sideloading through a one-time setup. The advanced flow adds a 24-hour delay and verification steps intended to disrupt coercive pressure and give users time to make decisions. It’s designed to address scenarios where attackers pressure individuals to install unsafe software and play on the urgency of the operation to push them to bypass security warnings and disable protections before they can pause or seek help.
* **[Critical Langflow Flaw Comes Under Attack](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html)** — A critical security flaw impacting Langflow has come under active exploitation within 20 hours of public disclosure, highlighting the speed at which threat actors weaponize newly published vulnerabilities. The security defect, tracked as CVE-2026-33017 (CVSS score: 9.3), is a case of missing authentication combined with code injection that could result in remote code execution. Cloud security firm Sysdig said that the attacks weaponize the vulnera...