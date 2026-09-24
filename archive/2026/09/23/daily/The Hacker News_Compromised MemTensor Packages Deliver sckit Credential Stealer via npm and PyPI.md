---
title: Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI
url: https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:24.186511
---

# Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI](https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html)

**Ravie Lakshmanan**Sep 23, 2026Malware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFThFSFsti-2SIka75bNuMKpyJHtOW2ZPrZtcSjbjFQ64GCNn0WtdssYuWlVTbhaLB5cAJ0vu8FgyNmNsDa8g0Ijy-D1zP4FW7ihVfAjk9xWMYDMMdfZPICGyVdjeDwH3-jyKLHOUnjfaXBJIMxGn_3ngeXFsbb4CLnOibRd4fbwXHYpBkMQTcBQAf0edq/s1700-nu-rw-lo-l85-e365/npm-pypi.jpg)

Unknown threat actors have managed to compromise two legitimate MemTensor packages across the npm and Python Package Index (PyPI) repositories to push a platform-specific Go-based implant dubbed **sckit** designed for Windows, Linux, and macOS.

According to reports from [Aikido](https://www.aikido.dev/blog/supplychain-local-memtensor-npm-pypi), [SafeDep](https://safedep.io/memtensor-sckit-worm-npm-pypi/), [Socket](https://socket.dev/blog/memtensor-compromise), and [StepSecurity](https://www.stepsecurity.io/blog/sckit-supply-chain-worm-hits-memtensor-npm-pypi-scopes), the libraries in question below -

* [@memtensor/memos-cloud-openclaw-plugin](https://www.npmjs.com/package/%40memtensor/memos-cloud-openclaw-plugin) versions 0.1.21, 0.1.23 and 0.1.25 (versions 0.1.22 and 0.1.24 are clean)
* [MemoryOS](https://pypi.org/project/MemoryOS/) version 2.0.34 (project currently quarantined on PyPI)

The malicious npm package versions include a "hidden Go payload into a legitimate AI memory integration. Versions 0.1.21, 0.1.23, and 0.1.25 contain code that launches the payload when the agent gateway starts and whenever the plugin handles a memory-recall event," StepSecurity said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"The launcher passes the host process environment and, during recall, the user's prompt text directly to the malicious executable."

The PyPI package, on the other hand, starts the statically-linked Go binary as soon as the "memos" module is imported into an application.

Regardless of the ecosystem targeted, the end goal is to launch a cross-platform credential-stealing payload capable of harvesting sensitive data from cloud services, source-code platforms, package registries, and developer tools and exfiltrating the details to an external server ("skyleen[.]fr").

According to Socket, targets include npm, PyPI, GitHub, GitLab, AWS, Vault and SSH secrets -

* Credential files (.npmrc, .vault-token, id\_ecdsa, credentials.db, access\_tokens.json and stored\_tokens)
* Environment variables that indicate tokens, passwords, API keys, private keys, session cookies and database or message-broker connection strings (e.g., NPM\_TOKEN and PYPI\_API\_TOKEN)
* AWS access keys, GitHub and GitLab tokens, npm and PyPI tokens, Hugging Face, HashiCorp Vault, Slack, Stripe and SendGrid keys, and JWTs

SafeDep, in its analysis of the supply chain attack, said the attacker obtained the publish tokens from MemTensor's own GitHub Actions release pipelines by pushing commits that caused the workflow to hand over the npm or PyPI token.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEih9Eq3x05ST2UXweOaS-XCZ1cdO7H_JA7mKniiQTEp3M1QHZBFvppYcCVWEe-GzOc6NzP9ApIc7Kn6adsYciQ3J3Okl185Ji1enErQai6l2G2XZ5AXUWkyU5b523LXogsByGTl-1iw6l_UFXFCYTOiIxtEcPIvGuPmGjVqUnU1fOanLLYbnbzHnnzBuPcN/s1700-nu-rw-lo-l85-e365/sckit.jpg)

A deeper examination of the implant suggests that it can function like a worm by self-proliferating through GitHub and direct npm and PyPI package publishing. As of writing, it's unclear if there are packages other than MemTensor that are impacted by the compromise.

"It collects credentials from developer machines and from CI jobs," SafeDep [said](https://safedep.io/sckit-go-implant-framework/). "It receives signed tasks from a command-and-control (C2) server. It also contains templates to install itself in npm packages, Python packages, and GitHub Actions workflows."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

Given that the malicious versions of the npm packages are still available for download, it's essential to pin the packages to a safe baseline version (0.1.20 for the npm package, 2.0.33 for the PyPI package), rotate exposed secrets, kill any sckit process, and block "skyleen[.]fr" and all its subdomains.

"The MemOS Cloud plugin connects the OpenClaw agent runtime to a memory service," StepSecurity said. "Its normal work includes recalling relevant memories before an agent processes a prompt and adding memories after a run. The package also declares integration points for the Clawdbot and Moltbot runtimes."

"This places the plugin inside a process that routinely handles user input and may inherit valuable credentials. On a developer workstation, the same user account can have access to cloud configuration, source repositories, package publishing tokens, and application secrets. In automation, the process may receive credentials injected for a particular job."

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

[Cloud s...