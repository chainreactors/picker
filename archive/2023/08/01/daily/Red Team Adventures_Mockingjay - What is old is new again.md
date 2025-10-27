---
title: Mockingjay - What is old is new again
url: https://riccardoancarani.github.io/2023-07-31-mockingjay-what-is-old-is-new-again/
source: Red Team Adventures
date: 2023-08-01
fetch_date: 2025-10-06T16:59:33.683545
---

# Mockingjay - What is old is new again

Toggle navigation

[Riccardo Ancarani - Red Team Adventures](https://riccardoancarani.github.io/)

* [About Me](/aboutme)
* [Medium](https://medium.com/%40riccardo.ancarani94)

[![](/img/hack.ico)](https://riccardoancarani.github.io/)

# Mockingjay - What is old is new again

## Riding the hype train to see if we can get something useful out of it

Posted on July 31, 2023

# Mockingjay - What is old is new again

There has been quite a lot of rumor recently around the release of a piece of research that discuss a new (?) process injection technique that evades EDRs (what does that even mean?). For reference, these are the blog post I am referring to:

* [New Mockingjay process injection technique evades EDR detection](https://www.bleepingcomputer.com/news/security/new-mockingjay-process-injection-technique-evades-edr-detection/)
* [Process Mockingjay: Echoing RWX In Userland To Achieve Code Execution](https://www.securityjoes.com/post/process-mockingjay-echoing-rwx-in-userland-to-achieve-code-execution)

As consultants specialised in purple and red teaming, we get asked to analyse specific pieces of threat intelligence to achieve the following:

* Understand the research and determine the impact of the technique
* From a red team perspective, understand if there are aspect of the technique that present an advancement in the tradecraft that is worth incorporating in our internal arsenal

Without further ado, let’s get stuck in!

## Understanding the technique

The core of the research is based off the idea that it is possible to DLLs with specific characteristics that make them “vulnerable”. What do the authors exactly mean by that? Put simply, DLLs are just PE files, that - exactly like EXEs - have a number of sections.
Each section can have different permission, specifically, a combination of Read, Write or Execute.
The authors of the post focused on DLLs that happen to have one or more sections with Read, Write and Execute permissions (RWX).
If you ever dealt with parsing a PE file, you will recall that usually RWX permission on a section is quite unusual and in the malware analysis world this is often associated with the usage of packers.
There are - of course - multiple instances of DLLs that have such characteristics but are totally legitimate, and some of them are even signed by Microsoft. The authors of the research found that the msys-2.0.dll DLL have a section with approximately 16kB with RWX permissions.

So, why is this useful and relevant?

Recent advancements on the EDR world allowed these defensive software to gain more and more insights on the memory operations that processes perform. These advancements were necessary to combat process injection, one of the most common defense evasion techniques that is employed by red teamers (us lol) and actual threat actors. From a technical perspective, these advancements can be summarised in these three points:

* More aggressive and robust memory scanners - [CobaltStrike - Can I have your signature](https://www.cobaltstrike.com/blog/cobalt-strike-and-yara-can-i-have-your-signature/)
* Insights on memory operations using Threat Intelligence ETW
* Insights on the callstack when an API call is made - [Upping the Ante: Detecting In-Memory Threats with Kernel Call Stacks](https://www.elastic.co/security-labs/upping-the-ante-detecting-in-memory-threats-with-kernel-call-stacks)

Usually, to perform process injection, you need three actions:

* Allocate memory
* Write a malicious payload into that memory
* Trigger its execution

The existence of RWX “legitimate” RWX sections allow us to skip 2 out of the 3 primitives needed to achieve code execution. Specifically, we won’t need to allocate any new memory as we can simply rely on the one that was previsouly allocated and when it comes to writing, we can avoid using well-known APIs, such as WriteProcess memory and instead copy byte by byte the malicious payload into the RWX memory blob.
Please note that we still need to somehow trigger execution, the authors of the blog post mentioned that it doesn’t need any thread creation - hard to understand exactly what they meant with that.

Now this part of the research is where things get a bit sketchy, as the authors implement various defense evasion techniques but don’t really exploit the power of this technique. In fact, the approach that the researchers suggested was to use the RWX blobs as some sort of trampoline where to store syscall instructions.

What are syscalls instructions? It would take too long to explain here, so please refer to the [Outflank](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/) blog post about the subject.

The authors decided to use direct syscalls, using the Hell’s Gate technique, that are stored in the RWX memory space, to perform userland hook removal. While this is all good and cool, we should consider the following:

* More products are relying less and less on userland hooks to provide protection, as it was found to be a foundamentally flawed concept
* Hook removal is a big IoC on its own, and products that will keep using them will likely start implementing integrity checks on these

In addition, since most of the memory operation are still visible by the kernel using the TiETW provider, userland hooks are not the only mechanism that will come into play when it comes to process injection detection.

## Let’s Steal Some TTPs

In general I liked the idea of piggybacking an existing RWX blob to do evil stuff, however, I think there is much more potential that the PoC that was shown. My plan was to find other DLLs with similar traits that will hopefully have a section big enough to store the entire cobalt strike stageless payload, and as we will see later on, even more…

The first thing was to find as many DLLs as possible that satisfed what I was looking for, to achieve this, I used Yara with the following rule:

```
import "pe"

rule RWX_Search
{
	condition:

		for any i in (0..pe.number_of_sections - 1): (
			(pe.sections[i].characteristics & pe.SECTION_MEM_READ) and
			(pe.sections[i].characteristics & pe.SECTION_MEM_EXECUTE) and
			(pe.sections[i].characteristics & pe.SECTION_MEM_WRITE) and pe.sections[i].virtual_size > 200KB )
}
```

Note that the Yara rule above was adapted from Bill Demirkapi’s [blog post](https://billdemirkapi.me/sharing-is-caring-abusing-shared-sections-for-code-injection/). You can also adjust the `virtual_size` parameter to be greater or equal to the size of the target shellcode.

Running it with `yara.exe pe-hunter.yar -r C:\` revealed a few interesting entries, including a very weird python310.dll that was dropped by PyInstaller in its temporary cache. Analysis of the DLL revealed that it was packed using UPX, and therefore had a section marked as RWX. The idea of finding packed DLLs was first introduced by namazso in 2018.

To perform the attack, we could use the following code:

```
let python_dll_name = "python310.dll\0";

let shellcode = include_bytes!("beacon.bin");

// decrypt the shellcode

unsafe {
    let h_base = LoadLibraryA(python_dll_name.as_ptr() as _);

    let position = (h_base as u64 + 0x1000 as u64) as LPVOID;
    std::ptr::copy_nonoverlapping(shellcode.as_ptr(), position as *mut u8, shellcode.len());

    drop(shellcode);

    let ep: extern "system" fn(LPVOID) -> BOOL = { std::mem::transmute(position) };

    ep(null_mut());
}
```

We can see that the code simply calls LoadLibrary and then copies the shellcode to a hardcoded offset starting from the base address of the python DLL. The injection is done using function pointers but can be achieved using callbacks, fibers or whatever you’re fancy.

This all works pretty well, however, given that we have plenty of spare space in the RWX blob, why not taking advantage of it?

When injecting complex C2 frameworks, we have to take into account the fact that we likely have a reflective loader. The reflective loader, as outlin...