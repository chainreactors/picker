---
title: Microsoft Defender for Endpoint leaves some Linux boxes defenseless after update
url: https://www.theregister.com/patches/2026/07/27/microsoft-defender-for-endpoint-leaves-some-linux-boxes-defenseless-after-update/5278914
source: www.theregister.com - Articles
date: 2026-07-27
fetch_date: 2026-07-28T05:00:21.919518
---

# Microsoft Defender for Endpoint leaves some Linux boxes defenseless after update

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

PATCHES

# Microsoft Defender for Endpoint leaves some Linux boxes defenseless after update

One bug disabled the security service on restart, another blocked installation on hardened RHEL systems

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)
MICROSOFT ECOSYSTEM REPORTER

Published
mon 27 Jul 2026 // 14:45 UTC

Not content with broken Windows updates, Microsoft has disclosed two problems with Defender for Endpoint on Linux – one that could disable the security service after a reboot, and another that prevents updates on FIPS-enabled Red Hat Enterprise Linux 8 and 9.

The more serious problem affected versions 101.26042.0000 through 101.26042.0009 across all supported Linux operating systems. After an upgrade or reinstall followed by a reboot, "the Defender service might be disabled on some devices," [according to Microsoft](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint-releases#linux--june-2026—101260420009).

"If you use Defender for Servers (Plan 1 or 2) with Defender for Cloud and have the MDE [Microsoft Defender Endpoint] integration enabled, automatic updates for the MDE.Linux extension are enabled by default, which means your machines could have received an affected version automatically," it explained.

REG AD

"If an affected version was installed, the issue might impact active protection on rebooted devices until remediation steps are taken."

REG AD

Microsoft did not specify what caused Defender to become disabled, but anything that could knock out endpoint protection will give administrators sweaty palms.

A separate problem affected RHEL 8 and 9 systems running in FIPS mode: the 101.26042.x update could fail to install, leaving devices on their previous version. FIPS refers to US Federal Information Processing Standards, which in this context impose requirements on the cryptography used by government and other regulated systems.

Although [Microsoft's alert](https://mc.merill.net/message/MC1438566) did not mention an available update, its release notes direct users affected by the disabled-service bug to build 101.26042.0011. The separate FIPS installation problem is fixed in version 101.26052.0011 and later.

## MORE CONTEXT

* [### Microsoft upgrades Defender to lock down Linux gear for its own good](/security/2023/01/31/microsoft-upgrades-defender-to-lock-down-linux-devices/1046723)
* [### AI is making Patch Tuesday (kinda) fun again](/patches/2026/06/09/ai-is-making-patch-tuesday-kinda-fun-again/5253225)
* [### Windows boot partition runs out of space for Microsoft's May security update](/oses/2026/05/18/windows-boot-partition-runs-out-of-space-for-microsofts-may-security-update/5241799)
* [### Microsoft puts stability in the driver's seat with new initiative](/oses/2026/05/15/microsoft-puts-stability-in-the-drivers-seat-with-new-initiative/5241381)

Microsoft Defender for Endpoint on Linux protects server workloads on-premises and in the cloud. According to Microsoft, "it helps you prevent, detect, investigate, and respond to advanced threats with unified visibility through the Microsoft Defender portal."

Other endpoint security platforms are available, but where an organization has gone all-in with Microsoft, the unified management offered by Defender for Endpoint on Linux can be difficult to resist.

Microsoft has an unfortunate habit of shipping broken updates for its flagship operating system, Windows. An update that breaks software specifically designed to protect a device takes things to another level, particularly given the relentless rise in attacks and the need to both fend them off and monitor activity. Hence the appeal of unified visibility through the Microsoft Defender portal.

However, an update that could leave Defender disabled after a reboot – while also refusing to install on some security-hardened systems – is less than ideal. ®

[security](/tag/security)
[linux](/tag/linux)
[patches](/tag/patches)
[microsoft](/tag/microsoft)

REG AD

[![](https://image.theregister.com/230490.jpg?imageId=230490&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI AND ML

## China fights back in AI spat with claim US AI companies distil Chinese models

Beijing happy to ‘take all necessary measures’ if sanctioned](https://www.theregister.com/ai-and-ml/2026/07/28/china-fights-back-in-ai-spat-with-claim-us-ai-companies-distil-chinese-models/5279315)

[ai and ml

## Leading AI models (even Grok) are all a bun...