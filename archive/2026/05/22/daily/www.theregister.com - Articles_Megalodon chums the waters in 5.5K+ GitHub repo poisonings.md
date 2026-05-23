---
title: Megalodon chums the waters in 5.5K+ GitHub repo poisonings
url: https://www.theregister.com/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342
source: www.theregister.com - Articles
date: 2026-05-22
fetch_date: 2026-05-23T05:43:04.411835
---

# Megalodon chums the waters in 5.5K+ GitHub repo poisonings

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
  + [PaaS + IaaS](/tag/paas-iaas)
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
  + [AI + ML](/tag/ai-ml)
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

# Megalodon chums the waters in 5.5K+ GitHub repo poisonings

Will Jason Statham save us?

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
fri 22 May 2026 // 19:57 UTC

A malware-spreading scumbag swimming through GitHub pushed malicious commits to more than 5,500 repositories on Monday as part of an automated campaign called Megalodon.

Similar to the earlier [TeamPCP attacks](https://www.theregister.com/devops/2026/05/20/github-says-internal-repos-exfiltrated-after-poisoned-vs-code-extension-attack/5243206) that poisoned about 3,800 GitHub repositories, this new campaign has so far infected 5,561 repos with CI/CD credential-stealing malware, according to SafeDep researchers, who uncovered the predatory commits and published a [full list of the compromised repositories](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/#full-list-of-compromised-github-repositories).

If a repository owner merges the commit, the malware executes inside their CI/CD pipeline and propagates further, Ox Security lead researcher Moshe Siman Tov Bustan [said](https://www.ox.security/blog/megalodon-cicd-malware-github/) in a Thursday blog post.

REG AD

Megalodon steals AWS secret keys and Google Cloud access tokens. It also queries AWS, Google Cloud Platform, and Azure metadata for instance role credentials, reads SSH private keys, Docker and Kubernetes configurations, Vault tokens, Terraform credentials, and scans source code for more than 30 secret regex patterns. Then it exfiltrates GitHub tokens, including secrets used to authenticate with cloud providers, thus allowing attackers to impersonate developers’ cloud identities, along with Bitbucket tokens.

REG AD

In other words: consider ALL of your CI/CD variables pwned.

"We’ve entered a new supply chain attack era, and TeamPCP compromising GitHub was only the beginning,” Bustan told The Register. “What’s coming next is an endless wave, a tsunami of cyber attacks on developers worldwide.”

Plus, he added, hacking GitHub “compromises the security of every company with a private repository hosted on the platform.”

### Malicious code is still reaching their servers, and nothing is stopping it before it does

This new wave of supply chain attacks hitting developers’ environments won’t stop until “companies like npm and GitHub take serious action against the spread of malicious code on their servers,” Bustan said.

He noted npm’s statement on X saying it “invalidated npm granular access tokens with write access that bypass 2FA” to prevent additional supply-chain attacks like [Mini Shai Hulud](https://www.theregister.com/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180).

“That could help a little with account hijacking, but it doesn’t solve the actual problem,” Bustan said. “Malicious code is still reaching their servers, and nothing is stopping it before it does.”

### npm … but not TeamPCP

SafeDep spotted Megalodon hidden inside a legitimate package: [Tiledesk](https://www.tiledesk.com/), an open source live chat and chatbot platform. The attacker backdoored versions 2.18.6 (May 19) through 2.18.12 (May 21), and the same npm maintainer published the last clean version, 2.18.5, before unknowingly publishing these newer compromised versions.

REG AD

“The attacker never touched the npm account,” the open source supply-chain security startup researchers [said](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/). “They compromised the [GitHub repository](https://github.com/Tiledesk/tiledesk-server), and the maintainer published from the poisoned source without realizing it.”

While publishing [malicious packages on npm](https://www.theregister.com/security/2026/03/31/top-npm-package-backdoored-to-drop-dirty-rat-on-dev-machines/5219910) is a [TeamPCP signature move](https://www.theregister.com/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180), Bustan said there’s no threat-intel or code-analysis evidence that connects Megalodon to the crew behind the [Trivy](https://www.theregister.com/security/2026/03/24/litellm-infected-with-credential-stealing-code-via-trivy/5223422), [Checkmarx](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780), and other [recent supply-chain attacks](https://www.theregister.com/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019). “Our best guess now is that it's a different threat actor copying their behavior and style, but not much of the code itself,” he told us.

And despite [TeamPCP open sourcing](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-sh...