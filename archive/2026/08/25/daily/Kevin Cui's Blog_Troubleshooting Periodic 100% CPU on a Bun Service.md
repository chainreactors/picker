---
title: Troubleshooting Periodic 100% CPU on a Bun Service
url: http://bugs.cc/posts/troubleshooting-bun-kafkajs-cpu-spin/
source: Kevin Cui's Blog
date: 2026-08-25
fetch_date: 2026-08-26T03:05:55.306717
---

# Troubleshooting Periodic 100% CPU on a Bun Service

[# Kevin Cui's Blog](/)[Home](/)
[Posts](/posts/)
[Docs](https://docs.bugs.cc)
[RSS](https://bugs.cc/index.xml)
[zh-CN 🇨🇳](/zh/posts/troubleshooting-bun-kafkajs-cpu-spin/)

# Troubleshooting Periodic 100% CPU on a Bun Service

2026-08-25

A few days ago we hit a fairly interesting production issue. A Bun service was periodically pegging one CPU core across three pods, for exactly 10 minutes each time, then dropping back on its own. The service itself was fine: requests worked, health checks never failed. The CPU graph just looked awful.

It turned out to be two problems that are each pretty mild on their own, stacked on a specific kernel version and a specific Bun patch release. Writing it down.

**Environment:**

* Bun 1.3.14 (pinned in the Dockerfile)
* kafkajs 2.2.4
* Kubernetes node kernel 5.10.134

Repro: [bun-epoll-timer-spin-repro](https://github.com/BlackHole1/bun-epoll-timer-spin-repro). I’ll come back to this later.

## [The symptom](#the-symptom)

![Minute-level CPU of three pods on one day](/images/troubleshooting-bun-kafkajs-cpu-spin/cpu-day.png)

Minute-level CPU for the three pods on one day. The vertical lines at the bottom are Kafka produces; more on that later. A few things stand out:

* The plateau sits at 0.99 cores and never goes above 1.0. Only one thread is busy.
* Every stretch is a multiple of 600 seconds. It jumps up and down within a single scrape interval, not a gradual climb.
* All three pods often start the stretch together.
* Almost nothing overnight. It tracks traffic.
* During a spike, user is about 2/3 and sys about 1/3. Network, fd count, and memory look the same as a quiet period.

That last point already rules a lot out. We weren’t chewing through large payloads, and it wasn’t pure JS compute (sys wouldn’t be that high). It looked like a busy loop that still makes syscalls.

I first wondered if a worker was stuck in a tight loop on some job. But over 24 hours, every log related to job timeouts, retries, and heartbeats was zero. Busy periods and idle periods produced almost the same amount of logs. It also wasn’t introduced by a deploy: every one of the 16 days we have metrics for looks the same.

## [Reading /proc in the pod](#reading-proc-in-the-pod)

Can’t poke production casually, and there’s no perf in the container, so I `kubectl exec`’d and read `/proc`. That’s fully read-only.

Diff utime/stime of every thread in `/proc/<pid>/task/*/stat` over 3 seconds and find the hot one. During a spike (100 ticks = one core):

```
tid   comm        d_utime  d_stime
8     bun         197      100
95    HTTP        0        0
9     bun         0        0
16    Bun         0        0
15    Bun         0        0
14    Bun         0        0
13    Bun         0        0
12    HeapHelper  0        0
11    HeapHelper  0        0
10    HeapHelper  0        0
```

The hot thread is the main thread (the one where tid equals pid). Then I sampled `/proc/<pid>/task/<tid>/syscall` as fast as I could. The first column is the syscall number the thread is currently in, followed by six arguments. When the thread is in userspace, the file says `running`:

```
i=0
while [ $i -lt 3000 ]; do
  cat /proc/8/task/8/syscall >> /tmp/sc.txt
  i=$((i+1))
done
# which syscall it is blocked on
awk '{print $1}' /tmp/sc.txt | sort | uniq -c | sort -rn
# epoll_pwait timeout (4th argument, i.e. column 5)
awk '$1 == 281 {print $5}' /tmp/sc.txt | sort | uniq -c | sort -rn
```

Syscall numbers depend on the architecture. On x86\_64 the table is [syscall\_64.tbl](https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl) in the kernel tree; if the box has auditd, `ausyscall x86_64 281` works too. These are the ones that show up later:

```
202  futex
281  epoll_pwait
441  epoll_pwait2
```

On arm64, `epoll_pwait` is 22. `epoll_pwait2` is one of the newer syscalls that got a single number across architectures: 441 everywhere.

Idle:

```
   2969 281
     29 running
      2 202

   1850 0x63
    325 0x53
    201 0x56
    192 0x57
     90 0x5d
```

2969 of 3000 samples were sitting in syscall 281, `epoll_pwait`, with a timeout of tens to hundreds of milliseconds. Normal. One detail: 441 (`epoll_pwait2`) never showed up at all. That matters later.

During a spike:

```
   2979 running
     21 281

     21 0x1
```

Almost entirely in userspace. The rare times it was in `epoll_pwait`, the timeout was 1ms.

Then `/proc/<pid>/net/tcp`: 4 connections when idle (Redis, Postgres). During a spike, two extra connections to port 9095, the Kafka broker.

## [Every spike was a Kafka send](#every-spike-was-a-kafka-send)

The service publishes metering events with kafkajs. I pulled 48 hours of logs that trigger a Kafka produce and lined them up against 115 CPU stretches:

* Every stretch starts within -13s to +1s of the nearest produce (within scrape jitter)
* Every stretch ends 600s to 611s after the last produce in that stretch
* The other way around: all 373 produces fall inside some stretch. None missed.

600s is the default `connections.max.idle.ms` on a Kafka broker: the broker closes a connection after 10 minutes idle. So the length of a CPU stretch is the lifetime of one Kafka connection. The three pods spiked together because one user’s batch of jobs landed on three machines, each of which sent a message within a few seconds.

## [The 1ms setTimeout in kafkajs](#the-1ms-settimeout-in-kafkajs)

kafkajs 2.2.4, `src/network/requestQueue/index.js`:

```
checkPendingRequests() {
  while (this.pending.length > 0 && this.canSendSocketRequestImmediately()) {
    // ...
  }
  this.scheduleCheckPendingRequests()
}

scheduleCheckPendingRequests() {
  let scheduleAt = this.throttledUntil - Date.now()
  if (!this.throttleCheckTimeoutId) {
    if (this.pending.length > 0) {
      scheduleAt = scheduleAt > 0 ? scheduleAt : CHECK_PENDING_REQUESTS_INTERVAL
    }
    this.throttleCheckTimeoutId = setTimeout(() => {
      this.throttleCheckTimeoutId = null
      this.checkPendingRequests()
    }, scheduleAt)
  }
}
```

`checkPendingRequests` always calls `scheduleCheckPendingRequests`. When pending is empty and there’s no throttle, that still arms a `setTimeout`, whose callback calls `checkPendingRequests` again. `throttledUntil` starts at -1, so `scheduleAt` is a huge negative number. Both Node and Bun treat a negative delay as 1ms.

So from the first response on a broker connection, that connection runs a 1ms `setTimeout` loop until `destroy()` is called. And `destroy()` only runs when the connection drops.

This has been reported upstream ([kafkajs#1556](https://github.com/tulios/kafkajs/issues/1556), [kafkajs#1704](https://github.com/tulios/kafkajs/issues/1704)). A fix PR has been sitting around for a long time ([kafkajs#1572](https://github.com/tulios/kafkajs/pull/1572)) and never landed. We had already patched it in our repo, but the patch only clamped the negative value with `Math.max(1, scheduleAt || 1)`, which keeps the 1ms loop around instead of killing it.

Still: a 1ms `setTimeout` loop is maybe 2% CPU on Node. Why does it peg a whole core?

## [Why Bun pegs a whole core](#why-bun-pegs-a-whole-core)

The event loop. Bun 1.3.14, `packages/bun-usockets/src/eventing/epoll_kqueue.c`:

```
static int bun_epoll_pwait2(int epfd, struct epoll_event *events, int maxevents, const struct timespec *timeout) {
    if (has_epoll_pwait2 != 0) {
        // ... sys_epoll_pwait2(...)
    }

    int timeoutMs = -1;
    if (timeout) {
        timeoutMs = timeout->tv_sec * 1000 + timeout->tv_nsec / 1000000;
    }

    do {
        ret = epoll_pwait(epfd, events, maxevents, timeoutMs, &mask);
    } while (IS_EINTR(ret));

    return ret;
}
```

Bun prefers `epoll_pwait2`, which takes a nanosecond `timespec`. `epoll_pwait2` only exists since Linux 5.11; Bun checks the kernel version and falls back to `epoll_pwait` with a millisecond timeout below that. The bug is `tv_nsec / 1000000`: it truncates toward zero.

A 1ms timer re-arms itself in its own callback. The event...