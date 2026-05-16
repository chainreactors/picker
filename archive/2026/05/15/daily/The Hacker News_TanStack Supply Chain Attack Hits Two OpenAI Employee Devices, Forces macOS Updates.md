---
title: TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces macOS Updates
url: https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
source: The Hacker News
date: 2026-05-15
fetch_date: 2026-05-16T05:15:45.085975
---

# TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces macOS Updates

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces macOS Updates](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html)

**Ravie Lakshmanan**May 15, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1l4Vq20M4553fkDfGbO9VqLV9Au-6EefivLp8HT2W5QxJvgWf1mr6pg5xsbC5j3FCJzOOCJv_CImY1LjjFYIN_25ajki1iS_EVPvTyeVY7bC3ogcQFzHmE1Xyaz3cRXneilC0rWcb8dLbUapLI_jZ-uBaUkku48absoxM6TG16jS3xxtw9lhhtCvJmemK/s1700-e365/chatgpt.jpg)

OpenAI has disclosed that two of its employee devices in its corporate environment were impacted via the [Mini Shai-Hulud supply chain attack](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html) on TanStack, but noted that no user data, production systems, or intellectual property were compromised or modified in an unauthorized manner.

"Upon identification of the malicious activity, we worked quickly to investigate, contain, and take steps to protect our systems," OpenAI [said](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/). "We observed activity consistent with the malware's publicly described behavior, including unauthorized access and credential-focused exfiltration activity, in a limited subset of internal source code repositories to which the two impacted employees had access."

The artificial intelligence (AI) upstart said only limited credential material was successfully transferred from these code repositories, adding no other information or code was impacted.

Upon being alerted of the activity, OpenAI said it isolated impacted systems and identities, revoked user sessions, rotated all credentials across impacted repositories, temporarily restricted code-deployment workflows, and audited user and credential behavior.

Since the impacted repositories included signing certificates for iOS, macOS, and Windows products, the company has taken the step of revoking the certificates and issuing new ones. As a result, macOS users of ChatGPT Desktop, Codex App, Codex CLI, and Atlas are required to update their apps to the latest versions.

"This helps prevent any risk, however unlikely, of someone attempting to distribute a fake app that appears to be from OpenAI," OpenAI said. "Users do not need to take any action for Windows and iOS apps."

The certificates are scheduled to be revoked on June 12, 2026, after which new downloads and launches of apps signed with the previous certificate will be blocked by built-in macOS protections. Users are therefore advised to apply the updates before the cut-off date for optimal protection.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

This is the second time OpenAI has rotated its code-signing certificates for its macOS in as many months. Around mid-April 2026, it [rotated](https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html) the certificates after a GitHub Actions workflow used to sign its macOS apps led to the download of the malicious Axios library on March 31, which was compromised by a North Korean hacking group called UNC1069.

"This incident reflects a broader shift in the threat landscape: attackers are increasingly targeting shared software dependencies and development tooling rather than any single company," OpenAI said.

"Modern software is built on a deeply interconnected ecosystem of open-source libraries, package managers, and continuous integration and continuous deployment infrastructure, which means that a vulnerability introduced upstream can propagate widely and quickly across organizations."

The development comes close on the heels of TeamPCP claiming a number of fresh victims, compromising hundreds of packages associated with TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI as part of an ongoing supply chain attack campaign designed to push malware to downstream developers and steal credentials from their systems to further extend the scale of the breaches.

"Just to be clear, no maintainer was phished, had a password leak, or a token stolen from their account," TanStack [said](https://tanstack.com/blog/incident-followup). "The attacker managed to engineer a path where our own CI pipeline stole its own publish token for them, at the exact moment it was created, by way of a cache that everyone in the chain implicitly trusted. It is a sophisticated approach that we hadn't anticipated and that we're taking very seriously."

TeamPCP has since [announced](https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html#supply-chain-contest) a supply chain attack contest in partnership with Breached cybercrime, offering participants with a $1,000 in Monero to compromise open-source packages using the Shai-Hulud worm that it has made freely available to others. The hacking group has also threatened to leak about 5GB of internal source code from Mistral AI, asking for $25,000 BIN from prospective buyers.

"We are looking for $25k BIN or they can pay this and we will shred these permanently, only selling to the best offer and limited to one person, if we cannot find a buyer within a week we will leak all of these for free to the forums," TeamPCP [said](https://x.com/H4ckmanac/status/2054671490210009307) in the post.

In an updated advisory, Mistral AI [confirmed](https://docs.mistral.ai/resources/security-advisories) it was impacted by a supply chain attack caused by the compromise of TanStac, leading to the release of trojanized versions of its npm and PyPI SDKs. It also said a lone developer device was impacted in the hack. There is no evidence to suggest its infrastructure was breached.

A deeper analysis of the modular Python toolkit delivered to Linux systems via the guardrails-ai and mistralai packages has uncovered that the primary command-and-control (C2) server address ("83.142.209[.]194") is hard-coded. In case the primary C2 becomes unreachable, a fallback mechanism c...