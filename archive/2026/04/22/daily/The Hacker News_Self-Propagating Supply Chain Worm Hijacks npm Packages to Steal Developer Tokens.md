---
title: Self-Propagating Supply Chain Worm Hijacks npm Packages to Steal Developer Tokens
url: https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.352678
---

# Self-Propagating Supply Chain Worm Hijacks npm Packages to Steal Developer Tokens

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

# [Self-Propagating Supply Chain Worm Hijacks npm Packages to Steal Developer Tokens](https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html)

**Ravie Lakshmanan**Apr 22, 2026Malware / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIdq7inTckksldfLXx5JPM1spcmvj-W0C5jvCNGSfvUlWfhmFERkPhE9WNRTkTib4uZFsKKn2lBvxnhsZbEaOnGKI4pkSKu8kpyBn7VEsY3BbVN5ZklAoliWNZC-b526mJbr5xiYxKwRFXB8pnV2K-H5ww5mG3_1GrWjgvrsnqJ2EJu1gZJ15-D29njRY9/s1700-e365/npm.jpg)

Cybersecurity researchers have flagged a fresh set of packages that have been compromised by bad actors to deliver a self-propagating worm that spreads through stolen developer npm tokens.

The supply chain worm has been detected by both [Socket](https://socket.dev/blog/namastex-npm-packages-compromised-canisterworm) and [StepSecurity](https://www.stepsecurity.io/blog/pgserve-compromised-on-npm-malicious-versions-harvest-credentials), with the companies tracking the activity under the name **[CanisterSprawl](https://socket.dev/supply-chain-attacks/canistersprawl)** owing to the use of an [ICP canister](https://dashboard.internetcomputer.org/canister/cjn37-uyaaa-aaaac-qgnva-cai) to exfiltrate the stolen data, in a tactic reminiscent of TeamPCP's [CanisterWorm](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html) to make the infrastructure resilient to takedowns.

The list of affected packages is below -

* @automagik/genie (4.260421.33 - 4.260421.40)
* @fairwords/loopback-connector-es (1.4.3 - 1.4.4)
* @fairwords/websocket (1.0.38 - 1.0.39)
* @openwebconcept/design-tokens (1.0.1 - 1.0.3)
* @openwebconcept/theme-owc (1.0.1 - 1.0.3)
* pgserve (1.1.11 - 1.1.14)

The malware is triggered during install time via a postinstall hook to steal credentials and secrets from developer environments, and then leverage the stolen npm tokens to push poisoned versions of the packages to the registry with a new malicious postinstall hook so as to expand the reach of the campaign.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-blindspot-d-2)

Captured information includes -

* .npmrc
* SSH keys and SSH configurations
* .git-credentials
* .netrc
* cloud credentials for Amazon Web Services, Google Cloud, and Microsoft Azure
* Kubernetes and Docker configurations
* Terraform, Pulumi, and Vault material
* Database password files
* Local .env\* files
* Shell history files

In addition, it attempts to access credentials from Chromium-based web browsers and data associated with cryptocurrency wallet extension apps. The information is exfiltrated to an HTTPS webhook ("telemetry.api-monitor[.]com") and an ICP canister ("cjn37-uyaaa-aaaac-qgnva-cai.raw.icp0[.]io").

"It also contains PyPI propagation logic," Socket said. "The script generates a Python .pth-based payload designed to execute when Python starts, then prepares and uploads malicious Python packages with Twine if the required credentials are present."

"In other words, this is not just a credential stealer. It is designed to turn one compromised developer environment into additional package compromises."

The disclosure comes as JFrog revealed that multiple versions of the legitimate Python package "xinference" (2.6.0, 2.6.1, and 2.6.2) have been compromised to include a Base64-encoded payload that fetches a second-stage collector module responsible for harvesting a wide range of credentials and secrets from the infected host

"The decoded payload opens with the comment '# hacked by teampcp,' the same actor marker seen in recent TeamPCP compromises," the company [said](https://research.jfrog.com/post/xinference-compromise/). However, in a post shared on X, TeamPCP disputed they were behind the compromise and claimed it was the work of a copycat.

### Attacks Target npm and PyPI

The findings are the latest additions to a long list of attacks that have targeted the open-source ecosystem. This includes two malicious packages, each on npm (kube-health-tools) and PyPI (kube-node-health), that masquerade as Kubernetes utilities, but silently install a Go-based binary to establish a SOCKS5 proxy, a reverse proxy, an SFTP server, and a large language model (LLM) proxy on the victim's machine.

The LLM proxy is an OpenAI-compatible API gateway that accepts requests and routes them to upstream APIs, including Chinese LLM routers like shubiaobiao.

"Beyond providing cheap access to AI, LLM routers like the one deployed here sit on a trust boundary that is easily abused," Aikido Security researcher Ilyas Makari [said](https://www.aikido.dev/blog/gpt-proxy-backdoor-npm-pypi-chinese-llm-relay). "Because every request passes through the router in plaintext, a malicious operator can [...] inject malicious tool calls into responses of coding agents before they reach the client, introducing malicious pip install or curl | bash payloads mid-flight."

Alternatively, the router can be used to exfiltrate secrets from request and response bodies, including API keys, AWS credentials, GitHub tokens, Ethereum private keys, and system prompts.

Another sustained npm supply chain attack campaign [documented](https://panther.com/blog/false-claims-an-npm-supply-chain-campaign-impersonates-asurion) by Panther has impersonated phone insurance provider Asurion and its subsidiaries, publishing malicious npm packages (sbxapps, asurion-hub-web, soluto-home-web, and asurion-core) from April 1 through April 8, 2026, containing a multi-stage credential harvester.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The stolen credentials were exfiltrated initially to a Slack webhook and then to an AWS API Gateway endpoint ("pbyi76s0e9.execute-api.us-east-1.amazonaws[.]com"). By April 7, the AWS exfiltration URL is said to have been obfuscated using XOR encoding.

Last but not least, Google-owned cloud security firm Wiz [shed light](https://www.wiz.io/blog/six-accounts-one-actor-inside-the-prt-scan-supply-chain-campaign) on an artificial intelligence (AI)-powered campaign dubbed prt-scan that has systematically exploited the "[pull\_request\_target](https://thehackernews.com/2025/04/spotbugs-access-token-theft-identified.html)" GitHub Actions workflow trigger since March 11, 2026, to steal developer secrets.

The attac...