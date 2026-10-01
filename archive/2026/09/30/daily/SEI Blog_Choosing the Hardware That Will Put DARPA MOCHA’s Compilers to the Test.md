---
title: Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test
url: https://www.sei.cmu.edu/blog/choosing-the-hardware-that-will-put-darpa-mochas-compilers-to-the-test/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-09-30
fetch_date: 2026-10-01T07:59:32.412875
---

# Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test

[Skip to main content](#main-content)

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Wohlbier, J., 2026: Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test. Software Engineering Institute blog, Accessed September 30, 2026, https://doi.org/10.58012/vj42-a808.

Copy

APA Citation

Wohlbier, J. (2026, September 30). Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test. Retrieved September 30, 2026, from https://doi.org/10.58012/vj42-a808.

Copy

Chicago Citation

Wohlbier, John. "Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, September 30, 2026. https://doi.org/10.58012/vj42-a808.

Copy

IEEE Citation

J. Wohlbier, "Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 30-Sep-2026 [Online]. Available: https://doi.org/10.58012/vj42-a808. [Accessed: 30-Sep-2026].

Copy

BibTeX Code

```
@misc{wohlbier_2026,
author={Wohlbier, John},
title={Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test},
month={Sep},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/vj42-a808},
url={https://doi.org/10.58012/vj42-a808},
note={Accessed: 2026-Sep-30}
}
```

Copy

# Choosing the Hardware That Will Put DARPA MOCHA’s Compilers to the Test

![](/media/images/Wohlbier_John_026_230111.max-180x180.format-webp.webp)

###### [John Wohlbier](/authors/john-wohlbier)

###### September 30, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/vj42-a808>

Get Citation

##### SHARE

Modern computers are no longer built around single processors. A capable system today is a heterogeneous ensemble: CPUs, GPUs, and an expanding zoo of specialized accelerators for machine learning, signal processing, and networking. Getting good performance out of that ensemble is hard, and getting it *quickly* on hardware the compiler has never seen before is harder still. DARPA [MOCHA](https://www.darpa.mil/research/programs/mocha-machine-learning)—DARPA’s Machine Learning and Optimization-guided Compilers for Heterogeneous Architectures program—exists to close that gap. The Advanced Computing Lab in the SEI’s AI Division has spent the last several months considering a question that will shape the next two years of the effort: which hardware should the program’s compilers be tested against?

This post walks through how we are approaching that question. We describe what MOCHA is trying to do, the role the SEI plays, how we selected candidate hardware, the list of that hardware and how we pressure-tested each candidate, and where the final choices landed.

## Automating Computer Optimization

MOCHA is a program in DARPA’s Information Processing Techniques Office, managed by [Dr. Howard Shrobe](https://www.darpa.mil/about/people/howard-shrobe). A well-known frustration drives its work: traditional compilers were not designed to generate efficient machine code for heterogeneous mixes of CPUs, GPUs, and application accelerators. To exploit a new accelerator, developers typically hand-write specialized code and rely on vendor-tuned libraries. Although that approach works, it is slow and expensive, and it quietly encourages vendor lock-in: once an application is written against a proprietary library, moving it to different hardware means rewriting it.

Extending a compiler to support a genuinely new computational element is a manual job that can only be done by compiler experts. It is time-consuming and error-prone, and it does not scale to the pace at which novel silicon is appearing. MOCHA’s hypothesis is that data-driven methods, machine learning, and advanced optimization can accelerate that process, allowing compilers to be adapted to new hardware rapidly and with minimal human intervention. A key insight is that performance models of the target hardware drive every step of compilation, and that building those models by hand is the central bottleneck. If those models can instead be generated by measuring generated code on real hardware and by mining architectural documentation, the cost of supporting a new device drops dramatically.

A guiding principle for DARPA MOCHA is *ALARA*—keeping human involvement As Low As Reasonably Achievable. ALARA captures MOCHA’s emphasis on both rapidly enabling compilation for novel hardware and enabling compilation across heterogeneous hardware. Speed on one new chip is not sufficient; the program cares about how little human effort it takes to span a diverse collection of computational elements at once.

## The SEI’s Role

The SEI’s [Advanced Computing Lab](https://www.sei.cmu.edu/projects/the-advanced-computing-lab/), part of the AI Division, supports the government team, comprised of the DARPA program manager and several systems engineering and technical assistants (SETAs), with a focus on test and evaluation. In practice, that means we gather and assess the options and provide the program manager with the information he needs to decide which computational elements enter the program. We then stand up and maintain the evaluation machine where those elements are integrated, and we build the measurement methodology for MOCHA to compare performer results fairly. Performer teams develop the compiler technology; our job is to give them a well-characterized, representative, and appropriately challenging set of targets to aim at, and to maximize validity of the evaluation itself.

DARPA plans for MOCHA to include six distinct computing types by the end of the effort. A computing type is defined not just by a hardware architecture but by a distinct instruction set and programming model. Under that definition, a data-center GPU, a device that fuses a field-programmable gate array (FPGA) fabric with a spatial AI-engine array, a long-vector processor, and a RISC-V-plus-dataflow AI accelerator are four different types, even though a casual observer might lump the last three together as “accelerators.” The point of the program is to demonstrate rapid, low-effort retargeting across architectural and [instruction set architecture (ISA)](https://en.wikipedia.org/wiki/Instruction_set_architecture) boundaries, so architectural diversity in the target set is essential.

There is also a concrete constraint: any hardware chosen must physically fit inside the evaluation machine. That machine is a workstation-class tower built around an Intel Core Ultra 9 285K, which brings its own compute types: AVX2 SIMD on the CPU, an integrated Xe GPU, and a neural processing unit plus PCIe 5.0 connectivity and an NVIDIA RTX 4500 Ada card already installed as a baseline reference. Candidate accelerators therefore need to be available as PCIe cards that fit the chassis, power envelope, and cooling of a single tower.

## Five Factors for Selecting a Candidate Accelerator

Five factors shaped our candidate list: *availability*, *maturity*, *affordability*, *programmability*, and *the ability to host the device in the evaluation machine*. Availability and hosting knocked out otherwise fascinating options, including wafer-scale engines and reconfigurable-dataflow systems that only ship as complete servers and cloud-only accelerators you cannot buy and install. Affordability kept us honest about parts that cost more than the res...