---
title: GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections
url: https://www.theregister.com/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169
source: www.theregister.com - Articles
date: 2026-06-08
fetch_date: 2026-06-09T06:03:46.560197
---

# GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections

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
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
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
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
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
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
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

* [Computex 2026](/special_features/computex)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

security

# GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections

Miasma worm shapeshifts, but cloud secret-scouting remains the goal

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
mon 8 Jun 2026 // 14:56 UTC

Microsoft’s GitHub has disabled over 70 repositories after they were reportedly compromised by a worm in the latest open source supply chain attack.

The code shack took down 73 repos within the space of 105 seconds after its alarms were tripped on Friday, June 5, after detecting signs of the Miasma worm infecting its projects, according to StepSecurity’s co-founder and CTO, Ashish Kurmi.

Users reported issues quickly on Friday, after visits to those repos all resulted in the same message displayed, indicating that they had been disabled due to terms of service violations.

REG AD

According to StepSecurity’s analysis, the attack kicked off after a compromised contributor account pushed a malicious commit to Azure/durabletask. The commit dropped configuration files that triggered remote code execution on machines when a developer opened the repo in an IDE or AI coding tool, such as Claude Code, Gemini CLI, and Cursor.

REG AD

Several developers soon reported broken CI/CD pipelines, a [support thread](https://learn.microsoft.com/en-us/answers/questions/5912595/github-action-azure-functions-action-down) showed, although a moderator said at the time this was due to “an internal management issue.”

"The repo that most immediately caused issues was Azure/functions-action,” Kurmi wrote, used to deploy code to Azure. With it being taken down, every workflow that referenced Azure/functions-action@v1 stopped resolving.

GitHub stepped in a few hours after the repos were infected by the malicious commit. Its automated detections kicked in and disabled the repos in under two minutes, in two separate waves.

However, it was the borking of the durabletask family that hinted at the bigger picture, that the attack was indeed a re-opening of the previous Miasma worm attack that hit Microsoft last month.

## MORE CONTEXT

* [### Shai-Hulud malware worms Red Hat npm package versions downloaded 80K times a week](/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803)
* [### GitHub says internal repos exfiltrated after poisoned VS Code extension attack](/devops/2026/05/20/github-says-internal-repos-exfiltrated-after-poisoned-vs-code-extension-attack/5243206)
* [### Malware crew TeamPCP open-sources its Shai-Hulud worm on GitHub](/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319)
* [### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops](/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)

Microsoft’s durabletask PyPi package was a previous target of the Miasma worm on May 19. Within a 35-minute window, three versions of the package were uploaded to PyPi, which planted infostealers on developers’ machines, specifically sniffing out cloud secrets and developer tool configurations on Linux systems.

Crucially, the re-targeting of durabletask suggests the tokens associated with the compromised developer account used to execute the PyPi attack were not fully rotated, allowing an attacker to gain access and push commits to GitHub, Kurmi said.

It was either that, or the contributor was re-compromised through the worm's own propagation loop, or a different contributor's token was used but the attacker altered the metadata to make it look like a repeated attack.

Security shop Snyk described Miasma as a [descendant of the Mini Shai Hulud worm](https://snyk.io/blog/node-gyp-supply-chain-compromise-self-propagating-npm-worm-binding-gyp/). It’s the same one that ravaged open source packages over at the npm registry, [including Red Hat’s](https://www.theregister.com/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803), earlier this month.

REG AD

Cybercrime group TeamPCP claimed responsibility for developing Mini Shai Hulud, which itself is named after an [earlier worm of the same name](https://www.theregister.com/special-features/2025/09/16/self-propagating-worm-fuels-latest-npm-supply-chain-attack/1437180), sans “mini.”

However, because TeamPCP [open-sourced Mini Shai Hulud](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319), it’s difficult to tell whether it was also behind Miasma or if someone else took the reins on the follo...