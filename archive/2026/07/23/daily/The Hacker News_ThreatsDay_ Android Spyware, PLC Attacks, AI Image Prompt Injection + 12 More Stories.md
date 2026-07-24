---
title: ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories
url: https://thehackernews.com/2026/07/threatsday-android-spyware-plc-attacks.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.125126
---

# ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories

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

# [ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories](https://thehackernews.com/2026/07/threatsday-android-spyware-plc-attacks.html)

**Ravie Lakshmanan**Jul 23, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsmJNuemIhGxFuSqY6pq1opCEJECkmIjXm5VnOqOAEjfpoLxQ89Q-qXBqKQmM8YnwyVP2_feUo4c-VLZ3cC6s_J0VCXdwhLKFezoK1-i4lWQs68yXaZS8XtHGAsDj5zsdOToB7yD1QHzuMYIVQFvb14U6Zhd1cqDOm78tRY1O3v_1LFr7CC-4ItBLpLgZ3/s1700-e365/th.jpg)

Most of this week's trouble came dressed as something useful.

A package stole data. A fake extension opened remote access. A safety app became spyware. An image gave hidden orders to an AI agent. Other threats hid in open systems, weak code, and normal network traffic.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

The danger was easy to miss because it looked ordinary. Here is the full list:

1. Support uploads face cutoff

   [GitHub Announces GHES Security Change](https://github.blog/changelog/2026-07-22-upcoming-ghes-change-impacting-uploading-support-bundles/)

   GitHub has announced an upcoming security change that may affect GitHub Enterprise Server (GHES) support bundle uploads. "Beginning August 18, 2026, GitHub will start rejecting command-line support bundle uploads from older GHES appliances that have not been updated with the required security patches," GitHub [said](https://github.blog/changelog/2026-07-22-upcoming-ghes-change-impacting-uploading-support-bundles/). "To avoid any disruption when submitting support bundles with ghe-support-bundle, ghe-cluster-support-bundle, or ghe-support-upload commands, please update your GHES instance to the latest patch release available for your current version line." At minimum, the required patch versions are: 3.21.3, 3.20.5, 3.19.9, 3.18.12, and 3.17.18.
2. Npm install triggers stealer

   [Npm Dropper Delivers macOS Infostealer](https://safedep.io/malicious-copilot-mcp-apex-npm-macos-infostealer/)

   An npm package named @copilot-mcp/apex has been found to act as a postinstall dropper that installs a macOS infostealer on any machine that runs npm install or npx @copilot-mcp/apex. The same payload is said to have been distributed via another dropper named @apexfdn/apex. "On macOS, the dropper's second stage decrypts and runs an AppleScript payload through osascript," SefeDep [said](https://safedep.io/malicious-copilot-mcp-apex-npm-macos-infostealer/). "The decrypted payload is a 707-line [AMOS-family stealer](https://thehackernews.com/2024/01/atomic-stealer-gets-upgrade-targeting.html): it phishes the login password through a fake system prompt, then harvests browser credentials, 20+ crypto wallets, SSH keys, AWS and Kubernetes credentials, the login Keychain, Telegram, and shell history into /tmp/osalogging.zip and uploads it over chunked HTTPS PUT to attacker infrastructure." The malware also sets up a LaunchAgent that polls the attacker's command-and-control server every 60 seconds to ensure that the infection outlives the initial exfiltration.
3. Fake extension opens backdoor

   [Counterfeit VS Extension Steals Machine Data](https://www.manifold.security/blog/a-beaconing-counterfeit-extension-on-the-vs-code-marketplace-the-markdown-all-pro-extension)

   A Microsoft Visual Studio Code (VS Code) marketplace extension called "Markdown All Pro" ("markdown.markdown-all-pro") has been found to impersonate the legitimate "Markdown All in One" extension with over 14 million downloads. Installing the rogue extension allows the machine's details to be shipped to the attacker and opens a channel through which the operator can send any additional commands without having to touch the extension again. "On install, these beacon the machine's username and hostname to a hardcoded IP over cleartext HTTP and fetch a remote file to disk, with no user interaction required," Manifold Security [said](https://www.manifold.security/blog/a-beaconing-counterfeit-extension-on-the-vs-code-marketplace-the-markdown-all-pro-extension). "This one is small, but it deliberately misrepresents itself as a trusted tool, and the remote fetch it performs is a live delivery channel whose payload the operator can change at any time." After the extension was removed by Microsoft, it reappeared under an identical name ("MarkdownLinks.markdown-links-pro"). The second extension has since been taken down as well.
4. Old releases locked down

   [PyPI Rejects New Files After 14 Days](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/)

   The Python Package Index (PyPI) has made a new security change that rejects new files being uploaded to releases that are older than 14 days. "This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised," PyPI [said](https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/). "As far as we are aware, this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible."
5. Phishing delivers banking malware

   [Lampion Malware Targets Portuguese Users](https://www.acronis.com/en/tru/posts/lampions-portugal-focused-phishing-campaign-delivers-multistage-malware/)

   A new malware campaign is targeting Portuguese users through phishing emails impersonating financial and administrative communications to deliver the [Lampion](https://thehackernews.com/2023/03/mispadu-banking-trojan-targets-latin.html) banking malware. First publicly documented in December 2019, the Brazilian banking malware family is derived from the ChePro lineage, and has consistently targeted Portugal and other Portuguese-speaking users. "Initial payloads are delivered through ZIP archives containing heavily obfuscated HTML files designed to evade static detection and analysis," Acr...