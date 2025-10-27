---
title: Name that Ware November, 2022
url: https://www.bunniestudios.com/blog/?p=6598
source: bunnie's blog
date: 2022-12-01
fetch_date: 2025-10-04T00:09:53.438365
---

# Name that Ware November, 2022

---

[« Winner, Name that Ware October 2022](https://www.bunniestudios.com/blog/2022/winner-name-that-ware-october-2022/)

[Towards a More Open Secure Element Chip »](https://www.bunniestudios.com/blog/2022/towards-a-more-open-secure-element-chip/)

## Name that Ware November, 2022

The Ware for November 2022 is shown below.

[![](https://bunniefoo.com/ntw/ntw_nov_22_a_sm.jpg)](https://bunniefoo.com/ntw/ntw_nov_22_a.jpg)

[![](https://bunniefoo.com/ntw/ntw_nov_22_b_sm.jpg)](https://bunniefoo.com/ntw/ntw_nov_22_b.jpg)

[![](https://bunniefoo.com/ntw/ntw_nov_22_c_sm.jpg)](https://bunniefoo.com/ntw/ntw_nov_22_c.jpg)

[![](https://bunniefoo.com/ntw/ntw_nov_22_d_sm.jpg)](https://bunniefoo.com/ntw/ntw_nov_22_d.jpg)

[![](https://bunniefoo.com/ntw/ntw_nov_22_e_sm.jpg)](https://bunniefoo.com/ntw/ntw_nov_22_e.jpg)

A grounded guard ring is placed around some of the most sensitive analog traces; I would love it if someone could teach me why the soldermask is removed for these guard rings. I imagine there must be some motivation to retain this motif even into mass production, since the mask-less traces run between SMT pins, which I have to imagine incurs a potential yield impact, or at the very least it makes rework more challenging.

Also, yet another tamper-proof seal broken:

![](https://bunniefoo.com/ntw/ntw_nov_22_f.jpg)

It was just a matter of time…such is the fate of any seal within my reach!

This entry was posted on Wednesday, November 30th, 2022 at 11:50 pm and is filed under [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/feed/) feed.
Both comments and pings are currently closed.

### 10 Responses to “Name that Ware November, 2022”

1. ![](https://secure.gravatar.com/avatar/907388c551864f831533d8e5f3a9d47e?s=32&d=mm&r=g) Josh M says:

   [December 1, 2022 at 1:23 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574540)

   I’ve already won once, and I can’t find a cute, cryptic thing to post, so I’ll just post a hash of what I think it is: 5292625fed0b36b9b37dc84225ce80e9 .
2. ![](https://secure.gravatar.com/avatar/0b2234f742cc16d700f83413eaf1cf41?s=32&d=mm&r=g) José Araújo says:

   [December 1, 2022 at 1:43 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574542)

   It’s a Keithley 2100 , found by the display part# in a Kazakhstan google result (?!?!)

   * ![](https://secure.gravatar.com/avatar/0b2234f742cc16d700f83413eaf1cf41?s=32&d=mm&r=g) José Araújo says:

     [December 1, 2022 at 1:50 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574544)

     Got a single result for “059-001-000002”, which took me to [http://topsa.kz/index.php/blog/august-2022—3/](http://topsa.kz/index.php/blog/august-2022---3/) , indicating it’s from the Keithley 2100, further confirmed by teardown photos from multiple eevblog threads.
3. ![](https://secure.gravatar.com/avatar/05e117702a984fb45ab4b5d55eb0bfb8?s=32&d=mm&r=g) [Rodrigo F.](https://www.pakequis.com.br) says:

   [December 1, 2022 at 1:43 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574543)

   Keithley 2110-240 Multimeter?

   * ![](https://secure.gravatar.com/avatar/907388c551864f831533d8e5f3a9d47e?s=32&d=mm&r=g) Josh M says:

     [December 1, 2022 at 7:43 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574554)

     Yeah, this is what I’m thinking, though I’m not sure about the -240 bit. I only got to the 2110 and called it. It’s cool that others got even further just as quickly, nicely done!

     There’s a neat teardown on youtube which includes an admonishment to not destroy the warranty sticker, which amused me in this context: <https://www.youtube.com/watch?v=xdqtuHaiVIQ> (sticker at 1:22).

     (And, closing the loop on my original comment:
     0] jbm@compressability:~$ echo “Keithley 2110” | md5sum
     5292625fed0b36b9b37dc84225ce80e9 –
     )
4. ![](https://secure.gravatar.com/avatar/ad29a22ed3009ca789feb59a2722b4d0?s=32&d=mm&r=g) Ian Mason says:

   [December 1, 2022 at 6:27 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574551)

   Yup, Keithley. Spotted it before even popping the images open to full size.

   The reason for stripping resist from over guard rings to to ensure that any leakage paths come into electrical contact with the guard ring. If you had, say, a bit of flux residue as a leakage path, if it passed between two pins but over the solder mask then the guard ring would be insulated from it and would have no effect. The whole point of a guard ring is that it’s a (relatively) low impedance path either to ground or to a duplicate of the measured signal – being insulated behind soldermask is anything but low impedance.
5. ![](https://secure.gravatar.com/avatar/6a92837883faabf5d8ad44d2ed439ae4?s=32&d=mm&r=g) miguel says:

   [December 1, 2022 at 2:59 pm](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574566)

   Yes, you found it. It is a Keithley 2110 Multimeter. I’ve found the teardown in this video:

   <https://www.youtube.com/watch?v=xdqtuHaiVIQ&ab_channel=GerrySweeney>
6. ![](https://secure.gravatar.com/avatar/d9631e37f10b3a4a0dbb86dccae61551?s=32&d=mm&r=g) [Xenador77](https://github.com/xenador77) says:

   [December 2, 2022 at 6:10 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574593)

   Wow, still amazed at how little time it takes for folks to identify these
7. ![](https://secure.gravatar.com/avatar/892bcd71debe35e68a84db650dc1c18a?s=32&d=mm&r=g) [Dev K](http://studiokumar.com) says:

   [December 10, 2022 at 3:05 am](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2574977)

   I suspect the solder mask relief is not for an analog signal reason per se but then the copper trace of the guard rings get thickened by HASL before paste and reflow, resulting in a thicker guard ring trace for free.

   * ![](https://secure.gravatar.com/avatar/c2c28662448b65b4bba8ec65352dde35?s=32&d=mm&r=g) [J. Peterson](https://www.saccade.com) says:

     [December 13, 2022 at 5:48 pm](https://www.bunniestudios.com/blog/2022/name-that-ware-november-2022/#comment-2575114)

     My thought as well. I’ve also seen this technique used to give extra current carrying capacity for high-current traces.

     That red thing in the corner is downright spooky.

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).