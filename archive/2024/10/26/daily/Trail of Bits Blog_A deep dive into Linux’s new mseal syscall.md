---
title: A deep dive into Linux’s new mseal syscall
url: https://blog.trailofbits.com/2024/10/25/a-deep-dive-into-linuxs-new-mseal-syscall/
source: Trail of Bits Blog
date: 2024-10-26
fetch_date: 2025-10-06T18:52:01.105077
---

# A deep dive into Linux’s new mseal syscall

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A deep dive into Linux’s new mseal syscall

Alan Cao

October 25, 2024

[linux](/categories/linux/), [research-practice](/categories/research-practice/)

If you love exploit mitigations, you may have heard of a new system call named `mseal` landing into the Linux kernel’s 6.10 release, providing a protection called “memory sealing.” Beyond notes from the authors, very little information about this mitigation exists. In this blog post, we’ll explain what this syscall is, including how it’s different from prior memory protection schemes and how it works in the kernel to protect virtual memory. We’ll also describe the particular exploit scenarios that `mseal` helps stop in Linux userspace, such as stopping malicious permissions tampering and preventing memory unmapping attacks.

### What mseal is (and isn’t)

Memory sealing allows developers to make memory regions immutable from illicit modifications during program runtime. When a virtual memory address (VMA) range is sealed, an attacker with a code execution primitive cannot perform subsequent virtual memory operations to change the VMA’s permissions or modify how it is laid out for their benefit.

