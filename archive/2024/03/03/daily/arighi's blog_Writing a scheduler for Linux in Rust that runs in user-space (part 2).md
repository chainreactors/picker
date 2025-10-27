---
title: Writing a scheduler for Linux in Rust that runs in user-space (part 2)
url: http://arighi.blogspot.com/2024/03/writing-scheduler-for-linux-in-rust.html
source: arighi's blog
date: 2024-03-03
fetch_date: 2025-10-04T12:08:08.303263
---

# Writing a scheduler for Linux in Rust that runs in user-space (part 2)

# [arighi's blog](http://arighi.blogspot.com/)

## Saturday, March 2, 2024

### Writing a scheduler for Linux in Rust that runs in user-space (part 2)

In the [first
part](https://arighi.blogspot.com/2024/02/writing-scheduler-for-linux-in-rust.html) of this series we covered the basic implementation details of
`scx_rustland`: a fully-functional Linux scheduler written in
Rust that runs in user space.

If having a Linux scheduler that run in user-space wasn’t enough, we
can push the concept even further and consider the possibility to evolve
this project into a **generic framework** that allows to
implement any scheduling policy in user-space, using Rust.

The primary advantage of such a framework would lie in significantly
lowering the bar of scheduling development. Using this framework,
developers could just focus solely on crafting the scheduling policy,
without delving into complex kernel internal details. This would make
scheduling development and testing really accessible to a broader
audience.

Moreover, as already mentioned in part 1, operating in user-space
provides access to a plethora of tools, libraries, debuggers, etc., that
really help to make the development environment much more
“comfortable”.

Now, the question arises: how can we realize all of this?

## Implementation

For those who have followed the previous post, you are already aware
that `scx_rustland` is made of two main components: an eBPF
part, responsible for implementing the low-level interface to
sched-ext/eBPF, using [libbpf-rs](https://github.com/libbpf/libbpf-rs), and the Rust
code operating in user-space.

Between these two layers there is actually an additional layer: a
Rust module (`bpf.rs`) that implements the low-level
communication between the Rust code and the eBPF code.

What if we could further abstract this module and relocate both the
eBPF code and `bpf.rs` to a separate standalone crate?

By doing so, we could simply import this crate into our project and
use the generic scheduling API to implement a fully functional Linux
scheduler.

This is precisely what I’ve recently been focused on: developing a
new Rust crate named `scx_rustland_core`, which is integrated
into the scx tools. Its purpose is to accomplish exactly this
abstraction.

A first version of this crate has been merged already in the [scx repository](https://github.com/sched-ext/scx/pull/161).

## API

The main challenge of this project is to figure out the best API to
achieve both implicitly and efficiency, and this is probably going to be
a long process (so, the API described below is subject to probable
alterations in the near future).

The `scx_rustland_core` crate provides a
`BpfScheduler` struct that represents the “connector” to the
eBPF code.

`BpfScheduler` provides the following public methods:

```
   pub fn dequeue_task(&mut self) -> Result<Option<QueuedTask>, libbpf_rs::Error>

   pub fn dispatch_task(&mut self, task: &DispatchedTask) -> Result<(), libbpf_rs::Error>
```

The former can be used to receive a task queued to the scheduler, the
latter can be used to send a task to the dispatcher.

Between the functions `dequeue_task()` and
`dispatch_task()`, the scheduler can decide to store tasks
within internal data structures, determine their order of execution, on
which CPU run them, and for how long.

Enqueued tasks and dispatched tasks are represented as following:

```
pub struct QueuedTask {
    pub pid: i32,              // pid that uniquely identifies a task
    pub cpu: i32,              // CPU where the task is running (-1 = exiting)
    pub cpumask_cnt: u64,      // cpumask generation counter
    pub sum_exec_runtime: u64, // Total cpu time
    pub nvcsw: u64,            // Voluntary context switches
    pub weight: u64,           // Task static priority
}

pub struct DispatchedTask {
    pub pid: i32,         // pid that uniquely identifies a task
    pub cpu: i32,         // target CPU selected by the scheduler
    pub cpumask_cnt: u64, // cpumask generation counter
    pub payload: u64,     // task payload (used for debugging)
}
```

To assign a specific CPU to task the scheduler can change the
attribute `cpu` within the `DispatchedTask`
struct. If the special value `NO_CPU` is specified, the
dispatcher will execute the task on the first CPU available.

Moreover, to decide the amount of time that each task can run on the
assigned CPU, a global time slice is used: there is a default global
time slice and a global effective time slice, that can be adjusted
dynamically by the scheduler using the following methods:

```
  pub fn set_effective_slice_us(&mut self, slice_us: u64)
  pub fn get_effective_slice_us(&mut self) -> u64
```

TODO: as a future improvement I’m planning to add also a local time
slice to the `DispatchedTask` struct. This will give the
possibility to set a different time slice to each task, and override the
global effective time slice on a per-task basis.

Last, but not least, an additional method is provided to notify the
eBPF component if the user-space scheduler has still some pending work
to complete:

```
    pub fn update_tasks(&mut self, nr_queued: Option<u64>, nr_scheduled: Option<u64>) {
```

`nr_queued` is a counter that represents the amount of
queued tasks that still need to be processed by the user-space
scheduler, `nr_scheduled` represents the amount of tasks that
have been currently queued into the scheduler and still need to be
dipsatched.

For example, it is possible to notify the eBPF dipatcher that the
scheduler doesn’t have any pending work using this method as
following:

```
  .update_tasks(Some(0), Some(0));
```

## scx\_rustland refactoring

`scx_rustland` has been rewritten on top of
`scx_rustland_core` and the scheduler code is **a
lot** more compact:

```
 $ git diff --stat origin/scx-user~9..origin/scx-user scheds/rust/scx_rustland/
 ...
  9 files changed, 40 insertions(+), 1592 deletions(-)
```

This is purely a code refactoring, performance-wise
`scx_rustland` can still achieve the same performance as
before

[ I can still play AAA games, such as Baldur’s Gate 3, CS2, etc.,
while recompiling the kernel in the background and achieve a higher fps
than the default Linux scheduler. ]

And if the scheduler isn’t ideal for a particular workload we can
simply switch to a different scx scheduler or move back to the default
Linux scheduler, at run-time and with zero downtime.

## Example

As a practical example, to demonstrate how to use
`scx_rustland_core`, I’ve added a new Rust scheduler to the
scx schedulers, called [`scx_rlfifo`](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rlfifo).

The scheduler is a plain FIFO scheduler (which may not be very
thrilling), but its simplicity facilitates its use as a template for
implementing more complex scheduling policies.

The entire code is compact enough that can fit in this blog post:

```
// Copyright (c) Andrea Righi <andrea.righi@canonical.com>

// This software may be used and distributed according to the terms of the
// GNU General Public License version 2.
mod bpf_skel;
pub use bpf_skel::*;
pub mod bpf_intf;

mod bpf;
use bpf::*;

use scx_utils::Topology;

use std::sync::atomic::AtomicBool;
use std::sync::atomic::Ordering;
use std::sync::Arc;

use std::time::{Duration, SystemTime};

use anyhow::Result;

struct Scheduler<'a> {
    bpf: BpfScheduler<'a>,
}

impl<'a> Scheduler<'a> {
    fn init() -> Result<Self> {
        let topo = Topology::new().expect("Failed to build host topology");
        let bpf = BpfScheduler::init(5000, topo.nr_cpus() as i32, false, false, false)?;
        Ok(Self { bpf })
    }

    fn now() -> u64 {
        SystemTime::now()
            .duration_since(SystemTime::UNIX_EPOCH)
            .unwrap()
            .as_secs()
    }

    fn dispatch_tasks(&mut self) {
        loop {
            // Get queued taks and dispatch them in order (FIFO).
            match self.bpf.dequeue_task() {
                Ok(Some(task)) => {
                    // task....