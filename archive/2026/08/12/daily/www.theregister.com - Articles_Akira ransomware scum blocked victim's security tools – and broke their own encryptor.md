---
title: Akira ransomware scum blocked victim's security tools – and broke their own encryptor
url: https://www.theregister.com/research/2026/08/12/akira-ransomware-scum-blocked-victims-security-tools-and-broke-their-own-encryptor/5286515
source: www.theregister.com - Articles
date: 2026-08-12
fetch_date: 2026-08-13T04:05:23.318762
---

# Akira ransomware scum blocked victim's security tools – and broke their own encryptor

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

Security

# Akira ransomware scum blocked victim's security tools – and broke their own encryptor

Gives a whole new meaning to Safe Mode

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 12 Aug 2026 // 14:00 UTC

An Akira ransomware affiliate rebooted a victim’s computer into Safe Mode to kill its security tools – and in the process sabotaged their own malware when the limited-function startup mode also broke their encryptor.

“Akira's encryptor is engineered for speed, relying on concurrent worker threads and heavy memory mapping rather than simple sequential read-and-write operations. That high-performance design is likely what caused it to break in Safe Mode,” Huntress security operations analyst James Northey told *The Register*.

“Safe Mode loads a minimal driver set, which can restrict storage controllers and pagefile availability,” he added. “A heavy, multi-threaded encryptor strains that constrained environment far more than the lighter, streamed-I/O designs used by other ransomware families.”

REG AD

But the ending wasn't entirely happy for the victim. The attacker had already stolen credentials and data from file shares before Safe Mode prevented the ransomware from doing its job.

REG AD

Northey detailed the incident in a Wednesday [blog](https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr) and cautioned that this was more likely a memory-configuration issue, and shouldn't be taken as a practical defense to prevent Akira ransomware from locking up valuable files.

“Ultimately this could be a case of winning the battle, but not the war,” Northey wrote.

“It’s possible that a host with more physical memory or a larger page file might give akira.exe enough virtual memory to encrypt the endpoint in Safe Mode,” Northey added. “Akira’s developers or affiliates could retool the encryptor to reduce its memory demands or make its Safe Mode launch sequence more reliable, meaning that the same failure may not occur in a future intrusion.”

Nonetheless, there's one big lesson here: For the love of all that is holy, [turn on multi-factor authentication (MFA)](https://www.theregister.com/security/2025/08/04/sonicwall-investigates-cyber-incidents-amid-0-day-reports/280383).

Here’s a closer look at what happened, and how to prevent it from happening to you.

### How it started…

In early August, Huntress responded to an incident that began, [as most Akira intrusions do](https://www.theregister.com/security/2025/09/10/akira-ransomware-crims-abusing-trifecta-of-sonicwall-flaws/736510), with a [SonicWall SSL VPN](https://www.theregister.com/security/2025/07/16/crims-hijacking-fully-patched-sonicwall-vpns/593464). On August 4, the VPN logged a credential-spray attack: a burst of failed logins using bad credentials that it denied. But then, seven minutes later, one of them succeeded when the attacker used a valid VPN account that wasn’t protected by MFA.

Once they had gained access, the criminal accessed the domain controller via Remote Desktop Protocol (RDP) and queried Active Directory to hoover up detailed information about the network, users, groups, computers – essentially everything an attacker needs to know about who and what to target for lateral movement and mass encryption in a ransomware attack.

REG AD

“The enumeration was a full-property dump of every user and every computer in the domain,” Northey wrote.

## MORE CONTEXT

* [### SonicWall releases rootkit-busting firmware update following wave of attacks](/security/2025/09/23/sonicwall-releases-rootkit-busting-firmware-update/1234604)
* [### Akira ransomware crims abusing trifecta of SonicWall security holes for extortion attacks](/security/2025/09/10/akira-ransomware-crims-abusing-trifecta-of-sonicwall-flaws/736510)
* [### SonicWall investigates 'cyber incidents,' including ransomware targeting suspected 0-day](/security/2025/08/04/sonicwall-investigates-cyber-incidents-amid-0-day-reports/280383)
* [### CISA flags imminent threat as Akira ransomware starts hitting Nutanix AHV](/security/2025/11/14/akira-ransomware-starts-hitting-nutanix-ahv/2569385)

The Akira ransomware affiliate then moved to the application server to start collecting stolen data, downloading Wi...