---
title: A Server That Forgets: Exploring Stateless Relays
url: https://blog.torproject.org/exploring-stateless-relays/
source: Tor Project blog
date: 2026-04-08
fetch_date: 2026-04-09T04:32:24.054457
---

# A Server That Forgets: Exploring Stateless Relays

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# A Server That Forgets: Exploring Stateless Relays

by [Osservatorio Nessuno](/author/osservatorio%20nessuno)
| April 8, 2026

![](/exploring-stateless-relays/lead.png)

Running Tor relays requires constant work against adversaries, private and state-backed, who try to undermine the network by attacking the nodes that make it up. On top of that, some operators have to deal with seizures, raids, and direct physical access to hardware. There are [precedents](https://www.zdnet.com/article/austrian-man-raided-for-operating-tor-exit-node/) in [Austria](https://www.zdnet.com/article/austrian-man-raided-for-operating-tor-exit-node/), [Germany](https://forum.torproject.org/t/tor-relays-artikel-5-e-v-another-police-raid-in-germany-general-assembly-on-sep-21st-2024/14533), [the United States](https://www.npr.org/sections/alltechconsidered/2016/04/04/472992023/when-a-dark-web-volunteer-gets-raided-by-the-police), [Russia](https://torservers.net/blog/2017-04-14-freebogatov-relaymob/), and likely many others. In those instances, the server can become a liability.

Tor exists because we want to shield internet users from unwanted surveillance. The network is designed so that no single operator or server can reconstruct who is talking to whom. Journalists, activists, and whistleblowers depend on that holding up. A relay that can be seized and its contents handed over erodes the very trust the system depends on. And that's a problem we want to solve.

In this post we explore how a stateless, diskless operating system can improve relay security, from firmware to user space, with a focus on software integrity and physical attack resistance. This work comes from the experience of [Osservatorio Nessuno](https://osservatorionessuno.org/) running exit relays in Italy. Managing relays varies greatly depending on context, technical capability, budget, and jurisdiction. We hope to stimulate discussion rather than propose a single model.

## What stateless means

A stateless system doesn't store anything between reboots. Every time it starts, it begins from a known, fixed image, just like [Tails](https://tails.net/) does. The idea of running a Tor relay entirely in RAM isn't new. [Tor-ramdisk](https://archive.torproject.org/websites/lists.torproject.org/pipermail/tor-talk/2015-July/038493.html), a uClibc-based micro Linux distribution built for exactly this purpose, dates back to at least 2015.

For relay operators, this approach raises the security bar by enforcing better behaviors by design:

**Physical attack resistance.** If the machine is seized or cloned, there is nothing to analyze. Depending on the setup, the extraction of relay keys might become infeasible.

**Declarative configuration.** The system is version controlled. A stateless system cannot drift from its declared configuration, since every boot is a fresh apply.

**Immutable runtime.** The filesystem is read-only. Even if an attacker gains code execution, they cannot persist anything across a reboot.

**Reproducibility.** A system that doesn't change between reboots is easier to verify and, eventually, to reproduce and audit.

## Why Tor relays are hard to make stateless

Tor relays build reputation over time: a relay that has been running for months earns bandwidth flags that make it more useful to the network. That reputation is tied to a long-term cryptographic identity key. Lose those keys and the relay loses its identity, and as such is reputation in the network, starting from scratch.

Thus, the relay's identity must survive reboots without being extractable. A key stored on disk can be seized and copied; a key stored in a security chip such as the TPM might be more challenging for attackers.

Beyond the identity key, a relay accumulates a state file containing bandwidth history and other temporary information. Discarding it on every reboot degrades performance, and running entirely in RAM means the OS has to fit in memory, with no possibility of swapping to disk. Whenever processes exceed available memory, the kernel's OOM killer terminates them outright. In practice, replacing glibc's allocator with jemalloc or mimalloc [reduces Tor's memory footprint significantly](https://1aeo.com/blog/tor-memory-optizations-what-actually-works.html), from around 5.7 GB to under 1.2 GB on a busy guard relay, largely by avoiding fragmentation from high-churn directory cache objects.

## The TPM as the primary tool

A TPM (Trusted Platform Module) is a dedicated hardware chip on the motherboard that stores cryptographic keys and performs operations with them without ever exposing the private key to the operating system. It can *seal* a secret: bind it to a specific measured state of the machine, so the key can only be used if the TPM sees the exact same software stack it saw when the key was created.

For a stateless relay, this means the identity key survives reboots, as it lives in the hardware, but can't be conventionally extracted even with physical access. TPMs also support *remote attestation*: the chip can prove to an external system what software the machine was started with, backed by a hardware-rooted signature. This makes it possible to verify what a node is running without trusting the operator.

The TPM doesn't solve everything. Tor's usage of ed25519-based keys are not supported by the TPM chips, so the key is encrypted by the TPM but still stored as a byte string in non-volatile memory, meaning it is still technically possible to export it.

Sealing also requires deciding upfront what software state the TPM will trust. When you update the kernel or bootloader, the measured state changes, and you have to re-seal the TPM by predicting what the next boot will look like.

## Existing approaches

Different operators have tackled this problem at different points on the trade-off curve between simplicity and depth of security.

**Minimal ramdisk.** The simplest approach: run everything in RAM, manage keys manually. [Tor-ramdisk](https://archive.torproject.org/websites/lists.torproject.org/pipermail/tor-talk/2015-July/038493.html) has done this since 2015. Identity keys are exported and imported over SCP; rebooting without doing so means starting over. No TPM, no attestation, no verified boot â just the guarantee that RAM doesn't survive a power cut. It remains a meaningful improvement over a conventional disk-based setup.

**VM-based ramdisk.** [Emerald Onion](https://blog.emeraldonion.org/evolving-our-tor-relay-security-architecture) runs per-relay Alpine Linux images (66 MB each) on a Proxmox hypervisor. The VMs boot entirely into RAM with no persistent storage attached. Identity is managed with Tor's OfflineMasterKey feature: the long-term master key is generated offline and never touches the relay. Updates are image rebuilds, rollback is trivial, and no special hardware is required.

**Bare metal with TPM-backed identity.** [Patela](https://github.com/osservatorionessuno/patela), our tool, takes a more hardware-focused approach. The relay boots via [stboot](https://docs.system-transparency.org/st-1.3.0/docs/reference/stboot-system/), a bootloader that fetches and cryptographically verifies a signed OS image before handing off control. Once running, the node pulls its configuration from a central server over mTLS, though a potentially compromised server can deny service but cannot push credentials or extract keys from the node. The relay's identity key lives in TPM non-volatile memory, bound to the measured boot state. It survives reboots but can't be extracted even with physical access. The trade-off is operational complexity: bare metal is required and re-sealing is needed after updates.

## Open problems

Some of these prob...