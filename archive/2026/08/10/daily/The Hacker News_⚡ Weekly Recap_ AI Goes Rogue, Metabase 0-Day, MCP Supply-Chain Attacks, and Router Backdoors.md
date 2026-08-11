---
title: ⚡ Weekly Recap: AI Goes Rogue, Metabase 0-Day, MCP Supply-Chain Attacks, and Router Backdoors
url: https://thehackernews.com/2026/08/weekly-recap-ai-goes-rogue-metabase-0.html
source: The Hacker News
date: 2026-08-10
fetch_date: 2026-08-11T03:31:51.130059
---

# ⚡ Weekly Recap: AI Goes Rogue, Metabase 0-Day, MCP Supply-Chain Attacks, and Router Backdoors

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

![cybersecurity](data:image/svg+xml;base64...)

# [⚡ Weekly Recap: AI Goes Rogue, Metabase 0-Day, MCP Supply-Chain Attacks, and Router Backdoors](https://thehackernews.com/2026/08/weekly-recap-ai-goes-rogue-metabase-0.html)

**Ravie Lakshmanan**Aug 10, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtXmkUOPD6prrNPMK9N1Rhu2dm3QFGQ2DUTiu3xrj2WWbauZ_IK2HemME36-4WBIqGh01SFOkNJuutFeXLgS_ZMUBFn5ZDzIP5_IeNrwJWDfKcOPQgZl3spOFVS8R84Hbthy6o3sx9IWJ1yRo4FiW5acGYGBrf2nljmx6yvSd55LWRrkX6JhJ9b5bHJX0g/s1700-e365/recaps.jpg)

A lot of security problems still begin with someone doing a completely normal thing. Cloning a repo. Answering a call. Leaving a box exposed. Trusting the default.

That pretty much covers the mood this week. Old bugs are back, supply chains are getting stranger, and some exploit paths are so short you wonder what was supposed to stop them in the first place.

That’s only part of it. Here’s everything else that made the Monday recap.

## **⚡ Threat of the Week**

**[Anthropic's Model Attempts to Poison Open-Source Project](https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html)** — A new evaluation conducted by the U.K. AI Security Institute (AISI) found that AI models with access to the internet reached out into the real world to target individuals and organizations autonomously across 10 of the total of 122 runs. Of 19 such actions recorded, 17 originated from Anthropic's Mythos 5 and the remaining two involved OpenAI's GPT-5.6-Sol with cyber classifiers. In the most serious case, Anthropic's Claude Mythos 5 spent 34 hours trying to get a malware dropper merged into a real open-source project and engaged in social engineering by creating fake online identities and using them to pressure the project's maintainer to approve the code. Ultimately, a human maintainer caught and refused to approve the malicious code. "These attempts were unsuccessful, and our investigations have not evidenced any resulting real-world harm," AISI said. But this is the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real-world."

[![Ransomware Encryption](data:image/png;base64... "Ransomware Encryption")

## Ransomware Encryption Dropped 38%. Here's What Attackers Do Instead

Data Encrypted for Impact fell from 21% to 13% of samples in one year. Meanwhile, Process Injection held #1 for the third straight year and sandbox evasion surged to #4. The Red Report 2026 ranks the top 10 ATT&CK techniques and the behaviors to hunt for each.](https://thehackernews.uk/red-threat-2026)
[Read the Report ➝](https://thehackernews.uk/red-threat-2026)

## **🔔 Top News**

* **[Metabase 0-Day Exploited in Attacks](https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html)** — Metabase warned that a maximum-severity security flaw impacting its business intelligence and data visualization software package has been exploited in the wild as a zero-day. The vulnerability (CVSS score: 10.0), which does not carry a CVE identifier, allows an unauthenticated remote attacker to inject arbitrary SQL into the Metabase application database, enabling them to gain administrator access to the instance. Armed with the elevated access, the attacker can change the application configuration, steal stored credentials for the connected databases, read any data accessible through those connections, and export data. One of the companies that has been affected is Framework.
* **[New Interrupt Injection Attack Bypass Spectre v2 Defenses on Intel and AMD CPUs](https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html)** — A group of researchers demonstrated a way to bypass defenses for the Spectre vulnerability impacting modern CPUs. "The defenses work by wiping or isolating the processor's prediction machinery, removing anything an attacker might have planted," MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL) said. "The catch [...] is that the wipe and the moment the predictions get used can't happen at the same instant. There is always a gap — sometimes only a handful of instructions wide. Anything that runs in that gap can dirty the machinery all over again. The researchers call this class of attack TONTOU." The study found a reliable way to get code into that gap using a technique called Interrupt Injection to ultimately pull secrets out of memory.
* **[New CSS Attacks Can Break Webmail Defenses](https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html)** — New research demonstrated at the Black Hat conference last week detailed attack chains spanning Microsoft Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and AOL Mail that can capture passwords, take over third-party accounts, leak tokens, hijack trusted UI actions, and manipulate AI tools that read email. "Trouble is you can create discrepancies between what the sanitizer thinks is safe and what the browser actually renders," PortSwigger said. "Some webmail clients go a step further by letting the browser parse the HTML and CSS first, then filtering the browser's interpreted output rather than the original source. Yet even this can be mutated into something malicious."
* **[UNC6671 Vishing Attacks Target Financial Firms](https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html)** — A recent wave of cyber attacks targeting financial services, private equity, and professional services has been attributed to a data extortion group known as UNC6671. The attacks employ voice phishing to target enterprise employees and trick them into visiting spoofed login portals where adversary-in-the-middle (AitM) infrastructure intercepts credentials and multi-factor authentication (MFA) tokens. The threat actors then leverage the captured data to establish session persistence and deploy automated Python and PowerShell scripts for data exfiltration from enterprise cloud environments and SaaS applications, including Microsoft 365 and Okta. UNC6671 has diversified its operations across multiple extortion brands including Redact, Pink (aka CL-CRI-1147), Helix, and Falcon (aka CL-CRI-1182). UNC6671 was previously said to have operated under the BlackFile (aka CL-CRI-1116) brand, targeting organizations v...