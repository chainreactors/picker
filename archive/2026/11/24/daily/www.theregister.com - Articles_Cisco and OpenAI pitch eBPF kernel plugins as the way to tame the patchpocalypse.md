---
title: Cisco and OpenAI pitch eBPF kernel plugins as the way to tame the patchpocalypse
url: https://www.theregister.com/security/2026/11/24/cisco-and-openai-pitch-ebpf-kernel-plugins-as-the-way-to-tame-the-patchpocalypse/5311795
source: www.theregister.com - Articles
date: 2026-11-24
fetch_date: 2026-11-25T10:48:26.522665
---

# Cisco and OpenAI pitch eBPF kernel plugins as the way to tame the patchpocalypse

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
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [SC 26](/special_features/sc26)
  + [Supercomputing Month 2026](/special_features/supercomputing_month_2026)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
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
* [Security](/tag/security)
* [Software](/tag/software)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Outages](/tag/outage)

REG AD

[security](/tag/security)

# Cisco and OpenAI pitch eBPF kernel plugins as the way to tame the patchpocalypse

‘Shirudo’ project promises to whip up compensating controls in a hurry

![Simon Sharwood. Asia-Pacific Editor, The Register.](https://image.theregister.com/5311211.webp?imageId=5311211&x=0.00&y=4.67&cropw=100.00&croph=66.67&width=360&height=360)

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
Asia-Pacific Editor

Published
tue 24 Nov 2026 // 01:46 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Critical Cisco remote code execution bug under attack

  1 day ago](/security/2026/11/23/critical-cisco-remote-code-execution-bug-under-attack/5311722)
* [#### Old-school Linux desktops find fresh routes to Wayland

  1 day ago](/os-platforms/2026/11/23/old-school-linux-desktops-find-fresh-routes-to-wayland/5311349)
* [#### Google claims last week’s critical VMware bug was under attack in September

  2 days ago](/virtualization/2026/11/23/google-claims-last-weeks-critical-vmware-bug-was-under-attack-in-september/5311547)
* [#### Flaws in VMware and KVM need attention, if you have time while fixing Java, PHP, and everything else

  5 days ago](/security/2026/11/20/flaws-in-vmware-and-kvm-need-attention-if-you-have-time-while-fixing-java-php-and-everything-else/5311193)
* [#### XXRI-OS explores the lowest end of the Linux desktop

  5 days ago](/os-platforms/2026/11/19/xxri-os-explores-the-lowest-end-of-the-linux-desktop/5311036)

Cisco and OpenAI have released an open-source tool called Shirudo to implement compensating controls in Linux, potentially improving security for users who can’t quickly patch newly discovered software flaws.

Shirudo relies on eBPF, the technology that makes it possible to run sandboxed programs in the Linux kernel. eBPF programs are effectively kernel plug-ins but don’t get unrestricted access to system resources.

Developers have mostly used eBPF to create network functions that enable things like the open source Kubernetes observability and security tool [Cilium](https://www.theregister.com/on-prem/2023/10/12/cilium-leaves-incubator-gets-nod-from-cncf/1022802), a Cloud Native Computing Foundation project.

REG AD

Cisco and OpenAI think eBPF can help organizations cope with the flood of [100,000-plus software flaws](https://www.theregister.com/security/2026/11/13/this-years-bug-count-just-passed-100k/5309882) reported this year, many after the debut of AI-powered bug finders.

REG AD

The increased volume of flaws, and patches to fix them, is a problem for many organizations which already struggle to test fixes or find change windows in which to implement them. That problem has seen greater interest in “compensating controls” – changes to applications or infrastructure that harden them against flaws or malware, without requiring a patch.

With Shirudo, Cisco and OpenAI are suggesting two things:

* The privileges eBPF programs enjoy make them a fine way to implement compensating controls for Linux;
* Agents should scan your infrastructure for vulnerabilities, then use tools like OpenAI’s Codex to write compensating controls as eBPF programs at machine speed.

“Shirudo” is apparently the Japanese word for “shield,” so Cisco and OpenAI have called the eBPF programs the tool creates “shields.” The two companies envision humans checking every shield Shirudo creates before putting it into production.

Shirudo is open source and available [here](https://github.com/shirudo-dev/shirudo). The two companies say they’ve already demonstrated it could mitigate the recently discovered flaws in [Java](https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661) without requiring downtime for an Elasticsearch implementation.

Cisco and OpenAI are not alone in advocating for compensating controls. Third-party software maintenance outfits like Rimini Street have used them for years to ...