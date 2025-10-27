---
title: Re-implementing my Linux Rust scheduler in eBPF
url: http://arighi.blogspot.com/2024/08/re-implementing-my-linux-rust-scheduler.html
source: arighi's blog
date: 2024-08-11
fetch_date: 2025-10-06T18:02:09.534728
---

# Re-implementing my Linux Rust scheduler in eBPF

# [arighi's blog](http://arighi.blogspot.com/)

## Saturday, August 10, 2024

### Re-implementing my Linux Rust scheduler in eBPF

## Overview

The main bottleneck of `scx_rustland`, a Linux scheduler
written in Rust, is the communication between kernel and user space.

Even if the communication itself has been improved a lot using ring
buffers (`BPF_MAP_TYPE_RINGBUF` /
`BPF_MAP_TYPE_USER_RINGBUF`) the multiple level of queues is
inevitably leading to the scheduler operating in a less work-conserving
way.

This has the double effect of making the vruntime-based scheduling
policy more effective (being able to accumulate more tasks and
prioritizing those that have more strict latency requirements), but the
queuing of tasks also has the downside of not using the CPUs at their
full capacity, potentially causing regressions in terms of
throughput.

To reduce this “bufferbloat” effect I have decided to re-implement
`scx_rustland` fully in BPF, getting rid of the user-space
overhead, and name this new scheduler `scx_bpfland`.

## Implementation

`scx_bpfland` uses the same logic as
`scx_rustland` for classifying interactive and regular tasks.
It identifies interactive tasks based on the average number of voluntary
context switches per second, classifying them as interactive when this
average surpasses a moving threshold. Additionally, tasks that are
explicitly awakened are immediately marked as interactive and remain so
unless their average voluntary context switches falls below the
threshold.

There are per-CPU queues that are used to directly dispatch tasks to
idle CPUs. If all CPUs are busy, tasks are either dispatched to a global
priority queue or a global regular queue (depending if a task has been
classified “interactive” or “regular”).

Tasks are then consumed from the per-CPU queues first, then from the
priority queue and lastly from the regular queue. This means that
regular tasks could be potentially starved by interactive tasks, so to
prevent indefinite starvation `scx_bpfland` has a “starvation
time threshold” parameter (configurable by command line) that forces the
scheduler to consume at least one task from the regular queue when the
threshold is exceeded.

Having a separate queue for the tasks classified as “interactive”
that is consumed before the global regular queue allows to immediately
process “interactive” events in an interrupt-like fashion.

Lastly, `scx_bpfland` assigns a variable time slice to
tasks, as a function of the amount of tasks waiting in the priority and
shared queues: the more tasks a waiting the shorter the time slice is.
This ensures that over a max time slice period all the queued tasks will
likely get a chance to run (depending on their priority and their
“interactiveness”).

## Testing

The logic of the scheduler is quite simple, but it proves to be quite
effective in practice. Of course it does not perform well in every
possible scenario, but the whole purpose of the scheduler is to be
extremely specialized to prioritize latency-sensitive workloads over
CPU-intensive workloads.

For this reason `scx_bpfland` *should not* be
considered a replacement for the default Linux scheduler (EEVDF), that
still remains the best choice in general.

However, in some special cases, where latency matters,
`scx_bpfland` can deliver an improved and consistent level of
responsiveness.

This run of a selection of tests from the [Phoronix Test Suite](https://www.phoronix-test-suite.com)
mostly aimed at measuring latency and response time shows some of the
benefits of the aggressive prioritizaton of interactive tasks performed
by `scx_bpfland`.

## Results

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLobDv8ZFnhw63MaKnxr1wkTB6c6E_0-61Ft-Rys2HjvYMBbopNHrOm6ef_3rVj_3Upc_0t3cJBAkteC5mw0c8GRdOG74cH6Eonz299I7bc7FkW15JeBmLhfvROswp-jf5iHBMGGhyphenhyphenVD9QtynlwBJUmu9hh4UKMkNomPmbMblIM3l-dK6b3lBoF3ml/s1600/bpfland-benchmark.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLobDv8ZFnhw63MaKnxr1wkTB6c6E_0-61Ft-Rys2HjvYMBbopNHrOm6ef_3rVj_3Upc_0t3cJBAkteC5mw0c8GRdOG74cH6Eonz299I7bc7FkW15JeBmLhfvROswp-jf5iHBMGGhyphenhyphenVD9QtynlwBJUmu9hh4UKMkNomPmbMblIM3l-dK6b3lBoF3ml/s1600/bpfland-benchmark.png)

Both PostgreSQL and Hackbench show a significant boost compared to
the default scheduler (up to 39% for read/write latency with
PostgreSQL), since their workload is purely latency bound.

FFMpeg also shows some improvements (9% with live-streaming and 7%
with the upload profile), mostly due to the fact that the workload is
not purely encoding, but there’s also message passing involved (in a
producer-consumer fashion).

nginx shows an improvement of 8.4%, also due to the fact that the
benchmark is mostly stressing short-lived connections (measuring
connection response time).

Apache, instead, shows a 9% performance regression with
`scx_bpfland`, compared to EEVDF.

Both the nginx and the Apache benchmarks rely on `wrk`, an
HTTP benchmarking tool with a multithreaded design and scalable event
notification systems via epoll and kqueue.

To better understand what is happening from a scheduler’s
perspective, we can look at the distribution of the runqueue latency
(the time a task spends waiting in the scheduler’s queue) of the clients
(wrk) in both scenarios during a 30s run period:

```
[nginx - EEVDF]

@usecs:
[1]                   21 |                                                    |
[2, 4)              1590 |@@@@                                                |
[4, 8)              6090 |@@@@@@@@@@@@@@@@@                                   |
[8, 16)            18371 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[16, 32)            7527 |@@@@@@@@@@@@@@@@@@@@@                               |
[32, 64)            8514 |@@@@@@@@@@@@@@@@@@@@@@@@                            |
[64, 128)           1915 |@@@@@                                               |
[128, 256)          1695 |@@@@                                                |
[256, 512)          2029 |@@@@@                                               |
[512, 1K)           2148 |@@@@@@                                              |
[1K, 2K)            2234 |@@@@@@                                              |
[2K, 4K)            2114 |@@@@@                                               |
[4K, 8K)            1729 |@@@@                                                |
[8K, 16K)           1274 |@@@                                                 |
[16K, 32K)           740 |@@                                                  |
[32K, 64K)           251 |                                                    |
[64K, 128K)           31 |                                                    |
[128K, 256K)           8 |                                                    |
[256K, 512K)           1 |                                                    |
[512K, 1M)             0 |                                                    |
[1M, 2M)               0 |                                                    |
[2M, 4M)               0 |                                                    |
[4M, 8M)               0 |                                                    |
[8M, 16M)              1 |                                                    |
[16M, 32M)             1 |                                                    |

Total samples: 58,284

[nginx - scx_bpfland]

@usecs:
[2, 4)              5552 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           |
[4, 8)              6944 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[8, 16)             5813 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         |
[16, 32)            4092 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      |
[32, 64)            2433 |@@@@@@@@@@@@@@@@@@                                  |
[64, 128)           1840 |@@@@@@@@@@@@@                                       |
[128, 256)          1867 |@@@@@@@@@@@@@                                       |
[256, 512)          2499 |@@@@@@@@@@@@@@@@@@  ...