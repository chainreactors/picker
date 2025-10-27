---
title: Gone in 5 Seconds: How WARN_ON Stole 10 Minutes
url: https://starlabs.sg/blog/2025/05-gone-in-5-seconds-how-warn_on-stole-10-minutes/
source: Blogs on STAR Labs
date: 2025-05-31
fetch_date: 2025-10-06T22:25:36.131126
---

# Gone in 5 Seconds: How WARN_ON Stole 10 Minutes

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Gone in 5 Seconds: How WARN\_ON Stole 10 Minutes

May 30, 2025 · 16 min · Tan Ze Jian

Table of Contents

* [Root Cause Analysis](#root-cause-analysis)

  - [Backing pages](#backing-pages)
  - [Mapping pages](#mapping-pages)
* [Exploit](#exploit)
  + [Arbitrary R/W](#arbitrary-rw)
  + [Other Pathways](#other-pathways)
  + [Privilege Escalation](#privilege-escalation)
    - [Bypass SELinux](#bypass-selinux)
    - [Root](#root)
  + [‘Fix’ delay](#fix-delay)
* [Bug Fix](#bug-fix)
* [References](#references)

As part of my internship at STAR Labs, I was tasked to conduct N-day analysis of CVE-2023-6241. The original PoC can be found [here](https://github.com/github/securitylab/tree/main/SecurityExploits/Android/Mali/CVE_2023_6241), along with the accompanying [write-up](https://github.blog/security/vulnerability-research/gaining-kernel-code-execution-on-an-mte-enabled-pixel-8/).

In this blog post, I will explain the root cause as well as an alternative exploitation technique used to exploit the page UAF, achieving arbitrary kernel code execution.

The following exploit was tested on a Pixel 8 running the latest version available prior to the patch.

```
shiba:/ $  getprop ro.build.fingerprint
google/shiba/shiba:14/UQ1A.240205.004/11269751:user/release-keys
```

# Root Cause Analysis[#](#root-cause-analysis)

The bug occurs due to a race condition in the `kbase_jit_grow` function ([*source*](https://android.googlesource.com/kernel/google-modules/gpu/%2B/9f172bc88cc5ff01c68fbab6f504058dd00138df/mali_kbase/mali_kbase_mem.c#4042)).

The race window opens when the number of physical pages requested by the caller exceed the number of pages in the `kctx`’s mempool. The lock will be dropped to allow the mempool to be refilled by the kernel.

After refilling, the previously calculated `old_size` value is used for calculation by `kbase_mem_grow_gpu_mapping`, for mapping the new pages. The code incorrectly assumes that the previous `old_size` and `nents` still hold the same value after the while loop below.

```
/* Grow the backing */
old_size = reg->gpu_alloc->nents; // previous old_size
/* Allocate some more pages */
delta = info->commit_pages - reg->gpu_alloc->nents;
pages_required = delta;
...
while (kbase_mem_pool_size(pool) < pages_required) {
    int pool_delta = pages_required - kbase_mem_pool_size(pool);
    int ret;
    kbase_mem_pool_unlock(pool);
    spin_unlock(&kctx->mem_partials_lock);
    kbase_gpu_vm_unlock(kctx); // lock dropped
    ret = kbase_mem_pool_grow(pool, pool_delta, kctx->task); // race window here
    kbase_gpu_vm_lock(kctx); // lock reacquired
    if (ret)
        goto update_failed;
    spin_lock(&kctx->mem_partials_lock);
    kbase_mem_pool_lock(pool);
}
// after race window, actual nents may be greater than the old_size
...
ret = kbase_mem_grow_gpu_mapping(kctx, reg, info->commit_pages,
					 old_size, mmu_sync_info);
```

If we were to introduce a page fault via a write instruction to grow the JIT memory region during the race window, the actual number of backing pages (`reg->gpu_alloc->nents`) will be greater than the cached `old_size`.

> *During a page fault, the page fault handler will map and back physical pages up to the faulting address.*

```
-----------------------------
|   old_size   | FAULT_SIZE |
-----------------------------
<----------- nents ---------->
```

### Backing pages[#](#backing-pages)

`kbase_jit_grow` adds backing pages to the memory region with the line:

```
kbase_alloc_phy_pages_helper_locked(reg->gpu_alloc, pool, delta, &prealloc_sas[0])
```

The `delta` argument is the cached value saved before the race window, which has the same value as `old_size`. When we look at the `kbase_alloc_phy_pages_helper_locked` function, it references the new `reg->gpu_alloc->nents` value instead, and uses it as the start offset to add `delta` pages ([source](https://android.googlesource.com/kernel/google-modules/gpu/%2B/9f172bc88cc5ff01c68fbab6f504058dd00138df/mali_kbase/mali_kbase_mem.c#2676)). In other words, physical backing pages are allocated from offset `nents` to `nents + delta`

### Mapping pages[#](#mapping-pages)

`kbase_jit_grow` then tries to map the pages with:

```
kbase_mem_grow_gpu_mapping(kctx, reg, info->commit_pages, old_size, mmu_sync_info)
```

When mapping the new pages, `kbase_mem_grow_gpu_mapping` calculates `delta` as `info->commit_pages - old_size` and starts mapping `delta` pages starting from `old_size`. Since `kbase_mem_grow_gpu_mapping` does not ‘know’ that the region’s actual `nents` have increased, it will fail to map the last `FAULT_SIZE` pages.

```
Expectation:
----------------------------------
|   old_size   |      delta      |
---------------------------------

Reality:
-----------------------------------------------
|   old_size   | FAULT_SIZE |      delta      |
-----------------------------------------------
                    or
-----------------------------------------------
|   old_size   |      delta      | FAULT_SIZE |
-----------------------------------------------
<----------------- backed -------------------->
<----------- mapped ------------> <- unmapped >
```

We will now end up with a state where the right portion of the memory region is unmapped but backed by physical pages.

# Exploit[#](#exploit)

In order to make this exploitable, we need to first understand how the Mali driver handles shrinking and freeing of memory regions.

> *The original [writeup](https://github.blog/security/vulnerability-research/gaining-kernel-code-execution-on-an-mte-enabled-pixel-8/#exploiting-ghsl-2023-005) explains it pretty well.*

The idea is to create a memory region in which a portion remains unmapped while the surrounding areas are still mapped. This configuration causes the shrinking routine to skip unmapping that specific portion, even if its backing page is marked for release.

To achieve that, we can introduce a second fault near the end of the existing memory region to fulfil the criteria.

```
--------------------------------------------------------------
|   old_size   |      delta      | FAULT_SIZE | second fault |
--------------------------------------------------------------
<----------- mapped ------------> <- unmapped ><-- mapped --->
```

After which, we shrink the memory region, which causes the GPU to start unmapping after `final_size`. The Mali driver will skip unmapping mappings in `PTE1` since it is unmapped and invalid. When it reaches `PTE2`, since the 1st entry in `PTE2` is invalid as the corresponding address is unmapped, `kbase_mmu_teardown_pgd_pages` will skip unmapping the next 512 virtual pages. However, that should not have been the case since there are still valid PTEs that needs to be unmapped.

```
<------------ final_size ------------><----- free pages ----->
--------------------------------------------------------------
|             mapped             |  unmapped  |    mapped    |
--------------------------------------------------------------
                                 |-- PTE1 --|-- PTE2 --|
                                               <---*--->

*region skipped unmapping but backing pages are freed
```

We can set `FAULT_SIZE` to be 0x300 pages, such that it occupies slightly more than 1 last level PTE (*can hold 0x200 pages*). Hence, there will be a portion of the memory in `second_fault` that remains mapped after shrinking. However, all the physical pages after `final_size` are freed.

At this point, we are st...