---
title: ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories
url: https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html
source: The Hacker News
date: 2026-07-02
fetch_date: 2026-07-03T05:48:49.352498
---

# ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html)

**Ravie Lakshmanan**Jul 02, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMzwXbN53zy07KSkFJL7uOzty4Pj7VgKS6lSwWWGSCppX0wEX5eY0ZLur2NiFcs-ByBBhbd1WZ270Y4VMMGL6WkvOIZ5MhyphenhyphenkDX2B45wiQue-W88oiF_-RZs0HxvrvcxCHI8Zhhv1-fqHDgnX-VLWk00gt463rQhyKY7Mzcd5STMCYeCUcyVri3aBSUpl2t/s1700-e365/threatsday-board.jpg)

This week’s security news is mostly about weak spots.

Browsers, bots, sandboxes, AI systems, and email flows all show the same problem in different ways. Everything looks normal until someone tests a small gap and finds a way through.

This is not one big break. It is small permissions, weak checks, open systems, and normal tools doing things they were allowed to do. That same pattern runs through the stories below.

1. Ransomware phishing lure

   [Fake INTERPOL Investigation Emails Lures Lead to Ransomware](https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-interpol-emails-serve-ransomware)

   A phishing campaign is targeting small businesses across Europe, Asia, the Middle East, and the U.S. with fake investigation emails impersonating law enforcement officials. "The emails claim to contain evidence of suspicious company activity and pressure recipients into opening a password-protected archive," Bitdefender [said](https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-interpol-emails-serve-ransomware). "Recipients are directed to a Proton Drive-hosted file that ultimately delivers ransomware. The ransomware appears to be a custom-built payload rather than a known ransomware family."
2. Sandbox root escape

   [Exploiting Root Execution in Claude Cowork Sandbox](https://www.armadin.com/blog-posts/exploiting-root-execution-in-claude-coworks-sandbox)

   New research from Armadin has discovered an attack chain affecting Claude Cowork on Windows. The attack allows an attacker with local code execution to plant a malicious file in Claude Desktop's application directory, hijacking a trusted process to communicate with Cowork's underlying VM service. "An attacker with local code execution could run arbitrary commands as root in Claude Cowork's sandbox without network egress restrictions," the company [said](https://www.armadin.com/blog-posts/exploiting-root-execution-in-claude-coworks-sandbox). The exploit takes advantage of two unvalidated parameters in the service's interface that allow the attacker to run commands as root and bypass network filtering entirely, thereby allowing sensitive data to be exfiltrated to attacker-controlled infrastructure. Following responsible disclosure on May 29, 2026, Anthropic said it does not consider it to be a security issue because exploitation requires pre-existing local code execution on the host.
3. Email privacy flaw

   [Flaw in Apple's Hide My Email](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/)

   A vulnerability has been disclosed in Apple's Hide My Email service that allows users' real email addresses to be unmasked. Tyler Murphy, the researcher who found the bug, said that he reported the issue to Apple over a year ago and that it continues to remain unpatched. "We don't know the full scope of the issue, but in our limited tests with volunteers, 100% of Hide My Email addresses were exploitable," Murphy [told](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/) 404 Media. Exact details surrounding the vulnerability have been withheld to avoid potential exploitation concerns.
4. China-linked RAT activity

   [New BeepRAT Remote Access Trojan Discovered](https://zerolabs.rubrik.com/blog/beeprat-behind-telecom-utility-lies-china-nexus-toolset)

   A customized version of the open-source DCRat framework dubbed BeepRAT has been identified as distributed via a Chinese phone number management utility packaged within a ZIP archive, per Rubrik Zero Labs. "The archive contained a .NET application named HFY.exe alongside several third-party libraries commonly associated with database-driven applications," Rubrik [said](https://zerolabs.rubrik.com/blog/beeprat-behind-telecom-utility-lies-china-nexus-toolset). "Although the application appeared to function as a telephone number management tool, further analysis revealed a sophisticated multi-stage infection chain that ultimately deployed the customized BeepRAT payload." The malware establishes persistence on the host via scheduled tasks, and resolves the command-and-control infrastructure using DNS-over-HTTPS (DoH) requests. It then beacons a packet containing information about the compromised host, after which a persistent communication channel is opened to receive incoming commands that allow the malware to transfer files between the host and the server, launch interactive command prompt sessions, issue commands to it, launch PowerShell sessions, enumerate running processes and available storage drives, terminate a specified process, perform file system operations, record through webcam, log keystrokes, take screenshots, list active network connections, download and run .NET assemblies in memory, and launch a proxy. It's assessed that BeepRAT operates within the China-nexus espionage ecosystem.
5. AI cyber benchmark

   [Evaluation of OpenAI GPT-5.6 Sol](https://www.irregular.com/research/assessing-gpt-5.6-sol)

   An evaluation of OpenAI's [GPT-5.6 Sol](https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html) on real-world offensive security benchmarks by AI security lab Irregular has found the model to perform slightly better than GPT-5.5, while continuing to struggle with well-defended targets and complete end-to-end attacks. "GPT-5.6 Sol demonstrated capabilities relevant to offensive cyber misuse, including finding and exploiting ...