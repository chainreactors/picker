---
title: Noooooooooo Touch!
url: https://sensepost.com/blog/2025/noooooooooo-touch/
source: Orange Cyberdefense
date: 2025-11-19
fetch_date: 2025-11-20T03:08:33.319961
---

# Noooooooooo Touch!

# [![Orange Cyberdefense](/img/master-logo.svg) ![](/images/orange-logo-small.svg) ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

* [![Orange Cyberdefense](/img/master-logo.svg)

  ![](/images/orange-logo-small.svg)

  ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

# Our Blog

* [2025 (17)](/blog/2025/)
* [2024 (10)](/blog/2024/)
* [2023 (19)](/blog/2023/)
* [2022 (10)](/blog/2022/)
* [2021 (13)](/blog/2021/)
* [2020 (30)](/blog/2020/)
* [2019 (10)](/blog/2019/)
* [2018 (14)](/blog/2018/)
* [2017 (27)](/blog/2017/)
* [2016 (22)](/blog/2016/)
* [2015 (17)](/blog/2015/)
* [2014 (15)](/blog/2014/)
* [2013 (30)](/blog/2013/)
* [2012 (27)](/blog/2012/)
* [2011 (33)](/blog/2011/)
* [2010 (36)](/blog/2010/)
* [2009 (81)](/blog/2009/)
* [2008 (75)](/blog/2008/)
* [2007 (80)](/blog/2007/)

# Noooooooooo Touch!

Reading time
~18 min

*Posted
by michael.rodger@orangecyberdefense.com
on
19 November 2025*

Categories:
[Physical](/blog/physical/),
[Tools](/blog/tools/),
[Hardware](/blog/hardware/),
[Red team](/blog/red%20team/),
[Reverse engineering](/blog/reverse%20engineering/)

*TL;DR I presented this work at Insomni’hack, if you’d prefer to watch the recording of that then you can find it here:* [*https://www.youtube.com/watch?v=Nvw\_BH7jPzE*](https://www.youtube.com/watch?v=Nvw_BH7jPzE)

Imagine you’re on a physical engagement, standing outside an office door. You need an access card but you don’t have one (yet). You notice that there’s a pattern where employees need to tag in, but to leave they just wave their hand and the door swings open. You pull a torch out of your backpack and switch it on. There’s no visible light but a subtle vibration assures you that it’s on and working. You shine it through the glass door, pointing it at a bookshelf, a chair or wall on the inside, like trying to line up a shot in pool. Within about 5 seconds… pop! The door swings open, there’s nobody else in sight and you walk right in. Not even a fingerprint left behind. It turns out, this scenario isn’t as farfetched as you might think.

![](/img/pages/blog/2025/noooooooooo-touch/IMG_6443.jpg)

The subject of my hackery

## A very good place to start

Let’s go back to the very beginning. This all started when I noticed a certain type of sensor being used for access control. A cheap-looking device with the words “no touch” across the front, opening doors when you waved your hand in front of them. In all honesty, the first experiments were centred around whether they responded differently to different skin tones (they don’t), but the lunchtime science experiments got me thinking – how strong are these controls really? In this case, they were used to allow people to exit areas which required some kind of access control to enter: an RFID fob or fingerprint, but leaving the area just required a hand wave. Fair enough, you shouldn’t need credentials to “log out”. What interested me was the range: they seemed to pick up a hand wave from about 5-10 cm away depending on the sensor. It was clear that they were using infrared (IR) to accomplish this based on the telltale colour of the lens (deep red and translucent), and the fact that it would be the cheapest, most reliable way to do what they were doing. Infrared is a common method of distance sensing. What if we could somehow trigger them from the other side of the door and let ourselves in from the outside?

Given that they were easily available, and cheap, the next step was to buy one. I found one on a local e-commerce site for R350 (around $20) and a few days later it was in my hands. Time to open it up! Given that access control tech is generally quite expensive and this was… not, the inside was more or less what you’d expect from a device made to be as cheap as possible.

![](/img/pages/blog/2025/noooooooooo-touch/image-1-901x1224.jpeg "IMG_6447.jpg")

The internals of the sensor (rear with adjustment knob not shown).

Tracing the connections revealed a few main components and their functions:

* An IR emitting LED
* An IR receiver
* An adjustment knob at the back that changes the brightness of the emitting LED
* 8 LEDs (blue and green) to signal a trigger (these light up a ring around the sensor)
* A relay to control something, usually a door lock
* A controller that ties it all together

This was a pretty good result overall. The controller was easy to stick a clip onto for watching the signals which was the next step: switch it on and see what’s actually happening.

![](/img/pages/blog/2025/noooooooooo-touch/image-4-1224x474.png)

A logic analyser trace showing an object coming into view of the sensor.

![](/img/pages/blog/2025/noooooooooo-touch/image-3-1224x474.png)

When the received signal matches the emitted signal, the relay energises (door opens).

This is a logic analyser trace of the unit powered up and operating as normal. The lines are the signal levels (high/low, analogous to binary 1 and 0 in the digital realm) of each leg on the chip over time. Some legs are just for power or aren’t used so they aren’t shown here.

The repeating signal at the top is what’s being sent to the emitting LED. The next signal shows what happens when an object comes close to the switch. First with quite a bit of loss, but steadily improving, the emitted signal is reflected and the device detects it. Despite the emitter and receiver being right next to each other, there’s a plastic shroud in between preventing them from interacting directly. The signal will only be received if something reflects it back to the device from a fairly narrow angle. As my hand gets closer, the received signal becomes more and more representative of the emitted signal until… pop! The third signal shows the relay being triggered and the theoretical door now opens.

You might have already noticed, I said that the second signal was representative of the first, but beyond the timing, they don’t actually look the same. This is because there’s a lot more going on in that IR receiver than you may think. Near-infrared (the specific range we’re dealing with) occurs naturally, there’s a bunch of it coming from the sun and indoor lights, so relying on the presence of energy at that wavelength isn’t going to be reliable. Something that doesn’t occur naturally is a high-frequency toggling of that energy – known as a carrier signal. This is why the first signal in the trace looks like a solid block, it’s actually a high-speed signal.

![](/img/pages/blog/2025/noooooooooo-touch/image-5-1224x474.png)

A zoomed-in view of the signal showing that it’s a ~30 kHz waveform.

The receiver has an internal filter that only responds when it detects this carrier, and an amplifier to boost the resultant signal. Carrier present equals signal high, carrier absent means signal low. It’s a surprisingly reliable system and it’s exactly what’s used in nearly every TV and air conditioning unit remote control made in the last few decades. Of course, the carrier signal needs to be present for a little while before the signal can assert high, and the time needed can vary depending on a variety of factors. The datasheet states that anything between 4 and 10 pulses are needed before the signal will assert high. This is great news for us because it means that there needs to be some tolerance in what the device will accept as a “representative” signal.

![](/img/pages/blog/2025/noooooooooo-touch/image.png)

The deceptively complex internals that make these receivers so reliable

![](/img/pages/blog/2025/noooooooooo-touch/image-2.png)

The timing specs, showing that at least 6 pulses are recommended for the signal to be reliably detected, with the typical range being between 4 and 10.

![](/img/pages/blog/2025/noooooooooo-touch/image-6-1224x474.png)

A real-world test, 9 emitter pulses occurred before the receiver reacted.

## The plan

The theory is that if we can introduce a signal that looks enough like the one the device is expecting, then it will detect a “reflection” and trigger the relay (op...