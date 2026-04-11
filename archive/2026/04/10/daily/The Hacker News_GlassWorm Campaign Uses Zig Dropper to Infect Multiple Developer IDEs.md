---
title: GlassWorm Campaign Uses Zig Dropper to Infect Multiple Developer IDEs
url: https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html
source: The Hacker News
date: 2026-04-10
fetch_date: 2026-04-11T04:22:56.737715
---

# GlassWorm Campaign Uses Zig Dropper to Infect Multiple Developer IDEs

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

# [GlassWorm Campaign Uses Zig Dropper to Infect Multiple Developer IDEs](https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html)

**Ravie Lakshmanan**Apr 10, 2026Malware / Blockchain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioOU2XpKmyRPz5kTr4GhD1YLJ2t7F6yv7bQD1upkiwmGwmzirnDAz92GvtjckyoBhBjaRqeR9XPm6e0yHdKLowfDDgZNkRlCvCneJEncgiviFu7PgD4wQg3Bo5JDhgg6JTytg_fY2M-iKeykCLebOdStW4A76JKnPbEQazihNOhKOdM9Ou8keMBh4IY4jo/s1700-e365/software.jpg)

Cybersecurity researchers have flagged yet another evolution of the ongoing **[GlassWorm](https://thehackernews.com/2026/03/glassworm-malware-uses-solana-dead.html)** campaign, which employs a new Zig dropper that's designed to stealthily infect all integrated development environments (IDEs) on a developer's machine.

The technique has been discovered in an Open VSX extension named "[specstudio.code-wakatime-activity-tracker](https://open-vsx.org/extension/specstudio/code-wakatime-activity-tracker)," which masquerades as WakaTime, a popular tool that measures the time programmers spend inside their IDE. The extension is no longer available for download.

"The extension [...] ships a Zig-compiled native binary alongside its JavaScript code," Aikido Security researcher Ilyas Makari [said](https://www.aikido.dev/blog/glassworm-zig-dropper-infects-every-ide-on-your-machine) in an analysis published this week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

"This is not the first time [GlassWorm](https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html) has resorted to using [native compiled code](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery) in extensions. However, rather than using the binary as the payload directly, it is used as a stealthy indirection for the known GlassWorm dropper, which now secretly infects all other IDEs it can find on your system."

The newly identified Microsoft Visual Studio Code (VS Code) extension is a near replica of WakaTime, save for a change introduced in a function named "activate()." The extension installs a binary named "win.node" on Windows systems and "mac.node," a universal Mach-O binary if the system is running Apple macOS.

These Node.js native addons are compiled shared libraries that are written in Zig and load directly into Node's runtime and execute outside the JavaScript sandbox with full operating system-level access.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFb_56sYOjx6ioCMNc4210rtcw2VFRZdOk6P356I7RATYkrbermGGWugCPYJZw-7FlvQXeqvQHhTEaaVHYl4o-AEW0ib-KuZ2IK5cYJDMqF4XQPlfFndWcFzxgk_P2sJe6CC5bIy4c9wc7YxbjrtMAEybNF7Gvj6Tydej5VQ_3kuzyKQGXBQciCJIjy3-Z/s1700-e365/chain.png)

Once loaded, the primary goal of the binary is to find every IDE on the system that supports VS Code extensions. This includes Microsoft VS Code and VS Code Insiders, as well as forks like VSCodium, Positron, and a number of artificial intelligence (AI)-powered coding tools like Cursor and Windsurf.

The binary then downloads a malicious VS Code extension (.VSIX) from an attacker-controlled [GitHub account](https://github.com/ColossusQuailPray). The extension – called "floktokbok.autoimport" – impersonates "[steoates.autoimport](https://marketplace.visualstudio.com/items?itemName=steoates.autoimport)," a legitimate extension with more than 5 million installs on the official Visual Studio Marketplace.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

In the final step, the downloaded .VSIX file is written to a temporary path and silently installed into every IDE using each editor's CLI installer. The second-stage VS Code extension [acts as a dropper](https://thehackernews.com/2026/03/glassworm-malware-uses-solana-dead.html) that avoids execution on Russian systems, talks to the Solana blockchain to fetch the command-and-control (C2) server, exfiltrates sensitive data, and installs a remote access trojan (RAT), which ultimately deploys an information-stealing Google Chrome extension.

Users who have installed "specstudio.code-wakatime-activity-tracker" or "floktokbok.autoimport" are advised to assume compromise and rotate all secrets.

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

[Blockchain](https://thehackernews.com/search/label/Blockchain), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Information Stealer](https://thehackernews.com/search/label/Information%20Stealer), [Malware](https://thehackernews.com/search/label/Malware), [Open VSX](https://thehackernews.com/search/label/Open%20VSX), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code)

Trending News

[![Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](data:image/svg+xml;base64... "Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass")

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html)

[![New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](data:image/svg+xml;base64... "New Chrome Zero-Day CVE-2026-5281 Under Activ...