---
title: Word worm crawls into Copilot, spreads chaos
url: https://www.theregister.com/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588
source: www.theregister.com - Articles
date: 2026-07-29
fetch_date: 2026-07-30T04:52:41.047782
---

# Word worm crawls into Copilot, spreads chaos

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
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
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

# Word worm crawls into Copilot, spreads chaos

Researcher says months of coordination with Microsoft have yet to produce a robust mitigation

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
wed 29 Jul 2026 // 17:43 UTC

UPDATED Watch out for untrusted documents. According to research, an attacker can hide malicious instructions in a Word document that, when included in Copilot for Word’s context, may alter document output and copy the instructions into newly created files that use the affected document as source material, without the victim noticing.

Håkon Måløy, a Norwegian data scientist with a PhD in applied AI and ML, publicly disclosed the issue in a [blog post](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) Tuesday. Måløy describes the issue in considerable detail while withholding the specific prompt payload, arguing that, because no robust mitigation exists, it would be irresponsible to disclose anything beyond the class of the vulnerability.

REG AD

“To my knowledge, this is among the first public demonstrations of document-borne AI-worm self-propagation through normal workflows in a mainstream commercial productivity suite,” Måløy noted.

REG AD

Måløy said that he has been working with Microsoft since March 2026 on addressing the vulnerability, but after multiple updates to Copilot, this new class of Copilot worm is still viable. Microsoft mitigated the exploit demonstrated by his original proof-of-concept prompt, but Måløy said rewording the payload allowed him to successfully propagate the worm and alter financial data in a target document. Måløy and Microsoft twice delayed public disclosure of the issue, but, after 144 days, he said in his report that people needed to be made aware.

“The coordination period agreed with Microsoft has been exhausted, and testing shows that no robust mitigation for the broader vulnerability class is currently available,” Måløy wrote. “Two mitigation attempts, including a model upgrade, did not close the class.”

### How Copilot propagates a Word worm

Måløy explained the worm’s execution with an example involving an employee preparing a financial report for their company.

The employee downloads a market analysis from a trusted website to help with the preparation of a financial report in Copilot, unaware that the source had been compromised and the document they downloaded contains hidden malicious instructions. The hidden instructions (inserted as small white text in his proof of concept) tell Copilot to alter figures in the report the employee generates and to copy the worm into the report they create with Copilot.

If another employee later adds that report to their own work, the whole process begins again, and documents generated from it also contain the worm, and, as it spreads, it makes tracing the infection to its source extremely difficult.

“The attack can therefore continue without further involvement from either the compromised website or the original malicious document,” Måløy said. “The attacker does not need access to the victim’s Microsoft 365 tenant. The attacker only needs to share a malicious document with the victim.”

Copilot should use information in documents a user includes in its context for a project without treating instructions embedded in a document as additional prompts, Måløy said, but his research suggests it doesn't always do that.

REG AD

### A fundamental flaw

Måløy argues that he’s essentially dug up a new type of cross-domain prompt injection attack that abuses a fundamental part of modern LLM architecture.

“For AI-assistants to be useful, they often must process emails, documents, webpages, memories, tool outputs, and other information that may be controlled by an attacker,” the researcher said. But if an LLM has to process data in order to determine it contains an attack, the attack could already be influencing that determination.

“Relying on the model to detect XPIAs therefore resembles asking an interpreter to execute an untrusted program to determine whether that program is safe to execute,” Måløy asserted.

Were Microsoft or some other company to pop another model in front of that model t...