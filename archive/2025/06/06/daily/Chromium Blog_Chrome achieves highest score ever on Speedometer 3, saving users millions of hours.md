---
title: Chrome achieves highest score ever on Speedometer 3, saving users millions of hours
url: http://blog.chromium.org/2025/06/chrome-achieves-highest-score-ever-on.html
source: Chromium Blog
date: 2025-06-06
fetch_date: 2025-10-06T22:51:54.563288
---

# Chrome achieves highest score ever on Speedometer 3, saving users millions of hours

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Chrome achieves highest score ever on Speedometer 3.1, saving users millions of hours](https://blog.chromium.org/2025/06/chrome-achieves-highest-score-ever-on.html "Chrome achieves highest score ever on Speedometer 3.1, saving users millions of hours")

Thursday, June 5, 2025

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7ibRIFh6_fd8s7ZyAA5Itvhk0OXNyAoVEfC_ctfRXwjGWIcRw-HBETVHqY9IFeZKJwkXj0uE2YsV27pJEjrIJkJkZDCK9Xhp38_jwg4inqSv360AChaT2R7my7jigmtLVeL79pawHZY9AX4HA9LyQ22VmOF-eVi2vjMIZdO61356_4AQu_xjWn7_BAyQz/s1600/Fast%20Curious_image.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7ibRIFh6_fd8s7ZyAA5Itvhk0OXNyAoVEfC_ctfRXwjGWIcRw-HBETVHqY9IFeZKJwkXj0uE2YsV27pJEjrIJkJkZDCK9Xhp38_jwg4inqSv360AChaT2R7my7jigmtLVeL79pawHZY9AX4HA9LyQ22VmOF-eVi2vjMIZdO61356_4AQu_xjWn7_BAyQz/s1600/Fast%20Curious_image.png)

*Update (6/10/2025): This blog was updated to reflect that testing was done using the Speedometer 3.1 benchmark, and resulted in a 22% performance improvement. The previous version incorrectly noted that the performance improvement was 10% and that the benchmark was Speedometer 3.*

Performance has always been one of the core pillars of Chrome and it’s something we’ve never stopped investing in. Publicly available and open benchmarks, which we create in open collaboration with other browsers, are useful tools for tracking our overall progress, understanding new areas of improvement, and validating potential optimizations. In today’s [The Fast and the Curious](https://blog.chromium.org/search/label/the%20fast%20and%20the%20curious) post, we’d like to go through Chrome’s recent work that enabled it to achieve the highest score ever on the Speedometer benchmark.

For Speedometer, these optimizations have resulted in a 22% improvement since August 2024. That 22% improvement leads to better browser experiences, higher conversions for businesses, and deeper enjoyment of what the web has to offer. If each Chrome user used Chrome for just 10 minutes a day, these improvements collectively save 116 million hours or roughly 166 lifetimes worth of waiting around for websites to load and do things.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNBzs94FRWaVl6_LwIzhqoAu5BQUjRUfMIeqPIW6f6hsKFlYw0yHAmXDAHvfOnNFgZc-XtC857Hwk4xAGNM2aYvZC4N7DAUdcWCTQzufE5tTV-pL2FesiTsL91_2aHaF7dCcEMmKjdwxe2rH2HumPUl_ZgAwmXROWUnokDtNiUkxsHaLXYCzptr-dZ7PJK/s1600/Screenshot%202025-06-10%20at%2012.24.01%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNBzs94FRWaVl6_LwIzhqoAu5BQUjRUfMIeqPIW6f6hsKFlYw0yHAmXDAHvfOnNFgZc-XtC857Hwk4xAGNM2aYvZC4N7DAUdcWCTQzufE5tTV-pL2FesiTsL91_2aHaF7dCcEMmKjdwxe2rH2HumPUl_ZgAwmXROWUnokDtNiUkxsHaLXYCzptr-dZ7PJK/s1600/Screenshot%202025-06-10%20at%2012.24.01%E2%80%AFPM.png)

Speedometer 3.1 score measured on Apple Macbook Pro M4 with MacOS 15

Speedometer is a benchmark created in open collaboration with other browsers and measures web application responsiveness through workloads that cover a large variety of different areas of the Blink rendering engine used in Chrome:

