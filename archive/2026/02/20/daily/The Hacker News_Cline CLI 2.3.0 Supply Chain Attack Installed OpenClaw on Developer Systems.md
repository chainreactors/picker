---
title: Cline CLI 2.3.0 Supply Chain Attack Installed OpenClaw on Developer Systems
url: https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html
source: The Hacker News
date: 2026-02-20
fetch_date: 2026-02-21T04:01:10.075430
---

# Cline CLI 2.3.0 Supply Chain Attack Installed OpenClaw on Developer Systems

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

# [Cline CLI 2.3.0 Supply Chain Attack Installed OpenClaw on Developer Systems](https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html)

**Ravie Lakshmanan**Feb 20, 2026Software Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvPoczCRsYg15Y2soZNAfhG8r-8FhwlnlnpNANn6DmZ9WPYJo203gJTPDaWyrBoK8eRtHTBE2Xl5hBEIka4d0PcU2zQX5T6bl1tM1bt8Kq2sDFEplKhMlrSMWbJUhGw3nvlUbN9_3zMqrv9o8SlUdCGIea3rV2u4Z_KdV1PrGBDIcT1GYnfzsozeUy54ee/s1700-e365/cline.jpg)

In yet another software supply chain attack, the open-source, artificial intelligence (AI)-powered coding assistant [Cline CLI](https://www.npmjs.com/package/cline) was updated to stealthily install [OpenClaw](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html), a self-hosted autonomous AI agent that has become exceedingly popular in the past few months.

"On February 17, 2026, at 3:26 AM PT, an unauthorized party used a compromised npm publish token to publish an update to Cline CLI on the NPM registry: cline@2.3.0," the maintainers of the Cline package [said](https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7) in an advisory. "The published package contains a modified package.json with an added postinstall script: 'postinstall": "npm install -g openclaw@latest.'"

As a result, this causes OpenClaw to be installed on the developer's machine when Cline version 2.3.0 is installed. Cline said no additional modifications were introduced to the package and there was no malicious behavior observed. However, it noted that the installation of OpenClaw was not authorized or intended.

The supply chain attack affects all users who installed the Cline CLI package published on npm, specifically version 2.3.0, during an approximately eight-hour window between 3:26 a.m. PT and 11:30 a.m. PT on February 17, 2026. The incident does not impact Cline's Visual Studio Code (VS Code) extension and JetBrains plugin.

To mitigate the unauthorized publication, Cline maintainers have released version 2.4.0. Version 2.3.0 has since been deprecated and the compromised token has been revoked. Cline also said the npm publishing mechanism has been updated to support OpenID Connect (OIDC) via GitHub Actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

In a [post](https://x.com/MsftSecIntel/status/2024575596941263040) on X, the Microsoft Threat Intelligence team said it observed a "small but noticeable uptick" in OpenClaw installations on February 17, 2026, as a result of the [supply chain compromise](https://socket.dev/blog/cline-cli-npm-package-compromised-via-suspected-cache-poisoning-attack) of the Cline CLI package. According to [StepSecurity](https://www.stepsecurity.io/blog/cline-supply-chain-attack-detected-cline-2-3-0-silently-installs-openclaw), the compromised Cline package was downloaded roughly 4,000 times during the eight-hour stretch.

Users are advised to update to the latest version, check their environment for any unexpected installation of OpenClaw, and remove it if not required.

"Overall impact is considered low, despite high download counts: OpenClaw itself is not malicious, and the installation does not include the installation/start of the Gateway daemon," Endor Labs researcher Henrik Plate [said](https://www.endorlabs.com/learn/supply-chain-attack-targeting-cline-installs-openclaw).

"Still, this event emphasizes the need for package maintainers to not only enable trusted publishing, but also disable publication through traditional tokens – and for package users to pay attention to the presence (and sudden absence) of corresponding attestations."

### Leveraging Clinejection to Leak Publication Secrets

While it's currently not clear who is behind the breach of the npm package and what their end goals were, it comes after security researcher Adnan Khan [discovered](https://adnanthekhan.com/posts/clinejection/) that attackers could steal the repository's authentication tokens through [prompt injection](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html) by taking advantage of the fact that it is configured to automatically triage any incoming issue raised on GitHub.

"When a new issue is opened, the workflow spins up Claude with access to the repository and a broad set of tools to analyze and respond to the issue," Khan explained. "The intent: automate first-response to reduce maintainer burden."

But a misconfiguration in the workflow meant that it gave Claude excessive permissions to achieve arbitrary code execution within the default branch. This aspect, combined with a prompt injection embedded within the GitHub issue title, could be exploited by an attacker with a GitHub account to trick the AI agent into running arbitrary commands and compromise production releases.

This shortcoming, which builds upon [PromptPwnd](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html), has been codenamed Clinejection. It was introduced in a [source code commit](https://github.com/cline/cline/commit/bb1d0681396b41e9b779f9b7db4a27d43570af0c) made on December 21, 2025. The attack chain is outlined below -

* Prompt Claude to run arbitrary code in issue triage workflow
* Evict legitimate cache entries by filling the cache with more than 10GB of junk data, triggering GitHub's Least Recently Used (LRU) cache eviction policy
* Set [poisoned cache entries](https://adnanthekhan.com/2024/12/21/cacheract-the-monster-in-your-build-cache/) matching the nightly release workflow's cache keys
* Wait for the nightly publish to run at around 2 a.m. UTC and trigger on the poisoned cache entry

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"This would allow an attacker to obtain code execution in the nightly workflow and steal the publication secrets," Khan noted. "If a threat actor were to obtain the ...