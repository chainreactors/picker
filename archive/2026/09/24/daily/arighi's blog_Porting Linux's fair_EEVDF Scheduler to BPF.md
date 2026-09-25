---
title: Porting Linux's fair/EEVDF Scheduler to BPF
url: http://arighi.blogspot.com/2026/09/porting-linuxs-faireevdf-scheduler-to.html
source: arighi's blog
date: 2026-09-24
fetch_date: 2026-09-25T06:51:52.213734
---

# Porting Linux's fair/EEVDF Scheduler to BPF

# [arighi's blog](http://arighi.blogspot.com/)

## Thursday, September 24, 2026

### Porting Linux's fair/EEVDF Scheduler to BPF

I've recently started a new hobby project: re-implementing the Linux fair/EEVDF scheduler 100% in BPF using sched\_ext. The main goal is not to replace the scheduler, it is to make the existing scheduler easier to experiment with, understand it and better document how it works.

The source code of the first prototype (`scx_eevdf`) is available here:
<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_eevdf>

## Why?

Suppose you have an idea for a small change to CPU scheduling policy: perhaps a different wakeup heuristic, a different way of selecting the next task, or a new load-balancing rule. Today, there are essentially two ways to experiment with it.

The first is to modify the kernel scheduler itself, rebuild the kernel, reboot, and repeat for every iteration. The second is to write a sched\_ext scheduler from scratch. That's much faster to build and test, but you first have to reimplement everything that isn't part of your idea.
Both approaches are expensive enough that many potentially interesting ideas never get tested.

What we're missing is a third option: a way to experiment with small changes to the default scheduler through sched\_ext, without having to reimplement everything from scratch, while retaining the fast edit-build-test cycle that sched\_ext provides.

That's the idea behind `scx_eevdf`. Instead of starting with a blank scheduler, start with something that looks as much as possible like the scheduler already running in the kernel. Then experiment with the parts that actually matter. If an idea turns out to be useful, it can eventually make its way back into the upstream scheduler.

## How it was built

The port was built with the help of LLMs, using an incremental approach: the upstream scheduler (`kernel/sched/fair.c`) was decomposed into small self-contained building blocks and ported one block at a time. For each block, I asked the agent to translate the implementation to BPF. Then I manually:

1. reviewed the generated code against the kernel source;
2. tested it with focused benchmarks;
3. used tracing to validate the expected behavior;
4. accepted, rejected, or modified the result before moving on to the next block.

Then I repeated the process, block by block. In other words, the models did most of the mechanical translation; I did the decomposition, review, validation, and accept/reject decisions. This turned out to be a really effective way of tackling a port of this size.

## What's in it?

At the time of writing, a very rough estimate of around **80% of the fair/EEVDF logic** is implemented in `scx_eevf`. It currently includes:

* **EEVDF core:** virtual deadlines, the per-runqueue reference `V`, lag across sleeps, reweighting, delayed dequeue, relative deadlines, and runtime accounting
* **Eligible-task selection:** backed by per-CPU eligible deadline queues (EDQ)
* **Preemption:** `PREEMPT_SHORT` short-request preemption and slice enforcement from the tick
* **Wakeup placement:** `wake_affine()`, idle search with the `SIS_UTIL` budget, and `SCHED_IDLE`-aware targets
* **Load balancing:** periodic and new-idle balancing, capacity-normalized averaged load, `sd->imbalance_pct`, one elected balancer per group, capacity-pressure estimation, and misfit handling
* **Utilization tracking:** PELT-equivalent utilization (ravg), including feeding utilization information to the cpufreq governor
* **cgroups:** cgroup scheduling with `cpu.weight` and `cpu.max` bandwidth control
* **Asymmetric CPUs:** capacity awareness and packing for hybrid CPUs

## What's missing?

Two major pieces are currently absent:

* **NUMA balancing.** There is no page-fault sampling, preferred-node tracking, or task grouping. Placement is topology-aware, but blind to where a task's memory actually lives.
* **EAS.** There is no energy model or equivalent of `find_energy_efficient_cpu()`. CPU selection currently relies on capacity and idleness.

