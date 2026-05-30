---
title: Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch libraries
url: https://www.theregister.com/security/2026/05/29/14-malicious-npm-packages-impersonated-opensearch-elasticsearch-libraries/5248792
source: www.theregister.com - Articles
date: 2026-05-29
fetch_date: 2026-05-30T05:44:29.164589
---

# Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch libraries

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

# Lone attacker published 14 malicious npm packages mimicking popular OpenSearch, Elasticsearch libraries

And then Microsoft busted them all

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
fri 29 May 2026 // 22:46 UTC

A single npm user on Thursday published 14 malicious packages within a four-hour window, all mimicking popular OpenSearch, Elasticsearch, DevOps, and environment-configuration libraries, according to Microsoft.

It’s the latest in a seemingly [never-ending](https://www.theregister.com/cyber-crime/2026/05/27/supply-chain-brain-drain-npm-attacker-foolishly-leaks-own-github-private-token/5247424) [string](https://www.theregister.com/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342) of [supply chain attacks](https://www.theregister.com/cyber-crime/2026/05/19/shai-hulud-keeps-burrowing-314-npm-packages-infected-after-another-account-compromise/5242601) targeting [developer tools](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837), and [stealing cloud credentials](https://www.theregister.com/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180) and [CI/CD pipeline secrets](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780) in its wake.

Using a newly created maintainer alias, vpmdhaj (a39155771@gmail[.]com), the threat actor published 14 packages impersonating legitimate libraries from the @opensearch and @elastic ecosystems and targeting Amazon Web Services, HashiCorp Vault, GitHub Actions, and the npm registry itself. This suggests that the attacker “likely chose a developer audience to have AWS and Elastic cloud credentials in their environments,” Microsoft [warned](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/) in a Thursday blog.

REG AD

REG AD

All of the malicious packages include the same install-time stager and the same Bun-compiled, second-stage payload: a 195 KB credential harvester purpose-built for cloud and CI/CD environments.

Plus, as we’ve seen with all of the other open source supply chain attacks of late, after stealing tokens and other secrets, the attacker can move laterally across cloud environments, steal additional sensitive data, and push even more poisoned updates to packages owned by hijacked maintainer identities, thus expanding the attack beyond the initial 14.

## MORE CONTEXT

* [### Megalodon chums the waters in 5.5K+ GitHub repo poisonings](/security/2026/05/22/megalodon-chums-the-waters-in-55k-github-repo-poisonings/5245342)
* [### Malware dev tries to steal Claude users' secrets, writes npm slop, leaks own GitHub private token](/cyber-crime/2026/05/27/supply-chain-brain-drain-npm-attacker-foolishly-leaks-own-github-private-token/5247424)
* [### No fix yet for critical RCE bug in open-source Git service Gogs - exploit module is out](/security/2026/05/29/no-fix-yet-for-critical-gogs-rce-bug-exploit-module-is-out/5248691)
* [### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops](/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)

All of the malicious libraries have since been removed, and Microsoft published a list of all 14 in its blog. Give that a read to help identify systems that installed or built affected package versions on or after May 28. Be sure to also rotate an AWS IAM/STS, HashiCorp Vault, npm publish, and GitHub Actions tokens that may have been exposed.

To trick users into installing these developer tools and search engines, the attacker used [typosquatting](https://www.theregister.com/2024/11/05/typosquatting_npm_campaign/) - naming a package one or two letters off from the legitimate one - or lookalike naming (such as opensearch-setup-tool, opensearch-config-utility, and elastic-opensearch-helper) to impersonate well-known libraries.

In addition to this social engineering technique, used to drive installs through users’ typing mistakes or trust, the attacker also used two other techniques to make the supply chain attack more believable.

This includes spoofing upstream metadata. “Every unscoped package sets its package.json homepage, repository, and bugs fields to the legitimate github.com/opensearch-project/opensearch-js project,” Microsoft’s threat hunters explained.

And finally, they inflated version numbers, so the phony “releases” jump straight to 1.0.7265, 1.0.9108, or 2.1.9201 to indicate a mature release history.

After tricking users into installing the npm packages - all 1...