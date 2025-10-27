---
title: Non-Destructive Silicon Imaging (and Winner of Name that Ware December 2022)
url: https://www.bunniestudios.com/blog/?p=6656
source: bunnie's blog
date: 2023-01-05
fetch_date: 2025-10-04T03:03:47.925290
---

# Non-Destructive Silicon Imaging (and Winner of Name that Ware December 2022)

---

[« Name that Ware, December 2022](https://www.bunniestudios.com/blog/2022/name-that-ware-december-2022/)

[Name that Ware, January 2023 »](https://www.bunniestudios.com/blog/2023/name-that-ware-january-2023/)

## Non-Destructive Silicon Imaging (and Winner of Name that Ware December 2022)

The ware for December 2022 is an AMD Radeon RX540 chip, part number 216-0905018. Congrats to SAM for guessing the ware; email me for your prize. The image is from [Fritzchen Fritz’s Flickr feed](https://www.flickr.com/photos/130561288%40N04/); I recommend checking out his photos (or you can [follow him on twitter](https://twitter.com/FritzchensFritz)). Even if you aren’t into photos of chips, he elevates it to an art. Even more amazingly, all of his work is public domain; hats off to him for contributing these photos to the commons with such a generous license, because it is not easy to prepare the material and take images of this quality. If any of my readers happens to know him and are willing to make an introduction, I’d appreciate that. I only discovered his work by chance while doing some background research.

First, here is the entire photo from which the ware was cropped:

[![](https://bunniefoo.com/bunnie/rx540_nir_sm.jpg)](https://bunniefoo.com/bunnie/rx540_nir.jpg)
*Credit: [Fritzchen Fritz](https://www.flickr.com/photos/130561288%40N04/)*

Interestingly, you can see the design of the chip in this photograph. This is not photoshop; based on the notes accompanying the photo, this was taken in “NIR”, or near-infrared, using a Sony NEX-5T.

Silicon is transparent to IR, and so, photographs taken in infra-red can be used to verify, at a coarse level, the construction of a chip!

I was pretty excited to see photos like this posted on the Internet, at full-resolution, because I have only read about this technique in journal articles. Silicon becomes very transparent in infrared:

![](https://bunniefoo.com/bunnie/absorption_si.jpg)
*Silicon’s absorption of light in the near infrared range. A lower value is more transparent. Generated using [PV lighthouse](https://www.pvlighthouse.com.au/refractive-index-library)*.

This principle forms the foundation of my efforts to verify the construction of silicon in a non-destructive fashion.

The line between NIR/SWIR (near/shortwave infrared) depends on who you ask, but according to [Edmud Optics](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/what-is-swir/), it places the line at 1000nm. By this definition, I’m inferring that the above photograph was probably taken using a powerful 900nm illuminator positioned to the left of the chip near the horizon. A bright light at that wavelength would have sufficient power to penetrate the ~1mm thickness of silicon to image the circuits on the other side, and placing it near the horizon prevents swamping the sensor with reflected light except for the bits of metal that happen to catch the light and reflect it upwards.

It’s also possible to do this with a [SWIR sensor](https://www.sony-semicon.com/en/products/is/industry/swir.html), using a wavelength closer to 1300nm (where silicon is as transparent as glass is to visible light), but the resolution of the photographs are much higher than the best SWIR sensor that I’m aware of. Unfortunately, it seems all interesting technologies are regulated by the US government’s ITAR, and SWIR area-scan sensors are no exception. I’m guessing they are also a critical component of night vision gear, and thus it is hard to obtain such sensors without a license. Regardless, even the photos taken at 900nm are a powerful demonstration of the utility of IR for inspecting the construction of silicon.

Here’s another image taken using what looks like the same technique:

[![](https://bunniefoo.com/bunnie/viacentaur_chasoc_sm.jpg)](https://bunniefoo.com/bunnie/viacentaur_chasoc.jpg)
*Credit: [Fritzchen Fritz](https://www.flickr.com/photos/130561288%40N04/)*

This is of the Via Centaur CHA, which has an excellently detailed [Wikichip](https://en.wikichip.org/wiki/centaur/microarchitectures/cha) page complete with floorplans, such as the one shown below.

![](https://bunniefoo.com/bunnie/centaur_cha_soc_die_(2)_annotated.png)
*Credit: [Wikichip](https://en.wikichip.org/wiki/centaur/microarchitectures/cha)*

Remember, the IR image is from the back side of the die, so you have to mirror-image (and rotate) the front-side floorplan in your head to line it up with orientation of the photograph.

According to Wikichip, this is a TSMC 16FFC (16nm) process, with a 194mm^2 die area. This means the die above is about 13.9 mm on a side. The image as-is (which is 90% package and 10% die) resolves at about 18um/pixel, so perhaps if it was a die-only shot we could resolve at something close to 5um/pixel in a single image.

With image stitching, the resolution can be even higher:

[![](https://bunniefoo.com/bunnie/viacentaur_chasoc1_sm.jpg)](https://bunniefoo.com/bunnie/viacentaur_chasoc1.jpg)
*Credit: [Fritzchen Fritz](https://www.flickr.com/photos/130561288%40N04/)*

[![](https://bunniefoo.com/bunnie/viacentaur_chasoc2_sm.jpg)](https://bunniefoo.com/bunnie/viacentaur_chasoc2.jpg)
*Credit: [Fritzchen Fritz](https://www.flickr.com/photos/130561288%40N04/)*

In these two photos, it seems the light source was rotated 90 degrees with respect to the chip, so that different sets of components are highlighted, depending on the bias of the metal routes for that component. Note that I’m inferring this image is taken through the back side because of the presence of scratches that would be from the exposed surface of the silicon, and the orientation of the imaged die is consistent with a back-side shot.

The resolution of the above images boils down to about 3um/pixel — getting fairly close to the limit of what you can do with NIR light. To put this in perspective, TSMC 16FFC has minimum metal pitch of 64nm, so a 9-track standard cell would be 0.576um tall, and an SRAM bitcell has a size of 0.074um^2, so one pixel encompasses roughly 25 logic gates or 120 bits of SRAM. In these images, you can clearly make out variations in the density of standard cell logic, as well as the size and location of individual memory macros; the internal structure of the PCI-express drivers is also readily apparent.

I’ve been contemplating silicon supply chain attacks [quite](https://www.bunniestudios.com/blog/?p=5706) a [bit](https://www.bunniestudios.com/blog/?p=5519), and I think that at this resolution, one can rule out the following forms of silicon supply chain attacks:

* Replacement of the chip with an entirely different design that emulates the original
* Insertion of a ROM larger than a few hundred bits containing alternate microcode or instruction codings
* Insertion of a RAM macro for recording data — probably of any practical size for a RAM macro, due to the presence of line drivers/amplifiers creating a high-signal reflection
* Insertion of extra I/O drivers
* Potential detection of extra eFuse elements
* Likely able to detect recompilation/resynthesis of standard cell blobs

This significantly constrains the types of attacks one has to worry about. Without backside imaging and just looking at the exterior package, it’s difficult to even know if a chip has been wholesale replaced for an inferior clone or an emulated version. The inability to add significant amounts of microcode ROM or RAM constrains the types of modifications one could make to a CPU and “get away with it”; with some additional design-level guard rails and open source RTL I suspect one could virtually eliminate effective CPU instruction-level modifications that doesn’t also introduce ISA-level flaws in every mode of operation that could be easily detected with a software-only test.

I have reasons to suspect that modifications to an eFuse box would be detectable, but because eFuses are carefully guarded black boxes such that even chip designers are not allowed to see their insides, it’s pos...