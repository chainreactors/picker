---
title: New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware
url: https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:12.937100
---

# New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware

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

# [New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware](https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html)

**Swati Khandelwal**Jul 09, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJRuXh4y7zy8C81w_JgJgWFg_sgF0IYcsvqWEsYeHIHu7nWdOl1aIMQdnmmRQF-KJK_XdTGxzSIAr57yFkzMIZ_VK5Kzx12xR4oW8QOZcnsf9zmySIT3YRvpPvo2q-P92sZc2LqB4M-NSlktwLGU85I0JQbCVCjvJ130GLEF6eGknO8VzkK66kHjlgkBg/s1700-e365/data-wiper-malware.jpg)

Microsoft has taken apart a destructive Windows backdoor it calls **GigaWiper**. What stands out is how it is built: not one tool but three older destructive programs bolted into one, offered as commands the operator can choose from.

Each is a different way to break a machine: wipe the whole disk, overwrite the Windows drive, or run fake "ransomware" that scrambles files with a key it never saves.

Because this is malware and not a single flaw, there is no patch to chase; GigaWiper is what an attacker runs after they are already inside, which makes early detection and clean, offline backups the real defense.

The same malicious files show up in a second report under another name: **BLUERABBIT**, a backdoor Binary Defense [flagged last month](https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html#backdoor-with-wiper-modules).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Microsoft lists four hashes for the [GigaWiper backdoor](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/); Binary Defense lists the same four for [BLUERABBIT](https://binarydefense.com/resources/blog/bluerabbit-a-golang-based-backdoor-with-ransomware-and-destructive-capabilities), and both command servers match. Binary Defense, citing Google's Threat Intelligence Group, ties the malware to a likely Iran-nexus group aimed at Israeli organizations. Microsoft names no country.

## Three ways to destroy a machine

GigaWiper is written in Go (also called Golang) and runs on Windows. It takes orders as numbered commands, and three of them destroy the machine, each in a different way:

* A raw disk wiper that overwrites the physical drive and wipes the partition table (the map of how the disk is laid out) before rebooting. There is no file-by-file deletion to reverse; it destroys the disk contents directly.
* Fake ransomware built on older code called **Crucio**. It encrypts files, adds a .candy extension, and changes the desktop wallpaper to an alarming warning image. There is no ransom note and no saved key, so there is nothing to pay and nothing to decrypt. This is destruction wearing a ransomware costume.
* The last targets the Windows drive, overwriting it several times with different data patterns. Microsoft says it is a Go rewrite of a wiper it tracks as **FlockWiper**.

None of these leaves a way back: encrypted files cannot be unlocked because the key is gone, and wiped drives can only be rebuilt from clean backups. The goal is a dead machine, not a payout.

## It spies, too

Destruction is only half of it. The same backdoor can quietly watch and control an infected PC. It takes screenshots of every monitor, records the screen while someone is working, and can open a hidden VNC session that streams the display and lets the attacker type and move the mouse.

It also collects system details, manages running programs and services, edits the registry, and can wipe Windows event logs to cover its tracks. Microsoft found more commands sitting dormant in the samples it examined, including stubs for a keylogger and additional wipers.

To stay out of sight, GigaWiper pretends to be OneDrive. It creates a scheduled task named OneDrive Update that runs every minute and tracks itself in a registry key under HKCU\SOFTWARE\OneDrive\Environment. When it opens its remote-control channel, it hides behind a firewall rule named after a real Windows component, Microsoft.Windows.CloudExperienceHost.

For its command traffic, it skips ordinary web requests and rides on real business services instead: RabbitMQ for tasking, Redis for results, and MinIO for exfiltration. Because those are legitimate tools rather than a custom malware channel, the traffic looks ordinary on networks that already run them.

## Where GigaWiper came from

Microsoft traces GigaWiper's fake-ransomware code back to Crucio and its multi-pass wiper back to FlockWiper, and assesses that the same developer built all three. It names no country. But Crucio is not anonymous. Its code was listed as suspected ransomware in a December 2023 [CISA advisory](https://www.cisa.gov/sites/default/files/2023-12/aa23-335a-irgc-affiliated-cyber-actors-exploit-plcs-in-multiple-sectors-1.pdf) on CyberAv3ngers, a group linked to Iran's Islamic Revolutionary Guard Corps.

That is the same crew, [THN reported](https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html), that broke into water and energy sites across the US, Israel, the UK, and Ireland in 2023, logging into internet-exposed industrial controllers. In one case, they took control of a booster station at a Pennsylvania water authority. The Crucio sample Microsoft cites carries the same fingerprint listed in that advisory.

Microsoft also found a recurring tag, "GRAT", in both FlockWiper's debug paths and GigaWiper's own function names, tying the two tools together and hinting at a further component that has not surfaced yet. The timing differs by source: Microsoft dates the destructive activity to October 2025, while Binary Defense first saw the same files as BLUERABBIT in March 2026.

## Part of a bigger wave

Iran-linked wiper activity against Israel has drawn repeated warnings through 2025 and 2026. Palo Alto Networks' [Unit 42](https://unit42.paloaltonetworks.com/handala-hack-wiper-attacks/) has tracked a parallel surge, much of i...