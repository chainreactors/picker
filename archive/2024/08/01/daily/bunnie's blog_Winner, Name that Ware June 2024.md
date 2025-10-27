---
title: Winner, Name that Ware June 2024
url: https://www.bunniestudios.com/blog/2024/winner-name-that-ware-june-2024/
source: bunnie's blog
date: 2024-08-01
fetch_date: 2025-10-06T17:59:27.515146
---

# Winner, Name that Ware June 2024

---

[« Name that Ware, June 2024](https://www.bunniestudios.com/blog/2024/name-that-ware-june-2024/)

[Name that Ware, July 2024 »](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/)

## Winner, Name that Ware June 2024

The Ware for June 2024 is a hash board from an Antminer S19 generation bitcoin miner, with the top side heatsinks removed. I’ll give the prize to Alex, for the thoughtful details related in the comments. Congrats, email me for your prize!

![](https://bunniefoo.com/ntw/ntw_june_2024.jpg)

I chose this portion of the miner to share for the ware because it clearly shows the “string of pearls” topology of the miner. Each chip’s ground is the VDD of the chip to the left. So, the large silvery bus on the left is ground, then the next rank is VDD, the next is VDD\*2, VDD\*3, and so forth, until you reach about 12 volts. The actual value of VDD itself is low – around 0.3V, if I recall correctly. Miners focus on efficiency, not performance, so the mining chips are operated at a lower core voltage to improve computational efficiency per joule of energy consumed, at the expense of having to throw more chips at the problem for the same computational throughput.

Along the bottom side of the image, you can see that the signals between chips cross the voltage domains without a level shifter. This is one of the things that I thought was kind of crazy, because there is a risk of [latch-up](https://en.wikipedia.org/wiki/Latch-up) whenever you feed voltages in that are above or below the power supply rails. However, because the core VDD is so low (0.3V), the ground difference between adjacent chips is small enough that the parasitic diode necessary to initiate the latch-up cascade isn’t triggered.

The whole arrangement relies on each chip maintaining its core voltage to under the latch-up threshold. But what controls that voltage? The answer is that it’s pretty much unregulated – if you were to say, run hashing on one chip but leave another chip idle, the core voltages will diverge rapidly, because the idle chip will have a higher impedance than the active chip but being wired in series, all the current of the active chip must flow through the idle chip, and thus the idle chip’s voltage rises until its idle leakage becomes big enough to feed the active chips in the chain.

Of course, the *intention* is that all the chips are simultaneously ramped up in terms of computational rate, so the energy consumption is equally distributed across the string and you don’t get any massive voltage shifts between ranks.

You’ll note the supplemental metal sheets soldered onto the power busses on the board. I had removed one of the sheets in the top right of the image. These bus bars are added to the board to reduce the V-I drop of the power distribution. Each string pushes 10’s of amps of current, so reducing the resistive losses of the copper traces by adding these bus bars in between chips measurably improves the efficiency of the hasher. If you look at a more zoomed-out version of the image, the distance between the chips actually increases as you go across the board. I’m not sure exactly why this is the case but I think it’s because one side is farther from the fans, and so they adjust the density of the chips to even out the air temperature as it makes its way across the board.

Anyways, at this massive current draw, any chip failure gets…”exciting”, to use a term of art. It turns out that a miner can operate with one busted chip in the chain. Since leakage goes up super-linearly with temperature and voltage, they basically rely on physics to turn the broken chip into a pass-through heating element. The voltage shift between ranks does go up slightly in that case, but apparently still by not enough to trigger latch-up.

That being said, latch-up is a big concern. Power cycling one of these beasts takes minutes — there is an interlock in the system that will wait a very long time with the power off to ensure that every capacitor in the chain has fully discharged. In order to prevent latch-up on a power-cycle, I imagine that every capacitor’s voltage has to be discharged to something quite a bit less than 0.3V. If you’ve ever poked around an “idle” board (powered off, but possibly with some live peripheral connector plugged in), you’ll know that even the tiniest leakages can easily develop 0.1V across a node, and 0.3V+ levels can persist for a very long time without explicit discharge clamps (I’ve seen some laptops designed with discrete FETs to discharge voltage rails internally so one can do a quick suspend/resume cycle without triggering latch-up). Since the design has no clamps to discharge the internal nodes (that I can see) I presume it just relies on the minutes of idle time on the reboot to ensure that the inherent leakage paths (which become exponentially less leaky as the voltages go down) discharge the massive amount of capacitance in the string of chips.

Of course, all these shenanigans are done in the name of efficiency and low cost. Providing a buck regulator per chip would be cost-prohibitive and less efficient; you can’t beat the string-of-pearls topology for efficiency (this is what all home LED lighting uses for a reason).

But, as a “regular” digital engineer who strives for everything to go to ground, and if ground isn’t ground you fix it so that the ground plane doesn’t move, it’s kind of mind blowing that you can get such a complicated circuit to work with no fixed ground between chips. The ground of each chip floats and finds its truth through the laws of physics and the vagaries of yield and computation-dependent energy usage patterns. It’s a really brilliant example that reinforces the notion that even though one may abstract ground to be a “global 0 voltage”, in reality, ground is always local and voltages only exist in relation to a locally measurable reference point – ground bounce is “just fine” so long as your *entire* ground bounces. If you told me the idea of stringing chips together VDD-to-GND without showing me an implementation, I would have vehemently asserted it’s not possible, and you’d have all sorts of field failures and yield problems. Yet, here we are: I am confronted with proof that my intuition is incorrect. Not only is it possible, you can do it at kilowatt-scales with hundreds of chips, tera-hashes of throughput, with countless deployments around the world. Hats off to the engineers who pulled this together! I have to imagine that on the way to getting this right, there had to be some lab somewhere that got filled with quite the puff of blue smoke, and the acrid smell that heralds new things to learn.

This entry was posted on Wednesday, July 31st, 2024 at 10:43 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-june-2024/feed/) feed.
Both comments and pings are currently closed.

### 2 Responses to “Winner, Name that Ware June 2024”

1. ![](https://secure.gravatar.com/avatar/f5301caa7488c8c960aec726637017b3?s=32&d=mm&r=g) karl says:

   [September 27, 2024 at 12:18 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-june-2024/#comment-2666401)

   Thanks for sharing your thoughts !
2. ![](https://secure.gravatar.com/avatar/12c464465bf1680d0ec8df2a41692aae?s=32&d=mm&r=g) Graham says:

   [December 3, 2024 at 6:15 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-june-2024/#comment-2680550)

   I don’t think I’ve ever felt such ambivalence about a design feature before. On the one hand, this is absolutely genius, incredibly cursed, and I love it. On the other hand, why oh why did it have to be in a damn mining rig? >\_<

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.b...