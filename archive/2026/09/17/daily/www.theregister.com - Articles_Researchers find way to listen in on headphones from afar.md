---
title: Researchers find way to listen in on headphones from afar
url: https://www.theregister.com/security/2026/09/17/researchers-find-way-to-listen-in-on-headphones-from-afar/5297303
source: www.theregister.com - Articles
date: 2026-09-17
fetch_date: 2026-09-18T06:53:42.548723
---

# Researchers find way to listen in on headphones from afar

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

[security](/tag/security)

# Researchers find way to listen in on headphones from afar

Eve's dropping in on Alice and Bob

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
thu 17 Sep 2026 // 20:36 UTC

### READ MORE

No content

Researchers based in China have devised a way to eavesdrop on signals handled by analog components in devices such as headphones, landline handsets, and smart devices by injecting electromagnetic (EM) signals.

The technique, referred to as InjectEave, is not simply listening in on a low-frequency analog signal. It's an EM side-channel attack that overcomes one of the longstanding barriers to exploiting EM leakage: the faintness of RF signals in devices like headphones makes it difficult for adversarial listeners to separate signal from noise.

Many different RF side-channel attacks have been explored, such as reading screen display emissions to reconstruct on-screen text or detecting the RF signals emitted by keys on a keyboard. But these techniques often prove impractical for passive EM capture because of the low signal-to-noise ratio.

REG AD

InjectEave trades passive signal capture for active signal manipulation. By transmitting a signal in the 0-9 MHz range – specifics have been withheld – an attacker can potentially modulate an otherwise difficult-to-detect audio signal so it can be captured by nearby equipment.

REG AD

"Our new project, [InjectEave](https://injecteave.github.io/), shows that RF [radio frequency] signals can induce information leakage from everyday headphones, allowing an attacker to recover headphone audio from up to 30 meters away, including through walls," said Yan Long, assistant professor at The Hong Kong University of Science and Technology (HKUST) in Guangzhou, in an email to The Register. "We have verified the new vulnerability on multiple commercial devices including devices from Sony, HP, Philips, etc."

Long and HKUST co-authors Haoran Yan, Ziyu Shao, and Shuhao Zhang, along with Qinhong Jiang of The Hong Kong Polytechnic University, describe their work in [a paper](https://injecteave.github.io/assets/paper/sec26cycle2-final651.pdf) [PDF] titled "Injected and Leaked: Actively Inducing Side-Channel Leakage Using Electromagnetic Injection and Hardware Nonlinearity," which was presented at [USENIX Security 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-haoran).

The attack targets [non-linear components](https://technav.ieee.org/topic/non-linear-analog-circuits/) found in computer systems, such as amplifiers, analog-to-digital converters, power converters, and switching MOSFETs. The interplay of the injected signals, the hardware, and the target audio signals essentially modulates the target signal so that it leaks and is detectable by the adversary.

Conducting an InjectEave attack requires commodity RF equipment: a USRP B210 software-defined radio; antennas for injection and reception; a Siglent SSA3075X Plus spectrum analyzer; a laptop for controlling the SDR; and optionally an RF power amplifier to increase attack range.

The researchers tested the technique with 11 off-the-shelf devices. One obvious application would be espionage, allowing an attacker to listen in on conversations carried over headphones or a landline phone. It could also be used to infer personal activities in households with smart fans or lamps through the monitoring and analysis of control signals and power consumption.

Tested devices include: Sony ZX110AP (2014, wired headphones); Apple Earbuds (2016, wired earbuds); UGreen MAX2, Philips TAH2020, HP H231R (2024, 2025, 2023 wireless headphones); Flyingvoice P23GW (2023, VoIP landline); OIDIRE ODI-MF10A and Xiaomi BPLDS10DM (2023, 2025 smart fans); and JINGZAO JDO-06 and Xiaomi 1S (2024, 2019 smart lamps).

"Our tests show that injection-induced side-channel attacks could eavesdrop on the majority of these devices from over 2m away and through walls, with a maximum distance of 30m for recovering intelligible headphone audio," the researchers state in their paper, noting that their tests indicate these scenarios are plausible in the wild.

For the devices listed by the researchers, ...