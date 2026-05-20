---
title: Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer
url: https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
source: The Hacker News
date: 2026-05-19
fetch_date: 2026-05-20T06:05:28.449325
---

# Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer

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

# [Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html)

**Ravie Lakshmanan**May 19, 2026Supply Chain Attack / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi61imbY3-QbM_mT_6WAxBXaFeZ3eXwprN147ox_bMvVqh9NrS69IwqwwL4qu2z1eRA8NfrWwyJi9bIDuREGEVZ-LdBMCGTSxdul92ZApPGrzwqOcr3b6YBKC19N97sk75izvamQxOqBzokKhF-__uaEuw74ZbKQLxKxMQWgRXSCR3FE6ULeHGxbiIhuEso/s1700-e365/nconsole.jpg)

Cybersecurity researchers have flagged a compromised version of the Nx Console extension that was published to the Microsoft Visual Studio Code (VS Code) Marketplace.

The extension in question is [rwl.angular-console](https://marketplace.visualstudio.com/items?itemName=nrwl.angular-console) (version 18.95.0), a popular user interface and plugin for code editors like VS Code, Cursor, and JetBrains. The VS Code extension has more than 2.2 million installations. The Open VSX version has not been affected by the incident.

"Within seconds of a developer opening any workspace, the compromised extension silently fetched and executed a 498 KB obfuscated payload from a dangling orphan commit hidden inside the official nrwl/nx GitHub repository," StepSecurity researcher Ashish Kurmi [said](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised).

The payload is a "multi-stage credential stealer and supply chain poisoning tool" that harvests developer secrets and exfiltrates them via HTTPS, the GitHub API, and DNS tunneling. It also installs a Python backdoor on macOS systems that abuses the GitHub Search API as a dead drop resolver for receiving further commands.

In an advisory issued Monday, the maintainers of the extension [said](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w) the root cause has been traced to one of its developers, whose machine was compromised in a recent security incident that leaked their GitHub credentials. Although the nature of the prior "incident" was not disclosed, the developer's credentials have since been temporarily revoked.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The access afforded by the credentials is said to have been abused to push an orphaned, unsigned commit to nrwl/nx, which introduces the stealer malware. The malicious action is triggered as soon as a developer opens any workspace in VS Code, leading to the installation of the Bun JavaScript runtime to run an obfuscated "index.js" payload.

The malware runs checks to avoid infecting machines likely located in the Russian/CIS time zones and launches itself as a detached background process to kick off the credential harvesting workflow, allowing it to retrieve secrets from 1Password vaults and Anthropic Claude Code configurations, and secrets associated with npm, GitHub, and Amazon Web Services (AWS).

"One capability that stands out: the payload contains full Sigstore integration, including Fulcio certificate issuance and SLSA provenance generation," StepSecurity said. "Combined with stolen npm OIDC tokens, this means the attacker could publish downstream npm packages with valid, cryptographically signed provenance attestations, making the malicious packages appear as legitimate, verified builds."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg57zzTzFXhbcEZXD8lKUO4OIdWgjL-FSyzxbAIFHT896u5OMxQH6PjsaTCl-BzaMUfvrE1gRtZY5DBOAr9MdNnyr1ZJYfTWo49xdfGyTiXD8pTjxyeqtxr3wWOganixx3wxWpPfJUFzjD9oWr5SqVa6ZI-y3iYuhsmzSY-VpA2UcSC8C2DXr7BsXHYdZ1L/s1700-e365/step.png)

The Nx team also acknowledged a "few users were compromised" as a result of this breach. Besides urging users to update to 18.100.0 or later, the maintainers have published the following indicators of compromise -

* Nx Console version 18.95.0 was installed during the exposure window between May 18, 2026, at 2:36 p.m. CEST and 2:47 p.m. CEST.
* Presence of files like ~/.local/share/kitty/cat.py, ~/Library/LaunchAgents/com.user.kitty-monitor.plist, /var/tmp/.gh\_update\_state, or /tmp/kitty-\*.
* Presence of any of the following running processes: a python process running cat.py and a process with \_\_DAEMONIZED=1 in its environment.

Affected users are recommended to terminate the aforementioned processes, delete artifacts on disk, and rotate all credentials reachable from the affected machine, including tokens, secrets, and SSH keys.

The development marks the second time the Nx ecosystem has been targeted within a year. In August 2025, several npm packages were [infected](https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware) by a credential stealer as part of a supply chain attack campaign named [s1ngularity](https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html). Unlike the previous iteration, the latest attack targets the VS Code extension.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

### Malicious npm Packages Galore

The findings coincide with the discovery of various malicious packages in the open-source repositories -

* [iceberg-javascript, supabase-javascript, auth-javascript, microsoft-applicationinsights-common, and ms-graph-types](https://safedep.io/malicious-npm-packages-claude-code-hooks/): Five npm packages containing a hidden ELF binary that backdoors Claude Code sessions to steal developer credentials.
* [noon-contracts](https://safedep.io/malicious-noon-contracts-npm-defi-rat/): an npm package that impersonates a Noon Protocol smart contract SDK to exfiltrate SSH keys, crypto wallet private keys, AWS credentials, Kubernetes secrets, all .env files, shell history, Docker/Git/npm tokens, and browser wallet storage paths.
* [martinez-polygon-clipping-tony](https://safedep.io/malicious-martinez-polygon-clipping-tony-npm-telegram-rat/)...