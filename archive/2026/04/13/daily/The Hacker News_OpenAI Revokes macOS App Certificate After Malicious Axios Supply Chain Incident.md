---
title: OpenAI Revokes macOS App Certificate After Malicious Axios Supply Chain Incident
url: https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
source: The Hacker News
date: 2026-04-13
fetch_date: 2026-04-14T04:46:07.498549
---

# OpenAI Revokes macOS App Certificate After Malicious Axios Supply Chain Incident

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

# [OpenAI Revokes macOS App Certificate After Malicious Axios Supply Chain Incident](https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html)

**Ravie Lakshmanan**Apr 13, 2026DevSecOps / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE5gb0KURzHAgdXMKzxbNFW1AJ8G2ezWXrHrLReEmbX6BKaG3-tIjiDVcjk-4nIZ3Kg2_564qiWXVVGcERIi4vaUvjqG-BuENXb7i6P3M2rdOHz-S9DOcKIHZ-pa1odUyUdTI-lLify_9CRXYcZu3hyY2LXeTMp1wMRr7mnu7yQdIIjGrFXCAecG4-XVpS/s1700-e365/openai.jpg)

OpenAI revealed a GitHub Actions workflow used to sign its macOS apps led to the download of the malicious Axios library on March 31, but noted that no user data or internal system was compromised.

"Out of an abundance of caution, we are taking steps to protect the process that certifies our macOS applications are legitimate OpenAI apps," OpenAI [said](https://openai.com/index/axios-developer-tool-compromise/) in a post last week. "We found no evidence that OpenAI user data was accessed, that our systems or intellectual property were compromised, or that our software was altered."

The disclosure comes a little over a week after Google Threat Intelligence Group (GTIG) attributed the [supply chain compromise](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html) of the popular npm package to a North Korean hacking group it tracks as [UNC1069](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html).

The attack enabled the threat actors to hijack the package maintainer's npm account to push two poisoned versions 1.14.1 and 0.30.4 that came embedded with a malicious dependency named "plain-crypto-js," which deployed a cross-platform backdoor called WAVESHAPER.V2 to infect Windows, macOS, and Linux systems.

The artificial intelligence (AI) company said a GitHub Actions workflow it uses as part of its macOS app-signing process downloaded and executed Axios version 1.14.1. The workflow, it added, had access to a certificate and notarization material used for signing ChatGPT Desktop, Codex, Codex CLI, and Atlas.

"Our analysis of the incident concluded that the signing certificate present in this workflow was likely not successfully exfiltrated by the malicious payload due to the timing of the payload execution, certificate injection into the job, sequencing of the job itself, and other mitigating factors," the company said.

Despite finding no evidence of data exfiltration, OpenAI said it's treating the certificate as compromised and that it's revoking and rotating it. As a result, older versions of all its macOS desktop apps will no longer receive updates or support starting May 8, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

This also means that apps signed with the previous certificate will be blocked by macOS security protections by default, preventing them from being downloaded or launched. The earliest releases signed with their updated certificate are listed below -

* ChatGPT Desktop - 1.2026.071
* Codex App - 26.406.40811
* Codex CLI - 0.119.0
* Atlas - 1.2026.84.2

As part of its remediation efforts, OpenAI is also working with Apple to ensure software signed with the previous certificate cannot be newly notarized. The 30-day window till May 8, 2026, is a way to minimize user disruption and give them enough time to make sure they are updated to the latest version, it pointed out.

"In the event that the certificate was successfully compromised by a malicious actor, they could use it to sign their own code, making it appear as legitimate OpenAI software," OpenAI said. "We have stopped new software notarizations using the old certificate, so new software signed with the old certificate by an unauthorized third-party would be blocked by default by macOS security protections unless a user explicitly bypasses them."

### Two Supply Chain Attacks Rock March

The breach of Axios, one of the most widely used HTTP client libraries, was one of the two major supply chain attacks that took place in March aimed at the open-source ecosystem. The [other incident](https://ramimac.me/teampcp/) targeted [Trivy](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/), a vulnerability scanner maintained by Aqua Security, resulting in [cascading impacts](https://snyk.io/articles/trivy-github-actions-supply-chain-compromise/) across five ecosystems, affecting a number of other popular libraries depending on it.

The attack, the work of a cybercriminal group called [TeamPCP](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html) (aka UNC6780), deployed a credential stealer dubbed SANDCLOCK that facilitated the extraction of sensitive data from developer environments. Subsequently, the threat actors weaponized the stolen credentials to compromise npm packages and push a self-propagating worm named [CanisterWorm](https://www.stepsecurity.io/blog/canisterworm-how-a-self-propagating-npm-worm-is-spreading-backdoors-across-the-ecosystem).

Days later, the crew used secrets pilfered from the Trivy intrusion to inject the same malware into two GitHub Actions workflows maintained by Checkmarx. The threat actors then followed it up by publishing malicious versions of [LiteLLM](https://docs.litellm.ai/blog/security-update-march-2026) and [Telnyx](https://www.akamai.com/blog/security-research/telnyx-pypi-2026-teampcp-supply-chain-attacks) to the Python Package Index (PyPI), both of which use Trivy in their CI/CD pipeline.

"The Telnyx compromise indicates a continued change in the techniques used in TeamPCP's supply chain activity, with adjustments to tooling, delivery methods, and platform coverage," Trend Micro [said](https://www.trendmicro.com/en_us/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html) in an [analysis of the attack](https://www.trendmicro.com/en_us/research/26/c/your-ai-stack-just-handed-over-your-root-keys-inside-the-litellm-pypi-breach.html).

"In just eight days, the actor has pivoted across security scanners, AI infrastructure, and now telecommunications tooling, evolving their delivery from inline Base64 to .pth auto-execution, and ultimately to split-file WAV steganography, while also expanding from Linux-only to dual-platform targeting with Win...