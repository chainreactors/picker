---
title: Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account
url: https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
source: The Hacker News
date: 2026-05-19
fetch_date: 2026-05-20T06:05:28.701472
---

# Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account

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

# [Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)

**Ravie Lakshmanan**May 19, 2026Supply Chain Attack / Malware

[![Mini Shai-Hulud](data:image/png;base64... "Mini Shai-Hulud")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpyJDg_FqUDfeOeVX8IyhBHj9HqwkGZ-hV7b998CMLiBK2uPpmuQEN1cv1xYXJzRiznN6u_oXjA0lAGWgrkUH9EqaqfOFyW85ZQiz_Cr2YrHl1uxUHqEztt_iWG1LtRfNMpYTIqhS8vKTUOdZiNAf_r_g0r7LzqsvjmCmsr7_lv9jmXvHs5s76BEQCMnql/s1700-e365/npm-malware.jpg)

Cybersecurity researchers have discovered a fresh software supply chain attack campaign that has compromised various npm packages associated with the @antv ecosystem as part of the ongoing Mini Shai-Hulud attack wave.

"The attack affects packages tied to the npm maintainer account atool, including echarts-for-react, a widely used React wrapper for Apache ECharts with roughly 1.1 million weekly downloads," Socket [said](https://socket.dev/blog/antv-packages-compromised).

The list of affected packages include @antv packages such as @antv/g2, @antv/g6, @antv/x6, @antv/l7, @antv/s2, @antv/f2, @antv/g, @antv/g2plot, @antv/graphin, and @antv/data-set, as well as related packages outside the @antv namespace, including echarts-for-react, timeago.js, size-sensor, canvas-nest.js, and others.

The application security company said the tradecraft matches Mini Shai-Hulud, where a compromised maintainer account is leveraged to push out trojanized versions in quick succession.

The development comes as the supply chain attack campaign continues to slither its way through the software supply chain, worming through different open-source registries rapidly and infecting hundreds of software packages by embedding credential-stealing code into popular development tools.

"The potential blast radius is significant because the affected publishing account is connected to widely used packages across data visualization, graphing, mapping, charting, and React component ecosystems," Socket said. "Even if only a subset of those packages received malicious updates, the popularity of the package ecosystem creates meaningful downstream exposure for organizations that automatically pull new dependency versions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The attacker is said to have published 639 malicious versions across 323 unique packages, including 558 versions across 279 unique @antv packages. The stealer payload harvests more than 20 credential types, Amazon Web Services, Google Cloud, Microsoft Azure, GitHub, npm, SSH, Kubernetes, Vault, Stripe, database connection strings, and attempts Docker container escape via the host socket. The stealer is identical to the Mini Shai-Hulud payload used in the [SAP compromise](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html).

The collected data is eventually serialized, compressed, encrypted, and exfiltrated to a threat actor-controlled domain ("t.m-kosche[.]com:443") and to "filev2.getsession[.]org/file/" via the Session P2P network. As a fallback mechanism, the malware leverages the stolen GitHub token to create a public repository under the victim's account and commit the data in a JSON file.

The repositories feature the description "niagA oG eW ereH :duluH-iahS," which reverses to "Shai-Hulud: Here We Go Again." As of writing, there are more than [2,500 repositories](https://github.com/search?q=%22niaga%20og%20ew%20ereh%20%3Aduluh-iahs%22&type=repositories) in GitHub containing this marker.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLS63DLKZxpgcQijf7gDgxTpqUZXdYou7KAOLE_1xdRtwkFfxDQ2NtitaxgWqrHMktV-QPZoMe4CZMhW-C8XfDbIgRowetsxexFKpW3TLh9vGF-hSy8-DNUk4CKO2lw_nAIQDVuEb-zDUld4RVAT26shg1hBLYt1PhJnMJoPh9-LuMYwLyKW7sXqyxJzuL/s1700-e365/Shai-Hulud-framework.png) |
| Shai-Hulud Framework |

"These repositories are created using GitHub tokens stolen from compromised CI/CD environments," StepSecurity [said](https://www.stepsecurity.io/blog/shai-hulud-here-we-go-again-mass-npm-supply-chain-attack-hits-the-antv-ecosystem). "The sheer volume, over two thousand repositories, provides a lower bound on the number of unique environments whose credentials were successfully exfiltrated. If your GitHub token was among those stolen, the attacker has used it to create at least one of these repositories under an account they control."

Furthermore, the malware incorporates an npm propagation logic that abuses the stolen npm tokens to first validate them through the npm registry API, enumerates packages maintained by the token owner, downloads package tarballs, injects the malicious payload, adds a preinstall hook, increases the package versions, and republishes them using the compromised maintainer's identity.

"The attack uses two execution paths," SafeDep [said](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/). "Each compromised version adds a preinstall hook (bun run index.js). 630 of the 637 malicious versions also inject an optionalDependencies entry [pointing to [imposter commits](https://www.chainguard.dev/unchained/what-the-fork-imposter-commits-in-github-actions-and-ci-cd)] that delivers a second copy of the payload via the legitimate antvis/G2 GitHub repository."

"The 22-minute publish burst across 317 packages (637 versions), with an identical obfuscated payload, rules out a gradual or targeted operation. This was automated, rapid exfiltration using a stolen token."

Another noteworthy feature introduced in the latest version of the [payload](https://research.jfrog.com/post/shai-hulud-here-we-go-again/) is a [Sigstore attestation pipeline](https://x.com/MsftSecIntel/status/2056639452999471210), allowing the attacker to sign artifacts with legitimate Sigstore certificates when running in CI environments using a newly minted OIDC token. The Supply-chain Leve...