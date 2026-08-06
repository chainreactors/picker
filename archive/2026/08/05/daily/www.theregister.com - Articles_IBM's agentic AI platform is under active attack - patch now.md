---
title: IBM's agentic AI platform is under active attack - patch now
url: https://www.theregister.com/security/2026/08/05/ibms-agentic-ai-platform-is-under-active-attack-patch-now/5283535
source: www.theregister.com - Articles
date: 2026-08-05
fetch_date: 2026-08-06T05:02:59.752627
---

# IBM's agentic AI platform is under active attack - patch now

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
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

security

# IBM's agentic AI platform is under active attack - patch now

A critical Langflow flaw allowing RCE on default deployments is being exploited, says the CISA

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
wed 5 Aug 2026 // 17:44 UTC

A critical vulnerability in IBM-owned, low-code AI builder Langflow lets unauthenticated attackers execute code remotely on vulnerable default deployments, potentially putting organizations running those instances at immediate risk.

The Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added [CVE-2026-9198](https://www.cve.org/CVERecord?id=CVE-2026-9198) to its Known Exploited Vulnerabilities [catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-9198) after identifying evidence of active exploitation and urged organizations to apply the vendor's mitigation guidance as soon as possible. IBM says the flaw affects Langflow OSS versions 1.0.0 through 1.10.0 and recommends upgrading to version 1.10.1 or later; at the time of writing, the [most recent](https://pypi.org/project/langflow/) version is 1.11.2.

Langflow, for those unfamiliar, is one of the more accessible AI agent builders on the market, as our [hands-on look at the tool](https://www.theregister.com/special-features/2026/01/28/how-to-build-an-ai-agent-using-langflow/4258892) earlier this year demonstrated. It’s available on Linux, Windows, and macOS, and is basically an end-to-end, drag-and-drop GUI where users can construct agent workflows without having to know much, if anything, about the underlying code.

REG AD

IBM owns the platform now, but Langflow was originally developed by Logspace, which was [acquired](https://www.businesswire.com/news/home/20240404291191/en/DataStax-Acquires-Langflow-to-Make-Building-Generative-AI-Applications-100x-Easier-at-Scale) by DataStax in 2024 before [IBM scooped up](https://www.langflow.org/blog/big-news-for-langflow) DataStax, and Langflow with it, in 2025.

REG AD

The acquisition of DataStax and its tools like Langflow by IBM paved the way for Langflow to be integrated into watsonx.ai, IBM’s AI development studio, as a piece of middleware extending watsonx.ai’s capabilities.

The ownership changes, however, didn't stop the critical flaw from making it into production releases before it was finally fixed.

[According to IBM](https://www.ibm.com/support/pages/node/7278927), the vulnerability affects default Langflow deployments and combines two issues that, when chained, allow an unauthenticated attacker to execute code remotely.

First, there’s the matter of an auto-login endpoint in default deployments that’s willing to mint superuser tokens to any network caller. Combine those easily obtained superuser rights with the second issue, a code validation endpoint that’ll run any old Python code thrown at it, and you’ve got a recipe for someone taking over your entire Langflow server, or worse.

The CVE itself was [published](https://www.cve.org/CVERecord?id=CVE-2026-9198) on July 17, meaning that it hasn’t taken long for bad actors to realize what they could do with RCE on any system hosting a default Langflow deployment with auto login enabled and that code validation endpoint left accessible on a network.

Langflow itself isn’t a vibe-coding platform, instead serving as an interface for building agentic and RAG workflows, so don’t blame vibe coding or no-code security failures for this one. Instead, what we appear to have is a standard case of how default configuration deployments can easily be a disaster.

## MORE CONTEXT

* [### Using AI to code does not mean your code is more secure](/software/2026/03/26/using-ai-to-code-does-not-mean-your-code-is-more-secure/5219716)
* [### IBM insists AI didn't kill software deals, just delayed them](/software/2026/07/23/ibm-insists-ai-didnt-kill-software-deals-just-delayed-them/5276977)
* [### Smooth AI criminal drives 'first' end-to-end agentic ransomware attack](/security/2026/07/02/smooth-ai-criminal-drives-first-end-to-end-agentic-ransomware-attack/5266073)
* [### Minor edits to AI skills can make agents go rogue](/ai-ml/2026/05/22/minor-edits-to-ai-skills-can-make-agents-go-rogue/5245413)...