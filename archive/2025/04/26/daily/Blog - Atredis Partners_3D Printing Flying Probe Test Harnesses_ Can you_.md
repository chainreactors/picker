---
title: 3D Printing Flying Probe Test Harnesses: Can you?
url: https://www.atredis.com/blog/2025/4/24/3d-printing-flying-probe-test-harnesses-can-you
source: Blog - Atredis Partners
date: 2025-04-26
fetch_date: 2025-10-06T22:05:07.862517
---

# 3D Printing Flying Probe Test Harnesses: Can you?

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# 3D Printing Flying Probe Test Harnesses: Can you?

Apr 25

Written By [Sam](/blog?author=680a6cb7a8e4bb451b126b93)

# Introduction

While testing a client's device, I found it included a [castellated](https://www.pcbdirectory.com/community/what-are-castellated-holes-on-a-pcb) board with non-standard pitched castellations. I had a lot of trouble probing the castellated component with SensePeek [PCBites](https://sensepeek.com/pcbite-kits) and other styles of probes.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/76ca2f28-d52b-4c4f-b2d0-bd106a7ef859/plated-half-holes.jpg)

Printed Circuit Board with Castellated Edges

Whether due to falling over hours after being set, or being bumped out of place while setting a subsequent probe and ultimately shorting a voltage regulator and bricking a device, I became desperate for a better solution. Because of this frustration, I started tinkering with designing an assembly to hold the PCBites in place before remembering my stash of pogo pins and sleeves, and instead began designing a harness to hold pogo pins at the non-standard pitch for the target. While the test ended successfully before the need for that assembly, the idea stuck all the same.

## What Are Probes (I’ll Keep This Brief).

Electronics are commonly tested at time of manufacture using a process called [Flying Probe Testing](https://www.protoexpress.com/blog/how-flying-probe-testing-works-for-pcb-assembly/). The probes used for these tests are manufactured in a variety of formats, but generally consist of a sleeve and spring loaded pin. In automated testing, these probes allow for some wiggle room in clearance when moving to contact circuit boards or components which might have varying dimensions.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/7089a4ae-2a9b-494a-9f50-6d9cbbcf272a/asdasfdimages.jpg)

Flying Test Probes

While suited quite well for their intended purpose, spring loaded test probes, or "[pogo pins](https://www.circuits-diy.com/what-is-pogo-pin/)" have seen an increase in popularity over the last couple of decades. Uses range from small-run console modchips to charging station contacts to handheld testing probes. As implementations like these have hit the scene, they have spurred a lot of innovation.

![514W+nvzmKS._AC_UF1000,1000_QL80_.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745522927454-WOV0EWWPKPMZ94GO4XXZ/514W%2BnvzmKS._AC_UF1000%2C1000_QL80_.jpg)![514W+nvzmKS._AC_UF1000,1000_QL80_.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745522927454-WOV0EWWPKPMZ94GO4XXZ/514W%2BnvzmKS._AC_UF1000%2C1000_QL80_.jpg)

![IMG1.jpg.5249e2e6266c3355db19cb630f43b11c.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745523010881-1KGZW2B7LOX807NGJRWD/IMG1.jpg.5249e2e6266c3355db19cb630f43b11c.jpg)![IMG1.jpg.5249e2e6266c3355db19cb630f43b11c.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745523010881-1KGZW2B7LOX807NGJRWD/IMG1.jpg.5249e2e6266c3355db19cb630f43b11c.jpg)

![168029943-origpic-e3696c.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745522933657-2TPHM58QZ9DGFXMLIDM2/168029943-origpic-e3696c.jpg)![168029943-origpic-e3696c.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745522933657-2TPHM58QZ9DGFXMLIDM2/168029943-origpic-e3696c.jpg)

## Why would we want to make our own?

The use case of interest for this project is the assembly of target-specific probe harnesses. While tools like sockets exist for various formats of components, such as flash chips or MCUs, the practice of designing custom System-on-Module (SoM) boards with castellated edges for mounting and connection to the main board has become more common, and there is generally no common socket for these types of boards.

In some cases, when such a board features a common pitch such as 2.54mm, it is possible to assemble sockets to suit them using special components such as Solder Party’s [FlexyPin](https://www.solder.party/docs/flexypin/).

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/6314aba1-ee6f-4564-9bf4-e8f3d82b48c8/rfm9x_adapter.jpg)

Castellated Board Mounted with FlexyPins

However, hardware designers do not always use standard pitch for board-to-board connections, even when using otherwise standard footprints for castellations.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/2320763b-3711-4332-9170-11a7be1f1e58/zigzag.jpg)

Non-Standard Pitch or Depth Castellations

When encountering these patterns of design in hardware assessments, existing solutions such as PCBite, or generic air nozzle-based third-hand devices become cumbersome and self defeating. With each probe added, the chances of knocking an already bitten probe over increase, which could and has resulted in shorting components and bricking a test target. Obviously, this is something we would want to avoid when performing testing, especially on a client's dime and time.

For cases such as these, the appeal of designing a probe harness is significant, however, acquiring such a harness is very likely impossible. Even when clients can provide engineering or debug builds of products, it is very uncommon for them to have it in their contract for their manufacturer to also provide them one of their own flying probe assemblies, and even less likely that the assembly would be designed to contact all traces from a given major component in the first place.

The advent of affordable 3D printers begs the question of whether it may be possible to design and manufacture test probe harnesses for uncommon targets in-situ. In this post we will go through some approaches taken to try to answer this question, including what did not work and what might work better next time.

## SLA vs. FDM and the Expected Challenges of the Latter

While SLA (Stereolithography Apparatus) printers seem quite well suited to this purpose, they are also expensive to operate and messy. I personally do not own an SLA printer for these reasons, and order out for resin prints when I want them. This, however, takes weeks usually! FDM (Fused Deposition Modeling) Printers are cheap, widely available, and the materials they consume are also quite affordable.

Despite these advantages, FDM printers also come saddled with several disadvantages for this purpose. Most likely you will be printing with a .4mm nozzle, which will introduce challenges in slicing. FDM printers struggle to make corners without loss of dimensional accuracy due to expansion and shrinking of the printed material, especially when laid in the motions made by the printer to achieve a corner. Similarly, the printer must have flow, extruder steps, x/y skew, and print speed tuned in order to achieve dimensional accuracy.

![IMG_6707.jpg](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1745523576734-Q849O4JLYH7PD9XUPYEJ/IMG_6707.jpg)![IMG_6707.jpg](https://ima...