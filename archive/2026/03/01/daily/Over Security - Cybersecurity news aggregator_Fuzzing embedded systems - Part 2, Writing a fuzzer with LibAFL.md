---
title: Fuzzing embedded systems - Part 2, Writing a fuzzer with LibAFL
url: https://blog.sparrrgh.me/fuzzing/embedded/2025/01/26/fuzzing-embedded-systems-2.html
source: Over Security - Cybersecurity news aggregator
date: 2026-03-01
fetch_date: 2026-03-02T04:07:02.506644
---

# Fuzzing embedded systems - Part 2, Writing a fuzzer with LibAFL

[Sparrrgh's blog](/)

[ ]

[About](/about/)

[About](/about/)

# Fuzzing embedded systems - Part 2, Writing a fuzzer with LibAFL

Jan 26, 2025

## Intro

In the previous post[1](#fn:1) we explored how I chose an embedded device to attack, how to extract its firmware and how to choose a target component to fuzz.

We explored why I chose to research CGI binaries and what they are and how they interact with Linux briefly.

Today we will delve into automated vulnerability research through fuzzing. How to write a fuzzer and how to triage vulnerabilities.

The vulnerability described affects the firmware *DSL-3788\_fw\_revA1\_1.01R1B036\_EU\_EN* , it has been fixed and MITRE assigned the following id to track it ***CVE-2024-57440***.

## Fuzzing

Fuzz testing (better known as fuzzing) is a dynamic application security testing technique where input is generated (or mutated), is fed to the program and finally feedback is observed for interesting behaviors.
Information about the running program is usually collected through instrumentation.

This definition is purposefully vague to comprehend a variety of different targets and techniques, but exposes the concepts which I find to be fundamental for fuzzing.

During the years fuzzers and all the tooling around them was built to trigger crashes from programs written using languages which manage memory manually (e.g., C).
This overfitted fuzzers to find memory corruption vulnerabilities, given common feedback loops like edge coverage.

This limitations are being worked on with new techniques like differential fuzzing and different feedback loops like the violation of previously decided invariants[2](#fn:2).

So, why use fuzzing? To find vulnerabilities faster (or try to) and with less effort than manual vulnerability research.

![GIF showing a meme with happy Pedro Pascal with "Fuzzing" written on his head, looking at angry Nicholas Cage with "Manual VR" written on his head](/assets/img/fuzz_vr.gif)

## LibAFL

Fuzzers are mostly built to do the same stuff, with very little differences or approaches. It can be useful then to have a library that collects the most important parts of a fuzzer while still allowing for customization for different targets and use cases.
LibAFL is just that, a library supporting a variety of different techniques and platforms and with great performance as a bonus (thanks Rust!).

### LibAFL and MIPS

Ok, so it’s time to build our fuzzer and get free 0days right?
LibAFL supports different platforms and architectures. We checked and MIPS is supported, right? ***Right?***

Yeah, LibAFL **did not** support MIPS when I started this project, and I didn’t bother to check before buying the router.
This meant I either could change target or delve into MIPS and Qemu internals to add support…

So, after a few days (and some pain) I managed to add support to LibAFL and the patched Qemu[3](#fn:3) it uses. Support for MIPS (with my contribution) was added in the 0.9.0 release[4](#fn:4).

I sadly was not able to make the most important feature work, QASAN. This feature allows for ASAN to be used on compiled binaries that would otherwise not support it.
We will talk later on why ASAN and sanitizers in general are fundamental when fuzzing for memory corruption vulnerabilities.

## Writing the fuzzer

Now that LibAFL supports our target, we have to choose the different approaches which the fuzzer will use to achieve our goal.

The code for the fuzzer is on the Github repository[5](#fn:5).

### Binary-only fuzzing challenges

Since we don’t have access to the source code of the CGIs we must use a **binary-only approach**.

With source code we would usually compile the instrumentation used to test the fuzzer statically. Without this we will rely only on analysis we can perform using the binary, which will lose some precision as well as performance (which is a priority when fuzz-testing). Between all the performance decreases we won’t be able to use *sanitizers*.

**Sanitizers** are compiler instrumentation modules which are used to detect different errors at run-time. The most popular is AddressSanitizer (ASAN) which can be used to detect most memory corruption errors.

Not being able to use such a tool leaves the fuzzer blind to a lot of vulnerabilities which do not cause an immediate crash of the executable. For this reason LibAFL implements **QASAN**[6](#fn:6), which allows the detection of memory errors in a guest Qemu emulator with a binary-only approach bypassing the need for compile-time instrumentation.
As said before, I couldn’t get this part to work for MIPS, which means we will be left with traditional crashes caused by signals like segfault.

Another approach used by a majority of fuzzers is **snapshot fuzzing**. This is an optimization technique which saves a snapshot of the state of the program (e.g., registers, stack, etc) before the target code and restores it after either a corruption happens or the end of the target function to fuzz is reached.

```
flowchart TD
    a[Program starts] --> b[State is saved]
    b[State is saved] --> c[Fuzz target]
    c[Fuzz target] --> d[Crash?]
    d --> f[Save crash file]
    d --> b[State is saved]
```

It only executes the portion of code between the **snapshot** and the end of the **fuzz target**, saving CPU cycles which would otherwise be dedicated to inizialization and destruction code (e.g., to load libraries).

### Feedback and objectives

**Feedback** guides the fuzzer towards interesting code paths. The most common (and easy to implement) feedback is *coverage*, more specifically ***edge-coverage***. This feedback instructs the fuzzer to save an input as interesting if it leads to the execution of a new portion of the executable, leading the fuzzer to autonomously discover the program.

An **objective** is an input which causes a state from the program which is desired. In our case we are only interested in inputs which cause a crash, which are sometimes a symptom of a memory corruption vulnerability.

### Input

We also have to choose what’s the best approach to create inputs for our target.
This can be either:

* **Mutational**
* **Generative**

**Mutational approaches** heavily rely on feedback to mutate a set of initial data (called seed), towards interesting code paths and crashes.
This is particularly effective for loosely structured input, or to test the structure of the input itself. It also does not require any knowledge on the target besides creating the set of inital inputs (valid or not).
This can be as simple as flipping bits of a valid input, to see if it leads to new coverage.

**Generative approaches** are useful for highly-structured input, for which most of the mutations would lead to rejected inputs (i.e., getting less coverage). It requires precise knowledge on the structure of the input, meaning some reverse-engineering must be performed.

As the input I will generate will be structured, the first approach would lead to a lot of the inputs being rejected because they’re not valid, while the second approach wouldn’t take advantage of any feedback and simply generate inputs which fit the grammar.

For this reasons I chose to use **Nautilus**[7](#fn:7) which it’s supported by LibAFL, and uses an hybrid approach taking advantage of both coverage as feedback and a grammar which it’s easy to implement.

### Harness

To create the harness, we need to know exactly how the input is consumed by the program (e.g., console arguments, standard input, sockets) and, if everything fails, how the input is represented in memory to inject it directly.
In my case part of the input is in environment variables which are easy to set, but since they are read right at the start of the program a snapshot could easily break them.

For this reason I decided to inject the input **directly in memory**.

Part of the input is a linked list in the stack (this is how environment variables are stored) while part of it is taken from the file descriptor 0 (sta...