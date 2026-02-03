---
title: Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users
url: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
source: The Hacker News
date: 2026-02-02
fetch_date: 2026-02-03T04:11:05.768209
---

# Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)

**Ravie Lakshmanan**Feb 02, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrHsgrh_iIHVwJdfZ-6tSVag1fs71bd15QISN82bzqvxchcyJGuWdbtZRqQ25tJC_HoeaGAMI3phpFy_TAy2NYbSpJTwuTJ5jIz_QKmNPTv_zqA2GNvuozLGpKCqTa-OI1Hp-zOy_B8wjkvoYcBn56g09PpoQOMd568LfGiH7J0Ee0hg65eBaHSWxDe92m/s1700-e365/OpenClaw-skills.jpg)

A security audit of 2,857 skills on ClawHub has found 341 malicious skills across multiple campaigns, according to [new findings](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) from Koi Security, exposing users to new supply chain risks.

[ClawHub](https://www.clawhub.ai/skills) is a marketplace designed to make it easy for [OpenClaw](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html) users to find and install third-party skills. It's an extension to the OpenClaw project, a self-hosted artificial intelligence (AI) assistant formerly known as both Clawdbot and Moltbot.

The analysis, which Koi conducted with the help of an OpenClaw bot named Alex, found that 335 skills use fake pre-requisites to install an Apple macOS stealer named [Atomic Stealer](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html) (AMOS). This set has been codenamed **ClawHavoc**.

"You install what looks like a legitimate skill – maybe solana-wallet-tracker or youtube-summarize-pro," Koi researcher Oren Yomtov said. "The skill's documentation looks professional. But there's a 'Prerequisites' section that says you need to install something first."

This step involves instructions for both Windows and macOS systems: On Windows, users are asked to download a file called "openclaw-agent.zip" from a GitHub repository. On macOS, the documentation tells them to copy an installation script hosted at glot[.]io and paste it into the Terminal app. The targeting of macOS is no coincidence, as reports have [emerged](https://www.businessinsider.com/clawdbot-ai-mac-mini-2026-1) of people [buying Mac Minis](https://mashable.com/article/jan-31-apple-mac-mini-deal) to run the AI assistant 24x7.

Present within the password-protected archive is a trojan with keylogging functionality to capture API keys, credentials, and other sensitive data on the machine, including those that the bot already has access to. On the other hand, the glot[.]io script contains obfuscated shell commands to fetch next-stage payloads from an attacker-controlled infrastructure.

This, in turn, entails reaching out to another IP address ("91.92.242[.]30") to retrieve another shell script, which is configured to contact the same server to obtain a universal Mach-O binary that exhibits traits consistent with Atomic Stealer, a commodity stealer available for $500-1000/month that can harvest data from macOS hosts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

According to Koi, the malicious skills masquerade as

* ClawHub typosquats (e.g., clawhub, clawhub1, clawhubb, clawhubcli, clawwhub, cllawhub)
* Cryptocurrency tools like Solana wallets and wallet trackers
* Polymarket bots (e.g., polymarket-trader, polymarket-pro, polytrading)
* YouTube utilities (e.g., youtube-summarize, youtube-thumbnail-grabber, youtube-video-downloader)
* Auto-updaters (e.g., auto-updater-agent, update, updater)
* Finance and social media tools (e.g., yahoo-finance-pro, x-trends-tracker)
* Google Workspace tools claiming integrations with Gmail, Calendar, Sheets, and Drive
* Ethereum gas trackers
* Lost Bitcoin finders

In addition, the cybersecurity company said it identified skills that hide reverse shell backdoors inside functional code (e.g., better-polymarket and polymarket-all-in-one), or exfiltrate bot credentials present in "~/.clawdbot/.env" to a webhook[.]site (e.g., rankaj).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdUIlSL9qpCVbfy1TNUn-HizuE9n6MdFG5YHsHFM9xPa-VGEUo9aaIOAYFIngxa3eySnljrSlNEswxcdWoqbVIa1r2QMMl6PKzfprbnsb-8Gr4wIa-CElQxwA-lufP6EutwkSLX5Zh-C-3-KiLa61nzkZF1nIw3_CVdEQ290WxL7gAXniTyHy2c5irJ_be/s1700-e365/skill-malware-2.png)

The development coincides with a report from OpenSourceMalware, which also flagged the same ClawHavoc campaign targeting OpenClaw users.

"The skills masquerade as cryptocurrency trading automation tools and deliver information-stealing malware to macOS and Windows systems," a security researcher who goes by the online alias 6mile [said](https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto).

"All these skills share the same command-and-control infrastructure (91.92.242[.]30) and use sophisticated social engineering to convince users to execute malicious commands, which then steal crypto assets like exchange API keys, wallet private keys, SSH credentials, and browser passwords."

## OpenClaw Adds a Reporting Option

The problem stems from the fact that ClawHub is open by default and allows anyone to upload skills. The only restriction at this stage is that a publisher must have a GitHub account that's at least one week old.

The issue with malicious skills [hasn't gone unnoticed](https://x.com/steipete/status/2018297794952651111) by OpenClaw's creator Peter Steinberger, who has since rolled out a reporting feature that allows signed-in users to flag a skill. "Each user can have up to 20 active reports at a time," the documentation [states](https://docs.openclaw.ai/tools/clawhub#security-and-moderation). "Skills with more than 3 unique reports are auto-hidden by default."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The findings underscore how open-source ecosystems continue to be abused by threat actors, who are now piggybacking on OpenClaw's sudden popularity to orchestrate malicious campaigns and distribute ...