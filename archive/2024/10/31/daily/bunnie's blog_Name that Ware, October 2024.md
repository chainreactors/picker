---
title: Name that Ware, October 2024
url: https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/
source: bunnie's blog
date: 2024-10-31
fetch_date: 2025-10-06T18:49:18.756897
---

# Name that Ware, October 2024

---

[« Winner, Name that Ware September 2024](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-september-2024/)

[Winner, Name that Ware October 2024 »](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-october-2024/)

## Name that Ware, October 2024

The Ware for October 2024 is shown below.

![](https://bunniefoo.com/ntw/ntw_oct_24_b.jpg)

This one should be a smidge easier to guess than last month’s ware. The main reason I liked this ware is actually the board shown below with the prominent star-routing. It’s such traditional hand-routing work, I love craftsmanship like this.

![](https://bunniefoo.com/ntw/ntw_oct_24_a.jpg)

For completeness, this is the top side of the board shown above:

[![](https://bunniefoo.com/ntw/ntw_oct_24_c_sm.jpg)](https://bunniefoo.com/ntw/ntw_oct_24_c.jpg)

Thanks to spida for sharing this ware!

Also, just in time for Halloween, this spooky ware made its way to my desk:

![](https://bunniefoo.com/ntw/halloware-24.jpg)

This is the “fuse box” that was connecting my flat to the power mains. I live in one of the oldest buildings in Singapore; I’m pretty sure this is part of the original wiring, which makes it over 50 years old. I guess at some point, someone decided to replace the fuse with a…wire.

OK, sure.

That’s spooky enough as it is … but also not so spooky, given that downstream of it are two very modern circuit breaker boxes with GFIs. So, I think its sole purpose was to give the power company a “switch” to disconnect the power meter from the mains, if they had to service the meter.

However, the fuse cartridge probably also played some role in pushing the copper fingers into the receptacle, so without the fuse in place, the fingers were not pushing firmly against the terminal block. Over time, one of the fingers turned into a miniature electron milling experiment.

The air quality sensor in my place had ticked up slightly a couple days ago, and I thought maybe it was the haze coming back; but then last night I smelled an acrid smell I know all too well, and when I poked my head out I heard the slight crackling of electricity arcing coming from the mains panel, and knew I had to drop everything and look for the source of trouble.

So, the servers were down for a bit yesterday, but at least I have power now and only a slightly charred mounting board at the power entry point of the unit, instead no electricity and an entirely charred unit. My place is now slightly less cursed, but if I were to be honest, this is probably not the most cursed circuit on the premises…my lab is a veritable crypt of cursed circuitry!

This entry was posted on Wednesday, October 30th, 2024 at 2:53 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/feed/) feed.
Both comments and pings are currently closed.

### 17 Responses to “Name that Ware, October 2024”

1. ![](https://secure.gravatar.com/avatar/048ec57f490baef1d7c2c2af5a3ccdaf?s=32&d=mm&r=g) [Hales](https://halestrom.net) says:

   [October 30, 2024 at 7:06 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/#comment-2673497)

   The style of PCBs immediately made my think of 90s VCRs and TVs (I think I can almost smell the gentle aromas from here).

   A couple of the part numbers give hints:

   PCM1710U = stereo audio DAC
   BA6397FP = CD player motor driver

   Probably pre-DVD because I suspect a seperate DAC on its own little PCB wouldn’t be done when you have a video codec chipset that could integrate those features. Perhaps.

   With this PCB style it’s specifically a TV/hifi appliance-scale device, not something that needs to be compact or portable.

   Guess: Consumer CD player, or maybe a more exotic audio disk media like Minidisc or perhaps Laserdisc?

   * ![](https://secure.gravatar.com/avatar/048ec57f490baef1d7c2c2af5a3ccdaf?s=32&d=mm&r=g) [Hales](https://halestrom.net) says:

     [October 30, 2024 at 7:21 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/#comment-2673501)

     I’ll add that it’s a subtly interesting power supply.

     Two stripy fuses on the right and a few bridge rectifiers. That means there is a big wound transformer in the box with this unit, with at least two sets of outputs.

     There are no inductors on this PCB, so all of the transistors on the PCB must be acting as linear regulators. That means the power budget for this unit is small, probably 10W or so.

     These design choices seem to confirm my elimination of a DVD player or VCR machine, those tended to have little self-oscillating power supplies like one of these:

     <https://ludens.cl/Electron/dcdc/dcdc.html>

     Rather cute things, but I don’t think they used the magnetics very efficiently, so they only made sense in an era where transformers were cheap but good switchmode control electronics were expensive. That pushes my date estimate back to late 80’s early 90’s.

     The two white components in the middle of the PCB are mysteries to me. “J only” = “japan only”? I think they’re fuses, perhaps Japan is more flammable… wait a second, your story about your apartment’s power isn’t completely unrelated to you opening this device up, is it? Fess up :)

     On the lower-left of the power supply board is a little display PCB. This suggests the whole thing fit into a low-profile case. A dedicated CD player is starting to seem more likely now — low power, mains transformer powered, linear regulators, low density single-sided phenolic PCB style, chip numbers that make sense.

     (That probably means I’m miles off like usual :D)
   * ![](https://secure.gravatar.com/avatar/048ec57f490baef1d7c2c2af5a3ccdaf?s=32&d=mm&r=g) [Hales](https://halestrom.net) says:

     [October 30, 2024 at 7:32 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/#comment-2673504)

     (Link in my other comment goes to the completely wrong type of power supply, sorry. I’m thinking of a mains->12V small flyback PSU, not a 12V->mains inverter. Woops. The rest of my comment regarding cost of magnetics vs switchmode controllers for this style of design still holds, however).
2. ![](https://secure.gravatar.com/avatar/bd2520e2686acee3feca0b55afa20165?s=32&d=mm&r=g) Joe says:

   [October 30, 2024 at 8:32 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/#comment-2673517)

   This has SONY written all over it, especially the style of routing and the arrow shapes pointing towards mounting screws. My guess would be a CD or MD player’s servo and controller board. One of the motors is the spindle motor whereas the other one is for moving the tray in and out. The solder side of an end-of-travel contact can also be seen. The flat flex ribbon pointing away from the spindle motor is probably going towards the laser pickup, and the other flat flex connects the assembly to the controller board (white connector in the bottom middle section)
3. ![](https://secure.gravatar.com/avatar/2a586cc0a8fca2740e5c5460b76a4218?s=32&d=mm&r=g) [TimMcNerney](https://4004.com) says:

   [October 30, 2024 at 9:42 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-october-2024/#comment-2673537)

   I’m building a backyard solar array, my first hobby project requiring an electrical inspector. Electricians in my city cost way too much, plus I previously installed a heat pump DIY, including my own wiring, and I don’t want the inspector to see what I did.
   So I’ve been grumbling about this situation, at the same time grateful that the U.S. National Electrical Code does at least keep amateurs from burning their houses down.

   Inspired by your fuse box, how about a crowdsourced send-in-your-photos campaign: absolutely terrible or vintage electrical work. There should be plenty of examples from around the world, some scary, some beautiful...