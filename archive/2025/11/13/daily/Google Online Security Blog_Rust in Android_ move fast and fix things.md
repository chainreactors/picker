---
title: Rust in Android: move fast and fix things
url: http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html
source: Google Online Security Blog
date: 2025-11-13
fetch_date: 2025-11-14T03:12:29.259890
---

# Rust in Android: move fast and fix things

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Rust in Android: move fast and fix things](https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html "Rust in Android: move fast and fix things")

November 13, 2025

Posted by Jeff Vander Stoep, Android

[Last year, we wrote](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html) about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how **this approach isn’t just fixing things, but helping us move faster**.

The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vulnerabilities for the first time.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjROV8ZUdZiVSj1rnMTi-vP1Dg7mBFBM2FkHYgIm8qwzvgYFfDd7Jl4P5EhrvQse9UC9o5WQSREZBgBBIsVeQqHmXJwLoXTJqkzjlmKD8W5oAoZJ0YWQSibsNLUxJrHOM9bQ_h2mQJqIlZdKJiofA8m8xCO2QukDD1RtRgJ853N4YNXYlVnl02R1hLV8zgK/s1600/image2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjROV8ZUdZiVSj1rnMTi-vP1Dg7mBFBM2FkHYgIm8qwzvgYFfDd7Jl4P5EhrvQse9UC9o5WQSREZBgBBIsVeQqHmXJwLoXTJqkzjlmKD8W5oAoZJ0YWQSibsNLUxJrHOM9bQ_h2mQJqIlZdKJiofA8m8xCO2QukDD1RtRgJ853N4YNXYlVnl02R1hLV8zgK/s1600/image2.png)

*Updated data for 2025. This data covers first-party and third-party (open source) code changes to the Android platform across C, C++, Java, Kotlin, and Rust. This post is published a couple of months before the end of 2025, but Android’s industry-standard 90-day patch window means that these results are very likely close to final. We can and will accelerate patching when necessary.*

We adopted Rust for its security and are seeing **a 1000x reduction in memory safety vulnerability density compared to Android’s C and C++ code**. But the biggest surprise was Rust's impact on software delivery. With Rust changes having **a 4x lower rollback rate** and spending **25% less time in code review**, the safer path is now also the faster one.

In this post, we dig into the data behind this shift and also cover:

* **How we’re expanding our reach:** We're pushing to make secure code the default across our entire software stack. We have updates on Rust adoption in first-party apps, the Linux kernel, and firmware.
* **Our first rust memory safety vulnerability...almost:** We'll analyze a near-miss memory safety bug in unsafe Rust: how it happened, how it was mitigated, and steps we're taking to prevent recurrence. It’s also a good chance to answer the question “if Rust can have memory safety issues, why bother at all?”

# Building Better Software, Faster

Developing an operating system requires the low-level control and predictability of systems programming languages like C, C++, and Rust. While Java and Kotlin are important for Android platform development, their role is complementary to the systems languages rather than interchangeable. [We introduced Rust into Android](https://security.googleblog.com/2021/04/rust-in-android-platform.html) as a direct alternative to C and C++, offering a similar level of control but without many of their risks. We focus this analysis on new and actively developed code because our data shows this to be [an effective approach](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html).

When we look at development in systems languages (excluding Java and Kotlin), two trends emerge: a steep rise in Rust usage and a slower but steady decline in new C++.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-MWhK4zEb7DBnAO8eF3DRxQ-T7p_LCkl7qApGBxda2fiHroOHwMQYlIfYHsZLakB6XiyOynkJbTVShIXe5pzqw7VXcZSAzflS7PyzUrM_8ZUVXOgudYo9bmgvhA7CVACfh5OS0wfOHbBczW_poHUfI8lngMWiuLs9Z5I0arQ-Z_e7WBzgSzOCUSHymx7Z/s1600/image1%20%281%29.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-MWhK4zEb7DBnAO8eF3DRxQ-T7p_LCkl7qApGBxda2fiHroOHwMQYlIfYHsZLakB6XiyOynkJbTVShIXe5pzqw7VXcZSAzflS7PyzUrM_8ZUVXOgudYo9bmgvhA7CVACfh5OS0wfOHbBczW_poHUfI8lngMWiuLs9Z5I0arQ-Z_e7WBzgSzOCUSHymx7Z/s1600/image1%20%281%29.png)

