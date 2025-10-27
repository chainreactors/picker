---
title: MTE As Implemented, Part 1: Implementation Testing
url: https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html
source: Project Zero
date: 2023-08-03
fetch_date: 2025-10-04T12:01:24.448635
---

# MTE As Implemented, Part 1: Implementation Testing

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Wednesday, August 2, 2023

### MTE As Implemented, Part 1: Implementation Testing

By Mark Brand, Project Zero

## Background

In 2018, in the [v8.5a version](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-a-profile-architecture-2018-developments-armv85a) of the ARM architecture, ARM proposed a hardware implementation of tagged memory, referred to as MTE (Memory Tagging Extensions).

Through mid-2022 and early 2023, Project Zero had access to pre-production hardware implementing this instruction set extension to evaluate the security properties of the implementation. In particular, we're interested in whether it's possible to use this instruction set extension to implement effective security mitigations, or whether its use is limited to debugging/fault detection purposes.

As of the v8.5a specification, MTE can operate in two distinct modes, which are switched between on a per-thread basis. The first mode is sync-MTE, where tag-check failure on a memory access will cause the instruction performing the access to deliver a fault at retirement. The second mode is async-MTE, where tag-check failure does not directly (at the architectural level) cause a fault. Instead, tag-check failure will cause the setting of a per-core flag, which can then be polled from the kernel context to detect when an invalid access has occurred.

This blog post documents the tests that we have performed so far, and the conclusions that we've drawn from them, [together with the code necessary to repeat these tests](https://github.com/googleprojectzero/p0tools/tree/master/MTETest). This testing was intended to explore both the details of the hardware implementation of MTE, and the current state of the software support for MTE in the Linux kernel. All of the testing is based on manually implemented tagging in statically-linked standalone binaries, so it should be easy to reproduce these results on any compatible hardware.

## Terminology

When designing and implementing security features, it's important to be conscious of the specific protection goal. In order to provide clarity in the rest of this post, we'll define some specific terminology that we use when talking about this:

1. Mitigation - A mitigation is something that reduces real exploitability of a vulnerability or class of vulnerability. The expectation is that attackers can (and eventually will) find their way around it. Examples would be DEP, ASLR, CFI.

1. "Soft" Mitigation - We consider a mitigation to be "soft" if the expectation is that an attacker pays a one-time cost in order to bypass the mitigation. Typically this would be a per-target cost, for example developing a ROP chain to bypass DEP, which can usually be largely re-used between different exploits for the same target software.
2. "Hard" Mitigation - We consider a mitigation to be "hard" if the expectation is that an attacker cannot develop a bypass technique which is reusable between different vulnerabilities (without, e.g. incorporating an additional vulnerability). An example would be ASLR, which is typically bypassed either by the use of a separate information leak vulnerability, or by developing an information leak primitive using the same vulnerability.

Note that the context can have an impact on the "hardness" of a mitigation -
        if a codebase is particularly rich in code-patterns which allow the construction of

information leaks, it's quite possible that an attacker can develop a reliable, reusable

technique for turning various memory corruption primitives into an information leak

within that codebase.

2. Solution - a solution is something that eliminates exploitability of a vulnerability or class of vulnerability. The expectation is that the only way for an attacker to bypass a solution would be an unintended implementation weakness in the solution.

For example (based purely on a theoretical implementation of memory tagging):

 - Randomly-allocating tags to heap allocations cannot be considered a solution for any class of heap-related memory corruption, since this provides at best probabilistic protection.

 - Allocating odd and even tags to adjacent heap allocations might theoretically be able to provide a solution for linear heap-buffer overflows.

## Hardware Implementation

The main hardware implementation question we had was, does a speculative side-channel exist that would allow leaking whether or not a tag-check has succeeded, without needing to architecturally execute the tag-check?

It is expected that Spectre-type speculative execution side-channels will still allow an attacker to leak pointer values from memory, indirectly leaking the tags. Here we consider whether the implementation introduces additional speculative side-channels that would allow an attacker to more efficiently leak tag-check success/failure.

TL; DR; In our testing we did not identify an additional[1](#h.d43f6ia2nolp) speculative side-channel that would allow such an attack to be performed.

### 1. Does MTE block Spectre? (NO)

The only way that MTE could prevent exploitation of Spectre-type weaknesses would be to have speculative execution stall the pipeline until the tag-check completes[2](#h.8v9sdwwdtqt). This might sound desirable ("prevent exploitation of Spectre-type weaknesses") but it's not - this would create a much stronger side-channel to allow an attacker to create an oracle for tag-check success, weakening the overall security properties of the MTE implementation.

This is easy to test. If we can still leak data out of speculative execution using Spectre when the pointer used for the speculative access has an incorrect tag, then this is not the case.

We wrote a [small patch](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/0001-Add-MTE-spectre-test.patch) to the [safeside](https://github.com/google/safeside) demo spectre\_v1\_pht\_sa that demonstrates this:

|  |
| --- |
| mte\_device:/data/local/tmp $ ./spectre\_v1\_pht\_sa\_mte  Leaking the string: 1t's a s3kr3t!!!  Done!  Checking that we would crash during architectural access:  Segmentation fault |

### 2. Does tag-check success/failure have a measurable impact on the speculation window length? (Probably NOT)

There is a deeper question that we'd like to understand: is the length of speculative execution after a memory access influenced by whether the tag-check for that access succeeds or fails? If this was the case, then we might be able to build a more complex speculative side-channel that we could use in a similar way.

In order to measure this, we need to force a mis-speculation, and then perform a read access to memory for which a tag-check would either succeed or fail, and then we need to use a speculative side-channel to measure how many further instructions were successfully speculatively executed. We wrote and tested a self-contained harness to measure this, which can be found in speculation\_window.c

This harness works by generating code for a test function with a variable number of no-op instructions at runtime, and then repeatedly executing this test function in a loop to train the branch-predictor before finally triggering mis-speculation. The test function is as follows:

|  |
| --- |
| ldr  x0, [x0]         ; this load is slow (\*x0 is uncached)    cbnz x0, speculation: ; this branch is always taken during warmup    ret    speculation:    ldr  x1, [x1]         ; this load is fast (\*x1 is cached)                          ; the tag-check success or fail will happen on                          ; this access, but during warmup the tag-check                          ; will always be a success.      orr  x2, x2, x1       ; this is a no-op (as x1 is always 0) but it    ... n times ...       ; maintains a data dependency between the    orr  x2, x2, x1       ; loads (and the no-ops), hopefully preventi...