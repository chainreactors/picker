---
title: ‘Reflections on Trusting Trust’, but completely by accident this time
url: https://secret.club/2024/10/21/unnecessarily-exhaustice-rca.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:24.881999
---

# ‘Reflections on Trusting Trust’, but completely by accident this time

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# 'Reflections on Trusting Trust', but completely by accident this time

![main authors image](/assets/author_img/duk.jpg)  [duk](/author/duk)

 Oct 21, 2024

---

> Compilers are complicated. You just won’t believe how vastly, hugely, mind-bogglingly complicated they are. I mean, you may think C build systems are painful, but they’re just peanuts to compilers.
>
> - Douglas Adams, probably

This blog post assumes you have some knowledge of LLVM internals - I’ll try to fill in some of the lesser-known gaps but there are likely some other, better resources out there for learning about that.

I have only one [other post](https://secret.club/2021/04/09/std-clamp.html) on this blog at the time of writing. It describes a somewhat boring, easily-explained missed optimization in one of the core components of LLVM with some actual, real-world implications. This blog post, although it follows roughly the same format, is the exact opposite:

# [An exhaustive analysis of a miscompilation that impacted basically no-one](#an-exhaustive-analysis-of-a-miscompilation-that-impacted-basically-no-one)

## [Introduction & disclaimer](#introduction--disclaimer)

Is *all* the complexity in modern-day optimizing compilers warranted? Probably not.

Take [LLVM](https://llvm.org/), for example - once you get to the backends it might as well be 200 compilers in a trench coat. Picture this: it’s two in the morning and you’ve figured out exactly what went wrong after several weeks of debugging. You’re on your fifth coffee and have an idea for a target-independent patch. There’s just one small problem - you’d have to reach out to other overworked people from other companies, convince them that giving you some of their extremely limited time is worthwhile, wait for a bit, address any and all potential concerns, wait a bit more, and Lord help you if something breaks on a piece of hardware you don’t have access to.

Alternatively, you could just add another if statement, ping a coworker to fast-track code review since the change is restricted to your little `llvm/lib/Target` sandbox, and be on your merry way. Repeat a few times a day and now your Modular™ framework ends up with a bunch of duplicated, convoluted, unnecessarily target-dependent code generation logic.

Yes, quite a bit of the complexity is the result of [Conway’s Law](https://en.wikipedia.org/wiki/Conway%27s_law) and the inevitable bitrot of a decades-old codebase. That being said, there is still an incredible amount of inherent messiness when targeting dozens of architectures in a (mostly) correct and performant way. Nobody is ever going to have a full, deep view of the entire system at once, and even if they did it would be out of date by the next `Revert "[NFC] ..."` commit.

## [Every computer on the planet is a compiler fuzzer](#every-computer-on-the-planet-is-a-compiler-fuzzer)

We tame the combinatorial explosion of potentially-buggy interactions through the kind of extraordinarily exhaustive testing only possible in the information age. Even a simple “Hello, world!” is a reliability test of the compiler, the linker, the runtime, the operating system, the terminal, any rendering middleware (which might **also** be running LLVM to compile shaders!), display drivers, the underlying hardware itself, and all software used in the process of building any of that. As such, you can be reasonably confident that release versions of production compilers, *when using the flags and target architectures everyone else does*, will *probably* not break anything. That’s not to say stuff doesn’t get through the cracks - [yarpgen](https://github.com/intel/yarpgen), [alive2](https://github.com/AliveToolkit/alive2), [Csmith](https://github.com/csmith-project/csmith), and similar tools would not have a long list of trophies otherwise - but those tools are also now just a part of this testing process too.

A direct corollary of this is that bugs are regularly introduced in mainline branches, even by seasoned developers, and fixed whenever this exhaustive testing happens ~~and people actually care about fixing them~~. Anyway, take a look at this commit:

<https://github.com/llvm/llvm-project/commit/c6e01627acf8591830ee1d211cff4d5388095f3d>

It is extremely important to emphasize: This committer knows what they’re doing! They’re good at their job! It’s just the nature of compilers and `llvm-project/main`; shit happens. The miscompile was found and fixed in roughly a week, and if this is all there was to it then we wouldn’t be here.

## [The funniest compiler bug](#the-funniest-compiler-bug)

Here’s a bug.

<https://issues.chromium.org/issues/336399264>

Credits to [@dougall](https://mastodon.social/%40dougall/112488200751670463).

As a summary, here’s what happened.

1. Compile clang with the commit right before the fix above - This is generally called a “stage 1” build
2. *Bootstrap clang with the newly-compiled clang* - This is a “stage 2” build
3. Build the repro script attached *with ASAN and fuzzing harnesses on* when targeting AArch64
4. Get a miscompile in the output.

Due to the Clang version being known-buggy and swapped out pretty much immediately, the stage 2 miscompile was noticed by pretty much nobody except people employed at companies that pay them to look at this stuff. This is the system working as intended! Unfortunately, I am a complete sucker for bugs like this but do not get paid to look at them. I wanted to figure out what went wrong here because it’s such a great example of the emergent complexity that comes with modern-day compilers.

*hear that? it’s the sound of my free time going down the drain for the next week. fwsssssssshhhhhhhhhhhhhhhhhhhhhhhh*

There’s some good news: this is a bug in the loop vectorizer, meaning our stage2 compiler is *probably* not going to be broken in the impossible-to-debug some-target-specific-register-allocation-thing-is-cooked-somehow way. That may not always be the case (especially if `undef`/`poison` are involved) but it seems like we’re going to get a nice, deterministic problem in the mostly-sorta-target-independent part of the pipeline.

`undef` and `poison` are, roughly, LLVM’s way of modelling the set of all possible values and a deferred form of undefined behavior. I will not be explaining how this is formalized or what the implications for compiler transforms are. [It gets weird](https://github.com/llvm/llvm-project/pull/90295#discussion_r1603903222). Please do not ask.

Unfortunately, there is also some bad news: this is a bug in the loop vectorizer. The vectorizer is probably the single most per-target-tuned pass in the entirety of the generic optimization pipeline. That means we’re probably going to have some trouble convincing the compiler to deliberately emit the wrong instruction sequence on platforms without cross-compiling. Cross-compiling is not fun. I do not want to cross-compile, so I would like to try to coax the compiler into emitting the right (wrong?) code on X86 if possible.

*Foreshadowing is a narrative device in which-*

## [Reproducing the bug with somewhat-helpful debugging information](#reproducing-the-bug-with-somewhat-helpful-debugging-information)

For now, it’s important to just reproduce the original bug with the aforementioned stage1/stage2 executables in exact the same build environment. While we’re at it, let’s tack on some useful debugging options that will hopefully help us down the line:

1. `-print-after=loop-vectorize` lets us print out a textual dump of the IR whenever the loop vectorizer pass has finished
2. `-ir-dump-directory` lets us redirect this output to a folder somewhere This is going to generate a *lot* of text files. That’s okay, though, because computers are really fast and it doesn’t impact the build times in any meaningful way if we use an SSD.

Simply run this easy-to-remember set of CMake incantations for the stage1 and stage2 builds:

```
LLVM_DIR=$(pwd)

cmake -S llvm -B bui...