---
title: More JFrog Artifactory bugs under attack, and all 3 have patches
url: https://www.theregister.com/security/2026/09/11/more-jfrog-artifactory-bugs-under-attack-and-all-3-have-patches/5295943
source: www.theregister.com - Articles
date: 2026-09-11
fetch_date: 2026-09-12T06:50:11.719543
---

# More JFrog Artifactory bugs under attack, and all 3 have patches

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
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

REG AD

security

# More JFrog Artifactory bugs under attack, and all 3 have patches

If you're waiting for a sign to upgrade to a fixed version: this is it

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
fri 11 Sep 2026 // 18:43 UTC

### READ MORE

* [#### AT&T store worker gets 16 months inside for SIM-swap side hustle

  14 hours ago](/cyber-crime/2026/09/11/att-store-worker-gets-16-months-inside-for-sim-swap-side-hustle/5295898)
* [#### Ukrainian lawyer's second career as a Conti coder earns him 4 years behind bars

  17 hours ago](/cyber-crime/2026/09/11/ukrainian-lawyers-second-career-as-a-conti-coder-earns-him-4-years-behind-bars/5295841)
* [#### Hundreds of AI agents helped PaperCut attacker hit 395+ orgs, and some went off script

  1 day ago](/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650)
* [#### Trezor, BitBox users targeted in newsletter phishing spree

  1 day ago](/cyber-crime/2026/09/10/trezor-bitbox-users-targeted-in-newsletter-phishing-spree/5295496)
* [#### Serial Microsoft 0-day hunter drops yet another Defender exploit

  2 days ago](/security/2026/09/09/serial-microsoft-0-day-hunter-drops-yet-another-defender-exploit/5295335)

JFrog Artifactory instances continue to get hit hard. Multiple attackers are exploiting three JFrog Artifactory bugs to gain administrative control over vulnerable instances - in some cases, just days after the vendor published a patch - and then using this illicit access to install malicious plugins and backdoors.

The three vulnerabilities are:

[CVE-2026-42018](https://docs.jfrog.com/releases/docs/jfrog-security-advisories#cve-2026-42018---anonymous-user-token-generation-exposure) is a high-severity, improper authentication flaw that can return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled. An attacker can use this token to authenticate to the repository manager and then access sensitive resources. JFrog patched this vulnerability on August 12.

REG AD

[CVE-2026-42016](https://docs.jfrog.com/releases/docs/jfrog-security-advisories#cve-2026-42016---incorrect-user-token-authorization-validation-allows-privilege-escalation) is a high-severity privilege-escalation bug. Artifactory doesn’t properly validate the token’s scope, and this can allow an attacker with low-privileged access to elevate privileges and perform actions that they should not be allowed to do. JFrog fixed this one on July 27.

REG AD

[CVE-2026-82329](https://docs.jfrog.com/releases/docs/jfrog-security-advisories#cve-2026-82329---potential-authentication-bypass-leading-to-administrative-access-in-artifactory) is a critical authentication-bypass vulnerability that allows unauthenticated attackers with network access to obtain administrative privileges. JFrog published a patch for it on August 28.

Earlier this month, security researchers told The Register that miscreants began battering internet-exposed systems vulnerable to CVE-2026-82329 just four days after JFrog disclosed the bug. In addition to creating new administrative credentials, watchTowr’s honeypot network caught miscreants “enumerating users, groups, credential sets and federated access topologies,” [said](https://www.theregister.com/security/2026/09/01/another-artifactory-cve-under-attack-by-ai-agents-or-humans/5293769) Yordan Ganchev, principal threat intelligence specialist at watchTowr.

The one thing everyone agrees upon is that attackers didn’t start exploiting any of these CVEs until after JFrog issued fixes.

In a Thursday report, Wiz security researchers “[confirmed](https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201) in-the-wild exploitation of all three vulnerabilities across multiple environments,” and noted that “patching velocity has been slow.”

JFrog has not responded to any of The Register’s inquiries about attacks against any of the three CVEs.

### 'Patching velocity has been slow'

Six weeks after JFrog disclosed CVE-2026-42016, 59 percent of organizations remain vulnerable, and 62 percent remain vulnerable to CVE-2026-42018 after four weeks...