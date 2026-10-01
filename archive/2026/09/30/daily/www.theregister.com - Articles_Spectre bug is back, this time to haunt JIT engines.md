---
title: Spectre bug is back, this time to haunt JIT engines
url: https://www.theregister.com/security/2026/09/30/spectre-bug-is-back-this-time-to-haunt-jit-engines/5299937
source: www.theregister.com - Articles
date: 2026-09-30
fetch_date: 2026-10-01T07:59:31.055678
---

# Spectre bug is back, this time to haunt JIT engines

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

[security](/tag/security)

# Spectre bug is back, this time to haunt JIT engines

Researchers find a way to recover stale indirect branch prediction entries

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
wed 30 Sep 2026 // 08:01 UTC

### READ MORE

* [#### Canonical begins pushing Resolute Raccoon

  13 hours ago](/os-platforms/2026/09/30/canonical-begins-pushing-resolute-raccoon/5300225)
* [#### New software dependency validation process increases speeds by 54x

  5 days ago](/software/2026/09/25/new-software-dependency-validation-process-increases-speeds-by-54x/5299256)
* [#### Asahi fork embraces LLMs and lands Linux on the M4 Mac mini

  5 days ago](/os-platforms/2026/09/25/asahi-fork-embraces-llms-and-lands-linux-on-the-m4-mac-mini/5298931)
* [#### Decades-old file security flaws found in Android, Linux, macOS, and Windows

  6 days ago](/security/2026/09/24/decades-old-file-security-flaws-found-in-android-linux-macos-and-windows/5298672)
* [#### Talk of AI in KDE sets the community ablaze

  6 days ago](/software/2026/09/24/talk-of-ai-in-kde-sets-the-community-ablaze/5298854)

The Spectre microarchitecture vulnerability has returned yet again, this time to vex just-in-time (JIT) engines that generate machine code for browsers, runtimes, and kernels.

The vulnerability is found in many CPUs that use speculative execution, the process of executing code before it is called to boost performance. Researchers found speculative execution opens the door to side channel attacks through which secrets can be exposed or inferred.

When news of that risk became known, chipmakers and OS developers [scrambled to fix these vulnerabilities](https://www.theregister.com/security/2018/01/02/kernel-memory-leaking-intel-processor-design-flaw-forces-linux-windows-redesign/660079), which were referred to as Spectre and Meltdown. And since then, researchers have found two or three dozen variations, such as 2025's [VMScape](https://github.com/comsec-group/vmscape), one of several so-called "Spectre v2" attacks that attempt to exploit indirect branch prediction, where program control is passed indirectly by pointing to an address where the next instruction can be found rather than specifying the instruction itself.

REG AD

The attacker trains the branch predictor to execute speculatively to a chosen address in order to leak data about the microarchitecture state.

REG AD

Researchers from Vrije Universiteit in the Netherlands and Scuola Superiore Sant’Anna in Italy have revived Spectre in a form called [Branch Target Reuse](https://www.vusec.net/projects/btr/) (BTR), which they describe as the first practical in-place Spectre v2 attack that attacks just-in-time (JIT) compilers. An in-place attack is confined to the victim's branch while an out-of-place attack relies on speculation directed toward a target on a different branch.

The researchers – Sander Wiebing, Yuhui Zhu, Alessandro Biondi, and Cristiano Giuffrida – found that this novel Spectre form can be conjured from code left in JIT engines including Linux cBPF, Oracle GraalVM, and Mozilla SpiderMonkey.

"The key insight behind the attack is that, while modern CPUs restore architectural code coherence after self-modification, they do not necessarily invalidate stale indirect branch prediction entries (i.e., branch targets)," the authors explain. "In JIT engines, these stale targets can outlive the original code and later be reused when the code cache is repopulated, yielding a speculative execute-after-free primitive."

The result is that an attacker can commandeer speculative control flow in a way that avoids some software defenses like [FineIBT](http://fineibt) [PDF]. The authors showed they could exploit this flaw by designing two proof-of-concept exploits against an Intel-based Linux kernel that [reveal the root password hash](https://www.youtube.com/watch?v=6en6nmF6Uyc) even with the constant binding defense provided by cBPF.

The expected leakage rate is 5.7 KB/sec for Intel Raptor Cove chips and 5.4 KB/sec for Lion Cove. It's slow but enough for an unprivileged user to c...