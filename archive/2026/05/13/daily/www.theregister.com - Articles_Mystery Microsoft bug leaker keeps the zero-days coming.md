---
title: Mystery Microsoft bug leaker keeps the zero-days coming
url: https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758
source: www.theregister.com - Articles
date: 2026-05-13
fetch_date: 2026-05-14T05:47:25.656961
---

# Mystery Microsoft bug leaker keeps the zero-days coming

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

Security

# Mystery Microsoft bug leaker keeps the zero-days coming

Security pros warn YellowKey claim could make stolen laptops a much bigger problem

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 13 May 2026 // 17:16 UTC

The anonymous security researcher who has already maliciously exposed three Windows zero-days this year has revealed two more, dropping them just after Microsoft's monthly Patch Tuesday update.

Nightmare-Eclipse, or Chaotic Eclipse, depending on which of their aliases you prefer, released details about [YellowKey](https://github.com/Nightmare-Eclipse/YellowKey) and [GreenPlasma](https://github.com/Nightmare-Eclipse/GreenPlasma) - respectively a BitLocker bypass and a privilege escalation flaw, handing SYSTEM access to attackers.

Experts speaking to The Register warned that both vulnerabilities present serious security concerns, especially since Nightmare-Eclipse released substantial technical information about exploiting them.

REG AD

Nightmare-Eclipse described YellowKey as "one of the most insane discoveries I ever found." They provided the files, which have to be loaded onto a USB drive, and if the attacker completes the key sequence correctly, they are granted unrestricted shell access to a BitLocker-protected machine.

REG AD

When it comes to claims like these, we usually exercise some caution, as this bug requires physical access to a Windows PC. However, seeing that [BitLocker](https://www.theregister.com/security/2026/01/23/surrender-as-a-service-microsoft-unlocks-bitlocker-for-feds/4387769) acts as Windows' last line of defense for stolen devices, bypassing the technology grants thieves the ability to access encrypted files.

Rik Ferguson, VP of security intelligence at Forescout, said: "If [the researcher's claim] holds up, a stolen laptop stops being a hardware problem and becomes a breach notification."

Despite the physical access requirement, Gavin Knapp, cyber threat intelligence principal lead at Bridewell, told The Register that YellowKey remains "a huge security problem for organizations using BitLocker."

Citing information shared in cyber threat intelligence circles, he added that YellowKey can be mitigated by implementing a BitLocker PIN and a BIOS password lock.

Nightmare-Eclipse hinted at YellowKey also acting as a backdoor, allegedly injected by Microsoft, although the people we spoke to said this was impossible to verify based on the information available.

The researcher also published partial exploit code for GreenPlasma, rather than a fully formed proof of concept exploit (PoC).

Ferguson noted attackers need to take the code provided by the researcher and figure out how to weaponize it themselves, which is no small task: in its current state it triggers a UAC consent prompt in default Windows configurations, meaning a silent exploit remains a work in progress.

Knapp warned that these kinds of privilege escalation flaws are often used by attackers after they gain an initial foothold in a victim's system.

REG AD

"These elevation of privilege vulnerabilities are often weaponized during post-exploitation to enable threat actors to discover and harvest credentials and data, before moving laterally to other systems, prior to end goals such as data theft and/or ransomware deployment," he said.

## MORE CONTEXT

* [### Doozy of a Patch Tuesday includes 30 critical Microsoft CVEs](/patches/2026/05/13/doozy-of-a-patch-tuesday-includes-30-critical-microsoft-cves/5239224)
* [### Microsoft's massive Patch Tuesday: It's raining bugs](/security/2026/04/14/microsofts-massive-patch-tuesday-its-raining-bugs/5219841)
* [### Researchers claim Windows Defender can be fooled into deleting databases](/security/2024/04/22/researchers-windows-defender-attack-can-delete-databases/319027)
* [### Surrender as a service: Microsoft unlocks BitLocker for feds](/security/2026/01/23/surrender-as-a-service-microsoft-unlocks-bitlocker-for-feds/4387769)

"Currently, there is no known mitigation for GreenPlasma. It will be important to patch when Microsoft addresses the issue."

### Four, five… and more?

YellowKey and GreenPlasma are the latest in a series of five Microsoft zero-day bugs the researcher has exposed this year.

When Nightmare-Eclipse [released BlueHammer](https://www.theregister.com/security/2026/04/14/microsofts-massive-patch-tuesday-its-raining-bugs/5219841) (CVE-2026-32201, 6.5) - patched by Microsoft in April - they were described as a disgruntled researcher who has since been rumored to be a former Microsoft employee.

According to their maiden blog post under the Chaotic Eclipse alias, the bug leak began after an alleged violation of trust.

"I never wanted to reopen a blog and a new [GitHub](https://www.theregis...