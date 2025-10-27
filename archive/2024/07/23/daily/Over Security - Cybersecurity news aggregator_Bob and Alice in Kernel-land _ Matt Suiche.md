---
title: Bob and Alice in Kernel-land | Matt Suiche
url: https://www.msuiche.com/posts/bob-and-alice-in-kernel-land/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:45:44.752298
---

# Bob and Alice in Kernel-land | Matt Suiche

[âHome](/)
[Blog](/posts)
[About](/about)
[Press](/press)
[Media](/media)
[Subscribe](https://www.msuiche.com/index.xml)

# Bob and Alice in Kernel-land

Jul 20, 2024

Â·

1029 words

Â·

5 minute read

![Blue Screens Everywhere](./images/main.webp)

Already dubbed “[The Largest IT](https://www.telegraph.co.uk/business/2024/07/19/world-is-horrifying-close-to-total-economic-collapse/), [Outage In History](https://www.wired.com/story/crowdstrike-outage-update-windows/), the CrowdStrike update from July 18, 2024, has affected at least [8.5 million Windows devices, according to Microsoft](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). Several of these devices are critical assets and run multiple essential services. For instance, I was unable to pay for my coffee in Dubai because the payment systems used by the coffee shop were down, and a friend lost her passport while stranded in Barcelona due to flight disruptions. The full impact and scope of the incident remain unknown, and it is likely be the main topic of discussion at DEFCON and BlackHat this summer and beyond.

Around 2010, many founders, whether in security or not, faced a critical question: “Kernel-mode or User-mode? Which should our agent be?” During this time, agent fatigue started becoming a real issue, with many customers reluctant to install additional agents on their machines. Moreover, the idea of adding agents that might require a kernel driver was met with significant skepticism.

Kernel mode obviously provides greater flexibility, information, and control. For example, when we developed our Windows-based application container solution, [CloudVolumes](https://blogs.vmware.com/euc/2014/08/cloudvolumes.html), kernel access was essential. It allowed us to utilize mini-filters to access file system and registry operations, unlike other solutions such as [ThinApp](https://docs.vmware.com/en/VMware-ThinApp/index.html), which had a more restrictive design.

Security products were also seen as prime targets for vulnerability research due to their ideal characteristics:

* Privileged access (Kernel or Administrator).
* Complex parsers, increasing the attack surface.
* Limited QA performed on them.

During a certain period, [Tavis Ormandy](https://x.com/taviso) conducted audits on multiple security products, successfully [uncovering](https://www.forbes.com/sites/thomasbrewster/2015/09/23/google-ormandy-finds-kaspersky-0days/) [numerous vulnerabilities](https://googleprojectzero.blogspot.com/2016/06/how-to-compromise-enterprise-endpoint.html). The more complex the code placed in kernel mode, the greater the risk, a persistent issue with kernel drivers on any operating system.

A prime example is `win32k`, the Windows GUI Subsystem and Windows Manager. A simple Google search for [“win32k”](https://www.google.com/search?q=win32k) will reveal why it has been a concern since [Alex Ionescu](https://www.alex-ionescu.com/black-hat-2008-wrap-up/) first covered it in 2008. The saying “Too big to fail” certainly does not apply to kernel drivers; in fact, the opposite is definitely in effect.

> This was a key decision we made at the very beginning of Capsule8: we would not be a kernel module and only use kprobes/uprobes as provided by the Linux kernel so that we could never panic the kernel. Choosing safety from the beginning made us have to work harder, but was right. <https://t.co/HSg4aziqfA>
>
> — Dino A. Dai Zovi (@dinodaizovi) [July 20, 2024](https://twitter.com/dinodaizovi/status/1814510114269008197?ref_src=twsrc%5Etfw)

Some solutions, such as Capsule8, intentionally avoided using kernel modules from the beginning. Instead, they relied exclusively on [kprobes/uprobes](https://x.com/dinodaizovi/status/1814510114269008197) before eventually incorporating eBPF support. eBPF has since gained prominence for powering the [Solana Virtual Machine](https://github.com/solana-labs/rbpf). However, eBPF is still in an [early stage on Windows](https://github.com/microsoft/ebpf-for-windows) and currently cannot provide as much telemetry as a kernel driver, making it an insufficient solution for now.

> My presentation slides for "Windows 11: security by-default" from [@BlueHatIL](https://twitter.com/BlueHatIL?ref_src=twsrc%5Etfw) covering:
>
> Rust in win32k, Adminless Windows, Token Binding, Sandboxing win32, and more!
>
>  posted here: <https://t.co/mfOcOh8f84> [pic.twitter.com/WDAbbIjaEv](https://t.co/WDAbbIjaEv)
>
> — David Weston (DWIZZZLE) (@dwizzzleMSFT) [April 18, 2023](https://twitter.com/dwizzzleMSFT/status/1648396427192840192?ref_src=twsrc%5Etfw)

The issue with kernel modules and drivers is that they can be [used](https://en.wikipedia.org/wiki/Sony_BMG_copy_protection_rootkit_scandal) and [abused](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/microsoft-recommended-driver-block-rules) on any modern operating system. As long as arbitrary code can run on a machine, defense in depth is necessary, requiring higher standards for development. This is why efforts to port core drivers like win32k to Rust have begun. We can expect Microsoft, and likely [Linux](https://www.reddit.com/r/rust/comments/16x21gw/linux_kernel_driver_development_in_rust_examples/), to [speed up their initiatives](https://www.theregister.com/2023/04/27/microsoft_windows_rust/) for the [Rust driver development platform](https://techcommunity.microsoft.com/t5/surface-it-pro-blog/open-source-rust-driver-development-platform/ba-p/3974222) with projects like `windows-drivers-rs`.

Apple decided to promote [`System Extensions`](https://support.apple.com/en-ae/guide/deployment/depa5fb8376f/web) that operate in user space, gradually phasing out `Kernel Extensions (kext)`. They also provided [a limited API](https://developer.apple.com/documentation/endpointsecurity) for third-party Endpoint Security solutions is only “good enough” when your operating system isn’t a priority for attackers. Microsoft undertook a similar initiative with its [`User Mode Driver Framework`](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2), though it is primarily used for Plug and Play (PnP) and power management functionalities and not monitoring/telemetry purposes.

![2008 Picture of Microsoft Research Singularity OS Team](./images/singularity-singularityteam2008.jpg)

The most straightforward way to prevent third-party drivers from causing system faults is to move them out of kernel space and prohibit third-party code execution in kernel mode. Unfortunately, this is at the moment unrealistic and would require a different OS design. This concept has been discussed for a long time, with various initiatives like Microsoft’s C# [Singularity OS](https://www.microsoft.com/en-us/research/project/singularity/) from Microsoft Research.

In the case of security solutions, you would naturally move complex code such as regexes and parsers out of kernel land but this would come at a performance cost and prevent “real time attack detections”. One bug does not reflect the quality of software produced by a company, but one bug can really destroy the purpose of a product.

Initiatives like `windows-drivers-rs` will undoubtedly enhance the stability and safety of kernel modules. However, we are still in the early stages of writing kernel drivers in Rust. Additionally, the incentives for third-party companies to adopt Rust for driver development are limited compared to the efforts required which also would most likely also endup with a lot of `unsafe {}` code anyway.
Convincing a large number of companies would also be necessary. For an idea of how many companies are potentially involved, you can refer to the [list of allocated filter altitudes](https://learn.microsoft.com/en-us/windows-hardware/drivers/ifs/allocated-altitudes).

Having user-mode only security solutions sound nice but it woul...