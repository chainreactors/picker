---
title: Introducing Skia Graphite: Chrome's rasterization backend for the future
url: http://blog.chromium.org/2025/07/introducing-skia-graphite-chromes.html
source: Chromium Blog
date: 2025-07-09
fetch_date: 2025-10-06T23:28:39.514334
---

# Introducing Skia Graphite: Chrome's rasterization backend for the future

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Introducing Skia Graphite: Chrome's rasterization backend for the future](https://blog.chromium.org/2025/07/introducing-skia-graphite-chromes.html "Introducing Skia Graphite: Chrome's rasterization backend for the future")

Tuesday, July 8, 2025

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_oXM-_56tbxbRYQxIunAhz47yN-RJHgS4FSb4wnuyaBN5amMkmRSGXu9oWoQ9apIB-DOl1RRi69mwcOLlV2EaD8HBjBPFg0p1dud7HStcmzIRYa3wwq11BjsKOeC_pUykrZMSJvsl2RlCQktC0xw28TpBnEbqBJxev7D-ZFHVBt20bshdN6wLtogSN6MG/s1600/Fast%20Curious_image%20%281%29.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_oXM-_56tbxbRYQxIunAhz47yN-RJHgS4FSb4wnuyaBN5amMkmRSGXu9oWoQ9apIB-DOl1RRi69mwcOLlV2EaD8HBjBPFg0p1dud7HStcmzIRYa3wwq11BjsKOeC_pUykrZMSJvsl2RlCQktC0xw28TpBnEbqBJxev7D-ZFHVBt20bshdN6wLtogSN6MG/s1600/Fast%20Curious_image%20%281%29.png)

*Today's The Fast and the Curious post covers the launch of Skia's new rasterization backend, Graphite, in Chrome on Apple Silicon Macs. Graphite is instrumental in helping Chrome achieve exceptional scores on Motionmark 1.3 and is key to unlocking a ton of future improvements in Chrome Graphics.*

# A brief history of Skia in Chrome

In Chrome, Skia is used to render paint commands from Blink and the browser UI into pixels on your screen, a process called rasterization. Skia has powered Chrome Graphics [since the very beginning](https://www.google.com/url?q=https://blog.chromium.org/2008/10/graphics-in-google-chrome.html&sa=D&source=docs&ust=1744655288075052&usg=AOvVaw2iZg3ILJvcyGeG8RDYzVNv). Skia eventually ran into performance issues as the web evolved and became more complex, which led Chrome and Skia to invest in a GPU accelerated rasterization backend called Ganesh.

Over the years, Ganesh matured into a solid highly performant rasterization backend and GPU rasterization launched on all platforms in Chrome on top of GL (via ANGLE on Windows D3D9/11). However, Ganesh always had a GL-centric design with too many specialized code paths and the team was hitting a wall when trying to implement optimizations that took advantage of modern graphics APIs in a principled manner.

This set the stage for the team to rethink GPU rasterization from the ground up in the form of a new rasterization backend, Graphite. Graphite was developed from the start to be principled by having fewer and more comprehensible code paths. This forward looking design helps take advantage of modern graphics APIs like Metal, Vulkan and D3D12 and paradigms like compute based path rasterization, and is multithreaded by default.

# Results

With Graphite in Chrome, we increased our Motionmark 1.3 scores by almost 15% on a Macbook Pro M3. At the same time, we improved real world metrics like INP (interaction to next paint time), LCP (time to largest contentful paint), graphics smoothness (percent dropped frames), GPU process malloc memory usage, and others. This all means substantially smoother interactions, less stutter when scrolling, and less time waiting for sites to show.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK7OcoGT0p5zxAfiA30b8wcjhxDlovG2IUL3DNsazr0NBYBK-yoizvfdjng-6jOXE_T4hEGGGR6D3MsytJj6qkFkjS8Fjs8PjYHbHvCljY6fwmpMUIalNFg4QRp2fpFolLIQJmwar4IrhBtgbzuyhh7zRMbSv_rHSsDBycZ0G0SDn53owruvmmkgqTs9qr/s1600/Screenshot%202025-07-08%20at%2012.40.51%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK7OcoGT0p5zxAfiA30b8wcjhxDlovG2IUL3DNsazr0NBYBK-yoizvfdjng-6jOXE_T4hEGGGR6D3MsytJj6qkFkjS8Fjs8PjYHbHvCljY6fwmpMUIalNFg4QRp2fpFolLIQJmwar4IrhBtgbzuyhh7zRMbSv_rHSsDBycZ0G0SDn53owruvmmkgqTs9qr/s1600/Screenshot%202025-07-08%20at%2012.40.51%E2%80%AFPM.png)

