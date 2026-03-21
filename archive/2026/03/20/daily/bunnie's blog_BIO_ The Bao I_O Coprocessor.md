---
title: BIO: The Bao I/O Coprocessor
url: https://www.bunniestudios.com/blog/2026/bio-the-bao-i-o-coprocessor/
source: bunnie's blog
date: 2026-03-20
fetch_date: 2026-03-21T04:06:37.487169
---

# BIO: The Bao I/O Coprocessor

---

[« Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications](https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/)

## BIO: The Bao I/O Coprocessor

BIO is the I/O co-processor in the Baochip-1x, a mostly open source 22nm SoC I helped design. You can read more about the [Baochip-1x’s background here](https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/), or pick up an evaluation board at [Crowd Supply](https://www.crowdsupply.com/baochip/dabao).

In this post, I’ll talk about the origins of the BIO, starting by working through a detailed study of the Raspberry Pi PIO as a reference, before diving into the architecture of the BIO. I’ll then work through three programming examples of the BIO, two in assembly and one in C. If all you’re interested in is how to use the BIO, you can skip the background details and go around halfway down the post to the section titled “Design of the BIO”, or go right into the code examples.

## **Background**

I/O co-processors off-load I/O tasks from main CPU cores. Main CPUs have to juggle multiple priorities using some form of multi-tasking, which leads to unpredictable response times. These unpredictable responses manifest as undesirable jitter or delays in critical responses. Dedicating a co-processor to an I/O task achieves a determinism approaching that of a dedicated hardware state machine while maintaining the flexibility of a general purpose CPU.

A well-known example of an I/O co-processor is the Raspberry Pi’s PIO. It consists of a set of four “processors”, each with nine instructions, with an instruction memory of 32 locations, highly tuned to provide great flexibility with easy cycle-accurate manipulation of GPIOs. For example, a SPI implementation with clock, in, and out consists of a configuration modifier plus just two instructions that are executed in an “effective loop” due to configurable side-effects available in the PIO configuration, such as automatic code wrap-around and FIFO management:

```
    ".side_set 1",
    "out pins, 1 side 0 [1]",
    "in pins, 1  side 1 [1]",
```

I wanted some form of I/O co-processor in Baochip, so I studied the PIO the best way I knew how – by copying it. I forked Lawrie Griffith’s [fpga\_pio](https://github.com/lawrie/fpga_pio) as a starting point, and did a whole bunch of regression testing and detail simulation to clean up all the missing corner cases. You can find what I think is fairly close to a fully spec-compliant RP2040-generation PIO core [in this github repo](https://github.com/buncram/cram-soc/tree/cram/deps/pio).

## **Lessons Learned from the PIO**

After building a PIO clone and compiling it for an FPGA, I was surprised to find that the PIO consumes a surprisingly large amount of resources. If you’re thinking about using it in an FPGA, you’d be better off skipping the PIO and just implementing whatever peripherals you want directly using RTL.

![](https://bunniefoo.com/baochip/pio-utilization.png)

Above is a hierarchical resource map of the placed & routed PIO core targeting a XC7A100 FPGA. I’ve highlighted the portion occupied by the PIO in magenta. It uses up more than half the FPGA, even more than the RISC-V CPU core (the “VexRiscAxi4” block on the right)! Despite only being able to run nine instructions, each PIO core consists of about 5,000 logic cells. Compare this to the VexRiscv CPU, which, if you don’t count the I-cache and D-cache, consumes only 4600 logic cells.

Furthermore, the critical path of the PIO core is at least 2x worse than that of the VexRiscv. The FPGA design easily closes timing at 100MHz with just the VexRiscv, but with the PIO core in place, it struggles to close timing at 50MHz.

A quick look at the timing analysis results in Vivado gives us some clues as to what’s going on.

![](https://bunniefoo.com/baochip/pio-path.png)

Above is the logic path isolated as one of the longest combination paths in the design, and below is a detailed report of what the cells are.

![](https://bunniefoo.com/baochip/pio-path-report.png)

The issue boils down to an argument that is almost as old as computer architecture itself: the CISC vs RISC debate. While the PIO “only” has nine instructions, each instruction is incredibly complicated. A single instruction can be tailored to do all of the following within a single cycle:

* Some nominal operation (JMP, WAIT, IN, OUT, PUSH, PULL MOV, IRQ, SET)
* Increment the program counter…but also wrap it back to a pre-set location if a certain condition is hit
* Rotate data through a 32-bit barrel shifter to/from a potential destination/source
* Check a threshold and decide whether to refill input/output FIFOs, which may or may not be joined
* Potentially side-set another pin
* Compute interrupt flags and potentially change the program counter based on the result
* Resolve priority conflicts in case multiple machines attempt to touch a shared resource

A lot of the logic area turns out to be consumed by the shifters needed to handle the flexibility of the pin mapping options. A look at the `PINCTRL` register reveals four “base” selectors which implies four 32-bit barrel shifters, plus a configurable run-length tacked onto the end of the shifters. Basically, the “rotate + mask” portion of the PIO consumes more logic area than the state machine itself, and having to smash a set of rotate-masks + clock division and FIFO threshold computations into a single cycle is quite expensive time-wise. The flexibility of the PIO’s options basically means you’re emulating an FPGA-like routing network on top of an FPGA – hence the inefficiency.

Perhaps my implementation of the PIO misses some optimizations that would make it more efficient. However, I was fairly careful to remain cycle-accurate, and in doing so I had to avoid optimizations that would impact fidelity, even if it could have improved timing closure.

The lessons learned from the FPGA study also carried over to the ASIC flow. After pushing the code base through the same toolchain used to generate the Baochip-1x, the gate count and delays were similarly large and “slow”. I use “slow” in quotes because it’s still plenty fast for what it needs to do – bit banging GPIO – it’s just slow compared to what you could do in an ASIC.

## **A Caveat to PIO Users**

There seems to be at least one patent encumbering the PIO. As a matter of policy I do not read patents, thus I can’t opine as to whether or not the re-implementation infringes on any patents. However, this is signaling from the Raspberry Pi foundation that they do not welcome open source re-implementations of their block. They haven’t forced me to take down the source code for the block, but also, anyone attempting to use the reference code I’ve shared should be aware of this issue, and consider the risks of incorporating it into a product.

## **An Alternative Approach**

My professional training and career influences put me solidly in the RISC camp of computer architecture. My PhD advisor, Tom Knight, would remind us that “it’s the wires, stupid!” when thinking about hardware architectures; that complexity today is a future liability (alternately stated as “simple designs are easier to port to new processes”), and that hardware novelty is worthless without good software tooling.

As a result, the PIO, while kind of neat as an abstract mental concept, really bugged me as an implementer. Barrel shifters are expensive in hardware. There’s a lot of wires in a barrel shifter, and I’ve been trained to use wires with deliberation. Furthermore, the custom instruction set is hard to code with, especially with all of the out-of-band settings that can affect instruction execution. Even after spending a couple months writing a lot of PIO code, I still struggled to get things to work on the first try, and I relied heavily on Verilator simulations to debug any custom PIO code (I have no idea what ...