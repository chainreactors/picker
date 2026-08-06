---
title: New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch
url: https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:52.039863
---

# New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch

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

![cybersecurity](data:image/svg+xml;base64...)

# [New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch](https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html)

**Swati Khandelwal**Aug 05, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhWC9UfjMK9e0KvUrcCjymLYZzuDDgZpArW3oZPtcds7CJ1pr1GleT46Wlm2_aWWpoe6TpgYcdnz_jhVOgjK6mnW_gekJkMotmfRiQ0xcp5v7mdx6CvVvUID0IyfSplGHGX-8JGoMJ1OLyEA96qVMTWwhEjKf21thNfvkBCg2DSgNjSkVEDyAugdcyJfk/s1700-e365/linux-exploit.jpg)

A memory corruption flaw in the Linux kernel's Open vSwitch datapath gives ordinary local users a path to root on a broad set of default-configured distributions, and a public exploit ships with pre-built records for roughly 800 kernel builds.

The vulnerability, tracked as **CVE-2026-64531** (CVSS score: 7.8) and codenamed **OVSwrap** by its discoverer, was disclosed by security researcher Asim Manizada on July 28, 2026.

The bug sits in the kernel datapath, not the userspace ovs-vswitchd daemon. In a [technical write-up](https://heyitsas.im/posts/ovswrap/), Manizada said an attacker needs "no existing OVS bridge, no running ovs-vswitchd, no host-level CAP\_NET\_ADMIN."

On affected systems where the OVS kernel datapath is available and unprivileged user namespaces are enabled, an ordinary user can create private user and network namespaces with unshare -Urn, gain CAP\_NET\_ADMIN inside that namespace, and reach the vulnerable flow-installation path.

If the openvswitch module is installed but not loaded, resolving its Generic Netlink family name can load it automatically. An empty lsmod output does not mean a system is safe.

The [upstream fix](https://github.com/torvalds/linux/commit/3f1f755366687d051174739fb99f7d560202f60b) shipped in stable trees on July 24. Where a patched vendor kernel is not yet available, and Open vSwitch is not required, block future module loads; if the module is already resident, unload it or reboot.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Manizada said he reported the issue to security@kernel.org and the OVS maintainers on June 19. The first fixed upstream releases are Linux 5.15.212, 6.1.178, 6.6.145, 6.12.97, 6.18.40, and 7.1.5. The end-of-life 6.13 through 6.17, 6.19, and 7.0 series will not receive upstream stable fixes.

Those upstream numbers are not enough on their own. Distribution kernels carry backports and downstream changes, so the vendor tracker is the safer source of truth.

Open vSwitch stores generated flow actions as Netlink attributes whose nla\_len field is 16 bits wide, capping any single nested attribute at 65,535 bytes. The unsafe assignment had existed for 13 years, but a 32 KiB cap on the total generated action stream kept a nested action below the wrap point.

A [March 2025 change](https://github.com/torvalds/linux/commit/a1e64addf3ff9257b45b78bc7d743781c3f41340) removed that cap because it produced unpredictable failures, including in large OpenStack deployments, and exposed the older truncation bug. The enabling commit's review thread discussed reliability and user-facing failures but did not address the security consequence of removing the guard.

An attacker submits a CLONE action packed with hundreds of conntrack sub-actions. On x86-64, the kernel expands each one to 164 bytes, pushing the generated nested action past 65,535 bytes. When OVS writes the result into the 16-bit length field, the value wraps.

Later code trusts that length and resumes parsing from inside attacker-controlled conntrack data, where forged OVS actions are waiting. Because the landing point is deterministic inside the same contiguous buffer, no heap grooming is required.

Manizada described the result as a memory corruption vulnerability with "logic-bug-grade reliability."

The exploit chains three primitives from the wraparound: a kernel pointer leak through a fake OUTPUT action, an arbitrary kernel read through a forged tunnel SET action, and a targeted decrement through teardown of a forged tun\_dst pointer. It uses those primitives to find a host process's credentials and, on modern kernels, decrement fsuid and fsgid to zero.

The released proof-of-concept is explicitly destructive. It also requires OVS conntrack support, the FTP conntrack helper, and sudo to be installed.

On success, it corrupts a live kernel credential, modifies /etc/sudoers.d or /etc/sudoers, opens a root shell, and leaves processes and OVS state behind to avoid unsafe teardown. The [PoC repository](https://github.com/manizada/OVSwrap) includes records for roughly 800 exact x86-64 kernel builds and attempts dynamic derivation from symbols or BTF for uncovered builds.

Manizada's non-exhaustive test matrix found default-config exploitation on tested AlmaLinux 9 and 10, Alpine 3.22 through 3.24, Amazon Linux 2023, Arch, CentOS Stream 9 and 10, Debian 12 and 13, Fedora 42 through 44, Gentoo, Kali 2026.1, Linux Mint 22.3, NixOS, openSUSE Tumbleweed, Pop!\_OS, Rocky Linux 9 and 10, and Ubuntu 22.04.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

On tested Ubuntu 24.04 systems, AppArmor blocked direct namespace creation, but the PoC's aa-exec -p trinity fallback restored reachability. Stock Ubuntu 26.04 blocked the ordinary-user route; disabling its AppArmor user-namespace restriction made the tested systems exploitable.

Tested Amazon Linux 2, Debian 11, Rocky Linux 8, and Ubuntu 20.04 retained older code paths and were not exploitable through this route.

Install a patched vendor kernel where one is available. Where Open vSwitch is not required, the fastest interim step is a module block:

echo 'install openvswitch /bin/false' > /etc/modprobe.d/ovswrap.conf

The override blocks future module-load attempts; a module already resident in memory must still be removed or cleared by rebooting.

Disabling unprivileged user namespaces closes the ordinary local-user route but does not block a container or other process that already has CAP\_NET\_ADMIN over an attacker-controlled network namespace. Manizada described the container direction as theoretically reachable but did not demonstrate it in the released PoC. The PoC repository also includes an emergency BPF guard for environments that must ke...