# Differences between Graphite and Ganesh

### Modern graphics APIs

Ganesh was originally implemented on OpenGL ES, which had minimal support for multi-threading or GPU capabilities like compute shaders. Since then, modern graphics APIs like Vulkan, Metal and D3D12 have evolved to take advantage of multithreading and expose new GPU capabilities. They allow applications to have much more control over when and how expensive work such as allocating GPU resources is performed and scheduled, while utilizing both the CPU and the GPU effectively.

While we were able to adapt Ganesh to support modern graphics APIs, it had accumulated enough technical debt that it became hard to fully take advantage of the multi-threading and GPU compute capabilities of modern graphics APIs.

For Graphite in Chrome, we chose to use Chrome's WebGPU implementation, [Dawn](https://dawn.googlesource.com/dawn), as the abstraction layer for platform native graphics APIs like Metal, Vulkan and D3D. Dawn provides a baseline for capabilities common in modern graphics APIs and helps us reduce the long term maintenance burden by leveraging Dawn's mature well tested native backends instead of implementing them from scratch for Graphite.

### 2D depth(?!) testing

A core part of the GPU rendering pipeline is depth testing, which can reduce or eliminate overdraw by drawing opaque objects in front to back order, followed by translucent objects back to front. In graphics, "overdraw" refers to the unnecessary rendering of the same pixels multiple times, which can negatively impact performance and battery life, especially on mobile devices.

Ganesh never utilized the depth testing capabilities of graphics cards, which was admittedly intended for rendering 3D content and not accelerating 2D graphics. Ganesh suffers from overdraw due to its reliance on adhering to strict painters order when drawing both opaque and translucent objects.

Graphite extends Skia’s GPU rendering to take advantage of the depth test by assigning each “draw” a *z* value defining its painter’s ordering index. While transparent effects and images must still be drawn from back to front, opaque objects in the foreground can now automatically eliminate overdraw. This means opaque draws can be re-ordered to minimize expensive GPU state changes while relying on the depth buffer to produce correct output.

Depth testing is also used to implement clipping in Graphite by treating clip shapes as depth only draws as opposed to maintaining a clip stack like in Ganesh. Besides reducing algorithmic complexity, a significant benefit to this approach is that the shader program required to render a “draw” does not also depend on the state of the clip stack.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJvgOlBS_vrfP7D7vbi9seLOrlsKLhSWmuo6Lc6RiHIjvm23kjXT7zNM_iFS_ojrEowtoLhvSaCgDeoSWlwFWDH5vyqE23zhLCjPPrs6fLVTiGWw-os-ErUrz3VicU1r_Za-A4tRzyeW1BrVmqz8sgK7QLNMK27eB2u7lPeX1Kb9O4o-6y3bNzRZi9z3VZ/s1600/Screenshot%202025-07-08%20at%2012.42.02%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJvgOlBS_vrfP7D7vbi9seLOrlsKLhSWmuo6Lc6RiHIjvm23kjXT7zNM_iFS_ojrEowtoLhvSaCgDeoSWlwFWDH5vyqE23zhLCjPPrs6fLVTiGWw-os-ErUrz3VicU1r_Za-A4tRzyeW1BrVmqz8sgK7QLNMK27eB2u7lPeX1Kb9O4o-6y3bNzRZi9z3VZ/s1600/Screenshot%202025-07-08%20at%2012.42.02%E2%80%AFPM.png)

Left: Frame from Motionmark Suits Right: Depth buffer for the same frame.

### Multithreading

Chromium is a complex multi-process application, with render processes issuing commands to a shared GPU process that is responsible for actually displaying everything in a webpage, tab, and even the browser UI. The GPU process main thread is the primary driver of all rendering work and is where all GPU commands are issued.

Due to the single threaded nature of Ganesh and OpenGL, only a limited set of work could be moved to other threads, making it easy to overload the main thread causing increased jank and latency ultimately hurting user experience.

In contrast, Graphite's API...