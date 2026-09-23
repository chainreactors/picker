---
title: New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory
url: https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.495998
---

# New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory](https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Virtualization

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCjDxUEx5QKzby2TlrL6Swi0MV7BdrkgjM6Y5Xby9IU8L9JSdG09pwRemVtrYQtUrvp8QIDduyiDuojZVzZ6GrpzUJIVrThvC4CZ_kd8kckdhBt0MLWDLXD_QwN2wciIA9bqLee51246mEpWx0ZnlcOfXD2U3QWpvmpKZyxx75T7MXK-b8zBMmrouCZJc/s1700-nu-rw-lo-l85-e365/linux-kvm.jpg)

A new flaw in the Linux kernel's KVM virtualization code for ARM64 processors can leave a freed piece of host memory exposed to a guest virtual machine on hosts with nested virtualization enabled.

The bug, tracked as [CVE-2026-89775](https://www.cve.org/CVERecord?id=CVE-2026-89775), allows a guest to read and write host kernel memory, and the researcher who found it says it can be used to escape the guest and run code on the host machine.

The affected code is part of the mainline Linux kernel for ARM64, and it is fixed in Linux 6.18.51, 7.2.5, and 7.3-rc1.

Nested virtualization allows a guest to run its own hypervisor, enabling it to host virtual machines. On ARM64, it is off by default. It is [an experimental boot-time mode](https://docs.redhat.com/en/documentation/Red_Hat_Enterprise_Linux/10/html/10.1_release_notes/kernel_parameters_changes) that needs Armv8.4 hardware with a feature called FEAT\_NV2, so a plain ARM64 KVM host that never turns it on is outside the reported attack path.

The flaw sits in the part of KVM that handles nested virtualization on ARM64. When a guest arranges its memory in a certain way, a size calculation comes out as zero, and a step that should clear stale entries from the processor's address cache, a TLB invalidation, is skipped.

A page of host memory that has been freed then stays mapped and writable, and the guest can read and write it 64 bits at a time, with no hardware trap to hand control back to the host.

Hyunwoo Kim, the security researcher who reported the flaw and [disclosed it on September 16](https://www.openwall.com/lists/oss-security/2026/09/16/14), says a guest can use this to escape to the host, breaking out of its own virtual machine to run code on the underlying machine. No exploit code has been published, and there is no sign the flaw has been used in an attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The kernel's own record lists the affected code as present from Linux 6.16. But the author tagged the fix against a later change, and the maintainer who [reviewed and tested it](https://ratatoskr.run/kvmarm/2026/07/17324847/t) said the "missed invalidation only starts at v6.17." By that account, a host on 6.16 carries the code but not the behavior an attacker needs.

There is a second way to abuse the flaw. On systems where any user can open /dev/kvm, the device a program uses to create a virtual machine, a local user could build a guest and use the same bug to gain root, Kim says.

He points to Red Hat Enterprise Linux, where that device is open to all users by default. Red Hat lists its version 10 kernel as affected and versions 6 through 9 as not affected. This path still needs the host to have nested virtualization enabled.

### Which Kernels Are Fixed

Upstream, the flaw is fixed in Linux 6.18.51, 7.2.5, and 7.3-rc1. Distributions are shipping the fix on their own schedules, and status differs by release.

| Kernel or distribution | Status as of September 22 |
| --- | --- |
| Mainline Linux | Fixed in 6.18.51, 7.2.5, and 7.3-rc1 |
| [Red Hat Enterprise Linux](https://access.redhat.com/security/cve/cve-2026-89775) | Version 10 kernel affected; versions 6 through 9 not affected |
| [Ubuntu](https://ubuntu.com/security/CVE-2026-89775) | 26.04, including its AWS, Azure, and GCP kernels, vulnerable; 24.04 LTS general kernel not affected, though its newer hardware-enablement kernels (6.17, 7.0) are vulnerable |
| [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2026-89775.html) | AL2023 kernel6.18 package: fix pending; other Amazon Linux kernels not affected |
| [Debian](https://security-tracker.debian.org/tracker/CVE-2026-89775) | bookworm and trixie not affected (code not present); sid fixed in 7.2.6-1; forky vulnerable |

For hosts that cannot yet be patched, Red Hat says no mitigation meets its criteria for a workaround. The one certain thing is scope: the attack only targets hosts with nested virtualization enabled, which is not the default on ARM64.

Vendors score the flaw from 7.8 to 9.3 out of 10. They agree the impact is high and the attack is local, meaning it cannot be launched over a network. The spread reflects how difficult each vendor thinks the flaw is to exploit, and Ubuntu, which shows the 9.3 figure, sets its own priority to medium.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

As of September 22, the flaw was not in the U.S. CISA catalog of exploited vulnerabilities, and its predicted exploitation score was below 1%.

The disclosure raises the question of whether cloud tenants could use the flaw to break into a provider's machines. On the largest providers, the configuration it needs is not on offer: Amazon Web Services lists only [Intel-based instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) for nested virtualization, and Google Cloud [excludes its ARM virtual machines](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) from it.

That is not a clean bill of health for those platforms, but the specific path this flaw takes is not exposed in their standard ARM offerings.

CVE-2026-89775 is the fourth KVM guest-to-host escape Kim has disclosed this year. Two were in the x86 version of KVM: [Januscape](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html) in July and ...