---
title: Progress orders emergency ShareFile server shutdown over mystery security threat
url: https://www.theregister.com/security/2026/07/13/progress-orders-emergency-sharefile-server-shutdown-over-mystery-security-threat/5270281
source: www.theregister.com - Articles
date: 2026-07-13
fetch_date: 2026-07-14T04:48:22.975392
---

# Progress orders emergency ShareFile server shutdown over mystery security threat

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
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
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
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Progress orders emergency ShareFile server shutdown over mystery security threat

Vendor insists there's no evidence of unauthorized access, but it's asking customers to take one of the most drastic precautions available

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
mon 13 Jul 2026 // 11:31 UTC

Progress Software has ordered some ShareFile customers to pull the plug on their own servers after detecting what it describes as a "credible external security threat" targeting the on-premises component of its enterprise file-sharing platform.

The emergency warning, sent by email and seen by The Register, instructed organizations running ShareFile Storage Zone Controllers to take the unusual step of manually shutting down the Windows servers that host the software, with no patch or configuration workaround yet announced.

"We have reason to believe there is a credible external security threat targeting Progress Software's ShareFile Storage Zone Controllers," the company wrote, adding that it had already disabled access to ShareFile accounts using Storage Zone Controllers, but warned this alone was not enough.

REG AD

"IMMEDIATE ACTION REQUIRED: You must manually shut down the server hosting your Storage Zone Controllers," the email continued. “This is a critical additional step to ensure the safety of your data."

REG AD

The company said the restrictions were being imposed "out of an abundance of caution" as it works with internal and external security experts to investigate the threat. Customers reported that Progress was also calling affected organizations directly to reinforce the message.

A follow-up notice over the weekend offered little additional detail. Progress said it had "no indication of unauthorized access to any ShareFile customer account or data, and we have not identified any active threat," but instructed customers to keep Storage Zone Controllers offline even as cloud services were gradually restored.

Exactly what prompted such a dramatic response remains unclear. Progress has not disclosed the nature of the threat, whether any customers have been compromised, which software versions are affected, or when administrators can safely power systems back on.

A spokesperson at Progress Software did not answer our questions, instead they sent a statement to The Register:

"Protecting our customers' data and maintaining the security of our services remain our highest priorities. As of 5 p.m. ET on Sunday, July 12, we notified all ShareFile customers with Storage Zone Controllers that their access to the Progress ShareFile cloud service has been restored. However, Storage Zone Controllers must remain turned off while we complete our investigation. At this time, we have no evidence of unauthorized access to any ShareFile customer account or data, and we have not identified any active threat. We will continue to provide customers with updates as additional information becomes available. "

The information vacuum has fueled speculation. One Progress customer on [Reddit](https://www.reddit.com/r/sysadmin/comments/1usohco/psa_shutdown_your_sharefile_storage_zone/) speculated that if the vendor is telling customers to completely shut down servers, "it's almost certainly an unauthenticated RCE being exploited in the wild."

## MORE CONTEXT

* [### Oracle E-Business Suite was under attack via critical flaw before the public exploit code was even released](/cyber-crime/2026/07/02/oracle-e-business-suite-was-under-attack-via-critical-flaw-before-the-public-exploit-code-was-even-released/5265710)
* [### Barts Health seeks High Court block after Clop pillages NHS trust data](/security/2025/12/08/barts-health-seeks-legal-block-after-clop-steals-nhs-data/2847000)
* [### Extra, extra, read all about it: Washington Post clobbered in Clop caper](/security/2025/11/13/washington-post-admits-clop-crew-lifted-bank-and-ssn-data/2449259)
* [### Red Hat fesses up to GitLab breach after attackers brag of data theft](/special-features/2025/10/03/red-hat-fesses-up-to-gitlab-breach-after-attackers-brag/428607)

Storage Zone Controllers are the on-premises component of ShareFile that allows organizations to keep files on their own infrastructure while continuing to use Progress's cloud platform for authentication and management. Because they typically sit on internet-facing Windows servers, they present an attractive target if a serious, remotely exploitable flaw emerges.

The incident also arrives just months after Progress patched two critical vulnerabilities in...