---
title: Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens
url: https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html
source: The Hacker News
date: 2026-02-16
fetch_date: 2026-02-17T04:21:51.131118
---

# Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html)

**Ravie Lakshmanan**Feb 16, 2026Artificial Intelligence / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeWsmjwrJY11WFbrvqG71cU065qr7gt-yAQRQv18KoDqnPG5x-HWXkFR1wwAmGNT2ujE6p0mlp1VsqvuDBnEokfqkSFtQX0bVdqdOxiZMZ2WXmqqVc1wrPOdZQ8kFgssie0Cs-1dmmyA7_QZzMhMTM0hcFjbXZtrhoTCwJFupvEgmLEYInUaGST-dmzAOz/s1700-e365/openclaw-hacked.jpg)

Cybersecurity researchers disclosed they have detected a case of an information stealer infection successfully exfiltrating a victim's [OpenClaw](https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html) (formerly Clawdbot and Moltbot) configuration environment.

"This finding marks a significant milestone in the evolution of infostealer behavior: the transition from stealing browser credentials to harvesting the 'souls' and identities of personal AI [artificial intelligence] agents," Hudson Rock [said](https://www.infostealers.com/article/hudson-rock-identifies-real-world-infostealer-infection-targeting-openclaw-configurations/).

Alon Gal, CTO of Hudson Rock, told The Hacker News that the stealer was likely a variant of Vidar based on the infection details. Vidar is an off-the-shelf information stealer that's known to be active since late 2018.

That said, the cybersecurity company said the data capture was not facilitated by a custom OpenClaw module within the stealer malware, but rather through a "broad file-grabbing routine" that's designed to look for certain file extensions and specific directory names containing sensitive data.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

This included the following files -

* openclaw.json, which contains details related to the [OpenClaw gateway token](https://docs.openclaw.ai/gateway), along with the victim's redacted email address and workspace path.
* device.json, which contains cryptographic keys for secure pairing and signing operations within the OpenClaw ecosystem.
* [soul.md](https://docs.openclaw.ai/reference/templates/SOUL), which contains details of the agent's core operational principles, behavioral guidelines, and ethical boundaries.

It's worth noting that the theft of the gateway authentication token can allow an attacker to connect to the victim's local OpenClaw instance remotely if the port is exposed, or even masquerade as the client in authenticated requests to the AI gateway.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXmaxLqVhpMpdIjbRs0CyGv8auUnhAM_mnVUZlqq8xYfX66z5r6takHTkuVchN4XdmLR2Skv02qsOLaBCy2ZIQR_6cmyyZVM7WyN8pRDiml3aMbELl0mFv0cANQ5Iw4RaZCMr0S9XWMrYj_RKXEjgNkNfvFLqwUEPZwFbSfhRMI48gVV4v2l6MaHRWU81B/s1700-e365/openclaw.png)

"While the malware may have been looking for standard 'secrets,' it inadvertently struck gold by capturing the entire operational context of the user's AI assistant," Hudson Rock added. "As AI agents like OpenClaw become more integrated into professional workflows, infostealer developers will likely release dedicated modules specifically designed to decrypt and parse these files, much like they do for Chrome or Telegram today."

The disclosure comes as [security issues](https://jfrog.com/blog/giving-openclaw-the-keys-to-your-kingdom-read-this-first/) with OpenClaw prompted the maintainers of the open-source agentic platform to [announce](https://trust.openclaw.ai) a partnership with VirusTotal to scan for malicious skills uploaded to ClawHub, establish a threat model, and add the ability to [audit for potential misconfigurations](https://docs.openclaw.ai/gateway/security).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKowa-Tw7Qt8vStnr5yBxAYV_a3OqmMgIOl4PQDdvuYOZZjJ59YncgXxeKtlZRgSykL4I8tLZKsPnuAPq190r4bimq09g80E1d7hINTUENt3H5nahyphenhyphen4Z2ORwC0RSF_5A60ELQTLTGrbHr4CgJrDzqMk2H0Nqeo-2wQMB67NwZefpUzL8SS2drTizo6DMnO/s1700-e365/star.jpg)

Last week, the OpenSourceMalware team detailed an ongoing ClawHub malicious skills campaign that uses a new technique to bypass VirusTotal scanning by hosting the malware on lookalike OpenClaw websites and using the skills purely as decoys, instead of embedding the payload directly in their SKILL.md files.

"The shift from embedded payloads to external malware hosting shows threat actors adapting to detection capabilities," security researcher Paul McCarty [said](https://opensourcemalware.com/blog/malicious-clawhub-skills-hide-in-plain-sight). "As AI skill registries grow, they become increasingly attractive targets for supply chain attacks."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Another [security problem](https://www.ox.security/blog/moltbook-blocks-account-deletion-privacy-risks/) highlighted by OX Security concerns [Moltbook](https://www.moltbook.com), a Reddit-like internet forum designed exclusively for artificial intelligence agents, mainly those running on OpenClaw. The research found that an AI Agent account, once created on Moltbook, cannot be deleted. This means that users who wish to delete the accounts and remove the associated data have no recourse.

What's more, an analysis published by SecurityScorecard's STRIKE Threat Intelligence team has also found [hundreds of thousands of exposed OpenClaw instances](https://declawed.io), likely exposing users to remote code execution (RCE) risks.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj72tdyrOUZ57-ssgqzO3i8raTYWPWGktIK2HRtNwg8-KA6HLHq9-MIZ-05JBSSiPZkHYmBKuIeRO-mqPBkW_AcX_xIgwOzzPuRaG8KZXCtQKin5DRPbyns8EN0UTvIJKw1rJYB9DQHE9zqvr8UTzdIw-rA3GnLVo5TzQCLXYT-jeU-V9VJavpesFdvg0G/s1700-e365/open.png) |
| Fake OpenClaw Website Serving Malware |

"RCE vulnerabilities allow an attacker t...