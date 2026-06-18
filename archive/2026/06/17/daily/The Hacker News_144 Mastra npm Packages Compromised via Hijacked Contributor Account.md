---
title: 144 Mastra npm Packages Compromised via Hijacked Contributor Account
url: https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
source: The Hacker News
date: 2026-06-17
fetch_date: 2026-06-18T06:51:59.459959
---

# 144 Mastra npm Packages Compromised via Hijacked Contributor Account

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [144 Mastra npm Packages Compromised via Hijacked Contributor Account](https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html)

**Ravie Lakshmanan**Jun 17, 2026Malware / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKLWn0zHFuJ8rkb2bqILIyAGxt_-VJ13Ytmv1TRWtGJkI6Rva5Oag5LdLasE2rmenokuRvoEI2wH0Ayfe_P4_5q1Qc5FQ2MrQgUHrgD9wY6DTlYugAtj8CP7Fh0OPjKkU5LbeRKWvPEh0Ol0CmLTe4QVayeZiNlVFvU7MO5tWl-b8Lbn80hKd45q9Z1yOd/s1700-e365/npms.jpg)

As many as 144 npm packages associated with the [Mastra](https://mastra.ai/) namespace ("@mastra/\*"), a popular open-source JavaScript and TypeScript framework for building artificial intelligence (AI) applications, have been compromised as part of a software supply chain attack codenamed **easy-day-js**, per findings from [Endor Labs](https://www.endorlabs.com/learn/mastra-npm-org-compromised-multiple-packages-trojanized-to-drop-a-remote-payload-via-easy-day-js), [JFrog](https://research.jfrog.com/post/easy-day-js/), [SafeDep](https://safedep.io/mastra-npm-scope-takeover-supply-chain-attack/), [Socket](https://socket.dev/blog/mastra-npm-packages-compromised), and [StepSecurity](https://www.stepsecurity.io/blog/mastra-npm-packages-compromised-using-easy-day-js).

"A single npm account (ehindero) mass-published more than 140 malicious packages across the Mastra scope within a short window on 2026-06-17," Socket said.

The infected packages themselves do not include malicious code. Instead, it's introduced by means of a third-party library named "easy-day-js" that has been added to each package's dependency list in what has been described as an automated publishing campaign spanning 88 minutes.

In its analysis, SafeDep described "easy-day-js" as a clone of the "dayjs" date library that downloads and runs a cryptocurrency-stealing remote access trojan. The JavaScript library was published by an npm user called "sergey2016" on June 16, 2026, at 7:05 a.m. UTC as a clean, fully functional copy, with the malicious changes introduced on June 17, 2026, at 1:01 a.m. UTC.

"Because Mastra sits at the intersection of AI development and cloud infrastructure, its packages are routinely installed in environments that hold some of the most sensitive credentials in modern software development," StepSecurity said. "This makes the Mastra ecosystem an exceptionally high-value target for supply chain attackers."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The "easy-day-js" package launches an obfuscated payload that's fired during a postinstall hook, which acts as a dropper or loader for a second-stage payload retrieved from attacker-controlled infrastructure ("23.254.164[.]92") after disabling TLS certificate validation.

The payload is then executed as a detached background process, following which the loader takes steps to erase itself to minimize the forensic trail.

The final stage is a cross-platform information stealer that can harvest browser history, store data from over 160 cryptocurrency wallet browser extensions, install persistence across Windows, macOS, and Linux, and exfiltrate the captured information to a command-and-control (C2) server ("23.254.164[.]123").

The malware is also capable of polling the C2 server to receive commands, including downloading a module from an attacker-supplied URL and executing it on Windows, Linux, and macOS systems.

"The malware combined familiar supply chain techniques with practical stealth: a clean decoy version, an obfuscated postinstall loader, runtime payload download, detached execution, self-deletion, Node-themed persistence, and a remote module system," JFrog said.

"Even if the first-stage package is removed after installation, the second-stage process may continue running and may have already installed persistence. This campaign shows how a small dependency change can become an install-time compromise across a large package ecosystem."

The attackers behind the campaign are said to have hijacked the "ehindero" account, a legitimate former Mastra contributor whose scope access was never revoked. Npm has since pulled the malicious versions from the highest-profile packages and reverted their latest tag.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgF9cwWgnA3fbURa67fpzPNtRuAAoA4UDsP3SVRtp8xc64DTbOZbS6ULj9johyphenhyphenOCJGSJRcblznnaCzcxCM4Puq1OXTjcbyZLsRZxJmVoiuI-4exlxufoVpnDUWeB3Dl-hfMMPzAGuBn_Skr-GG5b7fhq1Eb7tqcxyVYmTVxbBngRs8lBEaWcUvfHqdo8DSl/s1700-e365/StepSecurity.jpg) |
| Image Source: StepSecurity |

"Mastra ships its real releases from CI through npm's trusted publisher flow, and each one carries SLSA provenance attestations," SafeDep said. "The attacker pushed the malicious versions from a personal token and dropped the provenance."

"The same fingerprint repeats across the whole scope. Mastra generated provenance on CI publishes but did not require it, so a standard npm token could still publish without attestations. A signature-verifying install (npm audit signatures, or a policy that requires attestations) would have rejected every package in this wave."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Any workstation, CI runner, or build environment that installed the affected versions should be treated as potentially compromised. It's advised to roll back to a safe version, rotate any credentials, and audit the hosts for any artifacts linked to the campaign.

"The affected packages include @mastra/core, which receives more than 918K weekly npm downloads, giving this campaign a large potential blast radius," Socket said. "Because the payload executes during installation, systems may be exposed before developers import or use the package."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),...