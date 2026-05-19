---
title: Linux kernel flaw opens root-only files to unprivileged users
url: https://www.theregister.com/security/2026/05/18/linux-kernel-flaw-opens-root-only-files-to-unprivileged-users/5241950
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:15.803496
---

# Linux kernel flaw opens root-only files to unprivileged users

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

# Linux kernel flaw opens root-only files to unprivileged users

Plus ModuleJail, a radical proposal for minimizing the impact of similar bugs

Liam Proven
[Liam
Proven](https://www.theregister.com/author/liam-proven)

Published
mon 18 May 2026 // 17:20 UTC

Another Linux kernel flaw has handed local unprivileged users a way to peek at files they should never be able to read, including root-only secrets such as SSH keys. The bug affects multiple LTS kernel lines from 5.10 upward, although a fix has already landed – and there is now a proposal for reducing the odds of similar surprises in future.

What FOSS analytics vendor Metabase memorably dubbed the [strip-mining era of open source security](https://www.metabase.com/blog/strip-mining-era-of-open-source-security) continues. This time, the culprit is [CVE-2026-46333](https://nvd.nist.gov/vuln/detail/CVE-2026-46333), a local kernel vulnerability that lets an unprivileged user read files they should not be able to access, including those normally available only to root. An attacker who already has login access to an affected machine could therefore potentially grab SSH keys, password files, or other confidential credentials, as the [KnightLi
blog explains](https://www.knightli.com/en/2026/05/17/ssh-keysign-pwn-cve-2026-46333/).

Despite its official designation, a [demo
exploit](https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn) on GitHub calls it ssh-keysign-pwn. It is not quite as catchy a name as [Copy
Fail](https://www.theregister.com/software/2026/04/30/linux-cryptographic-code-flaw-offers-fast-route-to-root/5229187), or [Dirty
Frag](https://www.theregister.com/security/2026/05/08/dirty-frag-linux-flaw-one-ups-copyfail-with-no-patches-and-public-root-exploit/5237230), or indeed [Fragnesia](https://www.theregister.com/security/2026/05/14/dirty-frag-gets-a-sequel-as-fragnesia-hands-linux-attackers-root-level-access/5240270),
but we feel it is safe to say it hasn't been a good month.

REG AD

According to a [report
on Linux Stans](https://linuxstans.com/ai-just-found-another-linux-zero-day-and-security-researchers-are-freaking-out/), it affected LTS kernel versions 5.10, 5.15, 6.1, 6.6,
6.12, 6.18 and 7.0. The good news is that it's already been fixed: Linus
himself, in [commit 31e62c2](https://github.com/torvalds/linux/commit/31e62c2ebbfdc3fe3dbdf5e02c92a9dc67087a3a), called the fix "ptrace: slightly saner 'get\_dumpable()' logic."

REG AD

The issue was [reported
on the oss-security list](https://www.openwall.com/lists/oss-security/2026/05/15/2) on Friday by security consultancy Qualys,
as [noted
on X](https://x.com/spendergrsec/status/2054974174926430322) by grsecurity's Brad Spengler. In the same thread, Altan Baig
[pointed
out](https://x.com/acentasian/status/2054989938916270136) that the underlying issue was [reported
by Jann Horn](https://lore.kernel.org/all/20201016230915.1972840-1-jannh%40google.com/) on the Linux Kernel Mailing List way back in 2020. The problem with tracking security reports, which [Penguin
Emperor Torvalds described recently](https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633), is not new, alas.

### ModuleJail

This also seems like a good time to look at what we thought was an
interesting new defensive measure, Jasper Nuyens' [ModuleJail](https://github.com/jnuyens/modulejail). The top line of the README summarizes it:

**A single POSIX shell script that shrinks a Linux host's kernel-module attack surface by writing a modprobe.d blacklist for every kernel module not currently in use, minus a built-in baseline and an optional sysadmin whitelist. No daemons, no initramfs changes, no AI inside the tool. One script, one run, one blacklist file.**

The mention of "no AI inside the tool" is arguably something of a
giveaway, and you can see a CLAUDE.md file in the repo.

Even so, how it works is simple enough. Although Linux has a monolithic kernel, it is modular. When the kernel's source code is
compiled, the person or tool building it can choose if each individual
component is included (built into the binary), not included at all, or
compiled as a module, which can be loaded on the fly as and when it's
needed. Since the kernel is mostly device drivers, it's normal for
distribution vendors to compile most non-essential components as kernel modules –
as the [Arch
wiki explains](https://wiki.archlinux.org/title/Kernel_module). [Blacklisting](https://wiki.archlinux.org/title/Kernel_module#Blacklisting)
a module just means adding its name to a list of modules not to
load.

Blacklisting unused modules for added security isn't a new idea. It's
in the [RHEL
6 documentation](https://docs.redhat.com/en/documentation/red_hat_enterpr...