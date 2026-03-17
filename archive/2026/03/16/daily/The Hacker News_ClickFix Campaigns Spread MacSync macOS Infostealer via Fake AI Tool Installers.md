---
title: ClickFix Campaigns Spread MacSync macOS Infostealer via Fake AI Tool Installers
url: https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html
source: The Hacker News
date: 2026-03-16
fetch_date: 2026-03-17T04:17:12.150482
---

# ClickFix Campaigns Spread MacSync macOS Infostealer via Fake AI Tool Installers

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [ClickFix Campaigns Spread MacSync macOS Infostealer via Fake AI Tool Installers](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html)

**Ravie Lakshmanan**Mar 16, 2026Malvertising / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFYjqyJvKKEaCGLTQo4-iMO_9Iq0V0lJVBlggKNorjB_DmPjq0sw_wl0EJ1oklawc4r9V7Axxk_J1WW1HEbIZwKRo8ui7thLccLTtcD6ePD0EcbJCvXWa0eAv0BYdV1cYO2HcDEIbB5GMNxUnV0TGTD3O2YAnOUcPqFJvTPPbYhufQ-sBuh1K01E6Szx9O/s1700-e365/macos-clickfix.jpg)

Three different ClickFix campaigns have been found to act as a delivery vector for the deployment of a macOS information stealer called [MacSync](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html).

"Unlike traditional exploit-based attacks, this method relies entirely on user interaction – usually in the form of copying and executing commands – making it particularly effective against users who may not appreciate the implications of running unknown and obfuscated terminal commands," Sophos researchers Jagadeesh Chandraiah, Tonmoy Jitu, Dmitry Samosseiko, and Matt Wixey [said](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers).

It's currently not known if the campaigns are the work of the same threat actor. The use of ClickFix lures to distribute the malware was also flagged by Jamf Threat Labs in December 2025. The details of the three campaigns are as follows -

* November 2025: A campaign that used the OpenAI Atlas browser as bait, delivered via sponsored search results on Google, to direct users to a fake Google Sites URL with a download button that, when clicked, displayed instructions to open the Terminal app and paste a command to it. This action downloaded a shell script, which prompts the user to enter the system password and runs MacSync with user-level permissions.
* December 2025: A [malvertising campaign](https://guard.io/blog/mac-storage-fix-google-ads-scam) that leveraged sponsored links tied to searches for queries like "how to clean up your Mac" on Google to lead users to [shared conversations](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html) on the legitimate OpenAI ChatGPT site to give the impression that the links were safe. The ChatGPT conversations redirected victims to malicious GitHub-themed landing pages that tricked users into running malicious commands on the Terminal app.
* February 2026: A campaign targeting Belgium, India, and parts of North and South America that distributed a new variant of MacSync delivered through ClickFix lures. The latest iteration supports dynamic AppleScript payloads and in-memory execution to evade static analysis, bypass behavioral detections, and complicate incident response.

The shell script launched after running the Terminal command is designed to contact a hard-coded server and retrieve the AppleScript infostealer payload, while simultaneously taking steps to remove evidence of data theft. The stealer is equipped to harvest a wide range of data from compromised hosts, including exfiltrating credentials, files, keychain databases, and seed phrases from cryptocurrency wallets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The latest findings suggest the threat actors are adapting the formula to stay one step ahead of security tools, while weaponizing the trust associated with ChatGPT conversations to convince users to run malicious commands.

The new variant observed in the most recent campaign "likely represents the malware developer adjusting to OS and software security measures to maintain effectiveness," Sophos said. "Refinements to the typical ClickFix social engineering tactics are therefore one way in which such campaigns may continue to evolve in the future."

In recent months, ClickFix campaigns have used legitimate platforms like Cloudflare Pages (pages.dev), Squarespace, and Tencent EdgeOne to host bogus instructions for installing developer tools like Anthropic's Claude Code. The URLs are distributed via malicious search engine ads.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCW2Ib1JQNnsbeAVawmEAeLAKKB3LoNCdF4q89rGf8oL-zO96Roy0cDHAUxPLrG9-_QMcT9o9_TGo0dYuTbOwh2yjp8E7vJv1B1pryro0oMHU346xnMbsBVz6dq9hdnji5USwHbFKsKQfvmvdN7bUUESXquL7FC-ZAK6zo-_maf_DDc77WPw-8MPW-fcqr/s1700-e365/macos-clickfix.png)

The instructions, as before, deceive victims into [installing infostealer malware](https://www.pillar.security/resources/installfix-fake-claude-code-amatera-stealer) like [Amatera Stealer](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html) instead. The social engineering attack has been codenamed [InstallFix](https://pushsecurity.com/blog/installfix/) or [GoogleFix](https://x.com/bananahacks/status/2030618128787390600). According to Nati Tal, head of Guardio Labs, similar infection chains lead to the deployment of Alien infostealer on Windows and Atomic Stealer on macOS.

The PowerShell command executed after pasting and running the supposed installation command for Claude Code fetches a legitimate Chrome extension package within a malicious HTML Application (HTA) file, which then launches an obfuscated .NET loader for Alien in memory, per Tal.

"While traditional ClickFix attacks need to manufacture a reason for the user to run a command: a fake CAPTCHA, a fabricated error message, a bogus system prompt — InstallFix doesn't need any of that," Push Security said. "The pretext is simply the user wanting to install legit software."

According to Pillar Security, there have been at least 20 distinct malware campaigns that have targeted artificial intelligence (AI) and vibe coding tools between February and March 2026. These include code editors, AI agents, large language models (LLM) platforms, AI-powered browser extensions, AI video generators, and AI business tools. Of these, nine ha...