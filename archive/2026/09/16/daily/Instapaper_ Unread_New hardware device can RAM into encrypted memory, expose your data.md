---
title: New hardware device can RAM into encrypted memory, expose your data
url: https://www.theregister.com/security/2026/09/14/new-hardware-device-can-ram-into-encrypted-memory-expose-your-data/5296377
source: Instapaper: Unread
date: 2026-09-16
fetch_date: 2026-09-17T06:59:39.648284
---

# New hardware device can RAM into encrypted memory, expose your data

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

SECURITY

# New hardware device can RAM into encrypted memory, expose your data

Attackers would need physical access to the server to pull off the DDR5 trick

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
mon 14 Sep 2026 // 19:31 UTC

### READ MORE

* [#### AMD's Threadripper Halo is a local-AI workstation for researchers with deep pockets

  12 days ago](/on-prem/2026/09/04/amds-threadripper-halo-is-a-local-ai-workstation-for-researchers-with-deep-pockets/5294616)
* [#### VMware uses Nvidia-favored 'AI factory' brand to build something with rival AMD

  16 days ago](/virtualization/2026/08/31/vmware-uses-nvidia-favored-ai-factory-brand-to-build-something-with-rival-amd/5293520)
* [#### Intel's 256-core Xeon 7 CPUs are a Diamond in the rough

  22 days ago](/hpc/2026/08/25/intel-diamond-rapids-xeon-7-cpu-deep-dive/5292427)
* [#### OpenAI's upcoming Jalapeño chip looks like it'll be an inference beast

  22 days ago](/systems/2026/08/25/openais-upcoming-jalapeno-chip-looks-like-itll-be-an-inference-beast/5292052)
* [#### AMD grabs more CPU share while pricier PCs punish desktop demand

  26 days ago](/systems/2026/08/21/amd-grabs-more-cpu-share-while-pricier-pcs-punish-desktop-demand/5291053)

Computer security researchers have identified a design flaw in modern encryption hardware that allows access to protected memory in notionally confidential computing environments. But the attacker would need physical access to the victim system.

Boffins affiliated with KU Leuven, ETH Zurich, Durham University, and Google have found that scalable memory encryption hardware fails to check whether the data in memory is fresh.

As a result, they've been able to devise a small hardware interposer, dubbed [DDRop](https://ddropattack.eu/), that when wired to an appropriate circuit board, interferes with DDR5 write operations. Unable to tell that memory isn't fresh, a protected VM becomes vulnerable to a replay attack that uses stale, attacker-selected data.

REG AD

They describe their work in [a paper](https://github.com/ddropattack/ddrop) titled, "DDRop: Active Memory Interposer Attacks on Confidential VMs by Dropping DDR5 Writes." Their attack requires physical access and so it is relevant mainly in scenarios where confidential computing guarantees have been made to tenants by cloud service providers.

REG AD

"DDRop uses a custom-built 'interposer': a small, custom-designed circuit board, costing under $200, that sits between the processor and a memory module," explained Jo Van Bulck, a professor in the DistriNet lab at KU Leuven, Belgium, in an email to The Register. "It corrupts commands on the high-speed DDR5 memory bus to silently drop writes to encrypted memory. The protected VM keeps computing on old data that still decrypts perfectly. We are releasing the complete interposer design as open-source hardware."

The attack breaks the integrity of Intel TDX, Scalable SGX, and AMD SEV-SNP, used in trusted execution environments (TEEs).

Van Bulck and colleagues Jesse De Meulemeester, Stefan Gloor, Patrick Jattke, Daniel Moghimi, David Oswald, Martin Thompson, Kaveh Razavi, and Ingrid Verbauwhede developed a proof-of-concept attack on a current Intel TDX server.

"By injecting maliciously crafted secure page-table entries, we can force any protected VM into debug mode and read out its private memory in plaintext," said Van Bulck. "Furthermore, writing to critical TDX metadata structures enables forged attestation reports, so that a backdoored VM appears trusted to the remote user."

Both attacks, said Van Bulck, succeed deterministically in under two minutes without crashing the machine.

Several of these researchers [developed a similar attack on DDR4](https://www.theregister.com/2024/12/10/amd_secure_vm_tech_undone/). But Van Bulck said this is the first active interposer attack on DDR5.

"DDR5’s redesigned command bus prevents the address-aliasing tricks used by Battering RAM, and until now, only considerably weaker passive attacks had been demonstrated on DDR5: [TEE.fail](https://tee.fail) monitors the data bus using bulky, second-hand logic analyzers that are easier to detect and require slowing...