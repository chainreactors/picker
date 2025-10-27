---
title: Supporting Rowhammer research to protect the DRAM ecosystem
url: http://security.googleblog.com/2025/09/supporting-rowhammer-research-to.html
source: Google Online Security Blog
date: 2025-09-16
fetch_date: 2025-10-02T20:11:04.479602
---

# Supporting Rowhammer research to protect the DRAM ecosystem

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Supporting Rowhammer research to protect the DRAM ecosystem](https://security.googleblog.com/2025/09/supporting-rowhammer-research-to.html "Supporting Rowhammer research to protect the DRAM ecosystem ")

September 15, 2025

Posted by Daniel Moghimi

Rowhammer is a complex class of vulnerabilities across the industry. It is a hardware vulnerability in DRAM where repeatedly accessing a row of memory can cause bit flips in adjacent rows, leading to data corruption. This can be exploited by attackers to gain unauthorized access to data, escalate privileges, or cause denial of service. Hardware vendors have deployed various mitigations, such as [ECC](https://www.jedec.org/category/keywords/ecc) and Target Row Refresh (TRR) for DDR5 memory, to mitigate Rowhammer and enhance DRAM reliability. However, the resilience of those mitigations against sophisticated attackers remains an open question.

To address this gap and help the ecosystem with deploying robust defenses, Google has supported academic research and developed test platforms to analyze DDR5 memory. Our effort has led to the discovery of new attacks and a deeper understanding of Rowhammer on the current DRAM modules, helping to forge the way for further, stronger mitigations.

## What is Rowhammer?

[Rowhammer](https://dl.acm.org/doi/abs/10.1145/2678373.2665726) exploits a vulnerability in DRAM. DRAM cells store data as electrical charges, but these electric charges leak over time, causing data corruption. To prevent data loss, the memory controller periodically refreshes the cells. However, if a cell discharges before the refresh cycle, its stored bit may corrupt. Initially considered a reliability issue, it has been leveraged by security researchers to demonstrate privilege escalation attacks. By repeatedly accessing a memory row, an attacker can cause bit flips in neighboring rows. An adversary can exploit Rowhammer via:

1. Reliably cause bit flips by repeatedly accessing adjacent DRAM rows.
2. Coerce other applications or the OS into using these vulnerable memory pages.
3. Target security-sensitive code or data to achieve privilege escalation.
4. Or simply corrupt system’s memory to cause denial of service.

Previous work has repeatedly demonstrated the possibility of such attacks from software [[Revisiting rowhammer](https://ieeexplore.ieee.org/abstract/document/9138944/), [Are we susceptible to rowhammer?](https://ieeexplore.ieee.org/abstract/document/9152654/), [Drammer](https://dl.acm.org/doi/abs/10.1145/2976749.2978406),  [Flip feng shui](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/razavi), [Jolt](https://eprint.iacr.org/2022/1669)]. As a result, defending against Rowhammer is required for secure isolation in multi-tenant environments like the cloud.

## Rowhammer Mitigations

The primary approach to mitigate Rowhammer is to detect which memory rows are being aggressively accessed and refreshing nearby rows before a bit flip occurs. TRR is a common example, which uses a number of counters to track accesses to a small number of rows adjacent to a potential victim row. If the access count for these aggressor rows reaches a certain threshold, the system issues a refresh to the victim row. TRR can be incorporated within the DRAM or in the host CPU.

However, this mitigation is not foolproof. For example, the [TRRespass](https://ieeexplore.ieee.org/abstract/document/9152631) attack showed that by simultaneously hammering multiple, non-adjacent rows, TRR can be bypassed. Over the past couple of years, more sophisticated attacks [[Half-Double](https://www.usenix.org/conference/usenixsecurity22/presentation/kogler-half-double), [Blacksmith](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/525008/4/2021275594.pdf)] have emerged, introducing more efficient attack patterns.

In response, one of our efforts was to collaborate with [JEDEC](https://www.jedec.org/), external researchers, and experts to define the [PRAC](https://www.jedec.org/news/pressreleases/jedec-updates-jesd79-5c-ddr5-sdram-standard-elevating-performance-and-security) as a new mitigation that deterministically detects Rowhammer by tracking all memory rows.

However, current systems equipped with DDR5 lack support for PRAC or other robust mitigations. As a result, they rely on probabilistic approaches such as ECC and enhanced TRR to reduce the risk. While these measures have mitigated older attacks, their overall effectiveness against new techniques was not fully understood until our recent [findings](https://comsec.ethz.ch/phoenix).

## Challenges with Rowhammer Assessment

Mitigating Rowhammer attacks involves making it difficult for an attacker to reliably cause bit flips from software. Therefore, for an effective mitigation, we have to understand how a determined adversary introduces memory accesses that bypass existing mitigations. Three key information components can help with such an analysis:

1. How the improved TRR and in-DRAM ECC work.
2. How memory access patterns from software translate into low-level DDR commands.
3. (Optionally) How any mitigations (e.g., ECC or TRR) in the host processor work.

The first step is particularly challenging and involves reverse-engineering the proprietary in-DRAM TRR mechanism, which varies significantly between different manufacturers and device models. This process requires the ability to issue precise DDR commands to DRAM and analyze its responses, which is difficult on an off-the-shelf system. Therefore, specialized test platforms are essential.

The second and third steps involve analyzing the DDR traffic between the host processor and the DRAM. This can be done using an off-the-shelf interposer, a tool that sits between the processor and DRAM. A crucial part of this analysis is understanding how a live system translates software-level memory accesses into the DDR protocol.

The third step, which involves analyzing host-side mitigations, is sometimes optional. For example, host-side ECC (Error Correcting Code) is enabled by default on servers, while host-side TRR has only been implemented in some CPUs.

## Rowhammer testing platforms

For the first challenge, we partnered with Antmicro to develop two specialized, open-source FPGA-based Rowhammer test platforms. These platforms allow us to conduct in-depth testing on different types of DDR5 modules.

* [DDR5 RDIMM Platform:](https://antmicro.com/blog/2022/08/extending-the-open-source-rowhammer-testing-framework-to-ddr5/) A new DDR5 Tester board to meet the hardware requirements of Registered DIMM (RDIMM) memory, common in server computers.
* [SO-DIMM Platform:](https://antmicro.com/blog/2024/02/versatile-so-dimm-lpddr5-rowhammer-testing-platform/) A version that supports the standard SO-DIMM pinout compatible with off-the-shelf DDR5 SO-DIMM memory sticks, common in workstations and end-user devices.

Antmicro designed and manufactured these [open-source platforms](https://github.com/antmicro/rowhammer-tester) and we worked closely with them, and researchers from ETH Zurich, to test the applicability of these platforms for analyzing off-the-shelf memory modules in RDIMM and SO-DIMM forms.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_gVyZNNM5VDayDqZdu0oTgJlszT_po_A7Fku8jToBlYJsNyu3KxoX6KopaNiwm2VjxhlxoXGYVbVEbX_9fkVUh54zV5tfVn2ZrMi2bUZ8zveOYAbzVgfAg1KliqaNgdkp9-iYwAvoaHPqv2x1UallmAEC_D71V9B-pSdJn3yhxRo5HT24qBpftZJC2NIi/w446-h294/Screenshot%202025-09-12%20at%204.47.13%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_gVyZNNM5VDayDqZdu0oTgJlszT_po_A7Fku8jToBlYJsNyu3KxoX6KopaNiwm2VjxhlxoXGYVbVEbX_9fkVUh54zV5tfVn2Zr...