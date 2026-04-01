---
title: JetStream 3: A modern benchmark for high-performance, compute-intensive Web applications
url: http://blog.chromium.org/2026/03/jetstream-3-a-modern-benchmark.html
source: Chromium Blog
date: 2026-03-31
fetch_date: 2026-04-01T04:45:15.584300
---

# JetStream 3: A modern benchmark for high-performance, compute-intensive Web applications

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [JetStream 3: A modern benchmark for high-performance, compute-intensive Web applications](https://blog.chromium.org/2026/03/jetstream-3-a-modern-benchmark.html "JetStream 3: A modern benchmark for high-performance, compute-intensive Web applications")

Tuesday, March 31, 2026

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7mETepavttUoY0pDjkUG5z7WnmZPQRhUlQkPGWzY5afsHga0ExOpY1FIELBAIq3Ssfv7PJFdtvFIfmj4azUAEpalCw3vROcJyGfoJR-FZo_eRMAwKVYgUuFZNb5ixovknfmtUA7t860UmjYGctEumZvbcgGggl6MRDPqSRzenKHxH-px617F2H7Au53PL/s1600/Screenshot%202026-03-31%20at%201.26.23%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7mETepavttUoY0pDjkUG5z7WnmZPQRhUlQkPGWzY5afsHga0ExOpY1FIELBAIq3Ssfv7PJFdtvFIfmj4azUAEpalCw3vROcJyGfoJR-FZo_eRMAwKVYgUuFZNb5ixovknfmtUA7t860UmjYGctEumZvbcgGggl6MRDPqSRzenKHxH-px617F2H7Au53PL/s1600/Screenshot%202026-03-31%20at%201.26.23%E2%80%AFPM.png)

We’re incredibly excited to announce the release of JetStream 3, built in close collaboration with Apple, Mozilla, and other partners in the web ecosystem!

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheAHzDj95eAsg7G6hUGoXG1GX6HMnDUKXUmEMtoRy79QenUNyjOWKLaU5JxR72MkLs8A7IStrhBIt3r938XLUAHUY6A8vOo0Txxy6JevLwl8ifF5l-ME0_PqFSCFrTWeSuePS4z0zCHtPc3VMRltID7duvbF45AHOqRovrKXLwnd6XQNtgto894ZlnZ7sR/s1600/Screenshot%202026-03-31%20at%2010.30.35%E2%80%AFAM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheAHzDj95eAsg7G6hUGoXG1GX6HMnDUKXUmEMtoRy79QenUNyjOWKLaU5JxR72MkLs8A7IStrhBIt3r938XLUAHUY6A8vOo0Txxy6JevLwl8ifF5l-ME0_PqFSCFrTWeSuePS4z0zCHtPc3VMRltID7duvbF45AHOqRovrKXLwnd6XQNtgto894ZlnZ7sR/s1600/Screenshot%202026-03-31%20at%2010.30.35%E2%80%AFAM.png)