*Net lines of code added: Rust vs. C++, first-party Android code.
This chart focuses on first-party (Google-developed) code (unlike the previous chart that included all first-party and third-party code in Android.) We only include systems languages, C/C++ (which is primarily C++), and Rust.*

The chart shows that the volume of new Rust code now rivals that of C++, enabling reliable comparisons of software development process metrics. To measure this, we use the DORA[1](#fn1) framework, a decade-long research program that has become the industry standard for evaluating software engineering team performance. [DORA metrics](https://dora.dev/guides/dora-metrics-four-keys/) focus on:

* Throughput: the velocity of delivering software changes.
* Stability: the quality of those changes.

Cross-language comparisons can be challenging. We use several techniques to ensure the comparisons are reliable.

* Similar sized changes: Rust and C++ have similar functionality density, though Rust is slightly denser. This difference favors C++, but the comparison is still valid. We use [Gerrit’s change size definitions](https://issues.gerritcodereview.com/issues/40007892).
* Similar developer pools: We only consider first-party changes from Android platform developers. Most are software engineers at Google, and there is considerable overlap between pools with many contributing in both.
* Track trends over time: As Rust adoption increases, are metrics changing steadily, accelerating the pace, or reverting to the mean?

## Throughput

Code review is a time-consuming and high-latency part of the development process. Reworking code is a primary source of these costly delays. Data shows that Rust code requires fewer revisions. This trend has been consistent since 2023. Rust changes of a similar size need about 20% fewer revisions than their C++ counterparts.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisLm7jCyRVHZIyKf4awb-HpBwUdYAFui-tdFR9IqyyMN-OcdC91wsriqWRMsyTKtceUN3sGwe1DfcvFJliEH98ps2yq42sAAPGQFKtJ446pYENZK55x6AECT480e0lSTRZLkgLdRYvd-CT1cw1uXidOjw_aOJPDalbapWiL-lK8MjRGhqtduhTFINxT4AZ/s1600/image3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisLm7jCyRVHZIyKf4awb-HpBwUdYAFui-tdFR9IqyyMN-OcdC91wsriqWRMsyTKtceUN3sGwe1DfcvFJliEH98ps2yq42sAAPGQFKtJ446pYENZK55x6AECT480e0lSTRZLkgLdRYvd-CT1cw1uXidOjw_aOJPDalbapWiL-lK8MjRGhqtduhTFINxT4AZ/s1600/image3.png)

In addition, Rust changes currently spend about 25% less time in code review compared to C++. We speculate that the significant change in favor of Rust between 2023 and 2024 is due to increased Rust expertise on the Android team.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwkwkwfieBcBdcnJ1hyphenhyphenzN3YpbKpZgklKmySAgHablV87Y8zxx5JKuq1bHmMeoKGtFSKdVmttH2aUOgIyn424lKNF8z8BENijo9r687GGPF6k227fnj4eMQ4RTSqLTCysgLAli84iAI9TV6RxUwETfgLfGdsQL0BApI6QQpU_QsZ7Jb4HjBdxNosz3qS3W2/s1600/image4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwkwkwfieBcBdcnJ1hyphenhyphenzN3YpbKpZgklKmySAgHablV87Y8zxx5JKuq1bHmMeoKGtFSKdVmttH2aUOgIyn424lKNF8z8BENijo9r687GGPF6k227fnj4eMQ4RTSqLTCysgLAli84iAI9TV6RxUwETfgLfGdsQL0BApI6QQpU_QsZ7Jb4HjBdxNosz3qS3W2/s1600/image4.png)

While less rework and faster code reviews offer modest productivity gains, the most significant improvements are in the stability and quality of the changes.

## Stability

Stable and high-quality changes differentiate Rust. DORA uses rollback rate for evaluating change stability. Rust's rollback rate is very low and continues to decrease, even as its adoption in Android surpasses C++.

[![...