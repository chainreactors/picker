---
title: Accelerating micro-VM boot time with sched_ext
url: http://arighi.blogspot.com/2025/01/accelerating-micro-vm-boot-time-with.html
source: arighi's blog
date: 2025-01-19
fetch_date: 2025-10-06T20:08:11.030965
---

# Accelerating micro-VM boot time with sched_ext

# [arighi's blog](http://arighi.blogspot.com/)

## Saturday, January 18, 2025

### Accelerating micro-VM boot time with sched\_ext

## Overview

Booting short-lived virtual machines (VMs) can be a highly
CPU-intensive workload. In scenarios like serverless computing, where
booting and stopping a short-lived micro-VM is a common operation,
improving the single start/stop time can provide significant benefits.

This article shows the results of experiments using
`sched_ext` to accelerate the start/stop of a micro-VM,
by changing the scheduling policy on the hypervisor.

## Booting a VM

When booting a micro-VM, multiple tasks are spawned and distributed
across all the available CPUs (depending on how many vCPUs are assigned
to the guest). The workload is typically a high bursty CPU activity,
that occurs in short spikes, followed by periods of lower usage.

Unlike long-running workloads, which benefit from keeping tasks on
the same CPU to maximize cache locality, the boot process doesn’t
exhibit significant working set reuse. As a result, a scheduling policy
that is too conservative with migrations, where tasks tend to stay on
the same CPU, may be less effective in this scenario.

## Maximize core utilization

In this scenario the most effective strategy is to maximize core
utilization, without worrying too much about cache locality.

Therefore, a more effective scheduling policy would be to allow tasks
to migrate to idle CPUs as soon as their current CPU becomes busy, while
still keeping track of their “original” CPU and attempting to return
them there, preserving, in this way, cache locality for the tasks that
may still require it.

Moreover, using a single shared runqueue helps maximize core
utilization, making the scheduler more work-conserving.

## Using `sched_ext` to design a custom scheduling policy

`sched_ext` is a technology in the Linux kernel that
allows to implement scheduling policies as BPF program, that can be
loaded at runtime, without rebooting the kernel.

This helps designing and testing specialized scheduling policies,
providing rapid experimentation with quick turnarounds between tests,
all while ensuring safety, since BPF can’t crash the kernel.

The scheduling ideas described above have been implemented in
a modified version of [`scx_bpfland`](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_bpfland).

## Test case

The test case uses [virtme-ng](https://github.com/arighi/virtme-ng):
a tool commonly used for automating kernel testing in CI/CD environments.

The test consists in running a simple "`vng -r -- uname -r`",
which boots a micro-VM using the current host's kernel, executes the
`uname -r` command and then exits. This test aims to simulate
a very short-lived VM that runs a basic command before terminating.

## Results and Observations

The modified bpfland scheduler delivered the following results:

```
 +------------------------+------------------+----------+---------+
 | Scheduler              | Boot Time (avg)  |   stdev  | speedup |
 +------------------------+------------------+----------+---------+
 | EEVDF (default Linux)  |      1.437s      |   0.064  |    -    |
 | bpfland                |      1.295s      |   0.013  |  1.11   |
 +------------------------+------------------+----------+---------+
```

The speedup achieved by bpfland is approximately 1.11x, meaning that
bpfland reduced the micro-VM boot time by about 11% compared to the
default Linux scheduler. This improvement is notable not only in terms of
a faster average boot time, but also in its consistency across multiple
runs, with bpfland showing also a lower standard deviation.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5nJ467kkag7VcAlbYV4aUc42HSuKulTOTTbS2uEhtbIRFQY1VBVU-M3W1sCmNoi4kBaiT68Bx_Jt4P5rOzDawHbytxvdjf-6bA-uAFRompfnnmCWQGDhVv_EHn_cTN4FAdvZUNQaEQH0VOHq4zw88WMtT-fWQDNCV23XrakS800VcVthLT6ccA_mP/s600/vm-boot-time.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5nJ467kkag7VcAlbYV4aUc42HSuKulTOTTbS2uEhtbIRFQY1VBVU-M3W1sCmNoi4kBaiT68Bx_Jt4P5rOzDawHbytxvdjf-6bA-uAFRompfnnmCWQGDhVv_EHn_cTN4FAdvZUNQaEQH0VOHq4zw88WMtT-fWQDNCV23XrakS800VcVthLT6ccA_mP/s2000/vm-boot-time.png)

