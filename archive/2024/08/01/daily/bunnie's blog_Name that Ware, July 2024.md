---
title: Name that Ware, July 2024
url: https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/
source: bunnie's blog
date: 2024-08-01
fetch_date: 2025-10-06T17:59:22.141859
---

# Name that Ware, July 2024

---

[« Winner, Name that Ware June 2024](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-june-2024/)

[Winner, Name that Ware July 2024 »](https://www.bunniestudios.com/blog/2024/winner-name-that-ware-july-2024/)

## Name that Ware, July 2024

The Ware for July 2024 is shown below.

[![](https://bunniefoo.com/ntw/ntw_jul_2024_a_sm.jpg)](https://bunniefoo.com/ntw/ntw_jul_2024_a.jpg)
[![](https://bunniefoo.com/ntw/ntw_jul_2024_b_sm.jpg)](https://bunniefoo.com/ntw/ntw_jul_2024_b.jpg)
[![](https://bunniefoo.com/ntw/ntw_jul_2024_c_sm.jpg)](https://bunniefoo.com/ntw/ntw_jul_2024_c.jpg)
[![](https://bunniefoo.com/ntw/ntw_jul_2024_d_sm.jpg)](https://bunniefoo.com/ntw/ntw_jul_2024_d.jpg)

Thanks again to [jackw01](https://jackw01.github.io/) for contributing this ware! The last two images might be killer clues that give away the ware, but they are also so cool I couldn’t not include them as part of the post.

This entry was posted on Wednesday, July 31st, 2024 at 10:43 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/feed/) feed.
Both comments and pings are currently closed.

### 5 Responses to “Name that Ware, July 2024”

1. ![](https://secure.gravatar.com/avatar/c641bf78515c0061b2647950b72abf30?s=32&d=mm&r=g) Jacob Creedon says:

   [July 31, 2024 at 11:38 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/#comment-2653827)

   My guess is a mobile POS terminal like this: <https://www.alibaba.com/product-detail/Android-Smart-POS-Terminal-Supports-All_1601168799560.html?s=p&spm=a2706.7843667.0.0.2fae31e3Y04Y8X>

   It is hard to pick out a specific one because there are a bunch of vendors with very similar designs. The biggest giveaway even before the finger print sensor was the security mesh which is required for being certified to process EMV cards. But just looking at the first image, we are looking for something that has two buttons on one side with a USB Type C port on the other side. I have found tons of variations of this design, but not precisely this one. Maybe someone else has better sleuthing than I.

   * ![](https://secure.gravatar.com/avatar/021e5f239cbf132ed99da9ade792921b?s=32&d=mm&r=g) Anon says:

     [August 1, 2024 at 1:42 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/#comment-2654072)

     It’s definitely a POS system. Probably a card reader given the SAM and SIM slots on the board. That’s a 4G/5G cellular modem as well, so it’s definitely recent as well, newer than 2020.

     Is this some sort of Japanese Ingenico Axium EX8000? Either that or a PAX E700?
2. ![](https://secure.gravatar.com/avatar/021e5f239cbf132ed99da9ade792921b?s=32&d=mm&r=g) Anon says:

   [August 1, 2024 at 2:17 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/#comment-2654080)

   It could also potentially be a Clover Flex 3 or very recent Clover Flex device, since that might include 5G cellular. In that case, it would be running Android.

   The shape of that PCB suggests either a tablet or phone shaped pos system, since the cutout is often where the battery goes. It also might be relatively thin as well.

   * ![](https://secure.gravatar.com/avatar/021e5f239cbf132ed99da9ade792921b?s=32&d=mm&r=g) Anon says:

     [August 1, 2024 at 8:24 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/#comment-2654132)

     The SIM/SAM Card ports are pointing in opposite directions and look like they have a metal slide unlatch cover. So, there’s definitely a removable panel to access it
     It doesn’t appear that there’s a removable battery however, since there are no pogo pin connectors for one to connect.

     + ![](https://secure.gravatar.com/avatar/36726bd2f5bf87b3f739d904c14b2b07?s=32&d=mm&r=g) AZeta says:

       [August 2, 2024 at 11:29 pm](https://www.bunniestudios.com/blog/2024/name-that-ware-july-2024/#comment-2654361)

       Agreed with the Android based, mobile POS terminal for USA/Canada market (SQ808-NA –> North America), with magnetic, chip, fingerprint and NFC readers (NFC attached to black cable).

       The main SoC is the Qualcomm QCM2150 (4 Cortex A53 + LTE modem Cat6, roughly equivalent to Snapdragon 212 or 410): the modem is unfortunately only 4G, “5G” refers to WiFi either the standard or the band (802.11ac a.k.a. WiFi5 @ 2.4 and 5 GHz).
       The Tongxin micro THM36 secure SoC handles the financial side.

       The battery is likely a 2S pack with two 18650, hosted in the PCB hole and connected to the white connector near the central SIM/SAM slot.

       I can’t figure out the detached module in picture 3, with the maze-like paths for signal timing: perhaps the fingerprint reader IC?

       My second guess would be a mobile terminal for logistic (wharehouse management, packet delivery), but I would expect a barcode reader instead of the fingerprint one and the lack of security processor and SAM slots.

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).