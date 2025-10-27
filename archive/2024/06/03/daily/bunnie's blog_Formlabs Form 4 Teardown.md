---
title: Formlabs Form 4 Teardown
url: https://www.bunniestudios.com/blog/2024/formlabs-form-4-teardown/
source: bunnie's blog
date: 2024-06-03
fetch_date: 2025-10-06T17:32:14.568401
---

# Formlabs Form 4 Teardown

---

[« Name that Ware, May 2024](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/)

[Winner, Name that Ware May 2024 »](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-may-2024/)

## Formlabs Form 4 Teardown

[Formlabs](https://formlabs.com/) has recently launched the fourth edition of their flagship SLA printer line, the [Form 4](https://formlabs.com/3d-printers/form-4/). Of course, I jumped on the chance to do a teardown of the printer; I’m grateful that I was able to do the same for the [Form 1](https://www.bunniestudios.com/blog/2013/formlabs-form-1-teardown/), [Form 2](https://www.bunniestudios.com/blog/2016/formlabs-form-2-teardown/), and [Form 3](https://www.bunniestudios.com/blog/2020/formlabs-form-3-teardown/) generations. In addition to learning a lot from the process of tearing down a single printer, I am also gaining a unique perspective on how a successful hardware startup matures into an established player in a cut-throat industry.

*Financial interest disclosure: Formlabs provides me two printers for the teardown, with no contingencies on the contents or views expressed in this post. I am also a shareholder of Formlabs.*

**A Bit of Background**

The past few years has seen a step-function in the competitiveness of products out of China, and SLA 3D printers have been no exception. The Form 4 sits at a pivotal moment for Formlabs, and has parallels to the larger geopolitical race for technological superiority. In general, Chinese products tend to start from a low price point with fewer features and less reliability, focusing on the value segment and iterating their way towards up-market opportunities; US products tend to start at a high price point, with an eye on building (or defending) a differentiated brand through quality, support, and features, and iterate their way down into value-oriented models. We now sit at a point where both the iterate-up and iterate-down approaches are directly competing for the same markets, setting the stage for the current trade war.

Being the first to gain momentum in a field also results in the dilemma of inertia. Deep financial and human capital investments into older technology often create a barrier to adopting newer technology. Mobile phone infrastructure is a poster child for the inertia of legacy: developing countries often have spectacular 5G service compared to the US, since they have no legacy infrastructure on the balance sheet to depreciate and can thus leapfrog their nations directly into mature, cost-reduced and modern mobile phone infrastructure.

In the case of 3D printers, Formlabs was founded in 2011, back when UV lasers were expensive, UV LEDs weren’t commercially viable, and full HD LCD screens (1080p) were just becoming mainstream. The most viable technology for directing light at the time was the galvanometer: a tiny mirror mounted on a motor that can adjust its angle with parts-per-thousands accuracy, tens of thousands of times a second. They invested in full custom galvanometer technology to create a consumer-priced SLA 3D printer – a technology that remained a gold standard for almost a decade, and powered three generations of Form printers.

![Form 1 and 2 light architecture](https://bunniefoo.com/bunnie/form4/form1_2.png)

Above is the light path architecture of the Form 1 and Form 2 printers. Both used a laser plus a pair of galvanometers to direct light in a 2-D plane to cure a single layer of resin through raster scanning.

![Form 3 light architecture](https://bunniefoo.com/bunnie/form4/form3.png)

The Form 3, introduced in 2019, pushed galvanometer technology to its limit. This used a laser and a single galvanometer to scan one axis, bounced off a curved mirror and into the resin tank, all in a self-contained module called a “light processing unit” (LPU). The second axis came from sliding the LPU along the rail, creating the possibility of parallel LPUs for higher throughput, and “unlimited” printing volume in the Y direction.

In the decade since Formlabs’ founding, LCD and LED technology have progressed to the point where full-frame LCD printing has become viable, with the first devices available in the range of 2015-2017. I got to play with my first LCD printer in 2019, around the time that the Form 3 was launched. The benefits of an LCD architecture were readily apparent, the biggest being build speed: an LCD printer can expose the entire build area in a single exposure, instead of having to trace a slice of the model with a single point-like laser beam. However, LCD technology still had a learning curve to climb, but manufacturers climbed it quickly, iterating rapidly and introducing new models much faster than I could keep up with.

Five years later and one pandemic in between, the Form 4 is being launched, with the light processing engine fully transitioned from galvanometer-and-laser to an LCD-and-LED platform. I’m not privy to the inside conversations at Formlabs about the change, but I imagine it wasn’t easy, because transitioning away from a decade of human capital investment into a technology platform can be a difficult HR challenge. The LPU was a truly innovative piece of technology, but apparently it couldn’t match the speed and cost of parallel light processing with an LCD. However, I do imagine that the LPU is still indispensable for high-intensity 3D printing technologies such as Selective Laser Sintering (SLS).

![Form 4 light architecture](https://bunniefoo.com/bunnie/form4/form4_arch.png)

Above is the architecture of the Form 4 – “look, ma, no moving parts!” – an entirely solid state design, capable of processing an entire layer of resin in a single go.

I’m definitely no expert in 3D printing technology – my primary exposure is through doing these teardowns – but from a first-principles perspective I can see many facial challenges around using LCDs as a light modulator for UV, such as reliability, uniformity, and build volume.

As their name implies, LCDs (liquid crystal displays) are built around cells filled with liquid crystal. Liquid crystals are organic molecules; [5CB](https://en.wikipedia.org/wiki/4-Cyano-4%27-pentylbiphenyl) is a textbook example of an LC compound.

![5CB molecule, from Wikipedia](https://bunniefoo.com/bunnie/form4/5cb.png)

Above is the structure of 5CB, snagged from its [Wikipedia page](https://en.wikipedia.org/wiki/4-Cyano-4%27-pentylbiphenyl); a few other LC molecules I looked up share a similar structure. I’m no organic chemist, but if you asked me “do you think a molecule like this might interact with intense ultraviolet light”, my answer is “definitely yes” – look at those aromatic rings!

A quick search seems to indicate that LCDs as printer elements can have a lifetime as short as a few hundred hours – which, given that the UV light is only on for a fraction of the time during a print cycle, probably translates to a few hundred prints. So, I imagine some conversations were had at Formlabs on how to either mitigate the lifetime issues or to make the machine serviceable so the LCD element can be swapped out.

Another challenge is the uniformity of the underlying LEDs. This challenge comes in two flavors. The first problem is that the LEDs themselves don’t project a uniform light cone – LEDs tend to have structural hot spots and artifacts from things such as bond wires that can create shadows; but diffusers and lenses incur optical losses which reduce the effective intensity of the light. The second is that the LEDs themselves have variance between devices and over time as they age, particularly high power devices that operate at elevated temperatures. This can be mitigated in part with smart digital controls, feedback loops, and cooling. This is helped by the fact that the light source is not on 100% of the time – in tests of the Form 4 it seems to be much less than 25% duty cycle, which gives ample time for heat dissipation.

Build volume is possibly a toss-up between galvo and LCD tec...