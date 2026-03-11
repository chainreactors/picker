---
title: Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications
url: https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/
source: bunnie's blog
date: 2026-03-10
fetch_date: 2026-03-11T04:03:01.014134
---

# Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications

---

[« Name that Ware, February 2026](https://www.bunniestudios.com/blog/2026/name-that-ware-february-2026/)

## Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications

One of my latest projects is the Baochip-1x, a mostly-open, full-custom silicon chip fabricated in TSMC 22nm, targeted at high assurance applications. It’s a security chip, but far more open than any other security chip; it’s also a general purpose microcontroller that fills a gap in between the Raspberry Pi RP2350 (found on the Pi Pico2) and the NXP iMXRT1062 (found on the Teensy 4.1).

![](https://bunniefoo.com/baochip/dabao-thechip-narrow.jpg)

It’s the latest step in the [Betrusted](https://betrusted.io) initiative, spurred by [work I did with Ed Snowden](https://www.tjoe.org/pub/direct-radio-introspection/release/2) 8 years ago trying to answer the question of “can we trust hardware to not betray us?” in the context of mass surveillance by state-level adversaries. The Baochip-1x’s CPU core is descended directly from the FPGA SoC used inside [Precursor](https://precursor.dev), a device I made to keep secrets; designed explicitly to run [Xous](https://betrusted.io/xous-book/), a pure-Rust rethink of the embedded OS I helped write; and made deliberately compatible with [IRIS inspection](https://bunnie.org/iris/), a method I pioneered for non-destructively inspecting silicon for correct construction.

In a nutshell, the Baochip-1x is a SoC featuring a 350MHz Vexriscv CPU + MMU, combined with a I/O processor (“BIO”) featuring quad 700MHz PicoRV32s, 4MiB of nonvolatile memory (in the form of RRAM), and 2MiB of SRAM. Also packed into the chip are features typically found exclusively in secure elements, such as a TRNG, a variety of cryptographic accelerators, secure mesh, glitch sensors, ECC-protected RAM, hardware protected key slots and one-way counters.

![](https://bunniefoo.com/baochip/block-diagram.png)

The chip is fabricated using a fully-production qualified TSMC process using a dedicated mask set. In other words, this isn’t a limited-run MPW curiosity: Baochip’s supply chain is capable of pumping out millions of chips should such demand appear.

**Hardware Built to Run High-Assurance Software**

The Baochip-1x’s key differentiating feature is the inclusion of a Memory Management Unit (MMU). No other microcontroller in this performance/integration class has this feature, to the best of my knowledge. For those not versed in OS-nerd speak, the MMU is what sets the software that runs on your phone or desktop apart from the software that runs in your toaster oven. It facilitates secure, loadable apps by sticking every application in its own virtual memory space.

The MMU is a venerable piece of technology, dating back to the 1960’s. Its page-based memory protection scheme is well-understood and has passed the test of time; I’ve taught its principles to hundreds of undergraduates, and it continues to be a cornerstone of modern OSes.

![](https://bunniefoo.com/baochip/baochip1-atlas-vm.png)

*Above: Diagram illustrating an early virtual memory scheme from Kilburn, et al, “One-level storage system”, IRE Transactions, EC-11(2):223-235, **1962***

When it comes to evaluating security-oriented features, older is not always worse; in fact, withstanding the test of time is a positive signal. For example, the AES cipher is about 26 years old. This seems ancient for computer technology, yet many cryptographers recommend it over newer ciphers explicitly because AES has withstood the test of hundreds of cryptographers trying to break it, with representation from every nation state, over years and years.

I’m aware of newer memory protection technologies, such as [CHERI](https://en.wikipedia.org/wiki/Capability_Hardware_Enhanced_RISC_Instructions), PMPs, MPUs… and as a nerd, I love thinking about these sorts of things. In fact, [in my dissertation](https://bunniestudios.com/bunnie/phdthesis.pdf), I even advocated for the use of CHERI-style hardware capabilities and tagged pointers in new CPU architectures.

However, as a pragmatic system architect, I see no reason to eschew the MMU in favor of any of these. In fact, the MMU is composable with all of these primitives – it’s valid to have both a PMP and an MMU in the same RISC-V CPU. And, even if you’re using a CHERI-like technology for hardware-enforced bounds checking on pointers, it still doesn’t allow for transparent address space relocation. Without page-based virtual memory, each program would need to be linked to a distinct, non-overlapping region of physical address space at compile time, and you couldn’t have swap memory.

This begs the question: if the MMU is such an obvious addition, why isn’t it more prevalent? If it’s such an obvious choice, wouldn’t more players include it in their chips?

“Small” CPUs such as those found in embedded SoCs have lacked this feature since their inception. I trace this convention back to the introduction of the ARM7TDMI core in the 1990s. Back then, transistors were scarce, memory even more so, and so virtual memory was not a great product/market fit for devices with just a couple kilobytes of RAM, not even enough to hold a page table. The ARM7TDMI core’s efficiency and low cost made it a run-away success, shipping over a billion units and establishing ARM as the dominant player in the embedded SoC space.

Fast forward 30 years, and Moore’s Law has given us tens of thousands of times more capability; today, a fleck of silicon smaller than your pinky nail contains more transistors than a full-sized PC desktop from the 1990’s. Despite the progress, these small flecks of silicon continue to adhere to the pattern that was established in the 1990’s: small systems get flat memory spaces with no address isolation.

![](https://bunniefoo.com/baochip/baochip1-silicon-area.jpg)

*Above: Die shot of a modern 22nm system-on-chip (SoC). This fleck of silicon is about 4mm on a side and contains more transistors than a desktop PC from the 1990’s. Note how the logic region is more empty space than active gates by silicon area.*

The root cause turns out explicitly to be because MMUs are so valuable: without one, you can’t run Linux, BSD, or Mach. Thus, when ARM split their IP portfolio into the A, R, and M-series cores, the low-cost M-series cores were forbidden from having an MMU to prevent price erosion of their high-end A-series cores. Instead, a proprietary hack known as the “MPU” was introduced that gives some memory security, but without an easy path to benefits such as swap memory and address space relocation.

We’ve been locked into this convention for so long that we simply forgot to challenge the assumptions.

Thanks to the rise of open architecture specifications such as RISC-V, and fully-open implementations of the RISC-V spec such as the Vexriscv, I’m not bound by anyone’s rules for what can or can’t go onto an SoC. And so, I am liberated to make the choice to include an MMU in the Baochip-1x.

This naturally empowers enthusiasts to try and run Linux on the Baochip-1x, but we (largely Sean ‘xobs’ Cross and me) already wrote a pure-Rust OS called [“Xous”](https://betrusted.io/xous-book/) which incorporates an MMU but in a framework that is explicitly targeted towards small memory footprint devices like the Baochip-1x. The details of Xous are beyond the scope of this post, but if you’re interested, check out [the talk we gave at 39C3](https://media.ccc.de/v/39c3-xous-a-pure-rust-rethink-of-the-embedded-operating-system).

**“Now” Is Always the Right Time to Choose More Open Frameworks**

This couples into the core argument as to why a “mostly open RTL” SoC is the right thing for this moment in time. As a staunch advocate for open-source technologies, I would love to see a fully-open silicon stack, from the fabs-up. I’m heartened to see multiple initiatives working on fixing this problem, but it’s a hard problem. I estimate it could take more than a decade before we have a sufficiently robust o...