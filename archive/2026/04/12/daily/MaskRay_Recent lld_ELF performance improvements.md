---
title: Recent lld/ELF performance improvements
url: https://maskray.me/blog/2026-04-12-recent-lld-elf-performance-improvements
source: MaskRay
date: 2026-04-12
fetch_date: 2026-04-13T04:56:51.473369
---

# Recent lld/ELF performance improvements

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-04-12](/blog/2026-04-12-recent-lld-elf-performance-improvements)

# Recent lld/ELF performance improvements

Since the LLVM 22 branch was cut, I've landed patches that
parallelize more link phases and cut task-runtime overhead. This post
compares current `main` against lld 22.1, [mold](https://github.com/rui314/mold), and [wild](https://github.com/davidlattimore/wild).

Headline: a Release+Asserts clang `--gc-sections` link is
1.37x as fast as lld 22.1; Chromium debug with `--gdb-index`
is 1.07x as fast. mold and wild are still ahead â the last section
explains why.

## Benchmark

`lld-0201` is main at 2026-02-01 (6a1803929817);
`lld-load` is main plus the new
`[ELF] Parallelize input file loading`. `mold` and
`wild` run with `--no-fork` so the wall-clock
numbers include the linker process itself.

Three reproduce tarballs, `--threads=8`,
`hyperfine -w 1 -r 10`, pinned to CPU cores with
`numactl -C`.

| Workload | lld-0201 | lld-load | mold | wild |
| --- | --- | --- | --- | --- |
| clang-23 Release+Asserts, `--gc-sections` | 1.255 s | 917.8 ms | 552.6 ms | 367.2 ms |
| clang-23 Debug (no `--gdb-index`) | 4.582 s | 4.306 s | 2.464 s | 1.565 s |
| clang-23 Debug (`--gdb-index`) | 6.291 s | 5.915 s | 4.001 s | N/A |
| Chromium Debug (no `--gdb-index`) | 6.140 s | 5.904 s | 2.665 s | 2.010 s |
| Chromium Debug (`--gdb-index`) | 7.857 s | 7.322 s | 3.786 s | N/A |

Note that `llvm/lib/Support/Parallel.cpp` design keeps the
main thread idle during `parallelFor`, so
`--threads=N` really utilizes `N+1` threads.

wild does not yet implement `--gdb-index` â it silently
warns and skips, producing an output about 477 MB smaller on Chromium.
For fair 4-way comparisons I also strip `--gdb-index` from
the response file; the `no --gdb-index` rows above use that
setup.

A few observations before diving in:

* The `--gdb-index` surcharge on the Chromium link is
  `+1.42 s` for lld (5.90 s â 7.32 s) versus
  `+1.12 s` for mold (2.67 s â 3.79 s). This is currently one
  of the biggest remaining gaps.
* Excluding `--gdb-index`, mold is 1.66xâ2.22x as fast and
  wild 2.5xâ2.94x as fast on this machine. There is plenty of room
  left.
* `clang-23 Release+Asserts --gc-sections` (workload 1) has
  collapsed from 1.255 s to 918 ms, a 1.37x speedup over 10 weeks. Most of
  that came from the parallel `--gc-sections` mark, parallel
  input loading, and the task-runtime cleanup below â each contributing a
  multiplicative factor.

### macOS (Apple M4) notes

The same clang-23 Release+Asserts link, `--threads=8`, on
an Apple M4 (macOS 15, system allocator for all four linkers):

| Linker | Wall | User | Sys | (User+Sys)/Wall |
| --- | --- | --- | --- | --- |
| lld-0201 | 324.4 Â± 1.5 ms | 502.1 ms | 171.7 ms | 2.08x |
| lld-load | 221.5 Â± 1.8 ms | 476.5 ms | 368.8 ms | 3.82x |
| mold | 201.2 Â± 1.7 ms | 875.1 ms | 220.5 ms | 5.44x |
| wild | 107.1 Â± 0.5 ms | 456.8 ms | 284.6 ms | 6.92x |

## Parallelize `--gc-sections` mark

Garbage collection had been a single-threaded BFS over
`InputSection` graph. On a Release+Asserts clang link,
`markLive` was ~315 ms of the 1562 ms wall time (20%).

[6f9646a598f2](https://github.com/llvm/llvm-project/commit/6f9646a598f2)
adds `markParallel`, a level-synchronized BFS. Each BFS level
is processed with `parallelFor`; newly discovered sections
land in per-thread queues, which are merged before the next level. The
parallel path activates when
`!TrackWhyLive && partitions.size() == 1`.
Implementation details that turned out to matter:

* Depth-limited inline recursion (`depth < 3`) before
  pushing to the next-level queue. Shallow reference chains stay hot in
  cache and avoid queue overhead.
* Optimistic "load then compare-exchange" section-flag dedup instead
  of atomic fetch-or. The vast majority of sections are visited once, so
  the load almost always wins.

On the Release+Asserts clang link, `markLive` dropped from
315 ms to 82 ms at `--threads=8` (from 199 ms to 50 ms at
`--threads=16`); total wall time 1.16xâ1.18x.

Two prerequisite cleanups were needed for correctness:

* [6a874161621e](https://github.com/llvm/llvm-project/commit/6a874161621e)
  moved `Symbol::used` into the existing
  `std::atomic<uint16_t> flags`. The bitfield was
  previously racing with other mark threads.
* [2118499a898b](https://github.com/llvm/llvm-project/commit/2118499a898b)
  decoupled `SharedFile::isNeeded` from the mark walk.
  `--as-needed` used to flip `isNeeded` inside
  `resolveReloc`, which would have required coordinated writes
  across threads; it is now a post-GC scan of global symbols.

## Parallelize input file loading

Historically, `LinkerDriver::createFiles` walked the
command line and called `addFile` serially.
`addFile` maps the file (`MemoryBuffer::getFile`),
sniffs the magic, and constructs an `ObjFile`,
`SharedFile`, `BitcodeFile`, or
`ArchiveFile`. For thin archives it also materializes each
member. On workloads with hundreds of archives and thousands of objects,
this serial walk dominates the early part of the link.

The pending patch will rewrite `addFile` to record a
`LoadJob` for each non-script input together with a snapshot
of the driver's state machine (`inWholeArchive`,
`inLib`, `asNeeded`, `withLOption`,
`groupId`). After `createFiles` finishes,
`loadFiles` fans the jobs out to worker threads. Linker
scripts stay on the main thread because `INPUT()` and
`GROUP()` recursively call back into
`addFile`.

A few subtleties made this harder than it sounds:

* `BitcodeFile` and fatLTO construction call
  `ctx.saver` / `ctx.uniqueSaver`, both of which are
  non-thread-safe `StringSaver` /
  `UniqueStringSaver`. I serialized those constructors behind a
  mutex; pure-ELF links hit it zero times.
* Thin-archive member buffers used to be appended to
  `ctx.memoryBuffers` directly. To keep the output
  deterministic across `--threads` values, each job now
  accumulates into a per-job `SmallVector` which is merged into
  `ctx.memoryBuffers` in command-line order.
* `InputFile::groupId` used to be assigned inside the
  `InputFile` constructor from a global counter. With parallel
  construction the assignment race would have been unobservable but still
  ugly; [b6c8cba516da](https://github.com/llvm/llvm-project/commit/b6c8cba516da)
  hoists `++nextGroupId` into the serial driver loop and stores
  the value into each file after construction.

The output is byte-identical to the old lld and deterministic across
`--threads` values, which I verified with `diff`
across `--threads={1,2,4,8}` on Chromium.

A `--time-trace` breakdown is useful to set expectations.
On Chromium, the serial portion of `createFiles` accounts for
only ~81 ms of the 5.9 s wall, and `loadFiles` (after this
patch) runs in ~103 ms in parallel. Serial `readFile`/mmap is
not the bottleneck. What moves the needle is overlapping the per-file
constructor work â magic sniffing, archive member materialization,
bitcode initialization â with everything else that now kicks off on the
main thread while workers chew through the job list.

## Extending parallel relocation scanning

Relocation scanning has been parallel since LLVM 17, but three cases
had opted out via `bool serial`:

1. `-z nocombreloc`, because `.rela.dyn` merged
   relative and non-relative relocations and needed deterministic
   ordering.
2. MIPS, because `MipsGotSection` is mutated during
   scanning.
3. PPC64, because `ctx.ppc64noTocRelax` (a
   `DenseSet` of `(Symbol*, offset)` pairs) was
   written without a lock.

[076226f378df](https://github.com/llvm/llvm-project/commit/076226f378df)
and [dc4df5da886e](https://github.com/llvm/llvm-project/commit/dc4df5da886e)
separate relative and non-relative dynamic relocations...