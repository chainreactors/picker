---
title: Harnessing the eBPF Verifier
url: https://blog.trailofbits.com/2023/01/19/ebpf-verifier-harness/
source: Trail of Bits Blog
date: 2023-01-20
fetch_date: 2025-10-04T04:22:06.189677
---

# Harnessing the eBPF Verifier

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Harnessing the eBPF Verifier

Laura Bauman

January 19, 2023

[ebpf](/categories/ebpf/), [internship-projects](/categories/internship-projects/)

During my internship at Trail of Bits, I prototyped a harness that improves the testability of the [eBPF](https://ebpf.io) verifier, simplifying the testing of eBPF programs. [My eBPF harness](https://github.com/trailofbits/ebpf-verifier) runs in user space, independently of any locally running kernel, and thus opens the door to testing of eBPF programs across different kernel versions.

eBPF enables users to instrument a running system by loading small programs into the operating system kernel. As a safety measure, the kernel “verifies” eBPF programs at load time and rejects any that it deems unsafe. However, using eBPF is a CI / CD nightmare, because there’s no way to know whether a given eBPF program will successfully load and pass verification without testing it on a running kernel.

My harness aims to eliminate that nightmare by executing the eBPF verifier outside of the running kernel. To use the harness, a developer tweaks my `libbpf`-based sample programs ([hello.bpf.c](https://github.com/trailofbits/ebpf-verifier/blob/master/samples/hello.bpf.c) and [hello\_loader.c](https://github.com/trailofbits/ebpf-verifier/blob/master/samples/hello_loader.c)) to tailor them to the eBPF program being tested. The version of libbpf provided by my harness links against a “kernel library” that implements the actual `bpf` syscall, which provides isolation from the running kernel. The harness works well with kernel version 5.18, but it is still a proof of concept; enabling support for other kernel versions and additional eBPF program features will require a significant amount of work.

## With great power comes great responsibility

eBPF is an increasingly powerful technology that is [used](https://ebpf.io/applications) to increase system observability, implement security policies, and perform advanced networking operations. For example, the [osquery](https://osquery.io/) open-source endpoint agent uses eBPF for security monitoring, to enable organizations to watch process and file events happening across their fleets.

The ability to inject eBPF code into the running kernel seems like either a revelation or a huge risk to the kernel’s security, integrity, and dependability. But how on earth is it safe to load user-provided code into the kernel and execute it there? The answer to this question is twofold. First, eBPF isn’t “normal” code, and it doesn’t execute in the same way as normal code. Second, eBPF code is algorithmically “verified” to be safe to execute.

### eBPF isn’t normal code

eBPF (extended Berkeley Packet Filter) is an overloaded term that refers to both a specialized bytecode representation of programs and the in-kernel VM that runs those bytecode programs. eBPF is an extension of classic BPF, which has fewer features than eBPF (e.g., two registers instead of ten), uses an in-kernel interpreter instead of a just-in-time compiler, and focuses only on network packet filtering.

User applications can load eBPF code into kernel space and run it there without modifying the kernel’s source code or loading kernel modules. Loaded eBPF code is checked by the kernel’s eBPF verifier, which tries to prove that the code will terminate without crashing.

[![](/img/wpdump/165bfd224a95d12964270d38f4f6693d.png)](/img/wpdump/165bfd224a95d12964270d38f4f6693d.png)

[A diagram of the eBPF system](https://ebpf.io/static/loader-dff8db7daed55496f43076808c62be8f.png)

The picture above shows the general interaction between user space and kernel space, which occurs through the [`bpf` syscall](https://man7.org/linux/man-pages/man2/bpf.2.html). The eBPF program is represented in eBPF bytecode, which can be obtained through the Clang back end. The interaction begins when a user space process executes the first in the series of `bpf` syscalls used to load an eBPF program into the kernel. The kernel then runs the verifier, which enforces constraints that ensure the eBPF program is valid (more on that later). If the verifier approves the program, the verifier will finalize the process of loading it into the kernel, and it will run when it is triggered. The program will then serve as a socket filter, listening on a socket and forwarding only information that passes the filter to user space.

### Verifying eBPF

The key to eBPF safety is the eBPF verifier, which limits the set of valid eBPF programs to those that it can guarantee will not harm the kernel or cause other issues. This means that eBPF is, by design, not [Turing-complete](https://en.wikipedia.org/wiki/Turing_completeness).

Over time, the set of eBPF programs accepted by the verifier has expanded, though the testability of that set of programs has not. The following quote from the “[BPF Design Q&A” section](https://www.kernel.org/doc/html/latest/bpf/bpf_design_QA.html#q-what-are-the-verifier-limits) of the Linux kernel documentation is telling:

> The [eBPF] verifier is steadily getting ‘smarter.’ The limits are being removed. **The only way to know that the program is going to be accepted by the verifier is to try to load it**. The BPF development process guarantees that the future kernel versions will accept all BPF programs that were accepted by the earlier versions.

This “development process” relies on a limited set of regression tests that can be run through the `[kselftest](https://docs.kernel.org/dev-tools/kselftest.html)` system. These tests require that the version of the source match that of the running kernel and are aimed at kernel developers; the barrier to entry for others seeking to run or modify such tests is high. As eBPF is increasingly relied upon for critical observability and security infrastructure, it is concerning that the Linux kernel eBPF verifier is a single point of failure that is fundamentally difficult to test.

## Trust but verify

The main problem facing eBPF is portability—that is, it is notoriously difficult to write an eBPF program that will pass the verifier and work correctly on all kernel versions (or, heck, on even one). The introduction of [BPF Compile Once-Run Everywhere (CO-RE)](https://nakryiko.com/posts/bpf-portability-and-co-re/.) has significantly improved eBPF program portability, though issues still remain. BPF CO-RE relies on the eBPF loader library ([libbpf](https://github.com/libbpf/libbpf)), the Clang compiler, and the [eBPF Type Format](https://facebookmicrosites.github.io/bpf/blog/2018/11/14/btf-enhancement.html) (BTF) information in the kernel. In short, BPF CO-RE means that an eBPF program can be compiled on one Linux kernel version (e.g., by Clang), modified to match the configuration of another kernel version, and loaded into a kernel of that version (through `libbpf`) as though the eBPF bytecode had been compiled for it.

However, different kernel versions have different verifier limits and support different eBPF opcodes. This makes it difficult (from an engineering perspective) to tell whether a particular eBPF program will run on a kernel version other than the one it has been tested on. Moreover, different configurations of the same kernel version will also have different verifier behavior, so determining a program’s portability requires testing the program on all desired configurations. This is not practical when building CI infrastructure or trying to ship a production piece of software.

Projects that use eBPF take a variety of approaches to overcoming its portability challenges. For projects that primarily focus on tracing syscalls (like [osquery](https://github.com/osquery/osquery) and [opensnoop](https://github.com/brendangregg/perf-tools/blob/master/opensnoop)), BPF CO-RE is less necessary, since syscall arguments are stable between kernel versions. In those cases, th...