---
title: NoisyTCP bug gives Linux servers a remote crash problem 11 years in the making
url: https://www.theregister.com/security/2026/11/16/noisytcp-bug-gives-linux-servers-a-remote-crash-problem-11-years-in-the-making/5310144
source: www.theregister.com - Articles
date: 2026-11-16
fetch_date: 2026-11-17T09:57:52.755554
---

# NoisyTCP bug gives Linux servers a remote crash problem 11 years in the making

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
  + [Supercomputing](/special_features/supercomputing_month_2026)
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
* [Security](/security)
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Supercomputing](/special_features/supercomputing_month_2026)

REG AD

[security](/tag/security)

# NoisyTCP bug gives Linux servers a remote crash problem 11 years in the making

Flaw can take down an entire host, even when the vulnerable service is running inside a container

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
mon 16 Nov 2026 // 18:28 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Omaxian takes the Omarchy look down a different Linux backstreet

  23 hours ago](/os-platforms/2026/11/16/omaxian-takes-the-omarchy-look-down-a-different-linux-backstreet/5309750)
* [#### Microsoft’s Azure Linux dons Fedora to dress itself up for mainstream workloads

  1 day ago](/os-platforms/2026/11/16/microsofts-azure-linux-dons-fedora-to-dress-itself-up-for-mainstream-workloads/5310016)
* [#### Another Linux kernel developer steps back from some duties due to overload

  3 days ago](/ai-and-ml/2026/11/13/another-linux-kernel-developer-steps-back-from-some-duties-due-to-overload/5309628)
* [#### Linux joins Heathrow's grounded fleet of information screens

  5 days ago](/offbeat/2026/11/11/linux-joins-heathrows-grounded-fleet-of-information-screens/5308738)
* [#### Microsoft's Azure Linux gets 470-plus security fixes in one almighty patching session

  7 days ago](/security/2026/11/09/microsofts-azure-linux-gets-470-plus-security-fixes-in-one-almighty-patching-session/5308434)

The researcher who sounded the alarm over Dirty Frag earlier this year has uncovered another Linux kernel flaw, and this one lets attackers crash entire servers remotely without so much as a password.

The vulnerability, tracked as CVE-2026-99288 and dubbed NoisyTCP, was [discovered by security researcher Hyunwoo Kim](https://github.com/V4bel/NoisyTCP), who says it affects almost all Linux distributions. The flaw dates back to October 2015 and went unnoticed until this year, when Kim found and patched it.

Attackers don't need to log in or get their hands on any credentials to cause trouble. They can simply knock the server over, although there's no evidence yet that the flaw can be used to steal data or hijack a machine.

REG AD

The bug is buried in Linux's TCP networking code. Two parts of the kernel can trip over each other while processing incoming traffic, leaving one trying to use memory that's already been freed. When that happens, Linux can panic and take the whole machine down with it.

REG AD

Kim says there's no need for any special server configuration either. Services such as Nginx, Apache, and SSH can be vulnerable straight out of the box. An attacker needs access to an open TCP port on a system that processes incoming network traffic across multiple receive queues or CPUs.

Perhaps more concerning for administrators running containerized workloads, the damage isn't necessarily limited to the application being attacked. Because the flaw sits in the Linux kernel, crashing a web server inside a container can take down the underlying host and anything else running on it.

Kim found that the attack was particularly effective against virtual machines. During testing, he managed to crash Nginx, Apache, and SSH servers running on QEMU/KVM virtual machines in between five seconds and two minutes.

Physical hardware put up more of a fight. Even after tailoring his exploit to the target machine, Kim needed roughly 14 hours to crash a bare-metal server running Nginx.

Kim has a knack for finding holes in Linux. Back in May, he [uncovered Dirty Frag](https://www.theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230), a kernel bug that allowed local users to gain root privileges. That one caused headaches for administrators when a working exploit went public before patches were ready.

His latest discovery, NoisyTCP, has another potentially nasty trick up its sleeve. Kim identified a second exploitation path involving a use-a...