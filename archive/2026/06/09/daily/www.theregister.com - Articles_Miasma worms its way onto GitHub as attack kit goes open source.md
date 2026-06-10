---
title: Miasma worms its way onto GitHub as attack kit goes open source
url: https://www.theregister.com/cyber-crime/2026/06/09/miasma-supply-chain-attack-toolkit-goes-public-on-github/5253074
source: www.theregister.com - Articles
date: 2026-06-09
fetch_date: 2026-06-10T06:17:17.933294
---

# Miasma worms its way onto GitHub as attack kit goes open source

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

cyber-crime

# Miasma worms its way onto GitHub as attack kit goes open source

As if there weren't enough package poisonings to worry about

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
tue 9 Jun 2026 // 19:05 UTC

As if the Miasma situation weren't bad enough, now this weapon is spreading like wildfire. Someone open sourced the entire Miasma worm supply-chain attack toolkit, likely using previously compromised developers' accounts to publish GitHub repositories containing the self-spreading malware’s source code over the last 24 hours.

SafeDep, a company focused on open source supply chain security that developed Package Management Guard (PMG), spotted the malicious repos, named “Miasma-Open-Source-Release,” and said that they started appearing on Monday. Its researchers analyzed [one of these](https://github.com/YangYongAn/Miasma-Open-Source-Release) before GitHub nixed it, and described the code as more than just a supply chain worm.

“It is a full supply chain attack toolkit that allows the operator to execute various attacks via stolen credentials against arbitrary or targeted packages on public registries (PyPI, npm, RubyGems), JFrog Artifactory, GitHub repositories and GitHub Actions, AI coding tools config poisoning, SSH based lateral movement and other attack vectors,” the SafeDep team [said](https://safedep.io/inside-the-miasma-supply-chain-attack-toolkit/).

REG AD

## MORE CONTEXT

* [### GitHub nukes 70+ Microsoft repos, breaks CI/CD pipelines, following suspected worm infections](/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169)
* [### Shai-Hulud malware worms Red Hat npm package versions downloaded 80K times a week](/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803)
* [### Megalodon chums the waters in 5.5K+ GitHub repo poisonings](/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342)
* [### Shai-Hulud keeps burrowing: 314 npm packages infected after another account compromise](/cyber-crime/2026/05/19/shai-hulud-keeps-burrowing-314-npm-packages-infected-after-another-account-compromise/5242601)

REG AD

While we don’t know who is behind this publicly released worm, it follows in the footsteps of [TeamPCP](https://www.theregister.com/security/2026/04/11/two-different-attackers-poisoned-popular-open-source-tools/5221008), which [developed](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837) and then [open sourced the mini Shai-Hulud worm](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319) last month, announcing a supply-chain attack contest on BreachForums and spawning [copycat open source package poisonings](https://www.theregister.com/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180).

One of these copycat worms, Miasma, first hit upwards of 100 [Red Hat](https://www.theregister.com/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803) and [Microsoft](https://www.theregister.com/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169) open source projects before spreading to other victims, with app-security firm Socket tracking [473 affected package artifacts](https://socket.dev/supply-chain-attacks/miasma-mini-shai-hulud-supply-chain-attack) as of Tuesday.

“The Miasma repository is an evolution of the Mini Shai-Hulud toolkit, and was open-sourced June 8 via four previously compromised users,” Rami McCarthy, principal threat researcher at Wiz, told The Register. “Since we had already reversed the payload, this public release isn’t particularly useful for sophisticated defenders, and we haven't observed any opportunistic adoption of it yet.”

This, he added, mimics what happened when TeamPCP open sourced mini Shai-Hulud last month.

“We didn't see attackers weaponize it either,” McCarthy said. “It's not clear [whether] attackers benefit from adopting this out-of-the-box toolkit versus vibe coding their own. And while it raises concerns about muddying attribution, attackers tend to continue developing their private fork of the malware, providing a clear payload progression to track and deconflict from anyone utilizing the open-source version.”

An interesting aspect of both of these worms and other recent attacks like [this one dubbed “Comment-and-Control”](https://www.theregister.com/security/2026/04/15/anthropic-google-microsoft-paid-ai-bug-bounties-quietly/5221934) by AI bug hunter Aonan Guan is that they run entirely in GitHub - they d...