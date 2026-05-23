---
title: Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows
url: https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
source: The Hacker News
date: 2026-05-22
fetch_date: 2026-05-23T05:43:00.331135
---

# Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows

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

# [Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)

**Ravie Lakshmanan**May 22, 2026Supply Chain Attack / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjC_sjVeLejyyBZJ0DWW2y9-Z2Jvmrzz9h-5XEIKPFTcJvDj49Jlt-z1FNbSp51K9XcQ8FqC9MBDFPPPdZuzRfjqtYvKNaqT0Qzd61oCHVhNq59IcAVcWV3LvDmKCsX5pHn4nU3LclQPEozMp3XsgYZnVHCZEj89AGkWJpqL1EjCjiqMLnvggZLsgb08MYp/s1700-e365/github-worm.jpg)

Cybersecurity researchers have disclosed details of a new automated campaign called **Megalodon** that has pushed 5,718 malicious commits to 5,561 GitHub repositories within a six-hour window.

"Using throwaway accounts and forged author identities (build-bot, auto-ci, ci-bot, pipeline-bot), the attacker injected GitHub Actions workflows containing base64-encoded bash payloads that exfiltrate CI secrets, cloud credentials, SSH keys, OIDC tokens, and source code secrets to a C2 server at 216.126.225[.]129:8443," SafeDep [said](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/) in a report.

The complete list of data harvested by the malware is below -

* CI environment variables, /proc/\*/environ, and PID 1 environment
* Amazon Web Services (AWS) credentials
* Google Cloud access tokens
* Instance role credentials obtained by querying AWS IMDSv2, Google Cloud metadata, and Microsoft Azure Instance Metadata Service (IMDS) endpoints
* SSH private keys
* Docker and Kubernetes configurations
* Vault tokens
* Terraform credentials
* Shell history
* API keys, database connection strings, JWTs, PEM private keys, and cloud tokens matching more than 30 secret regular expression patterns
* GitHub Actions OIDC token request URL and token
* GITHUB\_TOKEN, GitLab CI/CD tokens, and Bitbucket tokens
* .env files, credentials.json, service-account.json, and other configuration files

One of the impacted packages is @tiledesk/tiledesk-server, which bundles a Base64-encoded bash payload within a GitHub Actions workflow file. In all, 5,718 commits were pushed against 5,561 distinct repositories on May 18, 2026, between 11:36 a.m. and 5:48 p.m. UTC.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"The attacker rotated through four author names (build-bot, auto-ci, ci-bot, pipeline-bot) and seven commit messages, all mimicking routine CI maintenance," SafeDep said. "The attacker used throwaway GitHub accounts with random 8-character usernames (e.g., rkb8el9r, bhlru9nr, lo6wt4t6), set git config to forge the author identity, and pushed via compromised PATs or deploy keys."

Two payload variants have been observed as part of the large-scale campaign: SysDiag, a mass variant which adds a new workflow that's triggered on every push and pull request, and Optimize-Build, a targeted variant that activates only on [workflow\_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch), a GitHub Actions trigger that allows users to manually run a workflow on-demand. In the case of Tiledesk, the targeted approach is used to target CI/CD runners, and not when the npm package is installed.

"The tradeoff is reach: on: push would guarantee execution on every commit to master, hitting more targets without intervention," SafeDep added. "Workflow\_dispatch sacrifices that for operational security. With 5,700+ repos compromised, even a small fraction yielding a usable GITHUB\_TOKEN gives the attacker enough targets for on-demand triggering."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgOi30e1RABlSxe7QyIGD14Z6CB-6zwYwf4Y3Xsecd5do01dlAZwYRJW2X16QpT90e3N9pKh8zh9THZtJJ-5KBK39DBDWSjJ0iXfxxclJ4Uz8N4wLFIPKts7jWdyD1XSm4czO7-cpOmP7s0MgdZG-4HRXFsDGhMsojb0Opxo2R8eKWeWTHXTJfPNV5YGe1/s1700-e365/megalodon.jpg)

The result is that once a repository owner merges the commit, the malware executes inside their CI/CD pipelines and spreads further, enabling the theft of credentials and secrets at scale.

"We've entered a new supply chain attack era, and [TeamPCP compromising GitHub](https://thehackernews.com/2026/05/github-internal-repositories-breached.html) was only the beginning," OX Security's Moshe Siman Tov Bustan [said](https://www.ox.security/blog/megalodon-cicd-malware-github/). "What's coming next is an endless wave, a tsunami of cyber attacks on developers worldwide."

The development comes as TeamPCP has weaponized the interlinked software supply chain to corrupt hundreds of open-source tools, worming their way through several ecosystems and extorting victims for profit in some cases. Microsoft-owned GitHub has become the latest addition to the group's long list of victims, which also includes TanStack, Grafana Labs, OpenAI, and Mistral AI.

TeamPCP attacks have fueled a cyclical exploitation of popular open-source projects, where one compromise feeds the next, allowing the malware to spread like wildfire in a worm-like fashion. The group also appears to be financially motivated and has established partnerships with BreachForums and other extortion crews like LAPSUS$ and VECT.

What's more, the group seems to be geopolitically motivated as well, as evidenced by the [deployment of wiper malware](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html) upon detecting machines located in Iran and Israel.

The fallout from TeamPCP's attack spree and the [Mini Shai-Hulud worm](https://trustedsec.com/blog/shai-hulud-is-back) has [prompted](https://x.com/npmjs/status/2056960835030016286) npm to invalidate granular access tokens with write access that bypasses two-factor authentication (2FA). NPM is also urging users to switch to [Trusted Publishing](https://docs.npmjs.com/trusted-publishers/) to reduce reliance on such tokens.

"By burning every bypass-2FA token on the platform, npm cuts off the credentials the worm has already c...