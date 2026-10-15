---
title: AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host
url: https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:39.867791
---

# AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host](https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html)

**Swati Khandelwal**Oct 14, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhavZnpNnmOBy6Wnkh7wfYD4-I32k65R7uyhYW32Doh3YVqtfJaagZZ_uo9JN-cixODo6h846eR89Aa55TGuMKfXmpjZEVZQ0ssFoP4-qVX6qrvSoyfRsu_q3MQcLKwolyKeE3Lw3MByz2Su8O0XOdRWNkJmyBdwpxsAtxi5y2goE7RhOSBPOLh4Evb60c/s1700-nu-rw-lo-l85-e365/linux-exploit.jpg)

A flaw in Linux's vhost subsystem lets a local user read and write kernel memory at will and become root across nearly a decade of kernel versions. In one virtualization setup, it lets an untrusted virtual machine write to the host's memory and hijack the program that runs the virtual machine.

The bug is tracked as [CVE-2026-74580](https://github.com/zhangutah/security-research/tree/main/pocs/linux/cve-2026-74580) and named **[Vghost](https://matrix.tencent.com/en/2026/10/12/vghost-cve-2026-74580)**. Tencent Zhuque Lab, which found the flaw, released a fix on August 3 and published a full write-up on October 12 with working demos of both attacks. There is no public sign it has been exploited yet.

**vhost** is the part of the Linux kernel that speeds up network and other input/output for virtual machines and containers. A local user reaches it by opening a device node, usually /dev/vhost-net or /dev/vhost-vsock.

On the host, the flaw gives an unprivileged user a reliable way to read and write any kernel address, bypass KASLR, and escalate to root. The attack is deterministic: it needs no memory grooming and no lucky timing.

The second attack is narrower. When a virtual machine's virtio device is placed behind a virtual IOMMU with iommu\_platform turned on, and vhost runs in device-IOTLB mode, an untrusted guest can trigger the same bug and make the host kernel write out of bounds into the host's QEMU process. From there, a guest can overwrite a function pointer in QEMU and take control of where the host process runs next, or crash it.

### How it works

vhost keeps a small cache of the memory mappings behind each virtual ring and the shared queues it uses to move data. A cache hit is treated as proof that the region was already checked. The cache is cleared when the mapping is updated or invalidated and when the queue is reset, but not when the VHOST\_SET\_VRING\_ADDR or VHOST\_SET\_VRING\_NUM commands change the ring's addresses or size while the queue is live.

With a device IOTLB attached, those commands accept the new addresses without checking them, leaving that check for later. Once the cache is filled, the subsequent check never runs, and vhost continues translating new addresses using the old mapping. The kernel then copies data to or from that pointer without a bounds check, so a write to the used ring or a read of a descriptor lands outside the mapped region. That gives the attacker kernel read and write.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The flaw sat in the code for about nine years because it took two reasonable changes to create it. A 2017 change (Linux 4.11) added the cache and its shortcut. A 2020 change (Linux 5.9) moved address checking out of the command and into a later step, removing the check that would otherwise have caught the stale translation.

### Who is affected, and what to do

The flaw affects Linux kernels from 4.11 up to 7.2-rc4. Tencent reproduced the full local-user-to-root chain on five distribution kernels: Ubuntu 26.04, RHEL 9.8, Amazon Linux 2023, Microsoft Azure Linux 3.0, and Oracle Linux 10.2. On Ubuntu, the device node was limited to the kvm group, so the starting point there was a member of that group rather than any user.

On the other four tested images, the node was world-readable at mode 0666, so any local user could reach it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvMSIb2_25PHPTQKCB68TzdhT0XPGhGRqhRpaq-BLmaiJJz7LLQeak31aPVIqwJbYlTpDYr0tF6noRmL1EsPBk7gBYojjZ8RPhpnzB90SfMLOpCwVVIdsLUcoZzOdVmlnsKO8QQxB2dyMaH11iuaJWHIdS6DdDlIoqQqK9uWdzT3HrYCRl_LTmwVxsnaU/s1700-nu-rw-lo-l85-e365/linux.gif)

The fix ([commit de845981da67](https://git.kernel.org/linus/de845981da67a6b049080c87e605130b0c30adc5)) clears the cache whenever the ring is reconfigured. Install a kernel that contains it and reboot. The first fixed upstream stable releases are listed below; vendors may also backport the fix without changing their version number.

| Stable branch | First fixed version |
| --- | --- |
| 5.10.y | 5.10.265 |
| 5.15.y | 5.15.216 |
| 6.1.y | 6.1.183 |
| 6.6.y | 6.6.152 |
| 6.12.y | 6.12.104 |
| 6.18.y | 6.18.45 |
| 7.1.y | 7.1.9 |
| 7.2 | 7.2 |

[Red Hat](https://access.redhat.com/security/cve/CVE-2026-74580), [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2026-74580.html), and [Oracle Linux](https://linux.oracle.com/cve/CVE-2026-74580.html) have shipped fixes. [Ubuntu](https://ubuntu.com/security/CVE-2026-74580) has fixed 22.04 and, as of October 13, still lists its 24.04 and 26.04 kernels as in progress.

Until a fixed kernel is in place, restrict access to the vhost device nodes. Remove world access to /dev/vhost-net and /dev/vhost-vsock, limit the owning group to trusted virtualization services, and treat membership in that group as a privilege while the vulnerable kernel is running.

There is no interim workaround for the guest-to-host escape; for that path, the patched kernel is the only remedy.

### The severity, and the AI finder

The flaw is rated high, not critical, and the raters disagree on how high. The kernel.org CVE team scores it 8.8 and marks its scope as changed, because the guest-to-host write reaches memory in the host's QEMU process and crosses the boundary between a guest and its host.

[![Cybersecurity](data:image/png;base64...)](http...