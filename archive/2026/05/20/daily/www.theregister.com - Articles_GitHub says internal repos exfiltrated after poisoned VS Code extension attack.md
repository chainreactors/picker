---
title: GitHub says internal repos exfiltrated after poisoned VS Code extension attack
url: https://www.theregister.com/devops/2026/05/20/github-says-internal-repos-exfiltrated-after-poisoned-vs-code-extension-attack/5243206
source: www.theregister.com - Articles
date: 2026-05-20
fetch_date: 2026-05-21T06:04:46.830533
---

# GitHub says internal repos exfiltrated after poisoned VS Code extension attack

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

DevOps

# GitHub says internal repos exfiltrated after poisoned VS Code extension attack

Initial assessment says customer data spared while users wonder what else may have slipped out

Tim Anderson
[Tim
Anderson](https://www.theregister.com/author/tim-anderson)

Published
wed 20 May 2026 // 11:27 UTC

GitHub, the world's biggest code repository and DevOps
platform, fell victim to a malicious Visual Studio Code (VS Code) extension. The company's initial assessment is that only internal repositories
were exfiltrated.

The incident was [reported by GitHub on X](https://x.com/github/status/2056884788179726685), with follow-up posts revealing a "poisoned
VS Code extension" as the cause. The Microsoft-owned code shack continues to "analyze
logs, validate secret rotation, and monitor for any follow-on activity."

One GitHub [post](https://x.com/github/status/2056949169701720157)
references "the attacker's current claims of ~3,800 repositories" as
consistent with its investigation. This may refer to a post attributed to TeamPCP, the malware crew linked to the Shai-Hulud worm, the code for which has been [published](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319) and caused widespread damage.

REG AD

In
a post, the crew advertised GitHub's internal source code for sale, claiming around 4,000 repositories. They said it was not a ransom and if no buyer was found, they would leak the code for free. Claims like these should be treated with caution.

REG AD

A key concern for GitHub users is whether private repositories are at risk, either immediately or in the future if the attackers have
gained a foothold into internal systems via stolen credentials. Risks include
leakage of commercial code and credentials. Although best practice is not to
check secrets into any repository, public or private, some organizations are less disciplined about this when repositories are private.

Last month, Wiz Research [discovered](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854)
a remote code execution flaw in GitHub.com and GitHub Enterprise Server (the
self-hosted version), which the researchers said was "remarkably easy to
exploit." The vulnerability was discovered using AI.

## MORE CONTEXT

* [### TanStack weighs invitation-only pull requests after supply chain attack](/security/2026/05/18/tanstack-weighs-invitation-only-pull-requests-after-supply-chain-attack/5241899)
* [### Shai-Hulud keeps burrowing: 314 npm packages infected after another account compromise](/cyber-crime/2026/05/19/shai-hulud-keeps-burrowing-314-npm-packages-infected-after-another-account-compromise/5242601)
* [### OpenAI caught in TanStack npm supply chain chaos after employee devices compromised](/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019)
* [### Malware crew TeamPCP open-sources its Shai-Hulud worm on GitHub](/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319)

Developer reactions to GitHub's latest problems combine alarm
and resignation – plus some humor. "How did the attackers find a large
enough uptime window to get in?" [quipped](https://x.com/anshuc/status/2056898035159056558)
one.

GitHub is in some difficulty. This compromise comes after a
surge in npm attacks, many related to Shai-Hulud code, which the company has
failed to prevent despite being aware of the issue since September 2025.
Further, the platform has reliability issues caused in part by AI bots [hoovering
public code](https://www.theregister.com/devops/2026/05/15/git-is-unprepared-for-the-ai-coding-tsunami/5241480) to feed large language models – problems that led [HashiCorp co-founder Mitchell Hashimoto to declare](https://www.theregister.com/software/2026/04/29/mitchell-hashimoto-says-github-no-longer-for-serious-work/5227505) GitHub "no longer a
place for serious work."

[Another](https://x.com/anshuc/status/2056898035159056558) [said](https://news.ycombinator.com/item?id=48203566)
that "the era where a developer machine with source code access also has
access to meaningful security systems should be over. Internal repository
access should mean nothing... GitHub compromise could happen at any time, even
from GitHub themselves."

Issues with cloud platforms also increase the appeal of
self-hosted systems such as the open source [Forgejo](https://forgejo.org), which powers Berlin-based Codeberg, a GitHub alternative.

GitHub has promised a fuller report "once the
investigation is complete," presumably posted to its own site rather than
only reported on X as is currently the case. ®

[devops](/tag/devops)
[developer](/tag/developer)
[github](/tag/github)
[security](/tag/security)

REG AD

[![](https://image.t...