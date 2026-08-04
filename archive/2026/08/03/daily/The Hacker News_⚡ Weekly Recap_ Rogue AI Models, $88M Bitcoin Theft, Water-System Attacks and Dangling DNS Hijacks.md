---
title: ⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks
url: https://thehackernews.com/2026/08/weekly-recap-rogue-ai-models-88m.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:12.117050
---

# ⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks

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

# [⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks](https://thehackernews.com/2026/08/weekly-recap-rogue-ai-models-88m.html)

**Ravie Lakshmanan**Aug 03, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoiIM6TX9TShDQoVLnmGNE_LZPas3bK4cwsNviskgSjdFASOmzcJPOixde9rkt0uawGd5D5IRHc09j5etqie865lUafh95s-TggQm3PluElF3XhILbJUCkl6vJy6lAM5FSu0GBNu6eWHcVzH7d9X86fvxOjnhwylSgakxghEq_05FsWzZ8mSVMHWYr5HBS/s1700-e365/weeklyrecap.jpg)

This week kept coming back to permission. A model crossed a boundary. A wallet trusted bad randomness. Webmail kept an intruder around. Public systems, package feeds, hotel networks, and login flows all gave away more than intended.

Some of it was clever. Most of it was just access left lying around: old bugs, exposed gear, poisoned dependencies, weak defaults, and tooling that moved from forum chatter to real targets.

The full weekly recap report follows.

## **⚡ Threat of the Week**

**[Anthropic Disclosed its Models Targeted 3 Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)** - Anthropic revealed that three of its models, including Claude Opus 4.7, Mythos 5, and an unnamed research model, breached three unnamed organizations during cybersecurity testing without its knowledge. The AI firm said the earliest incidents date back to April 2026, adding it made the discoveries after launching a "large-scale retrospective review" in response to the recent Hugging Face incident. "After reviewing 141,006 evaluation runs where Claude could have obtained internet access, we identified three incidents in which a model accessed the internet from within or while interacting with the evaluation environment of Irregular, one of our third-party evaluation partners, and then gained unauthorized access to the production infrastructure of three different organizations," it said.

[![Map Attack Paths](data:image/png;base64... "Map Attack Paths")

## Mythos: Map Attack Paths to Collapse Lateral Breach Routes

Access the Gartner® CTEM report to see how the Mythos platform continuously maps cross-domain attack paths and isolates key choke points to break active lateral movement to critical assets.](https://thehackernews.uk/mythos-fix-management)
[Get the full report ➝](https://thehackernews.uk/mythos-fix-management)

## **🔔 Top News**

* **[Coldcard Hardware Wallet Flaw Linked to $88.6M Bitcoin Theft](https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html)** - A vulnerability in Coldcard hardware wallet firmware is said to have been exploited to steal an estimated $88.6 million in Bitcoin from thousands of wallets whose seed phrases were generated using a flawed random number generator. "Coldcard firmware contains an RNG integration error that causes ngu.random to use MicroPython's deterministic Yasmarang fallback instead of the STM32 hardware RNG," Square Engineering [said](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware). "This does not mean every remote attacker can immediately recover every seed. Practical cost depends on available UID information, boot timing, prior RNG calls, and derivation cost."
* **[Russian Hackers Exploit Microsoft OWA Flaw to Maintain Mailbox Access](https://thehackernews.com/2026/07/russian-hackers-exploit-microsoft-owa.html)** - Russian threat actors exploited a security flaw in Microsoft Outlook Web Access (OWA), to target U.S. and European government entities, as well as the telecommunications, financial, hospitality, and aerospace sectors. The activity, which began on July 22, 2026, involves the weaponization of CVE-2026-42897 (CVSS score: 8.1), a cross-site scripting (XSS) vulnerability in OWA. It was flagged by Microsoft as having been exploited in attacks as far back as May 2026. The activity has been attributed to Laundry Bear. The new wave of exploitation revolving around CVE-2026-42897 culminates with the deployment of a previously unknown JavaScript browser-based implant codenamed OWAReaper that's specifically built for persistent access within Microsoft's webmail client.
* **[Critical Rails Flaw Leads to Arbitrary File Read](https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html)** - Ruby on Rails shipped patches for a critical Active Storage vulnerability (CVE-2026-66066, CVSS score: 9.5) that could let unauthenticated attackers read arbitrary files from application servers through crafted image uploads. The flaw can be exploited to expose Rails process environment and secrets such as secret\_key\_base, master key, database passwords, cloud storage credentials, and API tokens, which may enable remote code execution or lateral movement into connected systems. CVE-2026-66066 is exploitable when libvips is used, enabling an attacker to upload a specially crafted image to a vulnerable application and read arbitrary files on the server. A key prerequisite for the attack is that the server must allow image uploads from untrusted users. Additional details of the flaw have been [released](https://discuss.rubyonrails.org/t/cve-2026-66066-attack-details-and-tools-to-perform-a-forensic-investigation/91441) by the Rails team, along with tools to [help assess](https://github.com/rails/rails-forensics-CVE-2026-66066) vulnerable applications. "Because this vulnerability requires no authentication and targets the default image processor in modern Rails environments, it is essential to apply vendor patches and rotate secrets immediately," Akamai [said](https://www.akamai.com/blog/security-research/rails-active-storage-rce-cve-2026-66066).
* **[Coordinated Attacks Target 30+ Minnesota Water Systems](https://thehackernews.com/2026/07/coordinated-cyberattack-targets-30.html)** - A [coordinated cyber attack campaign](https://mn.gov/mnit/media/blog/?id=761869) targeted over 30 water systems in Minnesota on July 26 and 27, 2026. "The nature and extent of the impact varied by system, and the investigation is still determining how many experienced operational disruptions," Minnesota IT Services (MNIT) said. The activity has not been [officially attributed](https://apnews.com/article/cyberattack-minnesota-water-systems-5bb1dcba...