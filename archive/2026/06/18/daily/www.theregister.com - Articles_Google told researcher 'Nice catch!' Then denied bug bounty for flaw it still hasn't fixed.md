---
title: Google told researcher 'Nice catch!' Then denied bug bounty for flaw it still hasn't fixed
url: https://www.theregister.com/security/2026/06/18/google-told-researcher-nice-catch-then-denied-bug-bounty-for-flaw-it-still-hasnt-fixed/5258076
source: www.theregister.com - Articles
date: 2026-06-18
fetch_date: 2026-06-19T07:09:18.104554
---

# Google told researcher 'Nice catch!' Then denied bug bounty for flaw it still hasn't fixed

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
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

# Google told researcher 'Nice catch!' Then denied bug bounty for flaw it still hasn't fixed

EXCLUSIVE 'Working as intended' for the win … again

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 18 Jun 2026 // 16:00 UTC

EXCLUSIVE Google has a security hole in a Kubernetes operator that could allow attackers to bypass Google Cloud Platform (GCP) identity and access protections and gain full control over any organization's cloud environment. Or it has a serious communication and transparency problem when it comes to its bug bounty programs.

Maybe both.

Researcher and frequent cloud bug hunter Justin O'Leary told us that he found and reported to Google a major flaw that allows any Kubernetes namespace user to bypass GCP's Identity and Access Management (IAM) controls and therefore gain root access to managing an organization's cloud resources.

REG AD

Google initially rated the bug high priority and high severity, with a rep telling O'Leary "Nice Catch!" Then, the cloud giant changed course and told O'Leary and The Register that there's no vulnerability, so no fix and no reward payout.

REG AD

The bug report, however, is still marked high-priority and accepted.

O'Leary spoke exclusively with The Register about the vulnerability, which he named ConfigConfusion, and what has happened since he reported it to Google on March 8. He is also releasing a [blog post](https://olearysec.com/research/config-connector-authorization-bypass) with more details.

It stems from an issue in Config Connector, an open source Kubernetes add-on that lets users manage Google Cloud resources through Kubernetes.

According to O'Leary, Config Connector doesn't perform an authorization check, and this allows any Config Connector service account with org-level permissions to bypass Identity and Access Management (IAM)  authorization and gain the highest level of control (roles/owner) to an entire GCP Organization – the root node of all of a company's resources within Google Cloud.

On March 27, a Google security engineer accepted O'Leary's report and told him: "Nice catch!"

The employee said that they filed a bug based on O'Leary's report with the relevant product team and assured him the Chocolate Factory's security squad would work with relevant Google Cloud people to fix the flaw.

"We'll work with the product team to ensure this issue is address. We'll let you know when the issue was fixed," the engineer said. "In the meantime, review the payment option selected in your bughunters.google.com profile."

Google assigned the bug [P1 priority](https://developers.google.com/issue-tracker/concepts/issues) and S1 severity, signifying a flaw worthy of urgent repair because it affects a large percentage of users and can disrupt core organizational functions.

REG AD

"I figured that was the end of that," O'Leary said in a phone interview with *The Register*.

Eleven days later, on April 7, he received a new message from a Google Security Bot reversing the earlier decision. *The Reg* viewed the email, and O'Leary included a screenshot in his Thursday writeup.

The message said that the Cloud Vulnerability Reward Program panel decided that the "security impact of this issue does not meet the criteria to qualify for a reward."

After reviewing the bug report, Google determined the software "is working as intended," the message continued. It also noted that the program's decision not to pay a bounty "does not mean that the product team won't fix the issue."

Nearly three months later, the case remains P1/S1 with the status "in progress (accepted)." Google hasn't assigned a CVE or issued a fix. O'Leary didn't receive any reward for his research.

This isn't the first time this has happened to O'Leary – or other [security researchers](https://www.theregister.com/security/2026/04/19/ai-vendors-response-to-security-flaws-it-wasnt-me/5228722) [submitting bug bounty reports](https://www.theregister.com/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022).

O'Leary had a [similar experience with Microsoft](https://olearysec.com/research/azure-backup-aks-silent-patch/) earlier this year. In a story that has become [all too familiar](https://www.theregister.com/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059) among [bug hunters](https://www.theregister.com/security/2025/08/20/aws-patches-q-developer-after-prompt-injection-rce-demo/827867), O'Leary disclosed a privilege escalation vulnerability in Azure Backup for AKS. Microsoft rejected his report – and then [silently patched](https://www.theregister.com/security/2020/12/07/when-is-a-remote-code-execution-bug-in-teams-not-an-rce-when-...