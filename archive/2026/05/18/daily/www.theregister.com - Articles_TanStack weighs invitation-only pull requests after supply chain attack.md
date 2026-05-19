---
title: TanStack weighs invitation-only pull requests after supply chain attack
url: https://www.theregister.com/security/2026/05/18/tanstack-weighs-invitation-only-pull-requests-after-supply-chain-attack/5241899
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:16.139772
---

# TanStack weighs invitation-only pull requests after supply chain attack

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

Security

# TanStack weighs invitation-only pull requests after supply chain attack

Shai-Hulud worm exploited GitHub Actions misconfiguration to poison shared cache, now project weighing nuclear option on unsolicited contributions

Tim Anderson
[Tim
Anderson](https://www.theregister.com/author/tim-anderson)

Published
mon 18 May 2026 // 15:15 UTC

The TanStack team has documented security measures and proposals following a [damaging breach](https://www.theregister.com/cyber-crime/2026/05/12/cache-poisoning-caper-turns-tanstack-npm-packages-toxic/5238650) last week, including the possibility of making pull requests
(PRs) by invitation only - a break from the open-contribution model that defines most open source projects.

The attack used code from the Shai-Hulud
worm, [published](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319)
by malware outfit TeamPCP, which can extract secrets from memory
used by GitHub Actions. It began with a PR that triggered an automatic workflow via TanStack's use of the [pull\_request\_target](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target)
feature, causing the malicious code to be built and run by a GitHub Action, poisoning a
cache used across the entire repository.

REG AD

The TanStack team [said](https://tanstack.com/blog/incident-followup) that its workflow used a pattern GitHub [warns against](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/): pull\_request\_target id intended for PRs that "do not
require dangerous processing, say building or running the content of the
PR."

REG AD

Since the attack, TanStack has removed all use of
pull\_request\_target from its continuous integration (CI) pipeline, disabled
caches used by pnpm (a Node.js package manager) and GitHub Actions, pinned actions
to commit SHA (Secure Hash Algorithm) hashes rather than retargetable tags, and disabled use of text messages for 2-factor authentication.

The TanStack repository also now uses a feature of pnpm 11 called
[minimumReleaseAge](https://pnpm.io/settings#minimumreleaseage), which requires dependencies to have been published for a set period
before they can be installed. The idea is that compromised packages are usually
detected and removed before that period completes.

## MORE CONTEXT

* [### OpenAI caught in TanStack npm supply chain chaos after employee devices compromised](/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019)
* [### Cache-poisoning caper turns TanStack npm packages toxic](/cyber-crime/2026/05/12/cache-poisoning-caper-turns-tanstack-npm-packages-toxic/5238650)
* [### Malware crew TeamPCP open-sources its Shai-Hulud worm on GitHub](/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319)
* [### The never-ending supply chain attacks worm into SAP npm packages, other dev tools](/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837)
* [### Grafana Labs admits all its codebase are belong to someone who popped its GitHub account](/cyber-crime/2026/05/18/grafana-labs-admits-attackers-downloaded-its-codebase-from-github/5241686)

A more drastic proposal is closing the
ability for external contributors to open pull requests at all. "We are absolutely
not going closed source," the team said, but it could put in place a mechanism
where contributions begin with an issue or discussion, and a PR can be
submitted only by invitation.

TanStack acknowledged that it would be a radical step to take as "open PRs are part of how a lot of us became maintainers in the first
place." It might not be necessary if the repository can be hardened enough that
malicious PRs cannot cause damage.

It is a debate that maintainers of other open source
projects will watch with interest. Supply chain security is a huge issue, but making
pull requests invitation-only could hurt projects by deterring contributions.

Another aspect of this is the extent to which GitHub itself is
to blame. "Cache scoping in GitHub Actions shouldn't silently bridge fork
PRs and base-repo branches," said the TanStack team.®

[open source](/tag/open%20source)
[github actions](/tag/github%20actions)
[tanstack](/tag/tanstack)
[devops](/tag/devops)
[pull requests](/tag/pull%20requests)
[shai-hulud](/tag/shai-hulud)
[supply chain attack](/tag/supply%20chain%20attack)
[security](/tag/security)

REG AD

[![](https://image.theregister.com/4094156.jpg?imageId=4094156&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Networks

## Iran hints it could interfere with ...