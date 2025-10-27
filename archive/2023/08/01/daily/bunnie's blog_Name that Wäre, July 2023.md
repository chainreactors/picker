---
title: Name that Wäre, July 2023
url: https://www.bunniestudios.com/blog/?p=6802
source: bunnie's blog
date: 2023-08-01
fetch_date: 2025-10-06T16:57:18.905865
---

# Name that Wäre, July 2023

---

[« Winner, Name that Ware June 2023](https://www.bunniestudios.com/blog/2023/winner-name-that-ware-june-2023/)

[Winner, Name that Wäre July 2023 »](https://www.bunniestudios.com/blog/2023/winner-name-that-ware-july-2023/)

## Name that Wäre, July 2023

The “wäre” for July 2023 is shown below.

[![](https://bunniefoo.com/ntw/ntw_july_2023_sm.jpg)](https://bunniefoo.com/ntw/ntw_july_2023.jpg)

[![](https://bunniefoo.com/ntw/ntw_july_2023_a_sm.jpg)](https://bunniefoo.com/ntw/ntw_july_2023_a.jpg)

[![](https://bunniefoo.com/ntw/ntw_july_2023_b_sm.jpg)](https://bunniefoo.com/ntw/ntw_july_2023_b.jpg)

Thanks to zebonaut for submitting this ware. According to him, this was fished out of a dumpster in Germany, hence “wäre” (and yes, it’s a nonsense word, but I also think it’s cute). We had a little chuckle over the ware’s construction (or more precisely, the lack thereof). You could say, “they don’t build them like they used to” — could something like this pass certification in modern Germany? Well, it seemed to have at least passed the test of time, since it only recently found its way into a dumpster, and the rating label indicates a manufacturing date from the 14th week of 1996.

#### Update Aug 7

FETguy has contributed schematics for the ware, which he reverse engineered by hand:

[![](https://bunniefoo.com/ntw/ntw_july_2023_schematic_sm.jpg)](https://bunniefoo.com/ntw/ntw_july_2023_schematic.jpg)

A big thanks for contributing these! The spirit of Name that Ware is to inspire people to learn about electronics by taking things apart and observing their construction — and reverse engineering schematics is the asymptotic limit of that spirit!

This entry was posted on Monday, July 31st, 2023 at 9:05 am and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/feed/) feed.
Both comments and pings are currently closed.

### 11 Responses to “Name that Wäre, July 2023”

1. ![](https://secure.gravatar.com/avatar/1595dc2b01ba0f5f21c5dd6f5cdf737a?s=32&d=mm&r=g) Katie says:

   [July 31, 2023 at 2:24 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583762)

   Oddly enough, “wäre” is a perfectly normal German word. “Wenn ich kluger wäre, wäre ich glücklicher” -> “If I were smarter, I would be happier”
2. ![](https://secure.gravatar.com/avatar/7ab2f9d2cbc58d27ec359636f68df80f?s=32&d=mm&r=g) useful\_d says:

   [July 31, 2023 at 4:46 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583764)

   I’m going out on a wild guess here, but it looks like the insides of a monitoring relay or transducer (maybe phase sequence?) made by Crompton / Multitek, possibly rebranded by a German or other distributor. If the black plastic part on the left is part of the case, then it might have been awkwardly bodged into a different case from its original 55mm DIN rail mount case (the cutout on the left where the LEDs are would locate in the into the front panel giving clearance for the input/output terminals.
3. ![](https://secure.gravatar.com/avatar/9b7aed793f2caa002ef0b80fc02187ab?s=32&d=mm&r=g) Alex F says:

   [July 31, 2023 at 5:18 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583766)

   so… it has three-phase L1 L2 L3 inputs, AC coupled, which route through the trimmers and rectifier to an opto coupler. it then gets amplified (BA10358 is what it sounds like) somehow (I’m too lazy to trace out the schematics) and controls a relay. so it detects the phase (as adjusted by the trim pots) and acts on that.

   my guess is this monitors the phase imbalance in a 3-phase AC system (aka normal domestic power here in Germany) and switches in or out a capacitor bank to compensate.

   or all that circuitry is meant simply to have the relay switch during the zero crossing of a particular phase. this being a German ware, having something this massively overengineered does feel right… (IMHO German engineering isn’t any good. German manufacturing is simply good enough to actually build the overly complicated crap our engineers design.)

   I obviously thought “power supply” initially because of the mains transformer. but the circuitry clearly does more.

   * ![](https://secure.gravatar.com/avatar/9b7aed793f2caa002ef0b80fc02187ab?s=32&d=mm&r=g) Alex F says:

     [July 31, 2023 at 5:31 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583767)

     just realized there’s a glimpse of the front panel in one of the shots. whatever it does, given the PCB shape this is almost certainly meant to be mounted to a DIN rail in a fuse box.

     omg wait. 2 LEDs, 2 random pairs of wires leading to the front panel… please please tell me this thing isn’t an RCD! it would make sense: phase imbalance means current is leaking elsewhere, so the RCD needs to trip (the relay). the LEDs would be to indicate state, and the buttons are test and reset. the relay would then need to trip a larger 3-phase relay, though… that’s the part that doesn’t entirely fit.

     I do not approve of that construction for a safety-critical device… that heat darkening of the board doesn’t inspire confidence.

     as said, 3-phase AC is the normal domestic power in Germany, so 3-phase RCDs are found in many residential fuse boxes.
4. ![](https://secure.gravatar.com/avatar/49b2434398efe2ca3b257c58a7887243?s=32&d=mm&r=g) Casey Callendrello says:

   [July 31, 2023 at 8:23 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583772)

   I wonder if it this is a ripple control receiver? Some German utilities use ripple control for demand management and tariff selection – i.e. cheaper nightly rates for heating, etc.

   They inject harmonics in the 50hz wave to remotely trigger load switches, especially for so-called storage ovens.

   <https://de.wikipedia.org/wiki/Rundsteuertechnik> // <https://en.wikipedia.org/wiki/Load_management#Ripple_control>
5. ![](https://secure.gravatar.com/avatar/7382b440ba01d1e9c1cf0caff61bf446?s=32&d=mm&r=g) FETguy says:

   [July 31, 2023 at 11:57 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583778)

   I think it is just a phase loss/imbalance detector. It looks like the input circuitry just senses voltage differences between the 3 phases and two trimpots adjust that. That signal gets rectified and applied to the input of the optocoupler. Maybe the rest of the circuitry is delay, set/reset, etc.
6. ![](https://secure.gravatar.com/avatar/bd2520e2686acee3feca0b55afa20165?s=32&d=mm&r=g) Joe says:

   [August 1, 2023 at 4:05 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583807)

   First thought it might be this: <https://eu.mouser.com/ProductDetail/Carlo-Gavazzi/DPA71DM48>
   But then the relay certainly can’t switch three phases at a time, rather appears to select one out of two. I imagine this might be some kind of automatic phase selector that detects the ideal phase (out of two) and switches the relay (and thereby the 1-phase consumer) to it. Couldn’t find any such product though, let a lone with a black front panel…
7. ![](https://secure.gravatar.com/avatar/7382b440ba01d1e9c1cf0caff61bf446?s=32&d=mm&r=g) FETguy says:

   [August 4, 2023 at 5:07 am](https://www.bunniestudios.com/blog/2023/name-that-ware-july-2023/#comment-2583983)

   I went ahead and made a schematic of the board. Recreational reverse engineering. I would be happy to scan and share it, but have no ready way to post it anywhere. Send it to bunnie? Anyway, I have several observations; here are a few:

   It is indeed a phase loss detector The relay is normally on, and phase loss causes it to release and stay released by latching of the transistors.

   The 4 small red wires are a mystery, but two of them, if shorted, cause the fault latch to be ...