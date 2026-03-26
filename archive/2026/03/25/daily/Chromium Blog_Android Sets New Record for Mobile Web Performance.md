---
title: Android Sets New Record for Mobile Web Performance
url: http://blog.chromium.org/2026/03/android-sets-new-record-for-mobile-web.html
source: Chromium Blog
date: 2026-03-25
fetch_date: 2026-03-26T04:30:14.999987
---

# Android Sets New Record for Mobile Web Performance

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Android Sets New Record for Mobile Web Performance](https://blog.chromium.org/2026/03/android-sets-new-record-for-mobile-web.html "Android Sets New Record for Mobile Web Performance")

Wednesday, March 25, 2026

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1ID1ntGdw8mqTRlNGoEgDtJ9v6XC82v4G-WYeBFCIR7Tbq3A-UVpP9nxFryuS8mZsIkEL2HSurSzyRNbk1MFuUWK6CpbvZog1m5yiWVbaffWrHP9o4OrQelfTVNPvwcERw0kSbL7K7JgSWazLwcFfosxwmM3_V5l1cWbOUE1_mKIdr-HnzSr2VbahAy72/s1600/Screenshot%202026-03-24%20at%2010.58.02%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1ID1ntGdw8mqTRlNGoEgDtJ9v6XC82v4G-WYeBFCIR7Tbq3A-UVpP9nxFryuS8mZsIkEL2HSurSzyRNbk1MFuUWK6CpbvZog1m5yiWVbaffWrHP9o4OrQelfTVNPvwcERw0kSbL7K7JgSWazLwcFfosxwmM3_V5l1cWbOUE1_mKIdr-HnzSr2VbahAy72/s1600/Screenshot%202026-03-24%20at%2010.58.02%E2%80%AFAM.png)

A core part of the Android experience is the web. Whether you are browsing in Chrome or using one of the >90% of Android apps that utilize WebView, the speed of the web defines the speed of your phone. Today, we are proud to celebrate a major milestone: **Android is now the fastest mobile platform for web browsing.**

Through deep vertical integration across hardware, the Android OS, and the Chrome engine, the latest flagship Android devices are setting new performance records, outperforming all other mobile competitors in the key web performance benchmarks Speedometer and LoadLine and providing a level of responsiveness previously unseen on mobile.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoFmTNXcCKkGA3F2RDhRsjKH0dSVPB0tto857cyOzyOi6H8Cn5X2O2UH_8RJ4K8ejkfOroe4nLv66u6H8nQBT0CNEC9Ly58lBsv7umA0PLkRhCy9aufhXAssbOPsmoWEMcvKzydxY7XoIB17-DOAXjyHK53-X9d0THQqSXW1uDsBn-nw1syUivYeyIIYLv/s1600/score-chart.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoFmTNXcCKkGA3F2RDhRsjKH0dSVPB0tto857cyOzyOi6H8Cn5X2O2UH_8RJ4K8ejkfOroe4nLv66u6H8nQBT0CNEC9Ly58lBsv7umA0PLkRhCy9aufhXAssbOPsmoWEMcvKzydxY7XoIB17-DOAXjyHK53-X9d0THQqSXW1uDsBn-nw1syUivYeyIIYLv/s1600/score-chart.png)

Android flagship phones reach new high-scores in
web performance benchmarks (Chrome 146, March 2026)

### Why web performance matters

Web performance isn't just about high scores—it’s about how your device feels every day. On Android, web content and its performance is central to the user experience.

Whether searching for information, catching up on the latest news, or online-shopping, Android users spend a significant portion of their daily screen time interacting with web content. Chrome is one of the most popular Android apps in the US and worldwide. Furthermore, this usage increases sharply on tablets and foldables, where productivity use cases are key.

While the web is clearly important, a great web experience necessitates a fast browser and device: Modern websites are highly complex, with more than 200 million active sites serving everything from blog posts with dynamic ad auctions to desktop-class productivity tools. This complexity makes for a demanding workload that can stress even powerful devices.

To ensure a high-quality user experience, we focus on two critical pillars when evaluating web performance: **responsiveness** and **page load speed**.

