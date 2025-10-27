---
title: DDR4 memory organization and how it affects memory bandwidth
url: https://buaq.net/go-159480.html
source: unSafe.sh - 不安全
date: 2023-04-20
fetch_date: 2025-10-04T11:32:43.568141
---

# DDR4 memory organization and how it affects memory bandwidth

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3942769e6013a584cbef3ca145c27743.jpg)

DDR4 memory organization and how it affects memory bandwidth

Loading...
*2023-4-19 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-159480.htm)
阅读量:26
收藏*

---

Loading...

* [![Xiaomin Shen](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/mmexport1632277733244_mr1632497208886--1-.jpg)](https://blog.cloudflare.com/author/xiaomin/)

![DDR4 memory organization and how it affects memory bandwidth](https://blog.cloudflare.com/content/images/2023/04/DDR4-memory-organization-and-how-it-affects-memory-bandwidth.png)

When shopping for DDR4 memory modules, we typically look at the memory density and memory speed. For example a 32GB DDR4-2666 memory module has 32GB of memory density, and the data rate transfer speed is 2666 mega transfers per second (MT/s).

If we take a closer look at the selection of DDR4 memories, we will then notice that there are several other parameters to choose from. One of them is rank x organization, for example 1Rx8, 2Rx4, 2Rx8 and so on. What are these and does memory module rank and organization have an effect on DDR4 module performance?

In this blog, we will study the concepts of memory rank and organization, and how memory rank and organization affect the memory bandwidth performance by reviewing some benchmarking test results.

## Memory rank

Memory rank is a term that is used to describe how many sets of DRAM chips, or devices, exist on a memory module. A set of DDR4 DRAM chips is always 64-bit wide, or 72-bit wide if ECC is supported. Within a memory rank, all chips share the address, command and control signals.

The concept of memory rank is very similar to memory bank. Memory rank is a term used to describe memory modules, which are small printed circuit boards with memory chips and other electronic components on them; and memory bank is a term used to describe memory integrated circuit chips, which are the building blocks of the memory modules.

A single-rank (1R) memory module contains one set of DRAM chips. Each set of DRAM chips is 64-bits wide, or 72-bits wide if Error Correction Code (ECC) is supported.

A dual-rank (2R) memory module is similar to having two single-rank memory modules. It contains two sets of DRAM chips, therefore doubling the capacity of a single-rank module. The two ranks are selected one at a time through a chip select signal, therefore only one rank is accessible at a time.

Likewise, a quad-rank (4R) memory module contains four sets of DRAM chips. It is similar to having two dual-rank memories on one module, and it provides the greatest capacity. There are two chip select signals needed to access one of the four ranks. Again, only one rank is accessible at a time.

Figure 1 is a simplified view of the DQ signal flow on a dual-rank memory module. There are two identical sets of memory chips: set 1 and set 2. The 64-bit data I/O signals of each memory set are connected to a data I/O module. A single bit chip select (CS\_n) signal controls which set of memory chips is accessed and the data I/O signals of the selected set will be connected to the DQ pins of the memory module.

![](https://blog.cloudflare.com/content/images/2023/04/image4-5.png)

Figure 1: DQ signal path on a dual rank memory module

Dual-rank and quad-rank memory modules double or quadruple the memory capacity on a module, within the existing memory technology. Even though only one rank can be accessed at a time, the other ranks are not sitting idle. Multi-rank memory modules use a process called rank interleaving, where the ranks that are not accessed go through their refresh cycles in parallel. This pipelined process reduces memory response time, as soon as the previous rank completes data transmission, the next rank can start its transmission.

On the other hand, there is some I/O latency penalty with multi-rank memory modules, since memory controllers need additional clock cycles to move from one rank to another. The overall latency performance difference between single rank and multi-rank memories depend heavily on the type of application.

In addition, because there are less memory chips on each module, single-rank modules produce less heat and are less likely to fail.

## Memory depth and width

The capacity of each memory chip, or device, is defined as memory depth x memory width. Memory width refers to the width of the data bus, i.e. the number of DQ lines of each memory chip.

The width of memory chips are standard, they are either x4, x8 or x16. From here, we can calculate how many memory chips are in a 64-bit wide single rank memory. For example, with x4 memory chips, we will need 16 pieces (64 ÷ 4 = 16); and with x8 memory chips, we will only need 8 of them.

Let's look at the following two high-level block diagrams of 1Gbx8 and 2Gbx4 memory chips. The total memory capacity for both of them is 8Gb. Figure 2 describes the 1Gb x8 configuration, and Figure 3 describes the 2Gbx4 configuration. With DDR4, both x4 and x8 devices have 4 groups of 4 banks. x16 devices have 2 groups of 4 banks.

We can think of each memory chip as a library. Within that library, there are four bank groups, which are the four floors of the library. On each floor, there are four shelves, each shelf is similar to one of the banks. And we can locate each one of the memory cells by its row and column addresses, just like the library book call numbers. Within each bank, the row address MUX activates a line in the memory array through the Row address latch and decoder, based on the given row address. This line is also called the word line. When a word line is activated, the data on the word line is loaded on to the sense amplifiers. Subsequently, the column decoder accesses the data on the sense amplifier based on the given column address.

![](https://blog.cloudflare.com/content/images/2023/04/pasted-image-0-3.png)

Figure 2: 1Gbx8 block diagram

The capacity, or density of a memory chip is calculated as:

**Memory Depth** = Number of Rows \* Number of Columns \* Number of Banks

**Total Memory Capacity** = Memory Depth \* Memory Width

In the example of a 1Gbx8 device as shown in Figure 2 above:

Number of Row Address Bits = 16

Total Number of Rows = 2 ^ 16 = 65536

Number of Column Address Bits = 10

Total Number of Columns = 2 ^ 10 = 1024

And the calculation goes:

**Memory Depth** = 65536 Rows \* 1024 Columns \* 16 Banks = 1Gb

**Total Memory Capacity** = 1Gb \* 8 = 8Gb

Figure 3 describes the function block diagram of a 2 Gb x 4 device.

![](https://blog.cloudflare.com/content/images/2023/04/pasted-image-0--1--3.png)

Figure 3: 2Gbx4 Block Diagram

Number of Row Address Bits = 17

Total Number of Rows = 2 ^ 17 = 131072

Number of Column Address Bits = 10

Total Number of Columns = 2 ^ 10 = 1024

And the calculation goes:

**Memory Depth** = 131072 \* 1024 \* 16 = 2Gb

**Total Memory Capacity** = 2Gb\* 4 = 8Gb

## Memory module capacity

Memory rank and memory width determine how many memory devices are needed on each memory module.

A 64-bit DDR4 module with ECC support has a total of 72 bits for the data bus. Of the 72 bits, 8 bits are used for ECC. It would require a total of 18 x4 memory devices for a single rank module. Each memory device would supply 4 bits, and the total number of bits with 18 devices is 72 bits.  For a dual rank module, we would need to double the amount of memory devices to 36.

If each x4 memory device has a memory capacity of 8Gb, a single rank module with 16 + 2 (ECC) devices would have 16GB module capacity.

8Gb \* 16 = 128Gb = 16...