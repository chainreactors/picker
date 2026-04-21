---
title: ⚡ Weekly Recap: Vercel Hack, Push Fraud, QEMU Abused, New Android RATs Emerge & More
url: https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html
source: The Hacker News
date: 2026-04-20
fetch_date: 2026-04-21T04:51:45.736018
---

# ⚡ Weekly Recap: Vercel Hack, Push Fraud, QEMU Abused, New Android RATs Emerge & More

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [⚡ Weekly Recap: Vercel Hack, Push Fraud, QEMU Abused, New Android RATs Emerge & More](https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html)

**Ravie Lakshmanan**Apr 20, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirkQSoHlNZvcdjrevc7r-D8mPj49i3XRimQjk-HtEVDYVX4vKEcW4JLiTblV5oI8MtUib2Q5iFerdt0x4_mGDvMJqsDd2wX6QNQxM25Wnrq-MRYADw1YuJly5yoSTIz_ToqlWsAKA2hLwru4Crx8aSguTETpDl4mjRfrCg0G8Cca5Rk0Am6FCwRCNPIqBy/s1700-e365/recap-april.jpg)

Monday’s recap shows the same pattern in different places. A third-party tool becomes a way in, then leads to internal access. A trusted download path is briefly swapped to deliver malware. Browser extensions act normally while pulling data and running code. Even update channels are used to push payloads. It’s not breaking systems—it’s bending trust.

There’s also a shift in how attacks run. Slower check-ins, multi-stage payloads, andmore code kept in memory. Attackers lean on real tools and normal workflows instead of custom builds. Some cases hint at supply-chain spread, where one weak link reaches further than expected.

Go through the whole recap. The pattern across access, execution, and control only shows up when you see it all together.

## **⚡ Threat of the Week**

**[Vercel Discloses Data Breach](https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html)**—Web infrastructure provider Vercel has disclosed a security breach that allows bad actors to gain unauthorized access to "certain" internal Vercel systems. The incident originated from the compromise of Context.ai, a third-party artificial intelligence (AI) tool, which was used by an employee at the company, it added. "The attacker used that access to take over the employee's Vercel Google Workspace account, which enabled them to gain access to some Vercel environments and environment variables that were not marked as 'sensitive,'" the company said. It's currently not known who is behind the incident, but a threat actor using the ShinyHunters persona has claimed responsibility for the hack. Context.ai also disclosed a March 2026 incident involving unauthorized access to its AWS environment. However, it has since emerged that the attacker also likely compromised OAuth tokens for some of its consumer users. Furthermore, Hudson Rock uncovered that a Context.ai employee was compromised with Lumma Stealer in February 2026, raising the possibility that the infection may have triggered the "supply chain escalation."

[![Autonomous Validation](data:image/png;base64... "Autonomous Validation")

## 99% of What AI Found Is Still Unpatched. See the Defensive Answer

Anthropic's Mythos weaponized bugs that survived decades of human review. Atlassian's CISO, Frost & Sullivan, and leaders from Kraft Heinz and Glow Financial Services show how autonomous validation discovers what's exploitable, proves controls hold, and re-validates fixes.](https://thehackernews.uk/av2026-summit)
[Register for Free ➝](https://thehackernews.uk/av2026-summit)

## **🔔 Top News**

* **[Law Enforcement Operation Brings Down DDoS-for-Hire Operation](https://thehackernews.com/2026/04/operation-poweroff-seizes-53-ddos.html)**—Law enforcement agencies across Europe, the U.S., and other partner nations cracked down on the commercial DDoS-for-hire ecosystem, targeting both operators and customers of services used to target websites and knock them offline. As part of the effort, authorities took down 53 domains, arrested four people, and sent warning notifications to thousands of criminal users. The U.S. Justice Department said court-authorized actions were undertaken to disrupt Vac Stresser and Mythical Stress. The actions are a persistent cat-and-mouse game, as booted services often reappear under new names and domains despite repeated takedowns. While these disruptions tend to have short-term results, the resilience of the criminal activity indicates that arrests need to be combined with infrastructure seizures, financial disruption, and user deterrence for lasting impact.
* **[Newly Discovered PowMix Botnet Hits Czech Workers](https://thehackernews.com/2026/04/newly-discovered-powmix-botnet-hits.html)**—An active malicious campaign is targeting the workforce in the Czech Republic with a previously undocumented botnet dubbed PowMix since at least December 2025. "PowMix employs randomized command-and-control (C2) beaconing intervals, rather than persistent connection to the C2 server, to evade the network signature detections," Cisco Talos said. The never-before-seen botnet is designed to facilitate remote access, reconnaissance, and remote code execution, while establishing persistence by means of a scheduled task. At the same time, it verifies the process tree to ensure that another instance of the same malware is not running on the compromised host.
* **[AI-Driven Pushpaganda Exploits Google Discover to for Ad Fraud](https://thehackernews.com/2026/04/ai-driven-pushpaganda-scam-exploits.html)**—A novel ad fraud scheme has been found to leverage search engine poisoning (SEO) techniques and artificial intelligence (AI)-generated content to push deceptive news stories into Google's Discover feed and trick users into enabling persistent browser notifications that lead to scareware and financial scams. The Pushpaganda campaign has been found to target the personalized content feeds of Android and Chrome users. "This operation, named for push notifications central to the scheme, generates invalid organic traffic from real mobile devices by tricking users into subscribing to enabling notifications that presented alarming messages," HUMAN Security said. Google has since rolled out fixes and algorithmic updates to address the issue.
* **[Obsidian Plugin Abuse Delivers PHANTOMPULSE RAT](https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html)**—A social engineering campaign has abused Obsidian, a cross-platform note-taking application, as an initial access vector to distribute a previously undocumented Windows remote access trojan called PHANTOMPULSE in attacks targeting individuals in the financial and cryptocurrency sectors. Elastic Security Labs is tracking the activity under the name REF6598. It employs elaborate social engineering tactics thro...