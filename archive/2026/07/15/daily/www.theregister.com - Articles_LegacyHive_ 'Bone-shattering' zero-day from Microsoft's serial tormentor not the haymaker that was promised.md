---
title: LegacyHive: 'Bone-shattering' zero-day from Microsoft's serial tormentor not the haymaker that was promised
url: https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723
source: www.theregister.com - Articles
date: 2026-07-15
fetch_date: 2026-07-16T04:59:02.263032
---

# LegacyHive: 'Bone-shattering' zero-day from Microsoft's serial tormentor not the haymaker that was promised

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

# LegacyHive: 'Bone-shattering' zero-day from Microsoft's serial tormentor not the haymaker that was promised

Experts say it’s a useful post-compromise tool, for those with the brain cells required to put it together

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 15 Jul 2026 // 13:59 UTC

Microsoft’s worst nightmare - a prolific zero-day vulnerability hunter who calls themselves Nightmare Eclipse - published yet another zero-day on Tuesday, a vulnerability allowing attackers to mount user hives, including partial exploit code.

Suspected of being a disgruntled former Microsoft engineer, based on the sophistication of their prior vulnerabilities, NightmareEclipse came good on their promise to release another zero-day on July 14. Whether it lives up to the [promised “bone-shattering” standard](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) touted in June is up for debate, however.

Called “LegacyHive,” the proof of concept (PoC) code for the zero-day local privilege escalation (LPE) vulnerability targets [Windows’ user hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives) - the section of the Windows Registry that stores a user's specific desktop settings, application preferences, and environment configurations.

REG AD

The code exploits a weakness in profsvc, the Windows User Profile Service, and the way in which it loads hives. If exploited correctly it could grant regular users privileged read-write access to target other users' hives.

REG AD

Matei Badanoiu, lead security researcher at Pentest-Tools.com, said that while the exploit could prove useful for attackers who had already gained a foothold in a target environment, it falls short of providing a fuller system compromise.

“What caught my attention is the difference between what the public proof of concept actually demonstrates and what a full compromise would require,” he told The Register. “LegacyHive is a local privilege escalation in the Windows User Profile Service. It abuses arbitrary registry hive loading, so a standard user can mount another user’s hive, including an administrator’s, into their own classes root.

“For an attacker who already has a foothold, that is a genuinely useful primitive. Bundling it with credential access and persistence into ‘full compromise’ is more of an ambition than the released code.”

The LegacyHive publication differs from some of NightmareEclipse’s earlier drops in that the PoC code is stripped back in an effort to prevent widespread exploitation.

According to the bug hunter, there is more than one way of exploiting the profsvc flaw.

The public PoC requires additional user credentials for it to work, and is limited to the usrclass.dat hive.

NightmareEclipse said the original PoC, which differs from the one they published, does not require additional user credentials to exploit the bug, and it works beyond the usrclass.dat hive, “but you would need some brain cells to make the PoC do it.”

## MORE CONTEXT

* [### Microsoft's worst 'Nightmare' unleashes BitLocker bypass 0-day](/security/2026/06/11/nightmare-eclipse-drops-claimed-bitlocker-bypass-for-microsoft-windows/5254371)
* [### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops](/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)
* [### Angry bug hunter with Microsoft beef drops new Windows 0-day](/security/2026/06/10/nightmare-eclipse-publishes-new-windows-defender-zero-day/5253725)
* [### Mystery Microsoft bug leaker keeps the zero-days coming](/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)

This represents a divergence from NightmareEclipse’s previous approaches.

REG AD

As Badanoiu pointed out to us, some of NightmareEclipse’s earlier drops, such as BlueHammer and RedSun, went from PoC to widespread exploitation within days.

LegacyHive, however, comes without a fully working PoC and a CVE identifier.

Regardless, security experts told The Register that cyber practitioners should respond promptly since capable attackers could probably build a reliable exploit, despite the gaps left in the PoC by NightmareEclipse.

“Threat intelligence teams are advised to act with some urgency here,” said Dray Agha, senior manager of security operations at Huntress. “Huntress observed NightmareEc...