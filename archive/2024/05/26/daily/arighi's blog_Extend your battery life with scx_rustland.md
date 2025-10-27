---
title: Extend your battery life with scx_rustland
url: http://arighi.blogspot.com/2024/05/extend-your-battery-life-with.html
source: arighi's blog
date: 2024-05-26
fetch_date: 2025-10-06T16:49:19.360200
---

# Extend your battery life with scx_rustland

# [arighi's blog](http://arighi.blogspot.com/)

## Saturday, May 25, 2024

### Extend your battery life with scx\_rustland

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlUQ8IRIzR7COIaGUGw4MbJEishEeTdJy7XMq1OX0C1xC4PVU8IQmkvuDfb565ICO0Zo6oH6-43lg8J2a0njQ3j5mWQuN688intxzYMLfcov-eQczIQJ6Qo3EZjUiFDMhMGnrAJ-MQYVTEL9Y07NMyHDbeg7fnUU3v1cyS2YCvmwXtiW4EWy2GfJCr/s400/power.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlUQ8IRIzR7COIaGUGw4MbJEishEeTdJy7XMq1OX0C1xC4PVU8IQmkvuDfb565ICO0Zo6oH6-43lg8J2a0njQ3j5mWQuN688intxzYMLfcov-eQczIQJ6Qo3EZjUiFDMhMGnrAJ-MQYVTEL9Y07NMyHDbeg7fnUU3v1cyS2YCvmwXtiW4EWy2GfJCr/s844/power.png)

## Overview

The CPU scheduler can play a significant role to save energy in the
system. Typically we talk about Energy Aware Scheduling (EAS) when
scehduling decisions can impact on the energy consumed by the CPUs. EAS
relies on an Energy Model (EM) of the CPUs to select the most energy
efficient CPU for each task, with a minimal impact on throughput.

Effective energy-saving techniques can also be applied by maximizing
the idle time of the CPUs. Modern CPUs’ power consumption is heavily
influenced by how long they remain idle, sometimes yielding more
significant energy savings than Dynamic Voltage and Frequency Scaling
(DVFS) techniques (e.g., the cpufreq governor).

## Forcing CPUs to stay idle

The scheduler can force specific CPUs to stay idle by not assigning
tasks to them. However, it is essential to find a good balance between
energy savings and performance. For example, a drastic solution could be
scheduling all tasks on a single CPU while keeping others idle. This can
save energy in emergency situations, such as when a battery-powered
device is nearly out of power, but it can severely degrades the overall
system performance.

## Energy saving with `scx_rustland`

[scx\_rustland](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rustland)
uses a very simple, yet effective, strategy to save energy: when a CPU
enters an idle state, it attempts to keep it idle if other CPUs are
active, even if there are tasks queued for scheduling.

Since `scx_rustland` uses a vruntime-based policy,
latency-sensitive tasks are likely placed at the top of the queue. Thus,
active CPUs can quickly dispatch these tasks, maintaining system
responsiveness. CPU-intensive tasks, on the other hand, will spend more
time in the scheduler queue, waiting for an active CPU.

This approach reduces overall system throughput by intentionally
introducing bubbles in the scheduling, but it helps save power without
compromising system responsiveness.

Of course the overall throughput in the system is strongly reduced
(CPUs are explicitly under-utilized), but the “CPU throttling” is mostly
affecting background CPU-intensive tasks.

For this reason, this strategy is disabled by default and it can be
enabled starting the scheduler with the `--low-power`
option.

## Implementation

The implementation of this strategy is also very simple, technically
just a [one-liner](https://github.com/sched-ext/scx/blob/main/rust/scx_rustland_core/assets/bpf/main.bpf.c#L787).

All the logic is implemented in the
`rustland_update_idle()` callback, that is executed when a
CPU changes its idle state:

```
/*
 * A CPU is about to change its idle state.
 */
void BPF_STRUCT_OPS(rustland_update_idle, s32 cpu, bool idle)
{
    /*
     * Don't do anything if we exit from and idle state, a CPU owner will
     * be assigned in .running().
     */
    if (!idle)
        return;
    /*
     * A CPU is now available, notify the user-space scheduler that tasks
     * can be dispatched.
     */
    if (usersched_has_pending_tasks()) {
        set_usersched_needed();
        /*
         * Wake up the idle CPU, so that it can immediately accept
         * dispatched tasks.
         */
        if (!low_power || !nr_running)
            scx_bpf_kick_cpu(cpu, 0);
    }
}
```

In low-power mode the key part is:

```
...
    if (usersched_has_pending_tasks()) {
...
        /*
         * Wake up the idle CPU, so that it can immediately accept
         * dispatched tasks.
         */
        if (!low_power || !nr_running)
            scx_bpf_kick_cpu(cpu, 0);
    }
...
```

The variable `nr_running` keeps track of the active CPUs
and `scx_bpf_kick_cpu()` is used, in this context, to
immediately wake up a CPU when it enters an idle state.

In general immediately waking up the CPU at this point would be
totally reasonable if there are still tasks that are waiting to be
scheduled (see the `usersched_has_pending_tasks()` check a
few lines above).

However, in a “low power” scenario we can avoid to immediately wake
up the CPU, if other CPUs are active (`nr_running != 0`), in
order to maximize the idle state effectiveness and save power at the
cost of throttling CPU-intensive tasks even more.

## Result

The benefits of the low-power mode can be illustrated with the
following test case:

* play a video game (Terraria) while recompiling the kernel
* measure game performance (fps) and core power consumption (W)
* compare the result of normal mode vs low-power mode

Results:

```
                      Game performance | Power consumption |
         ------------+-----------------+-------------------+
         normal mode |          60 fps |               6W  |
      low-power mode |          60 fps |               3W  |
```

As we can see from these results, the game performance were pretty
much unaffected by the low-power mode, while the CPU consumption is cut
in half.

Real-world tests showed around 20-30% increase in laptop battery life
using `scx_rustland` in low-power mode with typical workloads
like reading emails, web browsing, listening to music, and compiling
code.

## Conclusion

This experiment highlights the ease and effectiveness of using
`sched_ext` and `scx_rustland` for kernel
scheduling development.

The ability to quickly edit-compile-run kernel scheduling changes
represents a significant improvement over traditional methods that
require kernel recompilation and rebooting, with potential for
catastrophic results in case of bugs.

The simplicity of the code change also demonstrates how easy it can
be to implement and test theories aimed at improving performance,
responsiveness, or energy savings. Moreover, operating in user-space
(remember that `scx_rustland` performs 100% of the scheduling
decisions in user-space) can be particularly advantageous for debugging
and profiling.

## Future development

While the described technique for energy saving is simple and
effective, there is room for improvement.

For instance, incorporating topology awareness could make the
low-power mode less aggressive in keeping CPUs idle. Avoiding idle
states for CPUs in the same core as an active CPU, for example, could
minimize unnecessary throttling of CPU-intensive tasks while
maintaining, potentially, the same level of energy savings.

Posted by

[arighi](https://www.blogger.com/profile/15223521151492879497 "author profile")

at
[7:48 PM](http://arighi.blogspot.com/2024/05/extend-your-battery-life-with.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4397409626710913610&postID=1658548608697488006&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=1658548608697488006&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=1658548608697488006&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=1658548608697488006&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=1658548608697488006&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=1658548608697488006&target=pinterest "Share to Pinterest")

#### ...