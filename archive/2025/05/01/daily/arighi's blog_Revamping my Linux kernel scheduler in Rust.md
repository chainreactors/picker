---
title: Revamping my Linux kernel scheduler in Rust
url: http://arighi.blogspot.com/2025/05/revamping-my-linux-kernel-scheduler-in.html
source: arighi's blog
date: 2025-05-01
fetch_date: 2025-10-06T22:24:51.371749
---

# Revamping my Linux kernel scheduler in Rust

# [arighi's blog](http://arighi.blogspot.com/)

## Thursday, May 1, 2025

### Revamping my Linux kernel scheduler in Rust

## Recap

Some time ago, I built a kernel scheduler in Rust, called [scx\_rustland](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rustland).
It runs entirely in user space, powered by [sched\_ext](https://github.com/sched-ext/scx), a technology in
the Linux kernel that lets you write CPU schedulers as [BPF](https://www.kernel.org/doc/html/latest/bpf/index.html)
programs.

The original goal of my project was to create a proof-of-concept, a
working example to demonstrate the potential of user-space scheduling.
The ideas was to use sched\_ext and BPF to capture scheduling events in
the kernel and pass them to a Rust program in user space, which makes
decisions and dispatches tasks back to the kernel.

Surprisingly, even that early prototype outperformed the default
Linux scheduler, but only in a very specific scenario: testing the
responsiveness of a videogame under heavy system load. (You can see this
in action in this video, where I play [Terraria](https://github.com/sched-ext/scx/assets/1051723/42ec3bf2-9f1f-4403-80ab-bf5d66b7c2d5)
at 60fps while compiling the kernel in the background.)

Since then, the project has evolved significantly. One key
improvement was switching to BPF ringbuffers for the communication
between BPF and user space. This allowed lockless, syscall-free message
passing through shared memory between kernel and user space, eliminating
bottlenecks and making the scheduler more viable beyond just demos or
niche cases.

Eventually, part of this work grew into a framework:
scx\_rustland\_core, a Rust crate for building fully functional Linux
schedulers, designed to abstract away all the boilerplate and offering
an easy scheduling development playground.

The original Rust scheduler (scx\_rustland) was then completely
rewritten on top of this new framework.

## Tackling the overhead of user-space scheduling

One of the weaknesses of user-space scheduling is the overhead of the
BPF-to-user roundtrip. For user responsiveness focused workloads,
usually this isn’t a huge issue. But for more throughput-oriented
workloads, the “bubbles” in the scheduling pipeline, caused by
synchronizing BPF and the user-space scheduler, can be significant.

To address this, the scx\_rustland\_core scheduling pipeline has been
re-architected and improved.

Now when a task releases a CPU, we check if there are other tasks
that want to run and we always “append” the user-space scheduler itself
at the end of the queue. In this way tasks can pile in and the scheduler
can process them in “bursts” making its prioritization logic more
effective. If there’s no pending action to be processed, the CPU can go
idle, but right before entering the actual idle state, we
opportunistically check for pending tasks again and immediately wakeup
the user-space scheduler if needed.

This tighter scheduling loop reduced latency and maximized CPU
utilization, as we can see in following trace, collected during a
parallel kernel build and visualised using [Perfetto](https://perfetto.dev/):

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk00GIg2dDxJABnJuH1qVmD6qNyJH142n6hgjNyy-k5HSsN2rW282wOiJA31Oy4sVz9L58jUklzNkLzMQbV2emMyGfqExEA-B7dUdT7NRsvJJwRl9jgNCs9dvShoLyX8ptMgHKUtgmfk416GKOuLBaBDHCrcfXmQA8KBXi2RKcp6VJuh2g6oAIy2Jl/s600/rustland-perfetto.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk00GIg2dDxJABnJuH1qVmD6qNyJH142n6hgjNyy-k5HSsN2rW282wOiJA31Oy4sVz9L58jUklzNkLzMQbV2emMyGfqExEA-B7dUdT7NRsvJJwRl9jgNCs9dvShoLyX8ptMgHKUtgmfk416GKOuLBaBDHCrcfXmQA8KBXi2RKcp6VJuh2g6oAIy2Jl/s1029/rustland-perfetto.png)

In the trace, you can see how the older rustland version introduced
~60us gaps between tasks across all the CPUs. The new version virtually
eliminates those bubbles (there are only rare ~5us gaps just before the
user-space scheduler itself runs).

Another improvement was handling task wakeups directly in BPF: now,
when a task wakes up and idle CPUs are available, the BPF code picks a nearby
CPU (preferably the one it previously ran on) and dispatches it immediately,
bypassing the user-space roundtrip entirely. This fast path improves
both latency and throughput performance.

The runqueue design of scx\_rustland\_core has also been improved a
bit, even if scx\_rustland is still using a global runqueue, which works
well for small-to-medium systems and allows perfect load balancing.
However, on large systems with multiple cores,
this can become a bottleneck due to contention (I’m planning to improve
this in the future introducing per-NUMA or per-LLC runqueues and provide
a proper API, so that other schedulers based on scx\_rustland\_core can use
such topology-aware runqueues).

## Benchmarking the Improvements

To evaluate the new improvements, I ran a subset of benchmarks from
the [Phoronix Test
Suite](https://www.phoronix-test-suite.com/), ranging from throughput-oriented workloads, such as kernel
builds and LLM inference to more latency-oriented workloads, such as
schbench, nginx and PostgreSQL.

### Test system

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRcw7di4fW4KXLFvN0PZA04d3TRWsA9LmRwMe6D_D_BH001LTfNfkAI1k0hK1VFbNlvSizDVMl6xE-NY-6E2n4Pk-qZjaaoqCxh0qh9993OLrJP8P_-1lcvT2URkFvvcU_tUlqEfHd8mayr4MF2SL6Up19kv7qlbkBZgfUyNEY7lHTaJmFuwW6ei_e/s600/hardware.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRcw7di4fW4KXLFvN0PZA04d3TRWsA9LmRwMe6D_D_BH001LTfNfkAI1k0hK1VFbNlvSizDVMl6xE-NY-6E2n4Pk-qZjaaoqCxh0qh9993OLrJP8P_-1lcvT2URkFvvcU_tUlqEfHd8mayr4MF2SL6Up19kv7qlbkBZgfUyNEY7lHTaJmFuwW6ei_e/s576/hardware.png)

### Old vs new scx\_rustland

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgR5MovalpXPJ1Mj32nCNiFSEFZrr9r0vpcp2SX03HE5OpSBusgBoCObsIW-UXCQhFsB0n16kdihfJ9_28sxN9xYnjPhVX-_8MK4gt0e1QtWy2DpYMq2RKFumZgiSkua2onf7wvzkWsKVLFPXfQqrIWG7DKNjd3zY_UEJeYBsrxaAa3_aavJwjBvuMR/s600/rustland-old-vs-rustland.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgR5MovalpXPJ1Mj32nCNiFSEFZrr9r0vpcp2SX03HE5OpSBusgBoCObsIW-UXCQhFsB0n16kdihfJ9_28sxN9xYnjPhVX-_8MK4gt0e1QtWy2DpYMq2RKFumZgiSkua2onf7wvzkWsKVLFPXfQqrIWG7DKNjd3zY_UEJeYBsrxaAa3_aavJwjBvuMR/s846/rustland-old-vs-rustland.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSU1BHlBgqskeIlSdviPEJxxZnE4P1t4wa3lcJIqT3Hqn7ODbTJrGM1N9JRetz4YvYDajvR1p0sdQ4dzQggdjMgToAfFi1hskDFNlp1KB_feq0CpYgBs-aAND2miuNJLBOqrWP993Y8NjD9WD2hUDM082RE88r-40twIzeydrmmDL8pe9UqgZEZBX4/s600/rustland-old-vs-rustland-score.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSU1BHlBgqskeIlSdviPEJxxZnE4P1t4wa3lcJIqT3Hqn7ODbTJrGM1N9JRetz4YvYDajvR1p0sdQ4dzQggdjMgToAfFi1hskDFNlp1KB_feq0CpYgBs-aAND2miuNJLBOqrWP993Y8NjD9WD2hUDM082RE88r-40twIzeydrmmDL8pe9UqgZEZBX4/s582/rustland-old-vs-rustland-score.png)

Notable results: nginx: +77% in requests/sec, PostgreSQL: +26% in
transactions/sec, schbench (99.9th latency) going from 9ms -> 3.4ms.
These significant gains highlight the effect of a more efficient
scheduling pipeline and better BPF/user-space synchronization.

### scx\_rustland vs EEVDF

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdLJC5hg_1gAB_NPeFyMayNzXtYr1fyD0UDDU1Qg5JPKavgcY4u6dYRZiaI2E4ZVEbWBbaJwEcx4hFpONp1H60z9WDxM5fp9331OHZCeagr3Lv1TIPj49Z6ZIssFm7cEVS_Lx40S9lD4bBbOug8ZAq-eFdxhDxItQRoFHYpNGqEx5HwbzRQFguR0Ds/s600/eevdf-vs-rustland.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdLJC5hg_1gAB_NPeFyMayNzXtYr1fyD0UDDU1Qg5JPKavgcY4u6dYRZiaI2E4ZVEbWBbaJwEcx4hFpONp1H60z9WDxM5fp9331OHZCeagr3Lv1TIPj49Z6ZIssFm7cEVS_Lx40S9lD4bBbOug8ZAq-eFdxhDxItQRoFHYpNGqEx5HwbzRQFguR0Ds/s842/eevdf-vs-rustland.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXG8tSb5KPJELS0U0PHZpZSrXZLpfQpOCAPDJtf68-QNNGNkeLEluq8Ou_Gp692PjpCmd5rLJVbV1J79VmBdyxQt3C6yPh8uT3pgTw52NuqQV0xqaCPnWX7m6Fj4lC5XP2uOv60Q3Chw6Zwp6gTefGPKzkc-QcGAP_Iwg2w9sNJkXd5n0uKWQbv1_R/s600/eevdf-vs-rustland-score.png)](https://bl...