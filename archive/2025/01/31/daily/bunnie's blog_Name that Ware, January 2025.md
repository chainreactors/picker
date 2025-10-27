---
title: Name that Ware, January 2025
url: https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/
source: bunnie's blog
date: 2025-01-31
fetch_date: 2025-10-06T20:07:31.500376
---

# Name that Ware, January 2025

---

[« Winner, Name that Ware December 2024](https://www.bunniestudios.com/blog/2025/winner-name-that-ware-december-2024/)

[Solution, Name that Ware January 2025 »](https://www.bunniestudios.com/blog/2025/solution-name-that-ware-january-2025/)

## Name that Ware, January 2025

The ware for January 2025 is shown below.

[![](https://bunniefoo.com/ntw/ntw_jan_2025_sm.jpg)](https://bunniefoo.com/ntw/ntw_jan_2025.jpg)

Thanks to [brimdavis](https://github.com/brimdavis) for contributing this ware! …back in the day when you would get wares that had “blue wires” in them…

One thing I wonder about this ware is…where are the ROMs? Perhaps I’ll find out soon!

Happy year of the snake!

***Update Feb 12 2025***

Seems to be a stumper. Lots of good analysis, but …

There’s been some mention about seeing the back side of the board; brimdavis was kind enough to provide a nice image of that:

[![](https://bunniefoo.com/ntw/ntw_jan_2025_bot_sm.jpg)](https://bunniefoo.com/ntw/ntw_jan_2025_bot.jpg)

I like how there is a dashed white line for where a blue wire should go.

Also, apparently the “wrinkly” effect is due to a problem “back in the day” where solder wicks under the solder mask during wave soldering? I never got a definitive answer on what causes that, or why modern boards don’t seem to have that issue anymore. In case nobody can guess what this ware is, I’d accept a convincing answer for the wrinkly soldermask mystery as a “tie breaker”.

I’ll drop another hint – brimdavis sent me a contextual photo of the assembly, and the ROM, RAM, and video board plug in through the 42-pin connector just above the telephone line connection unit.

This entry was posted on Thursday, January 30th, 2025 at 8:10 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/feed/) feed.
Both comments and pings are currently closed.

### 13 Responses to “Name that Ware, January 2025”

1. ![](https://secure.gravatar.com/avatar/bd2f0eb2365d2a1fcd6f4eb4d40366b1?s=32&d=mm&r=g) Cole says:

   [January 30, 2025 at 9:57 pm](https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/#comment-2692397)

   So, to start: we have an 8088 processor with a WD2797 floppy controller up top, an 8051. The original IBM PC used an 8048 for the keyboard, but maybe this clone used an 8051? The ADC0817 at the bottom is an ADC. The expansion slots use 21×2 pins, which isn’t ISA. I don’t want to say this is an IBM PC, because the ADC is quite peculiar.
2. ![](https://secure.gravatar.com/avatar/bd2f0eb2365d2a1fcd6f4eb4d40366b1?s=32&d=mm&r=g) Cole says:

   [January 30, 2025 at 10:29 pm](https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/#comment-2692400)

   Searching for “ADC0817” and “8088” only gives the “HERO 2000” line of robots. The only photo I can find of the mainboards doesn’t match. So no?

   The Cermetek CH1812 is a telephone line interface. Maybe that’s being fed into the ADC? The MC14503 buffers TL062CP op-amps between the two would match. Is it some kind of 8088-based answering machine with floppy drive storage? That would explain the lack of a DAC.

   That’s where I’m leaving it.
3. ![](https://secure.gravatar.com/avatar/bd2520e2686acee3feca0b55afa20165?s=32&d=mm&r=g) Joe says:

   [January 31, 2025 at 2:39 am](https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/#comment-2692418)

   A truly weird board. The 8088 plus 8051 would indicate this is some sort of computer, but it seems to be a very application-specific one.
   My observations so far:

   top left:
   \* ADC0817CCN is an 8-bit microprocessor compatible ADC with a 16-channel multiplexer (rather unusual for office or home computers)
   \* board (C) 1985 or 1983? (top-left corner)

   top center:
   \* Intel 8051 microcontroller (might be used for a keyboard or peripherals)
   \* interesting cutout for the connector which appears to be DB25, fixed to the case, and only 16 pins being used

   top right:
   \* J1..J4 might be for memory modules as no DRAM or SRAM chips can be found anywhere on the board
   \* 74HC245 bus transceiver with 8 traces going towards the J1..J4 sockets -> 8-bit memory bus?

   center left:
   \* wires on the left edge seem to go to a piezo buzzer

   center right:
   \* 96-pin? bus (J5)
   \* 32 pins are visible, and a “90” silkscreen print might indicate pin 90 (left of it are six more pins to complete 3 rows with 32 pins each)
   \* if that is true, it’s a DIN 41612 type C connector
   \* neighbor of the 8088 CPU: an MC146818P RTC with a 32.768Hz quartz oscillator and tunable capacitor next to it. However, the data sheet does not mention any way to power the RTC with a battery while the rest of the system is off so that’s probably not for maintaining a current date and time across off states

   bottom left:
   \* seven TL062 op-amps
   \* and three packs of MC14503 hex buffers, might have to do with the J9 connector nearby (another bus?)

   bottom center:
   \* DCPH (direct connect protective hybrid) telephone line interface – certainly not a feature of an early-80s home computer
   \* above it, a 42-pin connector J9 with bolts on its sides, probably to fix an extension board?

   bottom right:
   \* four potentiometers glued fixed, so only for factory adjustment
   \* WD2797 FDC and a 34-pin colorful floppy cable next to it plus classic 4-pin floppy power cable so there is some magnetic storage device attached
   \* unmarked shiny canned module might be a voltage regulator
   \* twisted thick black-and white pair of wires appears to carry 16V (indicated by the silk screen near the large electrolytics)
   \* maybe system power is provided by the bus at J5?

   more:
   \* large diameter holes will probably allow case plastic posts to route through the board (in operation, there might be more boards on top of or below this one)
   \* no video components
   \* ICs mostly from 1983 and 1984
   \* lots of 74 discrete logic
   \* lots of bodge wires and resistors especially around the ADC

   So we have a board with an 8051 MCU and 8088 CPU, phone line adapter (modem maybe?), floppy or winchester port, an ADC, an RTC, memory modules, no video, a 96-pin bus connector and another odd bus. Might be lab equipment, but I can’t make any sense of it.
4. ![](https://secure.gravatar.com/avatar/f7911f5669b811450e7ae34648de2423?s=32&d=mm&r=g) willmore says:

   [January 31, 2025 at 3:04 am](https://www.bunniestudios.com/blog/2025/name-that-ware-january-2025/#comment-2692423)

   This is an interesting board. We’ve got some generic parts and some specialized ones. The generic part is the 8088 and the 8051. We can assume the 8088 is the main processor and the 8051 is performing some simpler task for the 8088–maybe real time work with some of the specialized chips?

   The specialized chips are the A/D AD0817 and the Cermetek CH 1812 telephone line connection unit. This tell us we’re dealing with something that at least listens to a phone line. We would expect some D/A if it were interacting with the phone line in any complex fashon. There’s still the possibility that some simple TX is taking place on the phone side.

   Off the side is a floppy controller near a connector which is likely for the expected drive.

   The 8051 is next to a custom looking connector which is likely related. I would assume there’s some kind of digital connected device hanging off that port. The pins are just assigned sequentially from one side to another which tells me this isn’t some kind of standardized interface as those tend to use signals in a more haphazard manner. So this is likely a custom device hanging off–like a keyboard or some kind of customized I/O.

   The 8088 is right next to some small slots with 42 pins. They look to be mostly identical, but the slots may have individual detect/IRQ signals. Withtout ...