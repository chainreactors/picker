---
title: Security researcher claims they found KVM guest-host escape flaw
url: https://www.theregister.com/offbeat/2026/10/06/security-researcher-claims-they-found-kvm-guest-host-escape-flaw/5301267
source: www.theregister.com - Articles
date: 2026-10-06
fetch_date: 2026-10-07T07:55:48.283344
---

# Security researcher claims they found KVM guest-host escape flaw

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
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
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

[offbeat](/tag/offbeat)

# Security researcher claims they found KVM guest-host escape flaw

Firecracker MicroVMs, which started at AWS, seem to be the problem

![Simon Sharwood, Reg APAC editor](https://image.theregister.com/5299461.webp?imageId=5299461&x=0.00&y=6.18&cropw=100.00&croph=66.89&width=360&height=360)

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
tue 6 Oct 2026 // 03:06 UTC

### READ MORE

* [#### South Korean president calls for creation of tools that stop all cyber-attacks

  2 hours ago](/public-sector/2026/10/07/south-korean-president-calls-for-creation-of-tools-that-stop-all-cyber-attacks/5301533)
* [#### Anthropic reconfigures its cool kids security program

  7 hours ago](/security/2026/10/07/anthropic-reconfigures-its-cool-kids-security-program/5301509)
* [#### Trump Mobile customers' data dumped - and some never even received their gold device

  13 hours ago](/security/2026/10/06/trump-mobile-customers-data-dumped-and-some-never-even-received-their-gold-device/5301433)
* [#### Microsoft extends the Outlook naughty step with two more file types

  15 hours ago](/software/2026/10/06/microsoft-extends-the-outlook-naughty-step-with-two-more-file-types/5301350)
* [#### Zombie instructions on carefully constructed web pages could trick GitHub Copilot CLI into sharing secrets

  17 hours ago](/ai-and-ml/2026/10/06/zombie-instructions-on-carefully-constructed-web-pages-could-trick-github-copilot-cli-into-sharing-secrets/5301206)

Linux KVM, the hypervisor favoured by hyperscale clouds, apparently has a full VM escape bug.

That nasty news came from security researcher Paulos Yibelo, who on X [shared a screenshot](https://x.com/PaulosYibelo/status/2106378929158135903) of a bug bounty award he won for discovering what he described as “Full VM escape zeroday (guest>host root in industry standard hypervisors)!”

The bug bounty Yibelo participated in is run by Vercel, a company that provides MicroVMs as sandboxes for AI agents to work inside. The company’s Sandbox uses Firecracker MicroVMs, a technology [created by AWS](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/), which relies on Linux KVM – the kernel level hypervisor in Linux.

REG AD

Vercel CEO Guillermo Rauch [named](https://x.com/rauchg/status/210640202480402065) KVM as the hypervisor identified by Yibelo.

REG AD

“We’ve confirmed a KVM 0day through our Vercel Sandbox bounty program. Affecting the industry’s gold standard solution for Linux virtualization,” he wrote.

And that’s all the info that has made it into the public view at this time. *The Register* can find no chat on relevant mailing lists. We have asked Rauch and Yibelo for additional details.

Hopefully, we don’t hear from either of them for days or weeks, for two reasons.

One is that guest-host escapes are the nightmare virtualization scenario because they mean whoever runs a guest VM could take over an entire server, and perhaps gain the ability to control other guests.

The other is that KVM is astoundingly prevalent: AWS and Google both use it to power their public clouds. Enterprise virtualization players Nutanix, HPE, and Proxmox also rely on KVM. And of course KVM is also in Firecracker, which is open source and could therefore be running in all sorts of places.

Whatever Yibelo discovered therefore very much needs a responsible disclosure process, because if hints about the flaw emerge it could allow attackers to do a lot of damage.

Once a fix is found, the next question is whether implementing it will require disruption or downtime. It’s possible to hot-patch KVM, and to migrate live VMs from vulnerable hosts to machines running a patched version of Linux. Hopefully those techniques will work.

This might be the second nasty bug discovered in KVM this year, after the so-called [Januscape](https://www.theregister.com/virtualization/2026/07/21/ovh-reveals-semi-secret-plan-to-fix-critical-januscape-hypervisor-bug-with-mass-reboots-and-an-australian-crash-test-dummy/5275359) flaw.

REG AD

Beyond the potential risks this bug created, ob...