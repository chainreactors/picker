---
title: Spectre rears its ugly head again as researchers show some RISC-V chips are susceptible
url: https://www.theregister.com/security/2026/08/12/spectre-rears-its-ugly-head-again-as-researchers-show-some-risc-v-chips-are-susceptible/5286978
source: www.theregister.com - Articles
date: 2026-08-12
fetch_date: 2026-08-13T04:05:22.607325
---

# Spectre rears its ugly head again as researchers show some RISC-V chips are susceptible

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

security

# Spectre rears its ugly head again as researchers show some RISC-V chips are susceptible

Eight years on, we're still paying to hide the future glimpsed during speculative execution

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
wed 12 Aug 2026 // 20:42 UTC

If you thought that the famous Spectre security vulns were a relic of 2018, think again. Certain RISC-V chips are still very much subject to this hair-raising hole, researchers say.

Spectre refers to a family of vulnerabilities related to speculative execution, a performance optimization technique based on predicting the flow of data before instructions have been executed. Incorrect predictions get rolled back without affecting running applications but nonetheless leave traces that can be recovered and exploited to violate memory protections and access secrets.

[Spectre flaws](https://www.theregister.com/security/2018/01/02/kernel-memory-leaking-intel-processor-design-flaw-forces-linux-windows-redesign/660079) have dogged x86 and ARM chips for years, leading computer scientists to develop a series of defenses, including Indirect Branch Restricted Speculation (IBRS), Indirect Branch Prediction Barrier (IBPB), and Single Thread Indirect Branch Predictor (STIBP).

REG AD

Researchers affiliated with academic institutions in Belgium and Germany say that it's been popular to assume that the RISC-V chip architecture isn't affected by Spectre vulnerabilities because it's too simple.

REG AD

That assumption is incorrect, according to [a paper](https://www.usenix.org/conference/usenixsecurity26/presentation/gerlach) accepted at the 35th Usenix Security Symposium, "Spectre on RISC-V Silicon: Attacks and Defenses on Commercial Out-of-Order Processors." It says that commercially available [out-of-order](https://riscv.org/blog/europe-achieves-a-key-milestone-with-the-europes-first-out-of-order-risc-v-processor-chip-with-the-eprocessor-project/) RISC-V processors (SiFive P550 and T-Head Xuantie C910/C920) are vulnerable to all major Spectre variants.

RISC-V processors that process instructions in-order (SiFive U74, Xuantie C906, C908) do not appear to be vulnerable.

Prior research has shown that RISC-V processors used for academic research (e.g. BOOM, RiscyOO, RSD, Proteus, NaxRiscv, and NutShell) can be affected by one or more of the Spectre variants, but hasn't addressed commercial silicon.

"We demonstrate proof-of-concept attacks on both processors using Spectre-PHT, Spectre-BTB, SpectreRSB, and Spectre-STL, achieving up to 100 percent recall with more than 97 percent precision," the paper states.

Spectre-PHT involves mistraining the Pattern History Table; Spectre-BTB poisons the Branch Target Buffer; Spectre-RSB attacks the Return Stack Buffer; and Spectre-STL (Store To Load) exploits mispredicted store-to-load forwarding.

## MORE CONTEXT

* [### Nvidia's latest solution to soaring enterprise AI costs is...a router?](/ai-and-ml/2026/08/12/nvidias-latest-solution-for-soaring-enterprise-costs-nemo-switchyard-software-router/5286911)
* [### Microsoft-vendetta hacker has a new zero day that gives system privileges on fully patched Windows](/cyber-crime/2026/08/12/microsoft-vendetta-hacker-has-a-new-zero-day-that-gives-system-privileges-on-fully-patched-windows/5286889)
* [### OpenWALDO aims to blow the doors off proprietary AI training models](/ai-and-ml/2026/08/12/openwaldo-aims-to-blow-the-doors-off-proprietary-ai-training-models/5286864)
* [### CoreWeave revenue doubles as debt pile reaches $35.6B](/off-prem/2026/08/12/coreweave-revenue-doubles-as-debt-pile-reaches-356b/5286832)

To demonstrate the risk to RISC-V, they created a proof-of-concept Spectre exploit that leaks arbitrary Linux kernel memory on the Xuantie C910 at a rate of 338 B/s.

Software-based defenses have been developed for these vulnerabilities on x86 and ARM hardware. Unfortunately, the researchers say, these don't necessarily transfer. They also call out RISC-V hardware for its lack of introspection interfaces, necessary to observe and reason about microarchitectural features. In addition, the authors argue, the diversity of the RISC-V hardware ecosystem means that no single mitigation strategy is likely to be effecti...