There are also a few pieces that cannot currently be implemented because the required interfaces do not exist in sched\_ext yet. I'll come back to those later.

## Does it actually behave like EEVDF?

I compared `scx_eevdf` against the kernel's own fair/EEVDF scheduler on the same machine:

* Intel Core i7-13800H
* 20 logical CPUs: 12 P-core threads + 8 E-cores
* one NUMA node
* one LLC
* Linux 7.2

The results below are medians from five runs. The arm order was rotated on every iteration so thermal drift could not consistently favor one scheduler. Every sample waited for a quiet pre-window and recorded system-wide busy ticks during its measured window. This also makes it possible to identify noisy samples afterwards rather than silently averaging them away.

For each number, the `+-` value is the half-range across the five samples. For example, `95 +-27%` means that the five samples spanned 54% of the median.

The final column indicates whether `scx_eevdf` was better (`^`), worse (`v`), or whether the sample ranges overlapped (`~`).

```
+----------------------------------+-------+----------------+----------------+----+
|Metric                            |Unit   |      fair/EEVDF|       scx_eevdf|    |
+==================================+=======+================+================+====+
| schbench latency                                                                |
|  light load  - wakeup p50        |us     |        71 +-16%|        95 +-27%| ~  |
|  light load  - wakeup p90        |us     |       149 +-17%|       181 +-10%| ~  |
|  light load  - request p50       |us     |       4328 +-0%|      4712 +-26%| v  |
|  light load  - request p99       |us     |     13,264 +-6%|     18,016 +-0%| v  |
|  saturated   - wakeup p50        |us     |       106 +-25%|        81 +-75%| ~  |
|  saturated   - wakeup p90        |us     |    24,352 +-50%|    12,176 +-37%| ^  |
|  saturated   - request p50       |us     |    16,240 +-15%|     12,432 +-9%| ^  |
|  saturated   - request p99       |us     |    198,400 +-5%|   203,008 +-11%| ~  |
| scheduling latency (stress-ng --cyclic)                                         |
|  idle machine - p50              |ns     |       6458 +-1%|       5744 +-0%| ^  |
|  idle machine - p90              |ns     |       6697 +-2%|       5915 +-1%| ^  |
|  idle machine - p99              |ns     |       9082 +-7%|       9659 +-5%| ~  |
|  vs 20 hogs   - p50              |ns     |      2333 +-12%|      2461 +-15%| ~  |
|  vs 20 hogs   - p90              |ns     |      2643 +-13%|      2825 +-15%| ~  |
|  vs 20 hogs   - p99              |ns     |       3161 +-9%|      3399 +-11%| ~  |
| throughput                                                                      |
|  perf bench sched messaging -t   |s      |      0.260 +-0%|     0.264 +-1%| v  |
|  perf bench sched messaging -p   |s      |      1.000 +-1%|     0.894 +-3%| ^  |
|  perf bench sched pipe           |ops/s  |    578,640 +-6%|   431,181 +-12%| v  |
|  schbench -L pinned, rps         |rps    |  1,628,689 +-0%| 1,616,687 +-0%| v  |
|  stress-ng --cpu 20              |bogo/s |     28,856 +-1%|    28,743 +-1%| ~  |
|  stress-ng --sock 8              |bogo/s |     15,867 +-1%|    16,418 +-1%| ^  |
|  stress-ng --msg 8               |bogo/s | 15,136,274 +-0%|15,134,700 +-1%| ~  |
|  stress-ng --futex 8             |bogo/s |   480,751 +-31%|  519,239 +-68%| ~  |
| cost of identical delivered work (schbench held at 1000 rps)                    |
|  system CPU busy                 |%      |      45.80 +-3%|    43.28 +-2%| ^  |
|  package power                   |W      |      24.32 +-4%|    23.61 +-1%| ~  |
| power (schedutil, intel_pstate passive)                                         |
|  idle                            |W      |       2.13 +-5%|     1.95 +-6%| ~  |
|  wakeup storm, 50k rps           |W      |       2.99 +-2%|     2.90 +-4%| ~  |
|  full load, first 6 s            |W      |      6...