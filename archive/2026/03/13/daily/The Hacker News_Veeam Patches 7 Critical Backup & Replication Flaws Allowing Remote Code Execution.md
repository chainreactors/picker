---
title: Veeam Patches 7 Critical Backup & Replication Flaws Allowing Remote Code Execution
url: https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html
source: The Hacker News
date: 2026-03-13
fetch_date: 2026-03-14T04:14:27.852203
---

# Veeam Patches 7 Critical Backup & Replication Flaws Allowing Remote Code Execution

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

# [Veeam Patches 7 Critical Backup & Replication Flaws Allowing Remote Code Execution](https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html)

**Ravie Lakshmanan**Mar 13, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVixoCttO0Li1BNrJG6s8rsycHEzgVh52YFA_RHnrq4QMjt3fPQuKCJfw8rqCMZtgrSGrXxpPvTyhWQ_rD0D44_3TvBfNC0Eq_VRSWIqDFpDFdKdHMwQIidTX8E4Kc4iiWt3xcwhW_YC8oKLTZFMWN-uyCUjtIavnhXRHbs3gJOLuTUI1zg79tkK4gpsaQ/s1700-e365/veeam.png)

Veeam has released security updates to address multiple critical vulnerabilities in its Backup & Replication software that, if successfully exploited, could result in remote code execution.

The [vulnerabilities](https://www.veeam.com/kb4830) are as follows -

* **CVE-2026-21666** (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21667** (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21668** (CVSS score: 8.8) - A vulnerability that allows an authenticated domain user to bypass restrictions and manipulate arbitrary files on a Backup Repository.
* **CVE-2026-21672** (CVSS score: 8.8) - A vulnerability that allows local privilege escalation on Windows-based Veeam Backup & Replication servers.
* **CVE-2026-21708** (CVSS score: 9.9) - A vulnerability that allows a Backup Viewer to perform remote code execution as the postgres user.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

The shortcomings, which affect Veeam Backup & Replication 12.3.2.4165 and all earlier version 12 builds, have been addressed in [version 12.3.2.4465](https://www.veeam.com/kb4696). CVE-2026-21672 and CVE-2026-21708 have also been fixed in [Backup & Replication 13.0.1.2067](https://www.veeam.com/kb4738), along with [two more critical security flaws](https://www.veeam.com/kb4831) -

* **CVE-2026-21669** (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21671** (CVSS score: 9.1) - A vulnerability that allows an authenticated user with the Backup Administrator role to perform remote code execution in high availability (HA) deployments of Veeam Backup & Replication.

"It's important to note that once a vulnerability and its associated patch are disclosed, attackers will likely attempt to reverse-engineer the patch to exploit unpatched deployments of Veeam software," the company said in its advisory.

With vulnerabilities in Veeam software having been [repeatedly](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html) [exploited](https://thehackernews.com/2024/11/cisa-alert-active-exploitation-of.html) by [threat actors](https://thehackernews.com/2026/01/veeam-patches-critical-rce.html) to carry out ransomware attacks in the past, it's essential that users update their instances to the latest version to safeguard against any potential threat.

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

[Backup Security](https://thehackernews.com/search/label/Backup%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [ransomware](https://thehackernews.com/search/label/ransomware), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [software security](https://thehackernews.com/search/label/software%20security), [Veeam](https://thehackernews.com/search/label/Veeam), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket](data:image/svg+xml;base64... "ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket")

ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html)

[![Coruna iOS Exploit Kit Uses 23 Exploits Across Five Chains Targeting iOS 13–17.2.1](data:image/svg+xml;base64... "Coruna iOS Exploit Kit Uses 23 Exploits Across Five Chains Targeting iOS 13–17.2.1")

Coruna iOS Exploit Kit Uses 23 Exploits Across Five Chains Targeting iOS 13–17.2.1](https://thehackernews.com/2026/03/coruna-ios-exploit-kit-uses-23-exploits.html)

[![⚡ Weekly Recap: Qualcomm 0-Day, iOS Exploit Chains, AirSnitch Attack and Vibe-Coded Malware](data:image/svg+xml;base64... "⚡ Weekly Recap: Qualcomm 0-Day, iOS Exploit Chains, AirSnitch Attack and Vibe-Coded Malware")

⚡ Weekly Recap: Qualcomm 0-Day, iOS Exploit Chains, AirSnitch Attack and Vibe-Coded Malware](https://thehackernews.com/2026/03/weekly-recap-qualcomm-0-day-ios-exploit.html)

[![ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy Fine and More](data:image/svg+xml;base64... "ThreatsDay Bulletin: DDR5 Bot Scalping, Sams...