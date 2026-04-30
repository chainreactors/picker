---
title: Name that Ware, April 2026
url: https://www.bunniestudios.com/blog/2026/name-that-ware-april-2026/
source: bunnie's blog
date: 2026-04-29
fetch_date: 2026-04-30T05:28:56.292613
---

# Name that Ware, April 2026

---

[« Winner, Name that Ware March 2026](https://www.bunniestudios.com/blog/2026/winner-name-that-ware-march-2026/)

## Name that Ware, April 2026

The Ware for April 2026 is a little bit different. Instead of showing a circuit board, I thought it’d be interesting to go inside the chips themselves and try to identify what’s happening on at the silicon level.

Since chip reading isn’t a widely spread skill, we’ll start with a gentle introduction. For this series of wares, I’ll tell you exactly which chip these images are from: they’re from the Baochip-1x. It’s unique in that at least [some of the source code is available](https://github.com/baochip/baochip-1x) – enough of it to give significant hints as to what’s going on. It’s also unique in that it was packaged to explicitly facilitate non-destructive IR imaging, thus allowing us to look at the chip without destroying it.

A good place to start for chip reading is learning how to read RAM macros. So, this month’s ware consists of several RAM macros. The challenge is to guess the total number of bits (given as an X by Y amount) in each example. Each of these RAMs exist inside the Baochip-1x, so that pre-constrains the space of valid guesses. Here’s another hint: it’s typical for all RAM to be wired into a “built in self test” (BIST) system. Such a system would effectively contain a [central index of all RAM sizes](https://github.com/baochip/baochip-1x/blob/main/rtl/modules/rbist/rtl/rbist_wrp.sv).

SRAM architecture itself hasn’t changed much over the years. I pulled my copy of “Principles of CMOS VLSI Design” (2nd edition) from 1993 off the bookshelf and checked – at a high level, these macros still reflect exactly what’s taught in that book If you don’t have a copy of that book, there’s some pretty good [modern resources on the internet](https://linexplore.com/chip-memory-part-2-the-chimpanzees-memory/) that offer an overview of the basic structure of SRAM macros.

![](https://bunniefoo.com/ntw/baochip/macro_a.png)
![](https://bunniefoo.com/ntw/baochip/macro_b.png)
![](https://bunniefoo.com/ntw/baochip/macro_c.png)
![](https://bunniefoo.com/ntw/baochip/macro_d.png)
![](https://bunniefoo.com/ntw/baochip/macro_e.png)
![](https://bunniefoo.com/ntw/baochip/macro_f.png)
[![](https://bunniefoo.com/ntw/baochip/macro_g_sm.png)](https://bunniefoo.com/ntw/baochip/macro_g.png)

All of the macros show above are at the exact same resolution except for “Macro G” – you’ll need to click on that file to download a version that’s at full size (it’s a 2MiB PNG). Also note that the macros are not “tight cropped” – I left some of the standard cells as context around the macros. Those cells are not part of the competition this month, but I like to leave them in because it helps to have the cells in-frame to get a sense of scale.

These images are courtesy of [Fail Sec Labs](https://sec.fail), and done with a Hamamatsu iPhemos-MP 1.3um LSM. This is a non-destructive infra-red imaging technique similar to IRIS, but done using a very expensive machine equipped with a laser and precision mechano-optics, and thus capable of achieving a higher resolution than IRIS. A homebrew IRIS is able to resolve many of the details visible in these images, but not with the clarity and contrast of the iPhemos-MP system. Also note that the images presented here are picked from the raw, unstitched data, and hand-stitched to reduce artifacts.

If you’d like to compare and contrast the various techniques, here’s the full-chip image files taken by various systems for download:

* Fail Sec Labs [iPhemos image](https://bunniefoo.com/ntw/baochip/baochip-50x-failseclabs.jpg) (warning: 24MiB!)
* IRIS [Sony Alpha 5000 camera with a cheap monocular zoom objective](https://bunniefoo.com/ntw/baochip/baochip-sony.jpg)
* [IRIS automated scanner](https://bunniefoo.com/ntw/baochip/baochip-iris-ref.jpg) (warning: 39MiB!)

Note that images that lack the part markings are taken on a version of the chip that was specially prepared without any top markings.

This entry was posted on Wednesday, April 29th, 2026 at 11:18 pm and is filed under [baochip](https://www.bunniestudios.com/blog/category/baochip/), [IRIS](https://www.bunniestudios.com/blog/category/iris/), [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/). You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2026/name-that-ware-april-2026/feed/) feed.
You can [leave a response](#respond), or [trackback](https://www.bunniestudios.com/blog/2026/name-that-ware-april-2026/trackback/) from your own site.

### Leave a Reply

[Click here to cancel reply.](/blog/2026/name-that-ware-april-2026/#respond)

Name (required)

Mail (will not be published) (required)

Website

Δ

---

bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)
[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).