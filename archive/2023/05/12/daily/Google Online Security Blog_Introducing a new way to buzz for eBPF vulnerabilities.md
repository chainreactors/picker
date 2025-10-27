---
title: Introducing a new way to buzz for eBPF vulnerabilities
url: http://security.googleblog.com/2023/05/introducing-new-way-to-buzz-for-ebpf.html
source: Google Online Security Blog
date: 2023-05-12
fetch_date: 2025-10-04T11:38:10.925364
---

# Introducing a new way to buzz for eBPF vulnerabilities

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Introducing a new way to buzz for eBPF vulnerabilities](https://security.googleblog.com/2023/05/introducing-new-way-to-buzz-for-ebpf.html "Introducing a new way to buzz for eBPF vulnerabilities")

May 11, 2023

Juan José López Jaimez, Security Researcher and Meador Inge, Security Engineer

Today, we are announcing [Buzzer](http://github.com/google/buzzer), a new eBPF Fuzzing framework that aims to help hardening the Linux Kernel.

## What is eBPF and how does it verify safety?

[eBPF](https://ebpf.io/) is a technology that allows developers and sysadmins to easily run programs in a privileged context, like an operating system kernel. Recently, its popularity has increased, with more products adopting it as, for example, a network filtering solution. At the same time, it has maintained its relevance in the security research community, since it provides a powerful attack surface into the operating system.

While there are many solutions for fuzzing vulnerabilities in the Linux Kernel, they are not necessarily tailored to the unique features of eBPF. In particular, eBPF has many complex security rules that programs must follow to be considered valid and safe. These rules are enforced by a component of eBPF referred to as the ["verifier"](https://docs.kernel.org/bpf/verifier.html). The correctness properties of the verifier implementation have proven difficult to understand by reading the source code alone.

That’s why our security team at Google decided to create a new fuzzer framework that aims to test the limits of the eBPF verifier through generating eBPF programs.

The eBPF verifier’s main goal is to make sure that a program satisfies a certain set of safety rules, for example: programs should not be able to write outside designated memory regions, certain arithmetic operations should be restricted on pointers, and so on. However, like all pieces of software, there can be holes in the logic of these checks. This could potentially cause unsafe behavior of an eBPF program and have security implications.

##

## Introducing Buzzer a new way to fuzz eBPF

Buzzer aims to detect these errors in the verifier’s validation logic by generating a high volume of eBPF programs – around 35k per minute. It then takes each generated program and runs it through the verifier. If the verifier thinks it is safe, then the program is executed in a running kernel to determine if it is actually safe. Errors in the runtime behavior are detected through instrumentation code added by Buzzer.

It is with this technique that Buzzer found its first issue, [CVE-2023-2163](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=71b547f561247897a0a14f3082730156c0533fed), an error in the branch pruning logic of the eBPF verifier that can cause unsafe paths to be overlooked, thus leading to arbitrary reading and writing of kernel memory. This issue demonstrates not only the complexity in the task that the verifier tries to accomplish (to make sure a program is safe in an efficient manner), but also how Buzzer can help researchers uncover complex bugs by automatically exploring corner cases in the verifier’s logic.

Additionally, Buzzer includes an easy to use eBPF generation library that makes it unique from other eBPF, or other general purpose Linux kernel fuzzers. By focusing on this particular technology, Buzzer is allowed to tailor its strategies to the eBPF features.

We are excited about the contributions Buzzer will make to the overall hardening of the Linux Kernel by making the eBPF implementation safer. Our team plans to develop some [new features](https://github.com/google/buzzer/milestones), such as the ability to run eBPF programs across distributed VMs.

Now that the code is open source, we are looking for contributors! If you have any interesting ideas for a feature we could implement in Buzzer, let us know in our [GitHub repository](http://github.com/google/buzzer).

We look forward to hearing your ideas and making eBPF safer together! Let the fuzzing begin.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/4935123458065087357)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/05/22k-awarded-to-sbft-23-fuzzing.html "Newer Post")

[**](https://security.googleblog.com/2023/05/io-2023-android-security-and-privacy.html.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/search/label/google%20play)
* [google play protect](https://security.googleblog.com/search/label/google%20play%20protect)
* [hacking](https://security.googleblog.com/search/label/hacking)
* [interoperability](https://security.googleblog.com/search/label/interoperability)
* [iot security](https://security.googleblog.com/search/label/iot%20security)
* [kubernetes](https://security.googleblog.com/search/label/kubernetes)
* [linux kernel](https://security.googleblog.com/search/label/linux%20kernel)
* [memory safety](https://security.googleblog.com/search/label/memory%20safety)
* [Open Source](https://security.googleblog.com/search/label/Open%20Source)
* [pha family highlights](https://security.googleblog.com/search/label/pha%20family%20highlights)
* [pixel](https://security.googleblog.com/search/label/pixel)
* [privacy](https://security.googleblog.com/search/label/privacy)
* [private compute core](https://security.googleblog.com/search/label/private%20compute%20core)
* [Rowhammer](https://security.googleblog.com/search/label/Rowhammer)
* [rust](https://security.googleblog.com/search/label/rust)
* [Security](https://security.googleblog.com/search/label/Security)
* [security rewards program](https://security.googleblog.com/search/label/security%20rewards%20program)
* [sigs...