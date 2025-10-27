---
title: Towards a More Open Secure Element Chip
url: https://www.bunniestudios.com/blog/?p=6606
source: bunnie's blog
date: 2022-12-20
fetch_date: 2025-10-04T01:57:14.420894
---

# Towards a More Open Secure Element Chip

---

[« Name that Ware November, 2022](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/)

[Winner, Name that Ware November 2022 »](https://www.bunniestudios.com/blog/2022/winner-name-that-ware-november-2022/)

## Towards a More Open Secure Element Chip

“[Secure Element](https://en.wikipedia.org/wiki/Secure_element)” (SE) chips have traditionally taken a very closed-source, NDA-heavy approach. Thus, it piqued my interest when an early-stage SE chip startup, Cramium (still in stealth mode), approached me to advise on open source strategy. This blog post explains my reasoning for agreeing to advise Cramium, and what I hope to accomplish in the future.

As an open source hardware activist, I have been very pleased at the progress made by the eFabless/Google partnership at creating an open-to-the-transistors physical design kit (PDK) for chips. This would be about as open as you can get from the design standpoint. However, the partnership currently supports only lower-complexity designs in the 90nm to 180nm technology nodes. Meanwhile, Cramium is planning to tape out their security chip in the 22nm node. A 22nm chip would be much more capable and cost-effective than one fabricated in 90nm (for reference, the RP2040 is fabricated in 40nm, while the Raspberry Pi 4’s CPU is fabricated in 28nm), but it would not be open-to-the-transistors.

Cramium indicated that they want to push the boundaries on what one can do with open source, within the four corners of the foundry NDAs. Ideally, a security chip would be fabricated in an open-PDK process, but I still feel it’s important to engage and help nudge them in the right direction because there is a genuine possibility that an open SDK (but still closed PDK) SE in a 22nm process could gain a lot of traction. If it’s not done right, it could establish poor de-facto standards, with lasting impacts on the open source ecosystem.

For example, when Cramium approached me, their original thought was to ship the chip with an ARM Cortex M7 CPU. Their reasoning is that developers prize a high-performance CPU, and the M7 is one of the best offerings in its class from that perspective. Who doesn’t love a processor with lots of MHz and a high IPC?

However, if Cramium’s chip were to gain traction and ship to millions of customers, it could effectively entrench the ARM instruction set — and more importantly — quirks such as the Memory Protection Unit (MPU) as the standard for open source SEs. We’ve seen the power of architectural lock-in as the x86 serially shredded the Alpha, Sparc, Itanium and MIPS architectures; so, I worry that every new market embracing ARM as a de-facto standard is also ground lost to fully open architectures such as RISC-V.

So, after some conversations, I accepted an advisory position at Cramium as the Ecosystem Engineer under the condition that they also include a RISC-V core on the chip. This is in addition to the Cortex M7. The good news is that a RISC-V core is royalty-free, and the silicon area necessary to add it at 22nm is basically a rounding error in cost, so it was a relatively easy sell. If I’m successful at integrating the RISC-V core, it will give software developers a choice between ARM and RISC-V.

So why is Cramium leaving the M7 core in? Quite frankly, it’s for risk mitigation. The project will cost upwards of $20 million to tape out. The ARM M7 core has been taped out and shipped in millions of products, and is supported by a billion-dollar company with deep silicon experience. The [VexRiscv](https://github.com/SpinalHDL/VexRiscv) core that we’re planning to integrate, on the other hand, comes with no warranty of fitness, and it is not as performant as the Cortex M7. It’s just my word and sweat of brow that will ensure it hopefully works well enough to be usable. Thus, I find it understandable that the people writing the checks want a “plan B” that involves a battle-tested core, even if proprietary.

This will understandably ruffle the feathers of the open source purists who will only certify hardware as “Free” if and only if it contains solely libre components. I also sympathize with their position; however, our choices are either the open source community somehow provides a CPU core with a warranty of fitness, effectively underwriting a $20 million bill if there is a fatal bug in the core, or I walk away from the project for “not being libre enough”, and allow ARM to take the possibly soon-to-be-huge open source SE market without challenge.

In my view it’s better to compromise and have a seat at the table now, than to walk away from negotiations and simply cede green fields to proprietary technologies, hoping to retake lost ground only after the community has achieved consensus around a robust full-stack open source SE solution. So, instead of investing time arguing over politics before any work is done, I’m choosing to invest time building validation test suites. Once I have a solid suite of tests in hand, I’ll have a much stronger position to argue for the removal of any proprietary CPU cores.

### On the Limit of Openness in a Proprietary Ecosystem

Advising on the CPU core is just one of many tasks ahead of me as their open source Ecosystem Engineer. Cramium’s background comes from the traditional chip world, where NDAs are the norm and open source is an exotic and potentially fatal novelty. Fatal, because most startups in this space exit through acquisition, and it’s much harder to negotiate a high acquisition price if prized IP is already available free-of-charge. Thus my goal is to not alienate their team with contumelious condescension about the obviousness and goodness of open source that is regrettably the cultural norm of our community. Instead, I am building bridges and reaching across the aisle, trying to understand their concerns, and explaining to them how and why open source can practically benefit a security chip.

To that end, trying to figure out where to draw the line for openness is a challenge. The crux of the situation is that the perceived fear/uncertainty/doubt (FUD) around a particular attack surface tends to have an inverse relation to the actual size of the attack surface. This illustrates the perceived FUD around a given layer of the security hierarchy:

[![](https://bunniefoo.com/bunnie/cramium_perceived_fud.png)](https://bunniefoo.com/bunnie/cramium_perceived_fud.png)

Generally, the amount of FUD around an attack surface grows with how poorly understood the attack surface is: naturally we fear things we don’t understand well; likewise we have less fear of the familiar. Thus, “user error” doesn’t sound particularly scary, but “direct readout” with a focused ion beam of hardware security keys sounds downright leet and scary, the stuff of state actors and APTs, and also of factoids spouted over beers with peers to sound smart.

However, the actual size of the attack surface is quite the opposite:

[![](https://bunniefoo.com/bunnie/cramium_attack_surface.png)](https://bunniefoo.com/bunnie/cramium_attack_surface.png)

In practice, “user error” – weak passwords, spearphishing, typosquatting, or straight-up fat fingering a poorly designed UX – is common and often remotely exploitable. Protocol errors – downgrade attacks, failures to check signatures, TOCTOUs – are likewise fairly common and remotely exploitable. Next in the order are just straight-up software bugs – buffer overruns, use after frees, and other logic bugs. Due to the sheer volume of code (and more significantly the rate of code turnover) involved in most security protocols, there are a lot of bugs, and a constant stream of newly minted bugs with each update.

Beneath this are the hardware bugs. These are logical errors in the implementation of a function of a piece of hardware, such as memory aliasing, open test access ports, and oversights such as partially mutable cryptographic material (such as an AES key that can’t be read out, but can be updated one byte at a time...