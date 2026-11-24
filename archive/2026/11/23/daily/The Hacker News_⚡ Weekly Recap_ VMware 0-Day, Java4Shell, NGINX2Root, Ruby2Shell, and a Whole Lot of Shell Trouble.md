---
title: ⚡ Weekly Recap: VMware 0-Day, Java4Shell, NGINX2Root, Ruby2Shell, and a Whole Lot of Shell Trouble
url: https://thehackernews.com/2026/11/weekly-recap-vmware-0-day-java4shell.html
source: The Hacker News
date: 2026-11-23
fetch_date: 2026-11-24T11:49:19.558167
---

# ⚡ Weekly Recap: VMware 0-Day, Java4Shell, NGINX2Root, Ruby2Shell, and a Whole Lot of Shell Trouble

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [⚡ Weekly Recap: VMware 0-Day, Java4Shell, NGINX2Root, Ruby2Shell, and a Whole Lot of Shell Trouble](https://thehackernews.com/2026/11/weekly-recap-vmware-0-day-java4shell.html)

**Ravie Lakshmanan**Nov 23, 2026Cybersecurity News / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBkXdg7nYK3nVTpBuC9FL7mGBvzvUxU0VxYplArVFYSTg2d_6tFITemHBYRAOD29pVBKzfo2aZ9Jsy8avRdACCMqrVdlEER0zn2xIWDBdswcH_nZpnJYkfORK6CEaWwX3f-B8AvkUqbR2TLNa7odUG4PFu1uTk_cwsUt8DPGJBSjjF2wd8VPIa5ATJ4fo3/s1700-nu-rw-lo-l85-e365/crecap.jpg)

A stolen key. A trusted message. A routine update. None of these looks like the start of a major security problem. That's partly why they work. Attackers don't always need to break down a door. Sometimes they just use one that's already open.

This week's stories show how quickly a small opening can turn into a much bigger mess. One breach helps attackers reach another target. Tools people rely on become ways to get inside. Even features built for safety can end up helping the wrong person. And some of the latest research shows just how little effort certain attacks need.

The strange part is how normal it all looks until something goes wrong. A few attacks are clever. Others are almost embarrassingly simple. Both can do real damage. Here's what caught our attention this week.

## **⚡ Threat of the Week**

**[Threat Actor Exploits VMware vCenter Flaw as a 0-Day](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html)** — The suspected China-nexus cyber espionage group known as Armory Castle (formerly UNC5221) has been attributed to the zero-day exploitation of a critical security flaw in VMware vCenter Server in early September 2026. The vulnerability, tracked as CVE-2026-123890 (CVSS score: 9.8), is a case of authentication bypass in the VMware Directory Service that could be exploited to gain unauthorized access to the system. In October, Google described a campaign by Armory Castle to exploit organizations through BeyondTrust's Remote Support tool, using a zero-day to breach the edge appliance and steal secrets useful for network reconnaissance and downstream compromises within organizations. The latest findings show that BeyondTrust was merely an entry point to a deeper and more complex campaign that involved the deployment of backdoors on Linux machines.

[![Workforce Secured from AI Threats](data:image/png;base64... "Workforce Secured from AI Threats")

## Is Your Workforce Secured from AI Threats?](https://thehackernews.uk/security-awareness-tour)

Attackers now weaponize AI to launch personalized phishing attacks faster than employees can react. Fight AI with AI, using realistic simulations to train employees to spot and stop threats. [Stop phishing before it becomes a breach.](https://thehackernews.uk/phishing-simulation)

[Book a Demo ➝](https://thehackernews.uk/security-awareness-tour)

## **🔔 Top News**

* **[Cursor Links Malicious Claude Extension Release to Fireworks AI Incident](https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html)** — Cursor has traced the origins of a security incident involving a malicious version of Anthropic's Claude Code extension in its marketplace to a breach at AI infrastructure provider Fireworks. "An attacker obtained an access key we had issued to Fireworks," Cursor said. "The key was exposed by Fireworks, and the attacker used it to copy data from a read-only storage bucket we used to share data with them." The Cursor incident is another indication of how the rapid adoption of AI-powered development tools and increasingly interconnected software ecosystems has worsened software supply chain risks.
* **[Cold Relic Exploits Cloud Breaches to Target Organizations](https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html)** — The Russian cyberespionage group known as Cold Relic is turning cloud breaches into a springboard for targeting a victim organization's wider network of trusted relationships. In the first intrusion observed late last year, the attackers gained control of a cloud administrator account and harvested internal communications, employee details, and other organizational records. Cold Relic later used that information to impersonate an employee of the first organization to conduct a social engineering attack on an individual at a second organization. The campaigns "demonstrate the convergence of human-centric social engineering and cloud identity abuse," Google said. "By obtaining access to strategic personnel rosters and operational documents, Russian intelligence services turn legitimate business communications into attack vectors against trusted partners."
* **[Malicious Web Pages Can Hijack Meta Muse](https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html)** — New research from the NebuSec research team has demonstrated that an attacker-controlled web page can be exploited to gain unauthorized access to user data associated with Meta Muse and compromise the underlying virtual machine (VM) in which it operates. "An attacker could retrieve conversation history and stored memories without triggering Muse's network approval prompts," NebuSec [said](https://nebusec.ai/research/meta-muse-credential-exposure/). "The attack also allowed us to alter stored memories and conversation history, creating risks beyond unauthorized data access. By exploiting a vulnerability in the shared Linux kernel, we escaped the agent's runtime container and obtained root privileges in the underlying user VM." Meta has since addressed the issue.
* **[New FastUnlock Windows Narrator LockScreen Bypass Detailed](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)** — Security researcher Abdelhamid Naceri (aka Chaotic Eclipse) published [FastUnlock](https://github.com/MSNightmare/FastUnlock), a new unpatched Windows 11 zero-day that abuses the Narrator screen reader to get past the lock screen and execute code as t...