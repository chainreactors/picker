---
title: Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged
url: https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780
source: www.theregister.com - Articles
date: 2026-05-11
fetch_date: 2026-05-12T05:39:15.136899
---

# Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged

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

[DevOps](https://www.theregister.com/devops)

# Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged

Cybercrooks ruin engineers' weekends with Saturday attack

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
mon 11 May 2026 // 13:11 UTC

Checkmarx’s software engineers are still working to remove a malicious version of the code security outfit's Jenkins plugin after detecting an unauthorized upload over the weekend.

It updated customers on Saturday, May 9, after discovering a version of its AST Scanner, which is used for security scans in Jenkins CI pipelines, was made available via the Jenkins Marketplace.

“We are aware that a modified version of the Checkmarx Jenkins AST plugin was published to the Jenkins Marketplace,” it said in a statement. “We are in the process of publishing a new version of this plug-in.”

REG AD

Versions published as of May 9, 2026, should not be trusted, it added, before urging all users to check they’re running the correct release (2.0.13-829.vc72453fa\_1c16) published on December 17, 2025.

REG AD

## MORE CONTEXT

* [### Ongoing supply-chain attack 'explicitly targeting' security, dev tools](/security/2026/04/28/ongoing-supply-chain-attack-targets-security-dev-tools/5226665)
* [### Worm rubs out competitor's malware, then takes control](/security/2026/05/08/worm-rubs-out-competitors-malware-then-takes-control/5237389)
* [### Another npm supply chain worm is tearing through dev environments](/security/2026/04/22/another-npm-supply-chain-worm-hits-dev-environments/5220989)
* [### AI recruiting biz Mercor says it was 'one of thousands' hit in LiteLLM supply-chain attack](/security/2026/04/02/mercor-says-it-was-one-of-thousands-hit-in-litellm-attack/5222276)

Installed by several hundred controllers, the plugin [remains available](https://plugins.jenkins.io/checkmarx-ast-scanner/healthscore/) at the time of writing, and appears as the most recently available version, although pull requests actioned on Monday morning suggest this will soon be pulled down.

“What makes this particularly dangerous for Jenkins users is the trust model at play,” said SOCRadar in [its coverage](https://socradar.io/blog/checkmarx-jenkins-plugin-teampcp-backdoor/?utm_campaign=27596841-LeadGen_Organic-Social_Global_1025&utm_source=linkedin&utm_medium=social). “The Checkmarx Jenkins plugin is a tool people install specifically to improve the security of their pipelines.

“A backdoored version doesn’t just compromise one project; it rides trusted infrastructure into every build pipeline it touches, with access to source code, environment variables, tokens, and whatever secrets the runner can see.”

## Shai-Hulud?

The Dune-themed malware, named after its self-propagating wormable nature, first [caused a stir in September last year](https://www.theregister.com/special-features/2025/09/16/self-propagating-worm-fuels-latest-npm-supply-chain-attack/1437180) as hundreds of npm packages were compromised.

Shail-Hulud 2.0 was first seen in the [following November](https://www.theregister.com/security/2025/11/24/wormable-npm-attack-returns-as-25000-repos-spill-secrets/2329666), affecting over 25,000 GitHub repos, before the Mini Shai-Hulud packages, the same ones that were injected into Checkmarx’s Jenkins plugin, hit [SAP npm packages](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837) in the earlier stages of the recent TeamPCP supply chain attacks.

Security engineer Adnan Khan spotted the compromise quickly over the weekend. The crew behind the early supply chain attack affecting Checkmarx in April, TeamPCP, defaced the company’s GitHub and published six packages, each with a description alluding to the Shai-Hulud wormable malware.

These packages no longer appear on Checkmarx’s GitHub, but TeamPCP made multiple changes to the AST plugins page, renaming it to “Checkmarx-Fully-Hacked-by-TeamPCP-and-Their-Customers-Should-Cancel-Now,” and altering the description to claim CheckMarx failed to rotate its secrets.

The latest infiltration of Checkmarx’s internals marks the third time TeamPCP has compromised the company’s packages in as many months.

As [previously seen](https://www.theregister.com/security/2026/04/28/ongoing-supply-chain-attack-targets-security-dev-tools/5226665) in The Register, the crooks successfully targeted Checkmarx’s AST plugin for GitHub Actions and its KICS static analysis tool back in March, deploying credential-stealing malware.

SOCRadar said the latest TeamPCP compromise of the Jenkins plugin suggests that either TeamPCP was telling the truth about Checkmarx’s secrets rotation, or its members took advantage of an additional persistence mechanism that the secur...