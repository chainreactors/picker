---
title: MTE As Implemented, Part 3: The Kernel
url: https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-3-kernel.html
source: Project Zero
date: 2023-08-03
fetch_date: 2025-10-04T12:01:20.629316
---

# MTE As Implemented, Part 3: The Kernel

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Wednesday, August 2, 2023

### MTE As Implemented, Part 3: The Kernel

By Mark Brand, Project Zero

## Background

In 2018, in the [v8.5a version](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-a-profile-architecture-2018-developments-armv85a) of the ARM architecture, ARM proposed a hardware implementation of tagged memory, referred to as MTE (Memory Tagging Extensions).

In [Part 1](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html) we discussed testing the technical (and implementation) limitations of MTE on the hardware that we've had access to. In [Part 2](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html) we discussed the implications of this for mitigations built using MTE in various user-mode contexts. This post will now consider the implications of what we know on the effectiveness of MTE-based mitigations in the kernel context.

To recap - there are two key classes of bypass techniques for memory-tagging based mitigations, and these are the following:

1. Known-tag-bypasses - In general, confidentiality of tag values is key to the effectiveness of memory-tagging as a mitigation. A breach of tag confidentiality allows the attacker to directly or indirectly ensure that their invalid memory accesses will be correctly tagged, and therefore not detectable.
2. Unknown-tag-bypasses - Implementation limits might mean that there are opportunities for an attacker to still exploit a vulnerability despite performing memory accesses with incorrect tags that could be detected.

There are two main modes for MTE enforcement:

1. Synchronous (sync-MTE) - tag check failures result in a hardware fault on instruction retirement. This means that the results of invalid reads and the effects of invalid writes should not be architecturally observable.
2. Asynchronous (async-MTE) - tag check failures do not directly result in a fault. The results of invalid reads and the effects of invalid writes are architecturally observable, and the failure is delivered at some point after the faulting instruction in the form of a per-cpu flag.

Since Spectre, it has been clear that using standard memory-tagging approaches as a "hard probabilistic mitigation"[1](#h.gafo0jvm2gnw) is not generally possible - in any context where an attacker can construct a speculative side-channel, known-tag-bypasses are a fundamental weakness that must be accounted for.

## Kernel-specific problems

There are a number of additional factors which make robust mitigation design using MTE more problematic in the kernel context.

From a stability perspective, it might be considered problematic to enforce a panic on kernel-tag-check-failure detection - we believe that this would be essential for any mitigation based on async (or asymmetric) MTE modes.

Here are some problems that we think will be difficult to address systematically:

1. Similar to the Chrome renderer scenario discussed in [Part 2](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html), we expect there to be continued problems in guaranteeing confidentiality of kernel memory in the presence of CPU speculative side-channels.

   This fundamentally limits the effectiveness of an MTE-based mitigation in the kernel against a local attacker, making known-tag-bypasses highly likely.
2. [TCR\_ELx.TCMA1](https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Registers/TCR-EL1--Translation-Control-Register--EL1-?lang=en#fieldset_0-58_58-1) is required in the current kernel implementation. This means that any pointer with the tag 0b1111 can be dereferenced without enforcing tag checks. This is necessary for various reasons - there are many places in the kernel where, for example, we need to produce a dereferenceable pointer from a physical address, or an offset in a struct page.

   This makes it possible for an attacker to reliably forge pointers to any address, which is a significant advantage during exploitation.
3. [ASYNC-only] Direct access to the Tag Fault Status Register TFSR\_EL1 is likely necessary. If so, the kernel is capable of clearing the tag-check-failure flags for itself, this is a weakness that will likely form part of the simplest unknown-tag-bypass exploits. This weakness does not exist in user-space, as it is necessary to transition into kernel-mode to clear the tag-check-failure bits, and the transition into kernel-mode should detect the async tag-check-failure and dispatch an error appropriately.
4. DMA - typically multiple devices on the system have DMA access to various areas of physical memory, and in the cases of complex devices such as GPUs or hardware accelerators, this includes dynamically mapping parts of normal user space or kernel space memory.

   This can pose multiple problems - any code that sets up device mappings is already critical to security, but this is also potentially of use to an attacker in constructing powerful primitives (after the "first invalid access").
5. DMA from non-MTE enabled cores on the system - we've already seen in-the-wild attackers start to use coprocessor vulnerabilities to [bypass kernel mitigations](https://googleprojectzero.blogspot.com/2022/06/curious-case-carrier-app.html), and if those coprocessors have a lower level of general software mitigations in place we can expect to see this continue.

   This alone isn't a reason not to use MTE in kernels - it's just something that we should bear in mind, especially when considering the security implications of moving additional code to coprocessors.

Additionally, there are problems that limit coverage (due to current implementation details in the linux kernel):

6. The kcmp syscall is problematic for confidentiality of kernel pointers, as it allows user-space to compare two struct file\* pointers for equality. Other system calls have similar implementation details that allow user-space to leak information about equality of kernel pointers ([fuse\_lock\_owner\_id](https://elixir.bootlin.com/linux/latest/source/fs/fuse/file.c#L377)).
7. Similarly to the above issue, several kernel data structures use pointers as keys, which has also been used to leak information about kernel pointers to user-space. (See [here](https://googleprojectzero.blogspot.com/2021/10/how-simple-linux-kernel-memory.html), search for epoll\_fdinfo).

   This is an issue for user-space use of MTE as well, especially in the context of eg. a browser renderer process, but highlighting here that there are known instances of this pattern in the linux kernel that have already been used publicly.

8. TYPESAFE\_BY\_RCU regions require/allow use-after-free access by design, so allocations in these regions could not currently be protected by memory-tagging. (See
   [this thread](https://lore.kernel.org/linux-mm/CACT4Y%2BZHoQ5ZPfsvaiQMXrrTxv9-LgP%2Bv_o5Ah2gFBwqQjv-%2Bg%40mail.gmail.com/) for some discussion).
9. In addition to skipping specific tag-check-failures (as per 3 in the list above), it may also be currently possible for an attacker to disable kasan using a single memory write. This would also be a single point of failure that would need to be avoided.

### [1] A hard mitigation that does not provide deterministic protection, but which can be universally bypassed by the attacker "winning" a probabilistic condition, in the case of MTE (with 4 tag bits available, likely with one value reserved) this would probably imply a 1/15 chance of success.

Posted by

[Google Project Zero](https://www.blogger.com/profile/08975904405228580347 "author profile")

at
[9:30 AM](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-3-kernel.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4838136820032157985&postID=12846...