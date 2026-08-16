---
title: ChainDrop worm crawls into npm supply chain, evades standard defenses
url: https://www.theregister.com/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958
source: www.theregister.com - Articles
date: 2026-08-15
fetch_date: 2026-08-16T02:57:59.027562
---

# ChainDrop worm crawls into npm supply chain, evades standard defenses

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
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

SECURITY

# ChainDrop worm crawls into npm supply chain, evades standard defenses

Shai-Hulud variant poisons 444 packages, spreads via tarballs and dev-tool hooks

Joab Jackson
[Joab
Jackson](https://www.theregister.com/author/joab-jackson)
SOFTWARE DEVELOPMENT AND CLOUD REPORTER

Published
sat 15 Aug 2026 // 11:31 UTC

A new variant of the Shai-Hulud npm worm has poisoned hundreds of packages while adding propagation techniques that can leave little trace in the corresponding source repositories.

In Frank Herbert’s Dune, Shai-Hulud was the name of the giant self-sustaining desert sandworms that moved silently beneath the surface of the planet Arrakis. So it made sense that when some new self-replicating malware with computer worm-like behavior appeared in September 2025, security researchers would name it after Herbert’s fictional creatures.

The latest variant of Shai-Hulud, [dubbed “ChainDrop”](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/?msockid=1a63971b30c56eb437ea83ca31756f27) by Microsoft and others, is no mere sequel, however. Now, the npm community is discovering a Shai-Hulud variant spreading with new stealthy superpowers that circumvent the usual safeguards of open source repositories.

REG AD

On August 4, multiple security researchers identified a large-scale npm supply chain attack using this Shai-Hulud variant that had infected 444 packages from multiple publishers, which are collectively downloaded about 2 billion times a month. The operation targeted widely used deep infrastructure dependencies, such as [keyv](https://www.npmjs.com/package/keyv), [flat-cache](https://www.npmjs.com/package/flat-cache) and [cache-manager](https://www.npmjs.com/package/cache-manager).

REG AD

[Abby Kearns](https://www.abbykearns.com/), CEO of enterprise open source security company [ActiveState](https://www.activestate.com/company/about-us), [noted](https://medium.com/governed-at-the-source/the-chaindrop-npm-worm-august-2026-how-444-packages-were-compromised-without-a-single-npm-b0c9e5a4c387) in a Medium post that what is unique about this particular attack is that it doesn’t use the typical methods of breaching the defenses of open source repositories.

Even if you never install an infected package (“npm install” in npm argot), you can still get the nasties – though that is one possible route of infection. Once triggered, ChainDrop also places startup hooks into the repository configuration files themselves: Simply opening an infected Git branch in VS Code or Claude Code can bring your repository under ChainDrop’s control.

Scouring your code itself may not provide evidence of tampering. ChainDrop propagates not by repository source commits but by tarballs, an archive format for downloading file packages.

### ChainDrop travels by tarball

When executed, the software scours the user’s workspace for npm tokens with full write privileges, as well as for other credentials like cloud keys and secrets. It looks in shell configurations, environment variables and even live memory. Any purloined data is encrypted and sent back to attacker-controlled endpoints.

Should it find an npm token, it then downloads the tarballs of all the packages that token has full access to, bypassing the repositories themselves.

That’s the genius part: ChainDrop self-replicates by rebuilding the tarball to include its own payload. Reviewing the source code repository won’t reveal any evidence of shenanigans.

ChainDrop’s attack is two-pronged. It also searches for GitHub credentials. If it finds any, it queries the GitHub API to list all accessible repositories and branches and then commits its malicious configuration code directly into those branches.

REG AD

So when other developers open these repositories using Claude or VS Code, a background task gets triggered that harvests credentials, beginning the whole cycle anew.

### What a dev can do

This attack is particularly pernicious because npm is widely integrated into automated CI/CD pipelines, which can automatically pull patch updates for dependencies during a rebuild - giving the worm a path to wiggle into fresh builds.

If you think you've been infected, the first thing to do is check for any .claude/settings.jso...