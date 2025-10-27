---
title: Implement your own kernel CPU scheduler in Ubuntu with sched-ext
url: http://arighi.blogspot.com/2023/07/implement-your-own-cpu-scheduler-in.html
source: arighi's blog
date: 2023-07-21
fetch_date: 2025-10-04T11:53:24.722581
---

# Implement your own kernel CPU scheduler in Ubuntu with sched-ext

# [arighi's blog](http://arighi.blogspot.com/)

## Thursday, July 20, 2023

### Implement your own kernel CPU scheduler in Ubuntu with sched-ext

### What is sched-ext?

sched-ext is a new scheduling class introduced in the Linux kernel that provides a mechanism to implement scheduling policies as BPF (Berkeley Packet Filter) programs [[1]](#one). Such programs can also be connected to user-space counterparts to defer scheduling decisions to regular user-space processes.

### State of the art

The idea of "pluggable" schedulers is not new, it was initially proposed in 2004 [[2]](#two), but at that time it was strongly rejected, to prioritize the creation of a single generic scheduler (one to rule them all), that ended up being the “completely fair scheduler” (CFS).
However, with BPF and the sched-ext scheduling class, we now have the possibility to easily and quickly implement and test scheduling policies, making the “pluggable” approach an effective tool for easy experimentation.

### What is the main benefit of sched-ext?

The ability to implement custom scheduling policies via BPF greatly lowers the difficulty of testing new scheduling ideas (much easier than changing CFS or replacing it with a different scheduler). With this feature researchers or developers can test their own scheduler in a safe way, without even needing to reboot the system.

### How to use sched-ext in Ubuntu?

Unfortunately sched-ext is not yet available in the upstream Linux kernel, at the moment it is only available as a patch set in the Linux kernel mailing list [[3]](#three) (and it is unlikely to be applied upstream in the near future, because there are still some concerns and potential issues that need to be addressed).
However, it is possible to use an experimental version of the Ubuntu linux-unstable kernel [[4]](#four) [[5]](#five) that includes the sched-ext patch set (keep in mind that this kernel is very experimental, do not use it in production!).

### How to implement a custom scheduler?

The following example implements a “toy” CPU scheduler that passes all the scheduling “enqueue” events to a user-space task that processes them in a FIFO way and sends the “dispatch” events back to the kernel.
First of all let’s implement the BPF program:

```
/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Copyright 2023 Canonical Ltd.
 */

#include "scx_common.bpf.h"
#include "scx_toy.h"

char _license[] SEC("license") = "GPL";

/*
 * This contains the PID of the scheduler task itself (initialized in
 * scx_toy.c).
 */
const volatile s32 usersched_pid;

/* Set when the user-space scheduler needs to run */
static bool usersched_needed;

/* Notify the user-space counterpart when the BPF program exits */
struct user_exit_info uei;

/* Enqueues statistics */
u64 nr_failed_enqueues, nr_kernel_enqueues, nr_user_enqueues;

/*
 * BPF map to store enqueue events.
 *
 * The producer of this map is this BPF program, the consumer is the user-space
 * scheduler task.
 */
struct {
        __uint(type, BPF_MAP_TYPE_QUEUE);
        __uint(max_entries, MAX_TASKS);
        __type(value, struct scx_toy_enqueued_task);
} enqueued SEC(".maps");

/*
 * BPF map to store dispatch events.
 *
 * The producer of this map is the user-space scheduler task, the consumer is
 * this BPF program.
 */
struct {
        __uint(type, BPF_MAP_TYPE_QUEUE);
        __uint(max_entries, MAX_TASKS);
        __type(value, s32);
} dispatched SEC(".maps");

/* Return true if the target task "p" is a kernel thread */
static inline bool is_kthread(const struct task_struct *p)
{
	return !!(p->flags & PF_KTHREAD);
}

/* Return true if the target task "p" is the user-space scheduler task */
static bool is_usersched_task(const struct task_struct *p)
{
	return p->pid == usersched_pid;
}

/*
 * Dispatch user-space scheduler directly.
 */
static void dispatch_user_scheduler(void)
{
        struct task_struct *p;

        if (!usersched_needed)
                return;
        p = bpf_task_from_pid(usersched_pid);
        if (!p)
                return;
        usersched_needed = false;
        scx_bpf_dispatch(p, SCX_DSQ_GLOBAL, SCX_SLICE_DFL, 0);
        bpf_task_release(p);
}

void BPF_STRUCT_OPS(toy_enqueue, struct task_struct *p, u64 enq_flags)
{
	struct scx_toy_enqueued_task task = {
		.pid = p->pid,
	};

        /*
         * User-space scheduler will be dispatched only when needed from
         * toy_dispatch(), so we can skip it here.
         */
        if (is_usersched_task(p))
            return;

	if (is_kthread(p)) {
		/*
		 * We want to dispatch kernel threads and the scheduler task
		 * directly here for efficiency reasons, rather than passing
		 * the events to the user-space scheduler counterpart.
		 */
		__sync_fetch_and_add(&nr_kernel_enqueues, 1);
		scx_bpf_dispatch(p, SCX_DSQ_GLOBAL, SCX_SLICE_DFL, enq_flags);
		return;
	}
	if (bpf_map_push_elem(&enqueued, &task, 0)) {
		/*
		 * We couldn't push the task to the "enqueued" map, dispatch
		 * the event here and register the failure in the failure
		 * counter.
		 */
		__sync_fetch_and_add(&nr_failed_enqueues, 1);
		scx_bpf_dispatch(p, SCX_DSQ_GLOBAL, SCX_SLICE_DFL, enq_flags);
	} else {
		/*
		 * Enqueue event will be processed and task will be dispatched
		 * in user-space by the scheduler task.
		 */
		__sync_fetch_and_add(&nr_user_enqueues, 1);
	}
}

void BPF_STRUCT_OPS(toy_dispatch, s32 cpu, struct task_struct *prev)
{
	struct task_struct *p;
	s32 pid;

        dispatch_user_scheduler();

	/*
	 * Get a dispatch event from user-space and dispatch the corresponding
	 * task.
	 */
	if (bpf_map_pop_elem(&dispatched, &pid))
		return;

	p = bpf_task_from_pid(pid);
	if (!p)
		return;

	scx_bpf_dispatch(p, SCX_DSQ_GLOBAL, SCX_SLICE_DFL, 0);
	bpf_task_release(p);
}

s32 BPF_STRUCT_OPS(toy_init)
{
	/* Apply the "toy" scheduling class for all the tasks in the system */
	scx_bpf_switch_all();
	return 0;
}

void BPF_STRUCT_OPS(toy_exit, struct scx_exit_info *ei)
{
	/* Notify user-space counterpart that the BPF program terminated */
	uei_record(&uei, ei);
}

SEC(".struct_ops.link")
struct sched_ext_ops toy_ops = {
	.enqueue		= (void *)toy_enqueue,
	.dispatch		= (void *)toy_dispatch,
	.init			= (void *)toy_init,
	.exit			= (void *)toy_exit,
	.name			= "toy",
};
```

Then we can implement the user-space counterpart, that will intercept the “enqueue” events and will dispatch them back to the kernel:

```
/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Copyright 2023 Canonical Ltd.
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <sched.h>
#include <signal.h>
#include <assert.h>
#include <libgen.h>
#include <pthread.h>
#include <bpf/bpf.h>
#include <sys/mman.h>
#include <sys/queue.h>
#include <sys/syscall.h>
#include "user_exit_info.h"
#include "scx_toy.skel.h"
#include "scx_toy.h"

const char help_fmt[] =
"A toy sched_ext scheduler.\n"
"\n"
"See the top-level comment in .bpf.c for more details.\n"
"\n"
"Usage: %s\n"
"\n"
"  -h            Display this help and exit\n";

static volatile int exit_req;

/*
 * Descriptors used to communicate enqueue and dispatch event with the BPF
 * program.
 */
static int enqueued_fd, dispatched_fd;

static struct scx_toy *skel;

static void sigint_handler(int dummy)
{
	exit_req = 1;
}

/* Thread that periodically prints enqueue statistics */
static void *run_stats_printer(void *arg)
{
	while (!exit_req) {
		__u64 nr_failed_enqueues, nr_kernel_enqueues, nr_user_enqueues, total;

		nr_failed_enqueues = skel->bss->nr_failed_enqueues;
		nr_kernel_enqueues = skel->bss->nr_kernel_enqueues;
		nr_user_enqueues = skel->bss->nr_user_enqueues;
		total = nr_failed_enqueues + nr_kernel_enqueues + nr_user_enqueues;

		printf("\e[1;1H\e[2J");
		printf("o-----------------------o\n");
		printf("| BPF SCHED ENQUEUES    |\n");
		printf("|-----------------------|\n");
		printf("|  kern:     %10llu |\n", nr_kernel_enqueues);
		printf("|  user:     %10llu |\n", nr_user_enqueues);
		printf("|  failed:   %10llu |\n", nr_failed_enqueues);
		printf(...