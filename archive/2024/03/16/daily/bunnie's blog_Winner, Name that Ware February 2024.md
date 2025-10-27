---
title: Winner, Name that Ware February 2024
url: https://www.bunniestudios.com/blog/?p=7011
source: bunnie's blog
date: 2024-03-16
fetch_date: 2025-10-04T12:07:37.168363
---

# Winner, Name that Ware February 2024

---

[« IRIS (Infra-Red, *in situ*) Project Updates](https://www.bunniestudios.com/blog/2024/iris-infra-red-in-situ-project-updates/)

[Name that Ware, March 2024 »](https://www.bunniestudios.com/blog/2024/name-that-ware-march-2024/)

## Winner, Name that Ware February 2024

[![](https://bunniefoo.com/ntw/ntw_feb_2024_a_sm.jpg)](https://bunniefoo.com/ntw/ntw_feb_2024_a.jpg)

The ware for February 2024 is the core of a [B&G 213 Masthead Wind Sensor](https://www.bandg.com/bg/type/instrument-sensors-and-transducers/wind-sensors/213-masthead-unit/), an instrument capable of reporting both wind speed and direction. Thanks again to FETguy and [Renew Computers](https://renewcomputers.com/) for the contribution! The coil on the left hand side is a brushless [resolver](https://en.wikipedia.org/wiki/Resolver_%28electrical%29), which determines the angle of the wind; the speed of the wind is detected by the pair of inductors on the right hand side.

One might assume the right hand coils are part of a switching power regulator (due to their shape and size), but, interestingly, they are connected with tiny traces, and there are no large capacitors nearby that could be used for filtering. Instead, it seems the coils are used to pick up the movements of magnets that would revolve around the assembly. Presumably these magnets would be attached to the shaft of the anemometer cup assembly, thus giving a read on wind speed.

Personally, I would have implemented something like this using a Melexis rotary position sensor chip, like the [MLX90324](https://www.melexis.com/en/product/MLX90324/Triaxis-mainstream-rotary-position-sensor-IC-Analog-PWM-SENT). These gems can determine the angle of a magnetically coupled axis to 10 bits precision over its entire rated temperature range. I’m guessing there must be something that prevents the use of hall-effect sensors in the application — not sure what, but it would be interesting to know why.

I was thinking I’d give the prize to anyone who pointed out the oddity of the inductors on the right hand side of the board, but nobody seemed to have noticed that. There was one poster, Anon, who did name the exact make and model, but the explanation didn’t do enough to convince me that it wasn’t imaged-searched first and then backfilled with some details. If I judged this incorrectly, I apologize. But, given a lack of satisfactory answers, I will say this month there is no winner.

Perhaps if I let the competition run till the end of the month I’d have more entries, but the competition post will also get progressively more buried under IRIS updates. Thanks for playing, and hopefully my Name that Ware subscribers aren’t too annoyed by the temporary shift in gears!

This entry was posted on Saturday, March 16th, 2024 at 12:02 am and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/feed/) feed.
Both comments and pings are currently closed.

### 6 Responses to “Winner, Name that Ware February 2024”

1. ![](https://secure.gravatar.com/avatar/7ceafcad9ccf215b44b298acbe1ddeb4?s=32&d=mm&r=g) Paul Hutch says:

   [March 16, 2024 at 1:36 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2623556)

   I’ve been working in cup anemometer manufacturing for 40+ years so I know there are quite a few manufacturers who’s design refresh cycles are measured in decades. However I would not expect this from that particular manufacturer.

   Then I noticed this on the product page:

   “This is a replacement Wind Sensor for ongoing service support. We do not recommend this model for new systems, please see the latest WS300 or WS700 range for new system designs.”

   Good chance the newer models use all Hall Effect sensors.

   * ![](https://secure.gravatar.com/avatar/80798e90e0ad7f00bd9aa22d2638f82e?s=32&d=mm&r=g) bunnie says:

     [March 16, 2024 at 2:09 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2623561)

     Ah! thanks for the insight. That makes sense — this is the kind of market where customers would expect exact replacements for a long time.

     Kind of refreshing, actually, to see that kind of commitment to product longevity. And also consumers who would prefer to repair instead of throw away, although, I guess you don’t just throw away a boat because the wind sensor is busted, and probably upgrading a wind sensor could be non-trivial because it’s connected to a computer that is integrated into the boat’s console, etc. etc…

     + ![](https://secure.gravatar.com/avatar/09327be47d6db77ce88bd8504f41858e?s=32&d=mm&r=g) Bryce C says:

       [March 16, 2024 at 6:49 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2623603)

       I believe (but am only an armchair/Wikipedia expert) that a hall effect sensor’s accuracy would be impacted by magnetic fields in the environment such as those a steel hull may carry. At the very least, I know magnetic compasses require compensation/shielding aboard ships.
2. ![](https://secure.gravatar.com/avatar/ffb76266798b0dfdac6dd87c08184abf?s=32&d=mm&r=g) Jim Mussared says:

   [March 16, 2024 at 6:28 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2623597)

   I repaired and older version of this part about 10 years ago (one of the transistors had failed), much cheaper and faster turnaround than getting a replacement. We suspected lightning damage at the time (given where on the boat it lives and recent storms) but seems unlikely given that only a single part failed?

   Photos here including the full assembly: <https://photos.app.goo.gl/4k88ineWChieFQKFA>
3. ![](https://secure.gravatar.com/avatar/6d9c957393dae88d3fd211ae42094a6a?s=32&d=mm&r=g) [Tracy Hall](https://dreamsandlogic.com) says:

   [March 24, 2024 at 12:33 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2625425)

   There’s simply no \*need\* for higher precision – the wind itself is variable enough that any reading would be absolutely \*swamped\* in noise.
4. ![](https://secure.gravatar.com/avatar/7382b440ba01d1e9c1cf0caff61bf446?s=32&d=mm&r=g) FETguy says:

   [March 30, 2024 at 10:48 am](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-february-2024/#comment-2626595)

   Here are a few recap notes on this one for anyone who may see them:

   As bunnie said, I found this among board among some random e-waste at our local recycling facility. None of the rest of the instrument (vane, cups, etc, was there, but there was another board for a later version which I gather has solar power and Bluetooth comms. The sensing parts and circuitry for both wind speed and direction are identical, so I guess they like these methods.

   I didn’t know what the boards were and only found out by Googling the part number on one of them. I thought maybe Helmholtz coils for some sort of spacial location. So I wouldn’t have won the contest, either.

   I did figure out enough to try powering this board up. I found that the regulator (the SO-8) and one of the op amps were blown, so that’s why it was in the junk. Patching around those, I got it working enough to see that the coil around the middle of the black thing is driven by a 1.4 Mhz sine wave from a simple 1 transistor oscillator. And the two other coils go through circuitry to produce two analog outputs. So I agree with the guess that this is a brushless resolver used to measure wind direction.

   The two surface mount inductors on the end of the board measure wind speed, no doubt from a rotating permanent magnet and produce a pulse output. I think that’s clever, and better than the typical reed switch I see in some weather stations.

   In a nice coincidence, I designed and built my own wind direction instrument a f...