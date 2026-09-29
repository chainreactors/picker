---
title: JadePuffer crims hijacked Azure identities and used them to blow up cloud resources
url: https://www.theregister.com/security/2026/09/28/jadepuffer-crims-hijacked-azure-identities-and-used-them-to-blow-up-cloud-resources/5299591
source: www.theregister.com - Articles
date: 2026-09-28
fetch_date: 2026-09-29T07:41:34.790415
---

# JadePuffer crims hijacked Azure identities and used them to blow up cloud resources

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

[security](/tag/security)

# JadePuffer crims hijacked Azure identities and used them to blow up cloud resources

Smells like more agentic ransomware, Redmond warns

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
mon 28 Sep 2026 // 21:30 UTC

### READ MORE

* [#### Microsoft's Copilot super app comes with a meter attached

  15 hours ago](/ai-and-ml/2026/09/28/microsofts-copilot-super-app-comes-with-a-meter-attached/5299515)
* [#### Dutch government turns to NixOS for a sovereign desktop

  15 hours ago](/os-platforms/2026/09/28/dutch-government-turns-to-nixos-for-a-sovereign-desktop/5299501)
* [#### Microsoft tells nonprofits their deleted M365 data isn't coming back

  18 hours ago](/saas/2026/09/28/microsoft-tells-nonprofits-their-deleted-m365-data-isnt-coming-back/5299433)
* [#### Big AI's content problem: Take the work, keep the money

  1 day ago](/columnists/2026/09/27/big-ais-content-problem-take-the-work-keep-the-money/5299007)
* [#### Microsoft cells out, crams multiple values into Excel boxes

  3 days ago](/applications/2026/09/25/microsoft-cells-out-crams-multiple-values-into-excel-boxes/5299294)

The cyber criminal behind JadePuffer, the first known agentic ransomware infection reported over the summer, has also used stolen Azure identities to conduct destructive attacks on cloud storage and other resources, according to Microsoft.

In July, Sysdig threat hunters [uncovered JadePuffer](https://www.theregister.com/security/2026/07/02/smooth-ai-criminal-drives-first-end-to-end-agentic-ransomware-attack/5266073), the first-ever documented agentic ransomware infection in which an LLM drove the entire extortion operation, from gaining initial access to compromising a production database server and destroying data.

Now Redmond says that it has detected the same attacker, which it tracks as Storm-3168, up to new mischief.

REG AD

Over an 18-hour period in early June, Storm-3168 compromised two service principals and used these machine identities for “extensive Azure-focused resource destruction” and “cloud credential collection that could be used to facilitate future exfiltration,” researchers Yossi Weizman and Tushar Mudi [wrote](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/) on Friday.

REG AD

The two compromised service principals belonged to the same cloud tenant. The crims used one of them to conduct reconnaissance and resource discovery, and the other to carry out destructive operations and credential collection.

The Redmond researchers don’t know how Storm-3168 initially hijacked the service principals, but noted that an employee of the same organization previously exposed client IDs, client secrets, and tenant IDs in plaintext in a public GitHub issue.

“Since the beginning of this year, we also observed repeated probing from Storm-3168 linked infrastructure against multiple Azure App services for different customers,” the duo wrote.

The entire attack took about 18 hours, with the discovery piece lasting about 15 hours and 30 minutes. During this time, the compromised service principal collected detailed information about Azure Virtual Machines, subscriptions, resource groups, and resources, completing more than 300 successful read operations.

“This breadth of activity would give the threat actor visibility across the organization’s Azure environment,” Weizman and Mudi wrote.

About 90 minutes after the first machine identity began hoovering up Azure information, the second compromised service principal started its work, reading Azure VMs and resource groups across two subscriptions in just five seconds.

According to Redmond, both of these service principals used Storm-3168 linked infrastructure, the same network fingerprint, and the user agent python-requests/2.34.2.

About 16 hours after the initial target reads, the second service principal successfully discovered Azure App Service configuration stores - it was likely looking for exposed credentials, we’re told - and unsuccessfully attempted to find Azure OpenSearch resources.

REG AD

Seventy seconds after this, it also attempted a ...