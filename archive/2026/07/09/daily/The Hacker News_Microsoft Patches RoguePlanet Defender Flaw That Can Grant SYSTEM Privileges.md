---
title: Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges
url: https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:13.783774
---

# Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges

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

# [Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges](https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html)

**Ravie Lakshmanan**Jul 09, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuqwSaoB3zc0bIhf1aBmcHsVVAsGnRDBc681vhmlgHYy0xx5VSxyS2jqjmk-mq27QrSKPN3yorL3A7DffJYp3iMO7CY_8owm-Cn8r7IFuvqeGHTPSyiFM0KVTMTE8W0Qon84tCbzsLVNqoS5nLq1aX8_RNKg0sxa2ke4Su_p5qy9dAlFdakwYcjueBGNhD/s1700-e365/windows.jpg)

Microsoft has released security updates for a Defender vulnerability known as RoguePlanet, nearly a month after details of the flaw became public.

The vulnerability, tracked as **[CVE-2026-50656](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-50656)** (CVSS score: 7.8), is a privilege escalation issue in the Microsoft Malware Protection Engine ("mpengine.dll"), which provides scanning, detection, and cleaning capabilities for its antivirus and antispyware software.

The issue has been remediated in Microsoft Malware Protection Engine version 1.1.26060.3008, along with defense-in-depth updates to harden unspecified security-related features.

RoguePlanet was [first disclosed](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html) by a security researcher named Chaotic Eclipse (aka Nightmare-Eclipse), describing it as a race condition that could be abused to spawn a shell with SYSTEM-level privileges. This, in turn, grants the attacker the ability to run arbitrary code or perform unauthorized actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The exploit has been [found](https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html) to work on systems running up-to-date versions of Windows with the June 2026 Patch Tuesday updates installed. Subsequently, Chaotic Eclipse also revealed that the exploit works regardless of whether real-time protection is on or not. Microsoft [has not officially credited](https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html) Chaotic Eclipse with the vulnerability discovery.

RoguePlanet is the fourth Defender vulnerability disclosed by the researcher after [BlueHammer](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html) (CVE-2026-33825), [UnDefend](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) (CVE-2026-45498), and [RedSun](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) (CVE-2026-41091), all of which have since been patched by Microsoft.

The Windows maker said no customer action is required to install the update for CVE-2026-50656, as the software is frequently updated to secure customers against new and evolving threats.

"For enterprise deployments as well as end users, the default configuration in Microsoft antimalware software helps ensure that malware definitions and the Microsoft Malware Protection Engine are kept up to date automatically," Microsoft said.

"Depending on which Microsoft antimalware software is used and how it is configured, the software may search for engine and definition updates every day when connected to the Internet, up to multiple times daily. Customers can also choose to manually check for updates at any time."

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

[Antivirus](https://thehackernews.com/search/label/Antivirus), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [exploit](https://thehackernews.com/search/label/exploit), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Threat Detection](https://thehackernews.com/search/label/Threat%20Detection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](data:image/svg+xml;base64... "ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories")

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html)

[![Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](data:image/svg+xml;base64... "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability")

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)

[![New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](data:image/svg+xml;base64... "New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets")

New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](http...