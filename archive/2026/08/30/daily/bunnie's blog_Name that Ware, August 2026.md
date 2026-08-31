---
title: Name that Ware, August 2026
url: https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/
source: bunnie's blog
date: 2026-08-30
fetch_date: 2026-08-31T07:50:19.375958
---

# Name that Ware, August 2026

---

[« Winner, Name that Ware July 2026](https://www.bunniestudios.com/blog/2026/winner-name-that-ware-july-2026/)

## Name that Ware, August 2026

The Ware for August 2026 is shown below.

![](https://bunniefoo.com/ntw/ntw_aug_26.jpg)

Technically, this is an integrated circuit – just from a very different era than last month’s ware!

This entry was posted on Sunday, August 30th, 2026 at 2:29 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/feed/) feed.
You can skip to the end and leave a response. Pinging is currently not allowed.

### 7 Responses to “Name that Ware, August 2026”

1. ![](https://secure.gravatar.com/avatar/42e813143b99c9b96fb354b14966c9b7f12dcbd5ec4df2d1e6cba8d224d85884?s=32&d=mm&r=g) [Hales](https://halestrom.net/darksleep/) says:

   [August 30, 2026 at 8:30 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772129)

   It’s so pretty o.o

   I think this looks like it could be common-emitter or common-collector amplifier circuit.

   <https://halestrom.net/misc/bunnie/2026-08_namethatware_guesses.jpg>

   The black bits are resistors. The white thing in the middle is a transistor. The glass device on the left is a diode.

   The over-abundance of pads tells me this is a prototype or small run of parts where they wanted to be able to measure the voltage on every single circuit node. It’s statistically unlikely you really need a wire going to every node for a mass manufactured circuit.

   The transistor is a mystery. I’ve not seen white (ceramic?) cases like that except on microwave transistors. I doubt 182 means BC182 (NPN silicon) but I might be wrong. I’m going to assume it’s something like an NPN BJT for the rest of this. If anyone knows the package name or more info I’d love to know.

   The round entity on the right is intriguing. It looks like its top has been painted in silver or similar for the solder contact. It heavily resembles a piezo transducer from this angle, but it’s so small and oddly mounted so I don’t think it’s for sound. I’m leaning towards it being a ceramic capacitor for decoupling the power supply rails (which makes top-right and bottom-right pads likely some mix of VCC and GND).

   The resistors at the top might be used for biasing the transistor, but, this is where my BJT transistor theory falls apart a bit. It would be more useful for biasing if the two top resistors were both wired to the transistor base pin, rather than in series with each other. But perhaps this is actually a FET and we’re feeding in an external bias voltage through the resistors (but then that obviates the need for the resistor at the bottom left that I’m injecting a signal through). IDK.

   The biggest mystery of this circuit is the glass diode on the left. It’s not connected to anything else in this circuit. Which means it’s being used to sense something that isn’t electrical, like light (photodiode) or heat (diode temperature sensor). I worry that I should not read too far into the fact it is in a nice glass case, that could be a red herring (perhaps it was the most common diode package at the time) or it might be an important clue (optical).

   Everything is covered in some faintly orange liquid. @Bunnie is it still liquid in this photo or is it set solid and just very clean?

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772129#respond)
2. ![](https://secure.gravatar.com/avatar/1a12b8a2cc53d030b4c94e164866b6f92a581429eaa99993c26acee7d7085554?s=32&d=mm&r=g) [Parkview](http://none) says:

   [August 30, 2026 at 9:27 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772130)

   This is a PCB from 1972 Science Fair, 100 in 1 Electronic Project Kit. I was given this kit as a xmas or birthday present back in the day. Many happy hours spent playing around with it, as a grew up in Australia in a very small town some 7 hours drive away from the capitol city. Our town had no library, local radio, TV or newspaper. I had built the crystal radio with it and was playing around after dinner and heard my first pop song: Eagle Rock, by Daddy Cool. I was stunned and I was instantly hooked onto music and listening to the radio fading in an out each night. I see that this was released in Australia in: 1971. Google says the kit was first released in 1972. Good times and memories.

   [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772130#respond)

   * ![](https://secure.gravatar.com/avatar/05ae74945b815893e20c162d5a0bae74b9e9be256f963124882abaf708d5e4af?s=32&d=mm&r=g) Drew Macrae says:

     [August 31, 2026 at 2:35 am](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772133)

     Oh wow, yeah it’s right on the front of it next to a schematic. I wonder if it was designed for the kit, or for more general purpose transistor radio applications?

     [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772133#respond)
   * ![](https://secure.gravatar.com/avatar/530f73111fd1a639bc426899ce4b8e9fd248d0e8830cd31943439d540e26b8a3?s=32&d=mm&r=g) [Jeff Epler](https://emergent.unpythonic.net) says:

     [August 31, 2026 at 3:09 am](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772134)

     Found a good photo of the part and associated schematic on flickr: <https://www.flickr.com/photos/blazerman/1430289241/in/photostream/> — this particular one has a different transistor package though.

     The capacitor appears to allow an AC coupled output. It also looks like the whole thing is conformally coated which I now faintly see in our photo above.

     [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772134#respond)

     + ![](https://secure.gravatar.com/avatar/42e813143b99c9b96fb354b14966c9b7f12dcbd5ec4df2d1e6cba8d224d85884?s=32&d=mm&r=g) [Hales](https://halestrom.net/darksleep/) says:

       [August 31, 2026 at 2:03 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772138)

       Wow. Ty Parkview & Jeff Epler.

       Yeah the conformal coat looks clear in your photo. Maybe it’s an epoxy that has yellowed from light exposure in Bunnie’s photo.

       I am really disappointed that the diode isn’t some optical sensor :P I was also way off target for the capacitor (cap input vs cap output).

       [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772138#respond)
   * ![](https://secure.gravatar.com/avatar/30a12032177a5d027d21f2c283529e62a1021a723194bb8468559f07cbf6d891?s=32&d=mm&r=g) David Smith says:

     [August 31, 2026 at 5:36 am](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772135)

     Yep, that’s from the 100 in 1 project kit. As soon as I saw the picture, my ancient neuron connections knew that I had seen and that I had one of these a long time ago. I too received it for a present, either Christmas or my birthday. I remember playing with it for many hours connecting the different circuits. I had a lot of fun with this one and the other 150-, 200-, 250- in one type of project sets. Thank you for bringing up the memories.

     [Reply](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/?replytocom=2772135#respond)
3. ![](https://secure.gravatar.com/avatar/06d606ad47dce4f31e0c7269698239395392bf84038b2112ceeed65b68610aca?s=32&d=mm&r=g) Peter says:

   [August 30, 2026 at 10:38 pm](https://www.bunniestudios.com/blog/2026/name-that-ware-august-2026/#comment-2772131)

   The transistor is a 2SC182. Which is a silicon NPN in a three pin TO113 package. My old paperback transistor table gives the European alternative (in characteristics not in package) as BC238.

   [Repl...