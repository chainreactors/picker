---
title: GitHub pulls pin on npm's auto-run scripts
url: https://www.theregister.com/devops/2026/06/10/github-pulls-pin-on-npms-auto-run-scripts/5253453
source: www.theregister.com - Articles
date: 2026-06-10
fetch_date: 2026-06-11T06:37:03.769004
---

# GitHub pulls pin on npm's auto-run scripts

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

* [Space](/tag/space)
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

DevOPS

# GitHub pulls pin on npm's auto-run scripts

Shai-Hulud worm exploited exactly this. Better late than never, says everyone except the malware authors

Tim Anderson
[Tim
Anderson](https://www.theregister.com/author/tim-anderson)

Published
wed 10 Jun 2026 // 14:11 UTC

GitHub will change npm's defaults so the install command no longer runs scripts automatically, disabling a feature commonly exploited by malicious packages such as the notorious Shai-Hulud worm.

Maintainer Leo Balter [said](https://github.com/orgs/community/discussions/198547): "Install-time lifecycle scripts are the single largest code-execution surface in the npm ecosystem. Every npm install runs scripts from every transitive dependency, so a single compromised package anywhere in your tree can execute arbitrary code on a developer machine or CI (continuous integration) runner."

In npm 12, due July, three security-focused defaults are changing. Scripts configured for preinstall, install, or postinstall will no longer run unless explicitly permitted via allow-scripts. The --allow-git flag, which pulls dependencies from remote URLs, will default to off, closing an attack path where a malicious .npmrc file could override the Git executable and achieve arbitrary code execution. Finally, allow-remote will default to none, blocking dependency downloads from remote URLs entirely.

REG AD

It will still be possible to allow scripts to run via an allowlist in the package.json configuration file. This will be pinned to the installed version of a package by default.

REG AD

These are breaking changes, and Balter recommended developers run the commands to allow scripts for every currently installed package in a project that requires them. "This gets you protected against new, unexpected scripts immediately," he said. The next step is to review these packages and deny scripts for those where they are not needed.

Some packages require script approval to function, including native modules that compile on install, testing tools like Playwright and Puppeteer (which fetch binaries via postinstall), and Electron, which wraps the Chromium browser engine for cross-platform desktop applications.

These features have been available since npm version 11.10.0, released in February, but as opt-in flags rather than defaults. That version also introduced min-release-age, which blocks installation of package version newer than a specified number of days, designed as a safeguard against newly published malicious packages.

## MORE CONTEXT

* [### Miasma worms its way onto GitHub as attack kit goes open source](/cyber-crime/2026/06/09/miasma-supply-chain-attack-toolkit-goes-public-on-github/5253074)
* [### Shai-Hulud malware worms Red Hat npm package versions downloaded 80K times a week](/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803)
* [### GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections](/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169)
* [### Npm registry sets stage for more secure package publishing](/ai-ml/2026/05/21/npm-registry-sets-stage-for-more-secure-package-publishing/5244527)

Best security practice for developers using npm 11.16, the current version, is to set these flags on in .npmrc or via environment variables, which will also prepare a project for the changes in version 12. One annoyance is that the existing flag ignore-scripts does not support an allowlist, other than via an additional tool. The ignore-scripts setting will override allow-scripts, so developers will need to remove it, if set to true, to enable approved scripts to run. The allowScripts setting exists in npm 11 but is advisory only.

Will this fix npm security issues? Unfortunately not. "Now all the malware can move from the install script to the module itself where it will inevitably still be run," [said](https://news.ycombinator.com/item?id=48472386) one developer. Another common view is that developers should use [pnpm](https://pnpm.io), which already has safer defaults than npm, including a minimum release age.

There is consensus, though, that these changes do improve npm security and are long overdue. The [pull request](https://github.com/npm/rfcs/pull/868) for this change includes the remark that "npm is the only remaining major package manager that runs dependency install scripts by default. pnpm v10+, Yarn Berry, Bun, and Deno all block them." ®

[supply chain attack](/tag/supply%20chain%20attack)
[security](/tag/security)
[open source](/tag/open%20source)
[npm](/tag/npm)
[github](/tag/github)
[devops](/tag/devops)

REG AD

[![](https://image.theregister.com/5226078.jpg?imageId=5...