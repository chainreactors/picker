---
title: Name that Ware, March 2023
url: https://www.bunniestudios.com/blog/?p=6749
source: bunnie's blog
date: 2023-03-31
fetch_date: 2025-10-04T11:13:26.724007
---

# Name that Ware, March 2023

---

[« Winner, Name that Ware February 2023](https://www.bunniestudios.com/blog/2023/winner-name-that-ware-february-2023/)

[Winner, Name that Ware March 2023 »](https://www.bunniestudios.com/blog/2023/winner-name-that-ware-march-2023/)

## Name that Ware, March 2023

The Ware for March 2023 is shown below:

[![](https://bunniestudios.com/blog/images/ntw_mar_2023_atop_sm.jpg)](https://bunniestudios.com/blog/images/ntw_mar_2023_atop.jpg)

[![](https://bunniestudios.com/blog/images/ntw_mar_2023_abot_sm.jpg)](https://bunniestudios.com/blog/images/ntw_mar_2023_abot.jpg)

Thank again to spida for submitting this ware. I was certainly stumped when I first saw it! Again, some very big “clues” are not shown, which I will add to the post later if it turns out to be too difficult to guess.

### Hint #1 Update

*April 9, 2023:* Here’s an additional image, courtesy of spida, that enhances the contrast on some key parts.
[![](https://bunniestudios.com/blog/images/ntw_mar_2023_hint1_sm.jpg)](https://bunniestudios.com/blog/images/ntw_mar_2023_hint1.jpg)

I’ll also drop a meta-hint. As is the case for most modern, highly integrated MCU-based wares, any context photo revealing what plugs into the connectors basically gives away the entire function of the ware. If the enhanced image of the circuit board does not converge guesses toward a correct functional class, I’ll add a context photo in roughly one week that should do the trick.

This part of the reason why I personally like looking at vintage wares and test equipment…you can learn a lot just by looking at the circuit board!

### Hint #2 Update

*April 16, 2023:* Here’s a “context” image hint. This is a picture of the circuit board, installed in its case with all of its peripheral devices plugged in. My assumption is this image should rapidly lead to the ware being guessed, but…this one has been surprisingly difficult so far!

[![](https://bunniefoo.com/ntw//ntw_mar_2023_hint2_sm.jpg)](https://bunniefoocom/ntw/ntw_mar_2023_hint2.jpg)

This entry was posted on Friday, March 31st, 2023 at 5:05 am and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/feed/) feed.
Both comments and pings are currently closed.

### 37 Responses to “Name that Ware, March 2023”

1. ![](https://secure.gravatar.com/avatar/f5a247faeba41ba01a510b80a4a87152?s=32&d=mm&r=g) Johs says:

   [March 31, 2023 at 5:30 am](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/#comment-2579826)

   Seems like a detector for markings or the like on the edge of something rotating in the cut-out. My guess would be a controller for some kind of exercise bike.
2. ![](https://secure.gravatar.com/avatar/f7911f5669b811450e7ae34648de2423?s=32&d=mm&r=g) willmore says:

   [March 31, 2023 at 7:34 am](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/#comment-2579831)

   I’ll say right off that whomever designed this PCB has a lot of experience. This board is impressive. The RF (BT+NRF) module with ground void for the antenna, the diff pair routing, the variable width power runs… This person is on their game.

   Interesting choice of devices and I/O on here. We have a pretty capable ARM uC in the middle. There’s the BT+NRF module by Laird Connectivity Inc. There’s a USB-C jack. There’s some beefy capacitors. There’s \*vibration mounts\*! There’s a routed isolation channel around the high speed XTAL/OSC module for the uC. There’s a button on the prong opposite the USB-C connector next to an LED or some kind of opto sensor facking into the ‘channel’ cut into the board. There’s what can only be an I2C EEPROM of reasonably large capacity next to the uC which is interesting as the micro has enough FLASH to store quite a bit of data. So, they either do a lot of wiring and needed the better endurance of the EEPROM, or they thought there was a price/area tradeoff that made it a better idea then getting a micro with more FLASH.

   There’s several connectors. Likely one is for the NRF antenna. The large one by the caps is for the battery I’d guess. Nothing is labeled, so I’m guessing this was in an enclosure that was never meant to be opened–which might explain the apparent adhesive residue on a lot of the chips.

   As for its age, the USB-C and RF module make it very modern–last few years at most. The vibration mounts mean it was at lest a portable device if not a mobile one. It was self powered and needed to record a good deal of data and likely relay that to another system. I can’t put my finger on it, but it ‘smells’ medical to me.

   I don’t have a ton of time to play this month, so I’m going to wish everyone else luck and I hope I’m not too wrong and my errors throw people off. If so, sorry!
3. ![](https://secure.gravatar.com/avatar/0c17b32e90c175f1840ca2f12c349dc4?s=32&d=mm&r=g) itsme says:

   [March 31, 2023 at 7:54 am](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/#comment-2579833)

   Looks like something to measure light in the cutout. No display, but RF connectivity. has usb-c, a single button. The cutout would nicely fit the assembly of an rc helicopter (and the anti vibration mounts/beefy µC would fit too), or a mouse wheel, but the remaining connectors don’t really fit those use cases, since that would require multiple servo outputs for rc helicopter, or optical sensor for a mouse.
4. ![](https://secure.gravatar.com/avatar/1d0188ef332d08658f91fb27fa78620c?s=32&d=mm&r=g) Complutronic says:

   [March 31, 2023 at 5:01 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/#comment-2579848)

   Could it be some kind of barcode reader?
   BT, vibration mounts, aerodynamic shape…
5. ![](https://secure.gravatar.com/avatar/3d992e8e345c0e90f772b95174777293?s=32&d=mm&r=g) cpresser says:

   [March 31, 2023 at 6:58 pm](https://www.bunniestudios.com/blog/2023/name-that-ware-march-2023/#comment-2579853)

   Adding to what has already been said/identified:

   The connector next to TP601 seems to be power related. It looks like there are ferrtite beads and power-switches (the two sc70-6 packages) next to it on the top side.
   I am not sure what all the resistors on the left side of the CPU are for. They look like voltage dividers, but there are just to much of them to just be feedback-dividers for the various voltage regulators.

   The CPU has a 32kHz and a ‘fast’ crystal. It might sleep most of the time while keeping a RTC alive.
   The USB connector is routed directly to the STM32, so we can’t know which USB-Device-Class is used.

   The battery-charger-chip is a ‘LP3921 Battery Charger Management and Regulator Unit with Integrated Boomer™ Audio Amplifier’. It has 7 LDOs, the battery-stuff, and audio-amplifier (BOOMER^^). All of those are wired up and seem to be used. Its has only one channel, so we can rule out any kind of audio-equipment.
   I would guess that the audio is used for a some kind of UI, perhaps some speech2text to confirm actions/user-input. So one of the two connectors (next to TP303) is most likely for some kind of speaker.

   There is a button and a LED at the bottom of the cutout. I have no clue how they would be used. The LED points inwards, like it would for a photo-interrupter. But there is no receiver, so I think its unlikely to be that.
   Perhaps there is some kind of light-guide in the cutout which is illuminated by that LED.

   The device seems to be about the size of a hand. TI mentions the following applications for the LP3921:
   • CDMA Phone Handsets
   • Low Power Wireless Handsets
   • Handheld Information Appliances
   • Personal Media Players

   None of those seem to match. There is no display and no connector for one. The interaction with the user is only a button, audio and bluetooth.
   The shock-mounts and glue/whatever residue also don’t match any of those device categories....