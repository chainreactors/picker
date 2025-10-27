---
title: Infra-Red, In Situ (IRIS) Inspection of Silicon
url: https://www.bunniestudios.com/blog/?p=6712
source: bunnie's blog
date: 2023-03-09
fetch_date: 2025-10-04T08:59:23.035258
---

# Infra-Red, In Situ (IRIS) Inspection of Silicon

---

[« Name that Ware, February 2023](https://www.bunniestudios.com/blog/2023/name-that-ware-february-2023/)

[Winner, Name that Ware February 2023 »](https://www.bunniestudios.com/blog/2023/winner-name-that-ware-february-2023/)

## Infra-Red, *In Situ* (IRIS) Inspection of Silicon

Cryptography tells us how to make a chain of trust rooted in special-purpose chips known as secure elements. But how do we come to trust our secure elements? I have been [searching](https://www.bunniestudios.com/blog/?p=5706) for [solutions](https://www.bunniestudios.com/blog/?p=5921) to this [thorny supply chain problem](https://www.bunniestudios.com/blog/?p=5519). Ideally, one can directly inspect the construction of a chip, but any viable inspection method must verify the construction of silicon chips *after* they have been integrated into finished products, *without* having to unmount or destroy the chips (“*in situ*“). The method should also ideally be *cheap and simple* enough for end users to access.

This post introduces a technique I call “Infra-Red, *In Situ*” (IRIS) inspection. It is founded on two insights: first, that silicon is transparent to infra-red light; second, that a digital camera can be modified to “see” in infra-red, thus effectively “seeing through” silicon chips. We can use these insights to inspect an increasingly popular family of chip packages known as Wafer Level Chip Scale Packages (WLCSPs) by shining infrared light through the back side of the package and detecting reflections from the lowest layers of metal using a digital camera. This technique works even after the chip has been assembled into a finished product. However, the resolution of the imaging method is limited to micron-scale features.

This post will start by briefly reviewing why silicon inspection is important, as well as some current methods for inspecting silicon. Then, I will go into the IRIS inspection method, giving background on the theory of operation while disclosing methods and initial results. Finally, I’ll contextualize the technique and discuss methods for closing the gap between micron-scale feature inspection and the nanometer-scale features found in today’s chip fabrication technology.

[DOI: 10.48550/arXiv.2303.07406](https://doi.org/10.48550/arXiv.2303.07406)

### Side Note on Trust Models

Many assume the point of trustable hardware is so that a third party can control what you do with your computer – like the secure enclave in an iPhone or a TPM in a PC. In this model, users delegate trust to vendors, and vendors do not trust users with key material: anti-tamper measures take priority over inspectability.

Readers who make this assumption would be confused by a trust method that involves open source and user inspections. To be clear, the threat model in this post assumes no third parties can be trusted, especially not the vendors. The IRIS method is for users who want to be empowered to manage their own key material. I acknowledge this is an increasingly minority position.

## Why Inspect Chips?

The problem boils down to chips being literal black boxes with nothing but the label on the outside to identify them.

[![](https://bunniefoo.com/iris/microsd_lineup_sm.jpg)](https://bunniefoo.com/iris/microsd_lineup.jpg)

For example, above is [a study I performed](https://www.bunniestudios.com/blog/?page_id=1022) surveying the construction of microSD cards in an effort to trace down the root cause of a failed lot of products. Although every microSD card ostensibly advertised the same product and brand (Kingston 2GB), a decap study (where the exterior black epoxy is dissolved using a strong acid revealing the internal chips while destroying the card) revealed a great diversity in internal construction and suspected ghost runs. The take-away is that labels can’t be trusted; if you have a high-trust situation, something more is needed to establish a device’s internal construction than the exterior markings on a chip’s package.

### What Are Some Existing Options for Inspecting Chips?

There are many options for inspecting the construction of chips; however, all of them suffer from a “Time Of Check versus Time Of Use” (TOCTOU) problem. In other words, none of these techniques are *in situ*. They must be performed either on samples of chips that are merely representative of the exact device in your possession, or they must be done at remote facilities such that the sample passes through many stranger’s hands before returning to your possession.

[![](https://bunniefoo.com/iris/DSEM_0120_sm.png)](https://bunniefoo.com/iris/DSEM_0120.png)

Scanning Electron Microscopy (SEM), exemplified above, is a popular method for inspecting chips (*image credit: tmbinc*). The technique can produce highly detailed images of even the latest nanometer-scale transistors. However, the technique is destructive: it can only probe the surface of a material. In order to image transistors one has to remove (through etching or polishing) the overlying layers of metal. Thus, the technique is not suitable for *in situ* inspection.

[![](https://bunniefoo.com/iris/fernvale-mtk6260DA_sm.jpg)](https://bunniefoo.com/iris/fernvale-mtk6260DA.jpg)

X-rays, exemplified in the above image of a [MTK6260DA](https://www.bunniestudios.com/blog/?p=4297) , are capable of non-destructive *in situ* inspection; anyone who has traveled by air is familiar with the applicability of X-rays to detect foreign objects inside locked suitcases. However, silicon is nearly transparent to the types of X-rays used in security checkpoints, making it less suitable for establishing the contents of a chip package. It can identify the size of a die and the position of bond wires, but it can’t establish much about the pattern of transistors on a die.

[![](https://bunniefoo.com/iris/pxct.png)](https://www.nature.com/articles/nature21698)

X-Ray Ptychography is a technique using high energy X-rays that can non-destructively establish the pattern of transistors on a chip. The image above is an example of a high-resolution 3D image generated by the technique, as disclosed in [this Nature paper](https://www.nature.com/articles/nature21698).

[![](https://bunniefoo.com/iris/sls_sm.jpg)](https://en.wikipedia.org/wiki/Swiss_Light_Source)

It is a very powerful technique, but unfortunately it requires a light source the size of a building, such as the Swiss Light Source (SLS) (donut-shaped building in the image above), of which there are few in the world. While it is a powerful method, it is impractical for inspecting every end user device. It also suffers from the TOCTOU problem in that your sample has to be mailed to the SLS and then mailed back to you. So, unless you hand-carried the sample to and from the SLS, your device is now additionally subject to “evil courier” attacks.

Optical microscopy – with a simple benchtop microscope, similar to those found in grade-school classrooms around the world – is also a noteworthy tool for inspecting chips that is easier to access than the SLS. Visible light can be a useful tool for checking the construction of a chip, if the chip itself has not been obscured with an opaque, over-molded plastic shell.

Fortunately, in the world of chip packaging, it has become increasingly popular to package chips with no overmolded plastic. The downside of exposing delicate silicon chips to possible mechanical abuse is offset by improved thermal performance, better electrical characteristics, smaller footprints, as well as typically lower costs when compared to overmolding. Because of its compelling advantages this style of packaging is ubiquitous in mobile devices. A common form of this package is known as the “Wafer Level Chip Scale Package” (WLCSP), and it can be optically inspected prior to assembly.

[![](https://bunniefoo.com/iris/bq27z561yphr_frontside_color_sm.jpg)](https://bunniefoo.com/iris/bq27z561yphr_frontside_color.jpg)

Above is an example of such a package viewed with an optical microscope, pri...