### Speedometer: Measuring web responsiveness

**[Speedometer](https://browserbench.org/Speedometer3.1/)** is the collaborative industry standard used by all major browser engine developers to measure web app responsiveness. It simulates real-world user actions—like adding items to a to-do list—to measure interaction latency.

While synthetic, Speedometer's workloads offer high consistency and are built using relevant, state-of-the-art web frameworks, such as React, Angular or jQuery, and include to-do apps, text editors, chart rendering, and a mock news portal.

Speedometer scores have a strong correlation (-0.8) with 99th-percentile interaction latency (INP) in the field. Thus, a higher Speedometer score directly translates to a more fluid, snappy feeling when you tap, scroll, or type on a website.

### LoadLine: Measuring the complete page load

While interaction responsiveness is vital, it’s only half of the story. Users also care about how fast a page appears after they click a link. To measure this, Chrome and Android teams worked with Android SoC and OEM partners to develop **[LoadLine](https://chromium.googlesource.com/crossbench/%2B/refs/heads/main/config/benchmark/loadline2/)**, an emerging end-to-end benchmark that simulates the complete process of loading a website.

Where traditional benchmarks often focus on synthetic tasks, LoadLine uses recorded, stable versions of select **real-world websites**. This includes simpler and more complex sites with varied characteristics, reflecting the most important types of mobile web content, such as shopping, search, and news portals.

LoadLine has proven that Android's page load performance is world-class: Top tier Android phones score up to 47% higher than non-Android competitors. And this matters: LoadLine scores also correlate well (-0.8) with median and high-percentile page load latency in the field.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpyiDHC_oGrj_rfEPNRG0oveFID-onA60JeyQ3oHGCgpnb-bphc3UAg0eCsOt0kQZlI863IdYlNYy2PsIcfshBgsRp2srGZQ5aCvWjrSFhO9j02ReVz7uTaouRLbb_dnHBWO-Pt39hSn7uq_gD4oSbxVV99ql-yn27G5mAWn1L4FmcnHy4204FCQLfOb3b/s1600/speedometer_loadline_optimized.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpyiDHC_oGrj_rfEPNRG0oveFID-onA60JeyQ3oHGCgpnb-bphc3UAg0eCsOt0kQZlI863IdYlNYy2PsIcfshBgsRp2srGZQ5aCvWjrSFhO9j02ReVz7uTaouRLbb_dnHBWO-Pt39hSn7uq_gD4oSbxVV99ql-yn27G5mAWn1L4FmcnHy4204FCQLfOb3b/s1600/speedometer_loadline_optimized.gif)

Speedometer (left) and examples of LoadLine workloads (right)

### Success through vertical optimization

Android’s current lead is the result of a concerted effort to tune the entire "stack"—from silicon to software.

We encouraged our Android partners to evaluate and tune their devices against Speedometer and LoadLine. While advances in SoCs' core performance build the foundation for fast web experiences, tuning of the OS and browser software stack are critical to utilize the hardware effectively. Collaborating with select SoC and OEM partners, we utilized Speedometer and LoadLine to optimize Chrome and kernel scheduler policies.

As a result of these improvements, some Android flagship phones improved their Speedometer and LoadLine scores by 20-60% year-over-year, compared to their respective predecessor models. And these improvements translate to faster real-world web performance: Today, page loads are 4-6% faster and high-percentile interactions 6-9% faster on these newer models, for real users in the field.

We invite all developers and hardware partners to join us in using these benchmarks to push the boundaries of what’s possible on the mobile web.

Posted by Eric Seckler, software engineer, Chrome

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

Labels:

[the fast and the curious](https://blog.chromium.org/search/label/the%20fast%20and%20the%20curious)

[**](https://blog.chromium.org/)
**

[**](https://blog.chromium.org/2026/03/bringing-chrome-to-arm64-linux-devices.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [$200K](https://blog.chromium.org/search/label/%24200K)

  1
* [10th birthday](https://blog.chromium.org/search/label/10th%20birthday)

  4
* [abusive ads](https://blog.c...