While we’ve covered the high-level details of this release in our [shared announcement blog post](https://browserbench.org/announcements/jetstream3/), we wanted to take a moment here to dive a little deeper. In this post, we’ll pull back the curtain on the benchmark itself, explore the methodology behind our choices, and share the motivations driving these major updates.

---

### **Why Do We Benchmark, Anyway?**

Before we get into the "what," it helps to talk about the "why." Why do browser engineers care so much about benchmarks?

At its core, benchmarking serves as a critical safety net for catching performance regressions before they ever reach users. But beyond that, benchmarks act as a powerful motivation function—a sort of "gamification" for browser engineers. Having a clear target helps us prioritize our efforts and decide exactly which optimizations deserve our focus. It also drives healthy competitiveness between different browser engines, which ultimately lifts the entire web ecosystem.

Of course, the ultimate goal isn't just to make a number on a chart go up; it's to meaningfully improve user experience and real-world performance.

### **Driven by Open Governance**

Just like Speedometer 3, JetStream 3 is the result of a massive [collaborative effort](https://github.com/WebKit/Jetstream) across all major browser engines, including Apple, Mozilla, and Google.

We adopted a strict consensus model for this release. This means we only added new workloads when everyone agreed they were valuable and representative. This open governance model has led to an incredibly productive collaboration with buy-in from multiple parties, ensuring the benchmark serves the best interests of the overall Web ecosystem.

### **Ripe for an Update**

The last major release, JetStream 2, came out in 2019. In the technology space—and especially on the Web—six years is an eternity.

There's a well-known concept in economics called Goodhart's Law, which states that when a measure becomes a target, it ceases to be a good measure. Over time, engines naturally optimize for the specific patterns of a benchmark, and the metrics slowly lose their correlation with real-world performance. Speedometer recently received a massive update to account for this, and it only makes sense that JetStream is next in line.

### **JetStream vs. Other Benchmarks**

You might be wondering: with the recent release of [Speedometer 3](https://blog.chromium.org/2024/03/speedometer-3-building-benchmark-that.html), why do we need another benchmark?

While Speedometer is fantastic for measuring UI rendering and DOM manipulation, JetStream has a different focus: the computationally intensive parts of Web applications. We're talking about use cases like browser-based games, physics simulations, framework cores, cryptography, and complex algorithms.

There are also practical engineering considerations. JetStream is designed so that it can run in engine shells—like `d8`, the standalone shell for V8. For engine developers, this is a massive advantage. Building a shell is significantly quicker than compiling a full browser like Chrome, allowing engineers to iterate faster. Because `d8` is single-process, it also produces far less background noise, leading to more stable testing. This shell-compatibility also makes JetStream highly valuable for hardware and device vendors running simulators. It is a trade-off—a shell is slightly further removed from a full, real-world browser environment—but the engineering velocity it unlocks is well worth it.

### **How We Select Workloads**

Building a benchmark requires a delicate balance between microbenchmarks and real applications.

Microbenchmarks are great engineering tools; they have a high signal-to-noise ratio and make it easy to see the effects of one specific optimization. While they make sense for early improvements of new features, they also often encourage overfitting in the long run. Engines might optimize heavily for a tiny loop that looks great on the benchmark but does absolutely nothing to help real users.

Because of this, a primary criterion for inclusion in JetStream 3 is that a workload should represent a real, end-to-end use case (or at least a highly abstracted form of one).

We also heavily prioritized diversity. We don’t want workloads that all exercise the exact same hot loop. We want coverage across different frameworks, varied libraries, diverse source languages, and distinct toolchains.

Finally, we had to lay down some practical ground rules:

* **Time:** The full benchmark suite needs to complete in a few minutes.
* **Memory:** It shouldn't consume so much RAM that it crashes low-end devices.
* **Network:** It shouldn't require massive payload transfers.
* **Consistency:** Results should be deterministic and repeatable from one run to the next.

---

### **Rethinking WebAssembly**

One of the most significant shifts in JetStream 3 is an increased focus and major update with regards to WebAssembly (Wasm).

When JetStream 2 was created, Wasm was still in its infancy. Fast forward to today, and Wasm is significantly more widespread.

Because the language has evolved so rapidly, JetStream 2 became outdated quickly. It only tested the Wasm MVP (Minimum Viable Product). Today, the Wasm spec includes powerful features like [SIMD](https://en.wikipedia.org/wiki/Single_instruction%2C_multiple_data) (single instruction, multiple data), [WasmGC](https://developer.chrome.com/blog/wasmgc), and Exception Handling—none of which were being properly benchmarked.

The ecosystem of tools has also completely transformed. The old workloads relied almost entirely on ancient versions of Emscripten compiling C/C++, often utilizing the deprecated `asm.js` backend via `asm2wasm`. Furthermore, some of the old microbenchmarks mis-incentivized the wrong optimizations. For example, the old `HashSet-wasm` workload rewarded aggressive inlining that actually *hurt* performance in real-world u...