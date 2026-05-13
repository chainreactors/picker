---
title: Cache-poisoning caper turns TanStack npm packages toxic
url: https://www.theregister.com/cyber-crime/2026/05/12/cache-poisoning-caper-turns-tanstack-npm-packages-toxic/5238650
source: www.theregister.com - Articles
date: 2026-05-12
fetch_date: 2026-05-13T05:47:38.544882
---

# Cache-poisoning caper turns TanStack npm packages toxic

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/paas_iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI + ML](/ai_ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Cyber-Crime

# Cache-poisoning caper turns TanStack npm packages toxic

Six-minute supply chain blitz pushed 84 malicious versions with credential theft and disk-wiping code

Tim Anderson
[Tim
Anderson](https://www.theregister.com/author/tim-anderson)

Published
tue 12 May 2026 // 13:00 UTC

An attacker has published 84 malicious versions of official TanStack npm packages, with the impact including
credential theft, self-propagation, and complete disk wipe of an infected host.

The attack is part of a wave of attacks across npm and PyPI,
continuing the [Mini Shai-Hulud campaign](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837). Supply chain security company Socket [reports](https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack) that other compromised packages include the OpenSearch client, Mistral AI, UiPath, and
Guardrails AI.

Malicious npm packages for TanStack, an open source
application stack, were published
between 19:20 and 19:26 UTC on May 11. The attack was detected and
[reported](https://github.com/TanStack/router/issues/7383) within 30 minutes by StepSecurity, triggering incident response and npm deprecation. GitHub published a [security advisory](https://github.com/advisories/GHSA-g7cv-rxg3-hmpx) at 21:30 UTC, including a list of affected packages.

REG AD

TanStack founder Tanner Linsley published a [postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) describing how the attacker used a malicious commit on a fork to create a pull
request on the TanStack repository, causing scripts to auto-run and build the malware. This poisoned the GitHub Actions cache in what Linsley
said is a variant of a known [GitHub Action vulnerability](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/) discovered in 2024. The malware then extracted the npm OpenID Connect (OIDC)
token, used for trusted npm publishing, from runner memory using the same code used
to [compromise tj-actions](https://www.theregister.com/software/2025/04/07/stolen-spotbugs-tokens-sparked-the-massive-github-attack/1176250) in an attack last year.

REG AD

No TanStack maintainers were compromised.

StepSecurity has a [detailed analysis](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem) of the attack, noting that the payload "reads files from over 100
hardcoded paths" including those that may contain cloud credentials, SSH
(secure shell) keys, developer tool configuration files, crypto wallets, VPN configurations,
messaging credentials, and shell history. Shell history may contain tokens and
passwords pasted into the terminal.

## MORE CONTEXT

* [### The never-ending supply chain attacks worm into SAP npm packages, other dev tools](/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837)
* [### Supply chain blast: Top npm package backdoored to drop dirty RAT on dev machines](/security/2026/03/31/top-npm-package-backdoored-to-drop-dirty-rat-on-dev-machines/5219910)
* [### PostHog admits Shai-Hulud 2.0 was its biggest ever security bungle](/software/2025/11/28/posthog-admits-shai-hulud-20-was-its-biggest-security-scare/1817272)
* [### Supply chain attacks now fuel a 'self-reinforcing' cybercrime economy](/security/2026/02/12/supply-chain-breaches-fuel-cybercrime-cycle-report-says/4769503)

Security researcher Nicholas Carlini [warned](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340) the payload "installs a dead-man's switch… as a system user service."
The service checks whether a stolen GitHub token has been revoked and, if it
has, runs a command to wipe the local disk completely.

Socket's write-up includes recommended actions such as rotating all secrets on any affected system. GitHub's advisory
suggests "any developer or CI environment that ran npm install, pnpm
install, or yarn install against an affected version on 2026-05-11 should be
considered compromised."

The Mistral AI has also been [reported](https://github.com/mistralai/client-python/issues/523) on GitHub, and at the time of writing, the Mistral AI project is quarantined on PyPI.

This attack is still evolving and will likely have a far-reaching impact. It confirms again that running everyday commands like npm install is unsafe, that for all their efforts major package repositories including npm and PyPI are still not secured, and that software development is now best done in isolated, ephemeral environments. ®

[github](/tag/github)
[development](/tag/development)
[cyber-crime](/tag/cyber-crime)
[npm](/tag/npm)
[security](/tag/security)

REG AD

[![](https://image.theregister.com/5239315.jpg?imageId=5239...