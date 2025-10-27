---
title: Name that Ware, May 2024
url: https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/
source: bunnie's blog
date: 2024-06-01
fetch_date: 2025-10-06T16:55:07.879066
---

# Name that Ware, May 2024

---

[« Winner, Name that Ware April 2024](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-april-2024/)

[Formlabs Form 4 Teardown »](https://www.bunniestudios.com/blog/2024/formlabs-form-4-teardown/)

## Name that Ware, May 2024

The Ware for May 2024 is shown below.

[![](https://bunniefoo.com/ntw/ntw_may_2024_sm.jpg)](https://bunniefoo.com/ntw/ntw_may_2024.jpg)

This is a guest ware, but I’ll reveal the contributor when I reveal the ware next month, as the name and link would also lead to the solution.

This entry was posted on Friday, May 31st, 2024 at 2:39 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/feed/) feed.
Both comments and pings are currently closed.

### 16 Responses to “Name that Ware, May 2024”

1. ![](https://secure.gravatar.com/avatar/44e9eb2c9c369484d8591d32ecebe45c?s=32&d=mm&r=g) Franz says:

   [May 31, 2024 at 3:31 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638318)

   Power board for a garage opener, or for a CNC/mill?
2. ![](https://secure.gravatar.com/avatar/44e9eb2c9c369484d8591d32ecebe45c?s=32&d=mm&r=g) Franz says:

   [May 31, 2024 at 3:38 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638322)

   Or more generally some kind of 4-channel home automation system. Just a bit puzzled by the absence of wifi/radio and the 8-pin power connector on the right…
3. ![](https://secure.gravatar.com/avatar/183ca4dca94f7bfe174344bd07798741?s=32&d=mm&r=g) Allen says:

   [May 31, 2024 at 7:45 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638372)

   Obviously controls 4 of something. It looks like it could be a home furnace control, but the four LEDs make a better UI than most furnace controls I have seen. The relays can handle switching 2700W which is beefier than home stuff. I am going to guess a commercial lighting controller. Something that turns on the lights in a grocery store or the whole floor of an office building

   * ![](https://secure.gravatar.com/avatar/dfd1fbad210ef53a07c79385a9a85e2f?s=32&d=mm&r=g) Allen says:

     [May 31, 2024 at 7:55 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638375)

     I just noticed the 50hz/60hz jumper. The micro could be counting zero crossings for accurate timing. Possibly to turn lights on/off at a specific time without drifting
4. ![](https://secure.gravatar.com/avatar/6fae1680c677883ba988d5815acd2565?s=32&d=mm&r=g) chris says:

   [May 31, 2024 at 10:57 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638417)

   Is that conformal coating ? This thing commutes main power and could be exposed to humidity, I’d say it’s coming from an A/C unit or heater.
5. ![](https://secure.gravatar.com/avatar/ba4fb75112ab988d6fa40515811614ce?s=32&d=mm&r=g) archie4oz says:

   [May 31, 2024 at 11:03 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638419)

   A controller for commercial fire doors?
6. ![](https://secure.gravatar.com/avatar/f7911f5669b811450e7ae34648de2423?s=32&d=mm&r=g) willmore says:

   [June 1, 2024 at 5:08 am](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638472)

   What’s the button for?
7. ![](https://secure.gravatar.com/avatar/046740ef9769bc8e01eba29d1064c51e?s=32&d=mm&r=g) Auswahltropf says:

   [June 1, 2024 at 12:08 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638583)

   Looks like a Industrial Controller or Motor Controller for something for something that is to be used in a rather humid environment
8. ![](https://secure.gravatar.com/avatar/cc51006c0c57971e46aaad5e7a74f506?s=32&d=mm&r=g) wrm says:

   [June 1, 2024 at 4:49 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638615)

   OK so four DC contollers and one AC control with optocoupler. PIC and EEPROM (I am making wild guesses here). Yes RTC based on mains frequency. So, time based something control. Lights, access, who knows. But how is it programmed?

   Anyway any guess is good so I’m going with “security door interlock controller”.
9. ![](https://secure.gravatar.com/avatar/f7911f5669b811450e7ae34648de2423?s=32&d=mm&r=g) willmore says:

   [June 3, 2024 at 12:14 am](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2638866)

   I question why it needs the 50/60Hz jumper. If it can see the power line (why else does it need to know the power line frequency if it doesn’t somehow do thing relative to it?) why doesn’t it just \*count\* the frequency. There’s a proper XTAL \*right there\* on the board, so the chip is running at a very accurate frequency. Telling 50 from 60 Hz isn’t rocket science!

   The important question is why FH1 is \*backwards\*???? How many of these boards failed because someone didn’t read the label and put fuse 1 in wrong? Classic design mistake.
10. ![](https://secure.gravatar.com/avatar/2493e87ed696f2a282c53849dfe5bee2?s=32&d=mm&r=g) Ben says:

    [June 3, 2024 at 6:17 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2639050)

    A few things stand out to me:

    – the 50/60Hz jumper suggests some degree of mains frequency detection (as mentioned previously, the crystal would be likely ok just for timekeeping). Mains failure detection?
    – Four upper relays are outputs – controlled from the MCU, with unsurprising LED, resistors, and transistor each.
    – The fifth relay is not controlled from the MCU (no transistor etc) but seems to be controlled from the screw terminals (flyback diode & low-current tracks on LHS of relay). Possibly controlling an inductive load, connected to the 8 pin molex plug?
    – High wattage resistors are possibly measuring current?

    No exact answer, but all of this points me to some kind of mains powered/battery-backed device. Garden lights? Gate opener?
11. ![](https://secure.gravatar.com/avatar/1b144e574dabadf7293fb876ed9f234a?s=32&d=mm&r=g) [Dirk](http://zeromips.org) says:

    [June 4, 2024 at 7:08 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2639274)

    J2 seems to be the connector for 4 relay outputs. The relay outputs are controlled by U1, probably some kind of micro.
    J1 seems to be a control connector that enables K1.
    J4 connects two voltages that get measured.
    If I identify the color codes correctly, R40/41 and R42/43 are 22k and 51k resistors, so they cannot possibly be currents shunts. At least R40/41 seem to be in series and tapped in the middle, so it looks more like a voltage divider. But the high wattage resistors, the fuses and the thick traces imply some higher current, so I don’t really get it.
    J3 and the white studs point to a daughterboard on the other side.
    The 50/60Hz jumper might be to get the sampling period right to cancel out hum from the net.

    * ![](https://secure.gravatar.com/avatar/1b144e574dabadf7293fb876ed9f234a?s=32&d=mm&r=g) [Dirk](http://zeromips.org) says:

      [June 5, 2024 at 2:20 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2639433)

      The partly applied conformal coating may point to outdoor usage. And the switch on the edge of the board might disable the device when the housing is opened, just guessing.
12. ![](https://secure.gravatar.com/avatar/42893db5560558fd4f7e057e656b2758?s=32&d=mm&r=g) Joe Obermiller says:

    [June 7, 2024 at 12:45 am](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#comment-2639857)

    This looks very similar to tanning bed controllers that I have seen.

    * ![](https://secure.gravatar.com/avatar/183ca4dca94f7bfe174344bd07798741?s=32&d=mm&r=g) Allen says:

      [June 7, 2024 at 4:36 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-may-2024/#...