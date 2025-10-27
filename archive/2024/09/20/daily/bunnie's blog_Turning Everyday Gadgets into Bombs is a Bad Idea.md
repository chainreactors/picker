---
title: Turning Everyday Gadgets into Bombs is a Bad Idea
url: https://www.bunniestudios.com/blog/2024/turning-everyday-gadgets-into-bombs-is-a-bad-idea/
source: bunnie's blog
date: 2024-09-20
fetch_date: 2025-10-06T18:23:43.545948
---

# Turning Everyday Gadgets into Bombs is a Bad Idea

---

[« Name that Ware, August 2024](https://www.bunniestudios.com/blog/2024/name-that-ware-august-2024/)

[Winner, Name that Ware August 2024 »](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-august-2024/)

## Turning Everyday Gadgets into Bombs is a Bad Idea

I think turning everyday gadgets into bombs is a bad idea. However, recent [news coverage](https://edition.cnn.com/2024/09/17/business/pagers-cell-phones-batteries/index.html) has been framing the weaponization of pagers and radios in the Middle East as something we do not need to concern ourselves with because “we” are safe.

I respectfully disagree. Our militaries wear uniforms, and our weapons of war are clearly marked as such because our societies operate on trust. As long as we don’t see uniformed soldiers marching through our streets, we can assume that the front lines of armed conflict are far from home. When enemies violate that trust, we call it terrorism, because we no longer feel safe around everyday people and objects.

The reason we don’t see exploding battery attacks more often is not because it’s technically hard, it’s because the [erosion of public trust in everyday things](https://www.npr.org/2021/09/06/1034631928/the-cias-hunt-for-bin-laden-has-had-lasting-repercussions-for-ngos-in-pakistan) isn’t worth it. The current discourse around the potential reach of such explosive devices is clouded by the assumption that it’s technically difficult to implement and thus unlikely to find its way to our front door.

That assumption is wrong. It is both surprisingly easy to do, and could be nearly impossible to detect. After I read about the attack, it took half an hour to combine fairly common supply chain knowledge with Wikipedia queries to propose the mechanism detailed below.

**Why It’s Not Hard**

Lithium pouch batteries are ubiquitous. They are produced in enormous volumes by countless factories around the world. Small laboratories in universities regularly build them in efforts to improve their capacity and longevity. One can purchase all the tools to produce batteries in R&D quantities for a surprisingly small amount of capital, on the order of $50,000. This is a good thing: more people researching batteries means more ideas to make our gadgets last longer, while getting us closer to our green energy objectives even faster.

![](https://bunniefoo.com/bunnie/bp24-alibaba1.png)

Above is a screenshot I took today of search results on Alibaba for “pouch cell production line”.

The process to build such batteries is well understood and documented. Here is an excerpt from one vendor’s site promising to sell the equipment to build batteries in limited quantities (tens-to-hundreds per batch) for as little as $15,000:

![](https://bunniefoo.com/bunnie/bp24-alibaba2.png)

Pouch cells are made by laying cathode and anode foils between a polymer separator that is folded many times:

![](https://bunniefoo.com/bunnie/bp24-layers.png)

*Above from “High-resolution Interferometric Measurement of Thickness Change on a Lithium-Ion Pouch Battery” by Gunther Bohn, DOI:10.1088/1755-1315/281/1/012030, CC BY 3.0*

The stacking process automated, where a machine takes alternating layers of cathode and anode material (shown as bare copper in the demo below) and wraps them in separator material:

![](https://bunniefoo.com/bunnie/bp24-battery2.gif)

There’s numerous videos on Youtube showing how this is done, here’s a [couple](https://www.youtube.com/watch?v=x7t67EQzwUY) of [videos](https://www.youtube.com/watch?v=GnQ-HLZH41c) to get you started if you are curious.

After stacking, the assembly is laminated into an aluminum foil pouch, which is then trimmed and marked into the final lithium pouch format:

![](https://bunniefoo.com/bunnie/bp24-precursor_cell.jpg)

Above is a cell I had custom-fabricated for a product I make, the [Precursor](https://precursor.dev). It probably has about 10-15 layers inside, and it costs a few thousand dollars and a few weeks to get a thousand of these made. Point is, making custom pouch batteries isn’t rocket science – there’s a whole bunch of people who know how to do it, and a whole industry behind it.

Reports indicate the explosive payload in the cells is made of [PETN](https://en.wikipedia.org/wiki/Pentaerythritol_tetranitrate). I can’t comment on how credible this is, but let’s assume for now that it’s accurate. I’m not an expert in organic chemistry or explosives, but a read-through the Wikipedia page indicates that it’s a fairly stable molecule, and it can be incorporated with plasticizers to create plastic explosives. Presumably, it can be mixed with binders to create a screen-printed sheet, and passivated if needed to make it electrically insulating. The pattern of the screen printing may be constructed to additionally create a shaped-charge effect, increasing the “bang for the buck” by concentrating the shock wave in an area, effectively turning the case around the device into a small fragmentation grenade.

Such a sheet could be inserted into the battery fold-and-stack process, after the first fold is made (or, with some effort, perhaps PETN could be incorporated into the spacer polymer itself – but let’s assume for now it’s just a drop-in sheet, which is easy to execute and likely effective). This would have the effect of making one of the cathode/anode pairs inactive, reducing the battery capacity, but only by a small amount: only one layer out of at least 10 layers is affected, thus reducing capacity by 10% or less. This may be well within the manufacturing tolerance of an inexpensive battery pack; alternatively, the cell could have an extra layer added to it to compensate for the capacity loss, with a very minor increase in the pack height (0.2mm or so, about the thickness of a sheet of paper – within the “swelling tolerance” of a battery pack).

**Why It Could Be Hard to Detect**

Once folded into the core of the battery, it is sealed in an aluminum pouch. If the manufacturing process carefully isolates the folding line from the laminating line, and/or rinses the outside of the pouch with acetone to dissolve away any PETN residue prior to marking, no explosive residue can escape the pouch, thus defeating swabs that look for chemical residue. It may also well evade methods such as X-Ray fluorescence (because the elements that compose the battery, separator and PETN are too similar and too light to be detected), and through-case methods like SORS (Spatially Offset Raman Spectroscopy) would likely be defeated by the multi-layer copper laminate structure of the battery itself blocking light from probing the inner layers.

Thus, I would posit that a lithium battery constructed with a PETN layer inside is largely undetectable: no visual inspection can see it, and no surface analytical method can detect it. I don’t know off-hand of a low-cost, high-throughput X-ray method that could detect it. A high-end CT machine could pick out the PETN layer, but it’d cost around a million dollars for one machine and [scan times are around a half hour](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4755519/) – not practical for i.e. airport security or high throughput customs screening. Electrical tests of capacity and impedance through electromechanical impedance spectroscopy ([EIS](https://www.mdpi.com/2032-6653/14/11/305)) may struggle to differentiate a tampered battery from good batteries, especially if the battery was specifically engineered to fool such tests. An ultrasound test might be able to detect an extra layer, but it would require the battery to placed in intimate contact with an ultrasound scanner for screening. I also think that that PETN could be incorporated into the spacer polymer film itself, which would defeat even CT scanners (but may leave a detectable EIS fingerprint). Then again, this is just what I’m coming up with stream-of-consciousness: presumably an adversary with a staff of engineers and months of time could figure out numerous m...