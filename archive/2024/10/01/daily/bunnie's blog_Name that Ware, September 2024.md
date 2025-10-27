---
title: Name that Ware, September 2024
url: https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/
source: bunnie's blog
date: 2024-10-01
fetch_date: 2025-10-06T18:48:55.763414
---

# Name that Ware, September 2024

---

[« Winner, Name that Ware August 2024](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-august-2024/)

[Winner, Name that Ware September 2024 »](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-september-2024/)

## Name that Ware, September 2024

The Ware for September 2024 is shown below:

[![](https://bunniefoo.com/ntw/ntw_sep_2024_a_sm.jpg)](https://bunniefoo.com/ntw/ntw_sep_2024_a.jpg)
[![](https://bunniefoo.com/ntw/ntw_sep_2024_b_sm.jpg)](https://bunniefoo.com/ntw/ntw_sep_2024_b.jpg)

This ware was a gift, but I won’t credit the donor until the solution is revealed, because the credit itself might give a clue about the ware.

My first reaction to seeing this board is: “this thing has a high BOM cost”. My second thought is the engineers who put it together (hopefully) got a lot of free lunches and design advice from US-based FAEs (been there, done that!). My third reaction is, huh, [this is a thing](https://www.digikey.com/en/products/detail/sharp-socle-technology/GP1S396HCPSF/4103809) (link goes to a Digikey listing for the tiniest photointerrupter that I have ever seen – 2.26 x 1.4 x 1.6mm – it’s ISO1 and ISO2 in the first image of the board; they are flanking the top and bottom of the rectangular cut-out in the board. Could come in handy someday, especially with the compact electromechanics of [IRIS](https://www.bunniestudios.com/blog/2024/iris-infra-red-in-situ-project-updates/)…).

This entry was posted on Monday, September 30th, 2024 at 3:46 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/feed/) feed.
Both comments and pings are currently closed.

### 5 Responses to “Name that Ware, September 2024”

1. ![](https://secure.gravatar.com/avatar/084bc09084831c3dd532e8e278405716?s=32&d=mm&r=g) SaakNeMah says:

   [September 30, 2024 at 9:18 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/#comment-2667166)

   I’ll go first:

   I’d say it is a (personal or stationary) gas detector/monitor e.g. measuring CO / VOC gas concentrations.
   Giveaway is the LMP91000 sensor frontend + supporting circuitry.
   Some battery chips from TI, power supply/charging via USB-C, Bluetooth SoC for wireless readout. Topped off with some LED drivers for an UI on the device.
   Given some analog switching logic (ADG704), it might even be a multichannel sensor monitor, muxing the sensors one by one to the LMP91000.

   As for the photo-interrupter: ATEX-safe push buttons? Since a conventional push button might cause a mini spark and are usually a no-go in ATEX situations.
   That would also explain the efforts taken on the BMS part of this device (and why BOM is less of an issue).

   Guessing a brand: Riken Keiki?
2. ![](https://secure.gravatar.com/avatar/bd2f0eb2365d2a1fcd6f4eb4d40366b1?s=32&d=mm&r=g) Cole says:

   [September 30, 2024 at 10:06 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/#comment-2667169)

   Looks like a Microsoft SurfLink connector on the upper-right.
3. ![](https://secure.gravatar.com/avatar/21a5590e27be9955f59b644a68a7791f?s=32&d=mm&r=g) Joseph Ruggiero says:

   [October 2, 2024 at 11:08 am](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/#comment-2667535)

   Automated insulin pump, maybe?
4. ![](https://secure.gravatar.com/avatar/0df73b73accf54cafe3c7d8ee073d141?s=32&d=mm&r=g) Jimmy says:

   [October 9, 2024 at 9:27 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/#comment-2668686)

   Somewhat IP rated usbc connector, but U17 looks like a one of those bosch BMEx80 sensors. So definitely not sealed and probably not Ex-rated.

   bq27441 fuel gauge and bq24160 charger, unit is battery powered.

   We also don’t see the buzzer/flashing led associated with the usual gas sensors/monitor. With that said, we do have 2x LP55231 9ch PWM LED driver going off to CON1. Multispectral source?

   Electrochemical cell AFE and 16bit ADC.
   Bluetooth
   One button and no display, 18 dimmable LED is probably not enough for UI. Unit is headless?

   Strange Grey Plastic with some transistors around it, and a footprint for a photomos underneath, RL1, bypassed with R74.

   ISO1 and 2 around the rectangular cutout. Interactive mechanical elements missing.

   My guess would be some kind of Microfluidic Lab on a chip type thing.
5. ![](https://secure.gravatar.com/avatar/79c6744b7d14faaaa0cf636601f0aeb5?s=32&d=mm&r=g) lamp says:

   [October 22, 2024 at 10:56 am](https://www.bunniestudios.com/blog/2024/name-that-ware-september-2024/#comment-2671379)

   That photointerrupter looks like the one framework uses for their webcam/microphone module switch (FRANJB0001). Although I’m not sure what this board is.

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).