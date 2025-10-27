---
title: Symbolic Triage: Making the Best of a Good Situation
url: https://www.atredis.com/blog/2022/10/29/symbolic-triage-making-the-best-of-a-good-situation
source: Blog - Atredis Partners
date: 2022-11-01
fetch_date: 2025-10-03T21:24:56.932382
---

# Symbolic Triage: Making the Best of a Good Situation

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Symbolic Triage: Making the Best of a Good Situation

Oct 31

Written By [Jordan Whitehead](/blog?author=607868e1c0c84d602cd982b5)

Symbolic Execution can get a bad rap. Generic symbex tools have a hard time proving their worth when confronted with a sufficiently complex target. However, I have found symbolic execution can be very helpful in certain targeted situations. One of those situations is when triaging a large number of crashes coming out of a fuzzer, especially in cases where dealing with a complicated or opaque target. This is the "Good Situation" I have found myself in before, where my fuzzer handed me a large load of crashes that resisted normal minimization and de-duplication. By building a small symbolic debugger I managed a much faster turnaround time from fuzz-case to full understanding.

In this post I want to share my process for writing symbolic execution tooling for triaging crashes, and try to highlight tricks I use to make the tooling effective and flexible. The examples here all use the great [Triton](https://triton-library.github.io) library for our symbolic execution and solving. The examples all use code hosted at: [github.com/atredis-jordan/SymbolicTriagePost](https://github.com/atredis-jordan/SymbolicTriagePost)

> (Oh BTW, we have a course!) Do you reverse engineer and symbolically execute in your workflows, or want to?
>
> Are you using fuzzing today but want to find more opportunities to improve it and find deeper and more interesting bugs?
>
> Can you jam with the console cowboys in cyberspace?
>
> We've developed a 4-day course called "Practical Symbolic Execution for VR and RE" that's tailored towards these exact goals. It’s fun and practical, with lots of demos and labs to practice applying these concepts in creative ways. If that sounds interesting to you, there is more information at the bottom of this post. Hope to see you there!

We will be using a bunch of crashes in *Procmon64.exe* for our examples. Procmon's parsing of PML (Process Monitor Log) files is pretty easy to knock over, and we can quickly get lots of crashes out of a short fuzzing session. It is a large opaque binary with some non-determinism to the crashes, so useful tooling here will help us to speed up our reverse engineering efforts. Note that we weren't exhaustive in trying to find bugs in Procmon; so although these bugs we will talk about here don't appear super useful to an attacker, I won't be opening any untrusted PML files any time soon.

I gathered a bunch of crashes by making a few very small PML files and throwing [Jackalope](https://github.com/googleprojectzero/Jackalope) at the target. After a few hours we had 200ish odd crashes to play with. Many of the crashes were unstable, and only reproduced occasionally.

```
..\Jackalope\Release\fuzzer.exe -iterations_per_round 30 -minimize_samples false -crash_retry 0 -nthreads 32 -in - -resume -out .\out -t 5000 -file_extension PML -instrument_module procmon64.exe -- procmon64.exe /OpenLog @@ /Quiet /Runtime 1 /NoFilter /NoConnect
```

> Fuzzing Procmon's PML paser with Jackalope

## A Simple Debugger

With all this hyping up symbolic execution, our first step is to not use Symbolic Execution! Knowing when to turn to symbolic execution and when just to use emulation or a debugger is a good skill to have. In this case, we are going to write a very simple debugger using the Windows debugging API. This debugger can be used to re-run our crashing inputs, find out how stable they are, see if they all happen in the main thread, gather stack traces, etc.

Also, having a programmatic debugger will be very useful when we start symbolically executing. We will talk about that here in a second, first let's get our debugger off the ground.

> Quick aside. All my code examples here are in python, because I like being able to pop into IPython in my debuggers. I defined a bunch of ctypes structures in the [win\_types.py](https://github.com/atredis-jordan/SymbolicTriagePost/blob/main/win_types.py) file. I recommend having some programmatic way to to generate the types you need. Look into [PDBRipper](https://github.com/horsicq/PDBRipper) or [cvdump](https://github.com/microsoft/microsoft-pdb/blob/master/cvdump/cvdump.exe) as a good place to start.

Okay, so first we want a debugger that can run the process until it crashes and collect the exception information. The basic premise is we start a process as debugged (our [*connect\_debugger* function in triage.py](https://github.com/atredis-jordan/SymbolicTriagePost/blob/main/triage.py#L77)), and then wait on it until we get an unhandled exception. Like so:

```
    handle, main_tid = connect_debugger(cmd)

    log("process", 3, f": -- ")

    event = dbg_wait(handle, None)
    code = event.dwDebugEventCode

    if code == EXIT_PROCESS_DEBUG_EVENT:
        log("crash", 1, f" Closed with no crash")
    elif code == EXCEPTION_DEBUG_EVENT:
        # exception to investigate
        log("crash", 1, f" crashed:")
        er = event.u.Exception.ExceptionRecord
        log("crash", 1, exceptionstr(handle, er, event.dwThreadId))

    else:
        log("process", 1, f" hit unexpected Debug Event ")

    dbg_kill(handle)
```

> A piece of [triage.py's handle\_case](https://github.com/atredis-jordan/SymbolicTriagePost/blob/main/triage.py#L1028), running a single test case

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1325b83b-f8de-419b-b515-2802b291355d/crash.png)

*Running the above code to get the exception information from a crash*

Many of the crashes will not happen every time due to some non-determinism. Running through all our test cases multiple times in our debugger, we can build a picture of which crashes are the most stable, if they stay in the main thread, and what kind of exception is happening.

```
.\crsh\access_violation_0000xxxxxxxxx008_00000xxxxxxxx5AA_1.PML -- 100% (18) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x520 read at 0x5aa
         EXCEPTION_STACK_BUFFER_OVERRUN(0xc0000409) @ 0x83c
.\crsh\access_violation_0000xxxxxxxxx008_00000xxxxxxxx5AA_2.PML -- 100% (34) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x520 read at 0x5aa
.\crsh\access_violation_0000xxxxxxxxx063_00000xxxxxxxx3ED_1.PML -- 100% (34) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x520 read at 0x3ed
...
.\crsh\access_violation_0000xxxxxxxxx3D4_00000xxxxxxxxED1_2.PML -- 52% (23) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x87a read at 0xed1
.\crsh\access_violation_0000xxxxxxxxx234_00000xxxxxxxxED4_3.PML -- 45% (22) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x649 read at 0xa2
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x87a read at 0xed4
.\crsh\access_violation_0000xxxxxxxxx3CA_00000xxxxxxxxED1_1.PML -- 45% (22) -- main thread
         EXCEPTION_ACCESS_VIOLATION(0xc0000005) @ 0x87a read at 0xed1
.\crsh\access_violation_0000xxxxxxxxx5EC_00000xxxxxxxx0A2_1.PML -- 45% (22) -- main thread
         EXCEPTION_ACCE...