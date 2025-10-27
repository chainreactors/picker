---
title: How Chrome doubled its Speedometer scores on Android
url: http://blog.chromium.org/2024/12/doubling-speedometer-scores-android.html
source: Chromium Blog
date: 2024-12-05
fetch_date: 2025-10-06T19:37:05.031195
---

# How Chrome doubled its Speedometer scores on Android

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [How Chrome doubled its Speedometer scores on Android](https://blog.chromium.org/2024/12/doubling-speedometer-scores-android.html "How Chrome doubled its Speedometer scores on Android")

Wednesday, December 4, 2024

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjscHFeqCsz-nA-3e5XHLXHDD9nSRLgkL9jxZng8O_AiIn_WvC2G4x1AL4l-EgVAbPNAXQR3qZGmWzUtu6KjcagkBFKV4zg1vMWur7DaciR0i9eXaJrt6mFPM_OJcCBQBkXixZTSPh32YpsnM4LSq1y_ifhhRoIRuF5yB_so0zePYf8ko7kfnYnwsAqtu0F/s1600/Fast%20Curious_image.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjscHFeqCsz-nA-3e5XHLXHDD9nSRLgkL9jxZng8O_AiIn_WvC2G4x1AL4l-EgVAbPNAXQR3qZGmWzUtu6KjcagkBFKV4zg1vMWur7DaciR0i9eXaJrt6mFPM_OJcCBQBkXixZTSPh32YpsnM4LSq1y_ifhhRoIRuF5yB_so0zePYf8ko7kfnYnwsAqtu0F/s1600/Fast%20Curious_image.png)

Today’s *The Fast and the Curious* post covers how Chrome achieved best-in-class Speedometer scores on mobile devices, resulting in faster and smoother web experiences for Android users.

Chrome has always been about speed. Whether it's loading pages quickly, running complex web apps smoothly, or delivering a seamless browsing experience, performance is at the heart of our browser. And we're always looking for ways to make Chrome even faster.

Over the last two years, we have been hard at work on a number of **performance improvements for Android devices**. We're excited to share some of the progress we've made.

# Speedometer on Android

One of the key metrics we use to track Chrome's performance is the [Speedometer benchmark](https://browserbench.org/Speedometer3.0/). This benchmark is developed in collaboration with other major web browser engines and measures how quickly Chrome can complete interactions with web pages, including parsing/rendering HTML or CSS and running JavaScript.

Since the release of Chrome M112, we've seen a **significant increase in Speedometer 2.1 scores on Android devices [1]**. In fact, on many devices, scores more than doubled, with the newest Snapdragon® 8 Elite Mobile Platform setting new records for Speedometer performance on mobile devices! These huge accomplishments are a testament to the work not only of the Chrome and Android teams, but also our silicon and SoC partners.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7ULeiY7XhUwFlFUcyUnTZc8AorKMA5I5VhW3ENj7chwRB-Sgc_NQWPgNUBLnX7QhRIsBYH-THYueE-lg5hi4CVg_n-yrPvvCIUPXMmHagNT3Y9PpgID8nrwud7UAT5LMMkaHduXeylctnroj7aQHqOUefGucCKoW3MK6sfU1AsJshwEO2EMyfUkR1Vnm9/s1600/s2.1_rel.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7ULeiY7XhUwFlFUcyUnTZc8AorKMA5I5VhW3ENj7chwRB-Sgc_NQWPgNUBLnX7QhRIsBYH-THYueE-lg5hi4CVg_n-yrPvvCIUPXMmHagNT3Y9PpgID8nrwud7UAT5LMMkaHduXeylctnroj7aQHqOUefGucCKoW3MK6sfU1AsJshwEO2EMyfUkR1Vnm9/s1600/s2.1_rel.jpg)

Since Chrome M112, Speedometer 2.1 scores have more than doubled on many Android devices. [1]

# How Did We Do It?

The improvements resulted from several changes, including:

* **Build optimizations:** We've made a number of changes to the way Chrome is built, which has resulted in faster code execution tuned to modern premium Android devices and SoCs.
* **V8 and Blink improvements:** Many improvements to the JavaScript engine (V8) and the rendering engine (Blink) have further boosted performance.
* **Scheduling, OS and SoCs:** We worked closely with Android partners to optimize the way Chrome interacts with the operating system and its thread scheduling to make the best use of the silicon on the devices.

