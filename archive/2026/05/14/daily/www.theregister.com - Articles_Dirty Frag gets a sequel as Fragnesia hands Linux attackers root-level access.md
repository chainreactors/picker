---
title: Dirty Frag gets a sequel as Fragnesia hands Linux attackers root-level access
url: https://www.theregister.com/security/2026/05/14/dirty-frag-gets-a-sequel-as-fragnesia-hands-linux-attackers-root-level-access/5240270
source: www.theregister.com - Articles
date: 2026-05-14
fetch_date: 2026-05-15T05:53:29.838925
---

# Dirty Frag gets a sequel as Fragnesia hands Linux attackers root-level access

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

# Dirty Frag gets a sequel as Fragnesia hands Linux attackers root-level access

Fresh kernel flaw comes with public exploit code and continues ugly run of highly reliable privilege escalation bugs tied to memory and page-cache handling

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
thu 14 May 2026 // 11:01 UTC

Linux admins hoping Dirty Frag was a one-off horror from the kernel networking stack are about to have a considerably worse week.

Researchers at [Wiz have published an analysis](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp) of "Fragnesia," a Linux kernel local privilege escalation flaw discovered by William Bowling of the V12 security team that allows unprivileged users to gain root by corrupting page cache memory. The bug, tracked as CVE-2026-46300, has public proof-of-concept exploit code [documented by V12 on GitHub](https://github.com/v12-security/pocs/tree/main/fragnesia) that demonstrates the vulnerability being used against /usr/bin/su to spawn a root shell.

According to Google-owned Wiz, the flaw sits in the Linux kernel's XFRM subsystem, specifically ESP-in-TCP processing tied to IPsec support. By carefully triggering the bug, attackers can modify protected file data in memory without changing the original files stored on disk.

REG AD

Wiz describes Fragnesia as part of the broader "Dirty Frag" bug family rather than a completely separate class of issue. Dirty Frag itself only surfaced days ago and was already attracting attention thanks to public exploit code, incomplete patch coverage, and unusually reliable privilege escalation.

REG AD

According to researcher Hyunwoo Kim, who uncovered Dirty Frag, "Fragnesia" emerged as an unintended side effect of patches shipped to fix the original Dirty Frag vulnerabilities, adding yet another entry to the long tradition of security fixes accidentally creating new security problems.

As The Register previously reported, [Dirty Frag](https://www.theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230) followed hot on the heels of [Copy Fail](https://www.theregister.com/software/2026/04/30/linux-cryptographic-code-flaw-offers-fast-route-to-root/5229187), another Linux kernel privilege escalation flaw that abused page cache handling to overwrite supposedly read-only files.

## MORE CONTEXT

* [### Linux kernel maintainers pitch emergency killswitch after CopyFail and Dirty Frag chaos](/oses/2026/05/11/linux-kernel-maintainers-pitch-emergency-killswitch-after-copyfail-and-dirty-frag-chaos/5237801)
* [### Half of exposed React servers remain unpatched amid active exploitation](/security/2025/12/12/half-of-exposed-react-servers-remain-unpatched-amid-attacks/2826645)
* [### Anthropic’s bug-hunting Mythos was greatest marketing stunt ever, says cURL creator](/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)
* [### AI bug reports went from junk to legit overnight, says Linux kernel czar](/software/2026/03/26/linux-kernel-czar-says-ai-bug-reports-arent-slop-anymore/5226256)

Historically, local Linux privilege escalation bugs had a reputation for being unreliable, crash-prone, or fiddly enough that attackers needed good timing and a fair bit of luck to pull them off cleanly. Fragnesia looks different, as Wiz and V12 both say the exploit avoids race conditions entirely, making it far more predictable than older Linux root exploits like [Dirty COW](https://www.theregister.com/security/2018/11/08/oops-cisco-accidentally-leaked-in-house-dirty-cow-exploit-code-with-biz-conf-call-software/1275153).

That makes the bug much more useful after an initial compromise. An attacker who gains access to a system through phishing, stolen credentials, or a vulnerable cloud workload suddenly has a cleaner path to full root access.

The V12 proof-of-concept repository is already public, while Linux vendors have started pushing out advisories and mitigation guidance. AlmaLinux [warned](https://almalinux.org/blog/2026-05-13-fragnesia-cve-2026-46300/) that all supported releases are affected and urged administrators to patch quickly or disable unused ESP-related functionality where possible.

Similar advisories have also been issued by Amazon Linux, CloudLinux, Debian, Gentoo, Red Hat Enterprise Linux, SUSE, and Ubuntu as distributors scramble to assess exposure across supported kernel versions.

Microsoft also [urged](https://x.com/MsftSecIntel/status/2054701609024934064) organizations to patch quickly, noting that though it had not observed in-the-wild exploitation so far, Fragnesia "can modify any file readable by the user, including [/]etc[/]passwd."

The Linux networking st...