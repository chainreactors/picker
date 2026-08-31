---
title: Winner, Name that Ware July 2026
url: https://www.bunniestudios.com/blog/2026/winner-name-that-ware-july-2026/
source: bunnie's blog
date: 2026-08-30
fetch_date: 2026-08-31T07:50:20.484082
---

# Winner, Name that Ware July 2026

---

[« Name that Ware, July 2026](https://www.bunniestudios.com/blog/2026/name-that-ware-july-2026/)

[Name that Ware, August 2026 »](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/)

## Winner, Name that Ware July 2026

The structure in question for last month’s ware are a pair of NPN transistors that form the core of a bandgap voltage reference circuit.

As its name implies, a bandgap voltage reference generates a near-constant voltage for use inside chips. The voltage is intended to be fairly constant over process variations, temperature variations, and power supply fluctuations. The circuit itself is [extremely clever](https://bunniefoo.com/ntw/ntw_july_2026_annotated.png), using circuit elements that have offsets that move in opposite directions with temperature to cancel each other out. Without this circuit, chips would have performance characteristics that strongly depend upon its operating temperature. Therefore, almost every system on chip has at least one of these.

![](https://bunniefoo.com/ntw/ntw_july_2026_annotated.png)

If you’re ever looking at a chip micrograph, the circuit will jump out because it’s likely to be the only thing that has two arrays of perfectly square NPN transistors next to each other. I’ve highlighted the active transistors in pink. In this case, the transistor ratio is 1:64. Modern chip designs will always include a ring of extra “dummy” transistors around the active transistors. The reason for the dummies is that they protect the core from process variations. At these insanely small geometries, a well-known problem is that transistors on the edge of an array behave differently from those in the core. This is due to a myriad of problems, but a simple example of the problem for visualization purposes is to imagine the devices going through an etching process: the concentration of the etchant will depend upon the density of the pattern being etched. The devices on the edge of an array will etch at a different rate than those in the center, and thus they will have a slightly different net performance characteristic. As a result, for very sensitive circuits like a bandgap voltage reference, it’s standard practice to “throw away” the edge devices as their characteristics are harder to control.

The orange region above the pair of NPN transistors is a pair of PMOS devices that are current mirrors that drive the NPN transistors. The blue square are a pair of resistors, and the green square is a differential amplifier that forms the active circuit core of the bandgap circuit. These circuits are so commonplace that it’s fairly easy to find a representative schematic just Googling for one:

[![](https://bunniefoo.com/ntw/Schematic-of-the-proposed-bandgap-circuit.png)](https://www.researchgate.net/figure/Schematic-of-the-proposed-bandgap-circuit_fig2_2978563)

The above was one of the first hits I got googling for “[bandgap circuit](https://www.researchgate.net/figure/Schematic-of-the-proposed-bandgap-circuit_fig2_2978563)“. The actual topology of this schematic is not exactly the same, but very similar to the circuit in the layout above.

When looking at a large, unknown die shot, I will often orient myself by first looking for a bandgap circuit, and then looking for an SRAM. Between the two of these, I get a size standard to which I can use to compare analog and digital circuits against, and work my way from there towards other functional elements on a chip.

While nobody guessed this circuit, asdf’s response gave me a chuckle, so I’ll give asdf the prize. Drop me an email to claim your prize!

This entry was posted on Sunday, August 30th, 2026 at 2:27 pm and is filed under [baochip](https://www.bunniestudios.com/blog/category/baochip/), [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2026/winner-name-that-ware-july-2026/feed/) feed.
You can skip to the end and leave a response. Pinging is currently not allowed.

### Leave a Reply

[Click here to cancel reply.](/blog/2026/winner-name-that-ware-july-2026/#respond)

Name (required)

Mail (will not be published) (required)

Website

Δ

* Name\*

  Email\*

  ![Loading](https://www.bunniestudios.com/wordpress/wp-content/plugins/email-subscribers/lite/public/images/spinner.gif)
* [Sponsor bunnie on Github](https://github.com/sponsors/bunnie)
* ## Categories

  + [Administrative](https://www.bunniestudios.com/blog/category/administrative/)
  + [baochip](https://www.bunniestudios.com/blog/category/baochip/)
  + [betrusted](https://www.bunniestudios.com/blog/category/betrusted/)
  + [Biology](https://www.bunniestudios.com/blog/category/ponderings/biology/)
  + [chibitronics](https://www.bunniestudios.com/blog/category/chibitronics/)
  + [chumby](https://www.bunniestudios.com/blog/category/chumby/)
  + [covid-19](https://www.bunniestudios.com/blog/category/covid-19/)
  + [Feminism](https://www.bunniestudios.com/blog/category/ponderings/feminism/)
  + [gongkai](https://www.bunniestudios.com/blog/category/gongkai/)
  + [Hacking](https://www.bunniestudios.com/blog/category/hacking/)
  + [IRIS](https://www.bunniestudios.com/blog/category/iris/)
  + [Made in China](https://www.bunniestudios.com/blog/category/chumby/made-in-china/)
  + [Made in Italy](https://www.bunniestudios.com/blog/category/hacking/made-in-italy/)
  + [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/)
  + [NeTV](https://www.bunniestudios.com/blog/category/hacking/netv/)
  + [novena](https://www.bunniestudios.com/blog/category/novena/)
  + [open source](https://www.bunniestudios.com/blog/category/hacking/open-source/)
  + [Ponderings](https://www.bunniestudios.com/blog/category/ponderings/)
  + [precursor](https://www.bunniestudios.com/blog/category/betrusted/precursor/)
  + [Social](https://www.bunniestudios.com/blog/category/social/)
  + [The Factory Floor](https://www.bunniestudios.com/blog/category/the-factory-floor/)
  + [Uncategorized](https://www.bunniestudios.com/blog/category/uncategorized/)
* ## Pages

  + [2012 Name That Ware Calendar](https://www.bunniestudios.com/blog/2012-name-that-ware-calendar/)
  + [Contact bunnie](https://www.bunniestudios.com/blog/contact-bunnie/)
  + [Crosslicense 1.0 (XL-1.0)](https://www.bunniestudios.com/blog/crosslicense-1-0-xl-1-0/)
  + [On Influenza A (H1N1)](https://www.bunniestudios.com/blog/on-influenza-a-h1n1/)
  + [On MicroSD Problems](https://www.bunniestudios.com/blog/on-microsd-problems/)
    - [On Hacking MicroSD Cards](https://www.bunniestudios.com/blog/on-microsd-problems/on-hacking-microsd-cards/)
  + [The $12 “Gongkai” Phone](https://www.bunniestudios.com/blog/the-12-gongkai-phone/)
  + [The Factory Floor, Part 1 of 4:
    The Quotation (or, How to Make a BOM)](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/)
    - [The Factory Floor, Part 2 of 4:
      On Design for Manufacturing](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-2-of-4on-design-for-manufacturing/)
    - [The Factory Floor, Part 3 of 4:
       Industrial Design for Startups](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-3-of-4-industrial-design-for-upstarts/)
    - [The Factory Floor, Part 4 of 4:
      Picking (and Maintaining) a Partner](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-4-of-4picking-and-maintaining-a-partner/)
  + [Why the Best Days of Open Hardware are Yet to Come](https://www.bunniestudios.com/blog/why-the-best-days-of-open-hardware-are-yet-to-come/)
  + [Add a VGA LCD to a Chumby](https://www.bunniestudios.com/blog/add-a-vga-lcd-to-a-chumby/)
  + [Dvorak on the Tandy 102](https://www.bunniestudios.com/blog/dvorak-...