Let's take a closer look at each of these areas.

# Build optimizations

The Android device ecosystem is very diverse. From entry-level phones to the newest premium ones, Chrome needs to run well on all devices. Up until last year, we shipped the same Chrome build to all these different Android devices. The memory and disk size constraints on entry-level devices resulted in Chrome having to prioritize a small binary size. Consequently, many modern build optimizations were out of reach, as they resulted in much larger binaries.

With M113, Chrome was finally able to ship a **separate higher-performance build targeting premium Android devices** via the Google Play Store. While we still ship a more binary-size-constrained build to other devices, this approach allowed us to land some of those modern optimizations into the new premium build:

* By targeting 64-bit Arm instead of 32-bit Arm, we can make use of more efficient Arm instruction set features and larger 64-bit operations.
* Since binary size is less relevant on premium devices with large disks and sufficient memory, we can now compile C++ code [optimized for speed](https://chromium-review.googlesource.com/c/chromium/src/%2B/3936329) (-O2 / -O3) rather than size (-Oz).
* Furthermore, we tweaked the inlining thresholds used by the compiler to enable more inlining in hot code ([within](https://chromiumdash.appspot.com/commit/f5361ce9a99a600ec483e2694414d4fb638f1b6a) and [across modules](https://chromiumdash.appspot.com/commit/1cdd49ffd503bac5e6779d48503865bf5a5a0095)), while updating the model and policy used by another compiler pass (MLGO) to [reduce inlining in cold code](https://chromiumdash.appspot.com/commit/a181985aec42c2547b774cd0e1e8903bd0c797b4).
* We now also apply [profile-guided optimization](https://chromium.googlesource.com/chromium/src/%2B/refs/heads/main/docs/pgo.md) (PGO) techniques to the build to further improve the code layout and optimization level for hot code.
* Finally, we improved cross-function code ordering by aligning Chrome's [orderfile](https://chromium.googlesource.com/chromium/src/%2B/main/docs/orderfile.md) generation with the new 64-bit build. We also now [include Speedometer 3](https://chromiumdash.appspot.com/commit/1c90dc12223d10411b096a2fcda13b4a14e39ec2), the latest version of the industry-standard browser speed benchmark, in the workloads used to generate the orderfile.

Together, these build optimizations account for more than half of the overall Speedometer score improvements. This progress was facilitated by our collaboration with Arm, who contributed valuable insights and improvements, including to identify and address inefficiencies in Chrome's PGO setup and inlining.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDpBrRfRMVPKZIjnRSAo7Ea1Wsx00QrnL9VJQl7LEqMi3zWC7vLzfNlLY7tbNPjRzhhq44Yt7lxoY0sEA1OstCQKNcS3z6BWdmZpYxj-3UetcQtatu-4xusYX-LJ1sV76axpmvHvQ-dDVrOMJl4QK6tE1h_ACeK7WsWyduJXKZdkEccf7ng_WVEmygS59K/s1600/Screenshot%202024-12-04%202.03.43%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDpBrRfRMVPKZIjnRSAo7Ea1Wsx00QrnL9VJQl7LEqMi3zWC7vLzfNlLY7tbNPjRzhhq44Yt7lxoY0sEA1OstCQKNcS3z6BWdmZpYxj-3UetcQtatu-4xusYX-LJ1sV76axpmvHvQ-dDVrOMJl4QK6tE1h_ACeK7WsWyduJXKZdkEccf7ng_WVEmygS59K/s1600/Screenshot%202024-12-04%202.03.43%20PM.png)

# V8 and Blink improvements

Chrome continuously improves the performance of its JavaScript and web rendering engines, V8 and Blink. Most optimizations are small in individual impact, but stacked together, these improvements add up and contributed most of the remaining Speedometer impact! Notable ones include:

* We now utilize an [optimized fast-path HTML parser](https://chromiumdash.appspot.com/commit/dfbc1a660bbe3a219dbbd61365036009008188ad) to parse innerHTML attributes.
* V8 launched its *[Sparkplug](https://v8.dev/blog/sparkplug)* compiler tier, a super fast baseline compiler that sits right above its *Ignition* interpreter and generates non-optimized code very quickly. Later, V8 also launched *[Maglev](https://v8.dev/blog/maglev)*, a new mid-tier compiler that generates semi-optimized code. It takes longer to do so than Sparkplug, but much less time than *Turb...