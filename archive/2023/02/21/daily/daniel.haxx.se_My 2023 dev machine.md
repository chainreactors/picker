---
title: My 2023 dev machine
url: https://daniel.haxx.se/blog/2023/02/20/my-2023-dev-machine/
source: daniel.haxx.se
date: 2023-02-21
fetch_date: 2025-10-04T07:37:35.565237
---

# My 2023 dev machine

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/05/home-office-computers-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# My 2023 dev machine

[February 20, 2023](https://daniel.haxx.se/blog/2023/02/20/my-2023-dev-machine/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2023/02/20/my-2023-dev-machine/#comments)

My desktop computer is my trusted work machine that I do the majority of all my (curl) development on. When the [15th computer I’ve owned](https://daniel.haxx.se/computers.html) through the times was [ten years old](https://daniel.haxx.se/blog/2012/11/20/say-hello-to-moo/) the time was ripe to bump things up a notch.

## Requirements

I don’t do games (as in: never) and I don’t do any other 3D stuff. I just need my two 4K monitors to display my desktops and browser windows fine.

In my ordinary days I compile C code and I run tests. CPU and memory will be used to build and test faster and to be able to run separate VM runtimes in parallel without problems. I rarely even build very large or complicated software projects. (The days of [building Firefox are long gone](https://daniel.haxx.se/blog/2018/11/18/im-leaving-mozilla/)…)

Ideally, this upgrade will last for a long time again so I’ve tried to push it a little to increase those chances.

## New machine

This new baby is (of course) built from components and I’ve relied heavily on advice, research and help by my brother [Björn](https://bjorn.haxx.se/) for this.

### CPU

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/intel-core-i7-13700k-raptor-lake.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/intel-core-i7-13700k-raptor-lake.jpg)

I’m a sucker for maximum single-thread performance. Lots of things I do still run in single-threaded in a single core so I think this is good for me.

The [Intel Core i7-13700K](https://www.intel.com/content/www/us/en/products/sku/230500/intel-core-i713700k-processor-30m-cache-up-to-5-40-ghz/specifications.html) at 3.4 GHz is benchmarked at a CPU Mark that is over 7 times faster than the CPU of my old machine. 16 cores, Socket 1700 Raptor Lake. “13th gen”

On [cpubenchmark.net](https://www.cpubenchmark.net/singleThread.html), this model is currently ranked 4th among all current CPUs in single-thread performance.

### CPU Cooling

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/noctua_nh_u12a_1_2.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/noctua_nh_u12a_1_2.jpg)

I think I’m not alone in having past happy experiences with Noctua. This time I use the [Noctua NH-U12A](https://noctua.at/en/nh-u12a), which I have gotten reports does a good job for this CPU.

### Motherboard

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/MSI-PRO-B660M-A-DDR4.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/MSI-PRO-B660M-A-DDR4.jpg)

Something to host the CPU that just does the job. [MSI PRO B660M-A DDR4](https://www.msi.com/Motherboard/PRO-B660M-A-DDR4) is a small board, but I don’t need anything more.

Turned out to require a little dance to make it accept my CPU since the BIOS it shipped with did not support it, so we had to insert an older CPU first just in order to upgrade the BIOS to make it boot with the intended CPU!

### Graphics

My plan is to start trying out the built-in Intel video capabilities. Nothing extra. Lots of space in the box!

### Memory

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/corsair-VENGEANCE-RGB-PRO-SL-BLACK-01.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/corsair-VENGEANCE-RGB-PRO-SL-BLACK-01.jpg)

I don’t think I’ve experienced a situation when I have run out of my memory in my current 32GB setup, so my original plan was to go with 64GB in this new machine. However it turned out that the motherboard does not work with all four slots using my 3600MHz memories at full speed and I decided it is better to start out with 32 really fast gigabytes than 64GB at 2100MHz (which was the alternative)!

[Corsair Vengeance RGB PRO SL / 3600MHz / DDR4 / CL18](https://www.corsair.com/eu/en/Categories/Products/Memory/Vengeance-RGB-PRO-SL-Black/p/CMH32GX4M2D3600C18). Two 16GB modules installed makes it 32GB in total. I can go 2x32GB in a future when if this turns out to be too limited.

RGB-LEDs on the memory modules is apparently a thing now.

Should be >50% faster than my old memory.

### Storage

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/samsung-990-pro.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/samsung-990-pro.jpg)

I am not a data hoarder. On the disks in my current machine I use just a few hundred gigabytes. 2 TB will give me sufficient space to play with for a while. My old machine had a 3 TB spinning disk so this is less room than before, but I don’t expect that to be a problem. This storage is speced doing 14 times faster reads than my previous SSD.

The [Samsung 980 Pro series SSD 2TB M.2 (MZ-V8P2T0)](https://www.webhallen.com/se/product/331649-Samsung-980-Pro-series-SSD-2TB-M-2-MZ-V8P2T0)

### Power Supply

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/kolink-enclave.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/kolink-enclave.jpg)

The [Kolink Enclave / 600W / 80+ Gold](https://www.webhallen.com/se/product/306332-Kolink-Enclave-600W-80-Gold) is nothing special. A modular and cheap alternative that my preferred supplier happened to offer. Again, I will not run any power hungry graphics cards.

### Case

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Fractal-Define_7_TGD_Black_Compact_Left_Front-1440x1440-1.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Fractal-Define_7_TGD_Black_Compact_Left_Front-1440x1440-1.jpg)

Me and friends have been happy with Fractal Design cases in the past and a friend of mine mentioned that he recently purchased this model and is very happy, so I went with the [Fractal Design Define 7 Compact / Solid](https://www.fractal-design.com/products/cases/define/define-7-compact/).

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/dev23-internals.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/dev23-internals.jpg)

Internals with motherboard and CPU cooler in place. Not a lot of extra things in this…

This is a big case for a what is otherwise a very small computer (need). Partly because of the recommendation but also partly because that my preferred supplier did not offer any smaller Fractal Design case at the moment. At least there will be lots of air in the box.

This case looks almost identical to my old case which will make my machine upgrade at least physically impossible to detect in my home office once installed.

Front interface from left to right: Reset button, Audio I/O, 1x USB 3.1 Gen 2 Type-C, Power button, 2x USB 2.0, 2x USB 3.0,

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/dev23-front.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/dev23-front.jpg)

## Speed comparisons

Here’s how the new beast compares to the old box when doing a few of my regular every day tasks.

## Building stuff

On a typical curl debug build of mine, identical setups. Run-time in seconds on the new machine vs the old.

|  |  |  |
| --- | --- | --- |
| **Task** | **Old** | **New** |
| build curl with make -sj | 13.1 | 2.7 |
| autoreconf -fi | 13.2 | 5.6 |
| configure | 19.3 | 10.1 |
| build in curl’s test directory | 30.1 | 7.6 |
| run the first 200 curl tests **with** valgrind | 331 | 194 |

Downloading 100 GB from http:...