If you’re like me and followed the [spicy discourse](https://lore.kernel.org/lkml/CAHk-%3Dwh%2B6n6f0zuezKem%2BW%3DaytHMv2bib6Fbrg-xnWOoujFb6g%40mail.gmail.com/) surrounding this syscall in the kernel mailing lists, you may have observed that Chrome’s Security team introduced it to support their [V8 CFI strategy](https://v8.dev/blog/control-flow-integrity), initially for Linux-based ChromeOS. After some lengthy deliberation and several rewrites, it finally landed in the kernel, with plans to expand its use case beyond browsers with [its integration into glibc, possibly in version 2.41](https://lwn.net/Articles/978010/).

`mseal`’s security guarantees are unlike Linux’s `memfd_create` and its `memfd_secret` variant, which provide file sealing. `memfd_create` and `memfd_secret` allow one to create RAM-backed anonymous files as an alternative to storing content to `tmpfs`, with `memfd_secret` taking it a step further by ensuring that the region of memory is accessible only to the process holding the file descriptor. This lets developers create “secure enclave”-style userspace mappings that can guard sensitive in-memory data.

`mseal` digresses from prior memory protection schemes on Linux because it is a syscall tailored specifically for *exploit mitigation* against remote attackers seeking code execution rather than potentially local ones looking to exfiltrate sensitive secrets in-memory.

To understand `mseal`’s security mitigations, we must first study its implementation to understand how it operates. Luckily, `mseal` is simple to understand, so let’s look at how it works in the kernel!

### A look under the hood

`mseal` has a simple function signature:

```
int mseal(unsigned long start, size_t len, unsigned long flags)
```

* `start` and `len` represent the start/end range of a valid VMA that we want to seal, and len must be properly page-aligned.
* `flags` are unused at the time of writing and must be set to 0.

In the 6.12 kernel, its syscall definition calls [`do_mseal`](https://elixir.bootlin.com/linux/v6.12-rc3/source/mm/mseal.c#L212):

```
static int do_mseal(unsigned long start, size_t len_in, unsigned long flags)
{
    size_t len;
    int ret = 0;
    unsigned long end;
    struct mm_struct *mm = current->mm;     // [1]

    // ... Check flags == 0, check page alignment, and compute `end`

    if (mmap_write_lock_killable(mm))          // [2]
        return -EINTR;

    /*
     * First pass, this helps to avoid
     * partial sealing in case of error in input address range,
     * e.g. ENOMEM error.
     */
    ret = check_mm_seal(start, end);            // [3]
    if (ret)
        goto out;

    /*
     * Second pass, this should success, unless there are errors
     * from vma_modify_flags, e.g. merge/split error, or process
     * reaching the max supported VMAs, however, those cases shall
     * be rare.
     */
    ret = apply_mm_seal(start, end);            // [4]

out:
    mmap_write_unlock(current->mm);
    return ret;
}
```

`do_mseal` will first compute an `end` offset from the provided length and lock the memory region `[2]` to prevent concurrent access to the page. The global `current` at `[1]` represents the current executing `task_struct` (i.e., the process invoking `mseal`). The referenced field is the [`mm_struct`](https://elixir.bootlin.com/linux/v6.12-rc3/source/include/linux/mm_types.h#L790) representing the task’s entire virtual memory address space. The critical field in `mm_struct` on which this syscall will operate is `mmap`, a list of [`vm_area_struct`](https://elixir.bootlin.com/linux/v6.12-rc3/source/include/linux/mm_types.h#L667) values. This represents a single contiguous memory region created by `mmap`, such as the stack or VDSO.

The `check_mm_seal` call at `[3]` ensures that the targeted memory map for sealing is a valid range by iterating over each VMA from `current->mm` to test boundary correctness.

```
static int check_mm_seal(unsigned long start, unsigned long end)
{
    struct vm_area_struct *vma;
    unsigned long nstart = start;

    VMA_ITERATOR(vmi, current->mm, start);

    /* going through each vma to check. */
    for_each_vma_range(vmi, vma, end) {
        if (vma->vm_start > nstart)
            /* unallocated memory found. */
            return -ENOMEM;
        if (vma->vm_end >= end)
            return 0;

        nstart = vma->vm_end;
    }
    return -ENOMEM;
}
```

The magic happens in the `apply_mm_seal` call `[4]`, which walks over each VMA again and arranges for the targeted region to have an additional `VM_SEALED` flag through the `mseal_fixup` call:

```
static int apply_mm_seal(unsigned long start, unsigned long end)
{
    // ...
    nstart = start;
    for_each_vma_range(vmi, vma, end) {
        int error;
        unsigned long tmp;
        vm_flags_t newflags;

        newflags = vma->vm_flags | VM_SEALED;
        tmp = vma->vm_end;
        if (tmp > end)
            tmp = end;
        error = mseal_fixup(vmi, vma, &prev, nstart, tmp, newflags);
        if (error)
            return error;
        nstart = vma_iter_end(&vmi);
    }
    return 0;
}
```

To ensure that unwanted memory operations respect this new flag, the `mseal` patchset adds `VM_SEALED` checks to the following files:

```
 mm/madvise.c                                |   12 +
 mm/mmap.c                                   |   31 +-
 mm/mprotect.c                               |   10 +
 mm/mremap.c                                 |   31 +
 mm/mseal.c                                  |  307 ++++
```

For instance, `mprotect` and `pkey_mprotect` will enforce this check when it eventually invokes [`mprotect_fixup`](https://elixir.bootlin.com/linux/v6.12-rc3/source/mm/mprotect.c#L614):

```
int
mprotect_fixup(..., struct vm_area_struct *vma, ...)
{
    // ...
    if (!can_modify_vma(vma))
        return -EPERM;
    }
    // ...
}
```

To determine whether the syscall should continue, `can_modify_vma`—defined in [`mm/vma.h`](https://elixir.bootlin.com/linux/v6.12-rc3/source/mm/vma.h#L534)—will test for the existence of `VM_SEALED` in the specified `vm_area_struct`:

```
static inline bool vma_is_sealed(struct vm_area_struct *vma)
{
    return (vma->vm_flags & VM_SEALED);
}

/*
 * check if a vma is sealed for modification.
 * return true, if modification is allowed.
 */
static inline bool can_modify_vma(struct vm_area_struct *vma)
{
    if (unlikely(vma_is_sealed(vma)))
        return false;

    return true;
}
```

From the changes in other memory-management syscalls, we can determine the operations that are not permitted on a VMA after it is sealed:

* Changing permission bits with `mprotect` and `pkey_mprotect`
* Unmapping with `munmap`
* Replace...