* HTML parsing
* JavaScript and JSON processing
* JavaScript and Document Object Model (DOM) interaction
* DOM manipulations (element insertion and removal)
* Text size computation (font shaping)
* Cascading Style Sheet (CSS) application and layout calculation
* Pixel rendering

In essence, Speedometer tests critical components of the entire rendering pipeline. For a deeper dive into these individual parts, we recommend the presentation [Life of a Script at Chrome University](https://www.youtube.com/watch?v=K2QHdgAKP-s).

Achieving exceptional web performance requires a multifaceted approach, and optimizing for Speedometer is a testament to overall product excellence. Over the past year, our team has focused on refining fundamental rendering paths across the entire stack. Here are some notable optimization examples.

The team heavily optimized memory layouts of many internal data structures across DOM, CSS, layout, and painting components. Blink now avoids a lot of useless churn on system memory by keeping state where it belongs with respect to access patterns, maximizing utilization of CPU caches. Where internal memory was already relying on garbage collection in Oilpan, e.g. DOM, the usage was expanded by converting types from using malloc to Oilpan. This generally speeds up the affected areas as it packs memory nicely in Oilpan’s backend.

Strings in the renderer improved quite a bit over the last year by avoiding costly representations where possible and switching hashing to rapidhash. More generally, lots of data structures were equipped with better hashes, filters, and probing algorithms.

Where rendering becomes inherently expensive, e.g., for computing CSS styles across various elements, caches are now used much more effectively with better hit rates. At the same time we cache fewer things that are not relevant. Another area where rendering becomes expensive is font shaping; the team significantly improved [Apple Advanced Typography](https://en.wikipedia.org/wiki/Apple_Advanced_Typography) font shaping performance which is relevant everywhere text is rendered.

Posted by Thomas Nattestad

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

[**](https://blog.chromium.org/)

[**](https://blog.chromium.org/2025/07/introducing-skia-graphite-chromes.html "Newer Post")

[**](https://blog.chromium.org/2025/05/fighting-unwanted-notifications-with.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [$200K](https://blog.chromium.org/search/label/%24200K)

  1
* [10th birthday](https://blog.chromium.org/search/label/10th%20birthday)

  4
* [abusive ads](https://blog.chromium.org/search/label/abusive%20ads)

  1
* [abusive notifications](https://blog.chromium.org/search/label/abusive%20notifications)

  2
* [accessibility](https://blog.chromium.org/search/label/accessibility)

  3
* [ad blockers](https://blog.chromium.org/search/label/ad%20blockers)

  1
* [ad blocking](https://blog.chromium.org/search/label/ad%20blocking)

  2
* [advanced capabilities](https://blog.chromium.org/search/label/advanced%20capabilities)

  1
* [android](https://blog.chromium.org/search/label/android)

  2
* [anti abuse](https://blog.chromium.org/search/label/anti%20abuse)

  1
* [anti-deception](https://blog.chromium.org/search/label/anti-deception)

  1
* [background periodic sync](https://blog.chromium.org/search/label/background%20periodic%20sync)

  1
* [badging](https://blog.chromium.org/search/label/badging)

  1
* [benchmarks](https://blog.chromium.org/search/label/benchmarks)

  1
* [beta](https://blog.chromium.org/search/label/beta)

  83
* [better ads standards](https://blog.chromium.org/search/label/better%20ads%20standards)

  1
* [billing](https://blog.chromium.org/search/label/billing)

  1
* [birthday](https://blog.chromium.org/search/label/birthday)

  4
* [blink](https://blog.chromium.org/search/label/blink)

  2
* [browser](https://blog.chromium.org/search/label/browser)

  2
* [browser interoperability](https://blog.chromium.org/search/label/browser%20interoperability)

  1
* [bundles](https://blog.chromium.org/search/label/bundles)

  1
* [capabilities](https://blog.chromium.org/search/label/capabilities)

  6
* [capable web](https://blog.chromium.org/search/label/capable%20web)

  1
* [cds](https://blog.chromium.org/search/label/cds)

  1
* [cds18](https://blog.chromium.org/se...