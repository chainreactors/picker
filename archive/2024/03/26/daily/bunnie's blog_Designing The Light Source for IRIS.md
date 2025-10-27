---
title: Designing The Light Source for IRIS
url: https://www.bunniestudios.com/blog/?p=7035
source: bunnie's blog
date: 2024-03-26
fetch_date: 2025-10-04T12:09:52.267624
---

# Designing The Light Source for IRIS

---

[« Sidebar on Meta-Knowledge](https://www.bunniestudios.com/blog/2024/sidebar-on-meta-knowledge/)

[A Kinematically Coupled, Nanometer-Resolution Piezo Focus Stage »](https://www.bunniestudios.com/blog/2024/a-kinematically-coupled-nanometer-resolution-piezo-focus-stage/)

## Designing The Light Source for IRIS

This post is part of a longer-running series about giving users a tangible reason to trust their hardware through my [IRIS (Infra-Red, in-situ)](https://www.bunniestudios.com/blog/?p=6937) technique. IRIS allows us to see the insides of certain types of chips, even after they are soldered to a circuit board. This is possible because under infrared light, silicon is practically transparent:

[![](https://bunniefoo.com/iris/2024/ir_sample2_sm.jpg)](https://bunniefoo.com/iris/2024/ir_sample2.jpg)

And this is what the current generation of IRIS machinery looks like:

[![](https://bunniefoo.com/iris/2024/imager-head_sm.jpg)](https://bunniefoo.com/iris/2024/imager-head.jpg)

Previously, I introduced the [context of IRIS](https://www.bunniestudios.com/blog/?p=6937), and touched on my [general methods for learning and exploring](https://www.bunniestudios.com/blog/?p=7025). This post will cover how I arrived at the final design for the light source featured in the above machine. It is structured as a case study on the general methods for learning that I covered in my [previous post](https://www.bunniestudios.com/blog/?p=7025), so if you see foofy statements about “knowing it” or “being ignorant of it”, [that’s where it comes from](https://www.bunniestudios.com/blog/?p=7025). Thus, this post will be a bit longer and more circuitous than usual; however, future posts will be more direct and to the point.

Readers interested in the TL;DR can scroll past most of this post and just look at the pretty pictures and video loops near the bottom.

As outlined in my methods post, the first step is to make an assessment of what you know and don’t know about a topic. One of the more effective rhetorical methods I use is to first try really hard to find someone else who has done it, and copy their work.

**Try Really Hard to Copy Someone Else**

As Tom Knight, my PhD advisor, used to quip, “did you know you could save a whole afternoon in the library by spending two weeks in the lab?” If there’s already something out there that’s pretty close to what I’m trying to do, perhaps my idea is not as interesting as I had thought. Maybe my time is better spent trying something else!

In practice, this means going back to the place where I had the “a-ha!” moment for the idea, and reading everything I can find about it. The original idea behind IRIS came from [reading papers on key extraction](https://eprint.iacr.org/2018/717.pdf) that used the [Hamamatsu Phemos](https://www.hamamatsu.com/jp/en/product/semiconductor-manufacturing-support-systems/failure-analysis-system.html) series of failure analysis systems. These sophisticated systems use scanning lasers to non-destructively generate high-resolution images of chips with a variety of techniques. It’s an extremely capable system, but only available to labs with multi-million dollar budgets.

[![](https://bunniefoo.com/iris/2024/iphemos-brochure.jpg)](https://bunniefoo.com/iris/2024/SSMS0063E_iPHEMOS-MPX.pdf)

*Above: except from a Hamamatsu brochure. Originally retrieved from [this link](https://www.hamamatsu.com/content/dam/hamamatsu-photonics/sites/documents/99_SALES_LIBRARY/sys/SSMS0063E_iPHEMOS-MPX.pdf), but hosted locally because the site’s link structure is not stable over time.*

So, I tried to learn as much as I could about how it was implemented, and how I might be able to make a “shallow copy” of it. I did a bunch of dumpster-diving and acquired some old galvanometers, lasers, and a scrapped confocal microscope system to see what I could learn from reverse engineering it (reverse engineering is especially effective for learning about any system involving electromechanics).

[![Nvidia@5nm@AdaLovelace@AD102@GeForce_RTX_4090@S_TW_2324A1_U2F028.MOW_AD102-301-A1___DSCx6@IR](https://live.staticflickr.com/65535/53156939446_d096ecb23b.jpg)](https://www.flickr.com/photos/130561288%40N04/53156939446/ "Nvidia@5nm@AdaLovelace@AD102@GeForce_RTX_4090@S_TW_2324A1_U2F028.MOW_AD102-301-A1___DSCx6@IR")

However, in the process of reading articles about laser scanning optics, I stumbled upon [Fritzchens Fritz’s Flickr feed](https://www.flickr.com/photos/130561288%40N04/page2) (you can browse a slideshow of his feed, above), where he uses a CMOS imager (i.e. a Sony mirrorless camera) to do bulk imaging of silicon from the backside, with an IR lamp as a light source. This is a perfect example of the “I am ignorant of it” stage of learning: I had negative emotions when I first saw it, because I had previously invested so much effort in laser scanning. How could I have missed something so obvious? Have I really been wasting my time? Surely, there must be a reason why it’s not widely adopted already… I recognized these feelings as my “ignorance smell”, so I pushed past the knee-jerk bad feelings I had about my previously misdirected efforts, and tried to learn everything I could about this new technique.

After getting past “I am ignorant of it” and “I am aware of it”, I arrived at the stage of “I know of it”. It turns out Fritz’s technique is a great idea, and much better than anything I had previously thought of. So, I abandoned my laser scanner plan and tried to move to the stage of “tried it out” by copying Fritzchen Fritz’s setup. I dug around on the Internet and found a post where some details about his setup were revealed:

[![](https://cdn.mos.cms.futurecdn.net/ErKEoBDjHJKgZP8ENRbVzM-1200-80.jpg.webp)](https://www.tomshardware.com/news/amd-64-core-epyc-cpu-die-design-architecture-ryzen-3000)

I bought a used Sony camera from [Kolari Vision](https://kolarivision.com/product-category/camera-conversion/) with the IR filter removed to try it out (you can also swap out the filter yourself, but I wanted to be able to continue using my existing camera for visible light photos). The results were spectacular, and I shared my findings in a short [arXiv paper](https://arxiv.org/abs/2303.07406).

![](https://bunniefoo.com/iris/2024/ir_sample2_sm.jpg)

Above is an example of an early image I collected using a Sony camera photographing an iPhone6 motherboard. The chip’s internal circuitry isn’t overlaid with Photoshop — it’s actually how it appears to the camera in infrared lighting.

**Extending the Technique**

Now that I was past the stage of “I have tried it out”, it was time to move towards “I know it” and beyond. The photographs are a great qualitative tool, but verification requires something more quantitative: in the end, we want a “green/red light” indicator for if a chip is true to its blueprint, or not. This would entail some sort of automated acquisition and analysis of a die image that can put tight bounds on things like the number of bits of RAM or how many logic gates are in chip. Imaging is just one part of several technologies that have to come together to achieve this.

I’m going to need:

* A camera that can image the chip
* A light source that can illuminate the chip
* A CNC robot that can move things around so we can image large chips
* Stitching software to put the images together
* Analysis software to correlate the images against designs
* Scan chain techniques to complement the gate count census

Unfortunately, the sensors in Sony’s Alpha-NEX cameras aren’t available in a format that is easily integrated with automated control software. However, Sony CMOS sensors from the Starvis2 line are available from a variety sources (for example, [Touptek](http://E3ISPM08300KPE IP108300E(2022))) in compact C-mount cases with USB connectors and automation-ready software interfaces. The [Starvis2 line](https://www.sony-semicon.com/en/technology/security/index.html) targets the surveillance camera market, where IR sensitivity ...