---
title: Testing race conditions with memory access tracing and stack-based delay injection
url: https://projectzero.google/2026/09/maccconc-race-condition.html
source: Project Zero
date: 2026-09-08
fetch_date: 2026-09-09T06:57:08.322014
---

# Testing race conditions with memory access tracing and stack-based delay injection

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Testing race conditions with memory access tracing and stack-based delay injection

[2026-Sep-08](/2026/09/maccconc-race-condition.html "Permalink to this post")
Jann Horn

Many security bugs are race conditions, where multi-threaded execution has to occur with the right interleaving for a negative effect to appear. This creates challenges for several use cases:

* Confirming bug candidates that have been discovered manually or through static analysis.
* Regression tests: After fixing a race condition bug, there is often no good way to write a regression test that reliably triggers the bug as part of a test suite.
* Automatic bug discovery, such as fuzzing: It is hard for a fuzzer to exercise all interesting interleavings of concurrent operations, or reach code paths that are only exercised when operations are racing.

I mostly discover bugs by manually reading code. When I think Iâve found a bug, I normally write a test case to either prove or disprove that the bug exists. For race condition bugs, it can be hard to achieve either outcome. For Linux kernel bugs, I often resort to recompiling the kernel after adding conditional `mdelay()` calls (which spinloop for roughly the specified amount of time) in appropriate places; I usually make these conditional based on the name of the running thread, though sometimes more complex conditions are needed. On platforms that support DTrace (like macOS and [Windows](https://github.com/microsoft/DTrace-on-Windows/commit/dbfb82f7fb70e001f303eab497ec4338295605f8)), it is possible to use DTrace probes that call [`chill()`](https://docs.oracle.com/cd/E19253-01/817-6223/chp-actsub-chill/index.html) for similar effect, though the utility of this is limited as DTrace can only trace on non-inline function boundaries or explicit trace points, rather than on every instruction. Regardless of platform, this approach can be time consuming and can require trial and error to definitely determine whether code is buggy.

Additionally, in the Linux kernel, fixes for race condition bugs are often accompanied by hand-written ASCII diagrams showing problematic thread interleavings with call graphs and relevant memory accesses (for example, see this recent [rt\_spin\_unlock UAF fix](https://git.kernel.org/linus/89038cc87d80c77e7aa6f42a64b2573b74af339f), or this recent [jbd2 deadlock fix](https://git.kernel.org/linus/981fcc5674e67158d24d23e841523eccba19d0e7)). It would be convenient to have developer tooling that can analyze potentially vulnerable code and show results in a similar representation.

## Summary

I wrote tools for exploring possible interleavings of multi-threaded test cases for the Linux kernel:

* A tool that automatically tests all possible A-B-A interleavings of a test case.
* A terminal UI for manual exploration of possible interleavings.
* A GUI for manual exploration of possible interleavings.

The kernel part of this is intended to also be usable for discovering race conditions via fuzzing, but userspace tooling for that still needs to be implemented.

The tools are available [on GitHub](https://github.com/googleprojectzero/MAccConc) under the name MAccConc, short for âMemory Access Concurrencyâ; see the README there for installation and usage instructions.

If you just want to see the tooling in action, skip to [Demo: automatic testing](#demo-automatic-testing).

If youâre just interested in the theory behind the tooling, read section [Stable identifiers for memory accesses across runs: count-augmented stack traces](#stable-identifiers-for-memory-accesses-across-runs-count-augmented-stack-traces).

## Prior work

This project was inspired by discussions with Ned Williamson, whose [sockfuzzer](https://projectzero.google/2021/04/designing-sockfuzzer-network-syscall.html#h.bydr5qowo002) project involved exploration of concurrency bugs by using a custom scheduler that can reschedule at synchronization primitives to explore interleavings. See the conference talk [slides](https://github.com/googleprojectzero/SockFuzzer/blob/main/third_party/concurrence/presentations/catch_me_if_you_can.pdf) and [recording](https://www.youtube.com/watch?v=OpQvXGJcH4s) focused on the concurrency testing aspect of this.

My tooling is largely based on ideas similar to [SKI](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/fonseca), but SKI uses a different implementation: It records memory accesses and controls scheduling of vCPUs using a patched version of QEMU in TCG mode, and uses VM snapshots to explore different execution interleavings.

## Discovering memory accesses that could contribute to race conditions (communication points)

As described in the SKI paper, interesting execution interleavings of a given multi-threaded test case can be discovered by tracing memory accesses of all threads and searching for pairs of accesses on two threads that could interact with each other - meaning, roughly, that at least one of them is a write operation, and they access overlapping memory ranges. The SKI paper calls such memory accesses *communication points*.

This requires some mechanism to collect memory access coverage. SKI did this by patching QEMUâs TCG mode; I am instead relying on ASAN instrumentation in âoutlineâ mode (compiler backend flag `asan-instrumentation-with-call-threshold=0`, selected by `CONFIG_KASAN_OUTLINE` in the Linux kernel), which generates helper function calls on memory access. I believe that the kernel is the right place to collect this data because it would allow the kernel to also provide higher-level information about lock acquire/release events and such, though I have not implemented this at this time. Implementing this in the kernel also means that it would theoretically be possible to test on bare-metal hardware, rather than inside VMs.

Since Linux already has [KCOV](https://docs.kernel.org/dev-tools/kcov.html) as a mechanism to feed basic block kernel coverage information to userspace, I decided to use the same mechanism to record information about memory accesses. An alternative would have been to use ftrace, which is oriented towards tracing use cases, and includes a function graph tracing mode built on fentry hooks and more complex output buffer management that is oriented towards use cases including system-wide data collection. I chose to use KCOV because of its simpler in-memory representation of trace data (which could become relevant for recovering trace data from crashed VMs); because it uses static always-on instrumentation rather than runtime-enabled instrumentation with near-zero overhead in disabled state; and because my impression is that KCOV is designed for higher-frequency trace events than ftrace.

### Implementation detail: ASAN and TSAN

ASAN normally merges helper calls for subsequent memory accesses. To receive one callback per memory access, the kernel patches explicitly disable this compiler optimization using the `asan-opt-same-temp` backend flag.

ASAN is intended for identifying UAF, so it does not emit helper calls on direct stack memory access unless there is potential for out-of-bounds access. This means that some race conditions involving on-stack objects, such as wait queues, may not be detectable with this. ASAN also by default emits no helper calls for access to globals, but this optimization can be disabled using the `asan-opt-globals` backend flag.

An alternative would be to use TSAN instrumentation instead, which is designed for detecting data races and...