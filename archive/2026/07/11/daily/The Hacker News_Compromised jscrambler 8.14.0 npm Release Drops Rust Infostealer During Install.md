---
title: Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install
url: https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
source: The Hacker News
date: 2026-07-11
fetch_date: 2026-07-12T05:12:04.938135
---

# Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install

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

# [Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html)

**Swati Khandelwal**Jul 11, 2026Software Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhodiWPXDsex6YL7v4e2n_D5MJFMht76GRRmHTdiG61tfEmsoZyow4tkiS3ORACILDl2fNP27YQkw1XLSBKGcom-DhCVzzPDdkdSgeMGdxcVL_rgO70x5LqZcjxKAPTtFOquB8LwSBPWrSpflqCzns-cFZ_EVm0WZfV7wSoPM3S-7_IGtCT3AjxY0rfITU/s1700-e365/npm-js.jpg)

The jscrambler npm package was compromised, and simply installing its 8.14.0 release runs an infostealer on your machine. Published on July 11, 2026, the malicious version carries a preinstall hook that drops and executes a native binary, one build each for Windows, macOS, and Linux.

Socket flagged the release [six minutes after it was published](https://socket.dev/blog/jscrambler-supply-chain-attack). If you or one of your build systems pulled it in that window, the payload has already run with whatever access your install process had.

None of this is in the prior release, 8.13.0. [The package diff](https://socket.dev/npm/package/jscrambler/diff/8.14.0) shows two new files under dist/: setup.js, a small loader, and intro.js. Despite the name, intro.js is not JavaScript but a roughly 7.8MB container packing three gzip-compressed native binaries, one each for Linux, Windows, and macOS.

On install, setup.js picks the binary for the host operating system, writes it under a random name in the system temp directory, marks it executable, and launches it detached with its output hidden.

The added files are in the published package, but nowhere in jscrambler's public source. [StepSecurity](https://www.stepsecurity.io/blog/jscrambler-npm-package-publishes-malicious-preinstall-binary) and [SafeDep](https://safedep.io/jscrambler-npm-supply-chain-compromise/) both pulled and analyzed the release, and both report no matching commit, tag, or pull request for 8.14.0 in the GitHub repository.

Its latest tag is still 8.13.0. The version was pushed straight to npm under a legitimate maintainer account, bypassing the project's normal release flow. That points to a compromised npm account or build pipeline. Which of the two has not been established.

The payload is a Rust infostealer, built for all three platforms, that sweeps a developer machine for secrets and ships them to a drop server over TLS, according to Socket's updated analysis and a statement to The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The target list is broad and aimed at developers: cloud credentials from AWS, Azure, and Google Cloud, including the metadata endpoints CI runners use; cryptocurrency wallets and seed phrases from MetaMask, Phantom, and Exodus; the Bitwarden password manager vault; browser-stored passwords and cookies; and Discord, Slack, Telegram, and Steam sessions.

It also goes after something newer: the config files for AI coding tools, including Claude Desktop, Cursor, Windsurf, VS Code, and Zed, where API keys and Model Context Protocol server credentials tend to sit.

The binaries do more than steal. On Linux, the payload links the kernel's BPF library and can load an eBPF program straight into the kernel from memory. That is a foothold in the kernel, not the userspace file access that the rest of the stealer relies on. StepSecurity and SafeDep both flagged the capability, though what the eBPF does is still being pulled apart.

The Windows and macOS builds add anti-debugging checks, and the stealer wires in persistence to survive a reboot: a hidden Windows scheduled task set to relaunch every minute, and a macOS LaunchAgent that reloads on login. Its command-and-control details stay encrypted in the binary and never surfaced in static analysis.

StepSecurity's runtime monitoring caught the dropped binary reaching out to two hard-coded IP addresses and to Tor infrastructure, the first network indicators published for the campaign.

jscrambler is a build-time tool, installed as a development dependency or run from CI. Those environments hold what the stealer collects: cloud keys, deploy tokens, and source code that a build or CI process can reach.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi31tvSsQoYD4uTw5y2PID3PwQgCXwPYz8oOnO1Y7L0KFfaSLiWm60x7RHZGMUzVWvcYJyBtzW0GtKmx4cTCluKWu-LrkxSuD4VSCI_tEfW971OnP41ygsaVhKKrJZSDAJh1oaOJiWfId-NO2EG7uFr5o0W-FZGZzjluGWPZmYzlFJ4PJVm6WLL1f0Xly4/s1700-e365/tor.png) |
| Source: Step Security |

The package sees about 15,800 downloads a week, and how many pulled the compromised version is not yet known. That is a far smaller footprint than the packages hit in the big npm compromises of the past year, which pull billions of downloads a week between them.

For a stealer aimed at build machines, though, reach was never the point. The access is.

The [Shai-Hulud worm](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) ran from an install hook to steal tokens and [spread through hundreds of packages](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/) that September. The widely used [chalk and debug](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html) packages were [taken over through a phished maintainer account](https://www.paloaltonetworks.com/blog/cloud-security/npm-supply-chain-attack/) and used to reroute crypto payments.

In March, a hijacked account pushed a cross-platform trojan into [Axios](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html), an HTTP library with more than 83 million weekly downloads. What makes the timing here sharp is that npm had just moved against this exact route: [npm 12](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/) shipped on July 8, three days before this releas...