By examining the following scheduling traces (visualized in [Perfetto](https://perfetto.dev/)), we can observe that in the
bpfland case (second diagram), tasks tend to migrate more, maximizing
core utilization. In contrast, the first diagram shows that tasks tend
to remain a bit more on their CPU, before migrating.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjB1CLW725xyRHKbLJeTAFJd4C8Csw7BWcRoGGgzxX6p7FT_-M0rRi1pPZiMfpbmvhd6vo0tpGt1ZGIngRiOOxREXngRUPszM6If03rKrWHEzgcFSvLU4I7GmpkOcBmvi0k01m3f8ONKeHoVryC0mpa56Lorzpeitm3C-PjTrOlNuujF41Kh351Dsor/s600/eevdf-vs-bpfland.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjB1CLW725xyRHKbLJeTAFJd4C8Csw7BWcRoGGgzxX6p7FT_-M0rRi1pPZiMfpbmvhd6vo0tpGt1ZGIngRiOOxREXngRUPszM6If03rKrWHEzgcFSvLU4I7GmpkOcBmvi0k01m3f8ONKeHoVryC0mpa56Lorzpeitm3C-PjTrOlNuujF41Kh351Dsor/s1243/eevdf-vs-bpfland.png)

## Conclusion and future ideas

The goal of this experiment was to showcase the flexibility of
`sched_ext` and highlight the benefits of rapid
experimentation. By analyzing a specific workload, it was possible to
quickly conceptualize, design, and test a custom scheduler, specifically
crafted to enhance performance for a particular use case, all within a
very short time frame.

In a (not too) far future, we may even have an automated way
(possibly driven by an AI?) to analyze scheduling traces, generate
customized scheduling policies, test them and select the most suitable
one for the current system workload. However, we’re not quite there
yet…

Posted by

[arighi](https://www.blogger.com/profile/15223521151492879497 "author profile")

at
[10:39 PM](http://arighi.blogspot.com/2025/01/accelerating-micro-vm-boot-time-with.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4397409626710913610&postID=7200779736631781329&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=7200779736631781329&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=7200779736631781329&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=7200779736631781329&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=7200779736631781329&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=7200779736631781329&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4397409626710913610/7200779736631781329)

[Newer Post](http://arighi.blogspot.com/2025/02/ubuntu-2504-is-now-schedext-ready.html "Newer Post")

[Older Post](http://arighi.blogspot.com/2024/09/ai-generated-linux-kernel-schedulers-in.html "Older Post")
[Home](http://arighi.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://arighi.blogspot.com/feeds/7200779736631781329/comments/default)

## Blog Archive

* [May](http://arighi.blogspot.com/2025/05/) (1)
* [February](http://arighi.blogspot.com/2025/02/) (1)
* [January](http://arighi.blogspot.com/2025/01/) (1)
* [September](http://arighi.blogspot.com/2024/09/) (1)
* [August](http://arighi.blogspot.com/2024/08/) (1)
* [May](http://arighi.blogspot.com/2024/05/) (1)
* [April](http://arighi.blogspot.com/2024/04/) (1)
* [March](http://arighi.blogspot.com/2024/03/) (1)
* [February](http://arighi.blogspot.com/2024/02/) (1)
* [July](http://arighi.blogspot.com/2023/07/) (1)
* [August](http://arighi.blogspot.com/2019/08/) (1)
* [December](http://arighi.blogspot.com/2018/12/) (1)
* [August](http://arighi.blogspot.com/2013/08/) (1)
* [May](http://arighi.blogspot.com...