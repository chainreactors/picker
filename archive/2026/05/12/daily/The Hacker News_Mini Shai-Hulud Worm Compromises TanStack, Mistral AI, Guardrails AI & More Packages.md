---
title: Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages
url: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
source: The Hacker News
date: 2026-05-12
fetch_date: 2026-05-13T05:47:30.073475
---

# Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages

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

# [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)

**Ravie Lakshmanan**May 12, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXIhs2kZt0YGdDcd-Io67mq1GIN_iI_71LYhuin4qqmlgUgCuZ3fGUvglg_5nh5DK8kfPP8RHki86yMyqh4rTE27PGgPBh4RQjkh91-QGoB8cav5NUsYAwcV3ZJ7aEf-uEoH3pLGQ2eWuCh8lZSWAlTIa2U5I6eeB3HZmYMn4q-YoV7Ytmkpr1tN0lC2rG/s1700-e365/mistral.jpg)

**TeamPCP**, the threat actor behind the recentsupply chain attack spree, has been linked to the compromise of the npm and PyPI packages from TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI as part of a fresh Mini Shai-Hulud campaign.

The affected npm packages have been modified to include an obfuscated JavaScript file ("router\_init.js") that's designed to profile the execution environment and launch a comprehensive credential stealer capable of targeting cloud providers, cryptocurrency wallets, AI tools, messaging apps, and CI systems, including Github Actions, multiple reports from [Aikido Security](https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised), [Endor Labs](https://www.endorlabs.com/learn/shai-hulud-compromises-the-tanstack-ecosystem-80-packages-compromised), [SafeDep](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/), [Socket](https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack), [StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem), and [Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/) show. The data is exfiltrated to the "filev2.getsession[.]org" domain.

Using Session Protocol infrastructure is a deliberate attempt on the part of the attackers to evade detection, as the domain is unlikely to be blocked within enterprise environments, given that it belongs to a decentralized, privacy-focused messaging service. As a fallback option, the encrypted data is committed to attacker-controlled repositories under the author name "claude@users.noreply.github.com" via the GitHub GraphQL API using the stolen GitHub tokens.

The malware is also capable of establishing persistence hooks in Claude Code and Microsoft Visual Studio Code (VS Code) to survive reboots and re-execute the stealer on every launch of the IDEs.

Furthermore, it installs a gh-token-monitor service to monitor and re-exfiltrate GitHub tokens, and injects two malicious GitHub Actions workflows to serialize repository secrets into a JSON object and upload the data to an external server ("api.masscan[.]cloud").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Unlike the [previous SAP wave](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html), where the compromised packages added a preinstall hook to trigger the infection sequence, the latest TanStack cluster adopts a different strategy by including a JavaScript file within the package tarball and adding an optional dependency that points to a GitHub-hosted package. The GitHub dependency contains a prepare lifecycle hook that executes the JavaScript payload via the Bun runtime.

The updates to the Mistral AI packages, on the other hand, follow the earlier approach, replacing the contents of the "package.json" file with a preinstall hook to invoke "node setup.mjs," which downloads Bun and runs the same JavaScript malware.

The TanStack supply chain compromise has been assigned the CVE identifier [CVE-2026-45321](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx). It carries a CVSS score of 9.6 out of a maximum of 10.0, indicating critical severity. The incident has impacted 42 packages and 84 versions across the TanStack ecosystem.

TanStack has since [traced](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) the compromise to a chained GitHub Actions attack involving the "pull\_request\_target" trigger, [GitHub Actions cache poisoning](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/), and runtime memory extraction of an OIDC token from the GitHub Actions runner process. "No npm tokens were stolen, and the npm publish workflow itself was not compromised," TanStack said.

Specifically, the attackers are assessed to have staged the malicious payload in a GitHub fork via an orphaned commit, injected it into published npm tarballs, then hijacked the project's legitimate "TanStack/router" workflow to publish the compromised versions with valid SLSA provenance.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcDgUQOKnNQ-iSErOMUzl8A4sBrF5Mx3eFM-SFc66GgY3OroIZa1IQ96JZhFL1o2PqsvBj0e6F0jycjdbt4pmAxoK2BpGDvz8iIuiCGO_vMypxsw9PJis9ty6a_0OdzRVS3fiT1Gzwfn4C_jA8IDp3bevWo_GrUbMchilpS8NqGiaAel_nO1fb8_XnFXBx/s1700-e365/main.png)

"The attack published malicious versions through the project's own GitHub Actions release pipeline using hijacked OIDC tokens," StepSecurity researcher Ashish Kurmi said.

"In an extremely rare escalation, the compromised packages carry valid SLSA Build Level 3 provenance attestations, making this the first documented npm worm that produces validly attested malicious packages. The worm has since spread beyond TanStack to packages from UiPath, DraftLab, and other maintainers."

The attack is noteworthy for the fact that it abuses trusted publishing, allowing attacker-controlled code running within a workflow to leverage its OIDC permissions to "mint" a short-lived publish token during the build and use it to publish the packages without having to steal an npm token.

What makes the worm stand out is its ability to spread itself to other packages by locating a publishable npm token with bypass\_2fa set to true, enumerating every package published by the same maintainer, and ...