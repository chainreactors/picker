---
title: Exploring GrapheneOS secure allocator Hardened Malloc
url: https://synacktiv.com/en/publications/exploring-grapheneos-secure-allocator-hardened-malloc
source: Instapaper: Unread
date: 2025-09-25
fetch_date: 2025-10-02T20:40:19.005538
---

# Exploring GrapheneOS secure allocator Hardened Malloc

[Skip to main content](exploring-grapheneos-secure-allocator-hardened-malloc#main-content)

[Search](../../search)

Switch Language

EnglishToggle Dropdown

* English
* [French](../../publications/exploring-grapheneos-secure-allocator-hardened-malloc)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

[![Home](/sites/default/files/logo_synacktiv_blanc.webp)](../../en "Home")

* [Our offer](../our-offer)
  + [Penetration Test / Red Team](../features/penetration-test-red-team)
  + [Incident response](../features/incident-response)
  + [Reverse-engineering](../features/reverse-engineering)
  + [Development](../our-team/development)
  + [Products](../products/kraqozorus)
  + [CSIRT](../csirt)
* [Trainings](../offers/trainings)
* [Join us](../join-us)
* [Publications](../our-publications)
  + [Posts](../publications)
  + [Advisories](../advisories)
  + [Resources](../ressources)
* [The company](../the-company)
* [Contact](../contact)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

# Exploring GrapheneOS secure allocator: Hardened Malloc

Written by
Nicolas Stefanski
- 22/09/2025 - in
Exploit
, SystÃ¨me
, Reverse-engineering

- [Download](exploring-grapheneos-secure-allocator-hardened-malloc)

GrapheneOS is a mobile operating system based on Android and focusing on privacy and security. To enhance further the security of their product, GrapheneOS developers introduced a new libc allocator : **hardened malloc.** This allocator has a security-focused design in mind to protect processes against common memory corruption vulnerabilities. This article will explain in details its internal architecture and how security mitigation are implemented from a security researcher point of view.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings).

## Introduction

GrapheneOS is a security and privacy-focused mobile operating system based on a modified version of Android (AOSP). To enhance its protection, it integrates advanced security features, including its own memory allocator for libc: **hardened malloc**. Designed to be as robust as the operating system itself, this allocator specifically seeks to protect against memory corruption.

This technical article details the internal workings of hardened malloc and the protection mechanisms it implements to prevent common memory corruption vulnerabilities. It is intended for a technical audience, particularly security researchers or exploit developers, who wish to gain an in-depth understanding of this allocator's internals.

The analyses and tests in this article were performed on two devices running GrapheneOS:

* **Pixel 4a 5G**: `google/bramble/bramble:14/UP1A.231105.001.B2/2025021000:user/release-keys`
* **Pixel 9a**: `google/tegu/tegu:16/BP2A.250705.008/2025071900:user/release-keys`

The devices were rooted with Magisk 29 in order to use Frida to observe the internal state of **hardened malloc** within system processes. The study was based on the source code from the official [GrapheneOS GitHub repository](https://github.com/GrapheneOS/hardened_malloc) (commit `7481c8857faf5c6ed8666548d9e92837693de91b`).

## GrapheneOS

**GrapheneOS** is a hardened operating system based on Android. As an actively maintained open-source project, it benefits from frequent updates and the swift application of security patches. All information is available on [GrapheneOS website](https://grapheneos.org/).

To effectively protect the processes running on the device, GrapheneOS implements several security mechanisms. The following sections briefly describe the specific mechanisms that contribute to the hardening of its memory allocator.

### Extended Address Space

On standard Android systems, the address space for userland processes is limited to 39 bits, ranging from `0` to `0x8000000000`. On GrapheneOS, this space is extended to 48 bits, and to take advantage of this extension, ASLR entropy has also been increased from 24 to 33 bits. This detail is important as **hardened malloc** relies heavily on `mmap` for its internal structures and its allocations.

```
tegu:/ # cat /proc/self/maps
c727739a2000-c727739a9000 rw-p 00000000 00:00 0                          [anon:.bss]
c727739a9000-c727739ad000 r--p 00000000 00:00 0                          [anon:.bss]
c727739ad000-c727739b1000 rw-p 00000000 00:00 0                          [anon:.bss]
c727739b1000-c727739b5000 r--p 00000000 00:00 0                          [anon:.bss]
c727739b5000-c727739c1000 rw-p 00000000 00:00 0                          [anon:.bss]
e5af7fa30000-e5af7fa52000 rw-p 00000000 00:00 0                          [stack]
tegu:/ # cat /proc/self/maps
d112736be000-d112736c5000 rw-p 00000000 00:00 0                          [anon:.bss]
d112736c5000-d112736c9000 r--p 00000000 00:00 0                          [anon:.bss]
d112736c9000-d112736cd000 rw-p 00000000 00:00 0                          [anon:.bss]
d112736cd000-d112736d1000 r--p 00000000 00:00 0                          [anon:.bss]
d112736d1000-d112736dd000 rw-p 00000000 00:00 0                          [anon:.bss]
ea0de59be000-ea0de59e1000 rw-p 00000000 00:00 0                          [stack]
tegu:/ # cat /proc/self/maps
d71f87043000-d71f8704a000 rw-p 00000000 00:00 0                          [anon:.bss]
d71f8704a000-d71f8704e000 r--p 00000000 00:00 0                          [anon:.bss]
d71f8704e000-d71f87052000 rw-p 00000000 00:00 0                          [anon:.bss]
d71f87052000-d71f87056000 r--p 00000000 00:00 0                          [anon:.bss]
d71f87056000-d71f87062000 rw-p 00000000 00:00 0                          [anon:.bss]
f69f7c952000-f69f7c974000 rw-p 00000000 00:00 0                          [stack]
```

### Secure app spawning

On standard Android, each application is launched via a `fork` of the *zygote* process. This mechanism, designed to speed up startup, has a major security consequence: all applications inherit the same address space as *zygote*. In practice, this means that pre-loaded libraries end up at identical addresses from one application to another. For an attacker, this predictability makes it easy to bypass ASLR protection without needing a prior information leak.

To overcome this limitation, GrapheneOS fundamentally changes this process. Instead of just a `fork`, new applications are launched with `exec`. This method creates an entirely new and randomized address space for each process, thereby restoring the full effectiveness of ASLR. It is no longer possible to predict the location of remote memory regions. This enhanced security does, however, come at a cost: a slight impact on launch performance and an increased memory footprint for each application.

```
tegu:/ # cat /proc/$(pidof zygote64)/maps | grep libc\.so
d6160aac0000-d6160ab19000 r--p 00000000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d6160ab1c000-d6160abbe000 r-xp 0005c000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d6160abc0000-d6160abc5000 r--p 00100000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d6160abc8000-d6160abc9000 rw-p 00108000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
tegu:/ # cat /proc/$(pidof com.android.messaging)/maps | grep libc\.so
d5e4a9c68000-d5e4a9cc1000 r--p 00000000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d5e4a9cc4000-d5e4a9d66000 r-xp 0005c000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d5e4a9d68000-d5e4a9d6d000 r--p 00100000 07:f0 24                         /apex/com.android.runtime/lib64/bionic/libc.so
d5e4a9d70000-d5e4a9d71000 rw-p 00108000 07:f0 24                         /apex/com....